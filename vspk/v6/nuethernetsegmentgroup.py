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


from .fetchers import NUVLANsFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUEnterprisePermissionsFetcher

from bambou import NURESTObject


class NUEthernetSegmentGroup(NURESTObject):
    """ Represents a EthernetSegmentGroup in the VSD

        Notes:
            Group of Ethernet Segments with same ID.
    """

    __rest_name__ = "ethernetsegmentgroup"
    __resource_name__ = "ethernetsegmentgroups"

    
    ## Constants
    
    CONST_PORT_TYPE_ACCESS = "ACCESS"
    
    

    def __init__(self, **kwargs):
        """ Initializes a EthernetSegmentGroup instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ethernetsegmentgroup = NUEthernetSegmentGroup(id=u'xxxx-xxx-xxx-xxx', name=u'EthernetSegmentGroup')
                >>> ethernetsegmentgroup = NUEthernetSegmentGroup(data=my_dict)
        """

        super(NUEthernetSegmentGroup, self).__init__()

        # Read/Write Attributes
        
        self._vlan_range = None
        self._name = None
        self._description = None
        self._virtual = None
        self._port_type = None
        self._ethernet_segment_id = None
        
        self.expose_attribute(local_name="vlan_range", remote_name="VLANRange", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual", remote_name="virtual", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="port_type", remote_name="portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS'])
        self.expose_attribute(local_name="ethernet_segment_id", remote_name="ethernetSegmentID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vlans = NUVLANsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the EthernetSegment. Format must conform to a-b,c,d-f where a,b,c,d,f are integers from range 0 to 4094.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    @vlan_range.setter
    def vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the EthernetSegment. Format must conform to a-b,c,d-f where a,b,c,d,f are integers from range 0 to 4094.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Ethernet Segment Group

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Ethernet Segment Group

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Ethernet Segment Group

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Ethernet Segment Group

                
        """
        self._description = value

    
    @property
    def virtual(self):
        """ Get virtual value.

            Notes:
                Indicates if Ethernet Segment is Virtual.

                
        """
        return self._virtual

    @virtual.setter
    def virtual(self, value):
        """ Set virtual value.

            Notes:
                Indicates if Ethernet Segment is Virtual.

                
        """
        self._virtual = value

    
    @property
    def port_type(self):
        """ Get port_type value.

            Notes:
                Type of the Port.

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    @port_type.setter
    def port_type(self, value):
        """ Set port_type value.

            Notes:
                Type of the Port.

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    
    @property
    def ethernet_segment_id(self):
        """ Get ethernet_segment_id value.

            Notes:
                Unique Identifier of the Ethernet Segment.

                
                This attribute is named `ethernetSegmentID` in VSD API.
                
        """
        return self._ethernet_segment_id

    @ethernet_segment_id.setter
    def ethernet_segment_id(self, value):
        """ Set ethernet_segment_id value.

            Notes:
                Unique Identifier of the Ethernet Segment.

                
                This attribute is named `ethernetSegmentID` in VSD API.
                
        """
        self._ethernet_segment_id = value

    

    