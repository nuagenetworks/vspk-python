.. _nul2domaintemplate:

nul2domaintemplate
===========================================

.. class:: nul2domaintemplate.NUL2DomainTemplate(bambou.nurest_object.NUMetaRESTObject,):

An L2 Domain is a distributed logical switch that enables L2 communication. An L2 Domain template is a model that can be instantiated as often as required, thereby creating real, functioning L2 Domains.


Attributes
----------


- ``dhcp_managed``: decides whether L2Domain / L2Domain template DHCP is managed by VSD

- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4, DUALSTACK or IPv6

- ``ipv6_address``: IPV6 address of the route - Optional

- ``ipv6_gateway``: The IPv6 address of the gateway of this subnet

- ``name`` (**Mandatory**): Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway``: The IP address of the gateway of this l2 domain

- ``address``: Network address of the L2Domain / L2Domain template defined. 

- ``description``: A description field provided by the user that identifies the L2Domain / L2Domain template.

- ``netmask``: Netmask of the L2Domain / L2Domain template defined

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enable_dhcpv4``: This value indicates whether IPv4 DHCP is enabled or not. This is applicable in case the L2 Domain is DUALSTACK or IPv4

- ``enable_dhcpv6``: This value indicates whether IPv6 DHCP is enabled or not. This is applicable in case the L2 Domain is DUALSTACK or IPv6

- ``encryption``: Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entity_state``: Intermediate State of L2 Domain.

- ``policy_change_status``: None

- ``creation_date``: Time stamp when this object was created.

- ``use_global_mac``: Enable this flag to use system configured globalMACAddress as the gateway mac address for managed l2 domains

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``dual_stack_dynamic_ip_allocation``: This value indicates whether dynamic address allocation is enabled or not. This will be applicable when L2 Domain is managed and in dual stack mode

- ``multicast``: Indicates multicast policy on L2Domain template.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul2domain.NUL2Domain<nul2domain>`                                                                                                                         ``l2_domains`` 
:ref:`nuaddressrange.NUAddressRange<nuaddressrange>`                                                                                                             ``address_ranges`` 
:ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`                                                                      ``redirection_target_templates`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nupgexpressiontemplate.NUPGExpressionTemplate<nupgexpressiontemplate>`                                                                                     ``pg_expression_templates`` 
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nuegressadvfwdtemplate.NUEgressAdvFwdTemplate<nuegressadvfwdtemplate>`                                                                                     ``egress_adv_fwd_templates`` 
:ref:`nuvirtualfirewallpolicy.NUVirtualFirewallPolicy<nuvirtualfirewallpolicy>`                                                                                  ``virtual_firewall_policies`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`                                                                                  ``ingress_adv_fwd_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`                                                                                        ``policy_group_templates`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
:ref:`nuoverlaymirrordestinationtemplate.NUOverlayMirrorDestinationTemplate<nuoverlaymirrordestinationtemplate>`                                                 ``overlay_mirror_destination_templates`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

