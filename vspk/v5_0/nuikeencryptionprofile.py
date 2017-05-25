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


class NUIKEEncryptionprofile(NURESTObject):
    """ Represents a IKEEncryptionprofile in the VSD

        Notes:
            Represents an IKE Profile
    """

    __rest_name__ = "ikeencryptionprofile"
    __resource_name__ = "ikeencryptionprofiles"

    
    ## Constants
    
    CONST_IPSEC_ENCRYPTION_ALGORITHM_AES128 = "AES128"
    
    CONST_ISAKMP_HASH_ALGORITHM_SHA1 = "SHA1"
    
    CONST_ISAKMP_ENCRYPTION_ALGORITHM_AES128 = "AES128"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_2_1024_BIT_DH = "GROUP_2_1024_BIT_DH"
    
    CONST_DPD_MODE_REPLY_ONLY = "REPLY_ONLY"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_15_3072_BIT_DH = "GROUP_15_3072_BIT_DH"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_DPD_MODE_ON_DEMAND = "ON_DEMAND"
    
    CONST_ISAKMP_HASH_ALGORITHM_SHA256 = "SHA256"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_64 = "WINDOW_SIZE_64"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_128 = "WINDOW_SIZE_128"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_17_6144_BIT_DH = "GROUP_17_6144_BIT_DH"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_16_4096_BIT_DH = "GROUP_16_4096_BIT_DH"
    
    CONST_IPSEC_AUTHENTICATION_ALGORITHM_HMAC_SHA512 = "HMAC_SHA512"
    
    CONST_IPSEC_AUTHENTICATION_ALGORITHM_HMAC_SHA1 = "HMAC_SHA1"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_0 = "WINDOW_SIZE_0"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_1_768_BIT_DH = "GROUP_1_768_BIT_DH"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_18_8192_BIT_DH = "GROUP_18_8192_BIT_DH"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_1024 = "WINDOW_SIZE_1024"
    
    CONST_ISAKMP_AUTHENTICATION_MODE_PRE_SHARED_KEY = "PRE_SHARED_KEY"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_32 = "WINDOW_SIZE_32"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_256 = "WINDOW_SIZE_256"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_14_2048_BIT_DH = "GROUP_14_2048_BIT_DH"
    
    CONST_IPSEC_ENCRYPTION_ALGORITHM_TRIPLE_DES = "TRIPLE_DES"
    
    CONST_IPSEC_AUTHENTICATION_ALGORITHM_HMAC_SHA256 = "HMAC_SHA256"
    
    CONST_ISAKMP_ENCRYPTION_ALGORITHM_AES256 = "AES256"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_IPSEC_ENCRYPTION_ALGORITHM_AES256 = "AES256"
    
    CONST_IPSEC_ENCRYPTION_ALGORITHM_AES192 = "AES192"
    
    CONST_ISAKMP_ENCRYPTION_ALGORITHM_AES192 = "AES192"
    
    CONST_ISAKMP_ENCRYPTION_ALGORITHM_TRIPLE_DES = "TRIPLE_DES"
    
    CONST_ISAKMP_DIFFIE_HELMAN_GROUP_IDENTIFIER_GROUP_5_1536_BIT_DH = "GROUP_5_1536_BIT_DH"
    
    CONST_IPSEC_SA_REPLAY_WINDOW_SIZE_WINDOW_SIZE_512 = "WINDOW_SIZE_512"
    
    

    def __init__(self, **kwargs):
        """ Initializes a IKEEncryptionprofile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ikeencryptionprofile = NUIKEEncryptionprofile(id=u'xxxx-xxx-xxx-xxx', name=u'IKEEncryptionprofile')
                >>> ikeencryptionprofile = NUIKEEncryptionprofile(data=my_dict)
        """

        super(NUIKEEncryptionprofile, self).__init__()

        # Read/Write Attributes
        
        self._dpd_interval = None
        self._dpd_mode = None
        self._dpd_timeout = None
        self._ipsec_authentication_algorithm = None
        self._ipsec_dont_fragment = None
        self._ipsec_enable_pfs = None
        self._ipsec_encryption_algorithm = None
        self._ipsec_pre_fragment = None
        self._ipsec_sa_lifetime = None
        self._ipsec_sa_replay_window_size = None
        self._isakmp_authentication_mode = None
        self._isakmp_diffie_helman_group_identifier = None
        self._isakmp_encryption_algorithm = None
        self._isakmp_encryption_key_lifetime = None
        self._isakmp_hash_algorithm = None
        self._name = None
        self._last_updated_by = None
        self._sequence = None
        self._description = None
        self._entity_scope = None
        self._associated_enterprise_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="dpd_interval", remote_name="DPDInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dpd_mode", remote_name="DPDMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'ON_DEMAND', u'REPLY_ONLY'])
        self.expose_attribute(local_name="dpd_timeout", remote_name="DPDTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipsec_authentication_algorithm", remote_name="IPsecAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA512'])
        self.expose_attribute(local_name="ipsec_dont_fragment", remote_name="IPsecDontFragment", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipsec_enable_pfs", remote_name="IPsecEnablePFS", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipsec_encryption_algorithm", remote_name="IPsecEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES128', u'AES192', u'AES256', u'TRIPLE_DES'])
        self.expose_attribute(local_name="ipsec_pre_fragment", remote_name="IPsecPreFragment", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipsec_sa_lifetime", remote_name="IPsecSALifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ipsec_sa_replay_window_size", remote_name="IPsecSAReplayWindowSize", attribute_type=str, is_required=False, is_unique=False, choices=[u'WINDOW_SIZE_0', u'WINDOW_SIZE_1024', u'WINDOW_SIZE_128', u'WINDOW_SIZE_256', u'WINDOW_SIZE_32', u'WINDOW_SIZE_512', u'WINDOW_SIZE_64'])
        self.expose_attribute(local_name="isakmp_authentication_mode", remote_name="ISAKMPAuthenticationMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRE_SHARED_KEY'])
        self.expose_attribute(local_name="isakmp_diffie_helman_group_identifier", remote_name="ISAKMPDiffieHelmanGroupIdentifier", attribute_type=str, is_required=False, is_unique=False, choices=[u'GROUP_14_2048_BIT_DH', u'GROUP_15_3072_BIT_DH', u'GROUP_16_4096_BIT_DH', u'GROUP_17_6144_BIT_DH', u'GROUP_18_8192_BIT_DH', u'GROUP_1_768_BIT_DH', u'GROUP_2_1024_BIT_DH', u'GROUP_5_1536_BIT_DH'])
        self.expose_attribute(local_name="isakmp_encryption_algorithm", remote_name="ISAKMPEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES128', u'AES192', u'AES256', u'TRIPLE_DES'])
        self.expose_attribute(local_name="isakmp_encryption_key_lifetime", remote_name="ISAKMPEncryptionKeyLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="isakmp_hash_algorithm", remote_name="ISAKMPHashAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'SHA1', u'SHA256'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sequence", remote_name="sequence", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dpd_interval(self):
        """ Get dpd_interval value.

            Notes:
                ISAKMP Keep Alive Interval.

                
                This attribute is named `DPDInterval` in VSD API.
                
        """
        return self._dpd_interval

    @dpd_interval.setter
    def dpd_interval(self, value):
        """ Set dpd_interval value.

            Notes:
                ISAKMP Keep Alive Interval.

                
                This attribute is named `DPDInterval` in VSD API.
                
        """
        self._dpd_interval = value

    
    @property
    def dpd_mode(self):
        """ Get dpd_mode value.

            Notes:
                DPD Mode.

                
                This attribute is named `DPDMode` in VSD API.
                
        """
        return self._dpd_mode

    @dpd_mode.setter
    def dpd_mode(self, value):
        """ Set dpd_mode value.

            Notes:
                DPD Mode.

                
                This attribute is named `DPDMode` in VSD API.
                
        """
        self._dpd_mode = value

    
    @property
    def dpd_timeout(self):
        """ Get dpd_timeout value.

            Notes:
                DPD Timeout.

                
                This attribute is named `DPDTimeout` in VSD API.
                
        """
        return self._dpd_timeout

    @dpd_timeout.setter
    def dpd_timeout(self, value):
        """ Set dpd_timeout value.

            Notes:
                DPD Timeout.

                
                This attribute is named `DPDTimeout` in VSD API.
                
        """
        self._dpd_timeout = value

    
    @property
    def ipsec_authentication_algorithm(self):
        """ Get ipsec_authentication_algorithm value.

            Notes:
                IPsec Authentication Algorithm.

                
                This attribute is named `IPsecAuthenticationAlgorithm` in VSD API.
                
        """
        return self._ipsec_authentication_algorithm

    @ipsec_authentication_algorithm.setter
    def ipsec_authentication_algorithm(self, value):
        """ Set ipsec_authentication_algorithm value.

            Notes:
                IPsec Authentication Algorithm.

                
                This attribute is named `IPsecAuthenticationAlgorithm` in VSD API.
                
        """
        self._ipsec_authentication_algorithm = value

    
    @property
    def ipsec_dont_fragment(self):
        """ Get ipsec_dont_fragment value.

            Notes:
                IPsec Don't Fragment

                
                This attribute is named `IPsecDontFragment` in VSD API.
                
        """
        return self._ipsec_dont_fragment

    @ipsec_dont_fragment.setter
    def ipsec_dont_fragment(self, value):
        """ Set ipsec_dont_fragment value.

            Notes:
                IPsec Don't Fragment

                
                This attribute is named `IPsecDontFragment` in VSD API.
                
        """
        self._ipsec_dont_fragment = value

    
    @property
    def ipsec_enable_pfs(self):
        """ Get ipsec_enable_pfs value.

            Notes:
                IPsec Enable PFS

                
                This attribute is named `IPsecEnablePFS` in VSD API.
                
        """
        return self._ipsec_enable_pfs

    @ipsec_enable_pfs.setter
    def ipsec_enable_pfs(self, value):
        """ Set ipsec_enable_pfs value.

            Notes:
                IPsec Enable PFS

                
                This attribute is named `IPsecEnablePFS` in VSD API.
                
        """
        self._ipsec_enable_pfs = value

    
    @property
    def ipsec_encryption_algorithm(self):
        """ Get ipsec_encryption_algorithm value.

            Notes:
                IPsec Encryption Algorithm.

                
                This attribute is named `IPsecEncryptionAlgorithm` in VSD API.
                
        """
        return self._ipsec_encryption_algorithm

    @ipsec_encryption_algorithm.setter
    def ipsec_encryption_algorithm(self, value):
        """ Set ipsec_encryption_algorithm value.

            Notes:
                IPsec Encryption Algorithm.

                
                This attribute is named `IPsecEncryptionAlgorithm` in VSD API.
                
        """
        self._ipsec_encryption_algorithm = value

    
    @property
    def ipsec_pre_fragment(self):
        """ Get ipsec_pre_fragment value.

            Notes:
                IPsec PreFragment

                
                This attribute is named `IPsecPreFragment` in VSD API.
                
        """
        return self._ipsec_pre_fragment

    @ipsec_pre_fragment.setter
    def ipsec_pre_fragment(self, value):
        """ Set ipsec_pre_fragment value.

            Notes:
                IPsec PreFragment

                
                This attribute is named `IPsecPreFragment` in VSD API.
                
        """
        self._ipsec_pre_fragment = value

    
    @property
    def ipsec_sa_lifetime(self):
        """ Get ipsec_sa_lifetime value.

            Notes:
                IPsec SA Lifetime in Seconds.

                
                This attribute is named `IPsecSALifetime` in VSD API.
                
        """
        return self._ipsec_sa_lifetime

    @ipsec_sa_lifetime.setter
    def ipsec_sa_lifetime(self, value):
        """ Set ipsec_sa_lifetime value.

            Notes:
                IPsec SA Lifetime in Seconds.

                
                This attribute is named `IPsecSALifetime` in VSD API.
                
        """
        self._ipsec_sa_lifetime = value

    
    @property
    def ipsec_sa_replay_window_size(self):
        """ Get ipsec_sa_replay_window_size value.

            Notes:
                IPsec Replay Window Size in Packets.

                
                This attribute is named `IPsecSAReplayWindowSize` in VSD API.
                
        """
        return self._ipsec_sa_replay_window_size

    @ipsec_sa_replay_window_size.setter
    def ipsec_sa_replay_window_size(self, value):
        """ Set ipsec_sa_replay_window_size value.

            Notes:
                IPsec Replay Window Size in Packets.

                
                This attribute is named `IPsecSAReplayWindowSize` in VSD API.
                
        """
        self._ipsec_sa_replay_window_size = value

    
    @property
    def isakmp_authentication_mode(self):
        """ Get isakmp_authentication_mode value.

            Notes:
                ISAKMP Authentication Algorithm.

                
                This attribute is named `ISAKMPAuthenticationMode` in VSD API.
                
        """
        return self._isakmp_authentication_mode

    @isakmp_authentication_mode.setter
    def isakmp_authentication_mode(self, value):
        """ Set isakmp_authentication_mode value.

            Notes:
                ISAKMP Authentication Algorithm.

                
                This attribute is named `ISAKMPAuthenticationMode` in VSD API.
                
        """
        self._isakmp_authentication_mode = value

    
    @property
    def isakmp_diffie_helman_group_identifier(self):
        """ Get isakmp_diffie_helman_group_identifier value.

            Notes:
                ISAKMP Diffie-Helman Group Identifier.

                
                This attribute is named `ISAKMPDiffieHelmanGroupIdentifier` in VSD API.
                
        """
        return self._isakmp_diffie_helman_group_identifier

    @isakmp_diffie_helman_group_identifier.setter
    def isakmp_diffie_helman_group_identifier(self, value):
        """ Set isakmp_diffie_helman_group_identifier value.

            Notes:
                ISAKMP Diffie-Helman Group Identifier.

                
                This attribute is named `ISAKMPDiffieHelmanGroupIdentifier` in VSD API.
                
        """
        self._isakmp_diffie_helman_group_identifier = value

    
    @property
    def isakmp_encryption_algorithm(self):
        """ Get isakmp_encryption_algorithm value.

            Notes:
                ISAKMP Encryption Algorithm.

                
                This attribute is named `ISAKMPEncryptionAlgorithm` in VSD API.
                
        """
        return self._isakmp_encryption_algorithm

    @isakmp_encryption_algorithm.setter
    def isakmp_encryption_algorithm(self, value):
        """ Set isakmp_encryption_algorithm value.

            Notes:
                ISAKMP Encryption Algorithm.

                
                This attribute is named `ISAKMPEncryptionAlgorithm` in VSD API.
                
        """
        self._isakmp_encryption_algorithm = value

    
    @property
    def isakmp_encryption_key_lifetime(self):
        """ Get isakmp_encryption_key_lifetime value.

            Notes:
                ISAKMP Encryption Key Lifetime in Seconds

                
                This attribute is named `ISAKMPEncryptionKeyLifetime` in VSD API.
                
        """
        return self._isakmp_encryption_key_lifetime

    @isakmp_encryption_key_lifetime.setter
    def isakmp_encryption_key_lifetime(self, value):
        """ Set isakmp_encryption_key_lifetime value.

            Notes:
                ISAKMP Encryption Key Lifetime in Seconds

                
                This attribute is named `ISAKMPEncryptionKeyLifetime` in VSD API.
                
        """
        self._isakmp_encryption_key_lifetime = value

    
    @property
    def isakmp_hash_algorithm(self):
        """ Get isakmp_hash_algorithm value.

            Notes:
                ISAKMP Hash Algorithm.

                
                This attribute is named `ISAKMPHashAlgorithm` in VSD API.
                
        """
        return self._isakmp_hash_algorithm

    @isakmp_hash_algorithm.setter
    def isakmp_hash_algorithm(self, value):
        """ Set isakmp_hash_algorithm value.

            Notes:
                ISAKMP Hash Algorithm.

                
                This attribute is named `ISAKMPHashAlgorithm` in VSD API.
                
        """
        self._isakmp_hash_algorithm = value

    
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
    def sequence(self):
        """ Get sequence value.

            Notes:
                None

                
        """
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        """ Set sequence value.

            Notes:
                None

                
        """
        self._sequence = value

    
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

    

    