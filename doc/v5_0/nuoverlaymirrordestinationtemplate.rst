.. _nuoverlaymirrordestinationtemplate:

nuoverlaymirrordestinationtemplate
===========================================

.. class:: nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name`` (**Mandatory**): Name of this overlay mirror destination template

- ``last_updated_by``: ID of the user who last updated the object.

- ``redundancy_enabled``: Allow/Disallow redundant appliances and VIP

- ``description``: Description of this overlay mirror destination template

- ``end_point_type`` (**Mandatory**): VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a overlay mirror destination. Possible value is VIRTUAL_WIRE.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``trigger_type``: Trigger type, could be NONE/GARP - THIS IS READONLY

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


- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

