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




from .fetchers import NUOverlayManagementSubnetProfilesFetcher

from bambou import NURESTObject


class NUOverlayManagementProfile(NURESTObject):
    """ Represents a OverlayManagementProfile in the VSD

        Notes:
            Overlay Management Profiles link a DNA Subnet used for management traffic and other objects such as Syslog Destinations
    """

    __rest_name__ = "overlaymanagementprofile"
    __resource_name__ = "overlaymanagementprofiles"

    

    def __init__(self, **kwargs):
        """ Initializes a OverlayManagementProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlaymanagementprofile = NUOverlayManagementProfile(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayManagementProfile')
                >>> overlaymanagementprofile = NUOverlayManagementProfile(data=my_dict)
        """

        super(NUOverlayManagementProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.overlay_management_subnet_profiles = NUOverlayManagementSubnetProfilesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the profile

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the profile

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the profile

                
        """
        self._description = value

    

    