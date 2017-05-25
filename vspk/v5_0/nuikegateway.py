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


from .fetchers import NUIKEGatewayConfigsFetcher


from .fetchers import NUIKESubnetsFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUIKEGateway(NURESTObject):
    """ Represents a IKEGateway in the VSD

        Notes:
            Represents an IKE Gateway
    """

    __rest_name__ = "ikegateway"
    __resource_name__ = "ikegateways"

    
    ## Constants
    
    CONST_IK_EV1_MODE_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_IK_EV1_MODE_MAIN = "MAIN"
    
    CONST_IKE_VERSION_V1 = "V1"
    
    CONST_IK_EV1_MODE_AGGRESSIVE = "AGGRESSIVE"
    
    CONST_IKE_VERSION_V2 = "V2"
    
    

    def __init__(self, **kwargs):
        """ Initializes a IKEGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ikegateway = NUIKEGateway(id=u'xxxx-xxx-xxx-xxx', name=u'IKEGateway')
                >>> ikegateway = NUIKEGateway(data=my_dict)
        """

        super(NUIKEGateway, self).__init__()

        # Read/Write Attributes
        
        self._ike_version = None
        self._ik_ev1_mode = None
        self._ip_address = None
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._associated_enterprise_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="ike_version", remote_name="IKEVersion", attribute_type=str, is_required=False, is_unique=False, choices=[u'V1', u'V2'])
        self.expose_attribute(local_name="ik_ev1_mode", remote_name="IKEv1Mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'AGGRESSIVE', u'MAIN', u'NONE'])
        self.expose_attribute(local_name="ip_address", remote_name="IPAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ike_gateway_configs = NUIKEGatewayConfigsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.ike_subnets = NUIKESubnetsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ike_version(self):
        """ Get ike_version value.

            Notes:
                The IKE Version

                
                This attribute is named `IKEVersion` in VSD API.
                
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, value):
        """ Set ike_version value.

            Notes:
                The IKE Version

                
                This attribute is named `IKEVersion` in VSD API.
                
        """
        self._ike_version = value

    
    @property
    def ik_ev1_mode(self):
        """ Get ik_ev1_mode value.

            Notes:
                Mode for IKEv1

                
                This attribute is named `IKEv1Mode` in VSD API.
                
        """
        return self._ik_ev1_mode

    @ik_ev1_mode.setter
    def ik_ev1_mode(self, value):
        """ Set ik_ev1_mode value.

            Notes:
                Mode for IKEv1

                
                This attribute is named `IKEv1Mode` in VSD API.
                
        """
        self._ik_ev1_mode = value

    
    @property
    def ip_address(self):
        """ Get ip_address value.

            Notes:
                IP Address of the IKEv2 Gateway

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        """ Set ip_address value.

            Notes:
                IP Address of the IKEv2 Gateway

                
                This attribute is named `IPAddress` in VSD API.
                
        """
        self._ip_address = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the IKEv2 Gateway

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the IKEv2 Gateway

                
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
    def description(self):
        """ Get description value.

            Notes:
                Description of the IKEv2 Gateway

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the IKEv2 Gateway

                
        """
        self._description = value

    
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
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
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

    

    