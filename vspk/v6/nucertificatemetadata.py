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


class NUCertificateMetadata(NURESTObject):
    """ Represents a CertificateMetadata in the VSD

        Notes:
            An object to store metadata about an end entity's certificate.
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a CertificateMetadata instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> certificatemetadata = NUCertificateMetadata(id=u'xxxx-xxx-xxx-xxx', name=u'CertificateMetadata')
                >>> certificatemetadata = NUCertificateMetadata(data=my_dict)
        """

        super(NUCertificateMetadata, self).__init__()

        # Read/Write Attributes
        
        self._sha1_fingerprint = None
        self._serial = None
        self._not_after = None
        self._not_before = None
        self._issuer = None
        self._subject = None
        
        self.expose_attribute(local_name="sha1_fingerprint", remote_name="SHA1Fingerprint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="serial", remote_name="serial", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="not_after", remote_name="notAfter", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="not_before", remote_name="notBefore", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="issuer", remote_name="issuer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subject", remote_name="subject", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def sha1_fingerprint(self):
        """ Get sha1_fingerprint value.

            Notes:
                The SHA1 FingerPrint of the certificate.

                
                This attribute is named `SHA1Fingerprint` in VSD API.
                
        """
        return self._sha1_fingerprint

    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value):
        """ Set sha1_fingerprint value.

            Notes:
                The SHA1 FingerPrint of the certificate.

                
                This attribute is named `SHA1Fingerprint` in VSD API.
                
        """
        self._sha1_fingerprint = value

    
    @property
    def serial(self):
        """ Get serial value.

            Notes:
                The unique serial number of the certificate assigned by the certificate authority.

                
        """
        return self._serial

    @serial.setter
    def serial(self, value):
        """ Set serial value.

            Notes:
                The unique serial number of the certificate assigned by the certificate authority.

                
        """
        self._serial = value

    
    @property
    def not_after(self):
        """ Get not_after value.

            Notes:
                The end date of the certificate validity period.

                
                This attribute is named `notAfter` in VSD API.
                
        """
        return self._not_after

    @not_after.setter
    def not_after(self, value):
        """ Set not_after value.

            Notes:
                The end date of the certificate validity period.

                
                This attribute is named `notAfter` in VSD API.
                
        """
        self._not_after = value

    
    @property
    def not_before(self):
        """ Get not_before value.

            Notes:
                The start date of the certificate validity period.

                
                This attribute is named `notBefore` in VSD API.
                
        """
        return self._not_before

    @not_before.setter
    def not_before(self, value):
        """ Set not_before value.

            Notes:
                The start date of the certificate validity period.

                
                This attribute is named `notBefore` in VSD API.
                
        """
        self._not_before = value

    
    @property
    def issuer(self):
        """ Get issuer value.

            Notes:
                The distinguished name of the certificate issuer.

                
        """
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        """ Set issuer value.

            Notes:
                The distinguished name of the certificate issuer.

                
        """
        self._issuer = value

    
    @property
    def subject(self):
        """ Get subject value.

            Notes:
                The subject distinguished name of the certificate.

                
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        """ Set subject value.

            Notes:
                The subject distinguished name of the certificate.

                
        """
        self._subject = value

    

    