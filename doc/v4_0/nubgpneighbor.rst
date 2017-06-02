.. _nubgpneighbor:

nubgpneighbor
===========================================

.. class:: nubgpneighbor.NUBGPNeighbor(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name``: Name of the peer

- ``dampening_enabled``: Enable/disable route flap damping.

- ``peer_as`` (**Mandatory**): Local autonomous system to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number.

- ``peer_ip``: IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP. For uplink or bridge vPort neighbors the IP address must be specified 

- ``description``: Short description for this peer

- ``session``: neighbor session yang blob

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_export_routing_policy_id``: export policy ID

- ``associated_import_routing_policy_id``: import routing policy ID

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuvlan.NUVLAN<nuvlan>`

