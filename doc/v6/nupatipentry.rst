.. _nupatipentry:

nupatipentry
===========================================

.. class:: nupatipentry.NUPATIPEntry(bambou.nurest_object.NUMetaRESTObject,):

PATIPEntry is auto-generated (southbound case, decentralized for containers) or through REST (for centralized case, user can choose a IP).


Attributes
----------


- ``pat_centralized``: This flag will determine whether we can expect anchor point or not.

- ``ip_address``: Its own IPAddress.

- ``ip_type``: IPv4 or IPv6 (only IPv4 supported in R1.0)

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``associated_domain_id``: The ID of the associated l3-domain.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``hypervisor_id``: The ID of the PatMapper entity to which this domain is associated to.






Parents
--------


- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

