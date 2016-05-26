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


class NUBGPProfile(NURESTObject):
    """ Represents a BGPProfile in the VSD

        Notes:
            missing documentation.
    """

    __rest_name__ = "bgpprofile"
    __resource_name__ = "bgpprofiles"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a BGPProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bgpprofile = NUBGPProfile(id=u'xxxx-xxx-xxx-xxx', name=u'BGPProfile')
                >>> bgpprofile = NUBGPProfile(data=my_dict)
        """

        super(NUBGPProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._dampening_half_life = None
        self._dampening_max_suppress = None
        self._dampening_name = None
        self._dampening_reuse = None
        self._dampening_suppress = None
        self._description = None
        self._entity_scope = None
        self._associated_export_routing_policy_id = None
        self._associated_import_routing_policy_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="dampening_half_life", remote_name="dampeningHalfLife", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dampening_max_suppress", remote_name="dampeningMaxSuppress", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dampening_name", remote_name="dampeningName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dampening_reuse", remote_name="dampeningReuse", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dampening_suppress", remote_name="dampeningSuppress", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_export_routing_policy_id", remote_name="associatedExportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_import_routing_policy_id", remote_name="associatedImportRoutingPolicyID", attribute_type=str, is_required=False, is_unique=False)
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
                Per enterprise unique name

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Per enterprise unique name

                
        """
        self._name = value

    
    @property
    def dampening_half_life(self):
        """ Get dampening_half_life value.

            Notes:
                The time in minutes to wait before decrementing dampening penalty.

                
                This attribute is named `dampeningHalfLife` in VSD API.
                
        """
        return self._dampening_half_life

    @dampening_half_life.setter
    def dampening_half_life(self, value):
        """ Set dampening_half_life value.

            Notes:
                The time in minutes to wait before decrementing dampening penalty.

                
                This attribute is named `dampeningHalfLife` in VSD API.
                
        """
        self._dampening_half_life = value

    
    @property
    def dampening_max_suppress(self):
        """ Get dampening_max_suppress value.

            Notes:
                The maximum duration in minutes that a route will be suppressed.

                
                This attribute is named `dampeningMaxSuppress` in VSD API.
                
        """
        return self._dampening_max_suppress

    @dampening_max_suppress.setter
    def dampening_max_suppress(self, value):
        """ Set dampening_max_suppress value.

            Notes:
                The maximum duration in minutes that a route will be suppressed.

                
                This attribute is named `dampeningMaxSuppress` in VSD API.
                
        """
        self._dampening_max_suppress = value

    
    @property
    def dampening_name(self):
        """ Get dampening_name value.

            Notes:
                Name for the dampening profile. Unique per enterprise

                
                This attribute is named `dampeningName` in VSD API.
                
        """
        return self._dampening_name

    @dampening_name.setter
    def dampening_name(self, value):
        """ Set dampening_name value.

            Notes:
                Name for the dampening profile. Unique per enterprise

                
                This attribute is named `dampeningName` in VSD API.
                
        """
        self._dampening_name = value

    
    @property
    def dampening_reuse(self):
        """ Get dampening_reuse value.

            Notes:
                This value is compared with penalty to determine route reusability, If the penalty is greater than the suppress limit, the route will be suppressed; if not, it will be reused.

                
                This attribute is named `dampeningReuse` in VSD API.
                
        """
        return self._dampening_reuse

    @dampening_reuse.setter
    def dampening_reuse(self, value):
        """ Set dampening_reuse value.

            Notes:
                This value is compared with penalty to determine route reusability, If the penalty is greater than the suppress limit, the route will be suppressed; if not, it will be reused.

                
                This attribute is named `dampeningReuse` in VSD API.
                
        """
        self._dampening_reuse = value

    
    @property
    def dampening_suppress(self):
        """ Get dampening_suppress value.

            Notes:
                Specifies the penalty that will be used if a route is suppressed.

                
                This attribute is named `dampeningSuppress` in VSD API.
                
        """
        return self._dampening_suppress

    @dampening_suppress.setter
    def dampening_suppress(self, value):
        """ Set dampening_suppress value.

            Notes:
                Specifies the penalty that will be used if a route is suppressed.

                
                This attribute is named `dampeningSuppress` in VSD API.
                
        """
        self._dampening_suppress = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                The description of the BGP Profile

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                The description of the BGP Profile

                
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
    def associated_export_routing_policy_id(self):
        """ Get associated_export_routing_policy_id value.

            Notes:
                export BGP policy ID

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_export_routing_policy_id

    @associated_export_routing_policy_id.setter
    def associated_export_routing_policy_id(self, value):
        """ Set associated_export_routing_policy_id value.

            Notes:
                export BGP policy ID

                
                This attribute is named `associatedExportRoutingPolicyID` in VSD API.
                
        """
        self._associated_export_routing_policy_id = value

    
    @property
    def associated_import_routing_policy_id(self):
        """ Get associated_import_routing_policy_id value.

            Notes:
                import BGP policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        return self._associated_import_routing_policy_id

    @associated_import_routing_policy_id.setter
    def associated_import_routing_policy_id(self, value):
        """ Set associated_import_routing_policy_id value.

            Notes:
                import BGP policy ID

                
                This attribute is named `associatedImportRoutingPolicyID` in VSD API.
                
        """
        self._associated_import_routing_policy_id = value

    
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

    

    