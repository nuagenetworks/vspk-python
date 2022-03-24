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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUEsIndexConfig(NURESTObject):
    """ Represents a EsIndexConfig in the VSD

        Notes:
            Elasticsearch Index configuration
    """

    __rest_name__ = "esindexconfig"
    __resource_name__ = "esindexconfigs"

    
    ## Constants
    
    CONST_INDEX_TYPE_NUAGE_DPI_PROBESTATS = "NUAGE_DPI_PROBESTATS"
    
    CONST_INDEX_TYPE_NUAGE_IKE_PROBE_STATUS = "NUAGE_IKE_PROBE_STATUS"
    
    CONST_INDEX_TYPE_NUAGE_SYSMON = "NUAGE_SYSMON"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_INDEX_TYPE_NUAGE_IKE_STATS = "NUAGE_IKE_STATS"
    
    CONST_CONFIG_STATUS_SUCCESS = "SUCCESS"
    
    CONST_INDEX_TYPE_NUAGE_VPORT = "NUAGE_VPORT"
    
    CONST_ILM_STATUS_SUCCESS = "SUCCESS"
    
    CONST_INDEX_TYPE_NUAGE_EVENT = "NUAGE_EVENT"
    
    CONST_INDEX_TYPE_NUAGE_DPI_SLASTATS = "NUAGE_DPI_SLASTATS"
    
    CONST_INDEX_TYPE_NUAGE_IKE_PROBESTATS = "NUAGE_IKE_PROBESTATS"
    
    CONST_INDEX_TYPE_NUAGE_VLAN = "NUAGE_VLAN"
    
    CONST_INDEX_TYPE_NUAGE_FLOW = "NUAGE_FLOW"
    
    CONST_INDEX_TYPE_NUAGE_OAM = "NUAGE_OAM"
    
    CONST_ILM_STATUS_FAILED = "FAILED"
    
    CONST_INDEX_TYPE_NUAGE_GW_SEL_STATS = "NUAGE_GW_SEL_STATS"
    
    CONST_INDEX_TYPE_NUAGE_ACL = "NUAGE_ACL"
    
    CONST_INDEX_TYPE_NUAGE_WIFI = "NUAGE_WIFI"
    
    CONST_CONFIG_STATUS_FAILED = "FAILED"
    
    CONST_INDEX_TYPE_NUAGE_ADDRESSMAP = "NUAGE_ADDRESSMAP"
    
    CONST_INDEX_TYPE_NUAGE_VNF = "NUAGE_VNF"
    
    CONST_INDEX_TYPE_NUAGE_LTE = "NUAGE_LTE"
    
    CONST_CONFIG_STATUS_IN_PROGRESS = "IN_PROGRESS"
    
    CONST_INDEX_TYPE_NUAGE_DPI_FLOWSTATS = "NUAGE_DPI_FLOWSTATS"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_INDEX_TYPE_NUAGE_VPORT_QOS = "NUAGE_VPORT_QOS"
    
    CONST_INDEX_TYPE_NUAGE_NATT = "NUAGE_NATT"
    
    CONST_INDEX_TYPE_NUAGE_FEC = "NUAGE_FEC"
    
    

    def __init__(self, **kwargs):
        """ Initializes a EsIndexConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> esindexconfig = NUEsIndexConfig(id=u'xxxx-xxx-xxx-xxx', name=u'EsIndexConfig')
                >>> esindexconfig = NUEsIndexConfig(data=my_dict)
        """

        super(NUEsIndexConfig, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._ilm_status = None
        self._embedded_metadata = None
        self._index_pattern = None
        self._index_type = None
        self._entity_scope = None
        self._policy_name = None
        self._rollover_alias = None
        self._config_status = None
        self._associated_es_ilm_policy_id = None
        self._num_shards = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ilm_status", remote_name="ilmStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'SUCCESS'])
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="index_pattern", remote_name="indexPattern", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="index_type", remote_name="indexType", attribute_type=str, is_required=True, is_unique=False, choices=[u'NUAGE_ACL', u'NUAGE_ADDRESSMAP', u'NUAGE_DPI_FLOWSTATS', u'NUAGE_DPI_PROBESTATS', u'NUAGE_DPI_SLASTATS', u'NUAGE_EVENT', u'NUAGE_FEC', u'NUAGE_FLOW', u'NUAGE_GW_SEL_STATS', u'NUAGE_IKE_PROBE_STATUS', u'NUAGE_IKE_PROBESTATS', u'NUAGE_IKE_STATS', u'NUAGE_LTE', u'NUAGE_NATT', u'NUAGE_OAM', u'NUAGE_SYSMON', u'NUAGE_VLAN', u'NUAGE_VNF', u'NUAGE_VPORT', u'NUAGE_VPORT_QOS', u'NUAGE_WIFI'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="policy_name", remote_name="policyName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rollover_alias", remote_name="rolloverAlias", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="config_status", remote_name="configStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'IN_PROGRESS', u'SUCCESS'])
        self.expose_attribute(local_name="associated_es_ilm_policy_id", remote_name="associatedEsIlmPolicyId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="num_shards", remote_name="numShards", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the ES Index Config.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the ES Index Config.

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the ES Index Config.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the ES Index Config.

                
        """
        self._description = value

    
    @property
    def ilm_status(self):
        """ Get ilm_status value.

            Notes:
                Index Life Management Status.

                
                This attribute is named `ilmStatus` in VSD API.
                
        """
        return self._ilm_status

    @ilm_status.setter
    def ilm_status(self, value):
        """ Set ilm_status value.

            Notes:
                Index Life Management Status.

                
                This attribute is named `ilmStatus` in VSD API.
                
        """
        self._ilm_status = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def index_pattern(self):
        """ Get index_pattern value.

            Notes:
                The wildcard pattern for the specific ES index

                
                This attribute is named `indexPattern` in VSD API.
                
        """
        return self._index_pattern

    @index_pattern.setter
    def index_pattern(self, value):
        """ Set index_pattern value.

            Notes:
                The wildcard pattern for the specific ES index

                
                This attribute is named `indexPattern` in VSD API.
                
        """
        self._index_pattern = value

    
    @property
    def index_type(self):
        """ Get index_type value.

            Notes:
                The enum value corresponding to an ES index.

                
                This attribute is named `indexType` in VSD API.
                
        """
        return self._index_type

    @index_type.setter
    def index_type(self, value):
        """ Set index_type value.

            Notes:
                The enum value corresponding to an ES index.

                
                This attribute is named `indexType` in VSD API.
                
        """
        self._index_type = value

    
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
    def policy_name(self):
        """ Get policy_name value.

            Notes:
                The associated EsIlmPolicy name.

                
                This attribute is named `policyName` in VSD API.
                
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, value):
        """ Set policy_name value.

            Notes:
                The associated EsIlmPolicy name.

                
                This attribute is named `policyName` in VSD API.
                
        """
        self._policy_name = value

    
    @property
    def rollover_alias(self):
        """ Get rollover_alias value.

            Notes:
                The rollover alias for the specific ES index.

                
                This attribute is named `rolloverAlias` in VSD API.
                
        """
        return self._rollover_alias

    @rollover_alias.setter
    def rollover_alias(self, value):
        """ Set rollover_alias value.

            Notes:
                The rollover alias for the specific ES index.

                
                This attribute is named `rolloverAlias` in VSD API.
                
        """
        self._rollover_alias = value

    
    @property
    def config_status(self):
        """ Get config_status value.

            Notes:
                Configuration status of ES Config.

                
                This attribute is named `configStatus` in VSD API.
                
        """
        return self._config_status

    @config_status.setter
    def config_status(self, value):
        """ Set config_status value.

            Notes:
                Configuration status of ES Config.

                
                This attribute is named `configStatus` in VSD API.
                
        """
        self._config_status = value

    
    @property
    def associated_es_ilm_policy_id(self):
        """ Get associated_es_ilm_policy_id value.

            Notes:
                The UUID of the associated EsIlmPolicy object with ES Index Config.

                
                This attribute is named `associatedEsIlmPolicyId` in VSD API.
                
        """
        return self._associated_es_ilm_policy_id

    @associated_es_ilm_policy_id.setter
    def associated_es_ilm_policy_id(self, value):
        """ Set associated_es_ilm_policy_id value.

            Notes:
                The UUID of the associated EsIlmPolicy object with ES Index Config.

                
                This attribute is named `associatedEsIlmPolicyId` in VSD API.
                
        """
        self._associated_es_ilm_policy_id = value

    
    @property
    def num_shards(self):
        """ Get num_shards value.

            Notes:
                The number of primary shards for this index.

                
                This attribute is named `numShards` in VSD API.
                
        """
        return self._num_shards

    @num_shards.setter
    def num_shards(self, value):
        """ Set num_shards value.

            Notes:
                The number of primary shards for this index.

                
                This attribute is named `numShards` in VSD API.
                
        """
        self._num_shards = value

    
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

    

    