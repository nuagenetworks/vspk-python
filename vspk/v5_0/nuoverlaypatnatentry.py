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


class NUOverlayPATNATEntry(NURESTObject):
    """ Represents a OverlayPATNATEntry in the VSD

        Notes:
            None
    """

    __rest_name__ = "overlaypatnatentry"
    __resource_name__ = "overlaypatnatentries"

    

    def __init__(self, **kwargs):
        """ Initializes a OverlayPATNATEntry instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlaypatnatentry = NUOverlayPATNATEntry(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayPATNATEntry')
                >>> overlaypatnatentry = NUOverlayPATNATEntry(data=my_dict)
        """

        super(NUOverlayPATNATEntry, self).__init__()

        # Read/Write Attributes
        
        self._nat_enabled = None
        self._private_ip = None
        self._associated_domain_id = None
        self._associated_link_id = None
        self._public_ip = None
        
        self.expose_attribute(local_name="nat_enabled", remote_name="NATEnabled", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="private_ip", remote_name="privateIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_domain_id", remote_name="associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_link_id", remote_name="associatedLinkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="public_ip", remote_name="publicIP", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def nat_enabled(self):
        """ Get nat_enabled value.

            Notes:
                This flag will determine whether the entry is NAT or PAT.

                
                This attribute is named `NATEnabled` in VSD API.
                
        """
        return self._nat_enabled

    @nat_enabled.setter
    def nat_enabled(self, value):
        """ Set nat_enabled value.

            Notes:
                This flag will determine whether the entry is NAT or PAT.

                
                This attribute is named `NATEnabled` in VSD API.
                
        """
        self._nat_enabled = value

    
    @property
    def private_ip(self):
        """ Get private_ip value.

            Notes:
                Private IP address for the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, value):
        """ Set private_ip value.

            Notes:
                Private IP address for the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        self._private_ip = value

    
    @property
    def associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                The ID of the associated l3-domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    @associated_domain_id.setter
    def associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                The ID of the associated l3-domain.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    
    @property
    def associated_link_id(self):
        """ Get associated_link_id value.

            Notes:
                The ID of the associated domain-link.

                
                This attribute is named `associatedLinkID` in VSD API.
                
        """
        return self._associated_link_id

    @associated_link_id.setter
    def associated_link_id(self, value):
        """ Set associated_link_id value.

            Notes:
                The ID of the associated domain-link.

                
                This attribute is named `associatedLinkID` in VSD API.
                
        """
        self._associated_link_id = value

    
    @property
    def public_ip(self):
        """ Get public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, value):
        """ Set public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        self._public_ip = value

    

    