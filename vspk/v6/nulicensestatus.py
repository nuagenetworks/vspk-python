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


class NULicenseStatus(NURESTObject):
    """ Represents a LicenseStatus in the VSD

        Notes:
            None
    """

    __rest_name__ = "licensestatus"
    __resource_name__ = "licensestatus"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a LicenseStatus instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> licensestatus = NULicenseStatus(id=u'xxxx-xxx-xxx-xxx', name=u'LicenseStatus')
                >>> licensestatus = NULicenseStatus(data=my_dict)
        """

        super(NULicenseStatus, self).__init__()

        # Read/Write Attributes
        
        self._accumulate_licenses_enabled = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._total_licensed_avrsgs_count = None
        self._total_licensed_avrss_count = None
        self._total_licensed_gateways_count = None
        self._total_licensed_nics_count = None
        self._total_licensed_nsgs_count = None
        self._total_licensed_used_avrsgs_count = None
        self._total_licensed_used_avrss_count = None
        self._total_licensed_used_nics_count = None
        self._total_licensed_used_nsgs_count = None
        self._total_licensed_used_vdfgs_count = None
        self._total_licensed_used_vdfs_count = None
        self._total_licensed_used_vms_count = None
        self._total_licensed_used_vrsgs_count = None
        self._total_licensed_used_vrss_count = None
        self._total_licensed_vdfgs_count = None
        self._total_licensed_vdfs_count = None
        self._total_licensed_vms_count = None
        self._total_licensed_vrsgs_count = None
        self._total_licensed_vrss_count = None
        self._total_used_gateways_count = None
        self._external_id = None
        
        self.expose_attribute(local_name="accumulate_licenses_enabled", remote_name="accumulateLicensesEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="total_licensed_avrsgs_count", remote_name="totalLicensedAVRSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_avrss_count", remote_name="totalLicensedAVRSsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_gateways_count", remote_name="totalLicensedGatewaysCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_nics_count", remote_name="totalLicensedNICsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_nsgs_count", remote_name="totalLicensedNSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_avrsgs_count", remote_name="totalLicensedUsedAVRSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_avrss_count", remote_name="totalLicensedUsedAVRSsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_nics_count", remote_name="totalLicensedUsedNICsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_nsgs_count", remote_name="totalLicensedUsedNSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_vdfgs_count", remote_name="totalLicensedUsedVDFGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_vdfs_count", remote_name="totalLicensedUsedVDFsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_vms_count", remote_name="totalLicensedUsedVMsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_vrsgs_count", remote_name="totalLicensedUsedVRSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_used_vrss_count", remote_name="totalLicensedUsedVRSsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_vdfgs_count", remote_name="totalLicensedVDFGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_vdfs_count", remote_name="totalLicensedVDFsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_vms_count", remote_name="totalLicensedVMsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_vrsgs_count", remote_name="totalLicensedVRSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_licensed_vrss_count", remote_name="totalLicensedVRSsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="total_used_gateways_count", remote_name="totalUsedGatewaysCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def accumulate_licenses_enabled(self):
        """ Get accumulate_licenses_enabled value.

            Notes:
                Whether the various VRS license flavours be merged in one pool

                
                This attribute is named `accumulateLicensesEnabled` in VSD API.
                
        """
        return self._accumulate_licenses_enabled

    @accumulate_licenses_enabled.setter
    def accumulate_licenses_enabled(self, value):
        """ Set accumulate_licenses_enabled value.

            Notes:
                Whether the various VRS license flavours be merged in one pool

                
                This attribute is named `accumulateLicensesEnabled` in VSD API.
                
        """
        self._accumulate_licenses_enabled = value

    
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
    def total_licensed_avrsgs_count(self):
        """ Get total_licensed_avrsgs_count value.

            Notes:
                Indicates total AVRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedAVRSGsCount` in VSD API.
                
        """
        return self._total_licensed_avrsgs_count

    @total_licensed_avrsgs_count.setter
    def total_licensed_avrsgs_count(self, value):
        """ Set total_licensed_avrsgs_count value.

            Notes:
                Indicates total AVRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedAVRSGsCount` in VSD API.
                
        """
        self._total_licensed_avrsgs_count = value

    
    @property
    def total_licensed_avrss_count(self):
        """ Get total_licensed_avrss_count value.

            Notes:
                Indicates total AVRS count for all the licenses in the system

                
                This attribute is named `totalLicensedAVRSsCount` in VSD API.
                
        """
        return self._total_licensed_avrss_count

    @total_licensed_avrss_count.setter
    def total_licensed_avrss_count(self, value):
        """ Set total_licensed_avrss_count value.

            Notes:
                Indicates total AVRS count for all the licenses in the system

                
                This attribute is named `totalLicensedAVRSsCount` in VSD API.
                
        """
        self._total_licensed_avrss_count = value

    
    @property
    def total_licensed_gateways_count(self):
        """ Get total_licensed_gateways_count value.

            Notes:
                 Indicates total VRS+VRSG+VRSB licenses licensed in the system

                
                This attribute is named `totalLicensedGatewaysCount` in VSD API.
                
        """
        return self._total_licensed_gateways_count

    @total_licensed_gateways_count.setter
    def total_licensed_gateways_count(self, value):
        """ Set total_licensed_gateways_count value.

            Notes:
                 Indicates total VRS+VRSG+VRSB licenses licensed in the system

                
                This attribute is named `totalLicensedGatewaysCount` in VSD API.
                
        """
        self._total_licensed_gateways_count = value

    
    @property
    def total_licensed_nics_count(self):
        """ Get total_licensed_nics_count value.

            Notes:
                Indicates total NIC count for all the licenses in the system

                
                This attribute is named `totalLicensedNICsCount` in VSD API.
                
        """
        return self._total_licensed_nics_count

    @total_licensed_nics_count.setter
    def total_licensed_nics_count(self, value):
        """ Set total_licensed_nics_count value.

            Notes:
                Indicates total NIC count for all the licenses in the system

                
                This attribute is named `totalLicensedNICsCount` in VSD API.
                
        """
        self._total_licensed_nics_count = value

    
    @property
    def total_licensed_nsgs_count(self):
        """ Get total_licensed_nsgs_count value.

            Notes:
                Indicates total NSG count for all the licenses in the system

                
                This attribute is named `totalLicensedNSGsCount` in VSD API.
                
        """
        return self._total_licensed_nsgs_count

    @total_licensed_nsgs_count.setter
    def total_licensed_nsgs_count(self, value):
        """ Set total_licensed_nsgs_count value.

            Notes:
                Indicates total NSG count for all the licenses in the system

                
                This attribute is named `totalLicensedNSGsCount` in VSD API.
                
        """
        self._total_licensed_nsgs_count = value

    
    @property
    def total_licensed_used_avrsgs_count(self):
        """ Get total_licensed_used_avrsgs_count value.

            Notes:
                Indicates total used AVRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedAVRSGsCount` in VSD API.
                
        """
        return self._total_licensed_used_avrsgs_count

    @total_licensed_used_avrsgs_count.setter
    def total_licensed_used_avrsgs_count(self, value):
        """ Set total_licensed_used_avrsgs_count value.

            Notes:
                Indicates total used AVRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedAVRSGsCount` in VSD API.
                
        """
        self._total_licensed_used_avrsgs_count = value

    
    @property
    def total_licensed_used_avrss_count(self):
        """ Get total_licensed_used_avrss_count value.

            Notes:
                Indicates total used AVRS count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedAVRSsCount` in VSD API.
                
        """
        return self._total_licensed_used_avrss_count

    @total_licensed_used_avrss_count.setter
    def total_licensed_used_avrss_count(self, value):
        """ Set total_licensed_used_avrss_count value.

            Notes:
                Indicates total used AVRS count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedAVRSsCount` in VSD API.
                
        """
        self._total_licensed_used_avrss_count = value

    
    @property
    def total_licensed_used_nics_count(self):
        """ Get total_licensed_used_nics_count value.

            Notes:
                Indicates total used NIC count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedNICsCount` in VSD API.
                
        """
        return self._total_licensed_used_nics_count

    @total_licensed_used_nics_count.setter
    def total_licensed_used_nics_count(self, value):
        """ Set total_licensed_used_nics_count value.

            Notes:
                Indicates total used NIC count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedNICsCount` in VSD API.
                
        """
        self._total_licensed_used_nics_count = value

    
    @property
    def total_licensed_used_nsgs_count(self):
        """ Get total_licensed_used_nsgs_count value.

            Notes:
                Indicates total used NSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedNSGsCount` in VSD API.
                
        """
        return self._total_licensed_used_nsgs_count

    @total_licensed_used_nsgs_count.setter
    def total_licensed_used_nsgs_count(self, value):
        """ Set total_licensed_used_nsgs_count value.

            Notes:
                Indicates total used NSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedNSGsCount` in VSD API.
                
        """
        self._total_licensed_used_nsgs_count = value

    
    @property
    def total_licensed_used_vdfgs_count(self):
        """ Get total_licensed_used_vdfgs_count value.

            Notes:
                Indicates total used VDFG count for all the licenses in the system.

                
                This attribute is named `totalLicensedUsedVDFGsCount` in VSD API.
                
        """
        return self._total_licensed_used_vdfgs_count

    @total_licensed_used_vdfgs_count.setter
    def total_licensed_used_vdfgs_count(self, value):
        """ Set total_licensed_used_vdfgs_count value.

            Notes:
                Indicates total used VDFG count for all the licenses in the system.

                
                This attribute is named `totalLicensedUsedVDFGsCount` in VSD API.
                
        """
        self._total_licensed_used_vdfgs_count = value

    
    @property
    def total_licensed_used_vdfs_count(self):
        """ Get total_licensed_used_vdfs_count value.

            Notes:
                Indicates total used VDF count for all the licenses in the system.

                
                This attribute is named `totalLicensedUsedVDFsCount` in VSD API.
                
        """
        return self._total_licensed_used_vdfs_count

    @total_licensed_used_vdfs_count.setter
    def total_licensed_used_vdfs_count(self, value):
        """ Set total_licensed_used_vdfs_count value.

            Notes:
                Indicates total used VDF count for all the licenses in the system.

                
                This attribute is named `totalLicensedUsedVDFsCount` in VSD API.
                
        """
        self._total_licensed_used_vdfs_count = value

    
    @property
    def total_licensed_used_vms_count(self):
        """ Get total_licensed_used_vms_count value.

            Notes:
                Indicates total used VM count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVMsCount` in VSD API.
                
        """
        return self._total_licensed_used_vms_count

    @total_licensed_used_vms_count.setter
    def total_licensed_used_vms_count(self, value):
        """ Set total_licensed_used_vms_count value.

            Notes:
                Indicates total used VM count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVMsCount` in VSD API.
                
        """
        self._total_licensed_used_vms_count = value

    
    @property
    def total_licensed_used_vrsgs_count(self):
        """ Get total_licensed_used_vrsgs_count value.

            Notes:
                Indicates total used VRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVRSGsCount` in VSD API.
                
        """
        return self._total_licensed_used_vrsgs_count

    @total_licensed_used_vrsgs_count.setter
    def total_licensed_used_vrsgs_count(self, value):
        """ Set total_licensed_used_vrsgs_count value.

            Notes:
                Indicates total used VRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVRSGsCount` in VSD API.
                
        """
        self._total_licensed_used_vrsgs_count = value

    
    @property
    def total_licensed_used_vrss_count(self):
        """ Get total_licensed_used_vrss_count value.

            Notes:
                Indicates total used VRS count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVRSsCount` in VSD API.
                
        """
        return self._total_licensed_used_vrss_count

    @total_licensed_used_vrss_count.setter
    def total_licensed_used_vrss_count(self, value):
        """ Set total_licensed_used_vrss_count value.

            Notes:
                Indicates total used VRS count for all the licenses in the system

                
                This attribute is named `totalLicensedUsedVRSsCount` in VSD API.
                
        """
        self._total_licensed_used_vrss_count = value

    
    @property
    def total_licensed_vdfgs_count(self):
        """ Get total_licensed_vdfgs_count value.

            Notes:
                Indicates total VDFG count for all the licenses in the system

                
                This attribute is named `totalLicensedVDFGsCount` in VSD API.
                
        """
        return self._total_licensed_vdfgs_count

    @total_licensed_vdfgs_count.setter
    def total_licensed_vdfgs_count(self, value):
        """ Set total_licensed_vdfgs_count value.

            Notes:
                Indicates total VDFG count for all the licenses in the system

                
                This attribute is named `totalLicensedVDFGsCount` in VSD API.
                
        """
        self._total_licensed_vdfgs_count = value

    
    @property
    def total_licensed_vdfs_count(self):
        """ Get total_licensed_vdfs_count value.

            Notes:
                Indicates total VDF count for all the licenses in the system

                
                This attribute is named `totalLicensedVDFsCount` in VSD API.
                
        """
        return self._total_licensed_vdfs_count

    @total_licensed_vdfs_count.setter
    def total_licensed_vdfs_count(self, value):
        """ Set total_licensed_vdfs_count value.

            Notes:
                Indicates total VDF count for all the licenses in the system

                
                This attribute is named `totalLicensedVDFsCount` in VSD API.
                
        """
        self._total_licensed_vdfs_count = value

    
    @property
    def total_licensed_vms_count(self):
        """ Get total_licensed_vms_count value.

            Notes:
                Indicates total VM count for all the licenses in the system

                
                This attribute is named `totalLicensedVMsCount` in VSD API.
                
        """
        return self._total_licensed_vms_count

    @total_licensed_vms_count.setter
    def total_licensed_vms_count(self, value):
        """ Set total_licensed_vms_count value.

            Notes:
                Indicates total VM count for all the licenses in the system

                
                This attribute is named `totalLicensedVMsCount` in VSD API.
                
        """
        self._total_licensed_vms_count = value

    
    @property
    def total_licensed_vrsgs_count(self):
        """ Get total_licensed_vrsgs_count value.

            Notes:
                Indicates total VRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedVRSGsCount` in VSD API.
                
        """
        return self._total_licensed_vrsgs_count

    @total_licensed_vrsgs_count.setter
    def total_licensed_vrsgs_count(self, value):
        """ Set total_licensed_vrsgs_count value.

            Notes:
                Indicates total VRSG count for all the licenses in the system

                
                This attribute is named `totalLicensedVRSGsCount` in VSD API.
                
        """
        self._total_licensed_vrsgs_count = value

    
    @property
    def total_licensed_vrss_count(self):
        """ Get total_licensed_vrss_count value.

            Notes:
                Indicates total VRS count for all the licenses in the system

                
                This attribute is named `totalLicensedVRSsCount` in VSD API.
                
        """
        return self._total_licensed_vrss_count

    @total_licensed_vrss_count.setter
    def total_licensed_vrss_count(self, value):
        """ Set total_licensed_vrss_count value.

            Notes:
                Indicates total VRS count for all the licenses in the system

                
                This attribute is named `totalLicensedVRSsCount` in VSD API.
                
        """
        self._total_licensed_vrss_count = value

    
    @property
    def total_used_gateways_count(self):
        """ Get total_used_gateways_count value.

            Notes:
                Indicates total VRS+VRSG+VRSB+VDF+VDFG licenses used in the system

                
                This attribute is named `totalUsedGatewaysCount` in VSD API.
                
        """
        return self._total_used_gateways_count

    @total_used_gateways_count.setter
    def total_used_gateways_count(self, value):
        """ Set total_used_gateways_count value.

            Notes:
                Indicates total VRS+VRSG+VRSB+VDF+VDFG licenses used in the system

                
                This attribute is named `totalUsedGatewaysCount` in VSD API.
                
        """
        self._total_used_gateways_count = value

    
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

    

    