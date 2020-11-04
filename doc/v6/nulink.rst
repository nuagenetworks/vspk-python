.. _nulink:

nulink
===========================================

.. class:: nulink.NULink(bambou.nurest_object.NUMetaRESTObject,):

Border router links provide a way to interconnect VNS domains in the wide-area to datacenter domains. Service chaining links allow domain leaking in order to simplify and enhance capabilities of doing service chaining and traffic steering for NFV and service-provider-grade VPN services.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``acceptance_criteria``: A route filtering criteria enum. Defaults to ALL.

- ``read_only``: This is set to true if a link has been created in the opposite direction

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``associated_destination_id``: This is the  ID of the domain receiving the routes from the source. This can only be set for links of type OVERLAY_ADDRESS_TRANSLATION.

- ``associated_destination_name``: None

- ``associated_destination_type``: Type of the entity type for the source

- ``associated_source_id``: The ID of the domain receiving the routes from another domain

- ``associated_source_name``: None

- ``associated_source_type``: This is the source object type for the associatedSourceID

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: This is used to distinguish between different type of links: hub and spoke, IP address, VNS border router links.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudemarcationservice.NUDemarcationService<nudemarcationservice>`                                                                                           ``demarcation_services`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunexthop.NUNextHop<nunexthop>`                                                                                                                            ``next_hops`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicystatement.NUPolicyStatement<nupolicystatement>`                                                                                                    ``policy_statements`` 
:ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`                                                                                                                      ``csnat_pools`` 
:ref:`nupsnatpool.NUPSNATPool<nupsnatpool>`                                                                                                                      ``psnat_pools`` 
:ref:`nuoverlayaddresspool.NUOverlayAddressPool<nuoverlayaddresspool>`                                                                                           ``overlay_address_pools`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nudomain.NUDomain<nudomain>`

