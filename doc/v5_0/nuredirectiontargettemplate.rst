.. _nuredirectiontargettemplate:

nuredirectiontargettemplate
===========================================

.. class:: nuredirectiontargettemplate.NURedirectionTargetTemplate(bambou.nurest_object.NUMetaRESTObject,):

Template for a vporttag. It can be created only at the template level and available for all instances.


Attributes
----------


- ``name`` (**Mandatory**): Name of this redirection target template

- ``last_updated_by``: ID of the user who last updated the object.

- ``redundancy_enabled``: Allow/Disallow redundant appliances and VIP

- ``description``: Description of this redirection target template

- ``end_point_type`` (**Mandatory**): VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE and NSG_VNF.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``trigger_type``: Trigger type, could be NONE/GARP - THIS IS READONLY

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

