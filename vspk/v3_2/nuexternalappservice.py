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


class NUExternalAppService(NURESTObject):
    """ Represents a ExternalAppService in the VSD

        Notes:
            Represents an External Service in the Application Designer.
    """

    __rest_name__ = "externalappservice"
    __resource_name__ = "externalappservices"

    
    ## Constants
    
    CONST_EGRESS_TYPE_REDIRECT = "REDIRECT"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_INGRESS_TYPE_REDIRECT = "REDIRECT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_EGRESS_TYPE_ROUTE = "ROUTE"
    
    CONST_INGRESS_TYPE_ROUTE = "ROUTE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ExternalAppService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> externalappservice = NUExternalAppService(id=u'xxxx-xxx-xxx-xxx', name=u'ExternalAppService')
                >>> externalappservice = NUExternalAppService(data=my_dict)
        """

        super(NUExternalAppService, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._description = None
        self._destination_nat_address = None
        self._destination_nat_enabled = None
        self._destination_nat_mask = None
        self._metadata = None
        self._egress_type = None
        self._virtual_ip = None
        self._virtual_ip_required = None
        self._ingress_type = None
        self._entity_scope = None
        self._source_nat_address = None
        self._source_nat_enabled = None
        self._associated_service_egress_group_id = None
        self._associated_service_egress_redirect_id = None
        self._associated_service_ingress_group_id = None
        self._associated_service_ingress_redirect_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_nat_address", remote_name="destinationNATAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_nat_enabled", remote_name="destinationNATEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_nat_mask", remote_name="destinationNATMask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata", remote_name="metadata", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="egress_type", remote_name="egressType", attribute_type=str, is_required=False, is_unique=False, choices=[u'REDIRECT', u'ROUTE'])
        self.expose_attribute(local_name="virtual_ip", remote_name="virtualIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual_ip_required", remote_name="virtualIPRequired", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ingress_type", remote_name="ingressType", attribute_type=str, is_required=False, is_unique=False, choices=[u'REDIRECT', u'ROUTE'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="source_nat_address", remote_name="sourceNATAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_nat_enabled", remote_name="sourceNATEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_service_egress_group_id", remote_name="associatedServiceEgressGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_service_egress_redirect_id", remote_name="associatedServiceEgressRedirectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_service_ingress_group_id", remote_name="associatedServiceIngressGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_service_ingress_redirect_id", remote_name="associatedServiceIngressRedirectID", attribute_type=str, is_required=False, is_unique=False)
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
                Name of the flow.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the flow.

                
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
                Description of the flow.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the flow.

                
        """
        self._description = value

    
    @property
    def destination_nat_address(self):
        """ Get destination_nat_address value.

            Notes:
                Destination NAT Address

                
                This attribute is named `destinationNATAddress` in VSD API.
                
        """
        return self._destination_nat_address

    @destination_nat_address.setter
    def destination_nat_address(self, value):
        """ Set destination_nat_address value.

            Notes:
                Destination NAT Address

                
                This attribute is named `destinationNATAddress` in VSD API.
                
        """
        self._destination_nat_address = value

    
    @property
    def destination_nat_enabled(self):
        """ Get destination_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `destinationNATEnabled` in VSD API.
                
        """
        return self._destination_nat_enabled

    @destination_nat_enabled.setter
    def destination_nat_enabled(self, value):
        """ Set destination_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `destinationNATEnabled` in VSD API.
                
        """
        self._destination_nat_enabled = value

    
    @property
    def destination_nat_mask(self):
        """ Get destination_nat_mask value.

            Notes:
                netmask of the Destination NAT

                
                This attribute is named `destinationNATMask` in VSD API.
                
        """
        return self._destination_nat_mask

    @destination_nat_mask.setter
    def destination_nat_mask(self, value):
        """ Set destination_nat_mask value.

            Notes:
                netmask of the Destination NAT

                
                This attribute is named `destinationNATMask` in VSD API.
                
        """
        self._destination_nat_mask = value

    
    @property
    def metadata(self):
        """ Get metadata value.

            Notes:
                metadata

                
        """
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        """ Set metadata value.

            Notes:
                metadata

                
        """
        self._metadata = value

    
    @property
    def egress_type(self):
        """ Get egress_type value.

            Notes:
                Egress type.

                
                This attribute is named `egressType` in VSD API.
                
        """
        return self._egress_type

    @egress_type.setter
    def egress_type(self, value):
        """ Set egress_type value.

            Notes:
                Egress type.

                
                This attribute is named `egressType` in VSD API.
                
        """
        self._egress_type = value

    
    @property
    def virtual_ip(self):
        """ Get virtual_ip value.

            Notes:
                Virtual IP Address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, value):
        """ Set virtual_ip value.

            Notes:
                Virtual IP Address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        self._virtual_ip = value

    
    @property
    def virtual_ip_required(self):
        """ Get virtual_ip_required value.

            Notes:
                Boolean flag to indicate whether we require a VIP

                
                This attribute is named `virtualIPRequired` in VSD API.
                
        """
        return self._virtual_ip_required

    @virtual_ip_required.setter
    def virtual_ip_required(self, value):
        """ Set virtual_ip_required value.

            Notes:
                Boolean flag to indicate whether we require a VIP

                
                This attribute is named `virtualIPRequired` in VSD API.
                
        """
        self._virtual_ip_required = value

    
    @property
    def ingress_type(self):
        """ Get ingress_type value.

            Notes:
                Ingress type.

                
                This attribute is named `ingressType` in VSD API.
                
        """
        return self._ingress_type

    @ingress_type.setter
    def ingress_type(self, value):
        """ Set ingress_type value.

            Notes:
                Ingress type.

                
                This attribute is named `ingressType` in VSD API.
                
        """
        self._ingress_type = value

    
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
    def source_nat_address(self):
        """ Get source_nat_address value.

            Notes:
                Source NAT Address

                
                This attribute is named `sourceNATAddress` in VSD API.
                
        """
        return self._source_nat_address

    @source_nat_address.setter
    def source_nat_address(self, value):
        """ Set source_nat_address value.

            Notes:
                Source NAT Address

                
                This attribute is named `sourceNATAddress` in VSD API.
                
        """
        self._source_nat_address = value

    
    @property
    def source_nat_enabled(self):
        """ Get source_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `sourceNATEnabled` in VSD API.
                
        """
        return self._source_nat_enabled

    @source_nat_enabled.setter
    def source_nat_enabled(self, value):
        """ Set source_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `sourceNATEnabled` in VSD API.
                
        """
        self._source_nat_enabled = value

    
    @property
    def associated_service_egress_group_id(self):
        """ Get associated_service_egress_group_id value.

            Notes:
                ID of service port group identifying the output ports

                
                This attribute is named `associatedServiceEgressGroupID` in VSD API.
                
        """
        return self._associated_service_egress_group_id

    @associated_service_egress_group_id.setter
    def associated_service_egress_group_id(self, value):
        """ Set associated_service_egress_group_id value.

            Notes:
                ID of service port group identifying the output ports

                
                This attribute is named `associatedServiceEgressGroupID` in VSD API.
                
        """
        self._associated_service_egress_group_id = value

    
    @property
    def associated_service_egress_redirect_id(self):
        """ Get associated_service_egress_redirect_id value.

            Notes:
                the redirect target ID that identifies the output ports

                
                This attribute is named `associatedServiceEgressRedirectID` in VSD API.
                
        """
        return self._associated_service_egress_redirect_id

    @associated_service_egress_redirect_id.setter
    def associated_service_egress_redirect_id(self, value):
        """ Set associated_service_egress_redirect_id value.

            Notes:
                the redirect target ID that identifies the output ports

                
                This attribute is named `associatedServiceEgressRedirectID` in VSD API.
                
        """
        self._associated_service_egress_redirect_id = value

    
    @property
    def associated_service_ingress_group_id(self):
        """ Get associated_service_ingress_group_id value.

            Notes:
                ID of service port group identifying the input ports

                
                This attribute is named `associatedServiceIngressGroupID` in VSD API.
                
        """
        return self._associated_service_ingress_group_id

    @associated_service_ingress_group_id.setter
    def associated_service_ingress_group_id(self, value):
        """ Set associated_service_ingress_group_id value.

            Notes:
                ID of service port group identifying the input ports

                
                This attribute is named `associatedServiceIngressGroupID` in VSD API.
                
        """
        self._associated_service_ingress_group_id = value

    
    @property
    def associated_service_ingress_redirect_id(self):
        """ Get associated_service_ingress_redirect_id value.

            Notes:
                the redirect target ID that identifies the input ports

                
                This attribute is named `associatedServiceIngressRedirectID` in VSD API.
                
        """
        return self._associated_service_ingress_redirect_id

    @associated_service_ingress_redirect_id.setter
    def associated_service_ingress_redirect_id(self, value):
        """ Set associated_service_ingress_redirect_id value.

            Notes:
                the redirect target ID that identifies the input ports

                
                This attribute is named `associatedServiceIngressRedirectID` in VSD API.
                
        """
        self._associated_service_ingress_redirect_id = value

    
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

    

    