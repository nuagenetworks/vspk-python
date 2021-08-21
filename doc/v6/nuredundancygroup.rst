.. _nuredundancygroup:

nuredundancygroup
===========================================

.. class:: nuredundancygroup.NURedundancyGroup(bambou.nurest_object.NUMetaRESTObject,):

Represents Redundant Group formed by two Gateways.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Redundancy Group 

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_peer1_autodiscovered_gateway_id``: The Auto Discovered Gateway configuration owner in this Redundant Group. 

- ``gateway_peer1_connected``: Indicates status of the authoritative  gateway of this Redundancy Group.

- ``gateway_peer1_id`` (**Mandatory**): The gateway configuration owner in this Redundant Group.  When Redundant Group is deleted this gateway will receive vPort associated to the group.

- ``gateway_peer1_name``: The name of the authoritative gateway of the redundant group.

- ``gateway_peer2_autodiscovered_gateway_id``: The Auto Discovered Gateway  peer in this Redundant Group

- ``gateway_peer2_connected``: Indicates status of the secondary gateway of this Redundancy Group.

- ``gateway_peer2_id`` (**Mandatory**): The gateway peer in this Redundant Group. When Redundant Group is deleted this gateway will not recieve vport associations.

- ``gateway_peer2_name``: The gateway peer name in this Redundant Group

- ``redundant_gateway_status``: The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

- ``personality``: derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, VDFG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .

- ``description``:  Description of the Redundancy Group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: The enterprise associated with this Redundant Group. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``vtep``: Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`                                                                                                 ``mac_filter_profiles`` 
:ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`                                                                                        ``sap_egress_qo_s_profiles`` 
:ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`                                                                                     ``sap_ingress_qo_s_profiles`` 
:ref:`nugateway.NUGateway<nugateway>`                                                                                                                            ``gateways`` 
:ref:`nugatewayredundantport.NUGatewayRedundantPort<nugatewayredundantport>`                                                                                     ``gateway_redundant_ports`` 
:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nuwanservice.NUWANService<nuwanservice>`                                                                                                                   ``wan_services`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`                                                                                                          ``egress_profiles`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`                                                                                                       ``ingress_profiles`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nuport.NUPort<nuport>`                                                                                                                                     ``ports`` 
:ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`                                                                                                    ``ip_filter_profiles`` 
:ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`                                                                                              ``ipv6_filter_profiles`` 
:ref:`nuvsgredundantport.NUVsgRedundantPort<nuvsgredundantport>`                                                                                                 ``vsg_redundant_ports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nume.NUMe<nume>`

