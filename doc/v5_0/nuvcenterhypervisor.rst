.. _nuvcenterhypervisor:

nuvcenterhypervisor
===========================================

.. class:: nuvcenterhypervisor.NUVCenterHypervisor(bambou.nurest_object.NUMetaRESTObject,):

Host or Hypervisors.


Attributes
----------


- ``vcenter_ip``: IP Address of the VCenter.

- ``vcenter_password``: Password for VCenter.

- ``vcenter_user``: Username for VCenter.

- ``vrs_configuration_time_limit``: The maximum wait time limit in minutes to get VRS configured at cluster level

- ``vrs_metrics_id``: ID of the VRS metrics object.

- ``vrs_state``: Current state of the VRS VM on the hypervisor

- ``v_require_nuage_metadata``: Whether split-activation or not (Openstack/CloudStack)

- ``name`` (**Mandatory**): Name of the Hypervisor

- ``managed_object_id``: managed Object ID of hypervisor

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_vrs_deployed_date``: Determines the time the vrs vm was last deployed.

- ``data_dns1``: Data DNS 1

- ``data_dns2``: Data DNS 2

- ``data_gateway``: Data Gateway

- ``data_ip_address``: Data IP Address

- ``data_netmask``: Data NetMask

- ``data_network_portgroup`` (**Mandatory**): Data Network Port Group

- ``datapath_sync_timeout``: Datapath Sync Timeout

- ``scope``: Cluster in scope or not in scope.

- ``secondary_nuage_controller``: IP address of the secondary Controller (VSC)

- ``removed_from_vcenter_inventory``: Set to true if the hypervisor is removed from Vcenter inventory datacenter or cluster

- ``generic_split_activation``: Whether split-activation is needed from VRO

- ``separate_data_network``: Whether Data will use the management network or not

- ``deployment_count``: The number of times the vrs was deployed on this hypervisor

- ``personality``: VRS/VRS-G

- ``description`` (**Mandatory**): Description of the Hypervisor

- ``destination_mirror_port``: Extra Vnic to mirror access port

- ``metadata_server_ip``: Metadata Server IP

- ``metadata_server_listen_port``: Metadata Server Listen Port

- ``metadata_server_port``: Metadata Server Port

- ``metadata_service_enabled``: Metadata Service Enabled

- ``network_uplink_interface``: Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_gateway``: Network Uplink Interface Gateway

- ``network_uplink_interface_ip``: Ip Address to support PAT/NAT with no tunnels on VRS-VM

- ``network_uplink_interface_netmask``: Network Uplink Interface Netmask

- ``nfs_log_server``: IP address of NFS server to send the VRS log

- ``nfs_mount_path``: Location to mount the NFS server

- ``mgmt_dns1``: DNS server 1

- ``mgmt_dns2``: DNS server 2

- ``mgmt_gateway``: Gateway for the IP address

- ``mgmt_ip_address``: The Mangement IP address for VRS VM if needed to be given statically

- ``mgmt_netmask``: Netmask of the IP address above

- ``mgmt_network_portgroup`` (**Mandatory**): Management Network Port group

- ``dhcp_relay_server``: To provide IP address of the interface from which you will connect to the DHCP relay server

- ``mirror_network_portgroup``: Mirror Port Group Name

- ``site_id``: Site ID field for object profiles to support VSD Geo-redundancy

- ``allow_data_dhcp``: Whether to get the Data IP for the VRS VM from DHCP or statically

- ``allow_mgmt_dhcp``: Whether to get the management IP for the VRS VM from DHCP or statically

- ``flow_eviction_threshold``: Flow Eviction Threshold

- ``vm_network_portgroup`` (**Mandatory**): VM Network Port Group Name

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``toolbox_deployment_mode``: Flag to specify if VRS is deployed using tool box.

- ``toolbox_group``: Deployment Toolbox Group.

- ``toolbox_ip``: Deployment Toolbox IP.

- ``toolbox_password``: Deployment Toolbox password.

- ``toolbox_user_name``: Deployment Toolbox username.

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

- ``upgrade_package_password``: Upgrade package password used for script based upgrades

- ``upgrade_package_url``: Upgrade package URL used for script based upgrades

- ``upgrade_package_username``: Upgrade package username  used for script based upgrades

- ``upgrade_script_time_limit``: upgradeScriptTimeLimit

- ``upgrade_status``: Script based upgrade Status

- ``upgrade_timedout``: Time limit for the patch based upgrade functionality. If the upgrade process of a VRS has not returned a success or failure status within this time limit, the status will be changed to TIMEOUT. Specified in seconds

- ``primary_nuage_controller``: IP address of the primary Controller (VSC)

- ``vrs_id``: VCenter Name or Id used by toolbox to identify the VRS virtual machine

- ``vrs_password``: VRS password to be used by toolbox to communicate with VRS

- ``vrs_user_name``: VRS user name to be used by toolbox to communicate with VRS

- ``static_route``: static route to be configured in the VRS

- ``static_route_gateway``: Gateway for the static route given above

- ``static_route_netmask``: Nova region name

- ``ntp_server1``: IP of the NTP server 1

- ``ntp_server2``: IP of the NTP server 1

- ``mtu``: Maximum Transmission Unit for eth2 interface

- ``successfully_applied_upgrade_package_password``: The upgrade package Password that was successfully applied

- ``successfully_applied_upgrade_package_url``: The upgrade package URL that was successfully applied

- ``successfully_applied_upgrade_package_username``: The upgrade package Username that was successfully applied

- ``successfully_applied_version``: successfully Applied Version of the VRS VM

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

- ``available_networks``: List of the available network list for the hypervisor.

- ``ovf_url``: ovf url

- ``external_id``: External object ID. Used for integration with third party systems

- ``hypervisor_ip`` (**Mandatory**): IP Address of the Hypervisor

- ``hypervisor_password`` (**Mandatory**): Hypervisor username

- ``hypervisor_user`` (**Mandatory**): Hypervisor username




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`                                                                                                    ``vrs_address_ranges`` 
:ref:`nuvrsmetrics.NUVRSMetrics<nuvrsmetrics>`                                                                                                                   ``vrs_metrics`` 
:ref:`nuvrsredeploymentpolicy.NUVRSRedeploymentpolicy<nuvrsredeploymentpolicy>`                                                                                  ``vrs_redeploymentpolicies`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvcentercluster.NUVCenterCluster<nuvcentercluster>`

- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

- :ref:`nume.NUMe<nume>`

