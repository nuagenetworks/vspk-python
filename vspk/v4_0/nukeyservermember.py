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

from bambou import NURESTObject


class NUKeyServerMember(NURESTObject):
    """ Represents a KeyServerMember in the VSD

        Notes:
            Represents a KeyServer
    """

    __rest_name__ = "keyservermember"
    __resource_name__ = "keyservermembers"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a KeyServerMember instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservermember = NUKeyServerMember(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerMember')
                >>> keyservermember = NUKeyServerMember(data=my_dict)
        """

        super(NUKeyServerMember, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._pem_encoded = None
        self._certificate_serial_number = None
        self._entity_scope = None
        self._fqdn = None
        self._issuer_dn = None
        self._subject_dn = None
        self._public_key = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="pem_encoded", remote_name="pemEncoded", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="certificate_serial_number", remote_name="certificateSerialNumber", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="fqdn", remote_name="fqdn", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="issuer_dn", remote_name="issuerDN", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subject_dn", remote_name="subjectDN", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="public_key", remote_name="publicKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def pem_encoded(self):
        """ Get pem_encoded value.

            Notes:
                PEM Encoded Certificate

                
                This attribute is named `pemEncoded` in VSD API.
                
        """
        return self._pem_encoded

    @pem_encoded.setter
    def pem_encoded(self, value):
        """ Set pem_encoded value.

            Notes:
                PEM Encoded Certificate

                
                This attribute is named `pemEncoded` in VSD API.
                
        """
        self._pem_encoded = value

    
    @property
    def certificate_serial_number(self):
        """ Get certificate_serial_number value.

            Notes:
                Certificate serial number associated to the keyserver private key which it is currently signing with

                
                This attribute is named `certificateSerialNumber` in VSD API.
                
        """
        return self._certificate_serial_number

    @certificate_serial_number.setter
    def certificate_serial_number(self, value):
        """ Set certificate_serial_number value.

            Notes:
                Certificate serial number associated to the keyserver private key which it is currently signing with

                
                This attribute is named `certificateSerialNumber` in VSD API.
                
        """
        self._certificate_serial_number = value

    
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
    def fqdn(self):
        """ Get fqdn value.

            Notes:
                FQDN of the keyserver member

                
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, value):
        """ Set fqdn value.

            Notes:
                FQDN of the keyserver member

                
        """
        self._fqdn = value

    
    @property
    def issuer_dn(self):
        """ Get issuer_dn value.

            Notes:
                Issuer DN

                
                This attribute is named `issuerDN` in VSD API.
                
        """
        return self._issuer_dn

    @issuer_dn.setter
    def issuer_dn(self, value):
        """ Set issuer_dn value.

            Notes:
                Issuer DN

                
                This attribute is named `issuerDN` in VSD API.
                
        """
        self._issuer_dn = value

    
    @property
    def subject_dn(self):
        """ Get subject_dn value.

            Notes:
                Subject DN

                
                This attribute is named `subjectDN` in VSD API.
                
        """
        return self._subject_dn

    @subject_dn.setter
    def subject_dn(self, value):
        """ Set subject_dn value.

            Notes:
                Subject DN

                
                This attribute is named `subjectDN` in VSD API.
                
        """
        self._subject_dn = value

    
    @property
    def public_key(self):
        """ Get public_key value.

            Notes:
                Public Key

                
                This attribute is named `publicKey` in VSD API.
                
        """
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        """ Set public_key value.

            Notes:
                Public Key

                
                This attribute is named `publicKey` in VSD API.
                
        """
        self._public_key = value

    
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

    

    