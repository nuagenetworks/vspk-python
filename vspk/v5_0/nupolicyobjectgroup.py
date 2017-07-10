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



from .fetchers import NUNSGatewaysFetcher

from bambou import NURESTObject


class NUPolicyObjectGroup(NURESTObject):
    """ Represents a PolicyObjectGroup in the VSD

        Notes:
            None
    """

    __rest_name__ = "policyobjectgroup"
    __resource_name__ = "policyobjectgroups"

    
    ## Constants
    
    CONST_TYPE_NSGATEWAY = "NSGateway"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PolicyObjectGroup instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> policyobjectgroup = NUPolicyObjectGroup(id=u'xxxx-xxx-xxx-xxx', name=u'PolicyObjectGroup')
                >>> policyobjectgroup = NUPolicyObjectGroup(data=my_dict)
        """

        super(NUPolicyObjectGroup, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._type = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="type", remote_name="type", attribute_type=str, is_required=False, is_unique=False, choices=[u'NSGateway'])
        

        # Fetchers
        
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self, relationship="member")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Policy Object Group

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Policy Object Group

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Policy Object Group

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Policy Object Group

                
        """
        self._description = value

    
    @property
    def type(self):
        """ Get type value.

            Notes:
                Type of the Policy Object Group

                
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Set type value.

            Notes:
                Type of the Policy Object Group

                
        """
        self._type = value

    

    