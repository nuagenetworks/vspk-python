.. _nuvirtualfirewallrule:

nuvirtualfirewallrule
===========================================

.. class:: nuvirtualfirewallrule.NUVirtualFirewallRule(bambou.nurest_object.NUMetaRESTObject,):

Virtual firewall rules define intent based security policy entries to control traffic between source/destinations in the network. Virtual firewall rules are inherently stateful and are enforced as Ingress/Egress stateful ACLs in Nuage policy enforcement points


Attributes
----------


- ``acl_template_name``: The name of the parent template for this rule entry

- ``icmp_code``: The ICMP Code when protocol selected is ICMP.

- ``icmp_type``: The ICMP Type when protocol selected is ICMP.

- ``ipv6_address_override``: Overrides the source IPV6 for Ingress and destination IPV6 for Egress, macentries will use this address as the match criteria.

- ``dscp``: DSCP match condition to be set in the rule. It is either * or from 0-63

- ``failsafe_datapath``: Backup datapath option if VNF/VM is down

- ``last_updated_by``: ID of the user who last updated the object.

- ``action`` (**Mandatory**): The action of the rule, DROP or FORWARD. Possible values are DROP, FORWARD.

- ``address_override``: Overrides the source IP for Ingress and destination IP for Egress, macentries will use this address as the match criteria.

- ``web_filter_id``: ID of web filter

- ``web_filter_type``: Indicates type of web filter being set

- ``description``: Description of the rule entry

- ``destination_port``: The destination port to be matched if protocol is UDP or TCP. Value should be either * or a single port number or a port range like 1,2.. or 1 - 10

- ``network_entity_type``: Indicates whether the Network Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, SAASAPPLICATIONGROUP, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``network_id``: The ID of the destination endpoint (Subnet/Zone/PortGroup/PolicyGroupExpression/NetworkMacro/Internet Policy Group/Enterprise Network)

- ``network_type``: Type of the destination endpoint (Subnet/Zone/PortGroup/PolicyGroupExpression/NetworkMacro/Internet Policy Group/Enterprise Network)

- ``mirror_destination_group_id``: ID of the associated Mirror Destination Group.

- ``mirror_destination_id``: Destination ID of the mirror destination object.

- ``flow_logging_enabled``: Is flow logging enabled for this particular template

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_name``: The name of the enterprise for the domain's parent

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_entity_type``: Indicates whether the Location Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, REDIRECTIONTARGET, REDIRECTIONTARGETTEMPLATE, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``location_id``: The ID of the source endpoint (Subnet/Zone/PortGroup/PolicyGroupExpression/NetworkMacro/Internet Policy Group/Enterprise Network)

- ``location_type`` (**Mandatory**): Type of the source endpoint (Subnet/Zone/PortGroup/PolicyGroupExpression/NetworkMacro/Internet Policy Group/Enterprise Network)

- ``policy_state``: State of the policy.

- ``domain_name``: The name of the domain/domain template for the Rule TemplateName.

- ``source_port``: Source port to be matched if protocol is UDP or TCP. Value should be either * or a single port number or a port range like 1,2.. or 1 - 10

- ``priority``: The priority of the rule entry that determines the order of entries

- ``protocol``: Protocol number that must be matched

- ``associated_egress_entry_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``associated_ingress_entry_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``associated_l7_application_signature_id``: The UUID of the associated L7 Application Signature

- ``associated_live_entity_id``: In the draft mode, the rule entry refers to this LiveEntity. In live mode, this is null.

- ``associated_live_template_id``: In the draft mode, the ACL entity refers to this live entity parent. In non-drafted mode, this is null

- ``associated_traffic_type``: This property reflects the type of traffic in case a rule entry is created using an Service or Service Group. In case a protocol and port are specified for the ACL entry, this property has to be empty (null). Supported values are L4_SERVICE, L4_SERVICE_GROUP and empty.

- ``associated_traffic_type_id``: If a traffic type is specified as Service or Service Group, then the associated Id of  Service / Service Group should be specifed here

- ``stateful``: True means that this ACL entry is stateful, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.

- ``stats_id``: The statsID that is created in the VSD and identifies this Rule Template Entry. This is auto-generated by VSD

- ``stats_logging_enabled``: Indicates if stats logging is enabled for this particular template

- ``ether_type``: Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

- ``overlay_mirror_destination_id``: ID of the overlay mirror destination

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Virtual Firewall Rule Type




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`

