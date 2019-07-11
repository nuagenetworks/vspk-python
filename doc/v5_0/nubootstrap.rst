.. _nubootstrap:

nubootstrap
===========================================

.. class:: nubootstrap.NUBootstrap(bambou.nurest_object.NUMetaRESTObject,):

Gateway bootstrap details.


Attributes
----------


- ``zfb_info``: Base64 Encoded JSON String of NSG ZFB Attribute Value Pairs

- ``zfb_match_attribute``: Attribute to auto match on

- ``zfb_match_value``: Attribute value to auto match on

- ``last_updated_by``: ID of the user who last updated the object.

- ``installer_id``: The Installer ID

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_entity_type``: Object type of the associated entity.

- ``status``: Bootstrap status.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

