.. _nuospfinterface:

nuospfinterface
===========================================

.. class:: nuospfinterface.NUOSPFInterface(bambou.nurest_object.NUMetaRESTObject,):

The OSPF interface represents the connection of a router to the OSPF network. The OSPF interface defines the protocol metrics and security parameters for OSPF traffic on a V-Port on the specified subnet. An OSPF interface can exist in only one OSPF area.


Attributes
----------


- ``bfd_enabled``: Enable or disable Bidirectional Forwarding Detection for this OSPF Interface.

- ``name`` (**Mandatory**): Name of the OSPF Interface. The name has to be unique within the OSPFArea.

- ``passive_enabled``: Enable the passive property of the interface.

- ``last_updated_by``: ID of the user who last updated the object.

- ``admin_state``: Admin state of this OSPF interface

- ``dead_interval``: Time OSPF waits without receiving hello packets before declaring a neighbor down. If specified, it must be at least twice as long as 'helloInterval'.

- ``hello_interval``: Time interval between OSPF hellos issued on the interface.

- ``description``: Description of this OSPF Interface.

- ``message_digest_keys``: This attribute applies only when 'authenticationType' is 'MESSAGE_DIGEST'. In that case, this attribute is a list of pairs of key ID/password used for MD5 authentication. The key ID must by an integer between 1 and 255, and the value is a password (of 16 charachters maximum) used to generate an MD5 hash. The MD5 has is then used as authentication data in the OSPF packets. No duplicate key IDs are allowed. The format for each pair is 'keyID:password' (e.g. '1:foobar')

- ``metric``: Configure an explicit route cost metric for the interface.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``interface_type``: Can be BROADCAST or POINT_TO_POINT

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority``: Determines which routers are selected as the designated router and backup designated router of the area.

- ``associated_subnet_id`` (**Mandatory**): ID of the Subnet which is associated to the current OSPFInterface. Once the OSPF interface is created, the associated subnet ID cannot be updated. The interface must be deleted and re-created with a different subnet ID.

- ``mtu``: MTU to be used by OSPF for this logical interface

- ``authentication_key``: The authentication key that is used on the interface.

- ``authentication_type``: Authentication Type used for this OSPFInterface

- ``external_id``: External object ID. Used for integration with third party systems




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


- :ref:`nuospfarea.NUOSPFArea<nuospfarea>`

