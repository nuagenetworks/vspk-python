.. _nuvcentervrsconfig:

nuvcentervrsconfig
===========================================

.. class:: nuvcentervrsconfig.NUVCenterVRSConfig(bambou.nurest_object.NUMetaRESTObject,):

Default VRS Configuration parameters


Attributes
----------


- ``arp_reply``: Whether ARP Reply is enabled/disabled

- ``vrs_configuration_time_limit``: The maximum wait time limit in minutes to get VRS configured at cluster level

- ``v_require_nuage_metadata``: Whether split-activation or not (Openstack/CloudStack)

- ``manage_vrs_availability``: When this is set to true, the vCenter Integration Node will be responsible for marking a VRS Agent as available in the EAM framework. If VCIN fails to mark a VRS Agent as unavailable, vCenter will not migrate VMs to the host running the VRS Agent and will not allow VMs to be powered on that host.

- ``last_updated_by``: ID of the user who last updated the object.

- ``data_dns1``: Data DNS 1

- ``data_dns2``: Data DNS 2

- ``data_gateway``: Data Gateway

- ``data_network_portgroup``: Data Network Port Group

- ``datapath_sync_timeout``: Datapath Sync Timeout

- ``secondary_data_uplink_dhcp_enabled``: Enable DHCP on the secondary data uplink.

- ``secondary_data_uplink_enabled``: Enable secondary data uplink

- ``secondary_data_uplink_interface``: Interface to use for the secondary data uplink. This interface can be a normal interface or a VLAN on an existing interface. Please read the VMware integration guide for more details.

- ``secondary_data_uplink_mtu``: Secondary data uplink MTU

- ``secondary_data_uplink_primary_controller``: Secondary data uplink primary controller IP

- ``secondary_data_uplink_secondary_controller``: Secondary data uplink secondary controller IP

- ``secondary_data_uplink_underlay_id``: Secondary data uplink underlay ID

- ``secondary_data_uplink_vdf_control_vlan``: The VLAN for the control communication with VSC on the secondary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

- ``secondary_nuage_controller``: IP address of the secondary Controller (VSC)

- ``memory_size_in_gb``: VRS memory size in GB

- ``remote_syslog_server_ip``: Remote syslog server IP

- ``remote_syslog_server_port``: Remote syslog server port

- ``remote_syslog_server_type``: Remote syslog server type (UDP/TCP)

- ``generic_split_activation``: Whether split-activation is needed from VRO

- ``separate_data_network``: Whether Data will use the management network or not

- ``personality``: VCenter VRS Personality

- ``destination_mirror_port``: Extra Vnic to mirror access port

- ``metadata_server_ip``: Metadata Server IP

- ``metadata_server_listen_port``: Metadata Server Listen Port

- ``metadata_server_port``: Metadata Server Port

- ``metadata_service_enabled``: Metadata Service Enabled

- ``network_uplink_interface``: Network Uplink Interface to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_gateway``: Network Uplink Interface Gateway

- ``network_uplink_interface_ip``: Ip Address to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_netmask``: Network Uplink Interface Netmask

- ``revertive_controller_enabled``: Enable revertive controller behaviour. If this is enabled, OVS will make its primary VSC as its master VSC once it is back up.

- ``revertive_timer``: A timer in seconds indicating after how long OVS should retry to connect to the primary VSC as its master after a failure.

- ``nfs_log_server``: IP address of NFS server to send the VRS log

- ``nfs_mount_path``: Location to mount the NFS server

- ``mgmt_dns1``: DNS server 1

- ``mgmt_dns2``: DNS server 2

- ``mgmt_gateway``: Gateway for the IP address

- ``mgmt_network_portgroup``: Management Network Port group

- ``dhcp_relay_server``: To provide IP address of the interface from which you will connect to the DHCP relay server

- ``mirror_network_portgroup``: Mirror Network Port Group Name

- ``disable_gro_on_datapath``: Disable GRO on datapath

- ``disable_lro_on_datapath``: Disable LRO on datapath

- ``site_id``: Site ID field for object profiles to support VSD Geo-redundancy

- ``allow_data_dhcp``: Whether to get the Data IP for the VRS VM from DHCP or statically

- ``allow_mgmt_dhcp``: Whether to get the management IP for the VRS VM from DHCP or statically

- ``flow_eviction_threshold``: Flow Eviction Threshold

- ``vm_network_portgroup``: VM Network Port Group Name

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enable_vrs_resource_reservation``: Enable resource reservation on the VRS. When this is enabled, all memory and 100% of CPU resources allocated to the VRS will be reserved.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``configured_metrics_push_interval``: Configured VRS metrics push interval on VCIN

- ``portgroup_metadata``: Port Group Meta data

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

- ``upgrade_package_password``: Upgrade Package Password

- ``upgrade_package_url``: Upgrade Package URL

- ``upgrade_package_username``: Upgrade Package User Name

- ``upgrade_script_time_limit``: The maximum time limit in seconds before the vrs script based upgrade is marked as TIMED_OUT

- ``cpu_count``: Number of VRS vCPU's

- ``primary_data_uplink_underlay_id``: Primary data uplink underlay ID

- ``primary_data_uplink_vdf_control_vlan``: The VLAN for the control communication with VSC on the primary datapath interface, when VDF is enabled. This VLAN can not be used as a subnet VLAN in the VSD configuration.

- ``primary_nuage_controller``: IP address of the primary Controller (VSC)

- ``vrs_password``: VRS password to be used by toolbox to communicate with VRS

- ``vrs_user_name``: VRS user name to be used by toolbox to communicate with VRS

- ``static_route``: static route to be configured in the VRS

- ``static_route_gateway``: Gateway for the static route given above

- ``static_route_netmask``: Nova region name

- ``ntp_server1``: IP of the NTP server 1

- ``ntp_server2``: IP of the NTP server 1

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

- ``ovf_url``: The url for the ovf

- ``avrs_enabled``: AVRS enabled

- ``avrs_profile``: AVRS profile

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`                                                                                                    ``vrs_address_ranges`` 
:ref:`nuvrsredeploymentpolicy.NUVRSRedeploymentpolicy<nuvrsredeploymentpolicy>`                                                                                  ``vrs_redeploymentpolicies`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

