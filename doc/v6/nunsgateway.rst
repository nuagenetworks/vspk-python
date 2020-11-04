.. _nunsgateway:

nunsgateway
===========================================

.. class:: nunsgateway.NUNSGateway(bambou.nurest_object.NUMetaRESTObject,):

Network Services Gateways are a policy enforcement end-points responsible for the delivery of networking services. NSG access ports/VLANs may be attached to existing host or bridge VPorts.


Attributes
----------


- ``mac_address``: MAC Address of the NSG

- ``aar_application_release_date``: Release Date of the AAR Application

- ``aar_application_version``: The AAR Application Version

- ``nat_traversal_enabled``: This attribute is deprecated in version 4.0.

- ``tcpmss_enabled``: Boolean flag to indicate whether MSS on TCP is enabled or not

- ``tcp_maximum_segment_size``: Maximum Segment Size for TCP(min = 576, max = 7812).

- ``zfb_match_attribute``: The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

- ``zfb_match_value``: The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

- ``bios_release_date``: Release Date of the NSG BiOS

- ``bios_version``: NSG BIOS Version

- ``sku``: The part number of the NSG

- ``tpm_status``: TPM Status of the NSG based on the information received by the device during bootstrapping or upgrade.

- ``tpm_version``: TPM (Trusted Platform Module) version as reported by the NSG.

- ``cpu_core_allocation``: Current CPU allocation for network accelerated gateways.  Displays total number of cores and those isolated.

- ``cpu_type``: The NSG Processor Type as reported during bootstrapping.

- ``vsdaar_application_version``: Version of the latest imported Application Signatures.

- ``nsg_version``: The NSG Version (software) as reported during bootstrapping or following an upgrade.

- ``ssh_service``: Indicates if SSH Service is enabled/disabled on a NSG. The value configured for this attribute is used only when instanceSSHOverride is allowed on the associated Gateway Template.

- ``uuid``: The Redhat UUID of the NSG

- ``name`` (**Mandatory**): Name of the Gateway

- ``family``: The NSG Family type.

- ``last_configuration_reload_timestamp``: Time stamp of the last known configuration update of the NSG.  This timestamp gets updated when a bootstrap is successful or when a configuration reload request triggered by VSD is successful.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``datapath_id``: Identifier of the Gateway, based on the systemId

- ``gateway_config_raw_version``: Release version of NSG, which is used to determine the feature capabilties of NSG.

- ``gateway_config_version``: Interpreted version of NSG, which is used to determine the feature capabilities of NSG.

- ``gateway_connected``: Indicates status of this gateway

- ``redundancy_group_id``: The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

- ``template_id`` (**Mandatory**): The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

- ``pending``: Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

- ``serial_number``: The NSG's serial number

- ``derived_ssh_service_state``: Indicates the SSH Service state on a NSG. This value is derived based on the SSHService configuration on the NSG and the associated Gateway Template.

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``personality``: Personality of the Gateway - NSG, cannot be changed after creation.

- ``cert_validity_days``: The number of days for which the NSG's certificate is valid.

- ``description``: A description of the Gateway

- ``network_acceleration``: Attribute that enables or disables Network Acceleration (DPDK) on the NSGateway instance.  Changing the value of this field will cause the device to restart at the next configuration reload.

- ``threat_prevention_enabled``: Indicates if Threat Prevention capability enabled on NSG.

- ``libraries``: Transient representation of the same property on NSGInfo.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``inherited_ssh_service_state``: Indicates the SSH Service state which is configured on the associated template instance.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_id``: The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object

- ``configuration_reload_state``: Status resulting from a manually triggered configuration reload operation on an NSG.  This value only reflects the state for a manual action requested by the operator, not the automatic periodic configuration reload triggered by the NSG itself.

- ``configuration_status``: NSG Configuration status represents the NSG update state following a query by the NSG to get the latest version of the infraconfig.json file.  This status will be updated following a Bootstrap request or a Configuration Reload.  Success means that the NSG was able to apply the changes included in the latest infraconfig.json file.  A Failure response will be returned if the NSG was unable to apply the changes; this is normally accompanied with a rollback of the NSG to the previous configuration.

- ``configure_load_balancing``: Describes whether the load balancing behavior used for Fc's in inherited from enterprise or disabled. 

- ``control_traffic_cos_value``: CoS Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 7

- ``control_traffic_dscp_value``: DSCP Value for Self Generated Traffic (Control Traffic). Min is 0 and Max is 63

- ``bootstrap_id``: The bootstrap details associated with this NSGateway. NOTE: This is a read only property, it can only be set during creation of an NSG.

- ``bootstrap_status``: The bootstrap status of this NSGateway. NOTE: This is a read only property.

- ``operation_mode``: Operation mode of NSGateway

- ``operation_status``: Operation Status of NSGateway

- ``creation_date``: Time stamp when this object was created.

- ``product_name``: NSG Product Name as reported during bootstrapping.

- ``associated_gateway_security_id``: Read only ID of the associated gateway security object.

- ``associated_gateway_security_profile_id``: Read only ID of the associated gateway security profile object

- ``associated_nsg_info_id``: Read only ID of the associated NSG info object

- ``associated_nsg_upgrade_profile_id``: The UUID of the NSG Upgrade Profile associated to this NSG instance.

- ``associated_overlay_management_profile_id``: The ID of the associated Overlay Management Profile

- ``huge_page_setting``: The size and number of huge pages for an NSG that is running in network accelerated mode.  Hugepage values states the portion of memory reserved for network accelerated services.

- ``functions``: List of supported functions. This is only relevant for NSG-UBR and will be set to UBR by default in case an NSG-UBR is created. For a regular NSG, this will be set to null.

- ``tunnel_shaping``: Indicates if the UBR will perform tunnel shaping to the NSG when a tunnel shaper is associated to the NSG.

- ``auto_disc_gateway_id``: The Auto Discovered Gateway associated with this Gateway Instance

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``syslog_level``: The minimal logging level of the messages the NSG will be reporting to the external syslog server that has been configured on the Infrastructure Gateway Profile.

- ``system_id``: Identifier of the Gateway, cannot be modified after creation




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupatch.NUPatch<nupatch>`                                                                                                                                  ``patchs`` 
:ref:`nugatewaysecurity.NUGatewaySecurity<nugatewaysecurity>`                                                                                                    ``gateway_securities`` 
:ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`                                                                                                                   ``patnat_pools`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuthreatpreventioninfo.NUThreatPreventionInfo<nuthreatpreventioninfo>`                                                                                     ``threat_prevention_infos`` 
:ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`                                                                                                             ``wireless_ports`` 
:ref:`nuvirtualuplink.NUVirtualUplink<nuvirtualuplink>`                                                                                                          ``virtual_uplinks`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuunderlaytest.NUUnderlayTest<nuunderlaytest>`                                                                                                             ``underlay_tests`` 
:ref:`nuvnf.NUVNF<nuvnf>`                                                                                                                                        ``vnfs`` 
:ref:`nuinfrastructureconfig.NUInfrastructureConfig<nuinfrastructureconfig>`                                                                                     ``infrastructure_configs`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nulocation.NULocation<nulocation>`                                                                                                                         ``locations`` 
:ref:`nucommand.NUCommand<nucommand>`                                                                                                                            ``commands`` 
:ref:`nubootstrap.NUBootstrap<nubootstrap>`                                                                                                                      ``bootstraps`` 
:ref:`nubootstrapactivation.NUBootstrapActivation<nubootstrapactivation>`                                                                                        ``bootstrap_activations`` 
:ref:`nunsportinfo.NUNSPortInfo<nunsportinfo>`                                                                                                                   ``ns_port_infos`` 
:ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`                                                                                                 ``uplink_connections`` 
:ref:`nunsgatewaymonitor.NUNSGatewayMonitor<nunsgatewaymonitor>`                                                                                                 ``ns_gateway_monitors`` 
:ref:`nunsgatewaysummary.NUNSGatewaySummary<nunsgatewaysummary>`                                                                                                 ``ns_gateway_summaries`` 
:ref:`nunsginfo.NUNSGInfo<nunsginfo>`                                                                                                                            ``nsg_infos`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
:ref:`nusubnet.NUSubnet<nusubnet>`                                                                                                                               ``subnets`` 
:ref:`nusupplementalinfraconfig.NUSupplementalInfraConfig<nusupplementalinfraconfig>`                                                                            ``supplemental_infra_configs`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsredundantgatewaygroup.NUNSRedundantGatewayGroup<nunsredundantgatewaygroup>`

- :ref:`nuducgroup.NUDUCGroup<nuducgroup>`

- :ref:`nume.NUMe<nume>`

- :ref:`nupolicyobjectgroup.NUPolicyObjectGroup<nupolicyobjectgroup>`

- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

