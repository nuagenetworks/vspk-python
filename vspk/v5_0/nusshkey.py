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


class NUSSHKey(NURESTObject):
    """ Represents a SSHKey in the VSD

        Notes:
            SSH (Secure Shell) is used to provide secure remote console access to NSGs deployed in branch locations. When key-based authentication is in use, the SSH keys represent the list of public keys that are authorized to open an SSH connection with the username set at the Access Profile level.
    """

    __rest_name__ = "sshkey"
    __resource_name__ = "sshkeys"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_KEY_TYPE_RSA = "RSA"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SSHKey instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> sshkey = NUSSHKey(id=u'xxxx-xxx-xxx-xxx', name=u'SSHKey')
                >>> sshkey = NUSSHKey(data=my_dict)
        """

        super(NUSSHKey, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._key_type = None
        self._entity_scope = None
        self._public_key = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="key_type", remote_name="keyType", attribute_type=str, is_required=False, is_unique=False, choices=[u'RSA'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="public_key", remote_name="publicKey", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the SSH Key.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the SSH Key.

                
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
                A description of the SSH Key.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the SSH Key.

                
        """
        self._description = value

    
    @property
    def key_type(self):
        """ Get key_type value.

            Notes:
                Type of SSH Key defined. Only RSA supported for now.

                
                This attribute is named `keyType` in VSD API.
                
        """
        return self._key_type

    @key_type.setter
    def key_type(self, value):
        """ Set key_type value.

            Notes:
                Type of SSH Key defined. Only RSA supported for now.

                
                This attribute is named `keyType` in VSD API.
                
        """
        self._key_type = value

    
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
    def public_key(self):
        """ Get public_key value.

            Notes:
                Public Key of a SSH Key Pair.

                
                This attribute is named `publicKey` in VSD API.
                
        """
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        """ Set public_key value.

            Notes:
                Public Key of a SSH Key Pair.

                
                This attribute is named `publicKey` in VSD API.
                
        """
        self._public_key = value

    
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

    

    