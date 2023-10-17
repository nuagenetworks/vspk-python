.. _nuethernetsegmentgwgroup:

nuethernetsegmentgwgroup
===========================================

.. class:: nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup(bambou.nurest_object.NUMetaRESTObject,):

Group of Gateways with common Ethernet Segment IDs (upto 4 Gateways).


Attributes
----------


- ``name`` (**Mandatory**): Name of the Ethernet Segment Gateway Group.

- ``personality``: Personality of the Ethernet Segment Gateway Group.

- ``description``: Description of the Ethernet Segment Gateway Group.

- ``assoc_gateways_names``: Array of the names of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_name>", "<gw2_name>", "<gw3_name>", "<gw4_name>"].

- ``assoc_gateways_status``: Array of the connection status of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_status>", "<gw2_status>", "<gw3_status>", "<gw4_status>"].

- ``associated_gateway_ids`` (**Mandatory**): Array of the UUIDs of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_uuid>", "<gw2_uuid>", "<gw3_uuid>", "<gw4_uuid>"].




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`numacfilterprofile.NUMACFilterProfile<numacfilterprofile>`                                                                                                 ``mac_filter_profiles`` 
:ref:`nusapegressqosprofile.NUSAPEgressQoSProfile<nusapegressqosprofile>`                                                                                        ``sap_egress_qo_s_profiles`` 
:ref:`nusapingressqosprofile.NUSAPIngressQoSProfile<nusapingressqosprofile>`                                                                                     ``sap_ingress_qo_s_profiles`` 
:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nuegressprofile.NUEgressProfile<nuegressprofile>`                                                                                                          ``egress_profiles`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuingressprofile.NUIngressProfile<nuingressprofile>`                                                                                                       ``ingress_profiles`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nuipfilterprofile.NUIPFilterProfile<nuipfilterprofile>`                                                                                                    ``ip_filter_profiles`` 
:ref:`nuipv6filterprofile.NUIPv6FilterProfile<nuipv6filterprofile>`                                                                                              ``ipv6_filter_profiles`` 
:ref:`nuethernetsegmentgroup.NUEthernetSegmentGroup<nuethernetsegmentgroup>`                                                                                     ``ethernet_segment_groups`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

