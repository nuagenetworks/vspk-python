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



from .fetchers import NUVNFInterfaceDescriptorsFetcher

from bambou import NURESTObject


class NUVNFDescriptor(NURESTObject):
    """ Represents a VNFDescriptor in the VSD

        Notes:
            Represent Virtual Network Function Descriptor Object
    """

    __rest_name__ = "vnfdescriptor"
    __resource_name__ = "vnfdescriptors"

    

    def __init__(self, **kwargs):
        """ Initializes a VNFDescriptor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vnfdescriptor = NUVNFDescriptor(id=u'xxxx-xxx-xxx-xxx', name=u'VNFDescriptor')
                >>> vnfdescriptor = NUVNFDescriptor(data=my_dict)
        """

        super(NUVNFDescriptor, self).__init__()

        # Read/Write Attributes
        
        self._cpu_count = None
        self._name = None
        self._memory_mb = None
        self._vendor = None
        self._description = None
        self._metadata_id = None
        self._visible = None
        self._storage_gb = None
        
        self.expose_attribute(local_name="cpu_count", remote_name="CPUCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="memory_mb", remote_name="memoryMB", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="vendor", remote_name="vendor", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_id", remote_name="metadataID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="visible", remote_name="visible", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="storage_gb", remote_name="storageGB", attribute_type=int, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.vnf_interface_descriptors = NUVNFInterfaceDescriptorsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def cpu_count(self):
        """ Get cpu_count value.

            Notes:
                Number of CPUs to be allocated VNF instance when deployed

                
                This attribute is named `CPUCount` in VSD API.
                
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, value):
        """ Set cpu_count value.

            Notes:
                Number of CPUs to be allocated VNF instance when deployed

                
                This attribute is named `CPUCount` in VSD API.
                
        """
        self._cpu_count = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the VNF Descriptor

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the VNF Descriptor

                
        """
        self._name = value

    
    @property
    def memory_mb(self):
        """ Get memory_mb value.

            Notes:
                Memory (in MB) to be allocated for VNF instance when deployed

                
                This attribute is named `memoryMB` in VSD API.
                
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, value):
        """ Set memory_mb value.

            Notes:
                Memory (in MB) to be allocated for VNF instance when deployed

                
                This attribute is named `memoryMB` in VSD API.
                
        """
        self._memory_mb = value

    
    @property
    def vendor(self):
        """ Get vendor value.

            Notes:
                The vendor generating this VNF Descriptor

                
        """
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        """ Set vendor value.

            Notes:
                The vendor generating this VNF Descriptor

                
        """
        self._vendor = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the VNF Descriptor

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the VNF Descriptor

                
        """
        self._description = value

    
    @property
    def metadata_id(self):
        """ Get metadata_id value.

            Notes:
                Id of referenced Metadata Object

                
                This attribute is named `metadataID` in VSD API.
                
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, value):
        """ Set metadata_id value.

            Notes:
                Id of referenced Metadata Object

                
                This attribute is named `metadataID` in VSD API.
                
        """
        self._metadata_id = value

    
    @property
    def visible(self):
        """ Get visible value.

            Notes:
                Controls if descriptor visible in catalog to create new VNF

                
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        """ Set visible value.

            Notes:
                Controls if descriptor visible in catalog to create new VNF

                
        """
        self._visible = value

    
    @property
    def storage_gb(self):
        """ Get storage_gb value.

            Notes:
                Disk storage (in GB) to be allocated VNF instance when deployed

                
                This attribute is named `storageGB` in VSD API.
                
        """
        return self._storage_gb

    @storage_gb.setter
    def storage_gb(self, value):
        """ Set storage_gb value.

            Notes:
                Disk storage (in GB) to be allocated VNF instance when deployed

                
                This attribute is named `storageGB` in VSD API.
                
        """
        self._storage_gb = value

    

    