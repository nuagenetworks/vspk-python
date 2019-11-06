# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUSSIDConnectionsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUWirelessPort(NURESTObject):
    """ Represents a WirelessPort in the VSD

        Notes:
            Represents a Wireless (WiFi) interface configured on a Network Service Gateway (NSG) instance. The WirelessPort instance may map to a physical WiFi card or a WiFi port.
    """

    __rest_name__ = "wirelessport"
    __resource_name__ = "wirelessports"

    
    ## Constants
    
    CONST_FREQUENCY_CHANNEL_CH_116 = "CH_116"
    
    CONST_COUNTRY_CODE_HK = "HK"
    
    CONST_COUNTRY_CODE_HM = "HM"
    
    CONST_COUNTRY_CODE_HN = "HN"
    
    CONST_FREQUENCY_CHANNEL_CH_11 = "CH_11"
    
    CONST_FREQUENCY_CHANNEL_CH_10 = "CH_10"
    
    CONST_COUNTRY_CODE_SK = "SK"
    
    CONST_COUNTRY_CODE_TK = "TK"
    
    CONST_COUNTRY_CODE_GH = "GH"
    
    CONST_COUNTRY_CODE_TD = "TD"
    
    CONST_COUNTRY_CODE_SD = "SD"
    
    CONST_COUNTRY_CODE_WF = "WF"
    
    CONST_FREQUENCY_CHANNEL_CH_157 = "CH_157"
    
    CONST_COUNTRY_CODE_PY = "PY"
    
    CONST_COUNTRY_CODE_HR = "HR"
    
    CONST_COUNTRY_CODE_HT = "HT"
    
    CONST_COUNTRY_CODE_HU = "HU"
    
    CONST_FREQUENCY_CHANNEL_CH_140 = "CH_140"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_2_4_GHZ = "FREQ_2_4_GHZ"
    
    CONST_COUNTRY_CODE_GE = "GE"
    
    CONST_COUNTRY_CODE_GD = "GD"
    
    CONST_FREQUENCY_CHANNEL_CH_7 = "CH_7"
    
    CONST_COUNTRY_CODE_GF = "GF"
    
    CONST_COUNTRY_CODE_GA = "GA"
    
    CONST_COUNTRY_CODE_WS = "WS"
    
    CONST_COUNTRY_CODE_GB = "GB"
    
    CONST_COUNTRY_CODE_GM = "GM"
    
    CONST_COUNTRY_CODE_GL = "GL"
    
    CONST_COUNTRY_CODE_GN = "GN"
    
    CONST_CHANNEL_WIDTH_WIDTH_20_MHZ = "WIDTH_20_MHZ"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_COUNTRY_CODE_QA = "QA"
    
    CONST_COUNTRY_CODE_GU = "GU"
    
    CONST_COUNTRY_CODE_GT = "GT"
    
    CONST_COUNTRY_CODE_GW = "GW"
    
    CONST_FREQUENCY_CHANNEL_CH_136 = "CH_136"
    
    CONST_WIFI_FREQUENCY_BAND_FREQ_5_0_GHZ = "FREQ_5_0_GHZ"
    
    CONST_COUNTRY_CODE_GP = "GP"
    
    CONST_COUNTRY_CODE_GS = "GS"
    
    CONST_COUNTRY_CODE_GR = "GR"
    
    CONST_COUNTRY_CODE_TC = "TC"
    
    CONST_COUNTRY_CODE_GY = "GY"
    
    CONST_FREQUENCY_CHANNEL_CH_13 = "CH_13"
    
    CONST_COUNTRY_CODE_AW = "AW"
    
    CONST_COUNTRY_CODE_IN = "IN"
    
    CONST_COUNTRY_CODE_AU = "AU"
    
    CONST_COUNTRY_CODE_AT = "AT"
    
    CONST_COUNTRY_CODE_AS = "AS"
    
    CONST_COUNTRY_CODE_AR = "AR"
    
    CONST_COUNTRY_CODE_AQ = "AQ"
    
    CONST_COUNTRY_CODE_PG = "PG"
    
    CONST_COUNTRY_CODE_PH = "PH"
    
    CONST_COUNTRY_CODE_IE = "IE"
    
    CONST_COUNTRY_CODE_ID = "ID"
    
    CONST_COUNTRY_CODE_PL = "PL"
    
    CONST_COUNTRY_CODE_AZ = "AZ"
    
    CONST_COUNTRY_CODE_PN = "PN"
    
    CONST_COUNTRY_CODE_ST = "ST"
    
    CONST_COUNTRY_CODE_AG = "AG"
    
    CONST_COUNTRY_CODE_AF = "AF"
    
    CONST_COUNTRY_CODE_AE = "AE"
    
    CONST_COUNTRY_CODE_AD = "AD"
    
    CONST_COUNTRY_CODE_PT = "PT"
    
    CONST_COUNTRY_CODE_CD = "CD"
    
    CONST_COUNTRY_CODE_PW = "PW"
    
    CONST_COUNTRY_CODE_AO = "AO"
    
    CONST_COUNTRY_CODE_AN = "AN"
    
    CONST_COUNTRY_CODE_AM = "AM"
    
    CONST_COUNTRY_CODE_AL = "AL"
    
    CONST_COUNTRY_CODE_IS = "IS"
    
    CONST_COUNTRY_CODE_IR = "IR"
    
    CONST_COUNTRY_CODE_AI = "AI"
    
    CONST_COUNTRY_CODE_SI = "SI"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_COUNTRY_CODE_TF = "TF"
    
    CONST_CHANNEL_WIDTH_WIDTH_PLUS_40_MHZ = "WIDTH_PLUS_40_MHZ"
    
    CONST_COUNTRY_CODE_IT = "IT"
    
    CONST_FREQUENCY_CHANNEL_CH_2 = "CH_2"
    
    CONST_FREQUENCY_CHANNEL_CH_5 = "CH_5"
    
    CONST_COUNTRY_CODE_SN = "SN"
    
    CONST_FREQUENCY_CHANNEL_CH_4 = "CH_4"
    
    CONST_COUNTRY_CODE_US = "US"
    
    CONST_FREQUENCY_CHANNEL_CH_36 = "CH_36"
    
    CONST_FREQUENCY_CHANNEL_CH_144 = "CH_144"
    
    CONST_FREQUENCY_CHANNEL_CH_9 = "CH_9"
    
    CONST_COUNTRY_CODE_NZ = "NZ"
    
    CONST_COUNTRY_CODE_SO = "SO"
    
    CONST_COUNTRY_CODE_UZ = "UZ"
    
    CONST_COUNTRY_CODE_TG = "TG"
    
    CONST_COUNTRY_CODE_NU = "NU"
    
    CONST_COUNTRY_CODE_NR = "NR"
    
    CONST_COUNTRY_CODE_NP = "NP"
    
    CONST_COUNTRY_CODE_NO = "NO"
    
    CONST_COUNTRY_CODE_NL = "NL"
    
    CONST_COUNTRY_CODE_UG = "UG"
    
    CONST_COUNTRY_CODE_NI = "NI"
    
    CONST_COUNTRY_CODE_NF = "NF"
    
    CONST_COUNTRY_CODE_NG = "NG"
    
    CONST_CHANNEL_WIDTH_WIDTH_40_MHZ = "WIDTH_40_MHZ"
    
    CONST_COUNTRY_CODE_NE = "NE"
    
    CONST_COUNTRY_CODE_NC = "NC"
    
    CONST_COUNTRY_CODE_UM = "UM"
    
    CONST_COUNTRY_CODE_NA = "NA"
    
    CONST_COUNTRY_CODE_EC = "EC"
    
    CONST_COUNTRY_CODE_EG = "EG"
    
    CONST_COUNTRY_CODE_EE = "EE"
    
    CONST_WIFI_MODE_WIFI_A_N = "WIFI_A_N"
    
    CONST_COUNTRY_CODE_EH = "EH"
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    CONST_COUNTRY_CODE_ES = "ES"
    
    CONST_COUNTRY_CODE_ER = "ER"
    
    CONST_COUNTRY_CODE_ET = "ET"
    
    CONST_FREQUENCY_CHANNEL_CH_12 = "CH_12"
    
    CONST_COUNTRY_CODE_VU = "VU"
    
    CONST_FREQUENCY_CHANNEL_CH_153 = "CH_153"
    
    CONST_FREQUENCY_CHANNEL_CH_60 = "CH_60"
    
    CONST_FREQUENCY_CHANNEL_CH_108 = "CH_108"
    
    CONST_COUNTRY_CODE_IQ = "IQ"
    
    CONST_COUNTRY_CODE_OM = "OM"
    
    CONST_COUNTRY_CODE_VG = "VG"
    
    CONST_COUNTRY_CODE_VE = "VE"
    
    CONST_FREQUENCY_CHANNEL_CH_64 = "CH_64"
    
    CONST_CHANNEL_WIDTH_WIDTH_LESS_40_MHZ = "WIDTH_LESS_40_MHZ"
    
    CONST_COUNTRY_CODE_VA = "VA"
    
    CONST_COUNTRY_CODE_VN = "VN"
    
    CONST_COUNTRY_CODE_RU = "RU"
    
    CONST_STATUS_ORPHAN = "ORPHAN"
    
    CONST_COUNTRY_CODE_VI = "VI"
    
    CONST_COUNTRY_CODE_FO = "FO"
    
    CONST_COUNTRY_CODE_SH = "SH"
    
    CONST_COUNTRY_CODE_FM = "FM"
    
    CONST_COUNTRY_CODE_FJ = "FJ"
    
    CONST_COUNTRY_CODE_FK = "FK"
    
    CONST_COUNTRY_CODE_FI = "FI"
    
    CONST_COUNTRY_CODE_FR = "FR"
    
    CONST_FREQUENCY_CHANNEL_CH_48 = "CH_48"
    
    CONST_FREQUENCY_CHANNEL_CH_132 = "CH_132"
    
    CONST_FREQUENCY_CHANNEL_CH_14 = "CH_14"
    
    CONST_COUNTRY_CODE_VC = "VC"
    
    CONST_COUNTRY_CODE_SY = "SY"
    
    CONST_COUNTRY_CODE_SZ = "SZ"
    
    CONST_COUNTRY_CODE_TR = "TR"
    
    CONST_COUNTRY_CODE_LA = "LA"
    
    CONST_COUNTRY_CODE_LB = "LB"
    
    CONST_COUNTRY_CODE_LC = "LC"
    
    CONST_COUNTRY_CODE_PM = "PM"
    
    CONST_COUNTRY_CODE_GI = "GI"
    
    CONST_COUNTRY_CODE_SR = "SR"
    
    CONST_COUNTRY_CODE_LI = "LI"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_COUNTRY_CODE_LT = "LT"
    
    CONST_COUNTRY_CODE_LU = "LU"
    
    CONST_COUNTRY_CODE_LV = "LV"
    
    CONST_COUNTRY_CODE_SJ = "SJ"
    
    CONST_COUNTRY_CODE_SM = "SM"
    
    CONST_COUNTRY_CODE_SL = "SL"
    
    CONST_COUNTRY_CODE_LR = "LR"
    
    CONST_COUNTRY_CODE_LS = "LS"
    
    CONST_COUNTRY_CODE_SA = "SA"
    
    CONST_FREQUENCY_CHANNEL_CH_8 = "CH_8"
    
    CONST_COUNTRY_CODE_SC = "SC"
    
    CONST_COUNTRY_CODE_SB = "SB"
    
    CONST_COUNTRY_CODE_SE = "SE"
    
    CONST_COUNTRY_CODE_LY = "LY"
    
    CONST_COUNTRY_CODE_SG = "SG"
    
    CONST_COUNTRY_CODE_CI = "CI"
    
    CONST_COUNTRY_CODE_CH = "CH"
    
    CONST_COUNTRY_CODE_CK = "CK"
    
    CONST_COUNTRY_CODE_CM = "CM"
    
    CONST_COUNTRY_CODE_CL = "CL"
    
    CONST_COUNTRY_CODE_CO = "CO"
    
    CONST_COUNTRY_CODE_CN = "CN"
    
    CONST_COUNTRY_CODE_CA = "CA"
    
    CONST_FREQUENCY_CHANNEL_CH_56 = "CH_56"
    
    CONST_COUNTRY_CODE_CC = "CC"
    
    CONST_WIFI_MODE_WIFI_B_G = "WIFI_B_G"
    
    CONST_WIFI_MODE_WIFI_A_AC = "WIFI_A_AC"
    
    CONST_COUNTRY_CODE_CG = "CG"
    
    CONST_COUNTRY_CODE_CF = "CF"
    
    CONST_COUNTRY_CODE_CY = "CY"
    
    CONST_COUNTRY_CODE_CX = "CX"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_COUNTRY_CODE_CZ = "CZ"
    
    CONST_FREQUENCY_CHANNEL_CH_52 = "CH_52"
    
    CONST_COUNTRY_CODE_GQ = "GQ"
    
    CONST_COUNTRY_CODE_CR = "CR"
    
    CONST_COUNTRY_CODE_CU = "CU"
    
    CONST_COUNTRY_CODE_UY = "UY"
    
    CONST_COUNTRY_CODE_CV = "CV"
    
    CONST_COUNTRY_CODE_TL = "TL"
    
    CONST_COUNTRY_CODE_MZ = "MZ"
    
    CONST_COUNTRY_CODE_MY = "MY"
    
    CONST_COUNTRY_CODE_MX = "MX"
    
    CONST_COUNTRY_CODE_TZ = "TZ"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_COUNTRY_CODE_MS = "MS"
    
    CONST_COUNTRY_CODE_MR = "MR"
    
    CONST_COUNTRY_CODE_MQ = "MQ"
    
    CONST_COUNTRY_CODE_MP = "MP"
    
    CONST_COUNTRY_CODE_MW = "MW"
    
    CONST_COUNTRY_CODE_MV = "MV"
    
    CONST_COUNTRY_CODE_MU = "MU"
    
    CONST_COUNTRY_CODE_MT = "MT"
    
    CONST_COUNTRY_CODE_LK = "LK"
    
    CONST_COUNTRY_CODE_TM = "TM"
    
    CONST_COUNTRY_CODE_TN = "TN"
    
    CONST_COUNTRY_CODE_MH = "MH"
    
    CONST_COUNTRY_CODE_MO = "MO"
    
    CONST_COUNTRY_CODE_MN = "MN"
    
    CONST_WIFI_MODE_WIFI_A_N_AC = "WIFI_A_N_AC"
    
    CONST_COUNTRY_CODE_ML = "ML"
    
    CONST_COUNTRY_CODE_MC = "MC"
    
    CONST_FREQUENCY_CHANNEL_CH_128 = "CH_128"
    
    CONST_COUNTRY_CODE_MA = "MA"
    
    CONST_COUNTRY_CODE_JM = "JM"
    
    CONST_COUNTRY_CODE_MG = "MG"
    
    CONST_WIFI_MODE_WIFI_B_G_N = "WIFI_B_G_N"
    
    CONST_COUNTRY_CODE_ME = "ME"
    
    CONST_COUNTRY_CODE_MD = "MD"
    
    CONST_COUNTRY_CODE_DM = "DM"
    
    CONST_COUNTRY_CODE_DO = "DO"
    
    CONST_COUNTRY_CODE_DJ = "DJ"
    
    CONST_COUNTRY_CODE_DK = "DK"
    
    CONST_COUNTRY_CODE_DE = "DE"
    
    CONST_COUNTRY_CODE_ZW = "ZW"
    
    CONST_COUNTRY_CODE_UA = "UA"
    
    CONST_FREQUENCY_CHANNEL_CH_1 = "CH_1"
    
    CONST_FREQUENCY_CHANNEL_CH_124 = "CH_124"
    
    CONST_FREQUENCY_CHANNEL_CH_44 = "CH_44"
    
    CONST_FREQUENCY_CHANNEL_CH_40 = "CH_40"
    
    CONST_COUNTRY_CODE_DZ = "DZ"
    
    CONST_FREQUENCY_CHANNEL_CH_6 = "CH_6"
    
    CONST_COUNTRY_CODE_RS = "RS"
    
    CONST_STATUS_READY = "READY"
    
    CONST_CHANNEL_WIDTH_WIDTH_80_MHZ = "WIDTH_80_MHZ"
    
    CONST_COUNTRY_CODE_IO = "IO"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_COUNTRY_CODE_PS = "PS"
    
    CONST_COUNTRY_CODE_PA = "PA"
    
    CONST_COUNTRY_CODE_BF = "BF"
    
    CONST_FREQUENCY_CHANNEL_CH_112 = "CH_112"
    
    CONST_FREQUENCY_CHANNEL_CH_0 = "CH_0"
    
    CONST_COUNTRY_CODE_JO = "JO"
    
    CONST_WIFI_MODE_WIFI_A = "WIFI_A"
    
    CONST_FREQUENCY_CHANNEL_CH_149 = "CH_149"
    
    CONST_COUNTRY_CODE_JP = "JP"
    
    CONST_COUNTRY_CODE_IL = "IL"
    
    CONST_COUNTRY_CODE_MM = "MM"
    
    CONST_FREQUENCY_CHANNEL_CH_161 = "CH_161"
    
    CONST_COUNTRY_CODE_TO = "TO"
    
    CONST_COUNTRY_CODE_PE = "PE"
    
    CONST_FREQUENCY_CHANNEL_CH_120 = "CH_120"
    
    CONST_FREQUENCY_CHANNEL_CH_3 = "CH_3"
    
    CONST_COUNTRY_CODE_PF = "PF"
    
    CONST_FREQUENCY_CHANNEL_CH_104 = "CH_104"
    
    CONST_COUNTRY_CODE_YT = "YT"
    
    CONST_FREQUENCY_CHANNEL_CH_165 = "CH_165"
    
    CONST_COUNTRY_CODE_SV = "SV"
    
    CONST_COUNTRY_CODE_TT = "TT"
    
    CONST_COUNTRY_CODE_ZA = "ZA"
    
    CONST_STATUS_MISMATCH = "MISMATCH"
    
    CONST_STATUS_INITIALIZED = "INITIALIZED"
    
    CONST_COUNTRY_CODE_TH = "TH"
    
    CONST_COUNTRY_CODE_YE = "YE"
    
    CONST_COUNTRY_CODE_TV = "TV"
    
    CONST_COUNTRY_CODE_PK = "PK"
    
    CONST_COUNTRY_CODE_KE = "KE"
    
    CONST_COUNTRY_CODE_KG = "KG"
    
    CONST_COUNTRY_CODE_KI = "KI"
    
    CONST_COUNTRY_CODE_KH = "KH"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_COUNTRY_CODE_KM = "KM"
    
    CONST_COUNTRY_CODE_RW = "RW"
    
    CONST_COUNTRY_CODE_KN = "KN"
    
    CONST_COUNTRY_CODE_KP = "KP"
    
    CONST_COUNTRY_CODE_KR = "KR"
    
    CONST_COUNTRY_CODE_RO = "RO"
    
    CONST_COUNTRY_CODE_KW = "KW"
    
    CONST_COUNTRY_CODE_KY = "KY"
    
    CONST_FREQUENCY_CHANNEL_CH_100 = "CH_100"
    
    CONST_COUNTRY_CODE_KZ = "KZ"
    
    CONST_COUNTRY_CODE_RE = "RE"
    
    CONST_COUNTRY_CODE_BJ = "BJ"
    
    CONST_COUNTRY_CODE_MK = "MK"
    
    CONST_COUNTRY_CODE_BH = "BH"
    
    CONST_COUNTRY_CODE_BI = "BI"
    
    CONST_COUNTRY_CODE_BN = "BN"
    
    CONST_COUNTRY_CODE_BO = "BO"
    
    CONST_COUNTRY_CODE_BM = "BM"
    
    CONST_COUNTRY_CODE_BB = "BB"
    
    CONST_COUNTRY_CODE_BA = "BA"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_COUNTRY_CODE_BG = "BG"
    
    CONST_COUNTRY_CODE_BD = "BD"
    
    CONST_COUNTRY_CODE_BE = "BE"
    
    CONST_COUNTRY_CODE_BZ = "BZ"
    
    CONST_COUNTRY_CODE_BY = "BY"
    
    CONST_COUNTRY_CODE_TJ = "TJ"
    
    CONST_COUNTRY_CODE_PR = "PR"
    
    CONST_COUNTRY_CODE_BR = "BR"
    
    CONST_COUNTRY_CODE_BS = "BS"
    
    CONST_COUNTRY_CODE_TW = "TW"
    
    CONST_COUNTRY_CODE_BV = "BV"
    
    CONST_COUNTRY_CODE_BW = "BW"
    
    CONST_COUNTRY_CODE_BT = "BT"
    
    CONST_COUNTRY_CODE_ZM = "ZM"
    
    

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
        
        self._vlan_range = None
        self._name = None
        self._last_updated_by = None
        self._generic_config = None
        self._permitted_action = None
        self._description = None
        self._channel_width = None
        self._physical_name = None
        self._wifi_frequency_band = None
        self._wifi_mode = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._port_type = None
        self._country_code = None
        self._frequency_channel = None
        self._use_user_mnemonic = None
        self._user_mnemonic = None
        self._associated_egress_qos_policy_id = None
        self._status = None
        self._external_id = None
        
        self.expose_attribute(local_name="vlan_range", remote_name="VLANRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="generic_config", remote_name="genericConfig", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="channel_width", remote_name="channelWidth", attribute_type=str, is_required=False, is_unique=False, choices=[u'WIDTH_20_MHZ', u'WIDTH_40_MHZ', u'WIDTH_80_MHZ', u'WIDTH_LESS_40_MHZ', u'WIDTH_PLUS_40_MHZ'])
        self.expose_attribute(local_name="physical_name", remote_name="physicalName", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="wifi_frequency_band", remote_name="wifiFrequencyBand", attribute_type=str, is_required=True, is_unique=False, choices=[u'FREQ_2_4_GHZ', u'FREQ_5_0_GHZ'])
        self.expose_attribute(local_name="wifi_mode", remote_name="wifiMode", attribute_type=str, is_required=True, is_unique=False, choices=[u'WIFI_A', u'WIFI_A_AC', u'WIFI_A_N', u'WIFI_A_N_AC', u'WIFI_B_G', u'WIFI_B_G_N'])
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS'])
        self.expose_attribute(local_name="country_code", remote_name="countryCode", attribute_type=str, is_required=True, is_unique=False, choices=[u'AD', u'AE', u'AF', u'AG', u'AI', u'AL', u'AM', u'AN', u'AO', u'AQ', u'AR', u'AS', u'AT', u'AU', u'AW', u'AZ', u'BA', u'BB', u'BD', u'BE', u'BF', u'BG', u'BH', u'BI', u'BJ', u'BM', u'BN', u'BO', u'BR', u'BS', u'BT', u'BV', u'BW', u'BY', u'BZ', u'CA', u'CC', u'CD', u'CF', u'CG', u'CH', u'CI', u'CK', u'CL', u'CM', u'CN', u'CO', u'CR', u'CU', u'CV', u'CX', u'CY', u'CZ', u'DE', u'DJ', u'DK', u'DM', u'DO', u'DZ', u'EC', u'EE', u'EG', u'EH', u'ER', u'ES', u'ET', u'FI', u'FJ', u'FK', u'FM', u'FO', u'FR', u'GA', u'GB', u'GD', u'GE', u'GF', u'GH', u'GI', u'GL', u'GM', u'GN', u'GP', u'GQ', u'GR', u'GS', u'GT', u'GU', u'GW', u'GY', u'HK', u'HM', u'HN', u'HR', u'HT', u'HU', u'ID', u'IE', u'IL', u'IN', u'IO', u'IQ', u'IR', u'IS', u'IT', u'JM', u'JO', u'JP', u'KE', u'KG', u'KH', u'KI', u'KM', u'KN', u'KP', u'KR', u'KW', u'KY', u'KZ', u'LA', u'LB', u'LC', u'LI', u'LK', u'LR', u'LS', u'LT', u'LU', u'LV', u'LY', u'MA', u'MC', u'MD', u'ME', u'MG', u'MH', u'MK', u'ML', u'MM', u'MN', u'MO', u'MP', u'MQ', u'MR', u'MS', u'MT', u'MU', u'MV', u'MW', u'MX', u'MY', u'MZ', u'NA', u'NC', u'NE', u'NF', u'NG', u'NI', u'NL', u'NO', u'NP', u'NR', u'NU', u'NZ', u'OM', u'PA', u'PE', u'PF', u'PG', u'PH', u'PK', u'PL', u'PM', u'PN', u'PR', u'PS', u'PT', u'PW', u'PY', u'QA', u'RE', u'RO', u'RS', u'RU', u'RW', u'SA', u'SB', u'SC', u'SD', u'SE', u'SG', u'SH', u'SI', u'SJ', u'SK', u'SL', u'SM', u'SN', u'SO', u'SR', u'ST', u'SV', u'SY', u'SZ', u'TC', u'TD', u'TF', u'TG', u'TH', u'TJ', u'TK', u'TL', u'TM', u'TN', u'TO', u'TR', u'TT', u'TV', u'TW', u'TZ', u'UA', u'UG', u'UM', u'US', u'UY', u'UZ', u'VA', u'VC', u'VE', u'VG', u'VI', u'VN', u'VU', u'WF', u'WS', u'YE', u'YT', u'ZA', u'ZM', u'ZW'])
        self.expose_attribute(local_name="frequency_channel", remote_name="frequencyChannel", attribute_type=str, is_required=True, is_unique=False, choices=[u'CH_0', u'CH_1', u'CH_10', u'CH_100', u'CH_104', u'CH_108', u'CH_11', u'CH_112', u'CH_116', u'CH_12', u'CH_120', u'CH_124', u'CH_128', u'CH_13', u'CH_132', u'CH_136', u'CH_14', u'CH_140', u'CH_144', u'CH_149', u'CH_153', u'CH_157', u'CH_161', u'CH_165', u'CH_2', u'CH_3', u'CH_36', u'CH_4', u'CH_40', u'CH_44', u'CH_48', u'CH_5', u'CH_52', u'CH_56', u'CH_6', u'CH_60', u'CH_64', u'CH_7', u'CH_8', u'CH_9'])
        self.expose_attribute(local_name="use_user_mnemonic", remote_name="useUserMnemonic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_mnemonic", remote_name="userMnemonic", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_egress_qos_policy_id", remote_name="associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'INITIALIZED', u'MISMATCH', u'ORPHAN', u'READY'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ssid_connections = NUSSIDConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the Port. Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    @vlan_range.setter
    def vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the Port. Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    
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
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def generic_config(self):
        """ Get generic_config value.

            Notes:
                This field is used to contain the 'blob' parameters for the WiFi Card (physical module) on the NSG.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        return self._generic_config

    @generic_config.setter
    def generic_config(self, value):
        """ Set generic_config value.

            Notes:
                This field is used to contain the 'blob' parameters for the WiFi Card (physical module) on the NSG.

                
                This attribute is named `genericConfig` in VSD API.
                
        """
        self._generic_config = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted action to USE/EXTEND this Wireless Port

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted action to USE/EXTEND this Wireless Port

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
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
    def channel_width(self):
        """ Get channel_width value.

            Notes:
                The frequency width of the selected channel for an instance of a Wireless Port.  Generally, the default width is 20 MHz, but based on the WiFi mode and the frequency band, this could be changed to 40 or 80 MHz.  The values for specifying -40 MHz and +40 MHz have been replaced with a global "WIDTH_40_MHZ" value.  Options for WIDTH_LESS_40_MHZ and WIDTH_PLUS_40_MHZ should be avoided.

                
                This attribute is named `channelWidth` in VSD API.
                
        """
        return self._channel_width

    @channel_width.setter
    def channel_width(self, value):
        """ Set channel_width value.

            Notes:
                The frequency width of the selected channel for an instance of a Wireless Port.  Generally, the default width is 20 MHz, but based on the WiFi mode and the frequency band, this could be changed to 40 or 80 MHz.  The values for specifying -40 MHz and +40 MHz have been replaced with a global "WIDTH_40_MHZ" value.  Options for WIDTH_LESS_40_MHZ and WIDTH_PLUS_40_MHZ should be avoided.

                
                This attribute is named `channelWidth` in VSD API.
                
        """
        self._channel_width = value

    
    @property
    def physical_name(self):
        """ Get physical_name value.

            Notes:
                The identifier of the wireless port as identified by the OS running on the NSG. This name can't be modified once the port is created.

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    @physical_name.setter
    def physical_name(self, value):
        """ Set physical_name value.

            Notes:
                The identifier of the wireless port as identified by the OS running on the NSG. This name can't be modified once the port is created.

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    
    @property
    def wifi_frequency_band(self):
        """ Get wifi_frequency_band value.

            Notes:
                Wireless frequency band set on the WiFi card installed. The standard currently supports two frequency bands, 5 GHz and 2.4 GHz. A future variant under name 802.11ad will support 60 GHz.

                
                This attribute is named `wifiFrequencyBand` in VSD API.
                
        """
        return self._wifi_frequency_band

    @wifi_frequency_band.setter
    def wifi_frequency_band(self, value):
        """ Set wifi_frequency_band value.

            Notes:
                Wireless frequency band set on the WiFi card installed. The standard currently supports two frequency bands, 5 GHz and 2.4 GHz. A future variant under name 802.11ad will support 60 GHz.

                
                This attribute is named `wifiFrequencyBand` in VSD API.
                
        """
        self._wifi_frequency_band = value

    
    @property
    def wifi_mode(self):
        """ Get wifi_mode value.

            Notes:
                WirelessFidelity 802.11 norm used. The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

                
                This attribute is named `wifiMode` in VSD API.
                
        """
        return self._wifi_mode

    @wifi_mode.setter
    def wifi_mode(self, value):
        """ Set wifi_mode value.

            Notes:
                WirelessFidelity 802.11 norm used. The values supported represents a combination of modes that are to be enabled at once on the WiFi Card.

                
                This attribute is named `wifiMode` in VSD API.
                
        """
        self._wifi_mode = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def port_type(self):
        """ Get port_type value.

            Notes:
                Port type for the wireless port. This can be a port of type Access or Network.

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    @port_type.setter
    def port_type(self, value):
        """ Set port_type value.

            Notes:
                Port type for the wireless port. This can be a port of type Access or Network.

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    
    @property
    def country_code(self):
        """ Get country_code value.

            Notes:
                Country code where the NSG with a Wireless Port installed is defined. The country code allows some WiFi features to be enabled or disabled on the Wireless card.

                
                This attribute is named `countryCode` in VSD API.
                
        """
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        """ Set country_code value.

            Notes:
                Country code where the NSG with a Wireless Port installed is defined. The country code allows some WiFi features to be enabled or disabled on the Wireless card.

                
                This attribute is named `countryCode` in VSD API.
                
        """
        self._country_code = value

    
    @property
    def frequency_channel(self):
        """ Get frequency_channel value.

            Notes:
                The selected wireless frequency and channel used by the wireless interface. Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.

                
                This attribute is named `frequencyChannel` in VSD API.
                
        """
        return self._frequency_channel

    @frequency_channel.setter
    def frequency_channel(self, value):
        """ Set frequency_channel value.

            Notes:
                The selected wireless frequency and channel used by the wireless interface. Channels range is from 0 to 165 where 0 stands for Auto Channel Selection.

                
                This attribute is named `frequencyChannel` in VSD API.
                
        """
        self._frequency_channel = value

    
    @property
    def use_user_mnemonic(self):
        """ Get use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the Wireless Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        return self._use_user_mnemonic

    @use_user_mnemonic.setter
    def use_user_mnemonic(self, value):
        """ Set use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the Wireless Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        self._use_user_mnemonic = value

    
    @property
    def user_mnemonic(self):
        """ Get user_mnemonic value.

            Notes:
                User Mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        return self._user_mnemonic

    @user_mnemonic.setter
    def user_mnemonic(self, value):
        """ Set user_mnemonic value.

            Notes:
                User Mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        self._user_mnemonic = value

    
    @property
    def associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QoS Policy associated with this Wireless Port.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    @associated_egress_qos_policy_id.setter
    def associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QoS Policy associated with this Wireless Port.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Status of the Wireless Port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Status of the Wireless Port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

                
        """
        self._status = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    