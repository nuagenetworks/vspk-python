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


class NUDomainKindSummary(NURESTObject):
    """ Represents a DomainKindSummary in the VSD

        Notes:
            Represents a readonly domain summary object - various attributes of this object are gathered from Domain, Zones, SubNetwork, NSGInfo objects
    """

    __rest_name__ = "domainkindsummary"
    __resource_name__ = "domainkindsummaries"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DomainKindSummary instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> domainkindsummary = NUDomainKindSummary(id=u'xxxx-xxx-xxx-xxx', name=u'DomainKindSummary')
                >>> domainkindsummary = NUDomainKindSummary(data=my_dict)
        """

        super(NUDomainKindSummary, self).__init__()

        # Read/Write Attributes
        
        self._major_alarms_count = None
        self._last_updated_by = None
        self._gateway_count = None
        self._mesh_group_count = None
        self._minor_alarms_count = None
        self._embedded_metadata = None
        self._info_alarms_count = None
        self._entity_scope = None
        self._domain_kind_description = None
        self._domain_kind_name = None
        self._zone_count = None
        self._traffic_volume = None
        self._critical_alarms_count = None
        self._nsg_count = None
        self._sub_network_count = None
        self._external_id = None
        
        self.expose_attribute(local_name="major_alarms_count", remote_name="majorAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_count", remote_name="gatewayCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mesh_group_count", remote_name="meshGroupCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="minor_alarms_count", remote_name="minorAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="info_alarms_count", remote_name="infoAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="domain_kind_description", remote_name="domainKindDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="domain_kind_name", remote_name="domainKindName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zone_count", remote_name="zoneCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="traffic_volume", remote_name="trafficVolume", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="critical_alarms_count", remote_name="criticalAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_count", remote_name="nsgCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sub_network_count", remote_name="subNetworkCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def major_alarms_count(self):
        """ Get major_alarms_count value.

            Notes:
                Total count of alarms at MAJOR severity

                
                This attribute is named `majorAlarmsCount` in VSD API.
                
        """
        return self._major_alarms_count

    @major_alarms_count.setter
    def major_alarms_count(self, value):
        """ Set major_alarms_count value.

            Notes:
                Total count of alarms at MAJOR severity

                
                This attribute is named `majorAlarmsCount` in VSD API.
                
        """
        self._major_alarms_count = value

    
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
    def gateway_count(self):
        """ Get gateway_count value.

            Notes:
                Total count of gateways in this domain

                
                This attribute is named `gatewayCount` in VSD API.
                
        """
        return self._gateway_count

    @gateway_count.setter
    def gateway_count(self, value):
        """ Set gateway_count value.

            Notes:
                Total count of gateways in this domain

                
                This attribute is named `gatewayCount` in VSD API.
                
        """
        self._gateway_count = value

    
    @property
    def mesh_group_count(self):
        """ Get mesh_group_count value.

            Notes:
                Total count of mesh groups in this domain

                
                This attribute is named `meshGroupCount` in VSD API.
                
        """
        return self._mesh_group_count

    @mesh_group_count.setter
    def mesh_group_count(self, value):
        """ Set mesh_group_count value.

            Notes:
                Total count of mesh groups in this domain

                
                This attribute is named `meshGroupCount` in VSD API.
                
        """
        self._mesh_group_count = value

    
    @property
    def minor_alarms_count(self):
        """ Get minor_alarms_count value.

            Notes:
                Total count of alarms with MINOR severity

                
                This attribute is named `minorAlarmsCount` in VSD API.
                
        """
        return self._minor_alarms_count

    @minor_alarms_count.setter
    def minor_alarms_count(self, value):
        """ Set minor_alarms_count value.

            Notes:
                Total count of alarms with MINOR severity

                
                This attribute is named `minorAlarmsCount` in VSD API.
                
        """
        self._minor_alarms_count = value

    
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
    def info_alarms_count(self):
        """ Get info_alarms_count value.

            Notes:
                Total count of alarms with INFO severity

                
                This attribute is named `infoAlarmsCount` in VSD API.
                
        """
        return self._info_alarms_count

    @info_alarms_count.setter
    def info_alarms_count(self, value):
        """ Set info_alarms_count value.

            Notes:
                Total count of alarms with INFO severity

                
                This attribute is named `infoAlarmsCount` in VSD API.
                
        """
        self._info_alarms_count = value

    
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
    def domain_kind_description(self):
        """ Get domain_kind_description value.

            Notes:
                A description string of the domain that is provided by the user

                
                This attribute is named `domainKindDescription` in VSD API.
                
        """
        return self._domain_kind_description

    @domain_kind_description.setter
    def domain_kind_description(self, value):
        """ Set domain_kind_description value.

            Notes:
                A description string of the domain that is provided by the user

                
                This attribute is named `domainKindDescription` in VSD API.
                
        """
        self._domain_kind_description = value

    
    @property
    def domain_kind_name(self):
        """ Get domain_kind_name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
                This attribute is named `domainKindName` in VSD API.
                
        """
        return self._domain_kind_name

    @domain_kind_name.setter
    def domain_kind_name(self, value):
        """ Set domain_kind_name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
                This attribute is named `domainKindName` in VSD API.
                
        """
        self._domain_kind_name = value

    
    @property
    def zone_count(self):
        """ Get zone_count value.

            Notes:
                Total count of zones in this domain

                
                This attribute is named `zoneCount` in VSD API.
                
        """
        return self._zone_count

    @zone_count.setter
    def zone_count(self, value):
        """ Set zone_count value.

            Notes:
                Total count of zones in this domain

                
                This attribute is named `zoneCount` in VSD API.
                
        """
        self._zone_count = value

    
    @property
    def traffic_volume(self):
        """ Get traffic_volume value.

            Notes:
                Traffic volume within the domain in GB indicating whether the network is running ZERO, light, medium or heavy traffic based on last 24 hours traffic stats

                
                This attribute is named `trafficVolume` in VSD API.
                
        """
        return self._traffic_volume

    @traffic_volume.setter
    def traffic_volume(self, value):
        """ Set traffic_volume value.

            Notes:
                Traffic volume within the domain in GB indicating whether the network is running ZERO, light, medium or heavy traffic based on last 24 hours traffic stats

                
                This attribute is named `trafficVolume` in VSD API.
                
        """
        self._traffic_volume = value

    
    @property
    def critical_alarms_count(self):
        """ Get critical_alarms_count value.

            Notes:
                Total count of alarms with CRITICAL severity

                
                This attribute is named `criticalAlarmsCount` in VSD API.
                
        """
        return self._critical_alarms_count

    @critical_alarms_count.setter
    def critical_alarms_count(self, value):
        """ Set critical_alarms_count value.

            Notes:
                Total count of alarms with CRITICAL severity

                
                This attribute is named `criticalAlarmsCount` in VSD API.
                
        """
        self._critical_alarms_count = value

    
    @property
    def nsg_count(self):
        """ Get nsg_count value.

            Notes:
                Total count of nsg in this domain

                
                This attribute is named `nsgCount` in VSD API.
                
        """
        return self._nsg_count

    @nsg_count.setter
    def nsg_count(self, value):
        """ Set nsg_count value.

            Notes:
                Total count of nsg in this domain

                
                This attribute is named `nsgCount` in VSD API.
                
        """
        self._nsg_count = value

    
    @property
    def sub_network_count(self):
        """ Get sub_network_count value.

            Notes:
                Total count of sub networks in this domain

                
                This attribute is named `subNetworkCount` in VSD API.
                
        """
        return self._sub_network_count

    @sub_network_count.setter
    def sub_network_count(self, value):
        """ Set sub_network_count value.

            Notes:
                Total count of sub networks in this domain

                
                This attribute is named `subNetworkCount` in VSD API.
                
        """
        self._sub_network_count = value

    
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

    

    