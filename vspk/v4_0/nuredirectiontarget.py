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


from .fetchers import NUVirtualIPsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUVPortsFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NURedirectionTarget(NURESTObject):
    """ Represents a RedirectionTarget in the VSD

        Notes:
            A group/collection of vports that belong to the same domain.
    """

    __rest_name__ = "redirectiontarget"
    __resource_name__ = "redirectiontargets"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_END_POINT_TYPE_L3 = "L3"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_END_POINT_TYPE_NONE = "NONE"
    
    CONST_TRIGGER_TYPE_NONE = "NONE"
    
    CONST_END_POINT_TYPE_VIRTUAL_WIRE = "VIRTUAL_WIRE"
    
    CONST_TRIGGER_TYPE_GARP = "GARP"
    
    

    def __init__(self, **kwargs):
        """ Initializes a RedirectionTarget instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> redirectiontarget = NURedirectionTarget(id=u'xxxx-xxx-xxx-xxx', name=u'RedirectionTarget')
                >>> redirectiontarget = NURedirectionTarget(data=my_dict)
        """

        super(NURedirectionTarget, self).__init__()

        # Read/Write Attributes
        
        self._esi = None
        self._name = None
        self._last_updated_by = None
        self._redundancy_enabled = None
        self._template_id = None
        self._description = None
        self._virtual_network_id = None
        self._end_point_type = None
        self._entity_scope = None
        self._trigger_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="esi", remote_name="ESI", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_enabled", remote_name="redundancyEnabled", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual_network_id", remote_name="virtualNetworkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_point_type", remote_name="endPointType", attribute_type=str, is_required=True, is_unique=False, choices=[u'L3', u'NONE', u'VIRTUAL_WIRE'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="trigger_type", remote_name="triggerType", attribute_type=str, is_required=False, is_unique=False, choices=[u'GARP', u'NONE'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def esi(self):
        """ Get esi value.

            Notes:
                ESI id, globally unique

                
                This attribute is named `ESI` in VSD API.
                
        """
        return self._esi

    @esi.setter
    def esi(self, value):
        """ Set esi value.

            Notes:
                ESI id, globally unique

                
                This attribute is named `ESI` in VSD API.
                
        """
        self._esi = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of this redirection target

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of this redirection target

                
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
    def redundancy_enabled(self):
        """ Get redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        return self._redundancy_enabled

    @redundancy_enabled.setter
    def redundancy_enabled(self, value):
        """ Set redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        self._redundancy_enabled = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                Template to which this redirection target belongs to

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                Template to which this redirection target belongs to

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of this redirection target

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of this redirection target

                
        """
        self._description = value

    
    @property
    def virtual_network_id(self):
        """ Get virtual_network_id value.

            Notes:
                Auto Generated by VSD. Each vPortTag with redundancy=enable and EndpointType != none will have a globally unique ESI & VNID generated by VSD

                
                This attribute is named `virtualNetworkID` in VSD API.
                
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, value):
        """ Set virtual_network_id value.

            Notes:
                Auto Generated by VSD. Each vPortTag with redundancy=enable and EndpointType != none will have a globally unique ESI & VNID generated by VSD

                
                This attribute is named `virtualNetworkID` in VSD API.
                
        """
        self._virtual_network_id = value

    
    @property
    def end_point_type(self):
        """ Get end_point_type value.

            Notes:
                EndpointType defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. NONE type is deprecated. Possible values are NONE, L3, VIRTUAL_WIRE, .

                
                This attribute is named `endPointType` in VSD API.
                
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, value):
        """ Set end_point_type value.

            Notes:
                EndpointType defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. NONE type is deprecated. Possible values are NONE, L3, VIRTUAL_WIRE, .

                
                This attribute is named `endPointType` in VSD API.
                
        """
        self._end_point_type = value

    
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
    def trigger_type(self):
        """ Get trigger_type value.

            Notes:
                Trigger type, THIS IS READ ONLY. Possible values are NONE, GARP, .

                
                This attribute is named `triggerType` in VSD API.
                
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, value):
        """ Set trigger_type value.

            Notes:
                Trigger type, THIS IS READ ONLY. Possible values are NONE, GARP, .

                
                This attribute is named `triggerType` in VSD API.
                
        """
        self._trigger_type = value

    
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

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
    