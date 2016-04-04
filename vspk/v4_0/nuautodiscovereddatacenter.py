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


class NUAutodiscovereddatacenter(NURESTObject):
    """ Represents a Autodiscovereddatacenter in the VSD

        Notes:
            None
    """

    __rest_name__ = "autodiscovereddatacenter"
    __resource_name__ = "autodiscovereddatacenters"

    

    def __init__(self, **kwargs):
        """ Initializes a Autodiscovereddatacenter instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> autodiscovereddatacenter = NUAutodiscovereddatacenter(id=u'xxxx-xxx-xxx-xxx', name=u'Autodiscovereddatacenter')
                >>> autodiscovereddatacenter = NUAutodiscovereddatacenter(data=my_dict)
        """

        super(NUAutodiscovereddatacenter, self).__init__()

        # Read/Write Attributes
        
        self._assoc_vcenter_id = None
        self._managed_object_id = None
        self._name = None
        
        self.expose_attribute(local_name="assoc_vcenter_id", remote_name="assocVCenterId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="managed_object_id", remote_name="managedObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def assoc_vcenter_id(self):
        """ Get assoc_vcenter_id value.

            Notes:
                The ID of the vcenter to which this host is attached

                
                This attribute is named `assocVCenterId` in VSD API.
                
        """
        return self._assoc_vcenter_id

    @assoc_vcenter_id.setter
    def assoc_vcenter_id(self, value):
        """ Set assoc_vcenter_id value.

            Notes:
                The ID of the vcenter to which this host is attached

                
                This attribute is named `assocVCenterId` in VSD API.
                
        """
        self._assoc_vcenter_id = value

    
    @property
    def managed_object_id(self):
        """ Get managed_object_id value.

            Notes:
                VCenter Managed Object ID of the Datacenter

                
                This attribute is named `managedObjectID` in VSD API.
                
        """
        return self._managed_object_id

    @managed_object_id.setter
    def managed_object_id(self, value):
        """ Set managed_object_id value.

            Notes:
                VCenter Managed Object ID of the Datacenter

                
                This attribute is named `managedObjectID` in VSD API.
                
        """
        self._managed_object_id = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    

    