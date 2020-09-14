.. _nudemarcationservice:

nudemarcationservice
===========================================

.. class:: nudemarcationservice.NUDemarcationService(bambou.nurest_object.NUMetaRESTObject,):

Demarcation services provide the interconnection between the datacenter networks and the Wide Area Network.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_distinguisher``: The route distinguisher associated with the next hop. This is a read only property automatically created by VSD.

- ``priority``: Next hop priority assigned by the user.

- ``associated_gateway_id`` (**Mandatory**): The ID of the NSGBR Gateway used as next hop in the untrusted domain.

- ``associated_vlanid``: The VLAN ID of the BR VLAN used as next hop in the trusted domain.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: The type of next hop determines linking direction for a demarcation service, possible values: BR_PORT, GATEWAY 




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


- :ref:`nulink.NULink<nulink>`

