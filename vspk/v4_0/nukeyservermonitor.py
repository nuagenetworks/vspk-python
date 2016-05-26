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


from .fetchers import NUKeyServerMonitorEncryptedSeedsFetcher


from .fetchers import NUKeyServerMonitorSeedsFetcher


from .fetchers import NUKeyServerMonitorSEKsFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUKeyServerMonitor(NURESTObject):
    """ Represents a KeyServerMonitor in the VSD

        Notes:
            Represents a Keyserver Monitor Snapshot.
    """

    __rest_name__ = "keyservermonitor"
    __resource_name__ = "keyservermonitors"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a KeyServerMonitor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservermonitor = NUKeyServerMonitor(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerMonitor')
                >>> keyservermonitor = NUKeyServerMonitor(data=my_dict)
        """

        super(NUKeyServerMonitor, self).__init__()

        # Read/Write Attributes
        
        self._last_update_time = None
        self._last_updated_by = None
        self._gateway_secured_data_record_count = None
        self._keyserver_monitor_encrypted_sek_count = None
        self._keyserver_monitor_encrypted_seed_count = None
        self._keyserver_monitor_sek_count = None
        self._keyserver_monitor_seed_count = None
        self._enterprise_secured_data_record_count = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_update_time", remote_name="lastUpdateTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_secured_data_record_count", remote_name="gatewaySecuredDataRecordCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="keyserver_monitor_encrypted_sek_count", remote_name="keyserverMonitorEncryptedSEKCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="keyserver_monitor_encrypted_seed_count", remote_name="keyserverMonitorEncryptedSeedCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="keyserver_monitor_sek_count", remote_name="keyserverMonitorSEKCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="keyserver_monitor_seed_count", remote_name="keyserverMonitorSeedCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_secured_data_record_count", remote_name="enterpriseSecuredDataRecordCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.key_server_monitor_encrypted_seeds = NUKeyServerMonitorEncryptedSeedsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.key_server_monitor_seeds = NUKeyServerMonitorSeedsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.key_server_monitor_seks = NUKeyServerMonitorSEKsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def last_update_time(self):
        """ Get last_update_time value.

            Notes:
                The time the latest SEK or Seed was created/removed (milliseconds since epoch)

                
                This attribute is named `lastUpdateTime` in VSD API.
                
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        """ Set last_update_time value.

            Notes:
                The time the latest SEK or Seed was created/removed (milliseconds since epoch)

                
                This attribute is named `lastUpdateTime` in VSD API.
                
        """
        self._last_update_time = value

    
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
    def gateway_secured_data_record_count(self):
        """ Get gateway_secured_data_record_count value.

            Notes:
                Total number of Gateway Secured Data records

                
                This attribute is named `gatewaySecuredDataRecordCount` in VSD API.
                
        """
        return self._gateway_secured_data_record_count

    @gateway_secured_data_record_count.setter
    def gateway_secured_data_record_count(self, value):
        """ Set gateway_secured_data_record_count value.

            Notes:
                Total number of Gateway Secured Data records

                
                This attribute is named `gatewaySecuredDataRecordCount` in VSD API.
                
        """
        self._gateway_secured_data_record_count = value

    
    @property
    def keyserver_monitor_encrypted_sek_count(self):
        """ Get keyserver_monitor_encrypted_sek_count value.

            Notes:
                Total number of Keyserver Monitor Encrypted SEK records

                
                This attribute is named `keyserverMonitorEncryptedSEKCount` in VSD API.
                
        """
        return self._keyserver_monitor_encrypted_sek_count

    @keyserver_monitor_encrypted_sek_count.setter
    def keyserver_monitor_encrypted_sek_count(self, value):
        """ Set keyserver_monitor_encrypted_sek_count value.

            Notes:
                Total number of Keyserver Monitor Encrypted SEK records

                
                This attribute is named `keyserverMonitorEncryptedSEKCount` in VSD API.
                
        """
        self._keyserver_monitor_encrypted_sek_count = value

    
    @property
    def keyserver_monitor_encrypted_seed_count(self):
        """ Get keyserver_monitor_encrypted_seed_count value.

            Notes:
                Total number of Keyserver Monitor Encrypted Seed records

                
                This attribute is named `keyserverMonitorEncryptedSeedCount` in VSD API.
                
        """
        return self._keyserver_monitor_encrypted_seed_count

    @keyserver_monitor_encrypted_seed_count.setter
    def keyserver_monitor_encrypted_seed_count(self, value):
        """ Set keyserver_monitor_encrypted_seed_count value.

            Notes:
                Total number of Keyserver Monitor Encrypted Seed records

                
                This attribute is named `keyserverMonitorEncryptedSeedCount` in VSD API.
                
        """
        self._keyserver_monitor_encrypted_seed_count = value

    
    @property
    def keyserver_monitor_sek_count(self):
        """ Get keyserver_monitor_sek_count value.

            Notes:
                Total number of Keyserver Monitor SEK records

                
                This attribute is named `keyserverMonitorSEKCount` in VSD API.
                
        """
        return self._keyserver_monitor_sek_count

    @keyserver_monitor_sek_count.setter
    def keyserver_monitor_sek_count(self, value):
        """ Set keyserver_monitor_sek_count value.

            Notes:
                Total number of Keyserver Monitor SEK records

                
                This attribute is named `keyserverMonitorSEKCount` in VSD API.
                
        """
        self._keyserver_monitor_sek_count = value

    
    @property
    def keyserver_monitor_seed_count(self):
        """ Get keyserver_monitor_seed_count value.

            Notes:
                Total number of Keyserver Monitor Seed records

                
                This attribute is named `keyserverMonitorSeedCount` in VSD API.
                
        """
        return self._keyserver_monitor_seed_count

    @keyserver_monitor_seed_count.setter
    def keyserver_monitor_seed_count(self, value):
        """ Set keyserver_monitor_seed_count value.

            Notes:
                Total number of Keyserver Monitor Seed records

                
                This attribute is named `keyserverMonitorSeedCount` in VSD API.
                
        """
        self._keyserver_monitor_seed_count = value

    
    @property
    def enterprise_secured_data_record_count(self):
        """ Get enterprise_secured_data_record_count value.

            Notes:
                Total number of Enterprise Secured Data records

                
                This attribute is named `enterpriseSecuredDataRecordCount` in VSD API.
                
        """
        return self._enterprise_secured_data_record_count

    @enterprise_secured_data_record_count.setter
    def enterprise_secured_data_record_count(self, value):
        """ Set enterprise_secured_data_record_count value.

            Notes:
                Total number of Enterprise Secured Data records

                
                This attribute is named `enterpriseSecuredDataRecordCount` in VSD API.
                
        """
        self._enterprise_secured_data_record_count = value

    
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

    

    