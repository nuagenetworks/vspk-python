.. _nusapegressqosprofile:

nusapegressqosprofile
===========================================

.. class:: nusapegressqosprofile.NUSAPEgressQoSProfile(bambou.nurest_object.NUMetaRESTObject,):

7x50 SAP Egress QoS profile


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the Egress QoS Profile entity.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A detailed description of the Egress QoS Profile entity.

- ``blob_text``: Data definitions for pre-defined sets of attributes defined by blobType.

- ``blob_type``: Content type for blob text.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``assoc_entity_type``: Type of the entity to which the Profile belongs to.

- ``customer_id``: The customer ID given to parent enterprise. This is used by Netconf/Config manager.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




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


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

