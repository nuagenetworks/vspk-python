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


class NUDeploymentFailure(NURESTObject):
    """ Represents a DeploymentFailure in the VSD

        Notes:
            A deployment failure represents a deployment operation initiated by the VSD that resulted in a failure.
    """

    __rest_name__ = "deploymentfailure"
    __resource_name__ = "deploymentfailures"

    
    ## Constants
    
    CONST_EVENT_TYPE_DELETE = "DELETE"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_EVENT_TYPE_CREATE = "CREATE"
    
    CONST_EVENT_TYPE_UPDATE = "UPDATE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DeploymentFailure instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> deploymentfailure = NUDeploymentFailure(id=u'xxxx-xxx-xxx-xxx', name=u'DeploymentFailure')
                >>> deploymentfailure = NUDeploymentFailure(data=my_dict)
        """

        super(NUDeploymentFailure, self).__init__()

        # Read/Write Attributes
        
        self._last_failure_reason = None
        self._last_known_error = None
        self._last_updated_by = None
        self._affected_entity_id = None
        self._affected_entity_type = None
        self._diff_map = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._error_condition = None
        self._assoc_entity_id = None
        self._assoc_entity_type = None
        self._associated_domain_id = None
        self._associated_domain_type = None
        self._associated_network_entity_id = None
        self._associated_network_entity_type = None
        self._number_of_occurences = None
        self._event_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_failure_reason", remote_name="lastFailureReason", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_known_error", remote_name="lastKnownError", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="affected_entity_id", remote_name="affectedEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="affected_entity_type", remote_name="affectedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="diff_map", remote_name="diffMap", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="error_condition", remote_name="errorCondition", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_entity_id", remote_name="assocEntityId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_entity_type", remote_name="assocEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_type", remote_name="associatedDomainType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_entity_id", remote_name="associatedNetworkEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_network_entity_type", remote_name="associatedNetworkEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="number_of_occurences", remote_name="numberOfOccurences", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="event_type", remote_name="eventType", attribute_type=str, is_required=False, is_unique=False, choices=[u'CREATE', u'DELETE', u'UPDATE'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def last_failure_reason(self):
        """ Get last_failure_reason value.

            Notes:
                A detailed description of the last deployment failure.

                
                This attribute is named `lastFailureReason` in VSD API.
                
        """
        return self._last_failure_reason

    @last_failure_reason.setter
    def last_failure_reason(self, value):
        """ Set last_failure_reason value.

            Notes:
                A detailed description of the last deployment failure.

                
                This attribute is named `lastFailureReason` in VSD API.
                
        """
        self._last_failure_reason = value

    
    @property
    def last_known_error(self):
        """ Get last_known_error value.

            Notes:
                A string reporting the last reported deployment error condition.

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        return self._last_known_error

    @last_known_error.setter
    def last_known_error(self, value):
        """ Set last_known_error value.

            Notes:
                A string reporting the last reported deployment error condition.

                
                This attribute is named `lastKnownError` in VSD API.
                
        """
        self._last_known_error = value

    
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
    def affected_entity_id(self):
        """ Get affected_entity_id value.

            Notes:
                UUID of the entity on which deployment failed.

                
                This attribute is named `affectedEntityID` in VSD API.
                
        """
        return self._affected_entity_id

    @affected_entity_id.setter
    def affected_entity_id(self, value):
        """ Set affected_entity_id value.

            Notes:
                UUID of the entity on which deployment failed.

                
                This attribute is named `affectedEntityID` in VSD API.
                
        """
        self._affected_entity_id = value

    
    @property
    def affected_entity_type(self):
        """ Get affected_entity_type value.

            Notes:
                Managed object type corresponding to the entity on which deployment failed.

                
                This attribute is named `affectedEntityType` in VSD API.
                
        """
        return self._affected_entity_type

    @affected_entity_type.setter
    def affected_entity_type(self, value):
        """ Set affected_entity_type value.

            Notes:
                Managed object type corresponding to the entity on which deployment failed.

                
                This attribute is named `affectedEntityType` in VSD API.
                
        """
        self._affected_entity_type = value

    
    @property
    def diff_map(self):
        """ Get diff_map value.

            Notes:
                Object difference in json format.

                
                This attribute is named `diffMap` in VSD API.
                
        """
        return self._diff_map

    @diff_map.setter
    def diff_map(self, value):
        """ Set diff_map value.

            Notes:
                Object difference in json format.

                
                This attribute is named `diffMap` in VSD API.
                
        """
        self._diff_map = value

    
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
    def error_condition(self):
        """ Get error_condition value.

            Notes:
                A numerical code mapping to the deployment error condition.

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        return self._error_condition

    @error_condition.setter
    def error_condition(self, value):
        """ Set error_condition value.

            Notes:
                A numerical code mapping to the deployment error condition.

                
                This attribute is named `errorCondition` in VSD API.
                
        """
        self._error_condition = value

    
    @property
    def assoc_entity_id(self):
        """ Get assoc_entity_id value.

            Notes:
                ID of the parent entity

                
                This attribute is named `assocEntityId` in VSD API.
                
        """
        return self._assoc_entity_id

    @assoc_entity_id.setter
    def assoc_entity_id(self, value):
        """ Set assoc_entity_id value.

            Notes:
                ID of the parent entity

                
                This attribute is named `assocEntityId` in VSD API.
                
        """
        self._assoc_entity_id = value

    
    @property
    def assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Type of parent entity.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    @assoc_entity_type.setter
    def assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Type of parent entity.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                ID of the associated Domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                ID of the associated Domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def associated_domain_type(self):
        """ Get associated_domain_type value.

            Notes:
                Type of the associated Domain

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        return self._associated_domain_type

    @associated_domain_type.setter
    def associated_domain_type(self, value):
        """ Set associated_domain_type value.

            Notes:
                Type of the associated Domain

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        self._associated_domain_type = value

    
    @property
    def associated_network_entity_id(self):
        """ Get associated_network_entity_id value.

            Notes:
                ID of associated Network entity.

                
                This attribute is named `associatedNetworkEntityID` in VSD API.
                
        """
        return self._associated_network_entity_id

    @associated_network_entity_id.setter
    def associated_network_entity_id(self, value):
        """ Set associated_network_entity_id value.

            Notes:
                ID of associated Network entity.

                
                This attribute is named `associatedNetworkEntityID` in VSD API.
                
        """
        self._associated_network_entity_id = value

    
    @property
    def associated_network_entity_type(self):
        """ Get associated_network_entity_type value.

            Notes:
                Type of associated Network Entity. i.e Domain, Subnet, L2domain

                
                This attribute is named `associatedNetworkEntityType` in VSD API.
                
        """
        return self._associated_network_entity_type

    @associated_network_entity_type.setter
    def associated_network_entity_type(self, value):
        """ Set associated_network_entity_type value.

            Notes:
                Type of associated Network Entity. i.e Domain, Subnet, L2domain

                
                This attribute is named `associatedNetworkEntityType` in VSD API.
                
        """
        self._associated_network_entity_type = value

    
    @property
    def number_of_occurences(self):
        """ Get number_of_occurences value.

            Notes:
                A count of failed deployment attempts.

                
                This attribute is named `numberOfOccurences` in VSD API.
                
        """
        return self._number_of_occurences

    @number_of_occurences.setter
    def number_of_occurences(self, value):
        """ Set number_of_occurences value.

            Notes:
                A count of failed deployment attempts.

                
                This attribute is named `numberOfOccurences` in VSD API.
                
        """
        self._number_of_occurences = value

    
    @property
    def event_type(self):
        """ Get event_type value.

            Notes:
                Event type corresponding to the deployment failure

                
                This attribute is named `eventType` in VSD API.
                
        """
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """ Set event_type value.

            Notes:
                Event type corresponding to the deployment failure

                
                This attribute is named `eventType` in VSD API.
                
        """
        self._event_type = value

    
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

    

    