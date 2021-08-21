.. _nuingressadvfwdentrytemplate:

nuingressadvfwdentrytemplate
===========================================

.. class:: nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate(bambou.nurest_object.NUMetaRESTObject,):

Security Policy Entries defines what action to take for a particular type of traffic, based on its origin and its destination, its protocol, EtherType, eventual ports, DSCP value and other information.


Attributes
----------


- ``acl_template_name``: The name of the parent Template for this acl entry

- ``icmp_code``: The ICMP Code when protocol selected is ICMP.

- ``icmp_type``: The ICMP Type when protocol selected is ICMP.

- ``fc_override``: Value of the Service Class to be overridden in the packet when the match conditions are satisfied Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``ipv6_address_override``: Overrides the source IPv6 for Ingress and destination IPv6 for Egress, MAC entries will use this address as the match criteria.

- ``dscp`` (**Mandatory**): DSCP match condition to be set in the rule. It is either * or from 0-63

- ``dscp_remarking``: Remarking value for the DSCP field in IP header of customer packet.DSCP value range from enumeration of 65 values: NONE, 0, 1, ..., 63

- ``failsafe_datapath``: Backup datapath option if VNF/VM is down

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``action`` (**Mandatory**): The action of the ACL entry DROP or FORWARD or REDIRECT or FORWARDING_PATH_LIST. Actions REDIRECT and FORWARDING_PATH_LIST are allowed only for IngressAdvancedForwardingEntry. Possible values are DROP, FORWARD, REDIRECT, FORWARDING_PATH_LIST. If FORWARDING_PATH_LIST is selected in IngressAdvancedForwardingEntry, user will have to attach a ForwardingPathList (list of forwarding action-uplink preference entries) to the ACL.  

- ``address_override``: Overrides the source IP for Ingress and destination IP for Egress, MAC entries will use this address as the match criteria.

- ``address_override_type``: Address Override Type can be IPV4, IPV6 or MACRO_GROUP.

- ``web_filter_id``: ID of web filter category or web domain name entity used

- ``web_filter_stats_logging_enabled``: Indicates if web filter statistics logging is enabled for this particular template

- ``web_filter_type``: Indicates type of web filter being set

- ``redirect_rewrite_type``: The type of redirection rewrite. Currently only VLAN is supported

- ``redirect_rewrite_value``: The redirect rewrite value. Currently only vlan id is supported

- ``redirect_vport_tag_id``: VPort tag to which traffic will be redirected to, when ACL entry match criteria succeeds

- ``redirection_target_entity_type``: Indicates whether the Redirection Target of ACL Entry was derived from a L3 Domain template or instance. Possible Values: REDIRECTIONTARGET, REDIRECTIONTARGETTEMPLATE.

- ``remote_uplink_preference``: Indicates the preferencial path selection for network traffic for this ACL.

- ``description``: Description of the ACL entry

- ``destination_port``: The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

- ``network_entity_type``: Indicates whether the Network Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, SAASAPPLICATIONGROUP, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``network_id``: The destination network entity that is referenced(subnet/zone/macro/PolicyGroupExpression)

- ``network_type``: Type of the source network.

- ``mirror_destination_group_id``: ID of the associated Mirror Destination Group.

- ``mirror_destination_id``: Destination ID of the mirror destination object.

- ``vlan_range``: The range can be a single number or a range. Eg : 1,10,15-17

- ``flow_logging_enabled``: Is flow logging enabled for this particular template

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_name``: The name of the enterprise for the domains parent

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_entity_type``: Indicates whether the Location Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, REDIRECTIONTARGET, REDIRECTIONTARGETTEMPLATE, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``location_id``: The ID of the location entity (Subnet/Zone/VportTag/PolicyGroupExpression)

- ``location_type`` (**Mandatory**): Type of the location entity.

- ``policy_state``: State of the policy.  Possible values are DRAFT, LIVE, .

- ``domain_name``: The name of the domain/domain template for the aclTemplateNames parent

- ``source_port``: Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

- ``uplink_preference``: Indicates the preferencial path selection for network traffic for this ACL - default is DEFAULT when the attribute is applicable.

- ``app_type``: Type of application selected, ALL (all applications in match criteria), NONE (no application in match criteria), APPLICATION (specific application in match criteria).

- ``creation_date``: Time stamp when this object was created.

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``protocol``: Protocol number that must be matched

- ``is_sla_aware``: This flag denotes whether the Uplink Preference configured by the user will work with AAR or will over-ride AAR.

- ``associated_application_id``: Associated application UUID.

- ``associated_forwarding_path_list_id``: Associated forwarding path list UUID.

- ``associated_live_entity_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``associated_live_template_id``: In the draft mode, the ACL entity refers to this live entity parent. In non-drafted mode, this is null

- ``associated_traffic_type``: This property reflects the type of traffic in case an ACL entry is created using an Service or Service Group. In case a protocol and port are specified for the ACL entry, this property has to be empty (null). Supported values are L4_SERVICE, L4_SERVICE_GROUP and empty.

- ``associated_traffic_type_id``: If a traffic type is specified as Service or Service Group, then the associated Id of  Service / Service Group should be specifed here

- ``associated_virtual_firewall_rule_id``: The ID of the Virtual Firewall Rule, if this was derived as part of the Virtual Firewall Rule creation

- ``stats_id``: The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

- ``stats_logging_enabled``: Indicates if stats logging is enabled for this particular template

- ``ether_type`` (**Mandatory**): Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`

- :ref:`nume.NUMe<nume>`

