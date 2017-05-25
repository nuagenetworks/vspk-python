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


class NUVCenterEAMConfig(NURESTObject):
    """ Represents a VCenterEAMConfig in the VSD

        Notes:
            The EAM solution configuration.
    """

    __rest_name__ = "eamconfig"
    __resource_name__ = "eamconfigs"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VCenterEAMConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vcentereamconfig = NUVCenterEAMConfig(id=u'xxxx-xxx-xxx-xxx', name=u'VCenterEAMConfig')
                >>> vcentereamconfig = NUVCenterEAMConfig(data=my_dict)
        """

        super(NUVCenterEAMConfig, self).__init__()

        # Read/Write Attributes
        
        self._eam_server_ip = None
        self._eam_server_port_number = None
        self._eam_server_port_type = None
        self._last_updated_by = None
        self._vib_url = None
        self._entity_scope = None
        self._ovf_url = None
        self._extension_key = None
        self._external_id = None
        
        self.expose_attribute(local_name="eam_server_ip", remote_name="eamServerIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="eam_server_port_number", remote_name="eamServerPortNumber", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="eam_server_port_type", remote_name="eamServerPortType", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vib_url", remote_name="vibURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="ovf_url", remote_name="ovfURL", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="extension_key", remote_name="extensionKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def eam_server_ip(self):
        """ Get eam_server_ip value.

            Notes:
                The EAM server IP

                
                This attribute is named `eamServerIP` in VSD API.
                
        """
        return self._eam_server_ip

    @eam_server_ip.setter
    def eam_server_ip(self, value):
        """ Set eam_server_ip value.

            Notes:
                The EAM server IP

                
                This attribute is named `eamServerIP` in VSD API.
                
        """
        self._eam_server_ip = value

    
    @property
    def eam_server_port_number(self):
        """ Get eam_server_port_number value.

            Notes:
                The EAM server port number

                
                This attribute is named `eamServerPortNumber` in VSD API.
                
        """
        return self._eam_server_port_number

    @eam_server_port_number.setter
    def eam_server_port_number(self, value):
        """ Set eam_server_port_number value.

            Notes:
                The EAM server port number

                
                This attribute is named `eamServerPortNumber` in VSD API.
                
        """
        self._eam_server_port_number = value

    
    @property
    def eam_server_port_type(self):
        """ Get eam_server_port_type value.

            Notes:
                The EAM server port Type

                
                This attribute is named `eamServerPortType` in VSD API.
                
        """
        return self._eam_server_port_type

    @eam_server_port_type.setter
    def eam_server_port_type(self, value):
        """ Set eam_server_port_type value.

            Notes:
                The EAM server port Type

                
                This attribute is named `eamServerPortType` in VSD API.
                
        """
        self._eam_server_port_type = value

    
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
    def vib_url(self):
        """ Get vib_url value.

            Notes:
                The url for the optional vib

                
                This attribute is named `vibURL` in VSD API.
                
        """
        return self._vib_url

    @vib_url.setter
    def vib_url(self, value):
        """ Set vib_url value.

            Notes:
                The url for the optional vib

                
                This attribute is named `vibURL` in VSD API.
                
        """
        self._vib_url = value

    
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
    def ovf_url(self):
        """ Get ovf_url value.

            Notes:
                The url for the ovf

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        return self._ovf_url

    @ovf_url.setter
    def ovf_url(self, value):
        """ Set ovf_url value.

            Notes:
                The url for the ovf

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        self._ovf_url = value

    
    @property
    def extension_key(self):
        """ Get extension_key value.

            Notes:
                Key of the extension that the solution registers

                
                This attribute is named `extensionKey` in VSD API.
                
        """
        return self._extension_key

    @extension_key.setter
    def extension_key(self, value):
        """ Set extension_key value.

            Notes:
                Key of the extension that the solution registers

                
                This attribute is named `extensionKey` in VSD API.
                
        """
        self._extension_key = value

    
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

    

    