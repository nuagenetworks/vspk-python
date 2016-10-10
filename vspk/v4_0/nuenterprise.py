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



from .fetchers import NUL2DomainsFetcher


from .fetchers import NUL2DomainTemplatesFetcher


from .fetchers import NUL7applicationsignaturesFetcher


from .fetchers import NURateLimitersFetcher


from .fetchers import NUGatewaysFetcher


from .fetchers import NUGatewayTemplatesFetcher


from .fetchers import NUPATNATPoolsFetcher


from .fetchers import NULDAPConfigurationsFetcher


from .fetchers import NURedundancyGroupsFetcher


from .fetchers import NUPerformanceMonitorsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUMetadataTagsFetcher


from .fetchers import NUNetworkMacroGroupsFetcher


from .fetchers import NUNetworkPerformanceMeasurementsFetcher


from .fetchers import NUKeyServerMonitorsFetcher


from .fetchers import NUZFBRequestsFetcher


from .fetchers import NUBGPProfilesFetcher


from .fetchers import NUEgressQOSPoliciesFetcher


from .fetchers import NUSharedNetworkResourcesFetcher


from .fetchers import NUIKECertificatesFetcher


from .fetchers import NUIKEEncryptionprofilesFetcher


from .fetchers import NUIKEGatewaysFetcher


from .fetchers import NUIKEGatewayProfilesFetcher


from .fetchers import NUIKEPSKsFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUAllAlarmsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUEnterpriseNetworksFetcher


from .fetchers import NUEnterpriseSecuritiesFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUDomainsFetcher


from .fetchers import NUDomainTemplatesFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NURoutingPoliciesFetcher


from .fetchers import NUApplicationsFetcher


from .fetchers import NUApplicationperformancemanagementsFetcher


from .fetchers import NUApplicationServicesFetcher


from .fetchers import NUGroupsFetcher


from .fetchers import NUGroupKeyEncryptionProfilesFetcher


from .fetchers import NUDSCPForwardingClassTablesFetcher


from .fetchers import NUUsersFetcher


from .fetchers import NUNSGatewaysFetcher


from .fetchers import NUNSGatewayTemplatesFetcher


from .fetchers import NUNSRedundantGatewayGroupsFetcher


from .fetchers import NUPublicNetworkMacrosFetcher


from .fetchers import NUMultiCastListsFetcher


from .fetchers import NUAvatarsFetcher


from .fetchers import NUEventLogsFetcher


from .fetchers import NUExternalAppServicesFetcher


from .fetchers import NUExternalServicesFetcher

from bambou import NURESTObject


class NUEnterprise(NURESTObject):
    """ Represents a Enterprise in the VSD

        Notes:
            Definition of the enterprise object. This is the top level object that represents an enterprise.
    """

    __rest_name__ = "enterprise"
    __resource_name__ = "enterprises"

    
    ## Constants
    
    CONST_ENCRYPTION_MANAGEMENT_MODE_MANAGED = "MANAGED"
    
    CONST_AVATAR_TYPE_COMPUTEDURL = "COMPUTEDURL"
    
    CONST_ALLOWED_FORWARDING_CLASSES_NONE = "NONE"
    
    CONST_AVATAR_TYPE_BASE64 = "BASE64"
    
    CONST_ENCRYPTION_MANAGEMENT_MODE_DISABLED = "DISABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ALLOWED_FORWARDING_CLASSES_D = "D"
    
    CONST_ALLOWED_FORWARDING_CLASSES_E = "E"
    
    CONST_ALLOWED_FORWARDING_CLASSES_F = "F"
    
    CONST_ALLOWED_FORWARDING_CLASSES_G = "G"
    
    CONST_AVATAR_TYPE_URL = "URL"
    
    CONST_ALLOWED_FORWARDING_CLASSES_A = "A"
    
    CONST_ALLOWED_FORWARDING_CLASSES_B = "B"
    
    CONST_ALLOWED_FORWARDING_CLASSES_C = "C"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ALLOWED_FORWARDING_CLASSES_H = "H"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Enterprise instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> enterprise = NUEnterprise(id=u'xxxx-xxx-xxx-xxx', name=u'Enterprise')
                >>> enterprise = NUEnterprise(data=my_dict)
        """

        super(NUEnterprise, self).__init__()

        # Read/Write Attributes
        
        self._ldap_authorization_enabled = None
        self._ldap_enabled = None
        self._bgp_enabled = None
        self._dhcp_lease_interval = None
        self._name = None
        self._last_updated_by = None
        self._receive_multi_cast_list_id = None
        self._send_multi_cast_list_id = None
        self._description = None
        self._dictionary_version = None
        self._allow_advanced_qos_configuration = None
        self._allow_gateway_management = None
        self._allow_trusted_forwarding_class = None
        self._allowed_forwarding_classes = None
        self._floating_ips_quota = None
        self._floating_ips_used = None
        self._enable_application_performance_management = None
        self._encryption_management_mode = None
        self._enterprise_profile_id = None
        self._entity_scope = None
        self._local_as = None
        self._associated_enterprise_security_id = None
        self._associated_group_key_encryption_profile_id = None
        self._associated_key_server_monitor_id = None
        self._customer_id = None
        self._avatar_data = None
        self._avatar_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="ldap_authorization_enabled", remote_name="LDAPAuthorizationEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ldap_enabled", remote_name="LDAPEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bgp_enabled", remote_name="BGPEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dhcp_lease_interval", remote_name="DHCPLeaseInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="receive_multi_cast_list_id", remote_name="receiveMultiCastListID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="send_multi_cast_list_id", remote_name="sendMultiCastListID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dictionary_version", remote_name="dictionaryVersion", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_advanced_qos_configuration", remote_name="allowAdvancedQOSConfiguration", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_gateway_management", remote_name="allowGatewayManagement", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allow_trusted_forwarding_class", remote_name="allowTrustedForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_forwarding_classes", remote_name="allowedForwardingClasses", attribute_type=list, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name="floating_ips_quota", remote_name="floatingIPsQuota", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="floating_ips_used", remote_name="floatingIPsUsed", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enable_application_performance_management", remote_name="enableApplicationPerformanceManagement", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption_management_mode", remote_name="encryptionManagementMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'MANAGED'])
        self.expose_attribute(local_name="enterprise_profile_id", remote_name="enterpriseProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="local_as", remote_name="localAS", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_security_id", remote_name="associatedEnterpriseSecurityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_group_key_encryption_profile_id", remote_name="associatedGroupKeyEncryptionProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_key_server_monitor_id", remote_name="associatedKeyServerMonitorID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customer_id", remote_name="customerID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_data", remote_name="avatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="avatar_type", remote_name="avatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.l2_domain_templates = NUL2DomainTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.l7applicationsignatures = NUL7applicationsignaturesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.rate_limiters = NURateLimitersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.gateways = NUGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.gateway_templates = NUGatewayTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ldap_configurations = NULDAPConfigurationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.redundancy_groups = NURedundancyGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.performance_monitors = NUPerformanceMonitorsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadata_tags = NUMetadataTagsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.network_macro_groups = NUNetworkMacroGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.network_performance_measurements = NUNetworkPerformanceMeasurementsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.key_server_monitors = NUKeyServerMonitorsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.zfb_requests = NUZFBRequestsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.bgp_profiles = NUBGPProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_qos_policies = NUEgressQOSPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.shared_network_resources = NUSharedNetworkResourcesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_certificates = NUIKECertificatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_encryptionprofiles = NUIKEEncryptionprofilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_gateways = NUIKEGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_gateway_profiles = NUIKEGatewayProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ikepsks = NUIKEPSKsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.all_alarms = NUAllAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_networks = NUEnterpriseNetworksFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_securities = NUEnterpriseSecuritiesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domain_templates = NUDomainTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.routing_policies = NURoutingPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applications = NUApplicationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.applicationperformancemanagements = NUApplicationperformancemanagementsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.application_services = NUApplicationServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.group_key_encryption_profiles = NUGroupKeyEncryptionProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dscp_forwarding_class_tables = NUDSCPForwardingClassTablesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.users = NUUsersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_gateway_templates = NUNSGatewayTemplatesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ns_redundant_gateway_groups = NUNSRedundantGatewayGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.public_network_macros = NUPublicNetworkMacrosFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.multi_cast_lists = NUMultiCastListsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.avatars = NUAvatarsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.external_app_services = NUExternalAppServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.external_services = NUExternalServicesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ldap_authorization_enabled(self):
        """ Get ldap_authorization_enabled value.

            Notes:
                Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

                
                This attribute is named `LDAPAuthorizationEnabled` in VSD API.
                
        """
        return self._ldap_authorization_enabled

    @ldap_authorization_enabled.setter
    def ldap_authorization_enabled(self, value):
        """ Set ldap_authorization_enabled value.

            Notes:
                Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

                
                This attribute is named `LDAPAuthorizationEnabled` in VSD API.
                
        """
        self._ldap_authorization_enabled = value

    
    @property
    def ldap_enabled(self):
        """ Get ldap_enabled value.

            Notes:
                Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

                
                This attribute is named `LDAPEnabled` in VSD API.
                
        """
        return self._ldap_enabled

    @ldap_enabled.setter
    def ldap_enabled(self, value):
        """ Set ldap_enabled value.

            Notes:
                Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class

                
                This attribute is named `LDAPEnabled` in VSD API.
                
        """
        self._ldap_enabled = value

    
    @property
    def bgp_enabled(self):
        """ Get bgp_enabled value.

            Notes:
                Read only flag to display if BGP is enabled for this enterprise

                
                This attribute is named `BGPEnabled` in VSD API.
                
        """
        return self._bgp_enabled

    @bgp_enabled.setter
    def bgp_enabled(self, value):
        """ Set bgp_enabled value.

            Notes:
                Read only flag to display if BGP is enabled for this enterprise

                
                This attribute is named `BGPEnabled` in VSD API.
                
        """
        self._bgp_enabled = value

    
    @property
    def dhcp_lease_interval(self):
        """ Get dhcp_lease_interval value.

            Notes:
                DHCP Lease Interval (in hrs) to be used by an enterprise.

                
                This attribute is named `DHCPLeaseInterval` in VSD API.
                
        """
        return self._dhcp_lease_interval

    @dhcp_lease_interval.setter
    def dhcp_lease_interval(self, value):
        """ Set dhcp_lease_interval value.

            Notes:
                DHCP Lease Interval (in hrs) to be used by an enterprise.

                
                This attribute is named `DHCPLeaseInterval` in VSD API.
                
        """
        self._dhcp_lease_interval = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
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
    def receive_multi_cast_list_id(self):
        """ Get receive_multi_cast_list_id value.

            Notes:
                Readonly Id of the auto generated receive multicast list associated with this enterprise profile

                
                This attribute is named `receiveMultiCastListID` in VSD API.
                
        """
        return self._receive_multi_cast_list_id

    @receive_multi_cast_list_id.setter
    def receive_multi_cast_list_id(self, value):
        """ Set receive_multi_cast_list_id value.

            Notes:
                Readonly Id of the auto generated receive multicast list associated with this enterprise profile

                
                This attribute is named `receiveMultiCastListID` in VSD API.
                
        """
        self._receive_multi_cast_list_id = value

    
    @property
    def send_multi_cast_list_id(self):
        """ Get send_multi_cast_list_id value.

            Notes:
                Readonly Id of the auto generated send multicast list associated with this enterprise profile

                
                This attribute is named `sendMultiCastListID` in VSD API.
                
        """
        return self._send_multi_cast_list_id

    @send_multi_cast_list_id.setter
    def send_multi_cast_list_id(self, value):
        """ Set send_multi_cast_list_id value.

            Notes:
                Readonly Id of the auto generated send multicast list associated with this enterprise profile

                
                This attribute is named `sendMultiCastListID` in VSD API.
                
        """
        self._send_multi_cast_list_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the enterprise

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the enterprise

                
        """
        self._description = value

    
    @property
    def dictionary_version(self):
        """ Get dictionary_version value.

            Notes:
                L7 Application Type version

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        return self._dictionary_version

    @dictionary_version.setter
    def dictionary_version(self, value):
        """ Set dictionary_version value.

            Notes:
                L7 Application Type version

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        self._dictionary_version = value

    
    @property
    def allow_advanced_qos_configuration(self):
        """ Get allow_advanced_qos_configuration value.

            Notes:
                Controls whether this enterprise has access to advanced QoS settings

                
                This attribute is named `allowAdvancedQOSConfiguration` in VSD API.
                
        """
        return self._allow_advanced_qos_configuration

    @allow_advanced_qos_configuration.setter
    def allow_advanced_qos_configuration(self, value):
        """ Set allow_advanced_qos_configuration value.

            Notes:
                Controls whether this enterprise has access to advanced QoS settings

                
                This attribute is named `allowAdvancedQOSConfiguration` in VSD API.
                
        """
        self._allow_advanced_qos_configuration = value

    
    @property
    def allow_gateway_management(self):
        """ Get allow_gateway_management value.

            Notes:
                This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.

                
                This attribute is named `allowGatewayManagement` in VSD API.
                
        """
        return self._allow_gateway_management

    @allow_gateway_management.setter
    def allow_gateway_management(self, value):
        """ Set allow_gateway_management value.

            Notes:
                This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.

                
                This attribute is named `allowGatewayManagement` in VSD API.
                
        """
        self._allow_gateway_management = value

    
    @property
    def allow_trusted_forwarding_class(self):
        """ Get allow_trusted_forwarding_class value.

            Notes:
                Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

                
                This attribute is named `allowTrustedForwardingClass` in VSD API.
                
        """
        return self._allow_trusted_forwarding_class

    @allow_trusted_forwarding_class.setter
    def allow_trusted_forwarding_class(self, value):
        """ Set allow_trusted_forwarding_class value.

            Notes:
                Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

                
                This attribute is named `allowTrustedForwardingClass` in VSD API.
                
        """
        self._allow_trusted_forwarding_class = value

    
    @property
    def allowed_forwarding_classes(self):
        """ Get allowed_forwarding_classes value.

            Notes:
                Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `allowedForwardingClasses` in VSD API.
                
        """
        return self._allowed_forwarding_classes

    @allowed_forwarding_classes.setter
    def allowed_forwarding_classes(self, value):
        """ Set allowed_forwarding_classes value.

            Notes:
                Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `allowedForwardingClasses` in VSD API.
                
        """
        self._allowed_forwarding_classes = value

    
    @property
    def floating_ips_quota(self):
        """ Get floating_ips_quota value.

            Notes:
                Quota set for the number of floating IPs to be used by an enterprise.

                
                This attribute is named `floatingIPsQuota` in VSD API.
                
        """
        return self._floating_ips_quota

    @floating_ips_quota.setter
    def floating_ips_quota(self, value):
        """ Set floating_ips_quota value.

            Notes:
                Quota set for the number of floating IPs to be used by an enterprise.

                
                This attribute is named `floatingIPsQuota` in VSD API.
                
        """
        self._floating_ips_quota = value

    
    @property
    def floating_ips_used(self):
        """ Get floating_ips_used value.

            Notes:
                Number of floating IPs used by the enterprise from the assigned floatingIPsQuota

                
                This attribute is named `floatingIPsUsed` in VSD API.
                
        """
        return self._floating_ips_used

    @floating_ips_used.setter
    def floating_ips_used(self, value):
        """ Set floating_ips_used value.

            Notes:
                Number of floating IPs used by the enterprise from the assigned floatingIPsQuota

                
                This attribute is named `floatingIPsUsed` in VSD API.
                
        """
        self._floating_ips_used = value

    
    @property
    def enable_application_performance_management(self):
        """ Get enable_application_performance_management value.

            Notes:
                This flag indicates if the DPI can be enabled for this enterpriseenterprise/organization.

                
                This attribute is named `enableApplicationPerformanceManagement` in VSD API.
                
        """
        return self._enable_application_performance_management

    @enable_application_performance_management.setter
    def enable_application_performance_management(self, value):
        """ Set enable_application_performance_management value.

            Notes:
                This flag indicates if the DPI can be enabled for this enterpriseenterprise/organization.

                
                This attribute is named `enableApplicationPerformanceManagement` in VSD API.
                
        """
        self._enable_application_performance_management = value

    
    @property
    def encryption_management_mode(self):
        """ Get encryption_management_mode value.

            Notes:
                Readonly encryption management mode of the associated profile

                
                This attribute is named `encryptionManagementMode` in VSD API.
                
        """
        return self._encryption_management_mode

    @encryption_management_mode.setter
    def encryption_management_mode(self, value):
        """ Set encryption_management_mode value.

            Notes:
                Readonly encryption management mode of the associated profile

                
                This attribute is named `encryptionManagementMode` in VSD API.
                
        """
        self._encryption_management_mode = value

    
    @property
    def enterprise_profile_id(self):
        """ Get enterprise_profile_id value.

            Notes:
                Enterprise profile id for this enterprise

                
                This attribute is named `enterpriseProfileID` in VSD API.
                
        """
        return self._enterprise_profile_id

    @enterprise_profile_id.setter
    def enterprise_profile_id(self, value):
        """ Set enterprise_profile_id value.

            Notes:
                Enterprise profile id for this enterprise

                
                This attribute is named `enterpriseProfileID` in VSD API.
                
        """
        self._enterprise_profile_id = value

    
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
    def local_as(self):
        """ Get local_as value.

            Notes:
                Local autonomous system for the enterprise

                
                This attribute is named `localAS` in VSD API.
                
        """
        return self._local_as

    @local_as.setter
    def local_as(self, value):
        """ Set local_as value.

            Notes:
                Local autonomous system for the enterprise

                
                This attribute is named `localAS` in VSD API.
                
        """
        self._local_as = value

    
    @property
    def associated_enterprise_security_id(self):
        """ Get associated_enterprise_security_id value.

            Notes:
                Readonly Id of the associated group key encryption profile

                
                This attribute is named `associatedEnterpriseSecurityID` in VSD API.
                
        """
        return self._associated_enterprise_security_id

    @associated_enterprise_security_id.setter
    def associated_enterprise_security_id(self, value):
        """ Set associated_enterprise_security_id value.

            Notes:
                Readonly Id of the associated group key encryption profile

                
                This attribute is named `associatedEnterpriseSecurityID` in VSD API.
                
        """
        self._associated_enterprise_security_id = value

    
    @property
    def associated_group_key_encryption_profile_id(self):
        """ Get associated_group_key_encryption_profile_id value.

            Notes:
                Readonly Id of the associated group key encryption profile

                
                This attribute is named `associatedGroupKeyEncryptionProfileID` in VSD API.
                
        """
        return self._associated_group_key_encryption_profile_id

    @associated_group_key_encryption_profile_id.setter
    def associated_group_key_encryption_profile_id(self, value):
        """ Set associated_group_key_encryption_profile_id value.

            Notes:
                Readonly Id of the associated group key encryption profile

                
                This attribute is named `associatedGroupKeyEncryptionProfileID` in VSD API.
                
        """
        self._associated_group_key_encryption_profile_id = value

    
    @property
    def associated_key_server_monitor_id(self):
        """ Get associated_key_server_monitor_id value.

            Notes:
                Readonly Id of the associated keyserver monitor

                
                This attribute is named `associatedKeyServerMonitorID` in VSD API.
                
        """
        return self._associated_key_server_monitor_id

    @associated_key_server_monitor_id.setter
    def associated_key_server_monitor_id(self, value):
        """ Set associated_key_server_monitor_id value.

            Notes:
                Readonly Id of the associated keyserver monitor

                
                This attribute is named `associatedKeyServerMonitorID` in VSD API.
                
        """
        self._associated_key_server_monitor_id = value

    
    @property
    def customer_id(self):
        """ Get customer_id value.

            Notes:
                CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.

                
                This attribute is named `customerID` in VSD API.
                
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        """ Set customer_id value.

            Notes:
                CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.

                
                This attribute is named `customerID` in VSD API.
                
        """
        self._customer_id = value

    
    @property
    def avatar_data(self):
        """ Get avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        return self._avatar_data

    @avatar_data.setter
    def avatar_data(self, value):
        """ Set avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        self._avatar_data = value

    
    @property
    def avatar_type(self):
        """ Get avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        return self._avatar_type

    @avatar_type.setter
    def avatar_type(self, value):
        """ Set avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        self._avatar_type = value

    
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

    

    