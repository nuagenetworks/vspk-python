.. _nunsgateway:

nunsgateway
===========================================

.. class:: nunsgateway.NUNSGateway(bambou.nurest_object.NUMetaRESTObject,):

Represents a Network Service Gateway.


Attributes
----------


- ``mac_address``: MAC Address of the NSG

- ``nat_traversal_enabled``: This attribute is deprecated in version 4.0.

- ``tcpmss_enabled``: Boolean flag to indicate whether MSS on TCP is enabled or not

- ``tcp_maximum_segment_size``: Maximum Segment Size for TCP(min = 576, max = 7812).

- ``sku``: The part number of the NSG

- ``tpm_status``: TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

- ``cpu_type``: The NSG Processor Type

- ``nsg_version``: The NSG Version

- ``ssh_service``: Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

- ``uuid``: The Redhat UUID of the NSG

- ``name`` (**Mandatory**): Name of the Gateway

- ``family``: The NSG Type

- ``last_configuration_reload_timestamp``: Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

- ``last_updated_by``: ID of the user who last updated the object.

- ``datapath_id``: Identifier of the Gateway, based on the systemId

- ``redundancy_group_id``: The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

- ``template_id`` (**Mandatory**): The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

- ``pending``: Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

- ``serial_number``: The NSG's serial number

- ``derived_ssh_service_state``: Indicates the SSH Service state on a NSG. This value is derived based on the SSHService configuration on the NSG and the associated Gateway Template.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``personality``: Personality of the Gateway - NSG, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``libraries``: Transient representation of the same property on NSGInfo.

- ``inherited_ssh_service_state``: Indicates the SSH Service state which is configured on the associated template instance.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_id``: The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

- ``configuration_reload_state``: None

- ``configuration_status``: None

- ``bootstrap_id``: The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG

- ``bootstrap_status``: The bootstrap status of this NSGateway. NOTE: this is a read only property

- ``operation_mode``: Operation mode of NSGateway

- ``operation_status``: Operation Status of NSGateway

- ``associated_gateway_security_id``: Readonly Id of the associated gateway security object

- ``associated_gateway_security_profile_id``: Readonly Id of the associated gateway security profile object

- ``associated_nsg_info_id``: Readonly Id of the associated nsg info object

- ``auto_disc_gateway_id``: The Auto Discovered Gateway associated with this Gateway Instance

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the Gateway, cannot be modified after creation




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`                                                                                                    ``gateway_securities`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`                                                                                     ``infrastructure_configs`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nulocation.NULocation<nulocation>`                                                                                                                         ``locations`` 
:ref:`numonitorscope.NUMonitorscope<numonitorscope>`                                                                                                             ``monitorscopes`` 
:ref:`nubootstrap.NUBootstrap<nubootstrap>`                                                                                                                      ``bootstraps`` 
:ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`                                                                                        ``bootstrap_activations`` 
:ref:`nunsginfo.NUNSGInfo<nunsginfo>`                                                                                                                            ``nsg_infos`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nume.NUMe<nume>`

- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

