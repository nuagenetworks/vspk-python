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


class NUAutoDiscoverHypervisorFromDatacenter(NURESTObject):
    """ Represents a AutoDiscoverHypervisorFromDatacenter in the VSD

        Notes:
            None
    """

    __rest_name__ = "autodiscoveredcomputeresource"
    __resource_name__ = "autodiscoveredcomputeresources"

    

    def __init__(self, **kwargs):
        """ Initializes a AutoDiscoverHypervisorFromDatacenter instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> autodiscoverhypervisorfromdatacenter = NUAutoDiscoverHypervisorFromDatacenter(id=u'xxxx-xxx-xxx-xxx', name=u'AutoDiscoverHypervisorFromDatacenter')
                >>> autodiscoverhypervisorfromdatacenter = NUAutoDiscoverHypervisorFromDatacenter(data=my_dict)
        """

        super(NUAutoDiscoverHypervisorFromDatacenter, self).__init__()

        # Read/Write Attributes
        
        self._assoc_vcenter_data_center_id = None
        self._hypervisor_ip = None
        self._network_list = None
        
        self.expose_attribute(local_name="assoc_vcenter_data_center_id", remote_name="assocVCenterDataCenterId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hypervisor_ip", remote_name="hypervisorIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="network_list", remote_name="networkList", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def assoc_vcenter_data_center_id(self):
        """ Get assoc_vcenter_data_center_id value.

            Notes:
                The ID of the vcenter datacenter to which this host is attached

                
                This attribute is named `assocVCenterDataCenterId` in VSD API.
                
        """
        return self._assoc_vcenter_data_center_id

    @assoc_vcenter_data_center_id.setter
    def assoc_vcenter_data_center_id(self, value):
        """ Set assoc_vcenter_data_center_id value.

            Notes:
                The ID of the vcenter datacenter to which this host is attached

                
                This attribute is named `assocVCenterDataCenterId` in VSD API.
                
        """
        self._assoc_vcenter_data_center_id = value

    
    @property
    def hypervisor_ip(self):
        """ Get hypervisor_ip value.

            Notes:
                IP Address of the Hypervisor

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        return self._hypervisor_ip

    @hypervisor_ip.setter
    def hypervisor_ip(self, value):
        """ Set hypervisor_ip value.

            Notes:
                IP Address of the Hypervisor

                
                This attribute is named `hypervisorIP` in VSD API.
                
        """
        self._hypervisor_ip = value

    
    @property
    def network_list(self):
        """ Get network_list value.

            Notes:
                The available network list

                
                This attribute is named `networkList` in VSD API.
                
        """
        return self._network_list

    @network_list.setter
    def network_list(self, value):
        """ Set network_list value.

            Notes:
                The available network list

                
                This attribute is named `networkList` in VSD API.
                
        """
        self._network_list = value

    

    