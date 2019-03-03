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


class NUOverlayManagementSubnetProfile(NURESTObject):
    """ Represents a OverlayManagementSubnetProfile in the VSD

        Notes:
            The Overlay Management Subnet profile that maps to a DNA subnet and contains the syslog destinations. Where DNS means Do Not Advertise (Advertise=False)
    """

    __rest_name__ = "overlaymanagementsubnetprofile"
    __resource_name__ = "overlaymanagementsubnetprofiles"

    

    def __init__(self, **kwargs):
        """ Initializes a OverlayManagementSubnetProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> overlaymanagementsubnetprofile = NUOverlayManagementSubnetProfile(id=u'xxxx-xxx-xxx-xxx', name=u'OverlayManagementSubnetProfile')
                >>> overlaymanagementsubnetprofile = NUOverlayManagementSubnetProfile(data=my_dict)
        """

        super(NUOverlayManagementSubnetProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._description = None
        self._associated_dna_subnet_id = None
        self._syslog_destination_ids = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_dna_subnet_id", remote_name="associatedDNASubnetID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="syslog_destination_ids", remote_name="syslogDestinationIDs", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the profile

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the profile

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the profile

                
        """
        self._description = value

    
    @property
    def associated_dna_subnet_id(self):
        """ Get associated_dna_subnet_id value.

            Notes:
                The DNA Subnet ID associated with this profile. Where DNS means Do Not Advertise (Advertise=False)

                
                This attribute is named `associatedDNASubnetID` in VSD API.
                
        """
        return self._associated_dna_subnet_id

    @associated_dna_subnet_id.setter
    def associated_dna_subnet_id(self, value):
        """ Set associated_dna_subnet_id value.

            Notes:
                The DNA Subnet ID associated with this profile. Where DNS means Do Not Advertise (Advertise=False)

                
                This attribute is named `associatedDNASubnetID` in VSD API.
                
        """
        self._associated_dna_subnet_id = value

    
    @property
    def syslog_destination_ids(self):
        """ Get syslog_destination_ids value.

            Notes:
                JSON list of strings, each being a Syslog Destination ID which needs to be attached to this profile. Can be 0 to 2 IDs in the list

                
                This attribute is named `syslogDestinationIDs` in VSD API.
                
        """
        return self._syslog_destination_ids

    @syslog_destination_ids.setter
    def syslog_destination_ids(self, value):
        """ Set syslog_destination_ids value.

            Notes:
                JSON list of strings, each being a Syslog Destination ID which needs to be attached to this profile. Can be 0 to 2 IDs in the list

                
                This attribute is named `syslogDestinationIDs` in VSD API.
                
        """
        self._syslog_destination_ids = value

    

    