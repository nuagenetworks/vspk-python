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


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NULicense(NURESTObject):
    """ Represents a License in the VSD

        Notes:
            Enables retrieval/modification and creation of license files. Most of the attributes are retrieved from the encrypted license. The create API simply provides the encrypted license that is in base64 format.
    """

    __rest_name__ = "license"
    __resource_name__ = "licenses"

    
    ## Constants
    
    CONST_LICENSE_ENCRYPTION_ENCRYPTION_ENABLED = "ENCRYPTION_ENABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_LICENSE_TYPE_CLUSTERED = "CLUSTERED"
    
    CONST_LICENSE_TYPE_STANDARD = "STANDARD"
    
    CONST_LICENSE_ENCRYPTION_ENCRYPTION_DISABLED = "ENCRYPTION_DISABLED"
    
    

    def __init__(self, **kwargs):
        """ Initializes a License instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> license = NULicense(id=u'xxxx-xxx-xxx-xxx', name=u'License')
                >>> license = NULicense(data=my_dict)
        """

        super(NULicense, self).__init__()

        # Read/Write Attributes
        
        self._major_release = None
        self._last_updated_by = None
        self._phone = None
        self._license = None
        self._license_encryption = None
        self._license_id = None
        self._license_type = None
        self._minor_release = None
        self._zip = None
        self._city = None
        self._allowed_cpes_count = None
        self._allowed_nics_count = None
        self._allowed_vms_count = None
        self._allowed_vrsgs_count = None
        self._allowed_vrss_count = None
        self._email = None
        self._encryption_mode = None
        self._entity_scope = None
        self._company = None
        self._country = None
        self._product_version = None
        self._provider = None
        self._is_cluster_license = None
        self._user_name = None
        self._state = None
        self._street = None
        self._customer_key = None
        self._expiration_date = None
        self._external_id = None
        
        self.expose_attribute(local_name="major_release", remote_name="majorRelease", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="phone", remote_name="phone", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="license", remote_name="license", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="license_encryption", remote_name="licenseEncryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENCRYPTION_DISABLED', u'ENCRYPTION_ENABLED'])
        self.expose_attribute(local_name="license_id", remote_name="licenseID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="license_type", remote_name="licenseType", attribute_type=str, is_required=False, is_unique=False, choices=[u'CLUSTERED', u'STANDARD'])
        self.expose_attribute(local_name="minor_release", remote_name="minorRelease", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="zip", remote_name="zip", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="city", remote_name="city", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_cpes_count", remote_name="allowedCPEsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_nics_count", remote_name="allowedNICsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_vms_count", remote_name="allowedVMsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_vrsgs_count", remote_name="allowedVRSGsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="allowed_vrss_count", remote_name="allowedVRSsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="email", remote_name="email", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption_mode", remote_name="encryptionMode", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="company", remote_name="company", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="country", remote_name="country", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="product_version", remote_name="productVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="provider", remote_name="provider", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="is_cluster_license", remote_name="isClusterLicense", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="user_name", remote_name="userName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="state", remote_name="state", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="street", remote_name="street", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="customer_key", remote_name="customerKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="expiration_date", remote_name="expirationDate", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def major_release(self):
        """ Get major_release value.

            Notes:
                Major software release associated with this license

                
                This attribute is named `majorRelease` in VSD API.
                
        """
        return self._major_release

    @major_release.setter
    def major_release(self, value):
        """ Set major_release value.

            Notes:
                Major software release associated with this license

                
                This attribute is named `majorRelease` in VSD API.
                
        """
        self._major_release = value

    
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
    def phone(self):
        """ Get phone value.

            Notes:
                Phone number of the owner associated with the license file

                
        """
        return self._phone

    @phone.setter
    def phone(self, value):
        """ Set phone value.

            Notes:
                Phone number of the owner associated with the license file

                
        """
        self._phone = value

    
    @property
    def license(self):
        """ Get license value.

            Notes:
                Base 64 value of the license

                
        """
        return self._license

    @license.setter
    def license(self, value):
        """ Set license value.

            Notes:
                Base 64 value of the license

                
        """
        self._license = value

    
    @property
    def license_encryption(self):
        """ Get license_encryption value.

            Notes:
                License encryption

                
                This attribute is named `licenseEncryption` in VSD API.
                
        """
        return self._license_encryption

    @license_encryption.setter
    def license_encryption(self, value):
        """ Set license_encryption value.

            Notes:
                License encryption

                
                This attribute is named `licenseEncryption` in VSD API.
                
        """
        self._license_encryption = value

    
    @property
    def license_id(self):
        """ Get license_id value.

            Notes:
                Unique identifier of the license file

                
                This attribute is named `licenseID` in VSD API.
                
        """
        return self._license_id

    @license_id.setter
    def license_id(self, value):
        """ Set license_id value.

            Notes:
                Unique identifier of the license file

                
                This attribute is named `licenseID` in VSD API.
                
        """
        self._license_id = value

    
    @property
    def license_type(self):
        """ Get license_type value.

            Notes:
                

                
                This attribute is named `licenseType` in VSD API.
                
        """
        return self._license_type

    @license_type.setter
    def license_type(self, value):
        """ Set license_type value.

            Notes:
                

                
                This attribute is named `licenseType` in VSD API.
                
        """
        self._license_type = value

    
    @property
    def minor_release(self):
        """ Get minor_release value.

            Notes:
                Minor software release for which this license has been issued

                
                This attribute is named `minorRelease` in VSD API.
                
        """
        return self._minor_release

    @minor_release.setter
    def minor_release(self, value):
        """ Set minor_release value.

            Notes:
                Minor software release for which this license has been issued

                
                This attribute is named `minorRelease` in VSD API.
                
        """
        self._minor_release = value

    
    @property
    def zip(self):
        """ Get zip value.

            Notes:
                Zipcode of the owner associated with the license file

                
        """
        return self._zip

    @zip.setter
    def zip(self, value):
        """ Set zip value.

            Notes:
                Zipcode of the owner associated with the license file

                
        """
        self._zip = value

    
    @property
    def city(self):
        """ Get city value.

            Notes:
                City of the owner associated with the license file

                
        """
        return self._city

    @city.setter
    def city(self, value):
        """ Set city value.

            Notes:
                City of the owner associated with the license file

                
        """
        self._city = value

    
    @property
    def allowed_cpes_count(self):
        """ Get allowed_cpes_count value.

            Notes:
                Maximum number of CPEs enabled with this license. A value of -1 indicates an unlimited number of CPEs

                
                This attribute is named `allowedCPEsCount` in VSD API.
                
        """
        return self._allowed_cpes_count

    @allowed_cpes_count.setter
    def allowed_cpes_count(self, value):
        """ Set allowed_cpes_count value.

            Notes:
                Maximum number of CPEs enabled with this license. A value of -1 indicates an unlimited number of CPEs

                
                This attribute is named `allowedCPEsCount` in VSD API.
                
        """
        self._allowed_cpes_count = value

    
    @property
    def allowed_nics_count(self):
        """ Get allowed_nics_count value.

            Notes:
                Maximum number of NICs allowed. A value of -1 indicates unlimited number of NICs

                
                This attribute is named `allowedNICsCount` in VSD API.
                
        """
        return self._allowed_nics_count

    @allowed_nics_count.setter
    def allowed_nics_count(self, value):
        """ Set allowed_nics_count value.

            Notes:
                Maximum number of NICs allowed. A value of -1 indicates unlimited number of NICs

                
                This attribute is named `allowedNICsCount` in VSD API.
                
        """
        self._allowed_nics_count = value

    
    @property
    def allowed_vms_count(self):
        """ Get allowed_vms_count value.

            Notes:
                Maximum number of VMs enabled with this license. A value of -1 indicates an unlimited number of VMs

                
                This attribute is named `allowedVMsCount` in VSD API.
                
        """
        return self._allowed_vms_count

    @allowed_vms_count.setter
    def allowed_vms_count(self, value):
        """ Set allowed_vms_count value.

            Notes:
                Maximum number of VMs enabled with this license. A value of -1 indicates an unlimited number of VMs

                
                This attribute is named `allowedVMsCount` in VSD API.
                
        """
        self._allowed_vms_count = value

    
    @property
    def allowed_vrsgs_count(self):
        """ Get allowed_vrsgs_count value.

            Notes:
                Maximum number of VRSGs enabled with this license. A value of -1 indicates an unlimited number of VRSGs

                
                This attribute is named `allowedVRSGsCount` in VSD API.
                
        """
        return self._allowed_vrsgs_count

    @allowed_vrsgs_count.setter
    def allowed_vrsgs_count(self, value):
        """ Set allowed_vrsgs_count value.

            Notes:
                Maximum number of VRSGs enabled with this license. A value of -1 indicates an unlimited number of VRSGs

                
                This attribute is named `allowedVRSGsCount` in VSD API.
                
        """
        self._allowed_vrsgs_count = value

    
    @property
    def allowed_vrss_count(self):
        """ Get allowed_vrss_count value.

            Notes:
                Maximum number of VRSs enabled with this license. A value of -1 indicates an unlimited number of VRSs

                
                This attribute is named `allowedVRSsCount` in VSD API.
                
        """
        return self._allowed_vrss_count

    @allowed_vrss_count.setter
    def allowed_vrss_count(self, value):
        """ Set allowed_vrss_count value.

            Notes:
                Maximum number of VRSs enabled with this license. A value of -1 indicates an unlimited number of VRSs

                
                This attribute is named `allowedVRSsCount` in VSD API.
                
        """
        self._allowed_vrss_count = value

    
    @property
    def email(self):
        """ Get email value.

            Notes:
                Email of the owner associated with the license file

                
        """
        return self._email

    @email.setter
    def email(self, value):
        """ Set email value.

            Notes:
                Email of the owner associated with the license file

                
        """
        self._email = value

    
    @property
    def encryption_mode(self):
        """ Get encryption_mode value.

            Notes:
                Indicates if the system is associated with a license that allows encryption or not

                
                This attribute is named `encryptionMode` in VSD API.
                
        """
        return self._encryption_mode

    @encryption_mode.setter
    def encryption_mode(self, value):
        """ Set encryption_mode value.

            Notes:
                Indicates if the system is associated with a license that allows encryption or not

                
                This attribute is named `encryptionMode` in VSD API.
                
        """
        self._encryption_mode = value

    
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
    def company(self):
        """ Get company value.

            Notes:
                Company of the owner associated with the license file

                
        """
        return self._company

    @company.setter
    def company(self, value):
        """ Set company value.

            Notes:
                Company of the owner associated with the license file

                
        """
        self._company = value

    
    @property
    def country(self):
        """ Get country value.

            Notes:
                Country of the owner associated with the license file

                
        """
        return self._country

    @country.setter
    def country(self, value):
        """ Set country value.

            Notes:
                Country of the owner associated with the license file

                
        """
        self._country = value

    
    @property
    def product_version(self):
        """ Get product_version value.

            Notes:
                Version of the product that this license applies to

                
                This attribute is named `productVersion` in VSD API.
                
        """
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        """ Set product_version value.

            Notes:
                Version of the product that this license applies to

                
                This attribute is named `productVersion` in VSD API.
                
        """
        self._product_version = value

    
    @property
    def provider(self):
        """ Get provider value.

            Notes:
                Provider of the license file

                
        """
        return self._provider

    @provider.setter
    def provider(self, value):
        """ Set provider value.

            Notes:
                Provider of the license file

                
        """
        self._provider = value

    
    @property
    def is_cluster_license(self):
        """ Get is_cluster_license value.

            Notes:
                Indicates if the license is associated with standlone or cluster setup of VSD

                
                This attribute is named `isClusterLicense` in VSD API.
                
        """
        return self._is_cluster_license

    @is_cluster_license.setter
    def is_cluster_license(self, value):
        """ Set is_cluster_license value.

            Notes:
                Indicates if the license is associated with standlone or cluster setup of VSD

                
                This attribute is named `isClusterLicense` in VSD API.
                
        """
        self._is_cluster_license = value

    
    @property
    def user_name(self):
        """ Get user_name value.

            Notes:
                The name of the user associated with the license

                
                This attribute is named `userName` in VSD API.
                
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """ Set user_name value.

            Notes:
                The name of the user associated with the license

                
                This attribute is named `userName` in VSD API.
                
        """
        self._user_name = value

    
    @property
    def state(self):
        """ Get state value.

            Notes:
                State of the owner associated with the license file

                
        """
        return self._state

    @state.setter
    def state(self, value):
        """ Set state value.

            Notes:
                State of the owner associated with the license file

                
        """
        self._state = value

    
    @property
    def street(self):
        """ Get street value.

            Notes:
                Address of the owner associated with the license file

                
        """
        return self._street

    @street.setter
    def street(self, value):
        """ Set street value.

            Notes:
                Address of the owner associated with the license file

                
        """
        self._street = value

    
    @property
    def customer_key(self):
        """ Get customer_key value.

            Notes:
                Customer key associated with the licese

                
                This attribute is named `customerKey` in VSD API.
                
        """
        return self._customer_key

    @customer_key.setter
    def customer_key(self, value):
        """ Set customer_key value.

            Notes:
                Customer key associated with the licese

                
                This attribute is named `customerKey` in VSD API.
                
        """
        self._customer_key = value

    
    @property
    def expiration_date(self):
        """ Get expiration_date value.

            Notes:
                Expiration date of this license

                
                This attribute is named `expirationDate` in VSD API.
                
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        """ Set expiration_date value.

            Notes:
                Expiration date of this license

                
                This attribute is named `expirationDate` in VSD API.
                
        """
        self._expiration_date = value

    
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

    

    