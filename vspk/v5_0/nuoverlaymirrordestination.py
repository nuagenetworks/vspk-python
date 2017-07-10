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


from bambou import NURESTObject


class NUOverlayMirrorDestination(NURESTObject):
    """ Represents a OverlayMirrorDestination in the VSD

        Notes:
            None
    """

    __rest_name__ = "overlaymirrordestination"
    __resource_name__ = "overlaymirrordestinations"

    
    ## Constants
    
    CONST_TRIGGER_TYPE_GARP = "GARP"
    
    CONST_END_POINT_TYPE_VIRTUAL_WIRE = "VIRTUAL_WIRE"
    
    CONST_TRIGGER_TYPE_NONE = "NONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a OverlayMirrorDestination instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlaymirrordestination = NUOverlayMirrorDestination(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayMirrorDestination')
                >>> overlaymirrordestination = NUOverlayMirrorDestination(data=my_dict)
        """

        super(NUOverlayMirrorDestination, self).__init__()

        # Read/Write Attributes
        
        self._esi = None
        self._name = None
        self._redundancy_enabled = None
        self._template_id = None
        self._description = None
        self._virtual_network_id = None
        self._end_point_type = None
        self._trigger_type = None
        
        self.expose_attribute(local_name="esi", remote_name="ESI", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="redundancy_enabled", remote_name="redundancyEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual_network_id", remote_name="virtualNetworkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="end_point_type", remote_name="endPointType", attribute_type=str, is_required=True, is_unique=False, choices=[u'VIRTUAL_WIRE'])
        self.expose_attribute(local_name="trigger_type", remote_name="triggerType", attribute_type=str, is_required=False, is_unique=False, choices=[u'GARP', u'NONE'])
        

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
                Name of this overlay mirror destination

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of this overlay mirror destination

                
        """
        self._name = value

    
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
                Template to which this overlay mirror destination belongs to

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                Template to which this overlay mirror destination belongs to

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of this overlay mirror destination

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of this overlay mirror destination

                
        """
        self._description = value

    
    @property
    def virtual_network_id(self):
        """ Get virtual_network_id value.

            Notes:
                Auto Generated by VSD. Each overlay mirror destination with redundancy=enable and EndpointType != none will have a globally unique ESI & VNID generated by VSD

                
                This attribute is named `virtualNetworkID` in VSD API.
                
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, value):
        """ Set virtual_network_id value.

            Notes:
                Auto Generated by VSD. Each overlay mirror destination with redundancy=enable and EndpointType != none will have a globally unique ESI & VNID generated by VSD

                
                This attribute is named `virtualNetworkID` in VSD API.
                
        """
        self._virtual_network_id = value

    
    @property
    def end_point_type(self):
        """ Get end_point_type value.

            Notes:
                EndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a mirror destination. Possible value is VIRTUAL_WIRE

                
                This attribute is named `endPointType` in VSD API.
                
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, value):
        """ Set end_point_type value.

            Notes:
                EndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a mirror destination. Possible value is VIRTUAL_WIRE

                
                This attribute is named `endPointType` in VSD API.
                
        """
        self._end_point_type = value

    
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

    

    