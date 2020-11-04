.. _nupatmapper:

nupatmapper
===========================================

.. class:: nupatmapper.NUPATMapper(bambou.nurest_object.NUMetaRESTObject,):

PAT Mapper is a construct which will be associated with 1-N FIP Domains


Attributes
----------


- ``name`` (**Mandatory**): None

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: None

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

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

