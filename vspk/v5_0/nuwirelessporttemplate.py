# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from bambou import NURESTObject


class NUWirelessPortTemplate(NURESTObject):
    """ Represents a WirelessPortTemplate in the VSD

        Notes:
            Template of a Wireless Interface that may exist on a NSGateway Template instance.  Instantiation of NSG Template will result in the creation of a Wireless Port instance on the NSG instance.  Parameters defined on the template will be used to polulate the attributes on the Wireless Port instance inheriting from the template.
    """

    __rest_name__ = "wirelessporttemplate"
    __resource_name__ = "wirelessporttemplates"

    
    ## Constants
    
    CONST_COUNTRY_CODE_US = "US"
    
    CONST_COUNTRY_CODE_CA = "CA"
    
    CONST_WIFI_MODE_WIFI_A_N = "WIFI_A_N"
    
    CONST_WIFI_MODE_WIFI_B_G = "WIFI_B_G"
    
    CONST_WIFI_MODE_WIFI_A_AC = "WIFI_A_AC"
    
    CONST_WIFI_MODE_WIFI_A = "WIFI_A"
    
    CONST_FREQUENCY_CHANNEL_CH_1 = "CH_1"
    
    CONST_FREQUENCY_CHANNEL_CH_0 = "CH_0"
    
    CONST_FREQUENCY_CHANNEL_CH_2 = "CH_2"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_5_0_GHZ = "FREQ_5_0_GHZ"
    
    CONST_WIFI_MODE_WIFI_A_N_AC = "WIFI_A_N_AC"
    
    CONST_COUNTRY_CODE_UK = "UK"
    
    CONST_COUNTRY_CODE_FR = "FR"
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    CONST_WIFI_MODE_WIFI_B_G_N = "WIFI_B_G_N"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_2_4_GHZ = "FREQ_2_4_GHZ"
    
    

    def __init__(self, **kwargs):
        """ Initializes a WirelessPortTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> wirelessporttemplate = NUWirelessPortTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'WirelessPortTemplate')
                >>> wirelessporttemplate = NUWirelessPortTemplate(data=my_dict)
        """

        super(NUWirelessPortTemplate, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._generic_config = None
        self._description = None
        self._physical_name = None
        self._wifi_frequency_band = None
        self._wifi_mode = None
        self._port_type = None
        self._country_code = None
        self._frequency_channel = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="generic_config", remote_name="genericConfig", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="physical_name", remote_name="physicalName", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="wifi_frequency_band", remote_name="wifiFrequencyBand", attribute_type=str, is_required=True, is_unique=False, choices=[u'FREQ_2_4_GHZ', u'FREQ_5_0_GHZ'])
        self.expose_attribute(local_name="wifi_mode", remote_name="wifiMode", attribute_type=str, is_required=True, is_unique=False, choices=[u'WIFI_A', u'WIFI_A_AC', u'WIFI_A_N', u'WIFI_A_N_AC', u'WIFI_B_G', u'WIFI_B_G_N'])
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS'])
        self.expose_attribute(local_name="country_code", remote_name="countryCode", attribute_type=str, is_required=True, is_unique=False, choices=[u'CA', u'FR', u'UK', u'US'])
        self.expose_attribute(local_name="frequency_channel", remote_name="frequencyChannel", attribute_type=str, is_required=True, is_unique=False, choices=[u'CH_0', u'CH_1', u'CH_2'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A customer friendly name for the Wireless Port template.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A customer friendly name for the Wireless Port template.

                
        """
        self._name = value

    
    @property
    def generic_config(self):
        """ Get generic_config value.

            Notes:
                Configuration blob for the Wireless Port/Card installed on the NSG.  It contains the less common Wireless parameters that can be configured at the OS level for the WiFi card.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        return self._generic_config

    @generic_config.setter
    def generic_config(self, value):
        """ Set generic_config value.

            Notes:
                Configuration blob for the Wireless Port/Card installed on the NSG.  It contains the less common Wireless parameters that can be configured at the OS level for the WiFi card.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        self._generic_config = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A customer friendly description to be given to the Wireless Port Template.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A customer friendly description to be given to the Wireless Port Template.

                
        """
        self._description = value

    
    @property
    def physical_name(self):
        """ Get physical_name value.

            Notes:
                The identifier of the wireless port as identified by the OS running on the NSG.  This name can't be modified once the port is created.

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    @physical_name.setter
    def physical_name(self, value):
        """ Set physical_name value.

            Notes:
                The identifier of the wireless port as identified by the OS running on the NSG.  This name can't be modified once the port is created.

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    
    @property
    def wifi_frequency_band(self):
        """ Get wifi_frequency_band value.

            Notes:
                Wireless frequency band set on the WiFi card installed.  The standard currently supports two frequency bands, 5 GHz and 2.4 GHz.  A future variant under name 802.11ad will support 60 GHz.

                
                This attribute is named `wifiFrequencyBand` in VSD API.
                
        """
        return self._wifi_frequency_band

    @wifi_frequency_band.setter
    def wifi_frequency_band(self, value):
        """ Set wifi_frequency_band value.

            Notes:
                Wireless frequency band set on the WiFi card installed.  The standard currently supports two frequency bands, 5 GHz and 2.4 GHz.  A future variant under name 802.11ad will support 60 GHz.

                
                This attribute is named `wifiFrequencyBand` in VSD API.
                
        """
        self._wifi_frequency_band = value

    
    @property
    def wifi_mode(self):
        """ Get wifi_mode value.

            Notes:
                WirelessFidelity 802.11 norm used.  The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

                
                This attribute is named `wifiMode` in VSD API.
                
        """
        return self._wifi_mode

    @wifi_mode.setter
    def wifi_mode(self, value):
        """ Set wifi_mode value.

            Notes:
                WirelessFidelity 802.11 norm used.  The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

                
                This attribute is named `wifiMode` in VSD API.
                
        """
        self._wifi_mode = value

    
    @property
    def port_type(self):
        """ Get port_type value.

            Notes:
                Port type for the wireless port.  This can be a port of type Access or Network.

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    @port_type.setter
    def port_type(self, value):
        """ Set port_type value.

            Notes:
                Port type for the wireless port.  This can be a port of type Access or Network.

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    
    @property
    def country_code(self):
        """ Get country_code value.

            Notes:
                Country code where the NSG with a Wireless Port installed is defined.  The country code allows some WiFi features to be enabled or disabled on the Wireless card.

                
                This attribute is named `countryCode` in VSD API.
                
        """
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        """ Set country_code value.

            Notes:
                Country code where the NSG with a Wireless Port installed is defined.  The country code allows some WiFi features to be enabled or disabled on the Wireless card.

                
                This attribute is named `countryCode` in VSD API.
                
        """
        self._country_code = value

    
    @property
    def frequency_channel(self):
        """ Get frequency_channel value.

            Notes:
                The selected wireless frequency and channel used by the wireless interface.  Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.

                
                This attribute is named `frequencyChannel` in VSD API.
                
        """
        return self._frequency_channel

    @frequency_channel.setter
    def frequency_channel(self, value):
        """ Set frequency_channel value.

            Notes:
                The selected wireless frequency and channel used by the wireless interface.  Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.

                
                This attribute is named `frequencyChannel` in VSD API.
                
        """
        self._frequency_channel = value

    

    