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


class NUGroupKeyEncryptionProfile(NURESTObject):
    """ Represents a GroupKeyEncryptionProfile in the VSD

        Notes:
            Represents a Group Key Profile
    """

    __rest_name__ = "groupkeyencryptionprofile"
    __resource_name__ = "groupkeyencryptionprofiles"

    
    ## Constants
    
    CONST_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA512WITHRSA = "SHA512withRSA"
    
    CONST_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA256WITHRSA = "SHA256withRSA"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA1WITHRSA = "SHA1withRSA"
    
    CONST_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA512 = "HMAC_SHA512"
    
    CONST_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_TRIPLE_DES_CBC = "TRIPLE_DES_CBC"
    
    CONST_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA1 = "HMAC_SHA1"
    
    CONST_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA1 = "HMAC_SHA1"
    
    CONST_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA256 = "HMAC_SHA256"
    
    CONST_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA512WITHRSA = "SHA512withRSA"
    
    CONST_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA384 = "HMAC_SHA384"
    
    CONST_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA1WITHRSA = "SHA1withRSA"
    
    CONST_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA384WITHRSA = "SHA384withRSA"
    
    CONST_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA224WITHRSA = "SHA224withRSA"
    
    CONST_TRAFFIC_ENCRYPTION_ALGORITHM_TRIPLE_DES_CBC = "TRIPLE_DES_CBC"
    
    CONST_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"
    
    CONST_SEK_PAYLOAD_ENCRYPTION_ALGORITHM_RSA_1024 = "RSA_1024"
    
    CONST_SEK_PAYLOAD_SIGNING_ALGORITHM_SHA384WITHRSA = "SHA384withRSA"
    
    CONST_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_SHA256 = "HMAC_SHA256"
    
    CONST_TRAFFIC_ENCRYPTION_ALGORITHM_AES_192_CBC = "AES_192_CBC"
    
    CONST_TRAFFIC_ENCRYPTION_ALGORITHM_AES_256_CBC = "AES_256_CBC"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA256WITHRSA = "SHA256withRSA"
    
    CONST_TRAFFIC_ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"
    
    CONST_SEED_PAYLOAD_AUTHENTICATION_ALGORITHM_HMAC_SHA512 = "HMAC_SHA512"
    
    CONST_TRAFFIC_AUTHENTICATION_ALGORITHM_HMAC_MD5 = "HMAC_MD5"
    
    CONST_SEED_PAYLOAD_ENCRYPTION_ALGORITHM_AES_128_CBC = "AES_128_CBC"
    
    CONST_SEED_PAYLOAD_SIGNING_ALGORITHM_SHA224WITHRSA = "SHA224withRSA"
    
    

    def __init__(self, **kwargs):
        """ Initializes a GroupKeyEncryptionProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> groupkeyencryptionprofile = NUGroupKeyEncryptionProfile(id=u'xxxx-xxx-xxx-xxx', name=u'GroupKeyEncryptionProfile')
                >>> groupkeyencryptionprofile = NUGroupKeyEncryptionProfile(data=my_dict)
        """

        super(NUGroupKeyEncryptionProfile, self).__init__()

        # Read/Write Attributes
        
        self._sek_generation_interval = None
        self._sek_lifetime = None
        self._sek_payload_encryption_algorithm = None
        self._sek_payload_encryption_bc_algorithm = None
        self._sek_payload_encryption_key_length = None
        self._sek_payload_signing_algorithm = None
        self._name = None
        self._last_updated_by = None
        self._seed_generation_interval = None
        self._seed_lifetime = None
        self._seed_payload_authentication_algorithm = None
        self._seed_payload_authentication_bc_algorithm = None
        self._seed_payload_authentication_key_length = None
        self._seed_payload_encryption_algorithm = None
        self._seed_payload_encryption_bc_algorithm = None
        self._seed_payload_encryption_key_length = None
        self._seed_payload_signing_algorithm = None
        self._description = None
        self._entity_scope = None
        self._traffic_authentication_algorithm = None
        self._traffic_encryption_algorithm = None
        self._traffic_encryption_key_lifetime = None
        self._associated_enterprise_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="sek_generation_interval", remote_name="SEKGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sek_lifetime", remote_name="SEKLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sek_payload_encryption_algorithm", remote_name="SEKPayloadEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'RSA_1024'])
        self.expose_attribute(local_name="sek_payload_encryption_bc_algorithm", remote_name="SEKPayloadEncryptionBCAlgorithm", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sek_payload_encryption_key_length", remote_name="SEKPayloadEncryptionKeyLength", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sek_payload_signing_algorithm", remote_name="SEKPayloadSigningAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'SHA1withRSA', u'SHA224withRSA', u'SHA256withRSA', u'SHA384withRSA', u'SHA512withRSA'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_generation_interval", remote_name="seedGenerationInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_lifetime", remote_name="seedLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_payload_authentication_algorithm", remote_name="seedPayloadAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA512'])
        self.expose_attribute(local_name="seed_payload_authentication_bc_algorithm", remote_name="seedPayloadAuthenticationBCAlgorithm", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_payload_authentication_key_length", remote_name="seedPayloadAuthenticationKeyLength", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_payload_encryption_algorithm", remote_name="seedPayloadEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES_128_CBC', u'AES_256_CBC', u'TRIPLE_DES_CBC'])
        self.expose_attribute(local_name="seed_payload_encryption_bc_algorithm", remote_name="seedPayloadEncryptionBCAlgorithm", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_payload_encryption_key_length", remote_name="seedPayloadEncryptionKeyLength", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="seed_payload_signing_algorithm", remote_name="seedPayloadSigningAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'SHA1withRSA', u'SHA224withRSA', u'SHA256withRSA', u'SHA384withRSA', u'SHA512withRSA'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="traffic_authentication_algorithm", remote_name="trafficAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_MD5', u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA384', u'HMAC_SHA512'])
        self.expose_attribute(local_name="traffic_encryption_algorithm", remote_name="trafficEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES_128_CBC', u'AES_192_CBC', u'AES_256_CBC', u'TRIPLE_DES_CBC'])
        self.expose_attribute(local_name="traffic_encryption_key_lifetime", remote_name="trafficEncryptionKeyLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def sek_generation_interval(self):
        """ Get sek_generation_interval value.

            Notes:
                Group Key SEK Generation Interval in Seconds. Min=1, Max=86400

                
                This attribute is named `SEKGenerationInterval` in VSD API.
                
        """
        return self._sek_generation_interval

    @sek_generation_interval.setter
    def sek_generation_interval(self, value):
        """ Set sek_generation_interval value.

            Notes:
                Group Key SEK Generation Interval in Seconds. Min=1, Max=86400

                
                This attribute is named `SEKGenerationInterval` in VSD API.
                
        """
        self._sek_generation_interval = value

    
    @property
    def sek_lifetime(self):
        """ Get sek_lifetime value.

            Notes:
                Group Key SEK Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `SEKLifetime` in VSD API.
                
        """
        return self._sek_lifetime

    @sek_lifetime.setter
    def sek_lifetime(self, value):
        """ Set sek_lifetime value.

            Notes:
                Group Key SEK Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `SEKLifetime` in VSD API.
                
        """
        self._sek_lifetime = value

    
    @property
    def sek_payload_encryption_algorithm(self):
        """ Get sek_payload_encryption_algorithm value.

            Notes:
                Group Key SEK Payload Encryption Algorithm.

                
                This attribute is named `SEKPayloadEncryptionAlgorithm` in VSD API.
                
        """
        return self._sek_payload_encryption_algorithm

    @sek_payload_encryption_algorithm.setter
    def sek_payload_encryption_algorithm(self, value):
        """ Set sek_payload_encryption_algorithm value.

            Notes:
                Group Key SEK Payload Encryption Algorithm.

                
                This attribute is named `SEKPayloadEncryptionAlgorithm` in VSD API.
                
        """
        self._sek_payload_encryption_algorithm = value

    
    @property
    def sek_payload_encryption_bc_algorithm(self):
        """ Get sek_payload_encryption_bc_algorithm value.

            Notes:
                Group Key Sek Payload Encryption BC Algorithm (read only)

                
                This attribute is named `SEKPayloadEncryptionBCAlgorithm` in VSD API.
                
        """
        return self._sek_payload_encryption_bc_algorithm

    @sek_payload_encryption_bc_algorithm.setter
    def sek_payload_encryption_bc_algorithm(self, value):
        """ Set sek_payload_encryption_bc_algorithm value.

            Notes:
                Group Key Sek Payload Encryption BC Algorithm (read only)

                
                This attribute is named `SEKPayloadEncryptionBCAlgorithm` in VSD API.
                
        """
        self._sek_payload_encryption_bc_algorithm = value

    
    @property
    def sek_payload_encryption_key_length(self):
        """ Get sek_payload_encryption_key_length value.

            Notes:
                Group Key Sek Payload Encryption Key Length (read only)

                
                This attribute is named `SEKPayloadEncryptionKeyLength` in VSD API.
                
        """
        return self._sek_payload_encryption_key_length

    @sek_payload_encryption_key_length.setter
    def sek_payload_encryption_key_length(self, value):
        """ Set sek_payload_encryption_key_length value.

            Notes:
                Group Key Sek Payload Encryption Key Length (read only)

                
                This attribute is named `SEKPayloadEncryptionKeyLength` in VSD API.
                
        """
        self._sek_payload_encryption_key_length = value

    
    @property
    def sek_payload_signing_algorithm(self):
        """ Get sek_payload_signing_algorithm value.

            Notes:
                Group Key SEK Payload Signature Algorithm.

                
                This attribute is named `SEKPayloadSigningAlgorithm` in VSD API.
                
        """
        return self._sek_payload_signing_algorithm

    @sek_payload_signing_algorithm.setter
    def sek_payload_signing_algorithm(self, value):
        """ Set sek_payload_signing_algorithm value.

            Notes:
                Group Key SEK Payload Signature Algorithm.

                
                This attribute is named `SEKPayloadSigningAlgorithm` in VSD API.
                
        """
        self._sek_payload_signing_algorithm = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Encryption Profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Encryption Profile

                
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
    def seed_generation_interval(self):
        """ Get seed_generation_interval value.

            Notes:
                Group Key SEED Generation Interval in Seconds.

                
                This attribute is named `seedGenerationInterval` in VSD API.
                
        """
        return self._seed_generation_interval

    @seed_generation_interval.setter
    def seed_generation_interval(self, value):
        """ Set seed_generation_interval value.

            Notes:
                Group Key SEED Generation Interval in Seconds.

                
                This attribute is named `seedGenerationInterval` in VSD API.
                
        """
        self._seed_generation_interval = value

    
    @property
    def seed_lifetime(self):
        """ Get seed_lifetime value.

            Notes:
                Group Key SEED Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `seedLifetime` in VSD API.
                
        """
        return self._seed_lifetime

    @seed_lifetime.setter
    def seed_lifetime(self, value):
        """ Set seed_lifetime value.

            Notes:
                Group Key SEED Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `seedLifetime` in VSD API.
                
        """
        self._seed_lifetime = value

    
    @property
    def seed_payload_authentication_algorithm(self):
        """ Get seed_payload_authentication_algorithm value.

            Notes:
                Group Key SEK Payload Signature Algorithm.

                
                This attribute is named `seedPayloadAuthenticationAlgorithm` in VSD API.
                
        """
        return self._seed_payload_authentication_algorithm

    @seed_payload_authentication_algorithm.setter
    def seed_payload_authentication_algorithm(self, value):
        """ Set seed_payload_authentication_algorithm value.

            Notes:
                Group Key SEK Payload Signature Algorithm.

                
                This attribute is named `seedPayloadAuthenticationAlgorithm` in VSD API.
                
        """
        self._seed_payload_authentication_algorithm = value

    
    @property
    def seed_payload_authentication_bc_algorithm(self):
        """ Get seed_payload_authentication_bc_algorithm value.

            Notes:
                Group Key Seed Payload Authentication Algorithm (read only)

                
                This attribute is named `seedPayloadAuthenticationBCAlgorithm` in VSD API.
                
        """
        return self._seed_payload_authentication_bc_algorithm

    @seed_payload_authentication_bc_algorithm.setter
    def seed_payload_authentication_bc_algorithm(self, value):
        """ Set seed_payload_authentication_bc_algorithm value.

            Notes:
                Group Key Seed Payload Authentication Algorithm (read only)

                
                This attribute is named `seedPayloadAuthenticationBCAlgorithm` in VSD API.
                
        """
        self._seed_payload_authentication_bc_algorithm = value

    
    @property
    def seed_payload_authentication_key_length(self):
        """ Get seed_payload_authentication_key_length value.

            Notes:
                Group Key Seed Payload Authentication Key Length  (read only)

                
                This attribute is named `seedPayloadAuthenticationKeyLength` in VSD API.
                
        """
        return self._seed_payload_authentication_key_length

    @seed_payload_authentication_key_length.setter
    def seed_payload_authentication_key_length(self, value):
        """ Set seed_payload_authentication_key_length value.

            Notes:
                Group Key Seed Payload Authentication Key Length  (read only)

                
                This attribute is named `seedPayloadAuthenticationKeyLength` in VSD API.
                
        """
        self._seed_payload_authentication_key_length = value

    
    @property
    def seed_payload_encryption_algorithm(self):
        """ Get seed_payload_encryption_algorithm value.

            Notes:
                Group Key SEED Payload Encryption Algorithm.

                
                This attribute is named `seedPayloadEncryptionAlgorithm` in VSD API.
                
        """
        return self._seed_payload_encryption_algorithm

    @seed_payload_encryption_algorithm.setter
    def seed_payload_encryption_algorithm(self, value):
        """ Set seed_payload_encryption_algorithm value.

            Notes:
                Group Key SEED Payload Encryption Algorithm.

                
                This attribute is named `seedPayloadEncryptionAlgorithm` in VSD API.
                
        """
        self._seed_payload_encryption_algorithm = value

    
    @property
    def seed_payload_encryption_bc_algorithm(self):
        """ Get seed_payload_encryption_bc_algorithm value.

            Notes:
                Group Key Seed Payload Encryption Algorithm (read only)

                
                This attribute is named `seedPayloadEncryptionBCAlgorithm` in VSD API.
                
        """
        return self._seed_payload_encryption_bc_algorithm

    @seed_payload_encryption_bc_algorithm.setter
    def seed_payload_encryption_bc_algorithm(self, value):
        """ Set seed_payload_encryption_bc_algorithm value.

            Notes:
                Group Key Seed Payload Encryption Algorithm (read only)

                
                This attribute is named `seedPayloadEncryptionBCAlgorithm` in VSD API.
                
        """
        self._seed_payload_encryption_bc_algorithm = value

    
    @property
    def seed_payload_encryption_key_length(self):
        """ Get seed_payload_encryption_key_length value.

            Notes:
                Group Key Seed Payload Encryption Key Length (read only)

                
                This attribute is named `seedPayloadEncryptionKeyLength` in VSD API.
                
        """
        return self._seed_payload_encryption_key_length

    @seed_payload_encryption_key_length.setter
    def seed_payload_encryption_key_length(self, value):
        """ Set seed_payload_encryption_key_length value.

            Notes:
                Group Key Seed Payload Encryption Key Length (read only)

                
                This attribute is named `seedPayloadEncryptionKeyLength` in VSD API.
                
        """
        self._seed_payload_encryption_key_length = value

    
    @property
    def seed_payload_signing_algorithm(self):
        """ Get seed_payload_signing_algorithm value.

            Notes:
                Group Key Seed Payload Signature Algorithm.

                
                This attribute is named `seedPayloadSigningAlgorithm` in VSD API.
                
        """
        return self._seed_payload_signing_algorithm

    @seed_payload_signing_algorithm.setter
    def seed_payload_signing_algorithm(self, value):
        """ Set seed_payload_signing_algorithm value.

            Notes:
                Group Key Seed Payload Signature Algorithm.

                
                This attribute is named `seedPayloadSigningAlgorithm` in VSD API.
                
        """
        self._seed_payload_signing_algorithm = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Profile instance created.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Profile instance created.

                
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
    def traffic_authentication_algorithm(self):
        """ Get traffic_authentication_algorithm value.

            Notes:
                Group Key traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .

                
                This attribute is named `trafficAuthenticationAlgorithm` in VSD API.
                
        """
        return self._traffic_authentication_algorithm

    @traffic_authentication_algorithm.setter
    def traffic_authentication_algorithm(self, value):
        """ Set traffic_authentication_algorithm value.

            Notes:
                Group Key traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .

                
                This attribute is named `trafficAuthenticationAlgorithm` in VSD API.
                
        """
        self._traffic_authentication_algorithm = value

    
    @property
    def traffic_encryption_algorithm(self):
        """ Get traffic_encryption_algorithm value.

            Notes:
                Group Key traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

                
                This attribute is named `trafficEncryptionAlgorithm` in VSD API.
                
        """
        return self._traffic_encryption_algorithm

    @traffic_encryption_algorithm.setter
    def traffic_encryption_algorithm(self, value):
        """ Set traffic_encryption_algorithm value.

            Notes:
                Group Key traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

                
                This attribute is named `trafficEncryptionAlgorithm` in VSD API.
                
        """
        self._traffic_encryption_algorithm = value

    
    @property
    def traffic_encryption_key_lifetime(self):
        """ Get traffic_encryption_key_lifetime value.

            Notes:
                Group Key Traffic Encryption Key Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `trafficEncryptionKeyLifetime` in VSD API.
                
        """
        return self._traffic_encryption_key_lifetime

    @traffic_encryption_key_lifetime.setter
    def traffic_encryption_key_lifetime(self, value):
        """ Set traffic_encryption_key_lifetime value.

            Notes:
                Group Key Traffic Encryption Key Lifetime in Seconds. Min=1, Max=86400

                
                This attribute is named `trafficEncryptionKeyLifetime` in VSD API.
                
        """
        self._traffic_encryption_key_lifetime = value

    
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

    

    