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


class NUBootstrapActivation(NURESTObject):
    """ Represents a BootstrapActivation in the VSD

        Notes:
            NSG Gateway initiated Bootstrap Activation
    """

    __rest_name__ = "bootstrapactivation"
    __resource_name__ = "bootstrapactivations"

    
    ## Constants
    
    CONST_ACTION_ROLLBACK = "ROLLBACK"
    
    CONST_ACTION_INITIATE = "INITIATE"
    
    CONST_ACTION_NO_AUTH_REQUIRED = "NO_AUTH_REQUIRED"
    
    CONST_ACTION_AUTHENTICATE = "AUTHENTICATE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ACTION_NEW_NCPE_AUTH_REQUIRED = "NEW_NCPE_AUTH_REQUIRED"
    
    CONST_ACTION_UNSPECIFIED = "UNSPECIFIED"
    
    CONST_ACTION_INITIATE_RENEW = "INITIATE_RENEW"
    
    CONST_ACTION_CERTIFICATE_SIGNED = "CERTIFICATE_SIGNED"
    
    CONST_ACTION_ROLLED_BACK = "ROLLED_BACK"
    
    CONST_ACTION_CERTIFICATE_REVOKE = "CERTIFICATE_REVOKE"
    
    CONST_ACTION_BOOTSTRAP_COMPLETE = "BOOTSTRAP_COMPLETE"
    
    CONST_ACTION_CONFIRM = "CONFIRM"
    
    CONST_ACTION_CERTIFICATE_RENEW = "CERTIFICATE_RENEW"
    
    

    def __init__(self, **kwargs):
        """ Initializes a BootstrapActivation instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bootstrapactivation = NUBootstrapActivation(id=u'xxxx-xxx-xxx-xxx', name=u'BootstrapActivation')
                >>> bootstrapactivation = NUBootstrapActivation(data=my_dict)
        """

        super(NUBootstrapActivation, self).__init__()

        # Read/Write Attributes
        
        self._cacert = None
        self._hash = None
        self._last_updated_by = None
        self._action = None
        self._seed = None
        self._cert = None
        self._entity_scope = None
        self._config_url = None
        self._tpm_owner_password = None
        self._srk_password = None
        self._vsd_time = None
        self._csr = None
        self._status = None
        self._external_id = None
        
        self.expose_attribute(local_name="cacert", remote_name="cacert", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hash", remote_name="hash", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="action", remote_name="action", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTHENTICATE', u'BOOTSTRAP_COMPLETE', u'CERTIFICATE_RENEW', u'CERTIFICATE_REVOKE', u'CERTIFICATE_SIGNED', u'CONFIRM', u'INITIATE', u'INITIATE_RENEW', u'NEW_NCPE_AUTH_REQUIRED', u'NO_AUTH_REQUIRED', u'ROLLBACK', u'ROLLED_BACK', u'UNSPECIFIED'])
        self.expose_attribute(local_name="seed", remote_name="seed", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cert", remote_name="cert", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="config_url", remote_name="configURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_owner_password", remote_name="tpmOwnerPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="srk_password", remote_name="srkPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vsd_time", remote_name="vsdTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="csr", remote_name="csr", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def cacert(self):
        """ Get cacert value.

            Notes:
                The CA Certificate Chain

                
        """
        return self._cacert

    @cacert.setter
    def cacert(self, value):
        """ Set cacert value.

            Notes:
                The CA Certificate Chain

                
        """
        self._cacert = value

    
    @property
    def hash(self):
        """ Get hash value.

            Notes:
                The authentication hash of this request

                
        """
        return self._hash

    @hash.setter
    def hash(self, value):
        """ Set hash value.

            Notes:
                The authentication hash of this request

                
        """
        self._hash = value

    
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
    def action(self):
        """ Get action value.

            Notes:
                The bootstrap action to perform.

                
        """
        return self._action

    @action.setter
    def action(self, value):
        """ Set action value.

            Notes:
                The bootstrap action to perform.

                
        """
        self._action = value

    
    @property
    def seed(self):
        """ Get seed value.

            Notes:
                The random seed for this request

                
        """
        return self._seed

    @seed.setter
    def seed(self, value):
        """ Set seed value.

            Notes:
                The random seed for this request

                
        """
        self._seed = value

    
    @property
    def cert(self):
        """ Get cert value.

            Notes:
                The signed Certificate

                
        """
        return self._cert

    @cert.setter
    def cert(self, value):
        """ Set cert value.

            Notes:
                The signed Certificate

                
        """
        self._cert = value

    
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
    def config_url(self):
        """ Get config_url value.

            Notes:
                The configuration URL

                
                This attribute is named `configURL` in VSD API.
                
        """
        return self._config_url

    @config_url.setter
    def config_url(self, value):
        """ Set config_url value.

            Notes:
                The configuration URL

                
                This attribute is named `configURL` in VSD API.
                
        """
        self._config_url = value

    
    @property
    def tpm_owner_password(self):
        """ Get tpm_owner_password value.

            Notes:
                TPM owner passphrase

                
                This attribute is named `tpmOwnerPassword` in VSD API.
                
        """
        return self._tpm_owner_password

    @tpm_owner_password.setter
    def tpm_owner_password(self, value):
        """ Set tpm_owner_password value.

            Notes:
                TPM owner passphrase

                
                This attribute is named `tpmOwnerPassword` in VSD API.
                
        """
        self._tpm_owner_password = value

    
    @property
    def srk_password(self):
        """ Get srk_password value.

            Notes:
                TPM SRK passphrase

                
                This attribute is named `srkPassword` in VSD API.
                
        """
        return self._srk_password

    @srk_password.setter
    def srk_password(self, value):
        """ Set srk_password value.

            Notes:
                TPM SRK passphrase

                
                This attribute is named `srkPassword` in VSD API.
                
        """
        self._srk_password = value

    
    @property
    def vsd_time(self):
        """ Get vsd_time value.

            Notes:
                VSD Server time when an NSG is initiating a Bootstrapping request

                
                This attribute is named `vsdTime` in VSD API.
                
        """
        return self._vsd_time

    @vsd_time.setter
    def vsd_time(self, value):
        """ Set vsd_time value.

            Notes:
                VSD Server time when an NSG is initiating a Bootstrapping request

                
                This attribute is named `vsdTime` in VSD API.
                
        """
        self._vsd_time = value

    
    @property
    def csr(self):
        """ Get csr value.

            Notes:
                The CSR of the request

                
        """
        return self._csr

    @csr.setter
    def csr(self, value):
        """ Set csr value.

            Notes:
                The CSR of the request

                
        """
        self._csr = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                The agent status for the request

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                The agent status for the request

                
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

    

    