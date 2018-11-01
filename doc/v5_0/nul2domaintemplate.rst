.. _nul2domaintemplate:

nul2domaintemplate
===========================================

.. class:: nul2domaintemplate.NUL2DomainTemplate(bambou.nurest_object.NUMetaRESTObject,):

An L2 Domain is a distributed logical switch that enables L2 communication. An L2 Domain template is a model that can be instantiated as often as required, thereby creating real, functioning L2 Domains.


Attributes
----------


- ``dhcp_managed``: decides whether L2Domain / L2Domain template DHCP is managed by VSD

- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``ip_type``: IPv4 or DUALSTACK

- ``ipv6_address``: IPV6 address of the route - Optional

- ``ipv6_gateway``: The IPv6 address of the gateway of this subnet

- ``name`` (**Mandatory**): Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: The IP address of the gateway of this l2 domain

- ``address``: Network address of the L2Domain / L2Domain template defined. 

- ``description``: A description field provided by the user that identifies the L2Domain / L2Domain template.

- ``netmask``: Netmask of the L2Domain / L2Domain template defined

- ``encryption``: Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``entity_state``: Intermediate State of L2 Domain.

- ``policy_change_status``: None

- ``use_global_mac``: Enable this flag to use system configured globalMACAddress as the gateway mac address for managed l2 domains

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``multicast``: Indicates multicast policy on L2Domain template.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_ipv6_address``: Turn on or off dynamic allocation of IPV6 address




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

