.. _nubgpneighbor:

nubgpneighbor
===========================================

.. class:: nubgpneighbor.NUBGPNeighbor(bambou.nurest_object.NUMetaRESTObject,):

Virtual Cloud Services (VCS) in the data center BGP PE-CE is configured at vport level . Network Service Gateways (NSG) BGP is configured at subnet level.


Attributes
----------


- ``bfd_enabled``: Enable or disable Bidirectional Forwarding Detection for this BGP neighbor. Not Applicable for third-party Netconf Gateways.

- ``ip_type``: It can be either IPv4 or IPv6

- ``ipv6_address``: Peer IPv6 address

- ``name`` (**Mandatory**): Name of the peer

- ``dampening_enabled``: Enable/disable route flap damping.

- ``peer_as`` (**Mandatory**): Autonomous System (AS) value to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number.

- ``peer_configuration``: BGP Peer session configuration and default policies.

- ``peer_ip``: IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP. For uplink or bridge vPort neighbors the IP address must be specified 

- ``description``: Short description for this peer

- ``session``: neighbor session yang blob

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``domain_service_label``: Service ID or external label given to Domain

- ``associated_export_routing_policy_id``: export policy ID

- ``associated_import_routing_policy_id``: import routing policy ID

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nudeploymentfailure.NUDeploymentFailure<nudeploymentfailure>`                                                                                              ``deployment_failures`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nume.NUMe<nume>`

