.. _nunsgateway:

nunsgateway
===========================================

.. class:: nunsgateway.NUNSGateway(bambou.nurest_object.NUMetaRESTObject,):

Represents Network Service Gateway object.


Attributes
----------


- ``nat_traversal_enabled``: Boolean value that states if the NSG instance is in a network that is behind a NAT device and will use NAT Traversal procedures to talk to other NSGs and the Internet.

- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``datapath_id``: Identifier of the Gateway, based on the systemId

- ``redundancy_group_id``: The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

- ``template_id`` (**Mandatory**): The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

- ``pending``: Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``personality``: Personality of the Gateway - NSG, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_id``: The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

- ``configuration_reload_state``: 

- ``configuration_status``: 

- ``bootstrap_id``: The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG

- ``bootstrap_status``: The bootstrap status of this NSGateway. NOTE: this is a read only property

- ``associated_gateway_security_id``: Readonly Id of the associated gateway security object

- ``associated_gateway_security_profile_id``: Readonly Id of the associated gateway security profile object

- ``auto_disc_gateway_id``: The Auto Discovered Gateway associated with this Gateway Instance

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the Gateway, cannot be modified after creation




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`                                                                                     ``infrastructure_configs`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nulocation.NULocation<nulocation>`                                                                                                                         ``locations`` 
:ref:`nubootstrap.NUBootstrap<nubootstrap>`                                                                                                                      ``bootstraps`` 
:ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`                                                                                        ``bootstrap_activations`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

