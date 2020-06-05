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


class NUIDPSignature(NURESTObject):
    """ Represents a IDPSignature in the VSD

        Notes:
            Intrusion Detection & Prevention Signature groups
    """

    __rest_name__ = "idpsignature"
    __resource_name__ = "idpsignatures"

    

    def __init__(self, **kwargs):
        """ Initializes a IDPSignature instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> idpsignature = NUIDPSignature(id=u'xxxx-xxx-xxx-xxx', name=u'IDPSignature')
                >>> idpsignature = NUIDPSignature(data=my_dict)
        """

        super(NUIDPSignature, self).__init__()

        # Read/Write Attributes
        
        self._idp_signatures = None
        
        self.expose_attribute(local_name="idp_signatures", remote_name="IDPSignatures", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def idp_signatures(self):
        """ Get idp_signatures value.

            Notes:
                List of Intrusion Detection & Prevention Signature groups

                
                This attribute is named `IDPSignatures` in VSD API.
                
        """
        return self._idp_signatures

    @idp_signatures.setter
    def idp_signatures(self, value):
        """ Set idp_signatures value.

            Notes:
                List of Intrusion Detection & Prevention Signature groups

                
                This attribute is named `IDPSignatures` in VSD API.
                
        """
        self._idp_signatures = value

    

    