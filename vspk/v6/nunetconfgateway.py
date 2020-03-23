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




from .fetchers import NUL2DomainsFetcher


from .fetchers import NUMACFilterProfilesFetcher


from .fetchers import NUSAPEgressQoSProfilesFetcher


from .fetchers import NUSAPIngressQoSProfilesFetcher


from .fetchers import NUGatewaySecuritiesFetcher


from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NUDeploymentFailuresFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUWANServicesFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUEgressProfilesFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUInfrastructureConfigsFetcher


from .fetchers import NUIngressProfilesFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NULocationsFetcher


from .fetchers import NUDomainsFetcher


from .fetchers import NUBootstrapsFetcher


from .fetchers import NUBootstrapActivationsFetcher


from .fetchers import NUPortsFetcher


from .fetchers import NUIPFilterProfilesFetcher


from .fetchers import NUIPv6FilterProfilesFetcher


from .fetchers import NUSubnetsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUNetconfGateway(NURESTObject):
    """ Represents a NetconfGateway in the VSD

        Notes:
            Represents Netconf Gateway object.
    """

    __rest_name__ = "netconfgateway"
    __resource_name__ = "netconfgateways"

    
    ## Constants
    
    CONST_FAMILY_NSG_C = "NSG_C"
    
    CONST_PERMITTED_ACTION_ALL = "ALL"
    
    CONST_FAMILY_NSG_E = "NSG_E"
    
    CONST_PERSONALITY_EVDF = "EVDF"
    
    CONST_PERSONALITY_NUAGE_210_WBX_32_Q = "NUAGE_210_WBX_32_Q"
    
    CONST_ZFB_MATCH_ATTRIBUTE_MAC_ADDRESS = "MAC_ADDRESS"
    
    CONST_FAMILY_NSG_V = "NSG_V"
    
    CONST_VENDOR_NOKIA = "NOKIA"
    
    CONST_VENDOR_CISCO = "CISCO"
    
    CONST_BOOTSTRAP_STATUS_ACTIVE = "ACTIVE"
    
    CONST_FAMILY_NSG_X = "NSG_X"
    
    CONST_ZFB_MATCH_ATTRIBUTE_IP_ADDRESS = "IP_ADDRESS"
    
    CONST_FAMILY_VRS = "VRS"
    
    CONST_FAMILY_NSG_E200 = "NSG_E200"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_SENT = "NOTIFICATION_APP_REQ_SENT"
    
    CONST_PERSONALITY_EVDFB = "EVDFB"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_PERSONALITY_OTHER = "OTHER"
    
    CONST_ZFB_MATCH_ATTRIBUTE_HOSTNAME = "HOSTNAME"
    
    CONST_PERSONALITY_VDFG = "VDFG"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_ACK = "NOTIFICATION_APP_REQ_ACK"
    
    CONST_PERMITTED_ACTION_EXTEND = "EXTEND"
    
    CONST_BOOTSTRAP_STATUS_QUARANTINED = "QUARANTINED"
    
    CONST_PERMITTED_ACTION_INSTANTIATE = "INSTANTIATE"
    
    CONST_PERSONALITY_DC7X50 = "DC7X50"
    
    CONST_BOOTSTRAP_STATUS_CERTIFICATE_SIGNED = "CERTIFICATE_SIGNED"
    
    CONST_FAMILY_NSG_AZ = "NSG_AZ"
    
    CONST_FAMILY_ANY = "ANY"
    
    CONST_ZFB_MATCH_ATTRIBUTE_NONE = "NONE"
    
    CONST_PERSONALITY_VSA = "VSA"
    
    CONST_PERSONALITY_VSG = "VSG"
    
    CONST_PERMITTED_ACTION_READ = "READ"
    
    CONST_PERSONALITY_VRSB = "VRSB"
    
    CONST_PERMITTED_ACTION_USE = "USE"
    
    CONST_PERSONALITY_NETCONF_7X50 = "NETCONF_7X50"
    
    CONST_PERSONALITY_NUAGE_210_WBX_48_S = "NUAGE_210_WBX_48_S"
    
    CONST_FAMILY_NSG_X200 = "NSG_X200"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_FAMILY_NSG_E300 = "NSG_E300"
    
    CONST_PERSONALITY_VRSG = "VRSG"
    
    CONST_ZFB_MATCH_ATTRIBUTE_SERIAL_NUMBER = "SERIAL_NUMBER"
    
    CONST_ZFB_MATCH_ATTRIBUTE_UUID = "UUID"
    
    CONST_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_PERSONALITY_NETCONF_THIRDPARTY_HW_VTEP = "NETCONF_THIRDPARTY_HW_VTEP"
    
    CONST_FAMILY_NSG_AMI = "NSG_AMI"
    
    CONST_PERMITTED_ACTION_DEPLOY = "DEPLOY"
    
    CONST_BOOTSTRAP_STATUS_REVOKED = "REVOKED"
    
    CONST_BOOTSTRAP_STATUS_INACTIVE = "INACTIVE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NetconfGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> netconfgateway = NUNetconfGateway(id=u'xxxx-xxx-xxx-xxx', name=u'NetconfGateway')
                >>> netconfgateway = NUNetconfGateway(data=my_dict)
        """

        super(NUNetconfGateway, self).__init__()

        # Read/Write Attributes
        
        self._mac_address = None
        self._zfb_match_attribute = None
        self._zfb_match_value = None
        self._bios_release_date = None
        self._bios_version = None
        self._cpu_type = None
        self._uuid = None
        self._name = None
        self._family = None
        self._management_id = None
        self._last_updated_by = None
        self._datapath_id = None
        self._patches = None
        self._gateway_connected = None
        self._gateway_model = None
        self._gateway_version = None
        self._redundancy_group_id = None
        self._peer = None
        self._template_id = None
        self._pending = None
        self._vendor = None
        self._serial_number = None
        self._permitted_action = None
        self._personality = None
        self._description = None
        self._libraries = None
        self._embedded_metadata = None
        self._enterprise_id = None
        self._entity_scope = None
        self._location_id = None
        self._bootstrap_id = None
        self._bootstrap_status = None
        self._product_name = None
        self._use_gateway_vlanvnid = None
        self._associated_gateway_security_id = None
        self._associated_gateway_security_profile_id = None
        self._associated_nsg_info_id = None
        self._associated_netconf_profile_id = None
        self._vtep = None
        self._auto_disc_gateway_id = None
        self._external_id = None
        self._system_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_match_attribute", remote_name="ZFBMatchAttribute", attribute_type=str, is_required=False, is_unique=False, choices=[u'HOSTNAME', u'IP_ADDRESS', u'MAC_ADDRESS', u'NONE', u'SERIAL_NUMBER', u'UUID'])
        self.expose_attribute(local_name="zfb_match_value", remote_name="ZFBMatchValue", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_release_date", remote_name="BIOSReleaseDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_version", remote_name="BIOSVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'NSG_AMI', u'NSG_AZ', u'NSG_C', u'NSG_E', u'NSG_E200', u'NSG_E300', u'NSG_V', u'NSG_X', u'NSG_X200', u'VRS'])
        self.expose_attribute(local_name="management_id", remote_name="managementID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_id", remote_name="datapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patches", remote_name="patches", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_connected", remote_name="gatewayConnected", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_model", remote_name="gatewayModel", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_version", remote_name="gatewayVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_group_id", remote_name="redundancyGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer", remote_name="peer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="pending", remote_name="pending", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vendor", remote_name="vendor", attribute_type=str, is_required=False, is_unique=False, choices=[u'CISCO', u'NOKIA'])
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="permitted_action", remote_name="permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC7X50', u'EVDF', u'EVDFB', u'HARDWARE_VTEP', u'NETCONF_7X50', u'NETCONF_THIRDPARTY_HW_VTEP', u'NUAGE_210_WBX_32_Q', u'NUAGE_210_WBX_48_S', u'OTHER', u'VDFG', u'VRSB', u'VRSG', u'VSA', u'VSG'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="libraries", remote_name="libraries", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="location_id", remote_name="locationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_id", remote_name="bootstrapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_status", remote_name="bootstrapStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'CERTIFICATE_SIGNED', u'INACTIVE', u'NOTIFICATION_APP_REQ_ACK', u'NOTIFICATION_APP_REQ_SENT', u'QUARANTINED', u'REVOKED'])
        self.expose_attribute(local_name="product_name", remote_name="productName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="use_gateway_vlanvnid", remote_name="useGatewayVLANVNID", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_security_id", remote_name="associatedGatewaySecurityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_security_profile_id", remote_name="associatedGatewaySecurityProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_nsg_info_id", remote_name="associatedNSGInfoID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_netconf_profile_id", remote_name="associatedNetconfProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vtep", remote_name="vtep", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_disc_gateway_id", remote_name="autoDiscGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.mac_filter_profiles = NUMACFilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.sap_egress_qo_s_profiles = NUSAPEgressQoSProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.sap_ingress_qo_s_profiles = NUSAPIngressQoSProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.gateway_securities = NUGatewaySecuritiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.deployment_failures = NUDeploymentFailuresFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.wan_services = NUWANServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_profiles = NUEgressProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.infrastructure_configs = NUInfrastructureConfigsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_profiles = NUIngressProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.locations = NULocationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstraps = NUBootstrapsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bootstrap_activations = NUBootstrapActivationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ports = NUPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ip_filter_profiles = NUIPFilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ipv6_filter_profiles = NUIPv6FilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC Address of the first interface

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC Address of the first interface

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def zfb_match_attribute(self):
        """ Get zfb_match_attribute value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        return self._zfb_match_attribute

    @zfb_match_attribute.setter
    def zfb_match_attribute(self, value):
        """ Set zfb_match_attribute value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        self._zfb_match_attribute = value

    
    @property
    def zfb_match_value(self):
        """ Get zfb_match_value value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        return self._zfb_match_value

    @zfb_match_value.setter
    def zfb_match_value(self, value):
        """ Set zfb_match_value value.

            Notes:
                The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        self._zfb_match_value = value

    
    @property
    def bios_release_date(self):
        """ Get bios_release_date value.

            Notes:
                Release Date of the BIOS.  The format can vary based on the manufacturer but normally includes year/month/day or year/week details (eg. 01/01/2011 or 2018/06/15 or 2018/22)

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        return self._bios_release_date

    @bios_release_date.setter
    def bios_release_date(self, value):
        """ Set bios_release_date value.

            Notes:
                Release Date of the BIOS.  The format can vary based on the manufacturer but normally includes year/month/day or year/week details (eg. 01/01/2011 or 2018/06/15 or 2018/22)

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        self._bios_release_date = value

    
    @property
    def bios_version(self):
        """ Get bios_version value.

            Notes:
                BIOS Version (eg. 0.5.1)

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        return self._bios_version

    @bios_version.setter
    def bios_version(self, value):
        """ Set bios_version value.

            Notes:
                BIOS Version (eg. 0.5.1)

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        self._bios_version = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                The Processor Type as reported during bootstrapping.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                The Processor Type as reported during bootstrapping.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                UUID of the device

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                UUID of the device

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway

                
        """
        self._name = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                The family type of the gateway based on common characteristics with other members of a particular variation of an NSG hardware or of a virtual deployment.

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The family type of the gateway based on common characteristics with other members of a particular variation of an NSG hardware or of a virtual deployment.

                
        """
        self._family = value

    
    @property
    def management_id(self):
        """ Get management_id value.

            Notes:
                The identifier of this gateway's management interface.

                
                This attribute is named `managementID` in VSD API.
                
        """
        return self._management_id

    @management_id.setter
    def management_id(self, value):
        """ Set management_id value.

            Notes:
                The identifier of this gateway's management interface.

                
                This attribute is named `managementID` in VSD API.
                
        """
        self._management_id = value

    
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
    def datapath_id(self):
        """ Get datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemID which is generated when the instance is created in VSD.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        return self._datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        """ Set datapath_id value.

            Notes:
                Identifier of the Gateway, based on the systemID which is generated when the instance is created in VSD.

                
                This attribute is named `datapathID` in VSD API.
                
        """
        self._datapath_id = value

    
    @property
    def patches(self):
        """ Get patches value.

            Notes:
                Patches that have been installed on the NSG

                
        """
        return self._patches

    @patches.setter
    def patches(self, value):
        """ Set patches value.

            Notes:
                Patches that have been installed on the NSG

                
        """
        self._patches = value

    
    @property
    def gateway_connected(self):
        """ Get gateway_connected value.

            Notes:
                A boolean flag indicating the status of the gateway.

                
                This attribute is named `gatewayConnected` in VSD API.
                
        """
        return self._gateway_connected

    @gateway_connected.setter
    def gateway_connected(self, value):
        """ Set gateway_connected value.

            Notes:
                A boolean flag indicating the status of the gateway.

                
                This attribute is named `gatewayConnected` in VSD API.
                
        """
        self._gateway_connected = value

    
    @property
    def gateway_model(self):
        """ Get gateway_model value.

            Notes:
                The model string of the gateway. Applicable to netconf managed gateways

                
                This attribute is named `gatewayModel` in VSD API.
                
        """
        return self._gateway_model

    @gateway_model.setter
    def gateway_model(self, value):
        """ Set gateway_model value.

            Notes:
                The model string of the gateway. Applicable to netconf managed gateways

                
                This attribute is named `gatewayModel` in VSD API.
                
        """
        self._gateway_model = value

    
    @property
    def gateway_version(self):
        """ Get gateway_version value.

            Notes:
                The Gateway Software Version as reported during bootstrapping.

                
                This attribute is named `gatewayVersion` in VSD API.
                
        """
        return self._gateway_version

    @gateway_version.setter
    def gateway_version(self, value):
        """ Set gateway_version value.

            Notes:
                The Gateway Software Version as reported during bootstrapping.

                
                This attribute is named `gatewayVersion` in VSD API.
                
        """
        self._gateway_version = value

    
    @property
    def redundancy_group_id(self):
        """ Get redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        return self._redundancy_group_id

    @redundancy_group_id.setter
    def redundancy_group_id(self, value):
        """ Set redundancy_group_id value.

            Notes:
                The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

                
                This attribute is named `redundancyGroupID` in VSD API.
                
        """
        self._redundancy_group_id = value

    
    @property
    def peer(self):
        """ Get peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        return self._peer

    @peer.setter
    def peer(self, value):
        """ Set peer value.

            Notes:
                The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

                
        """
        self._peer = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def pending(self):
        """ Get pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        return self._pending

    @pending.setter
    def pending(self, value):
        """ Set pending value.

            Notes:
                Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

                
        """
        self._pending = value

    
    @property
    def vendor(self):
        """ Get vendor value.

            Notes:
                The vendor of the gateway. Applicable to netconf managed gateways

                
        """
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        """ Set vendor value.

            Notes:
                The vendor of the gateway. Applicable to netconf managed gateways

                
        """
        self._vendor = value

    
    @property
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The device's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The device's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
    @property
    def permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    @permitted_action.setter
    def permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway.

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway, cannot be changed after creation.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway, cannot be changed after creation.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Gateway

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Gateway

                
        """
        self._description = value

    
    @property
    def libraries(self):
        """ Get libraries value.

            Notes:
                Versions of monitored libraries currently installed on the Gateway.

                
        """
        return self._libraries

    @libraries.setter
    def libraries(self, value):
        """ Set libraries value.

            Notes:
                Versions of monitored libraries currently installed on the Gateway.

                
        """
        self._libraries = value

    
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
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Gateway. This is a read only attribute

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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
    def location_id(self):
        """ Get location_id value.

            Notes:
                Association to an object which contains location information about this gateway instance.

                
                This attribute is named `locationID` in VSD API.
                
        """
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        """ Set location_id value.

            Notes:
                Association to an object which contains location information about this gateway instance.

                
                This attribute is named `locationID` in VSD API.
                
        """
        self._location_id = value

    
    @property
    def bootstrap_id(self):
        """ Get bootstrap_id value.

            Notes:
                The bootstrap details associated with this Gateway. NOTE: This is a read only property, it can only be set during creation of a gateway.

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        return self._bootstrap_id

    @bootstrap_id.setter
    def bootstrap_id(self, value):
        """ Set bootstrap_id value.

            Notes:
                The bootstrap details associated with this Gateway. NOTE: This is a read only property, it can only be set during creation of a gateway.

                
                This attribute is named `bootstrapID` in VSD API.
                
        """
        self._bootstrap_id = value

    
    @property
    def bootstrap_status(self):
        """ Get bootstrap_status value.

            Notes:
                The bootstrap status of this Gateway. NOTE: This is a read only property.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        return self._bootstrap_status

    @bootstrap_status.setter
    def bootstrap_status(self, value):
        """ Set bootstrap_status value.

            Notes:
                The bootstrap status of this Gateway. NOTE: This is a read only property.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        self._bootstrap_status = value

    
    @property
    def product_name(self):
        """ Get product_name value.

            Notes:
                Product Name as reported during bootstrapping.

                
                This attribute is named `productName` in VSD API.
                
        """
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        """ Set product_name value.

            Notes:
                Product Name as reported during bootstrapping.

                
                This attribute is named `productName` in VSD API.
                
        """
        self._product_name = value

    
    @property
    def use_gateway_vlanvnid(self):
        """ Get use_gateway_vlanvnid value.

            Notes:
                When set, VLAN-VNID mapping must be unique for all the vports of the gateway

                
                This attribute is named `useGatewayVLANVNID` in VSD API.
                
        """
        return self._use_gateway_vlanvnid

    @use_gateway_vlanvnid.setter
    def use_gateway_vlanvnid(self, value):
        """ Set use_gateway_vlanvnid value.

            Notes:
                When set, VLAN-VNID mapping must be unique for all the vports of the gateway

                
                This attribute is named `useGatewayVLANVNID` in VSD API.
                
        """
        self._use_gateway_vlanvnid = value

    
    @property
    def associated_gateway_security_id(self):
        """ Get associated_gateway_security_id value.

            Notes:
                Read only ID of the associated gateway security object.

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        return self._associated_gateway_security_id

    @associated_gateway_security_id.setter
    def associated_gateway_security_id(self, value):
        """ Set associated_gateway_security_id value.

            Notes:
                Read only ID of the associated gateway security object.

                
                This attribute is named `associatedGatewaySecurityID` in VSD API.
                
        """
        self._associated_gateway_security_id = value

    
    @property
    def associated_gateway_security_profile_id(self):
        """ Get associated_gateway_security_profile_id value.

            Notes:
                Readonly Id of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        return self._associated_gateway_security_profile_id

    @associated_gateway_security_profile_id.setter
    def associated_gateway_security_profile_id(self, value):
        """ Set associated_gateway_security_profile_id value.

            Notes:
                Readonly Id of the associated gateway security profile object

                
                This attribute is named `associatedGatewaySecurityProfileID` in VSD API.
                
        """
        self._associated_gateway_security_profile_id = value

    
    @property
    def associated_nsg_info_id(self):
        """ Get associated_nsg_info_id value.

            Notes:
                Read only ID of the associated gateway information object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        return self._associated_nsg_info_id

    @associated_nsg_info_id.setter
    def associated_nsg_info_id(self, value):
        """ Set associated_nsg_info_id value.

            Notes:
                Read only ID of the associated gateway information object

                
                This attribute is named `associatedNSGInfoID` in VSD API.
                
        """
        self._associated_nsg_info_id = value

    
    @property
    def associated_netconf_profile_id(self):
        """ Get associated_netconf_profile_id value.

            Notes:
                UUID of the Netconf Profile associated to this gateway.

                
                This attribute is named `associatedNetconfProfileID` in VSD API.
                
        """
        return self._associated_netconf_profile_id

    @associated_netconf_profile_id.setter
    def associated_netconf_profile_id(self, value):
        """ Set associated_netconf_profile_id value.

            Notes:
                UUID of the Netconf Profile associated to this gateway.

                
                This attribute is named `associatedNetconfProfileID` in VSD API.
                
        """
        self._associated_netconf_profile_id = value

    
    @property
    def vtep(self):
        """ Get vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        return self._vtep

    @vtep.setter
    def vtep(self, value):
        """ Set vtep value.

            Notes:
                Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

                
        """
        self._vtep = value

    
    @property
    def auto_disc_gateway_id(self):
        """ Get auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        return self._auto_disc_gateway_id

    @auto_disc_gateway_id.setter
    def auto_disc_gateway_id(self, value):
        """ Set auto_disc_gateway_id value.

            Notes:
                The Auto Discovered Gateway associated with this Gateway Instance

                
                This attribute is named `autoDiscGatewayID` in VSD API.
                
        """
        self._auto_disc_gateway_id = value

    
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

    
    @property
    def system_id(self):
        """ Get system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                Identifier of the Gateway, cannot be modified after creation

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    