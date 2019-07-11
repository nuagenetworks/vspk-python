.. _nusapingressqosprofile:

nusapingressqosprofile
===========================================

.. class:: nusapingressqosprofile.NUSAPIngressQoSProfile(bambou.nurest_object.NUMetaRESTObject,):

7x50 SAP Ingress QoS profile


Attributes
----------


- ``name``: A unique name of the Ingress QoS Profile entity.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A detailed description of the Ingress QoS Profile entity.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``assoc_entity_type``: Type of the entity to which the Profile belongs to.

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


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nunetconfgateway.NUNetconfGateway<nunetconfgateway>`

- :ref:`nugateway.NUGateway<nugateway>`

