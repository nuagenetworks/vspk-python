.. _nupolicygrouptemplate:

nupolicygrouptemplate
===========================================

.. class:: nupolicygrouptemplate.NUPolicyGroupTemplate(bambou.nurest_object.NUMetaRESTObject,):

PolicyGroupTemplate represents the template of a policy group object. PolicyGroup is group of vports on which a user can policies like ACL, QoS, etc.


Attributes
----------


- ``evpn_community_tag``: An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.

- ``name`` (**Mandatory**): Name of the policy group

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Describes this policy group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external``: Indicates whether this PG is internal to VSP or not.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of policy group.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

