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



from .fetchers import NUAlarmsFetcher


from .fetchers import NUSSIDConnectionsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUWirelessPort(NURESTObject):
    """ Represents a WirelessPort in the VSD

        Notes:
            Represents a wireless (WiFi) interface configured on a Network Service Gateway (NSG) instance.  The WirelessPort instance may map to a physical WiFi card or a WiFi port.
    """

    __rest_name__ = "wirelessport"
    __resource_name__ = "wirelessports"

    
    ## Constants
    
    CONST_COUNTRY_CODE_HK = "HK"
    
    CONST_FREQUENCY_CHANNEL_CH_11 = "CH_11"
    
    CONST_FREQUENCY_CHANNEL_CH_10 = "CH_10"
    
    CONST_FREQUENCY_CHANNEL_CH_13 = "CH_13"
    
    CONST_FREQUENCY_CHANNEL_CH_12 = "CH_12"
    
    CONST_FREQUENCY_CHANNEL_CH_14 = "CH_14"
    
    CONST_FREQUENCY_CHANNEL_CH_149 = "CH_149"
    
    CONST_FREQUENCY_CHANNEL_CH_144 = "CH_144"
    
    CONST_COUNTRY_CODE_HU = "HU"
    
    CONST_FREQUENCY_CHANNEL_CH_140 = "CH_140"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_2_4_GHZ = "FREQ_2_4_GHZ"
    
    CONST_COUNTRY_CODE_GB = "GB"
    
    CONST_FREQUENCY_CHANNEL_CH_132 = "CH_132"
    
    CONST_FREQUENCY_CHANNEL_CH_136 = "CH_136"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_5_0_GHZ = "FREQ_5_0_GHZ"
    
    CONST_COUNTRY_CODE_GR = "GR"
    
    CONST_COUNTRY_CODE_IN = "IN"
    
    CONST_COUNTRY_CODE_AU = "AU"
    
    CONST_COUNTRY_CODE_IL = "IL"
    
    CONST_COUNTRY_CODE_PH = "PH"
    
    CONST_COUNTRY_CODE_IE = "IE"
    
    CONST_COUNTRY_CODE_ID = "ID"
    
    CONST_COUNTRY_CODE_PL = "PL"
    
    CONST_COUNTRY_CODE_PT = "PT"
    
    CONST_FREQUENCY_CHANNEL_CH_157 = "CH_157"
    
    CONST_COUNTRY_CODE_IT = "IT"
    
    CONST_FREQUENCY_CHANNEL_CH_153 = "CH_153"
    
    CONST_COUNTRY_CODE_SI = "SI"
    
    CONST_COUNTRY_CODE_LU = "LU"
    
    CONST_FREQUENCY_CHANNEL_CH_100 = "CH_100"
    
    CONST_COUNTRY_CODE_US = "US"
    
    CONST_FREQUENCY_CHANNEL_CH_36 = "CH_36"
    
    CONST_COUNTRY_CODE_NZ = "NZ"
    
    CONST_FREQUENCY_CHANNEL_CH_104 = "CH_104"
    
    CONST_COUNTRY_CODE_NO = "NO"
    
    CONST_COUNTRY_CODE_NL = "NL"
    
    CONST_FREQUENCY_CHANNEL_CH_161 = "CH_161"
    
    CONST_FREQUENCY_CHANNEL_CH_165 = "CH_165"
    
    CONST_COUNTRY_CODE_EE = "EE"
    
    CONST_WIFI_MODE_WIFI_A_N = "WIFI_A_N"
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    CONST_COUNTRY_CODE_ES = "ES"
    
    CONST_COUNTRY_CODE_FI = "FI"
    
    CONST_COUNTRY_CODE_FR = "FR"
    
    CONST_FREQUENCY_CHANNEL_CH_3 = "CH_3"
    
    CONST_COUNTRY_CODE_CZ = "CZ"
    
    CONST_COUNTRY_CODE_LT = "LT"
    
    CONST_FREQUENCY_CHANNEL_CH_0 = "CH_0"
    
    CONST_COUNTRY_CODE_SK = "SK"
    
    CONST_FREQUENCY_CHANNEL_CH_2 = "CH_2"
    
    CONST_FREQUENCY_CHANNEL_CH_5 = "CH_5"
    
    CONST_FREQUENCY_CHANNEL_CH_4 = "CH_4"
    
    CONST_FREQUENCY_CHANNEL_CH_7 = "CH_7"
    
    CONST_FREQUENCY_CHANNEL_CH_6 = "CH_6"
    
    CONST_FREQUENCY_CHANNEL_CH_9 = "CH_9"
    
    CONST_FREQUENCY_CHANNEL_CH_8 = "CH_8"
    
    CONST_FREQUENCY_CHANNEL_CH_108 = "CH_108"
    
    CONST_COUNTRY_CODE_SE = "SE"
    
    CONST_COUNTRY_CODE_SG = "SG"
    
    CONST_COUNTRY_CODE_CH = "CH"
    
    CONST_COUNTRY_CODE_CN = "CN"
    
    CONST_COUNTRY_CODE_CA = "CA"
    
    CONST_WIFI_MODE_WIFI_B_G = "WIFI_B_G"
    
    CONST_WIFI_MODE_WIFI_A_AC = "WIFI_A_AC"
    
    CONST_COUNTRY_CODE_CY = "CY"
    
    CONST_FREQUENCY_CHANNEL_CH_56 = "CH_56"
    
    CONST_FREQUENCY_CHANNEL_CH_52 = "CH_52"
    
    CONST_COUNTRY_CODE_MY = "MY"
    
    CONST_COUNTRY_CODE_TW = "TW"
    
    CONST_FREQUENCY_CHANNEL_CH_112 = "CH_112"
    
    CONST_COUNTRY_CODE_TH = "TH"
    
    CONST_WIFI_MODE_WIFI_A_N_AC = "WIFI_A_N_AC"
    
    CONST_FREQUENCY_CHANNEL_CH_116 = "CH_116"
    
    CONST_WIFI_MODE_WIFI_B_G_N = "WIFI_B_G_N"
    
    CONST_COUNTRY_CODE_DK = "DK"
    
    CONST_COUNTRY_CODE_DE = "DE"
    
    CONST_FREQUENCY_CHANNEL_CH_1 = "CH_1"
    
    CONST_FREQUENCY_CHANNEL_CH_44 = "CH_44"
    
    CONST_FREQUENCY_CHANNEL_CH_40 = "CH_40"
    
    CONST_FREQUENCY_CHANNEL_CH_48 = "CH_48"
    
    CONST_WIFI_MODE_WIFI_A = "WIFI_A"
    
    CONST_COUNTRY_CODE_JP = "JP"
    
    CONST_COUNTRY_CODE_AT = "AT"
    
    CONST_COUNTRY_CODE_LV = "LV"
    
    CONST_FREQUENCY_CHANNEL_CH_64 = "CH_64"
    
    CONST_FREQUENCY_CHANNEL_CH_60 = "CH_60"
    
    CONST_COUNTRY_CODE_KR = "KR"
    
    CONST_FREQUENCY_CHANNEL_CH_128 = "CH_128"
    
    CONST_FREQUENCY_CHANNEL_CH_124 = "CH_124"
    
    CONST_FREQUENCY_CHANNEL_CH_120 = "CH_120"
    
    CONST_COUNTRY_CODE_BE = "BE"
    
    CONST_COUNTRY_CODE_ZA = "ZA"
    
    CONST_COUNTRY_CODE_BR = "BR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a WirelessPort instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> wirelessport = NUWirelessPort(id=u'xxxx-xxx-xxx-xxx', name=u'WirelessPort')
                >>> wirelessport = NUWirelessPort(data=my_dict)
        """

        super(NUWirelessPort, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._template_id = None
        self._generic_config = None
        self._description = None
        self._physical_name = None
        self._wifi_frequency_band = None
        self._wifi_mode = None
        self._port_type = None
        self._country_code = None
        self._frequency_channel = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_config", remote_name="genericConfig", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="physical_name", remote_name="physicalName", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="wifi_frequency_band", remote_name="wifiFrequencyBand", attribute_type=str, is_required=True, is_unique=False, choices=[u'FREQ_2_4_GHZ', u'FREQ_5_0_GHZ'])
        self.expose_attribute(local_name="wifi_mode", remote_name="wifiMode", attribute_type=str, is_required=True, is_unique=False, choices=[u'WIFI_A', u'WIFI_A_AC', u'WIFI_A_N', u'WIFI_A_N_AC', u'WIFI_B_G', u'WIFI_B_G_N'])
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS'])
        self.expose_attribute(local_name="country_code", remote_name="countryCode", attribute_type=str, is_required=True, is_unique=False, choices=[u'AT', u'AU', u'BE', u'BR', u'CA', u'CH', u'CN', u'CY', u'CZ', u'DE', u'DK', u'EE', u'ES', u'FI', u'FR', u'GB', u'GR', u'HK', u'HU', u'ID', u'IE', u'IL', u'IN', u'IT', u'JP', u'KR', u'LT', u'LU', u'LV', u'MY', u'NL', u'NO', u'NZ', u'PH', u'PL', u'PT', u'SE', u'SG', u'SI', u'SK', u'TH', u'TW', u'US', u'ZA'])
        self.expose_attribute(local_name="frequency_channel", remote_name="frequencyChannel", attribute_type=str, is_required=True, is_unique=False, choices=[u'CH_0', u'CH_1', u'CH_10', u'CH_100', u'CH_104', u'CH_108', u'CH_11', u'CH_112', u'CH_116', u'CH_12', u'CH_120', u'CH_124', u'CH_128', u'CH_13', u'CH_132', u'CH_136', u'CH_14', u'CH_140', u'CH_144', u'CH_149', u'CH_153', u'CH_157', u'CH_161', u'CH_165', u'CH_2', u'CH_3', u'CH_36', u'CH_4', u'CH_40', u'CH_44', u'CH_48', u'CH_5', u'CH_52', u'CH_56', u'CH_6', u'CH_60', u'CH_64', u'CH_7', u'CH_8', u'CH_9'])
        

        # Fetchers
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ssid_connections = NUSSIDConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A customer friendly name for the Wireless Port instance.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A customer friendly name for the Wireless Port instance.

                
        """
        self._name = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Wireless Port was created from.  If the wireless port was not created from a template, then the value will be null.

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Wireless Port was created from.  If the wireless port was not created from a template, then the value will be null.

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def generic_config(self):
        """ Get generic_config value.

            Notes:
                This field is used to contain the "blob" parameters for the WiFi Card (physical module) on the NSG.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        return self._generic_config

    @generic_config.setter
    def generic_config(self, value):
        """ Set generic_config value.

            Notes:
                This field is used to contain the "blob" parameters for the WiFi Card (physical module) on the NSG.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        self._generic_config = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A customer friendly description to be given to the Wireless Port instance.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A customer friendly description to be given to the Wireless Port instance.

                
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

    

    