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




from .fetchers import NUIDPProfileActionsFetcher

from bambou import NURESTObject


class NUIDPProfile(NURESTObject):
    """ Represents a IDPProfile in the VSD

        Notes:
            IDP Profile/Rules are used to detect intrusion attempts and/or inspect network traffic and take appropriate action.
    """

    __rest_name__ = "idpprofile"
    __resource_name__ = "idpprofiles"

    

    def __init__(self, **kwargs):
        """ Initializes a IDPProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> idpprofile = NUIDPProfile(id=u'xxxx-xxx-xxx-xxx', name=u'IDPProfile')
                >>> idpprofile = NUIDPProfile(data=my_dict)
        """

        super(NUIDPProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._protect_against_insertion_evasion = None
        self._associated_enterprise_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="protect_against_insertion_evasion", remote_name="protectAgainstInsertionEvasion", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_enterprise_id", remote_name="associatedEnterpriseID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.idp_profile_actions = NUIDPProfileActionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Symbolic name of the IDP Rule

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Symbolic name of the IDP Rule

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Descriptive text for IDP Profile

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Descriptive text for IDP Profile

                
        """
        self._description = value

    
    @property
    def protect_against_insertion_evasion(self):
        """ Get protect_against_insertion_evasion value.

            Notes:
                Enable protection against insertion/evasion attacks.

                
                This attribute is named `protectAgainstInsertionEvasion` in VSD API.
                
        """
        return self._protect_against_insertion_evasion

    @protect_against_insertion_evasion.setter
    def protect_against_insertion_evasion(self, value):
        """ Set protect_against_insertion_evasion value.

            Notes:
                Enable protection against insertion/evasion attacks.

                
                This attribute is named `protectAgainstInsertionEvasion` in VSD API.
                
        """
        self._protect_against_insertion_evasion = value

    
    @property
    def associated_enterprise_id(self):
        """ Get associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        return self._associated_enterprise_id

    @associated_enterprise_id.setter
    def associated_enterprise_id(self, value):
        """ Set associated_enterprise_id value.

            Notes:
                The ID of the associated Enterprise

                
                This attribute is named `associatedEnterpriseID` in VSD API.
                
        """
        self._associated_enterprise_id = value

    

    