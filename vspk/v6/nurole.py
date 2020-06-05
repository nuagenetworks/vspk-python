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




from .fetchers import NURoleentriesFetcher

from bambou import NURESTObject


class NURole(NURESTObject):
    """ Represents a Role in the VSD

        Notes:
            Entity to create a new role for role based authentication
    """

    __rest_name__ = "role"
    __resource_name__ = "roles"

    

    def __init__(self, **kwargs):
        """ Initializes a Role instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> role = NURole(id=u'xxxx-xxx-xxx-xxx', name=u'Role')
                >>> role = NURole(data=my_dict)
        """

        super(NURole, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._csp_only = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="csp_only", remote_name="cspOnly", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.roleentries = NURoleentriesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the role

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the role

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A brief description of the purpose of the role

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A brief description of the purpose of the role

                
        """
        self._description = value

    
    @property
    def csp_only(self):
        """ Get csp_only value.

            Notes:
                Flag to state if a role is applicable only at the csp level

                
                This attribute is named `cspOnly` in VSD API.
                
        """
        return self._csp_only

    @csp_only.setter
    def csp_only(self, value):
        """ Set csp_only value.

            Notes:
                Flag to state if a role is applicable only at the csp level

                
                This attribute is named `cspOnly` in VSD API.
                
        """
        self._csp_only = value

    

    