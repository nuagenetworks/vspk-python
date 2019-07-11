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


class NUBFDSession(NURESTObject):
    """ Represents a BFDSession in the VSD

        Notes:
            Represents the Bidirectional Forwarding Detection session that can be configured on an uplink/BR connection.
    """

    __rest_name__ = "bfdsession"
    __resource_name__ = "bfdsessions"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_BFD_DESTINATION_IP_TYPE_IPV6 = "IPV6"
    
    CONST_BFD_DESTINATION_IP_TYPE_IPV4 = "IPV4"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a BFDSession instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bfdsession = NUBFDSession(id=u'xxxx-xxx-xxx-xxx', name=u'BFDSession')
                >>> bfdsession = NUBFDSession(data=my_dict)
        """

        super(NUBFDSession, self).__init__()

        # Read/Write Attributes
        
        self._bfd_destination_ip = None
        self._bfd_destination_ip_type = None
        self._bfd_destination_ipv6 = None
        self._bfd_multiplier = None
        self._bfd_timer = None
        self._last_updated_by = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._multi_hop_enabled = None
        self._external_id = None
        
        self.expose_attribute(local_name="bfd_destination_ip", remote_name="BFDDestinationIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bfd_destination_ip_type", remote_name="BFDDestinationIPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="bfd_destination_ipv6", remote_name="BFDDestinationIPv6", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bfd_multiplier", remote_name="BFDMultiplier", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bfd_timer", remote_name="BFDTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="multi_hop_enabled", remote_name="multiHopEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def bfd_destination_ip(self):
        """ Get bfd_destination_ip value.

            Notes:
                Destination IP Address used for Bidirectional Forwarding Detection.

                
                This attribute is named `BFDDestinationIP` in VSD API.
                
        """
        return self._bfd_destination_ip

    @bfd_destination_ip.setter
    def bfd_destination_ip(self, value):
        """ Set bfd_destination_ip value.

            Notes:
                Destination IP Address used for Bidirectional Forwarding Detection.

                
                This attribute is named `BFDDestinationIP` in VSD API.
                
        """
        self._bfd_destination_ip = value

    
    @property
    def bfd_destination_ip_type(self):
        """ Get bfd_destination_ip_type value.

            Notes:
                Destination IP Type of Bidirectional Forwarding Detection

                
                This attribute is named `BFDDestinationIPType` in VSD API.
                
        """
        return self._bfd_destination_ip_type

    @bfd_destination_ip_type.setter
    def bfd_destination_ip_type(self, value):
        """ Set bfd_destination_ip_type value.

            Notes:
                Destination IP Type of Bidirectional Forwarding Detection

                
                This attribute is named `BFDDestinationIPType` in VSD API.
                
        """
        self._bfd_destination_ip_type = value

    
    @property
    def bfd_destination_ipv6(self):
        """ Get bfd_destination_ipv6 value.

            Notes:
                Destination IPv6 Address used for Bidirectional Forwarding Detection. Required if BFD Destination IP Type is IPV6

                
                This attribute is named `BFDDestinationIPv6` in VSD API.
                
        """
        return self._bfd_destination_ipv6

    @bfd_destination_ipv6.setter
    def bfd_destination_ipv6(self, value):
        """ Set bfd_destination_ipv6 value.

            Notes:
                Destination IPv6 Address used for Bidirectional Forwarding Detection. Required if BFD Destination IP Type is IPV6

                
                This attribute is named `BFDDestinationIPv6` in VSD API.
                
        """
        self._bfd_destination_ipv6 = value

    
    @property
    def bfd_multiplier(self):
        """ Get bfd_multiplier value.

            Notes:
                Multiplier used for Bidirectional Forwarding Detection Timer.

                
                This attribute is named `BFDMultiplier` in VSD API.
                
        """
        return self._bfd_multiplier

    @bfd_multiplier.setter
    def bfd_multiplier(self, value):
        """ Set bfd_multiplier value.

            Notes:
                Multiplier used for Bidirectional Forwarding Detection Timer.

                
                This attribute is named `BFDMultiplier` in VSD API.
                
        """
        self._bfd_multiplier = value

    
    @property
    def bfd_timer(self):
        """ Get bfd_timer value.

            Notes:
                Timer for Bidirectional Forwarding Detection in milliseconds.

                
                This attribute is named `BFDTimer` in VSD API.
                
        """
        return self._bfd_timer

    @bfd_timer.setter
    def bfd_timer(self, value):
        """ Set bfd_timer value.

            Notes:
                Timer for Bidirectional Forwarding Detection in milliseconds.

                
                This attribute is named `BFDTimer` in VSD API.
                
        """
        self._bfd_timer = value

    
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
    def multi_hop_enabled(self):
        """ Get multi_hop_enabled value.

            Notes:
                Boolean flag to indicate whether the BFD Session has single hop or multi hop capability.

                
                This attribute is named `multiHopEnabled` in VSD API.
                
        """
        return self._multi_hop_enabled

    @multi_hop_enabled.setter
    def multi_hop_enabled(self, value):
        """ Set multi_hop_enabled value.

            Notes:
                Boolean flag to indicate whether the BFD Session has single hop or multi hop capability.

                
                This attribute is named `multiHopEnabled` in VSD API.
                
        """
        self._multi_hop_enabled = value

    
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

    

    