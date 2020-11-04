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


class NUVNFDomainMapping(NURESTObject):
    """ Represents a VNFDomainMapping in the VSD

        Notes:
            This represents domain segment identifier which is unique for domain per NSGateway.
    """

    __rest_name__ = "vnfdomainmapping"
    __resource_name__ = "vnfdomainmappings"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SEGMENTATION_TYPE_VLAN = "VLAN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VNFDomainMapping instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vnfdomainmapping = NUVNFDomainMapping(id=u'xxxx-xxx-xxx-xxx', name=u'VNFDomainMapping')
                >>> vnfdomainmapping = NUVNFDomainMapping(data=my_dict)
        """

        super(NUVNFDomainMapping, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._last_updated_date = None
        self._segmentation_id = None
        self._segmentation_type = None
        self._service_id = None
        self._embedded_metadata = None
        self._enterprise_name = None
        self._entity_scope = None
        self._creation_date = None
        self._associated_domain_id = None
        self._associated_domain_name = None
        self._associated_enterprise_id = None
        self._associated_ns_gateway_id = None
        self._associated_ns_gateway_name = None
        self._auto_created = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="segmentation_id", remote_name="segmentationID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="segmentation_type", remote_name="segmentationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'VLAN'])
        self.expose_attribute(local_name="service_id", remote_name="serviceId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_name", remote_name="associatedDomainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_id", remote_name="associatedNSGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_name", remote_name="associatedNSGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="auto_created", remote_name="autoCreated", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def segmentation_id(self):
        """ Get segmentation_id value.

            Notes:
                The segmentation ID (1-4095).

                
                This attribute is named `segmentationID` in VSD API.
                
        """
        return self._segmentation_id

    @segmentation_id.setter
    def segmentation_id(self, value):
        """ Set segmentation_id value.

            Notes:
                The segmentation ID (1-4095).

                
                This attribute is named `segmentationID` in VSD API.
                
        """
        self._segmentation_id = value

    
    @property
    def segmentation_type(self):
        """ Get segmentation_type value.

            Notes:
                The type of segmentation that is used.

                
                This attribute is named `segmentationType` in VSD API.
                
        """
        return self._segmentation_type

    @segmentation_type.setter
    def segmentation_type(self, value):
        """ Set segmentation_type value.

            Notes:
                The type of segmentation that is used.

                
                This attribute is named `segmentationType` in VSD API.
                
        """
        self._segmentation_type = value

    
    @property
    def service_id(self):
        """ Get service_id value.

            Notes:
                Service ID of the associated Domain

                
                This attribute is named `serviceId` in VSD API.
                
        """
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        """ Set service_id value.

            Notes:
                Service ID of the associated Domain

                
                This attribute is named `serviceId` in VSD API.
                
        """
        self._service_id = value

    
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
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                Name of the associated Enterprise

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                Name of the associated Enterprise

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
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
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                ID of the associated Domain

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                ID of the associated Domain

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def associated_domain_name(self):
        """ Get associated_domain_name value.

            Notes:
                Name of the associated Domain

                
                This attribute is named `associatedDomainName` in VSD API.
                
        """
        return self._associated_domain_name

    @associated_domain_name.setter
    def associated_domain_name(self, value):
        """ Set associated_domain_name value.

            Notes:
                Name of the associated Domain

                
                This attribute is named `associatedDomainName` in VSD API.
                
        """
        self._associated_domain_name = value

    
    @property
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    
    @property
    def associated_ns_gateway_id(self):
        """ Get associated_ns_gateway_id value.

            Notes:
                Associated NS Gateway

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        return self._associated_ns_gateway_id

    @associated_ns_gateway_id.setter
    def associated_ns_gateway_id(self, value):
        """ Set associated_ns_gateway_id value.

            Notes:
                Associated NS Gateway

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        self._associated_ns_gateway_id = value

    
    @property
    def associated_ns_gateway_name(self):
        """ Get associated_ns_gateway_name value.

            Notes:
                Name of associated NSGateway

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        return self._associated_ns_gateway_name

    @associated_ns_gateway_name.setter
    def associated_ns_gateway_name(self, value):
        """ Set associated_ns_gateway_name value.

            Notes:
                Name of associated NSGateway

                
                This attribute is named `associatedNSGatewayName` in VSD API.
                
        """
        self._associated_ns_gateway_name = value

    
    @property
    def auto_created(self):
        """ Get auto_created value.

            Notes:
                Indicates that this domain mapping was auto created by the system

                
                This attribute is named `autoCreated` in VSD API.
                
        """
        return self._auto_created

    @auto_created.setter
    def auto_created(self, value):
        """ Set auto_created value.

            Notes:
                Indicates that this domain mapping was auto created by the system

                
                This attribute is named `autoCreated` in VSD API.
                
        """
        self._auto_created = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
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

    

    