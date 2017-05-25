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


class NUBootstrap(NURESTObject):
    """ Represents a Bootstrap in the VSD

        Notes:
            Gateway bootstrap details.
    """

    __rest_name__ = "bootstrap"
    __resource_name__ = "bootstraps"

    
    ## Constants
    
    CONST_ZFB_MATCH_ATTRIBUTE_NONE = "NONE"
    
    CONST_ZFB_MATCH_ATTRIBUTE_NSGATEWAY_ID = "NSGATEWAY_ID"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_STATUS_NOTIFICATION_APP_REQ_SENT = "NOTIFICATION_APP_REQ_SENT"
    
    CONST_ZFB_MATCH_ATTRIBUTE_HOSTNAME = "HOSTNAME"
    
    CONST_STATUS_INACTIVE = "INACTIVE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ZFB_MATCH_ATTRIBUTE_MAC_ADDRESS = "MAC_ADDRESS"
    
    CONST_ZFB_MATCH_ATTRIBUTE_IP_ADDRESS = "IP_ADDRESS"
    
    CONST_ZFB_MATCH_ATTRIBUTE_SERIAL_NUMBER = "SERIAL_NUMBER"
    
    CONST_STATUS_ACTIVE = "ACTIVE"
    
    CONST_STATUS_NOTIFICATION_APP_REQ_ACK = "NOTIFICATION_APP_REQ_ACK"
    
    CONST_STATUS_CERTIFICATE_SIGNED = "CERTIFICATE_SIGNED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Bootstrap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bootstrap = NUBootstrap(id=u'xxxx-xxx-xxx-xxx', name=u'Bootstrap')
                >>> bootstrap = NUBootstrap(data=my_dict)
        """

        super(NUBootstrap, self).__init__()

        # Read/Write Attributes
        
        self._zfb_info = None
        self._zfb_match_attribute = None
        self._zfb_match_value = None
        self._last_updated_by = None
        self._installer_id = None
        self._entity_scope = None
        self._status = None
        self._external_id = None
        
        self.expose_attribute(local_name="zfb_info", remote_name="ZFBInfo", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zfb_match_attribute", remote_name="ZFBMatchAttribute", attribute_type=str, is_required=False, is_unique=False, choices=[u'HOSTNAME', u'IP_ADDRESS', u'MAC_ADDRESS', u'NONE', u'NSGATEWAY_ID', u'SERIAL_NUMBER'])
        self.expose_attribute(local_name="zfb_match_value", remote_name="ZFBMatchValue", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="installer_id", remote_name="installerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'CERTIFICATE_SIGNED', u'INACTIVE', u'NOTIFICATION_APP_REQ_ACK', u'NOTIFICATION_APP_REQ_SENT'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def zfb_info(self):
        """ Get zfb_info value.

            Notes:
                Base64 Encoded JSON String of NSG ZFB Attribute Value Pairs

                
                This attribute is named `ZFBInfo` in VSD API.
                
        """
        return self._zfb_info

    @zfb_info.setter
    def zfb_info(self, value):
        """ Set zfb_info value.

            Notes:
                Base64 Encoded JSON String of NSG ZFB Attribute Value Pairs

                
                This attribute is named `ZFBInfo` in VSD API.
                
        """
        self._zfb_info = value

    
    @property
    def zfb_match_attribute(self):
        """ Get zfb_match_attribute value.

            Notes:
                Attribute to auto match on

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        return self._zfb_match_attribute

    @zfb_match_attribute.setter
    def zfb_match_attribute(self, value):
        """ Set zfb_match_attribute value.

            Notes:
                Attribute to auto match on

                
                This attribute is named `ZFBMatchAttribute` in VSD API.
                
        """
        self._zfb_match_attribute = value

    
    @property
    def zfb_match_value(self):
        """ Get zfb_match_value value.

            Notes:
                Attribute value to auto match on

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        return self._zfb_match_value

    @zfb_match_value.setter
    def zfb_match_value(self, value):
        """ Set zfb_match_value value.

            Notes:
                Attribute value to auto match on

                
                This attribute is named `ZFBMatchValue` in VSD API.
                
        """
        self._zfb_match_value = value

    
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
    def installer_id(self):
        """ Get installer_id value.

            Notes:
                The Installer ID

                
                This attribute is named `installerID` in VSD API.
                
        """
        return self._installer_id

    @installer_id.setter
    def installer_id(self, value):
        """ Set installer_id value.

            Notes:
                The Installer ID

                
                This attribute is named `installerID` in VSD API.
                
        """
        self._installer_id = value

    
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
    def status(self):
        """ Get status value.

            Notes:
                Bootstrap status.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Bootstrap status.

                
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

    

    