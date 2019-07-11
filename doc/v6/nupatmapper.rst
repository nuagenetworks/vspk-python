.. _nupatmapper:

nupatmapper
===========================================

.. class:: nupatmapper.NUPATMapper(bambou.nurest_object.NUMetaRESTObject,):

PAT Mapper is a construct which will be associated with 1-N FIP Domains


Attributes
----------


- ``name`` (**Mandatory**): None

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: None

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`                                                                                  ``shared_network_resources`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

