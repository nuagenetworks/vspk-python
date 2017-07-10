.. _nuwirelessporttemplate:

nuwirelessporttemplate
===========================================

.. class:: nuwirelessporttemplate.NUWirelessPortTemplate(bambou.nurest_object.NUMetaRESTObject,):

Template of a Wireless Interface that may exist on a NSGateway Template instance.  Instantiation of NSG Template will result in the creation of a Wireless Port instance on the NSG instance.  Parameters defined on the template will be used to polulate the attributes on the Wireless Port instance inheriting from the template.


Attributes
----------


- ``name`` (**Mandatory**): A customer friendly name for the Wireless Port template.

- ``generic_config``: Configuration blob for the Wireless Port/Card installed on the NSG.  It contains the less common Wireless parameters that can be configured at the OS level for the WiFi card.

- ``description``: A customer friendly description to be given to the Wireless Port Template.

- ``physical_name`` (**Mandatory**): The identifier of the wireless port as identified by the OS running on the NSG.  This name can't be modified once the port is created.

- ``wifi_frequency_band`` (**Mandatory**): Wireless frequency band set on the WiFi card installed.  The standard currently supports two frequency bands, 5 GHz and 2.4 GHz.  A future variant under name 802.11ad will support 60 GHz.

- ``wifi_mode`` (**Mandatory**): WirelessFidelity 802.11 norm used.  The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

- ``port_type`` (**Mandatory**): Port type for the wireless port.  This can be a port of type Access or Network.

- ``country_code`` (**Mandatory**): Country code where the NSG with a Wireless Port installed is defined.  The country code allows some WiFi features to be enabled or disabled on the Wireless card.

- ``frequency_channel`` (**Mandatory**): The selected wireless frequency and channel used by the wireless interface.  Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.





