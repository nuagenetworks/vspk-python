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


from .fetchers import NUVNFInterfaceDescriptorsFetcher

from bambou import NURESTObject


class NUVNFDescriptor(NURESTObject):
    """ Represents a VNFDescriptor in the VSD

        Notes:
            The behavioral and deployment information of a VNF is defined in the VNF descriptor template. The template is based on the libvirt domain XML and is on-boarded in a VNF catalog. The resource requirements for CPU, memory and storage are defined in this screen and the rest of the template is inherited from the VNF Metadata object.
    """

    __rest_name__ = "vnfdescriptor"
    __resource_name__ = "vnfdescriptors"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TYPE_FIREWALL = "FIREWALL"
    
    CONST_TYPE_WAN_OPT = "WAN_OPT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

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
        self._embedded_metadata = None
        self._entity_scope = None
        self._associated_vnf_threshold_policy_id = None
        self._storage_gb = None
        self._external_id = None
        self._type = None
        
        self.expose_attribute(local_name="cpu_count", remote_name="CPUCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="memory_mb", remote_name="memoryMB", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="vendor", remote_name="vendor", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_id", remote_name="metadataID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="visible", remote_name="visible", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_vnf_threshold_policy_id", remote_name="associatedVNFThresholdPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="storage_gb", remote_name="storageGB", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'FIREWALL', u'WAN_OPT'])
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
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
    def associated_vnf_threshold_policy_id(self):
        """ Get associated_vnf_threshold_policy_id value.

            Notes:
                The Id of referenced VNF threshold policy

                
                This attribute is named `associatedVNFThresholdPolicyID` in VSD API.
                
        """
        return self._associated_vnf_threshold_policy_id

    @associated_vnf_threshold_policy_id.setter
    def associated_vnf_threshold_policy_id(self, value):
        """ Set associated_vnf_threshold_policy_id value.

            Notes:
                The Id of referenced VNF threshold policy

                
                This attribute is named `associatedVNFThresholdPolicyID` in VSD API.
                
        """
        self._associated_vnf_threshold_policy_id = value

    
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

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                Type of virtual network function

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Type of virtual network function

                
        """
        self._type = value

    

    