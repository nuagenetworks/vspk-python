.. _nuwirelessport:

nuwirelessport
===========================================

.. class:: nuwirelessport.NUWirelessPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a wireless (WiFi) interface configured on a Network Service Gateway (NSG) instance.  The WirelessPort instance may map to a physical WiFi card or a WiFi port.


Attributes
----------


- ``name`` (**Mandatory**): A customer friendly name for the Wireless Port instance.

- ``template_id``: The ID of the template that this Wireless Port was created from.  If the wireless port was not created from a template, then the value will be null.

- ``generic_config``: This field is used to contain the "blob" parameters for the WiFi Card (physical module) on the NSG.

- ``description``: A customer friendly description to be given to the Wireless Port instance.

- ``physical_name`` (**Mandatory**): The identifier of the wireless port as identified by the OS running on the NSG.  This name can't be modified once the port is created.

- ``wifi_frequency_band`` (**Mandatory**): Wireless frequency band set on the WiFi card installed.  The standard currently supports two frequency bands, 5 GHz and 2.4 GHz.  A future variant under name 802.11ad will support 60 GHz.

- ``wifi_mode`` (**Mandatory**): WirelessFidelity 802.11 norm used.  The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

- ``port_type`` (**Mandatory**): Port type for the wireless port.  This can be a port of type Access or Network.

- ``country_code`` (**Mandatory**): Country code where the NSG with a Wireless Port installed is defined.  The country code allows some WiFi features to be enabled or disabled on the Wireless card.

- ``frequency_channel`` (**Mandatory**): The selected wireless frequency and channel used by the wireless interface.  Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nussidconnection.NUSSIDConnection<nussidconnection>`                                                                                                       ``ssid_connections`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

