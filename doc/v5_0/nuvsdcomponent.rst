.. _nuvsdcomponent:

nuvsdcomponent
===========================================

.. class:: nuvsdcomponent.NUVSDComponent(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for components of VSD system.


Attributes
----------


- ``name``: Identifies the entity with a name.

- ``management_ip``: An optional management IP to log into this component.

- ``address``: An optional IP to access this component.

- ``description``: Description of the entity.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location``: Identifies the entity to be associated with a location.

- ``product_version``: Product version supported by this entity.

- ``status``: Current status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Type of the component.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsd.NUVSD<nuvsd>`

