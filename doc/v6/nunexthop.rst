.. _nunexthop:

nunexthop
===========================================

.. class:: nunexthop.NUNextHop(bambou.nurest_object.NUMetaRESTObject,):

Next-hop address used to leak the routes from source domain onto the destination domain.


Attributes
----------


- ``ip_type``: The IP Type of this Nexthop, possible values are IPV4, IPV6 or DUALSTACK.

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_distinguisher``: The next-hop's route distinguisher. A unique 8 byte long. If not provided one will be generated.

- ``ip`` (**Mandatory**): This is the /32 or /128 next-hop IP address. Currently we support only IPv4 address family.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Next hop type: IP only supported for service chaining




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

