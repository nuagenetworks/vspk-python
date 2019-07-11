Quickstart
==========


Installation
------------

The easiest way to install ``vspk`` is to use ``pip``:

.. code-block:: none

    pip install vspk


Creating a session
------------------

.. code-block:: python

    # we'll use the 4.0 API, but to use the 3.2 API, replace v4_0 by v3_2
    from vspk import v4_0 as vspk

    # enable logging. it makes debugging much easier
    import logging
    from vspk.utils import set_log_level
    set_log_level(logging.DEBUG, logging.Streamhandler())

    # create a new session for csproot
    session = vspk.NUVSDSession(
        username='csproot',
        password='csproot',
        enterprise='csp',
        api_url="https://my-vsd:8443")

    # start the session.
    try:
        session.start()
    # we'll see later how to properly handle vspk exceptions.
    # for now, just catch everything.
    except:
        logging.error('Failed to start the session')


If the session started successfully, ``session.user`` should be an instance of
:ref:`vspk.v4_0.nume.NUMe<nume>` corresponding to ``csproot``. Let's wrap this
in a function that we will reuse through this document:

.. code-block:: python

    from vspk import v4_0 as vspk

    def setup_logging():
        import logging
        from vspk.utils import set_log_level
        set_log_level(logging.DEBUG, logging.Streamhandler())

    def start_csproot_session():
        session = vspk.NUVSDSession(
            username='csproot',
            password='csproot',
            enterprise='csp',
            api_url="https://my-vsd:8443")
        try:
            session.start()
        except:
            logging.error('Failed to start the session')
        return session.user


CRUD operations
---------------

Each vspk class correspond to a VSD entity. All the classes provide the same
API to perform CRUD operations:

- a ``create_child()`` method for creating children
- a ``save()`` method to update the current entity
- a ``delete()`` method to delete the current entity
- a ``get()`` and a ``fetch()`` method to retrive the current entity
- multiple *fetchers* to retrieve children entities.



Creating objects
----------------

Here is an example of where we create an enterprise and a domain under
``csproot``:

.. code-block:: python

    # we assume we have the setup_logging() and start_csproot_session() methods
    # showed in the previous example

    from vspk import v4_0 as vspk
    setup_logging()
    csproot = start_csproot_session()

    # Create a new enterprise object. The only mandatory parameter is the name,
    # so we give it directly to the contructor
    new_enterprise = vspk.NUEnterprise(name="new-corp")

    # Create the enterprise on VSD.
    csproot.create_child(new_enterprise)

    # Create a new domain object.
    new_domain = vspk.NUDomain()
    # The attributes can also be set on the object directly
    new_domain.name = "new-dom"

    # Create the domain on VSD.
    new_enterprise.create_child(new_domain)


Updating objects
----------------

Let's change the name of the domain we just created. All we need to do to update an entity is change its attributes, and call ``save()``:

.. code-block:: python

    new_domain.name = "better-named-domain"
    new_domain.save()

That's it!

Deleting objects
----------------

Deleting objects dead simple: just call ``delete()``:

.. code-block:: python

    new_domain.delete()

Fetching objects
----------------

Fetching the current entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fetching the current entity is pretty simple:

.. code-block:: python

    new_enterprise.get()

There are two reasons why we would need to fetch the current entity:

- to get an up-to-date representation of the entity, in case it has been
  updated on the VSD by someone else
- to retrieve an entity from its UUID For example, if we know the UUID of a
  subnet on VSD, we could do:

.. code-block:: python

    my_subnet = NUSubnet(id="123e4567-e89b-12d3-a456-426655440000")
    my_subnet.get()

    # Now, the attributes of the object are populated with data from VSD. We
    # can for instance print the subnet's name:
    logging.info("Fetched subnet %s!" % my_subnet.name)


Fetching child entities
^^^^^^^^^^^^^^^^^^^^^^^

Each child entity has a corresponding *fetcher*. Calling the fetcher will
populate it. For instance, assuming we have vports under the
subnet we just fetched, we could retrieve them like this:

.. code-block:: python

    # fetch the vports
    my_subnet.vports.get()
    for vport in my_subnet.vports:
        logging.info("vport: %s" % vport.name)

        # fetch the host interfaces under the current vport
        vport.host_interfaces.get()
        for interface in vport.host_interfaces:
            logging.info("host ip: %s" % interface.ip_address)
            

Since ``get`` returns itself, we can make this shorter:

.. code-block:: python

    for vport in my_subnet.vports.get():
        logging.info("vport: %s" % vport.name)

        for interface in vport.host_interfaces.get():
            logging.info("host ip: %s" % interface.ip_address)

Filtering
^^^^^^^^^

By default, fetchers fetch all the child entities, which can lead to huge
responses. Fortunately, the API offers filters on some attributes, and vspk
provides a way to use them:

.. code-block:: python

    # get all the bridge vports in the current domain:
    for vport in domain.vports.get(filter='type is "BRIDGE"'):
        # do something


Assigning entities
------------------

Some entities do not follow the parent/children relationship. For example,
users are not children of groups, they `belong` to one or multiple groups.
Similarly, policy groups are `assigned` to vports. To assign entities to
another entity, we use the ``assign()`` method:

.. code-block:: python

        entity.assign(assigned_entities_list, assigned_entities_class)


This method takes two arguments:

- the list of entities to be assigned
- the class of the assigned entities

For example, to add a user "bob" to a group "engineers":

.. code-block:: python

    # Get the "engineers" group.
    #
    # get_first() is a convenient shortcut for get()[0], that returns None if
    # no entity was fetched.
    engineers = enterprise.groups.get_first(filter="name is 'engineers'")
    
    # Get the user we want to add to the group
    bob = enterprise.users.get_first(filter="userName is 'bob'")

    # Fetch the users already assigned to this group
    engineers.users.get()

    engineers.assign(
        # We assign the list of *all* the users, not only "bob"
        [bob] + engineers.users,
        # We need to specify the class of the entities we are assigning
        vspk.NUUser
    )


To un-assign resources, we just re-assign a list without these resources. To
remove the user "bob" we just added, we could to this:

.. code-block:: python

    # Fetch the assigned users
    assigned_users = engineers.users.get()

    # Make  new list of users without "bob"
    new_assigned_users = [user if user.user_name != "bob" for user in assigned_users]

    # Assign this new list
    engineers.assign(new_assigned_users, vspk.NUUser)

To un-assign all the entities, assign an empty list:

.. code-block:: python

    engineers.assign([], vspk.NUUser)


Error handling
--------------

All of the previous methods raise a ``bambou.exception.BambouHTTPError`` when
they fail, which contains some interesting information, like the HTTP status
code. It can be useful to catch these exceptions:

.. code-block:: python

    from bambou.exceptions import BambouHTTPError

    # We assume we have a parent trying to create a child.

    try:
        parent_entity.create_child(child_entity)
    except BambouHTTPError as exc:
        response = exc.connection.response
        if response.status_code == 409:
            # the entity probably already exists, so we just ignore this error:
            pass
        else:
            logging.Error("Failed to create entity: %s" % exc.message())
            # re-raise the exception
            raise
