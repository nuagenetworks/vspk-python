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



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUJobsFetcher

from bambou import NURESTObject


class NUZFBRequest(NURESTObject):
    """ Represents a ZFBRequest in the VSD

        Notes:
            A ZFB Request from an NSG
    """

    __rest_name__ = "zfbrequest"
    __resource_name__ = "zfbrequests"

    
    ## Constants
    
    CONST_ZFB_APPROVAL_STATUS_DENIED = "DENIED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ZFB_APPROVAL_STATUS_UNASSIGNED = "UNASSIGNED"
    
    CONST_ZFB_APPROVAL_STATUS_APPROVED = "APPROVED"
    
    CONST_ZFB_APPROVAL_STATUS_ASSIGNED = "ASSIGNED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ZFBRequest instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> zfbrequest = NUZFBRequest(id=u'xxxx-xxx-xxx-xxx', name=u'ZFBRequest')
                >>> zfbrequest = NUZFBRequest(data=my_dict)
        """

        super(NUZFBRequest, self).__init__()

        # Read/Write Attributes
        
        self._mac_address = None
        self._zfb_approval_status = None
        self._zfb_bootstrap_enabled = None
        self._zfb_info = None
        self._zfb_request_retry_timer = None
        self._sku = None
        self._ip_address = None
        self._cpu_type = None
        self._nsg_version = None
        self._uuid = None
        self._family = None
        self._last_connected_time = None
        self._last_updated_by = None
        self._serial_number = None
        self._entity_scope = None
        self._hostname = None
        self._associated_enterprise_id = None
        self._associated_enterprise_name = None
        self._associated_ns_gateway_id = None
        self._associated_ns_gateway_name = None
        self._status_string = None
        self._external_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_approval_status", remote_name="ZFBApprovalStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'APPROVED', u'ASSIGNED', u'DENIED', u'UNASSIGNED'])
        self.expose_attribute(local_name="zfb_bootstrap_enabled", remote_name="ZFBBootstrapEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_info", remote_name="ZFBInfo", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_request_retry_timer", remote_name="ZFBRequestRetryTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sku", remote_name="SKU", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="NSGVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_connected_time", remote_name="lastConnectedTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="hostname", remote_name="hostname", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_name", remote_name="associatedEnterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_id", remote_name="associatedNSGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_name", remote_name="associatedNSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status_string", remote_name="statusString", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC Address fo the NSG Port1 interface

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC Address fo the NSG Port1 interface

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def zfb_approval_status(self):
        """ Get zfb_approval_status value.

            Notes:
                the status of the request

                
                This attribute is named `ZFBApprovalStatus` in VSD API.
                
        """
        return self._zfb_approval_status

    @zfb_approval_status.setter
    def zfb_approval_status(self, value):
        """ Set zfb_approval_status value.

            Notes:
                the status of the request

                
                This attribute is named `ZFBApprovalStatus` in VSD API.
                
        """
        self._zfb_approval_status = value

    
    @property
    def zfb_bootstrap_enabled(self):
        """ Get zfb_bootstrap_enabled value.

            Notes:
                whether the NSG should bootstrap, or just simulate bootstrap. Set from System Config

                
                This attribute is named `ZFBBootstrapEnabled` in VSD API.
                
        """
        return self._zfb_bootstrap_enabled

    @zfb_bootstrap_enabled.setter
    def zfb_bootstrap_enabled(self, value):
        """ Set zfb_bootstrap_enabled value.

            Notes:
                whether the NSG should bootstrap, or just simulate bootstrap. Set from System Config

                
                This attribute is named `ZFBBootstrapEnabled` in VSD API.
                
        """
        self._zfb_bootstrap_enabled = value

    
    @property
    def zfb_info(self):
        """ Get zfb_info value.

            Notes:
                The Base64 encoded JSON string of ZFB Attributes

                
                This attribute is named `ZFBInfo` in VSD API.
                
        """
        return self._zfb_info

    @zfb_info.setter
    def zfb_info(self, value):
        """ Set zfb_info value.

            Notes:
                The Base64 encoded JSON string of ZFB Attributes

                
                This attribute is named `ZFBInfo` in VSD API.
                
        """
        self._zfb_info = value

    
    @property
    def zfb_request_retry_timer(self):
        """ Get zfb_request_retry_timer value.

            Notes:
                ZFB Request retry timer on NSG. Set from System Config

                
                This attribute is named `ZFBRequestRetryTimer` in VSD API.
                
        """
        return self._zfb_request_retry_timer

    @zfb_request_retry_timer.setter
    def zfb_request_retry_timer(self, value):
        """ Set zfb_request_retry_timer value.

            Notes:
                ZFB Request retry timer on NSG. Set from System Config

                
                This attribute is named `ZFBRequestRetryTimer` in VSD API.
                
        """
        self._zfb_request_retry_timer = value

    
    @property
    def sku(self):
        """ Get sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        return self._sku

    @sku.setter
    def sku(self, value):
        """ Set sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        self._sku = value

    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP Address of the NSG

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP Address of the NSG

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The Nuage NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The Nuage NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        self._nsg_version = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                Redhat UUID

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                Redhat UUID

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                NSG Type

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                NSG Type

                
        """
        self._family = value

    
    @property
    def last_connected_time(self):
        """ Get last_connected_time value.

            Notes:
                the time in which the last GET was made from the NSG

                
                This attribute is named `lastConnectedTime` in VSD API.
                
        """
        return self._last_connected_time

    @last_connected_time.setter
    def last_connected_time(self, value):
        """ Set last_connected_time value.

            Notes:
                the time in which the last GET was made from the NSG

                
                This attribute is named `lastConnectedTime` in VSD API.
                
        """
        self._last_connected_time = value

    
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
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The NSG's Serial Number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The NSG's Serial Number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
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
    def hostname(self):
        """ Get hostname value.

            Notes:
                hostname of the NSG

                
        """
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        """ Set hostname value.

            Notes:
                hostname of the NSG

                
        """
        self._hostname = value

    
    @property
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                the ID of the associated enteprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                the ID of the associated enteprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
    @property
    def associated_enterprise_name(self):
        """ Get associated_enterprise_name value.

            Notes:
                name of the associated Enterprise

                
                This attribute is named `associatedEnterpriseName` in VSD API.
                
        """
        return self._associated_enterprise_name

    @associated_enterprise_name.setter
    def associated_enterprise_name(self, value):
        """ Set associated_enterprise_name value.

            Notes:
                name of the associated Enterprise

                
                This attribute is named `associatedEnterpriseName` in VSD API.
                
        """
        self._associated_enterprise_name = value

    
    @property
    def associated_ns_gateway_id(self):
        """ Get associated_ns_gateway_id value.

            Notes:
                ID of the assigned NSG

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        return self._associated_ns_gateway_id

    @associated_ns_gateway_id.setter
    def associated_ns_gateway_id(self, value):
        """ Set associated_ns_gateway_id value.

            Notes:
                ID of the assigned NSG

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        self._associated_ns_gateway_id = value

    
    @property
    def associated_ns_gateway_name(self):
        """ Get associated_ns_gateway_name value.

            Notes:
                name of the associated NSG

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        return self._associated_ns_gateway_name

    @associated_ns_gateway_name.setter
    def associated_ns_gateway_name(self, value):
        """ Set associated_ns_gateway_name value.

            Notes:
                name of the associated NSG

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        self._associated_ns_gateway_name = value

    
    @property
    def status_string(self):
        """ Get status_string value.

            Notes:
                Extra status info

                
                This attribute is named `statusString` in VSD API.
                
        """
        return self._status_string

    @status_string.setter
    def status_string(self, value):
        """ Set status_string value.

            Notes:
                Extra status info

                
                This attribute is named `statusString` in VSD API.
                
        """
        self._status_string = value

    
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

    

    