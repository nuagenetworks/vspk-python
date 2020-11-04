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


class NUEsIlmPolicy(NURESTObject):
    """ Represents a EsIlmPolicy in the VSD

        Notes:
            An Elasticsearch Index Lifecycle Management Policy defines the phases and actions to manage the lifecycle of an ES index.
    """

    __rest_name__ = "esilmpolicy"
    __resource_name__ = "esilmpolicies"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ES_ILM_POLICY_TYPE_DEFAULT = "DEFAULT"
    
    CONST_ES_ILM_POLICY_TYPE_CUSTOM = "CUSTOM"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a EsIlmPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> esilmpolicy = NUEsIlmPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'EsIlmPolicy')
                >>> esilmpolicy = NUEsIlmPolicy(data=my_dict)
        """

        super(NUEsIlmPolicy, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._warm_phase_enabled = None
        self._warm_timer = None
        self._delete_phase_enabled = None
        self._delete_timer = None
        self._description = None
        self._embedded_metadata = None
        self._index_freeze = None
        self._index_read_only = None
        self._entity_scope = None
        self._cold_phase_enabled = None
        self._cold_timer = None
        self._rollover_max_age = None
        self._rollover_max_docs = None
        self._rollover_max_size = None
        self._force_merge_enabled = None
        self._force_merge_max_num_segments = None
        self._es_ilm_policy_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="warm_phase_enabled", remote_name="warmPhaseEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="warm_timer", remote_name="warmTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="delete_phase_enabled", remote_name="deletePhaseEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="delete_timer", remote_name="deleteTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="index_freeze", remote_name="indexFreeze", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name="index_read_only", remote_name="indexReadOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="cold_phase_enabled", remote_name="coldPhaseEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cold_timer", remote_name="coldTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rollover_max_age", remote_name="rolloverMaxAge", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rollover_max_docs", remote_name="rolloverMaxDocs", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="rollover_max_size", remote_name="rolloverMaxSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="force_merge_enabled", remote_name="forceMergeEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="force_merge_max_num_segments", remote_name="forceMergeMaxNumSegments", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="es_ilm_policy_type", remote_name="esIlmPolicyType", attribute_type=str, is_required=False, is_unique=False, choices=[u'CUSTOM', u'DEFAULT'])
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
                A unique name of the EsIlmPolicy object

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name of the EsIlmPolicy object

                
        """
        self._name = value

    
    @property
    def warm_phase_enabled(self):
        """ Get warm_phase_enabled value.

            Notes:
                Enable WARM phase for the ES index

                
                This attribute is named `warmPhaseEnabled` in VSD API.
                
        """
        return self._warm_phase_enabled

    @warm_phase_enabled.setter
    def warm_phase_enabled(self, value):
        """ Set warm_phase_enabled value.

            Notes:
                Enable WARM phase for the ES index

                
                This attribute is named `warmPhaseEnabled` in VSD API.
                
        """
        self._warm_phase_enabled = value

    
    @property
    def warm_timer(self):
        """ Get warm_timer value.

            Notes:
                The number of hours after the rollover of the index until it moves to the warm phase.

                
                This attribute is named `warmTimer` in VSD API.
                
        """
        return self._warm_timer

    @warm_timer.setter
    def warm_timer(self, value):
        """ Set warm_timer value.

            Notes:
                The number of hours after the rollover of the index until it moves to the warm phase.

                
                This attribute is named `warmTimer` in VSD API.
                
        """
        self._warm_timer = value

    
    @property
    def delete_phase_enabled(self):
        """ Get delete_phase_enabled value.

            Notes:
                Enable DELETE phase for the ES index

                
                This attribute is named `deletePhaseEnabled` in VSD API.
                
        """
        return self._delete_phase_enabled

    @delete_phase_enabled.setter
    def delete_phase_enabled(self, value):
        """ Set delete_phase_enabled value.

            Notes:
                Enable DELETE phase for the ES index

                
                This attribute is named `deletePhaseEnabled` in VSD API.
                
        """
        self._delete_phase_enabled = value

    
    @property
    def delete_timer(self):
        """ Get delete_timer value.

            Notes:
                The number of hours after the rollover of the index until it gets deleted. This value has to be higher than the cold timer value.

                
                This attribute is named `deleteTimer` in VSD API.
                
        """
        return self._delete_timer

    @delete_timer.setter
    def delete_timer(self, value):
        """ Set delete_timer value.

            Notes:
                The number of hours after the rollover of the index until it gets deleted. This value has to be higher than the cold timer value.

                
                This attribute is named `deleteTimer` in VSD API.
                
        """
        self._delete_timer = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Elasticsearch Index Lifecycle Management Policy.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Elasticsearch Index Lifecycle Management Policy.

                
        """
        self._description = value

    
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
    def index_freeze(self):
        """ Get index_freeze value.

            Notes:
                Mark the ES index as frozen when moving to the cold phase. This will freeze the index by calling the Freeze Index API.

                
                This attribute is named `indexFreeze` in VSD API.
                
        """
        return self._index_freeze

    @index_freeze.setter
    def index_freeze(self, value):
        """ Set index_freeze value.

            Notes:
                Mark the ES index as frozen when moving to the cold phase. This will freeze the index by calling the Freeze Index API.

                
                This attribute is named `indexFreeze` in VSD API.
                
        """
        self._index_freeze = value

    
    @property
    def index_read_only(self):
        """ Get index_read_only value.

            Notes:
                Mark the ES index as readonly in the warm phase

                
                This attribute is named `indexReadOnly` in VSD API.
                
        """
        return self._index_read_only

    @index_read_only.setter
    def index_read_only(self, value):
        """ Set index_read_only value.

            Notes:
                Mark the ES index as readonly in the warm phase

                
                This attribute is named `indexReadOnly` in VSD API.
                
        """
        self._index_read_only = value

    
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
    def cold_phase_enabled(self):
        """ Get cold_phase_enabled value.

            Notes:
                Enable COLD phase for the ES index.

                
                This attribute is named `coldPhaseEnabled` in VSD API.
                
        """
        return self._cold_phase_enabled

    @cold_phase_enabled.setter
    def cold_phase_enabled(self, value):
        """ Set cold_phase_enabled value.

            Notes:
                Enable COLD phase for the ES index.

                
                This attribute is named `coldPhaseEnabled` in VSD API.
                
        """
        self._cold_phase_enabled = value

    
    @property
    def cold_timer(self):
        """ Get cold_timer value.

            Notes:
                The number of hours after the rollover of the index until it moves to the cold phase. This value has to be higher than the warm timer value.

                
                This attribute is named `coldTimer` in VSD API.
                
        """
        return self._cold_timer

    @cold_timer.setter
    def cold_timer(self, value):
        """ Set cold_timer value.

            Notes:
                The number of hours after the rollover of the index until it moves to the cold phase. This value has to be higher than the warm timer value.

                
                This attribute is named `coldTimer` in VSD API.
                
        """
        self._cold_timer = value

    
    @property
    def rollover_max_age(self):
        """ Get rollover_max_age value.

            Notes:
                The number of hours after which the index is rolled over in case it isn't rolled over based on size or number of documents.

                
                This attribute is named `rolloverMaxAge` in VSD API.
                
        """
        return self._rollover_max_age

    @rollover_max_age.setter
    def rollover_max_age(self, value):
        """ Set rollover_max_age value.

            Notes:
                The number of hours after which the index is rolled over in case it isn't rolled over based on size or number of documents.

                
                This attribute is named `rolloverMaxAge` in VSD API.
                
        """
        self._rollover_max_age = value

    
    @property
    def rollover_max_docs(self):
        """ Get rollover_max_docs value.

            Notes:
                The number of documents after which the index is rolled over in case it isn't rolled over based on size or age.

                
                This attribute is named `rolloverMaxDocs` in VSD API.
                
        """
        return self._rollover_max_docs

    @rollover_max_docs.setter
    def rollover_max_docs(self, value):
        """ Set rollover_max_docs value.

            Notes:
                The number of documents after which the index is rolled over in case it isn't rolled over based on size or age.

                
                This attribute is named `rolloverMaxDocs` in VSD API.
                
        """
        self._rollover_max_docs = value

    
    @property
    def rollover_max_size(self):
        """ Get rollover_max_size value.

            Notes:
                The max size in GB after which the index is rolled over in case it isn't rolled over based on age or number of documents.

                
                This attribute is named `rolloverMaxSize` in VSD API.
                
        """
        return self._rollover_max_size

    @rollover_max_size.setter
    def rollover_max_size(self, value):
        """ Set rollover_max_size value.

            Notes:
                The max size in GB after which the index is rolled over in case it isn't rolled over based on age or number of documents.

                
                This attribute is named `rolloverMaxSize` in VSD API.
                
        """
        self._rollover_max_size = value

    
    @property
    def force_merge_enabled(self):
        """ Get force_merge_enabled value.

            Notes:
                Enable the Force Merge action for the ES index when moving to the warm phase.

                
                This attribute is named `forceMergeEnabled` in VSD API.
                
        """
        return self._force_merge_enabled

    @force_merge_enabled.setter
    def force_merge_enabled(self, value):
        """ Set force_merge_enabled value.

            Notes:
                Enable the Force Merge action for the ES index when moving to the warm phase.

                
                This attribute is named `forceMergeEnabled` in VSD API.
                
        """
        self._force_merge_enabled = value

    
    @property
    def force_merge_max_num_segments(self):
        """ Get force_merge_max_num_segments value.

            Notes:
                Max number of segments for Force Merge

                
                This attribute is named `forceMergeMaxNumSegments` in VSD API.
                
        """
        return self._force_merge_max_num_segments

    @force_merge_max_num_segments.setter
    def force_merge_max_num_segments(self, value):
        """ Set force_merge_max_num_segments value.

            Notes:
                Max number of segments for Force Merge

                
                This attribute is named `forceMergeMaxNumSegments` in VSD API.
                
        """
        self._force_merge_max_num_segments = value

    
    @property
    def es_ilm_policy_type(self):
        """ Get es_ilm_policy_type value.

            Notes:
                The type of EsIlm Policy. 

                
                This attribute is named `esIlmPolicyType` in VSD API.
                
        """
        return self._es_ilm_policy_type

    @es_ilm_policy_type.setter
    def es_ilm_policy_type(self, value):
        """ Set es_ilm_policy_type value.

            Notes:
                The type of EsIlm Policy. 

                
                This attribute is named `esIlmPolicyType` in VSD API.
                
        """
        self._es_ilm_policy_type = value

    
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

    

    