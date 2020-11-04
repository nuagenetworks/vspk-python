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




from .fetchers import NUL2DomainsFetcher


from .fetchers import NUMACFilterProfilesFetcher


from .fetchers import NUSAPEgressQoSProfilesFetcher


from .fetchers import NUSAPIngressQoSProfilesFetcher


from .fetchers import NUDeploymentFailuresFetcher


from .fetchers import NUPermissionsFetcher


from .fetchers import NUEgressProfilesFetcher


from .fetchers import NUAlarmsFetcher


from .fetchers import NUIngressProfilesFetcher


from .fetchers import NUEnterprisePermissionsFetcher


from .fetchers import NUJobsFetcher


from .fetchers import NUDomainsFetcher


from .fetchers import NUIPFilterProfilesFetcher


from .fetchers import NUIPv6FilterProfilesFetcher


from .fetchers import NUEthernetSegmentGroupsFetcher

from bambou import NURESTObject


class NUEthernetSegmentGWGroup(NURESTObject):
    """ Represents a EthernetSegmentGWGroup in the VSD

        Notes:
            Group of Gateways with common Ethernet Segment IDs (upto 4 Gateways).
    """

    __rest_name__ = "ethernetsegmentgwgroup"
    __resource_name__ = "ethernetsegmentgwgroups"

    
    ## Constants
    
    CONST_PERSONALITY_NETCONF_7X50 = "NETCONF_7X50"
    
    CONST_PERSONALITY_SR_LINUX = "SR_LINUX"
    
    

    def __init__(self, **kwargs):
        """ Initializes a EthernetSegmentGWGroup instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ethernetsegmentgwgroup = NUEthernetSegmentGWGroup(id=u'xxxx-xxx-xxx-xxx', name=u'EthernetSegmentGWGroup')
                >>> ethernetsegmentgwgroup = NUEthernetSegmentGWGroup(data=my_dict)
        """

        super(NUEthernetSegmentGWGroup, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._personality = None
        self._description = None
        self._assoc_gateways_names = None
        self._assoc_gateways_status = None
        self._associated_gateway_ids = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'NETCONF_7X50', u'SR_LINUX'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_gateways_names", remote_name="assocGatewaysNames", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="assoc_gateways_status", remote_name="assocGatewaysStatus", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_gateway_ids", remote_name="associatedGatewayIDs", attribute_type=list, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.mac_filter_profiles = NUMACFilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.sap_egress_qo_s_profiles = NUSAPEgressQoSProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.sap_ingress_qo_s_profiles = NUSAPIngressQoSProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.deployment_failures = NUDeploymentFailuresFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.egress_profiles = NUEgressProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ingress_profiles = NUIngressProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ip_filter_profiles = NUIPFilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ipv6_filter_profiles = NUIPv6FilterProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ethernet_segment_groups = NUEthernetSegmentGroupsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Ethernet Segment Gateway Group.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Ethernet Segment Gateway Group.

                
        """
        self._name = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Ethernet Segment Gateway Group.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Ethernet Segment Gateway Group.

                
        """
        self._personality = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Ethernet Segment Gateway Group.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Ethernet Segment Gateway Group.

                
        """
        self._description = value

    
    @property
    def assoc_gateways_names(self):
        """ Get assoc_gateways_names value.

            Notes:
                Array of the names of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_name>", "<gw2_name>", "<gw3_name>", "<gw4_name>"].

                
                This attribute is named `assocGatewaysNames` in VSD API.
                
        """
        return self._assoc_gateways_names

    @assoc_gateways_names.setter
    def assoc_gateways_names(self, value):
        """ Set assoc_gateways_names value.

            Notes:
                Array of the names of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_name>", "<gw2_name>", "<gw3_name>", "<gw4_name>"].

                
                This attribute is named `assocGatewaysNames` in VSD API.
                
        """
        self._assoc_gateways_names = value

    
    @property
    def assoc_gateways_status(self):
        """ Get assoc_gateways_status value.

            Notes:
                Array of the connection status of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_status>", "<gw2_status>", "<gw3_status>", "<gw4_status>"].

                
                This attribute is named `assocGatewaysStatus` in VSD API.
                
        """
        return self._assoc_gateways_status

    @assoc_gateways_status.setter
    def assoc_gateways_status(self, value):
        """ Set assoc_gateways_status value.

            Notes:
                Array of the connection status of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_status>", "<gw2_status>", "<gw3_status>", "<gw4_status>"].

                
                This attribute is named `assocGatewaysStatus` in VSD API.
                
        """
        self._assoc_gateways_status = value

    
    @property
    def associated_gateway_ids(self):
        """ Get associated_gateway_ids value.

            Notes:
                Array of the UUIDs of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_uuid>", "<gw2_uuid>", "<gw3_uuid>", "<gw4_uuid>"].

                
                This attribute is named `associatedGatewayIDs` in VSD API.
                
        """
        return self._associated_gateway_ids

    @associated_gateway_ids.setter
    def associated_gateway_ids(self, value):
        """ Set associated_gateway_ids value.

            Notes:
                Array of the UUIDs of the Gateways (2, 3, or 4), that constitutes the Gateway Group. For eg: ["<gw1_uuid>", "<gw2_uuid>", "<gw3_uuid>", "<gw4_uuid>"].

                
                This attribute is named `associatedGatewayIDs` in VSD API.
                
        """
        self._associated_gateway_ids = value

    

    