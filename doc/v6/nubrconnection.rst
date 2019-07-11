.. _nubrconnection:

nubrconnection
===========================================

.. class:: nubrconnection.NUBRConnection(bambou.nurest_object.NUMetaRESTObject,):

Configuration of VNS Gateway Border Router connection


Attributes
----------


- ``dns_address``: DNS Address for the vlan

- ``dns_address_v6``: DNS IPv6 Address

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: IP address of the gateway bound to the VLAN.

- ``gateway_v6``: IPv6 address of the gateway bound to the port.

- ``address``: Static IP address for the VLAN on which the BR Connection is created.

- ``address_family``: IP address family of this BRConnection

- ``address_v6``: IPv6 address for static configuration on the BR Connection instance.

- ``advertisement_criteria``: Advertisement Criteria for Traffic Flow on a BR Connection.

- ``netmask``: network mask

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``inherited``: This flag will determine if the abstract connection is inherited from the instance template

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``mode``: Connection mode: Only static is allowed on a Bridge Router Connection.

- ``uplink_id``: Internally generated ID in the range that idenitifies the uplink within the context of NSG.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nubfdsession.NUBFDSession<nubfdsession>`                                                                                                                   ``bfd_sessions`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvlan.NUVLAN<nuvlan>`

- :ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`

