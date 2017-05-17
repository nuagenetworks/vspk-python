.. _nul2domaintemplate:

nul2domaintemplate
===========================================

.. class:: nul2domaintemplate.NUL2DomainTemplate(bambou.nurest_object.NUMetaRESTObject,):

L2 Domain in VSD as derived by templates. This object describes the L2 Domain template.


Attributes
----------


- ``dhcp_managed``: decides whether L2Domain / L2Domain template DHCP is managed by VSD

- ``ip_type``: IPv4 or IPv6

- ``name`` (**Mandatory**): Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: The IP address of the gateway of this l2 domain

- ``address``: Network address of the L2Domain / L2Domain template defined. 

- ``description``: A description field provided by the user that identifies the L2Domain / L2Domain template.

- ``netmask``: Netmask of the L2Domain / L2Domain template defined

- ``encryption``: Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_change_status``: 

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

- ``multicast``: Indicates multicast policy on L2Domain template.

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
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`                                                                                  ``ingress_adv_fwd_templates`` 
:ref:`nuingressexternalservicetemplate.NUIngressExternalServiceTemplate<nuingressexternalservicetemplate>`                                                       ``ingress_external_service_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`                                                                                        ``policy_group_templates`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

