.. _nudomaintemplate:

nudomaintemplate
===========================================

.. class:: nudomaintemplate.NUDomainTemplate(bambou.nurest_object.NUMetaRESTObject,):

Domains in VSD are created from domain templates. This object provides the definition of the Domain Template.


Attributes
----------


- ``dpi``: determines whether or not Deep packet inspection is enabled

- ``name`` (**Mandatory**): The name of the domain template, that is unique within an enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Domain template description provided by the user

- ``encryption``: Determines whether IPSEC is enabled. Possible values are ENABLED, DISABLED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``policy_change_status``: None

- ``associated_bgp_profile_id``: The ID of the associated BGP profile

- ``associated_multicast_channel_map_id``: The ID of the Multi Cast Channel Map  this domain template is associated with. This has to be set when enableMultiCast is set to ENABLED

- ``associated_pat_mapper_id``: The ID of the PatMapper entity to which this domain-template is associated to.

- ``multicast``: Indicates multicast policy on domain.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuredirectiontargettemplate.NURedirectionTargetTemplate<nuredirectiontargettemplate>`                                                                      ``redirection_target_templates`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuegressacltemplate.NUEgressACLTemplate<nuegressacltemplate>`                                                                                              ``egress_acl_templates`` 
:ref:`nudomainfipacltemplate.NUDomainFIPAclTemplate<nudomainfipacltemplate>`                                                                                     ``domain_fip_acl_templates`` 
:ref:`nufloatingipacltemplate.NUFloatingIPACLTemplate<nufloatingipacltemplate>`                                                                                  ``floating_ipacl_templates`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressacltemplate.NUIngressACLTemplate<nuingressacltemplate>`                                                                                           ``ingress_acl_templates`` 
:ref:`nuingressadvfwdtemplate.NUIngressAdvFwdTemplate<nuingressadvfwdtemplate>`                                                                                  ``ingress_adv_fwd_templates`` 
:ref:`nuingressexternalservicetemplate.NUIngressExternalServiceTemplate<nuingressexternalservicetemplate>`                                                       ``ingress_external_service_templates`` 
:ref:`nujob.NUJob<nujob>`                                                                                                                                        ``jobs`` 
:ref:`nupolicygrouptemplate.NUPolicyGroupTemplate<nupolicygrouptemplate>`                                                                                        ``policy_group_templates`` 
:ref:`nudomain.NUDomain<nudomain>`                                                                                                                               ``domains`` 
:ref:`nuzonetemplate.NUZoneTemplate<nuzonetemplate>`                                                                                                             ``zone_templates`` 
:ref:`nuqos.NUQOS<nuqos>`                                                                                                                                        ``qoss`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nusubnettemplate.NUSubnetTemplate<nusubnettemplate>`                                                                                                       ``subnet_templates`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nudomain.NUDomain<nudomain>`

