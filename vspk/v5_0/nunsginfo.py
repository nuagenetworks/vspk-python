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



from bambou import NURESTObject


class NUNSGInfo(NURESTObject):
    """ Represents a NSGInfo in the VSD

        Notes:
            Device information coming from the NSG
    """

    __rest_name__ = "nsginfo"
    __resource_name__ = "nsginfos"

    
    ## Constants
    
    CONST_FAMILY_NSG_C = "NSG_C"
    
    CONST_FAMILY_NSG_E = "NSG_E"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_PERSONALITY_NSGDUC = "NSGDUC"
    
    CONST_FAMILY_NSG_V = "NSG_V"
    
    CONST_CMD_STATUS_RUNNING = "RUNNING"
    
    CONST_FAMILY_NSG_X = "NSG_X"
    
    CONST_FAMILY_NSG_DOCKER = "NSG_DOCKER"
    
    CONST_FAMILY_NSG_E200 = "NSG_E200"
    
    CONST_CMD_STATUS_COMPLETED = "COMPLETED"
    
    CONST_PERSONALITY_NSG = "NSG"
    
    CONST_CMD_STATUS_FAILED = "FAILED"
    
    CONST_FAMILY_NSG_AZ = "NSG_AZ"
    
    CONST_FAMILY_ANY = "ANY"
    
    CONST_CMD_STATUS_SKIPPED = "SKIPPED"
    
    CONST_CMD_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_FAMILY_NSG_X200 = "NSG_X200"
    
    CONST_FAMILY_NSG_E300 = "NSG_E300"
    
    CONST_CMD_TYPE_NSG_UPGRADE_TO_IMAGE = "NSG_UPGRADE_TO_IMAGE"
    
    CONST_CMD_STATUS_STARTED = "STARTED"
    
    CONST_FAMILY_NSG_AMI = "NSG_AMI"
    
    CONST_CMD_STATUS_ABANDONED = "ABANDONED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_CMD_TYPE_NSG_DOWNLOAD_OS_IMAGE = "NSG_DOWNLOAD_OS_IMAGE"
    
    CONST_PERSONALITY_NSGBR = "NSGBR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsginfo = NUNSGInfo(id=u'xxxx-xxx-xxx-xxx', name=u'NSGInfo')
                >>> nsginfo = NUNSGInfo(data=my_dict)
        """

        super(NUNSGInfo, self).__init__()

        # Read/Write Attributes
        
        self._mac_address = None
        self._aar_application_release_date = None
        self._aar_application_version = None
        self._bios_release_date = None
        self._bios_version = None
        self._sku = None
        self._tpm_status = None
        self._tpm_version = None
        self._cpu_type = None
        self._nsg_version = None
        self._uuid = None
        self._name = None
        self._family = None
        self._patches_detail = None
        self._serial_number = None
        self._personality = None
        self._libraries = None
        self._cmd_detailed_status = None
        self._cmd_detailed_status_code = None
        self._cmd_download_progress = None
        self._cmd_id = None
        self._cmd_last_updated_date = None
        self._cmd_status = None
        self._cmd_type = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._entity_scope = None
        self._bootstrap_status = None
        self._product_name = None
        self._associated_entity_type = None
        self._associated_ns_gateway_id = None
        self._external_id = None
        self._system_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_application_release_date", remote_name="AARApplicationReleaseDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_application_version", remote_name="AARApplicationVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_release_date", remote_name="BIOSReleaseDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bios_version", remote_name="BIOSVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sku", remote_name="SKU", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_status", remote_name="TPMStatus", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_version", remote_name="TPMVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="NSGVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'NSG_AMI', u'NSG_AZ', u'NSG_C', u'NSG_DOCKER', u'NSG_E', u'NSG_E200', u'NSG_E300', u'NSG_V', u'NSG_X', u'NSG_X200'])
        self.expose_attribute(local_name="patches_detail", remote_name="patchesDetail", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="personality", remote_name="personality", attribute_type=str, is_required=False, is_unique=False, choices=[u'NSG', u'NSGBR', u'NSGDUC'])
        self.expose_attribute(local_name="libraries", remote_name="libraries", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_detailed_status", remote_name="cmdDetailedStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_detailed_status_code", remote_name="cmdDetailedStatusCode", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_download_progress", remote_name="cmdDownloadProgress", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_id", remote_name="cmdID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_last_updated_date", remote_name="cmdLastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cmd_status", remote_name="cmdStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ABANDONED', u'COMPLETED', u'FAILED', u'RUNNING', u'SKIPPED', u'STARTED', u'UNKNOWN'])
        self.expose_attribute(local_name="cmd_type", remote_name="cmdType", attribute_type=str, is_required=False, is_unique=False, choices=[u'NSG_DOWNLOAD_OS_IMAGE', u'NSG_UPGRADE_TO_IMAGE'])
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_name", remote_name="enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="bootstrap_status", remote_name="bootstrapStatus", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="product_name", remote_name="productName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_entity_type", remote_name="associatedEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ns_gateway_id", remote_name="associatedNSGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                A comma separated list of MAC Addresses associated to the NSG's interfaces (eg, port1, port2, port3).

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                A comma separated list of MAC Addresses associated to the NSG's interfaces (eg, port1, port2, port3).

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
    @property
    def aar_application_release_date(self):
        """ Get aar_application_release_date value.

            Notes:
                Release Date of the AAR Application

                
                This attribute is named `AARApplicationReleaseDate` in VSD API.
                
        """
        return self._aar_application_release_date

    @aar_application_release_date.setter
    def aar_application_release_date(self, value):
        """ Set aar_application_release_date value.

            Notes:
                Release Date of the AAR Application

                
                This attribute is named `AARApplicationReleaseDate` in VSD API.
                
        """
        self._aar_application_release_date = value

    
    @property
    def aar_application_version(self):
        """ Get aar_application_version value.

            Notes:
                The AAR Application Version

                
                This attribute is named `AARApplicationVersion` in VSD API.
                
        """
        return self._aar_application_version

    @aar_application_version.setter
    def aar_application_version(self, value):
        """ Set aar_application_version value.

            Notes:
                The AAR Application Version

                
                This attribute is named `AARApplicationVersion` in VSD API.
                
        """
        self._aar_application_version = value

    
    @property
    def bios_release_date(self):
        """ Get bios_release_date value.

            Notes:
                Release Date of the NSG BiOS

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        return self._bios_release_date

    @bios_release_date.setter
    def bios_release_date(self, value):
        """ Set bios_release_date value.

            Notes:
                Release Date of the NSG BiOS

                
                This attribute is named `BIOSReleaseDate` in VSD API.
                
        """
        self._bios_release_date = value

    
    @property
    def bios_version(self):
        """ Get bios_version value.

            Notes:
                NSG BIOS Version as received from the NSG during bootstrap or a reboot.  If the information exeeds 255 characters, the extra characters will be truncated.

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        return self._bios_version

    @bios_version.setter
    def bios_version(self, value):
        """ Set bios_version value.

            Notes:
                NSG BIOS Version as received from the NSG during bootstrap or a reboot.  If the information exeeds 255 characters, the extra characters will be truncated.

                
                This attribute is named `BIOSVersion` in VSD API.
                
        """
        self._bios_version = value

    
    @property
    def sku(self):
        """ Get sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        return self._sku

    @sku.setter
    def sku(self, value):
        """ Set sku value.

            Notes:
                The part number of the NSG

                
                This attribute is named `SKU` in VSD API.
                
        """
        self._sku = value

    
    @property
    def tpm_status(self):
        """ Get tpm_status value.

            Notes:
                TPM status code as reported by the NSG during bootstrapping. This informate indicates if TPM is being used in securing the private key/certificate of an NSG. Possible values are 0(Unknown), 1(Enabled_Not_Operational), 2(Enabled_Operational), 3(Disabled).

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        return self._tpm_status

    @tpm_status.setter
    def tpm_status(self, value):
        """ Set tpm_status value.

            Notes:
                TPM status code as reported by the NSG during bootstrapping. This informate indicates if TPM is being used in securing the private key/certificate of an NSG. Possible values are 0(Unknown), 1(Enabled_Not_Operational), 2(Enabled_Operational), 3(Disabled).

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        self._tpm_status = value

    
    @property
    def tpm_version(self):
        """ Get tpm_version value.

            Notes:
                TPM (Trusted Platform Module) version as reported by the NSG.

                
                This attribute is named `TPMVersion` in VSD API.
                
        """
        return self._tpm_version

    @tpm_version.setter
    def tpm_version(self, value):
        """ Set tpm_version value.

            Notes:
                TPM (Trusted Platform Module) version as reported by the NSG.

                
                This attribute is named `TPMVersion` in VSD API.
                
        """
        self._tpm_version = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                The NSG Processor Type based on information extracted during bootstrapping.  This may refer to a type of processor manufactured by Intel, ARM, AMD, Cyrix, VIA, or others.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                The NSG Processor Type based on information extracted during bootstrapping.  This may refer to a type of processor manufactured by Intel, ARM, AMD, Cyrix, VIA, or others.

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The NSG Version as reported during a bootstrap or a reboot of the NSG. 

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The NSG Version as reported during a bootstrap or a reboot of the NSG. 

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        self._nsg_version = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                The Redhat/CentOS UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                The Redhat/CentOS UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Gateway.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Gateway.

                
        """
        self._name = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                The NSG Family type as it was returned by the NSG during bootstrapping.

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The NSG Family type as it was returned by the NSG during bootstrapping.

                
        """
        self._family = value

    
    @property
    def patches_detail(self):
        """ Get patches_detail value.

            Notes:
                Base64 Encoded JSON String of the extra details pertaining to each successfully installed patch

                
                This attribute is named `patchesDetail` in VSD API.
                
        """
        return self._patches_detail

    @patches_detail.setter
    def patches_detail(self, value):
        """ Set patches_detail value.

            Notes:
                Base64 Encoded JSON String of the extra details pertaining to each successfully installed patch

                
                This attribute is named `patchesDetail` in VSD API.
                
        """
        self._patches_detail = value

    
    @property
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The NSG's serial number as it is stored in the system's CMOS (Motherboard)

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The NSG's serial number as it is stored in the system's CMOS (Motherboard)

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
    @property
    def personality(self):
        """ Get personality value.

            Notes:
                Personality of the Gateway.

                
        """
        return self._personality

    @personality.setter
    def personality(self, value):
        """ Set personality value.

            Notes:
                Personality of the Gateway.

                
        """
        self._personality = value

    
    @property
    def libraries(self):
        """ Get libraries value.

            Notes:
                Tracks RPM package installed for some libraries installed on the NSG.

                
        """
        return self._libraries

    @libraries.setter
    def libraries(self, value):
        """ Set libraries value.

            Notes:
                Tracks RPM package installed for some libraries installed on the NSG.

                
        """
        self._libraries = value

    
    @property
    def cmd_detailed_status(self):
        """ Get cmd_detailed_status value.

            Notes:
                Detailed status of the current running or last run command.

                
                This attribute is named `cmdDetailedStatus` in VSD API.
                
        """
        return self._cmd_detailed_status

    @cmd_detailed_status.setter
    def cmd_detailed_status(self, value):
        """ Set cmd_detailed_status value.

            Notes:
                Detailed status of the current running or last run command.

                
                This attribute is named `cmdDetailedStatus` in VSD API.
                
        """
        self._cmd_detailed_status = value

    
    @property
    def cmd_detailed_status_code(self):
        """ Get cmd_detailed_status_code value.

            Notes:
                Numerical value representing the code mapping to detailed status of the current or last command operation.

                
                This attribute is named `cmdDetailedStatusCode` in VSD API.
                
        """
        return self._cmd_detailed_status_code

    @cmd_detailed_status_code.setter
    def cmd_detailed_status_code(self, value):
        """ Set cmd_detailed_status_code value.

            Notes:
                Numerical value representing the code mapping to detailed status of the current or last command operation.

                
                This attribute is named `cmdDetailedStatusCode` in VSD API.
                
        """
        self._cmd_detailed_status_code = value

    
    @property
    def cmd_download_progress(self):
        """ Get cmd_download_progress value.

            Notes:
                DownloadProgress object representing the progress of Gateway image download.

                
                This attribute is named `cmdDownloadProgress` in VSD API.
                
        """
        return self._cmd_download_progress

    @cmd_download_progress.setter
    def cmd_download_progress(self, value):
        """ Set cmd_download_progress value.

            Notes:
                DownloadProgress object representing the progress of Gateway image download.

                
                This attribute is named `cmdDownloadProgress` in VSD API.
                
        """
        self._cmd_download_progress = value

    
    @property
    def cmd_id(self):
        """ Get cmd_id value.

            Notes:
                Identifier of the running or last Command.

                
                This attribute is named `cmdID` in VSD API.
                
        """
        return self._cmd_id

    @cmd_id.setter
    def cmd_id(self, value):
        """ Set cmd_id value.

            Notes:
                Identifier of the running or last Command.

                
                This attribute is named `cmdID` in VSD API.
                
        """
        self._cmd_id = value

    
    @property
    def cmd_last_updated_date(self):
        """ Get cmd_last_updated_date value.

            Notes:
                Time stamp when the command was last updated.

                
                This attribute is named `cmdLastUpdatedDate` in VSD API.
                
        """
        return self._cmd_last_updated_date

    @cmd_last_updated_date.setter
    def cmd_last_updated_date(self, value):
        """ Set cmd_last_updated_date value.

            Notes:
                Time stamp when the command was last updated.

                
                This attribute is named `cmdLastUpdatedDate` in VSD API.
                
        """
        self._cmd_last_updated_date = value

    
    @property
    def cmd_status(self):
        """ Get cmd_status value.

            Notes:
                Status of the current or last command.

                
                This attribute is named `cmdStatus` in VSD API.
                
        """
        return self._cmd_status

    @cmd_status.setter
    def cmd_status(self, value):
        """ Set cmd_status value.

            Notes:
                Status of the current or last command.

                
                This attribute is named `cmdStatus` in VSD API.
                
        """
        self._cmd_status = value

    
    @property
    def cmd_type(self):
        """ Get cmd_type value.

            Notes:
                Specifies the type of command that is stated for execution on the system. A request for download or a request for upgrade.

                
                This attribute is named `cmdType` in VSD API.
                
        """
        return self._cmd_type

    @cmd_type.setter
    def cmd_type(self, value):
        """ Set cmd_type value.

            Notes:
                Specifies the type of command that is stated for execution on the system. A request for download or a request for upgrade.

                
                This attribute is named `cmdType` in VSD API.
                
        """
        self._cmd_type = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this Gateway.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this Gateway.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                Name of the Enterprise associated with this Gateway.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                Name of the Enterprise associated with this Gateway.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    
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
    def bootstrap_status(self):
        """ Get bootstrap_status value.

            Notes:
                The bootstrap status of the NSG from which the infomation was collected.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        return self._bootstrap_status

    @bootstrap_status.setter
    def bootstrap_status(self, value):
        """ Set bootstrap_status value.

            Notes:
                The bootstrap status of the NSG from which the infomation was collected.

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        self._bootstrap_status = value

    
    @property
    def product_name(self):
        """ Get product_name value.

            Notes:
                NSG Product Name as reported when the device bootstraps.

                
                This attribute is named `productName` in VSD API.
                
        """
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        """ Set product_name value.

            Notes:
                NSG Product Name as reported when the device bootstraps.

                
                This attribute is named `productName` in VSD API.
                
        """
        self._product_name = value

    
    @property
    def associated_entity_type(self):
        """ Get associated_entity_type value.

            Notes:
                Object type of the associated entity.

                
                This attribute is named `associatedEntityType` in VSD API.
                
        """
        return self._associated_entity_type

    @associated_entity_type.setter
    def associated_entity_type(self, value):
        """ Set associated_entity_type value.

            Notes:
                Object type of the associated entity.

                
                This attribute is named `associatedEntityType` in VSD API.
                
        """
        self._associated_entity_type = value

    
    @property
    def associated_ns_gateway_id(self):
        """ Get associated_ns_gateway_id value.

            Notes:
                The ID of the NSG from which the infomation was collected.

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        return self._associated_ns_gateway_id

    @associated_ns_gateway_id.setter
    def associated_ns_gateway_id(self, value):
        """ Set associated_ns_gateway_id value.

            Notes:
                The ID of the NSG from which the infomation was collected.

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        self._associated_ns_gateway_id = value

    
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
    def system_id(self):
        """ Get system_id value.

            Notes:
                System identifier of the Gateway.

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                System identifier of the Gateway.

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    