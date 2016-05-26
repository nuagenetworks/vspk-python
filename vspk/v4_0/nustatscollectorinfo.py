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

from bambou import NURESTObject


class NUStatsCollectorInfo(NURESTObject):
    """ Represents a StatsCollectorInfo in the VSD

        Notes:
            Identifies the IP address of the stats collector entity that must be used.
    """

    __rest_name__ = "statisticscollector"
    __resource_name__ = "statisticscollector"

    
    ## Constants
    
    CONST_ADDRESS_TYPE_FQDN = "fqdn"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ADDRESS_TYPE_IP = "ip"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a StatsCollectorInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> statscollectorinfo = NUStatsCollectorInfo(id=u'xxxx-xxx-xxx-xxx', name=u'StatsCollectorInfo')
                >>> statscollectorinfo = NUStatsCollectorInfo(data=my_dict)
        """

        super(NUStatsCollectorInfo, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._address_type = None
        self._entity_scope = None
        self._port = None
        self._ip_address = None
        self._proto_buf_port = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address_type", remote_name="addressType", attribute_type=str, is_required=False, is_unique=False, choices=[u'fqdn', u'ip'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="port", remote_name="port", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ip_address", remote_name="ipAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="proto_buf_port", remote_name="protoBufPort", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def address_type(self):
        """ Get address_type value.

            Notes:
                Type for stats collector address Possible values are ip, fqdn, .

                
                This attribute is named `addressType` in VSD API.
                
        """
        return self._address_type

    @address_type.setter
    def address_type(self, value):
        """ Set address_type value.

            Notes:
                Type for stats collector address Possible values are ip, fqdn, .

                
                This attribute is named `addressType` in VSD API.
                
        """
        self._address_type = value

    
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
    def port(self):
        """ Get port value.

            Notes:
                Port(s) of the stats collector process

                
        """
        return self._port

    @port.setter
    def port(self, value):
        """ Set port value.

            Notes:
                Port(s) of the stats collector process

                
        """
        self._port = value

    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP address(es) of the stats collector process

                
                This attribute is named `ipAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP address(es) of the stats collector process

                
                This attribute is named `ipAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def proto_buf_port(self):
        """ Get proto_buf_port value.

            Notes:
                Protobuf Port(s) of the stats collector process

                
                This attribute is named `protoBufPort` in VSD API.
                
        """
        return self._proto_buf_port

    @proto_buf_port.setter
    def proto_buf_port(self, value):
        """ Set proto_buf_port value.

            Notes:
                Protobuf Port(s) of the stats collector process

                
                This attribute is named `protoBufPort` in VSD API.
                
        """
        self._proto_buf_port = value

    
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

    

    