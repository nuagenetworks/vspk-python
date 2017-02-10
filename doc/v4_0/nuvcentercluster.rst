.. _nuvcentercluster:

nuvcentercluster
===========================================

.. class:: nuvcentercluster.NUVCenterCluster(bambou.nurest_object.NUMetaRESTObject,):

VCenter Clusters.


Attributes
----------


- ``vrs_configuration_time_limit``: The maximum wait time limit in minutes to get VRS configured at cluster level

- ``v_require_nuage_metadata``: Whether split-activation or not (Openstack/CloudStack)

- ``name`` (**Mandatory**): Name of the Cluster

- ``managed_object_id``: VCenter Managed Object ID of the Cluster.

- ``last_updated_by``: ID of the user who last updated the object.

- ``data_dns1``: Data DNS 1

- ``data_dns2``: Data DNS 2

- ``data_gateway``: Data Gateway

- ``data_network_portgroup``: Data Network Port Group

- ``datapath_sync_timeout``: Datapath Sync Timeout

- ``scope``: Cluster in scope or not in scope.

- ``secondary_nuage_controller``: IP address of the secondary Controller (VSC)

- ``deleted_from_vcenter_data_center``: Set to true if the cluster is deleted from Vcenter

- ``generic_split_activation``: Whether split-activation is needed from VRO

- ``separate_data_network``: Whether Data will use the management network or not

- ``personality``: VRS/VRS-G

- ``description``: Description of the Cluster

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

- ``mgmt_network_portgroup``: Management Network Port group

- ``dhcp_relay_server``: To provide IP address of the interface from which you will connect to the DHCP relay server

- ``mirror_network_portgroup``: Mirror Port Group Name

- ``site_id``: Site ID field for object profiles to support VSD Geo-redundancy

- ``allow_data_dhcp``: Whether to get the Data IP for the VRS VM from DHCP or statically

- ``allow_mgmt_dhcp``: Whether to get the management IP for the VRS VM from DHCP or statically.

- ``flow_eviction_threshold``: Flow Eviction Threshold

- ``vm_network_portgroup``: VM Network Port Group Name

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``portgroup_metadata``: Port Group Meta data

- ``nova_client_version``: Nova client Version 

- ``nova_metadata_service_auth_url``: Nova metadata service auth url

- ``nova_metadata_service_endpoint``: Nova metadata service endpoint

- ``nova_metadata_service_password``: Nova metadata service password

- ``nova_metadata_service_tenant``: Nova metadata service tenant

- ``nova_metadata_service_username``: Nova metadata service username

- ``nova_metadata_shared_secret``: Nova metadata shared secret

- ``nova_region_name``: Nova region name

- ``upgrade_package_password``: upgradePackagePassword

- ``upgrade_package_url``: upgradePackageURL

- ``upgrade_package_username``: upgradePackageUsername

- ``upgrade_script_time_limit``: upgradeScriptTimeLimit

- ``primary_nuage_controller``: IP address of the primary Controller (VSC)

- ``vrs_password``: VRS password to be used by toolbox to communicate with VRS

- ``vrs_user_name``: VRS user name to be used by toolbox to communicate with VRS

- ``assoc_vcenter_data_center_id``: The ID of the vcenter to which this host is attached

- ``assoc_vcenter_id``: ID of the associated VCenter.

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

- ``ovf_url``: ovf url

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuvcenterhypervisor.NUVCenterHypervisor<nuvcenterhypervisor>`                                                                                              ``vcenter_hypervisors`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuvrsaddressrange.NUVRSAddressRange<nuvrsaddressrange>`                                                                                                    ``vrs_address_ranges`` 
:ref:`nuvrsredeploymentpolicy.NUVRSRedeploymentpolicy<nuvrsredeploymentpolicy>`                                                                                  ``vrs_redeploymentpolicies`` 
:ref:`nuautodiscoverhypervisorfromcluster.NUAutoDiscoverHypervisorFromCluster<nuautodiscoverhypervisorfromcluster>`                                              ``auto_discover_hypervisor_from_clusters`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvcenterdatacenter.NUVCenterDataCenter<nuvcenterdatacenter>`

