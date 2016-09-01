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


class NUNSGInfo(NURESTObject):
    """ Represents a NSGInfo in the VSD

        Notes:
            Device information coming from the NSG
    """

    __rest_name__ = "nsginfo"
    __resource_name__ = "nsginfos"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_FAMILY_NSG_E = "NSG_E"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_TPM_STATUS_ENABLED_NOT_OPERATIONAL = "ENABLED_NOT_OPERATIONAL"
    
    CONST_TPM_STATUS_ENABLED_OPERATIONAL = "ENABLED_OPERATIONAL"
    
    CONST_FAMILY_NSG_V = "NSG_V"
    
    CONST_TPM_STATUS_UNKNOWN = "UNKNOWN"
    
    CONST_FAMILY_ANY = "ANY"
    
    CONST_TPM_STATUS_DISABLED = "DISABLED"
    
    

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
        self._sku = None
        self._tpm_status = None
        self._cpu_type = None
        self._nsg_version = None
        self._uuid = None
        self._family = None
        self._serial_number = None
        self._libraries = None
        self._entity_scope = None
        self._associated_ns_gateway_id = None
        self._external_id = None
        
        self.expose_attribute(local_name="mac_address", remote_name="MACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sku", remote_name="SKU", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tpm_status", remote_name="TPMStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED_NOT_OPERATIONAL', u'ENABLED_OPERATIONAL', u'UNKNOWN'])
        self.expose_attribute(local_name="cpu_type", remote_name="CPUType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="NSGVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="uuid", remote_name="UUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="family", remote_name="family", attribute_type=str, is_required=False, is_unique=False, choices=[u'ANY', u'NSG_E', u'NSG_V'])
        self.expose_attribute(local_name="serial_number", remote_name="serialNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="libraries", remote_name="libraries", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="associated_ns_gateway_id", remote_name="associatedNSGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac_address(self):
        """ Get mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        """ Set mac_address value.

            Notes:
                MAC Address of the NSG

                
                This attribute is named `MACAddress` in VSD API.
                
        """
        self._mac_address = value

    
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
                TPM status

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        return self._tpm_status

    @tpm_status.setter
    def tpm_status(self, value):
        """ Set tpm_status value.

            Notes:
                TPM status

                
                This attribute is named `TPMStatus` in VSD API.
                
        """
        self._tpm_status = value

    
    @property
    def cpu_type(self):
        """ Get cpu_type value.

            Notes:
                The NSG Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, value):
        """ Set cpu_type value.

            Notes:
                The NSG Processor Type

                
                This attribute is named `CPUType` in VSD API.
                
        """
        self._cpu_type = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The NSG Version

                
                This attribute is named `NSGVersion` in VSD API.
                
        """
        self._nsg_version = value

    
    @property
    def uuid(self):
        """ Get uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """ Set uuid value.

            Notes:
                The Redhat UUID of the NSG

                
                This attribute is named `UUID` in VSD API.
                
        """
        self._uuid = value

    
    @property
    def family(self):
        """ Get family value.

            Notes:
                The NSG Type

                
        """
        return self._family

    @family.setter
    def family(self, value):
        """ Set family value.

            Notes:
                The NSG Type

                
        """
        self._family = value

    
    @property
    def serial_number(self):
        """ Get serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The NSG's serial number

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    
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
    def associated_ns_gateway_id(self):
        """ Get associated_ns_gateway_id value.

            Notes:
                Associated NS Gateway ID

                
                This attribute is named `associatedNSGatewayID` in VSD API.
                
        """
        return self._associated_ns_gateway_id

    @associated_ns_gateway_id.setter
    def associated_ns_gateway_id(self, value):
        """ Set associated_ns_gateway_id value.

            Notes:
                Associated NS Gateway ID

                
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

    

    