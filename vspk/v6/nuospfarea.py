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


from .fetchers import NUOSPFInterfacesFetcher

from bambou import NURESTObject


class NUOSPFArea(NURESTObject):
    """ Represents a OSPFArea in the VSD

        Notes:
            OSPF relies on the concept of logical areas. The use of areas enables the hiding of topology information between areas whilst still providing reachability. Each router in the area shares the same routing tables, which simplifies the network topology and helps to optimize the route calculation algorithm. 
    """

    __rest_name__ = "ospfarea"
    __resource_name__ = "ospfareas"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_DEFAULT_ORIGINATE_OPTION_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_AREA_TYPE_NORMAL = "NORMAL"
    
    CONST_AREA_TYPE_NSSA = "NSSA"
    
    CONST_DEFAULT_ORIGINATE_OPTION_TYPE3 = "TYPE3"
    
    CONST_AREA_TYPE_STUB = "STUB"
    
    CONST_DEFAULT_ORIGINATE_OPTION_TYPE7 = "TYPE7"
    
    

    def __init__(self, **kwargs):
        """ Initializes a OSPFArea instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ospfarea = NUOSPFArea(id=u'xxxx-xxx-xxx-xxx', name=u'OSPFArea')
                >>> ospfarea = NUOSPFArea(data=my_dict)
        """

        super(NUOSPFArea, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._redistribute_external_enabled = None
        self._default_metric = None
        self._default_originate_option = None
        self._description = None
        self._aggregate_area_range = None
        self._aggregate_area_range_nssa = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._area_id = None
        self._area_type = None
        self._summaries_enabled = None
        self._suppress_area_range = None
        self._suppress_area_range_nssa = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redistribute_external_enabled", remote_name="redistributeExternalEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_metric", remote_name="defaultMetric", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="default_originate_option", remote_name="defaultOriginateOption", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'TYPE3', u'TYPE7'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aggregate_area_range", remote_name="aggregateAreaRange", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aggregate_area_range_nssa", remote_name="aggregateAreaRangeNSSA", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="area_id", remote_name="areaID", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="area_type", remote_name="areaType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NORMAL', u'NSSA', u'STUB'])
        self.expose_attribute(local_name="summaries_enabled", remote_name="summariesEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="suppress_area_range", remote_name="suppressAreaRange", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="suppress_area_range_nssa", remote_name="suppressAreaRangeNSSA", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ospf_interfaces = NUOSPFInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

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
    def redistribute_external_enabled(self):
        """ Get redistribute_external_enabled value.

            Notes:
                This flag will determine whether external routes will be redistributed into the area or not. This is enabled only for NSSA areas.

                
                This attribute is named `redistributeExternalEnabled` in VSD API.
                
        """
        return self._redistribute_external_enabled

    @redistribute_external_enabled.setter
    def redistribute_external_enabled(self, value):
        """ Set redistribute_external_enabled value.

            Notes:
                This flag will determine whether external routes will be redistributed into the area or not. This is enabled only for NSSA areas.

                
                This attribute is named `redistributeExternalEnabled` in VSD API.
                
        """
        self._redistribute_external_enabled = value

    
    @property
    def default_metric(self):
        """ Get default_metric value.

            Notes:
                Explicit route cost metric for the default route generated. For STUB areas, it defaults to 1. It is null for the other types of areas.

                
                This attribute is named `defaultMetric` in VSD API.
                
        """
        return self._default_metric

    @default_metric.setter
    def default_metric(self, value):
        """ Set default_metric value.

            Notes:
                Explicit route cost metric for the default route generated. For STUB areas, it defaults to 1. It is null for the other types of areas.

                
                This attribute is named `defaultMetric` in VSD API.
                
        """
        self._default_metric = value

    
    @property
    def default_originate_option(self):
        """ Get default_originate_option value.

            Notes:
                Specifies whether an NSSA area generates a default route, and if it does, whether it is advertised as type 3 LSA or type 7 LSA. If the attribute is set to 'NONE', no default is generated.

                
                This attribute is named `defaultOriginateOption` in VSD API.
                
        """
        return self._default_originate_option

    @default_originate_option.setter
    def default_originate_option(self, value):
        """ Set default_originate_option value.

            Notes:
                Specifies whether an NSSA area generates a default route, and if it does, whether it is advertised as type 3 LSA or type 7 LSA. If the attribute is set to 'NONE', no default is generated.

                
                This attribute is named `defaultOriginateOption` in VSD API.
                
        """
        self._default_originate_option = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of OSPFArea

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of OSPFArea

                
        """
        self._description = value

    
    @property
    def aggregate_area_range(self):
        """ Get aggregate_area_range value.

            Notes:
                Routes (type 3 LSAs) that belong to networks listed here will be aggregated.

                
                This attribute is named `aggregateAreaRange` in VSD API.
                
        """
        return self._aggregate_area_range

    @aggregate_area_range.setter
    def aggregate_area_range(self, value):
        """ Set aggregate_area_range value.

            Notes:
                Routes (type 3 LSAs) that belong to networks listed here will be aggregated.

                
                This attribute is named `aggregateAreaRange` in VSD API.
                
        """
        self._aggregate_area_range = value

    
    @property
    def aggregate_area_range_nssa(self):
        """ Get aggregate_area_range_nssa value.

            Notes:
                Routes (type 7 LSAs) that belong to networks listed here will be aggregated.

                
                This attribute is named `aggregateAreaRangeNSSA` in VSD API.
                
        """
        return self._aggregate_area_range_nssa

    @aggregate_area_range_nssa.setter
    def aggregate_area_range_nssa(self, value):
        """ Set aggregate_area_range_nssa value.

            Notes:
                Routes (type 7 LSAs) that belong to networks listed here will be aggregated.

                
                This attribute is named `aggregateAreaRangeNSSA` in VSD API.
                
        """
        self._aggregate_area_range_nssa = value

    
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
    def area_id(self):
        """ Get area_id value.

            Notes:
                OSPF Area ID

                
                This attribute is named `areaID` in VSD API.
                
        """
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        """ Set area_id value.

            Notes:
                OSPF Area ID

                
                This attribute is named `areaID` in VSD API.
                
        """
        self._area_id = value

    
    @property
    def area_type(self):
        """ Get area_type value.

            Notes:
                Set the OSPF area type. The default value is 'NORMAL', which represents either a backbone area or a standard area. If the areaID is 0, this attribute must be set to 'NORMAL'.

                
                This attribute is named `areaType` in VSD API.
                
        """
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        """ Set area_type value.

            Notes:
                Set the OSPF area type. The default value is 'NORMAL', which represents either a backbone area or a standard area. If the areaID is 0, this attribute must be set to 'NORMAL'.

                
                This attribute is named `areaType` in VSD API.
                
        """
        self._area_type = value

    
    @property
    def summaries_enabled(self):
        """ Get summaries_enabled value.

            Notes:
                This flag determines whether Summaries (Type 3 LSAs) will be redistributed into the area or not. Applicable only to NSSA and Stub area types. Disabling this will make the area a Totally Stub or Totally NSSA area.

                
                This attribute is named `summariesEnabled` in VSD API.
                
        """
        return self._summaries_enabled

    @summaries_enabled.setter
    def summaries_enabled(self, value):
        """ Set summaries_enabled value.

            Notes:
                This flag determines whether Summaries (Type 3 LSAs) will be redistributed into the area or not. Applicable only to NSSA and Stub area types. Disabling this will make the area a Totally Stub or Totally NSSA area.

                
                This attribute is named `summariesEnabled` in VSD API.
                
        """
        self._summaries_enabled = value

    
    @property
    def suppress_area_range(self):
        """ Get suppress_area_range value.

            Notes:
                Routes (type 3 LSAs) that belong to networks listed here will be suppressed.

                
                This attribute is named `suppressAreaRange` in VSD API.
                
        """
        return self._suppress_area_range

    @suppress_area_range.setter
    def suppress_area_range(self, value):
        """ Set suppress_area_range value.

            Notes:
                Routes (type 3 LSAs) that belong to networks listed here will be suppressed.

                
                This attribute is named `suppressAreaRange` in VSD API.
                
        """
        self._suppress_area_range = value

    
    @property
    def suppress_area_range_nssa(self):
        """ Get suppress_area_range_nssa value.

            Notes:
                Routes (type 7 LSAs) that belong to networks listed here will be suppressed.

                
                This attribute is named `suppressAreaRangeNSSA` in VSD API.
                
        """
        return self._suppress_area_range_nssa

    @suppress_area_range_nssa.setter
    def suppress_area_range_nssa(self, value):
        """ Set suppress_area_range_nssa value.

            Notes:
                Routes (type 7 LSAs) that belong to networks listed here will be suppressed.

                
                This attribute is named `suppressAreaRangeNSSA` in VSD API.
                
        """
        self._suppress_area_range_nssa = value

    
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

    

    