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


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUInfrastructureEVDFProfile(NURESTObject):
    """ Represents a InfrastructureEVDFProfile in the VSD

        Notes:
            An Infrastructure eVDF Profile instance contains common parameters used to bootstrap instances of eVDF (encryption enabled virtual distributed firewall).
    """

    __rest_name__ = "infrastructureevdfprofile"
    __resource_name__ = "infrastructureevdfprofiles"

    
    ## Constants
    
    CONST_NUAGE_PLATFORM_KVM = "KVM"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_NUAGE_PLATFORM_KVM_LXC = "KVM_LXC"
    
    CONST_NUAGE_PLATFORM_KVM_K8S = "KVM_K8S"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a InfrastructureEVDFProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> infrastructureevdfprofile = NUInfrastructureEVDFProfile(id=u'xxxx-xxx-xxx-xxx', name=u'InfrastructureEVDFProfile')
                >>> infrastructureevdfprofile = NUInfrastructureEVDFProfile(data=my_dict)
        """

        super(NUInfrastructureEVDFProfile, self).__init__()

        # Read/Write Attributes
        
        self._ntp_server_key = None
        self._ntp_server_key_id = None
        self._name = None
        self._last_updated_by = None
        self._active_controller = None
        self._service_ipv4_subnet = None
        self._description = None
        self._enterprise_id = None
        self._entity_scope = None
        self._proxy_dns_name = None
        self._use_two_factor = None
        self._standby_controller = None
        self._nuage_platform = None
        self._external_id = None
        
        self.expose_attribute(local_name="ntp_server_key", remote_name="NTPServerKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server_key_id", remote_name="NTPServerKeyID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="active_controller", remote_name="activeController", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="service_ipv4_subnet", remote_name="serviceIPv4Subnet", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="proxy_dns_name", remote_name="proxyDNSName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="use_two_factor", remote_name="useTwoFactor", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="standby_controller", remote_name="standbyController", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nuage_platform", remote_name="nuagePlatform", attribute_type=str, is_required=False, is_unique=False, choices=[u'KVM', u'KVM_K8S', u'KVM_LXC'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ntp_server_key(self):
        """ Get ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        return self._ntp_server_key

    @ntp_server_key.setter
    def ntp_server_key(self, value):
        """ Set ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        self._ntp_server_key = value

    
    @property
    def ntp_server_key_id(self):
        """ Get ntp_server_key_id value.

            Notes:
                Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        return self._ntp_server_key_id

    @ntp_server_key_id.setter
    def ntp_server_key_id(self, value):
        """ Set ntp_server_key_id value.

            Notes:
                Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        self._ntp_server_key_id = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the profile instance.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the profile instance.

                
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
    def active_controller(self):
        """ Get active_controller value.

            Notes:
                The IP address of the active Controller (VSC)

                
                This attribute is named `activeController` in VSD API.
                
        """
        return self._active_controller

    @active_controller.setter
    def active_controller(self, value):
        """ Set active_controller value.

            Notes:
                The IP address of the active Controller (VSC)

                
                This attribute is named `activeController` in VSD API.
                
        """
        self._active_controller = value

    
    @property
    def service_ipv4_subnet(self):
        """ Get service_ipv4_subnet value.

            Notes:
                K8 Service IPv4 Subnet

                
                This attribute is named `serviceIPv4Subnet` in VSD API.
                
        """
        return self._service_ipv4_subnet

    @service_ipv4_subnet.setter
    def service_ipv4_subnet(self, value):
        """ Set service_ipv4_subnet value.

            Notes:
                K8 Service IPv4 Subnet

                
                This attribute is named `serviceIPv4Subnet` in VSD API.
                
        """
        self._service_ipv4_subnet = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A brief description of the infrastructure profile.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A brief description of the infrastructure profile.

                
        """
        self._description = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
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
    def proxy_dns_name(self):
        """ Get proxy_dns_name value.

            Notes:
                The DNS name of the proxy device acting as an entry point of eVDF instances to contact VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        return self._proxy_dns_name

    @proxy_dns_name.setter
    def proxy_dns_name(self, value):
        """ Set proxy_dns_name value.

            Notes:
                The DNS name of the proxy device acting as an entry point of eVDF instances to contact VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        self._proxy_dns_name = value

    
    @property
    def use_two_factor(self):
        """ Get use_two_factor value.

            Notes:
                A flag that indicates if two-factor is enabled or not when gateway instances inheriting from this profile are bootstrapped.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        return self._use_two_factor

    @use_two_factor.setter
    def use_two_factor(self, value):
        """ Set use_two_factor value.

            Notes:
                A flag that indicates if two-factor is enabled or not when gateway instances inheriting from this profile are bootstrapped.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        self._use_two_factor = value

    
    @property
    def standby_controller(self):
        """ Get standby_controller value.

            Notes:
                The IP address of the standby Controller (VSC)

                
                This attribute is named `standbyController` in VSD API.
                
        """
        return self._standby_controller

    @standby_controller.setter
    def standby_controller(self, value):
        """ Set standby_controller value.

            Notes:
                The IP address of the standby Controller (VSC)

                
                This attribute is named `standbyController` in VSD API.
                
        """
        self._standby_controller = value

    
    @property
    def nuage_platform(self):
        """ Get nuage_platform value.

            Notes:
                The Hypervisor Platform

                
                This attribute is named `nuagePlatform` in VSD API.
                
        """
        return self._nuage_platform

    @nuage_platform.setter
    def nuage_platform(self, value):
        """ Set nuage_platform value.

            Notes:
                The Hypervisor Platform

                
                This attribute is named `nuagePlatform` in VSD API.
                
        """
        self._nuage_platform = value

    
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

    

    