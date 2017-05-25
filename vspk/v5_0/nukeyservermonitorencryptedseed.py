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


class NUKeyServerMonitorEncryptedSeed(NURESTObject):
    """ Represents a KeyServerMonitorEncryptedSeed in the VSD

        Notes:
            Represents a Keyserver Monitor Encrypted Seed Snapshot.
    """

    __rest_name__ = "keyservermonitorencryptedseed"
    __resource_name__ = "keyservermonitorencryptedseeds"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a KeyServerMonitorEncryptedSeed instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservermonitorencryptedseed = NUKeyServerMonitorEncryptedSeed(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerMonitorEncryptedSeed')
                >>> keyservermonitorencryptedseed = NUKeyServerMonitorEncryptedSeed(data=my_dict)
        """

        super(NUKeyServerMonitorEncryptedSeed, self).__init__()

        # Read/Write Attributes
        
        self._sek_creation_time = None
        self._last_updated_by = None
        self._key_server_certificate_serial_number = None
        self._enterprise_secured_data_id = None
        self._entity_scope = None
        self._associated_key_server_monitor_sek_creation_time = None
        self._associated_key_server_monitor_sekid = None
        self._associated_key_server_monitor_seed_creation_time = None
        self._associated_key_server_monitor_seed_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="sek_creation_time", remote_name="SEKCreationTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="key_server_certificate_serial_number", remote_name="keyServerCertificateSerialNumber", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_secured_data_id", remote_name="enterpriseSecuredDataID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_key_server_monitor_sek_creation_time", remote_name="associatedKeyServerMonitorSEKCreationTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_key_server_monitor_sekid", remote_name="associatedKeyServerMonitorSEKID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_key_server_monitor_seed_creation_time", remote_name="associatedKeyServerMonitorSeedCreationTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_key_server_monitor_seed_id", remote_name="associatedKeyServerMonitorSeedID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def sek_creation_time(self):
        """ Get sek_creation_time value.

            Notes:
                SEK Creation Time

                
                This attribute is named `SEKCreationTime` in VSD API.
                
        """
        return self._sek_creation_time

    @sek_creation_time.setter
    def sek_creation_time(self, value):
        """ Set sek_creation_time value.

            Notes:
                SEK Creation Time

                
                This attribute is named `SEKCreationTime` in VSD API.
                
        """
        self._sek_creation_time = value

    
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
    def key_server_certificate_serial_number(self):
        """ Get key_server_certificate_serial_number value.

            Notes:
                KeyServer Certificate Serial Number

                
                This attribute is named `keyServerCertificateSerialNumber` in VSD API.
                
        """
        return self._key_server_certificate_serial_number

    @key_server_certificate_serial_number.setter
    def key_server_certificate_serial_number(self, value):
        """ Set key_server_certificate_serial_number value.

            Notes:
                KeyServer Certificate Serial Number

                
                This attribute is named `keyServerCertificateSerialNumber` in VSD API.
                
        """
        self._key_server_certificate_serial_number = value

    
    @property
    def enterprise_secured_data_id(self):
        """ Get enterprise_secured_data_id value.

            Notes:
                Enterprise Secured ID record this monitor represents

                
                This attribute is named `enterpriseSecuredDataID` in VSD API.
                
        """
        return self._enterprise_secured_data_id

    @enterprise_secured_data_id.setter
    def enterprise_secured_data_id(self, value):
        """ Set enterprise_secured_data_id value.

            Notes:
                Enterprise Secured ID record this monitor represents

                
                This attribute is named `enterpriseSecuredDataID` in VSD API.
                
        """
        self._enterprise_secured_data_id = value

    
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
    def associated_key_server_monitor_sek_creation_time(self):
        """ Get associated_key_server_monitor_sek_creation_time value.

            Notes:
                The creation time of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSEKCreationTime` in VSD API.
                
        """
        return self._associated_key_server_monitor_sek_creation_time

    @associated_key_server_monitor_sek_creation_time.setter
    def associated_key_server_monitor_sek_creation_time(self, value):
        """ Set associated_key_server_monitor_sek_creation_time value.

            Notes:
                The creation time of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSEKCreationTime` in VSD API.
                
        """
        self._associated_key_server_monitor_sek_creation_time = value

    
    @property
    def associated_key_server_monitor_sekid(self):
        """ Get associated_key_server_monitor_sekid value.

            Notes:
                The ID of the associated KeyServer Monitor SEK ID

                
                This attribute is named `associatedKeyServerMonitorSEKID` in VSD API.
                
        """
        return self._associated_key_server_monitor_sekid

    @associated_key_server_monitor_sekid.setter
    def associated_key_server_monitor_sekid(self, value):
        """ Set associated_key_server_monitor_sekid value.

            Notes:
                The ID of the associated KeyServer Monitor SEK ID

                
                This attribute is named `associatedKeyServerMonitorSEKID` in VSD API.
                
        """
        self._associated_key_server_monitor_sekid = value

    
    @property
    def associated_key_server_monitor_seed_creation_time(self):
        """ Get associated_key_server_monitor_seed_creation_time value.

            Notes:
                The creation time of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedCreationTime` in VSD API.
                
        """
        return self._associated_key_server_monitor_seed_creation_time

    @associated_key_server_monitor_seed_creation_time.setter
    def associated_key_server_monitor_seed_creation_time(self, value):
        """ Set associated_key_server_monitor_seed_creation_time value.

            Notes:
                The creation time of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedCreationTime` in VSD API.
                
        """
        self._associated_key_server_monitor_seed_creation_time = value

    
    @property
    def associated_key_server_monitor_seed_id(self):
        """ Get associated_key_server_monitor_seed_id value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedID` in VSD API.
                
        """
        return self._associated_key_server_monitor_seed_id

    @associated_key_server_monitor_seed_id.setter
    def associated_key_server_monitor_seed_id(self, value):
        """ Set associated_key_server_monitor_seed_id value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedID` in VSD API.
                
        """
        self._associated_key_server_monitor_seed_id = value

    
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

    

    