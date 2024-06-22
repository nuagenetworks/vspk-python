.. _nuegressaclentrytemplate:

nuegressaclentrytemplate
===========================================

.. class:: nuegressaclentrytemplate.NUEgressACLEntryTemplate(bambou.nurest_object.NUMetaRESTObject,):

Security Policy Entries defines what action to take for a particular type of traffic, based on its origin and its destination, its protocol, EtherType, eventual ports, DSCP value and other information.


Attributes
----------


- ``acl_template_name``: The name of the parent Template for this acl entry

- ``icmp_code``: The ICMP Code when selected protocol is ICMP

- ``icmp_type``: The ICMP Type when selected protocol is ICMP

- ``ipv6_address_override``: Overrides Destination IPv6 match for Egress.

- ``dscp`` (**Mandatory**): DSCP match condition to be set in the rule. It is either * or from 0-63

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``action`` (**Mandatory**): The action of the ACL entry.

- ``address_override``: Overrides Destination IP match for Egress.

- ``web_filter_id``: ID of web filter category or web domain name entity used

- ``web_filter_stats_logging_enabled``: Indicates if web filter statistics logging is enabled for this particular template

- ``web_filter_type``: Indicates type of web filter being set

- ``description``: Description of the ACL entry

- ``destination_port``: The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

- ``network_entity_type``: Indicates whether the Network Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, SAASAPPLICATIONGROUP, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``network_id``: The ID of the source endpoint (Subnet/Zone/Macro/MacroGroup/PortGroup/PolicyGroupExpression)

- ``network_type``: Type of the source endpoint (Subnet/Zone/Macro/MacroGroup/PortGroup/PolicyGroupExpression)

- ``mirror_destination_group_id``: ID of the associated Mirror Destination Group.

- ``mirror_destination_id``: Destination ID of the mirror destination object.

- ``flow_logging_enabled``: Is flow logging enabled for this particular template

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_name``: The name of the enterprise for the domains parent

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_entity_type``: Indicates whether the Location Entity of ACL Entry was derived from a L2/L3 Domain template or instance. Possible Values: ENTERPRISENETWORK, NETWORKMACROGROUP, PGEXPRESSION, PGEXPRESSIONTEMPLATE, POLICYGROUP, POLICYGROUPTEMPLATE, PUBLICNETWORK, REDIRECTIONTARGET, REDIRECTIONTARGETTEMPLATE, SUBNET, SUBNETTEMPLATE, ZONE, ZONETEMPLATE.

- ``location_id``: The ID of the destination endpoint (Subnet/Zone/VportTag/PolicyGroup/PolicyGroupExpression)

- ``location_type`` (**Mandatory**): Type of the destination endpoint (Subnet/Zone/VportTag/PolicyGroup/PolicyGroupExpression

- ``policy_state``: State of the policy.  Possible values are DRAFT, LIVE, .

- ``domain_name``: The name of the domain/domain template for the aclTemplateNames parent

- ``source_port``: Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

- ``creation_date``: Time stamp when this object was created.

- ``priority``: The priority of the ACL entry that determines the order of entries

- ``protocol``: Protocol number that must be matched

- ``associated_l7_application_signature_id``: The UUID of the associated L7 Application signature

- ``associated_live_entity_id``: In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

- ``associated_live_template_id``: In the draft mode, the ACL entity refers to this live entity parent. In non-drafted mode, this is null

- ``associated_traffic_type``: This property reflects the type of traffic in case an ACL entry is created using an Service or Service Group. In case a protocol and port are specified for the ACL entry, this property has to be empty (null). Supported values are L4_SERVICE, L4_SERVICE_GROUP and empty.

- ``associated_traffic_type_id``: If a traffic type is specified as Service or Service Group, then the associated Id of  Service / Service Group should be specifed here

- ``associated_virtual_firewall_rule_id``: The ID of the Virtual Firewall Rule, if this was derived as part of the Virtual Firewall Rule creation

- ``stateful``: True means that this ACL entry is stateful, so there will be a corresponding rule that will be created by OVS in the network. False means that there is no corresponding rule created by OVS in the network.

- ``stats_id``: The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

- ``stats_logging_enabled``: Indicates if stats logging is enabled for this particular template

- ``ether_type`` (**Mandatory**): Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

- ``overlay_mirror_destination_id``: ID of the overlay mirror destination

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


- :ref:`nume.NUMe<nume>`

- :ref:`numirrordestination.NUMirrorDestination<numirrordestination>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`

