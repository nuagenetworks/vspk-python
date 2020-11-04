.. _nuvcenter:

nuvcenter
===========================================

.. class:: nuvcenter.NUVCenter(bambou.nurest_object.NUMetaRESTObject,):

Represents a VCenter.


Attributes
----------


- ``eam_extension_name``: Name of the Nugae EAM Plugin registered with VCenter for the current instance of VCIN

- ``arp_reply``: Whether ARP Reply is enabled/disabled

- ``vrs_configuration_time_limit``: The maximum wait time limit in minutes to get VRS configured at cluster level

- ``v_require_nuage_metadata``: Whether split-activation or not (Openstack/CloudStack)

- ``name`` (**Mandatory**): Name of the VCenter

- ``manage_vrs_availability``: When this is set to true, the vCenter Integration Node will be responsible for marking a VRS Agent as available in the EAM framework. Until a VRS Agent has been marked as available, vCenter will not migrate VMs to the host running the VRS Agent and will not allow VMs to be powered on that host.

- ``password`` (**Mandatory**): Password for the VCenter user

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``data_dns1``: Data DNS 1

- ``data_dns2``: Data DNS 2

- ``data_gateway``: Data Gateway

- ``data_network_portgroup``: Data Network Port Group

- ``datapath_sync_timeout``: Datapath Sync Timeout

- ``secondary_data_uplink_dhcp_enabled``: Enable DHCP on the secondary data uplink.

- ``secondary_data_uplink_enabled`` (**Mandatory**): Enable secondary data uplink

- ``secondary_data_uplink_interface``: Interface to use for the secondary data uplink. This interface can be a normal interface or a VLAN on an existing interface. Please read the VMware integration guide for more details.

- ``secondary_data_uplink_mtu``: Secondary data uplink MTU

- ``secondary_data_uplink_primary_controller``: Secondary data uplink primary controller IP

- ``secondary_data_uplink_secondary_controller``: Secondary data uplink secondary controller IP

- ``secondary_data_uplink_underlay_id``: Secondary data uplink underlay ID

- ``secondary_data_uplink_vdf_control_vlan``: The VLAN for the control communication with VSC on the secondary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

- ``secondary_nuage_controller``: IP address of the secondary Controller (VSC)

- ``memory_size_in_gb``: Memory in Gigabytes

- ``remote_syslog_server_ip``: Remote syslog server IP

- ``remote_syslog_server_port``: Remote syslog server port

- ``remote_syslog_server_type``: Remote syslog server type (UDP/TCP)

- ``generic_split_activation``: Whether split-activation is needed from VRO

- ``separate_data_network``: Whether Data will use the management network or not

- ``personality``: The personality of the VRS Agent, supported values when deploying through the vCenter Integration Node: VRS, VDF.

- ``description``: Description of the VCenter

- ``destination_mirror_port``: Extra Vnic to mirror access port

- ``metadata_server_ip``: Metadata Server IP

- ``metadata_server_listen_port``: Metadata Server Listen Port

- ``metadata_server_port``: Metadata Server Port

- ``metadata_service_enabled``: Metadata Service Enabled

- ``network_uplink_interface``: Network Uplink Interface to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_gateway``: Network Uplink Interface Gateway

- ``network_uplink_interface_ip``: Ip Address to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_netmask``: Network Uplink Interface Netmask

- ``revertive_controller_enabled`` (**Mandatory**): Enable revertive controller behaviour. If this is enabled, OVS will make its primary VSC as its master VSC once it is back up.

- ``revertive_timer`` (**Mandatory**): A timer in seconds indicating after how long OVS should retry to connect to the primary VSC as its master after a failure.

- ``nfs_log_server``: IP address of NFS server to send the VRS log

- ``nfs_mount_path``: Location to mount the NFS server

- ``mgmt_dns1``: DNS server 1

- ``mgmt_dns2``: DNS server 2

- ``mgmt_gateway``: Gateway for the IP address

- ``mgmt_network_portgroup``: Management Network Port group

- ``dhcp_relay_server``: To provide IP address of the interface from which you will connect to the DHCP relay server

- ``mirror_network_portgroup``: Mirror Port Group Name

- ``disable_gro_on_datapath``: Disable GRO on datapath

- ``disable_lro_on_datapath``: Disable LRO on datapath

- ``disable_network_discovery``: disable Network Discovery (true - dont fetch portgroups from vcenter, false - fetch portgroups from vcenter)

- ``site_id``: Site ID field for object profiles to support VSD Geo-redundancy

- ``old_agency_name``: Old Agency Name

- ``allow_data_dhcp``: Whether to get the Data IP for the VRS VM from DHCP or statically

- ``allow_mgmt_dhcp``: Whether to get the management IP for the VRS VM from DHCP or statically

- ``flow_eviction_threshold``: Flow Eviction Threshold

- ``vm_network_portgroup``: VM Network Port Group Name

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enable_vrs_resource_reservation``: Enable resource reservation on the VRS. When this is enabled, all memory and 100% of CPU resources allocated to the VRS will be reserved.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``configured_metrics_push_interval``: Configured VRS metrics push interval on VCIN

- ``connection_status``: VCenter connection status.

- ``portgroup_metadata``: Port Group Meta data

- ``host_level_management``: Flag to say if host level management is enabled

- ``nova_client_version``: Nova client Version 

- ``nova_identity_url_version``: Keystone identity version to use for the Nova metadata configuration on the VRS

- ``nova_metadata_service_auth_url``: Nova metadata service auth url

- ``nova_metadata_service_endpoint``: Nova metadata service endpoint

- ``nova_metadata_service_password``: Nova metadata service password

- ``nova_metadata_service_tenant``: Nova metadata service tenant

- ``nova_metadata_service_username``: Nova metadata service username

- ``nova_metadata_shared_secret``: Nova metadata shared secret

- ``nova_os_keystone_username``: Keystone username used by nova

- ``nova_project_domain_name``: Name of the project that the Nova service uses, can be determined from the nova.conf on the OpenStack controller

- ``nova_project_name``: Name of the default Nova project (example: services)

- ``nova_region_name``: Nova region name

- ``nova_user_domain_name``: Name of the user domain used by the Nova service, can be determined from the nova.conf on the OpenStack controller

- ``ip_address`` (**Mandatory**): IP Address of the VCenter

- ``upgrade_package_password``: Upgrade package password used for script based upgrades

- ``upgrade_package_url``: Upgrade package URLused for script based upgrades

- ``upgrade_package_username``: Upgrade package username used for script based upgrades

- ``upgrade_script_time_limit``: Time limit for the patch based upgrade functionality. If the upgrade process of a VRS has not returned a success or failure status within this time limit, the status will be changed to TIMEOUT. Specified in seconds

- ``cpu_count``: The number of vCPUs that will be assigned to the VRS.

- ``creation_date``: Time stamp when this object was created.

- ``primary_data_uplink_underlay_id``: Primary data uplink underlay ID

- ``primary_data_uplink_vdf_control_vlan``: The VLAN for the control communication with VSC on the primary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

- ``primary_nuage_controller``: IP address of the primary Controller (VSC)

- ``vrs_config_id``: The ID of the template that this Port was created from

- ``vrs_password``: VRS password to be used by toolbox to communicate with VRS

- ``vrs_user_name``: VRS user name to be used by toolbox to communicate with VRS

- ``user_name`` (**Mandatory**): User name of the VCenter

- ``static_route``: static route to be configured in the VRS

- ``static_route_gateway``: Gateway for the static route given above

- ``static_route_netmask``: Nova region name

- ``ntp_server1``: IP of the NTP server 1

- ``ntp_server2``: IP of the NTP server 1

- ``http_port``: Http proxy port for VCenter

- ``https_port``: Https proxy port of the VCenter

- ``mtu``: Maximum Transmission Unit for eth2 interface

- ``multi_vmssupport``: Whether Multi VM is to be used or not

- ``multicast_receive_interface``: Multicast Receive Interface

- ``multicast_receive_interface_ip``: IP address for eth3 interface

- ``multicast_receive_interface_netmask``: Multicast Interface netmask

- ``multicast_receive_range``: Allowed Range to receive the Multicast traffic from

- ``multicast_send_interface``: Multicast Send Interface

- ``multicast_send_interface_ip``: IP address for eth3 interface

- ``multicast_send_interface_netmask``: Multicast Interface netmask

- ``multicast_source_portgroup``: Multi Cast Source Port Group Name

- ``customized_script_url``: To provide a URL to install a custom app on VRS

- ``auto_resolve_frequency``: Frequency at which VCenter issues are to be resolved

- ``ovf_url``: The url for the ovf

- ``avrs_enabled``: When enabled, the AVRS functionality will be enabled on the VRS during bootstrapping. This feature requires special AVRS licenses and specific configuration which is described in the product documentation.

- ``avrs_profile``: The AVRS configuration profile that needs to be set up. This profile will configure the AVRS services so that it can support a certain type of performance.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`                                                                                              ``vcenter_data_centers`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`                                                                                                    ``vrs_address_ranges`` 
:ref:`nuvrsredeploymentpolicy.NUVRSRedeploymentpolicy<nuvrsredeploymentpolicy>`                                                                                  ``vrs_redeploymentpolicies`` 
:ref:`nuautodiscovereddatacenter.NUAutodiscovereddatacenter<nuautodiscovereddatacenter>`                                                                         ``autodiscovereddatacenters`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

