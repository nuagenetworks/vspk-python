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


class NUIDPProfileAction(NURESTObject):
    """ Represents a IDPProfileAction in the VSD

        Notes:
            An IDP Profile/Rule Action specifies what signatures to search for in the network traffic, and what action to take if those signatures are found.
    """

    __rest_name__ = "idpprofileaction"
    __resource_name__ = "idpprofileactions"

    
    ## Constants
    
    CONST_ACTION_PROTECT = "PROTECT"
    
    CONST_ACTION_AUDIT = "AUDIT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a IDPProfileAction instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> idpprofileaction = NUIDPProfileAction(id=u'xxxx-xxx-xxx-xxx', name=u'IDPProfileAction')
                >>> idpprofileaction = NUIDPProfileAction(data=my_dict)
        """

        super(NUIDPProfileAction, self).__init__()

        # Read/Write Attributes
        
        self._idp_signatures = None
        self._action = None
        self._priority = None
        self._associated_idp_profile_id = None
        
        self.expose_attribute(local_name="idp_signatures", remote_name="IDPSignatures", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="action", remote_name="action", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUDIT', u'PROTECT'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_idp_profile_id", remote_name="associatedIDPProfileID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def idp_signatures(self):
        """ Get idp_signatures value.

            Notes:
                IDP Signatures to search in network traffic

                
                This attribute is named `IDPSignatures` in VSD API.
                
        """
        return self._idp_signatures

    @idp_signatures.setter
    def idp_signatures(self, value):
        """ Set idp_signatures value.

            Notes:
                IDP Signatures to search in network traffic

                
                This attribute is named `IDPSignatures` in VSD API.
                
        """
        self._idp_signatures = value

    
    @property
    def action(self):
        """ Get action value.

            Notes:
                Specifies what action to take if given signatures is found

                
        """
        return self._action

    @action.setter
    def action(self, value):
        """ Set action value.

            Notes:
                Specifies what action to take if given signatures is found

                
        """
        self._action = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                The priority determines the order of IDP action

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority determines the order of IDP action

                
        """
        self._priority = value

    
    @property
    def associated_idp_profile_id(self):
        """ Get associated_idp_profile_id value.

            Notes:
                The ID of the associated IDP Profile

                
                This attribute is named `associatedIDPProfileID` in VSD API.
                
        """
        return self._associated_idp_profile_id

    @associated_idp_profile_id.setter
    def associated_idp_profile_id(self, value):
        """ Set associated_idp_profile_id value.

            Notes:
                The ID of the associated IDP Profile

                
                This attribute is named `associatedIDPProfileID` in VSD API.
                
        """
        self._associated_idp_profile_id = value

    

    