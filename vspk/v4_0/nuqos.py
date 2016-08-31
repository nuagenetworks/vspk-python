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


from .fetchers import NUVMsFetcher


from .fetchers import NUContainersFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUQOS(NURESTObject):
    """ Represents a QOS in the VSD

        Notes:
            The object manipulates the QoS parameters attached to a domain, zone, or subnet.
    """

    __rest_name__ = "qos"
    __resource_name__ = "qos"

    
    ## Constants
    
    CONST_SERVICE_CLASS_H = "H"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SERVICE_CLASS_A = "A"
    
    CONST_SERVICE_CLASS_B = "B"
    
    CONST_SERVICE_CLASS_C = "C"
    
    CONST_SERVICE_CLASS_D = "D"
    
    CONST_SERVICE_CLASS_E = "E"
    
    CONST_SERVICE_CLASS_F = "F"
    
    CONST_SERVICE_CLASS_G = "G"
    
    CONST_SERVICE_CLASS_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a QOS instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> qos = NUQOS(id=u'xxxx-xxx-xxx-xxx', name=u'QOS')
                >>> qos = NUQOS(data=my_dict)
        """

        super(NUQOS, self).__init__()

        # Read/Write Attributes
        
        self._fip_committed_burst_size = None
        self._fip_committed_information_rate = None
        self._fip_peak_burst_size = None
        self._fip_peak_information_rate = None
        self._fip_rate_limiting_active = None
        self._bum_committed_burst_size = None
        self._bum_committed_information_rate = None
        self._bum_peak_burst_size = None
        self._bum_peak_information_rate = None
        self._bum_rate_limiting_active = None
        self._name = None
        self._last_updated_by = None
        self._rate_limiting_active = None
        self._active = None
        self._peak = None
        self._service_class = None
        self._description = None
        self._rewrite_forwarding_class = None
        self._entity_scope = None
        self._committed_burst_size = None
        self._committed_information_rate = None
        self._trusted_forwarding_class = None
        self._assoc_qos_id = None
        self._associated_dscp_forwarding_class_table_id = None
        self._associated_dscp_forwarding_class_table_name = None
        self._burst = None
        self._external_id = None
        
        self.expose_attribute(local_name="fip_committed_burst_size", remote_name="FIPCommittedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="fip_committed_information_rate", remote_name="FIPCommittedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="fip_peak_burst_size", remote_name="FIPPeakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="fip_peak_information_rate", remote_name="FIPPeakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="fip_rate_limiting_active", remote_name="FIPRateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bum_committed_burst_size", remote_name="BUMCommittedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bum_committed_information_rate", remote_name="BUMCommittedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bum_peak_burst_size", remote_name="BUMPeakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bum_peak_information_rate", remote_name="BUMPeakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bum_rate_limiting_active", remote_name="BUMRateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rate_limiting_active", remote_name="rateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="active", remote_name="active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peak", remote_name="peak", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_class", remote_name="serviceClass", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rewrite_forwarding_class", remote_name="rewriteForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="committed_burst_size", remote_name="committedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="committed_information_rate", remote_name="committedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="trusted_forwarding_class", remote_name="trustedForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_qos_id", remote_name="assocQosId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_dscp_forwarding_class_table_id", remote_name="associatedDSCPForwardingClassTableID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_dscp_forwarding_class_table_name", remote_name="associatedDSCPForwardingClassTableName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="burst", remote_name="burst", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.containers = NUContainersFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def fip_committed_burst_size(self):
        """ Get fip_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.

                
                This attribute is named `FIPCommittedBurstSize` in VSD API.
                
        """
        return self._fip_committed_burst_size

    @fip_committed_burst_size.setter
    def fip_committed_burst_size(self, value):
        """ Set fip_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.

                
                This attribute is named `FIPCommittedBurstSize` in VSD API.
                
        """
        self._fip_committed_burst_size = value

    
    @property
    def fip_committed_information_rate(self):
        """ Get fip_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for FIP Shaper.

                
                This attribute is named `FIPCommittedInformationRate` in VSD API.
                
        """
        return self._fip_committed_information_rate

    @fip_committed_information_rate.setter
    def fip_committed_information_rate(self, value):
        """ Set fip_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for FIP Shaper.

                
                This attribute is named `FIPCommittedInformationRate` in VSD API.
                
        """
        self._fip_committed_information_rate = value

    
    @property
    def fip_peak_burst_size(self):
        """ Get fip_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.

                
                This attribute is named `FIPPeakBurstSize` in VSD API.
                
        """
        return self._fip_peak_burst_size

    @fip_peak_burst_size.setter
    def fip_peak_burst_size(self, value):
        """ Set fip_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.

                
                This attribute is named `FIPPeakBurstSize` in VSD API.
                
        """
        self._fip_peak_burst_size = value

    
    @property
    def fip_peak_information_rate(self):
        """ Get fip_peak_information_rate value.

            Notes:
                Peak rate setting for FIP rate limiting in Mb/s;

                
                This attribute is named `FIPPeakInformationRate` in VSD API.
                
        """
        return self._fip_peak_information_rate

    @fip_peak_information_rate.setter
    def fip_peak_information_rate(self, value):
        """ Set fip_peak_information_rate value.

            Notes:
                Peak rate setting for FIP rate limiting in Mb/s;

                
                This attribute is named `FIPPeakInformationRate` in VSD API.
                
        """
        self._fip_peak_information_rate = value

    
    @property
    def fip_rate_limiting_active(self):
        """ Get fip_rate_limiting_active value.

            Notes:
                Flag the indicates whether FIP rate limiting is enabled or disabled

                
                This attribute is named `FIPRateLimitingActive` in VSD API.
                
        """
        return self._fip_rate_limiting_active

    @fip_rate_limiting_active.setter
    def fip_rate_limiting_active(self, value):
        """ Set fip_rate_limiting_active value.

            Notes:
                Flag the indicates whether FIP rate limiting is enabled or disabled

                
                This attribute is named `FIPRateLimitingActive` in VSD API.
                
        """
        self._fip_rate_limiting_active = value

    
    @property
    def bum_committed_burst_size(self):
        """ Get bum_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.

                
                This attribute is named `BUMCommittedBurstSize` in VSD API.
                
        """
        return self._bum_committed_burst_size

    @bum_committed_burst_size.setter
    def bum_committed_burst_size(self, value):
        """ Set bum_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.

                
                This attribute is named `BUMCommittedBurstSize` in VSD API.
                
        """
        self._bum_committed_burst_size = value

    
    @property
    def bum_committed_information_rate(self):
        """ Get bum_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for BUM Shaper.

                
                This attribute is named `BUMCommittedInformationRate` in VSD API.
                
        """
        return self._bum_committed_information_rate

    @bum_committed_information_rate.setter
    def bum_committed_information_rate(self, value):
        """ Set bum_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for BUM Shaper.

                
                This attribute is named `BUMCommittedInformationRate` in VSD API.
                
        """
        self._bum_committed_information_rate = value

    
    @property
    def bum_peak_burst_size(self):
        """ Get bum_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).

                
                This attribute is named `BUMPeakBurstSize` in VSD API.
                
        """
        return self._bum_peak_burst_size

    @bum_peak_burst_size.setter
    def bum_peak_burst_size(self, value):
        """ Set bum_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).

                
                This attribute is named `BUMPeakBurstSize` in VSD API.
                
        """
        self._bum_peak_burst_size = value

    
    @property
    def bum_peak_information_rate(self):
        """ Get bum_peak_information_rate value.

            Notes:
                Peak rate setting in Mb/s for Broadcast/Multicast rate limiting 

                
                This attribute is named `BUMPeakInformationRate` in VSD API.
                
        """
        return self._bum_peak_information_rate

    @bum_peak_information_rate.setter
    def bum_peak_information_rate(self, value):
        """ Set bum_peak_information_rate value.

            Notes:
                Peak rate setting in Mb/s for Broadcast/Multicast rate limiting 

                
                This attribute is named `BUMPeakInformationRate` in VSD API.
                
        """
        self._bum_peak_information_rate = value

    
    @property
    def bum_rate_limiting_active(self):
        """ Get bum_rate_limiting_active value.

            Notes:
                Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

                
                This attribute is named `BUMRateLimitingActive` in VSD API.
                
        """
        return self._bum_rate_limiting_active

    @bum_rate_limiting_active.setter
    def bum_rate_limiting_active(self, value):
        """ Set bum_rate_limiting_active value.

            Notes:
                Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

                
                This attribute is named `BUMRateLimitingActive` in VSD API.
                
        """
        self._bum_rate_limiting_active = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name of the QoS object

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name of the QoS object

                
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
    def rate_limiting_active(self):
        """ Get rate_limiting_active value.

            Notes:
                Identifies if rate limiting must be implemented

                
                This attribute is named `rateLimitingActive` in VSD API.
                
        """
        return self._rate_limiting_active

    @rate_limiting_active.setter
    def rate_limiting_active(self, value):
        """ Set rate_limiting_active value.

            Notes:
                Identifies if rate limiting must be implemented

                
                This attribute is named `rateLimitingActive` in VSD API.
                
        """
        self._rate_limiting_active = value

    
    @property
    def active(self):
        """ Get active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        return self._active

    @active.setter
    def active(self, value):
        """ Set active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        self._active = value

    
    @property
    def peak(self):
        """ Get peak value.

            Notes:
                Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        return self._peak

    @peak.setter
    def peak(self, value):
        """ Set peak value.

            Notes:
                Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        self._peak = value

    
    @property
    def service_class(self):
        """ Get service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        return self._service_class

    @service_class.setter
    def service_class(self, value):
        """ Set service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        self._service_class = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the QoS object

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the QoS object

                
        """
        self._description = value

    
    @property
    def rewrite_forwarding_class(self):
        """ Get rewrite_forwarding_class value.

            Notes:
                Specifies if the rewrite flag is set for the QoS policy / template

                
                This attribute is named `rewriteForwardingClass` in VSD API.
                
        """
        return self._rewrite_forwarding_class

    @rewrite_forwarding_class.setter
    def rewrite_forwarding_class(self, value):
        """ Set rewrite_forwarding_class value.

            Notes:
                Specifies if the rewrite flag is set for the QoS policy / template

                
                This attribute is named `rewriteForwardingClass` in VSD API.
                
        """
        self._rewrite_forwarding_class = value

    
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
    def committed_burst_size(self):
        """ Get committed_burst_size value.

            Notes:
                Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.

                
                This attribute is named `committedBurstSize` in VSD API.
                
        """
        return self._committed_burst_size

    @committed_burst_size.setter
    def committed_burst_size(self, value):
        """ Set committed_burst_size value.

            Notes:
                Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.

                
                This attribute is named `committedBurstSize` in VSD API.
                
        """
        self._committed_burst_size = value

    
    @property
    def committed_information_rate(self):
        """ Get committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        return self._committed_information_rate

    @committed_information_rate.setter
    def committed_information_rate(self, value):
        """ Set committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        self._committed_information_rate = value

    
    @property
    def trusted_forwarding_class(self):
        """ Get trusted_forwarding_class value.

            Notes:
                Specifies if the trusted flag is set for the QoS policy / template

                
                This attribute is named `trustedForwardingClass` in VSD API.
                
        """
        return self._trusted_forwarding_class

    @trusted_forwarding_class.setter
    def trusted_forwarding_class(self, value):
        """ Set trusted_forwarding_class value.

            Notes:
                Specifies if the trusted flag is set for the QoS policy / template

                
                This attribute is named `trustedForwardingClass` in VSD API.
                
        """
        self._trusted_forwarding_class = value

    
    @property
    def assoc_qos_id(self):
        """ Get assoc_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocQosId` in VSD API.
                
        """
        return self._assoc_qos_id

    @assoc_qos_id.setter
    def assoc_qos_id(self, value):
        """ Set assoc_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocQosId` in VSD API.
                
        """
        self._assoc_qos_id = value

    
    @property
    def associated_dscp_forwarding_class_table_id(self):
        """ Get associated_dscp_forwarding_class_table_id value.

            Notes:
                ID of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableID` in VSD API.
                
        """
        return self._associated_dscp_forwarding_class_table_id

    @associated_dscp_forwarding_class_table_id.setter
    def associated_dscp_forwarding_class_table_id(self, value):
        """ Set associated_dscp_forwarding_class_table_id value.

            Notes:
                ID of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableID` in VSD API.
                
        """
        self._associated_dscp_forwarding_class_table_id = value

    
    @property
    def associated_dscp_forwarding_class_table_name(self):
        """ Get associated_dscp_forwarding_class_table_name value.

            Notes:
                Name of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableName` in VSD API.
                
        """
        return self._associated_dscp_forwarding_class_table_name

    @associated_dscp_forwarding_class_table_name.setter
    def associated_dscp_forwarding_class_table_name(self, value):
        """ Set associated_dscp_forwarding_class_table_name value.

            Notes:
                Name of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableName` in VSD API.
                
        """
        self._associated_dscp_forwarding_class_table_name = value

    
    @property
    def burst(self):
        """ Get burst value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        return self._burst

    @burst.setter
    def burst(self, value):
        """ Set burst value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        self._burst = value

    
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

    

    