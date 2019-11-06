.. _nuwirelessport:

nuwirelessport
===========================================

.. class:: nuwirelessport.NUWirelessPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a Wireless (WiFi) interface configured on a Network Service Gateway (NSG) instance. The WirelessPort instance may map to a physical WiFi card or a WiFi port.


Attributes
----------


- ``vlan_range``: VLAN Range of the Port. Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``name`` (**Mandatory**): A customer friendly name for the Wireless Port instance.

- ``last_updated_by``: ID of the user who last updated the object.

- ``generic_config``: This field is used to contain the 'blob' parameters for the WiFi Card (physical module) on the NSG.

- ``permitted_action``: The permitted action to USE/EXTEND this Wireless Port

- ``description``: A customer friendly description to be given to the Wireless Port instance.

- ``channel_width``: The frequency width of the selected channel for an instance of a Wireless Port.  Generally, the default width is 20 MHz, but based on the WiFi mode and the frequency band, this could be changed to 40 or 80 MHz.  The values for specifying -40 MHz and +40 MHz have been replaced with a global "WIDTH_40_MHZ" value.  Options for WIDTH_LESS_40_MHZ and WIDTH_PLUS_40_MHZ should be avoided.

- ``physical_name`` (**Mandatory**): The identifier of the wireless port as identified by the OS running on the NSG. This name can't be modified once the port is created.

- ``wifi_frequency_band`` (**Mandatory**): Wireless frequency band set on the WiFi card installed. The standard currently supports two frequency bands, 5 GHz and 2.4 GHz. A future variant under name 802.11ad will support 60 GHz.

- ``wifi_mode`` (**Mandatory**): WirelessFidelity 802.11 norm used. The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_type`` (**Mandatory**): Port type for the wireless port. This can be a port of type Access or Network.

- ``country_code`` (**Mandatory**): Country code where the NSG with a Wireless Port installed is defined. The country code allows some WiFi features to be enabled or disabled on the Wireless card.

- ``frequency_channel`` (**Mandatory**): The selected wireless frequency and channel used by the wireless interface. Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.

- ``use_user_mnemonic``: Determines whether to use user mnemonic of the Wireless Port

- ``user_mnemonic``: User Mnemonic of the Port

- ``associated_egress_qos_policy_id``: ID of the Egress QoS Policy associated with this Wireless Port.

- ``status``: Status of the Wireless Port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nussidconnection.NUSSIDConnection<nussidconnection>`                                                                                                       ``ssid_connections`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

