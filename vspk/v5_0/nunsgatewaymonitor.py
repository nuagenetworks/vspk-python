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


class NUNSGatewayMonitor(NURESTObject):
    """ Represents a NSGatewayMonitor in the VSD

        Notes:
            This API can be used to gather read-only information about an NSG, including information on its state, system metrics, alarm counts, location and version. It is a single view of the full data available for an NSG.
    """

    __rest_name__ = "nsgatewaysmonitor"
    __resource_name__ = "nsgatewaysmonitors"

    

    def __init__(self, **kwargs):
        """ Initializes a NSGatewayMonitor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgatewaymonitor = NUNSGatewayMonitor(id=u'xxxx-xxx-xxx-xxx', name=u'NSGatewayMonitor')
                >>> nsgatewaymonitor = NUNSGatewayMonitor(data=my_dict)
        """

        super(NUNSGatewayMonitor, self).__init__()

        # Read/Write Attributes
        
        self._vrsinfo = None
        self._vscs = None
        self._nsginfo = None
        self._nsgstate = None
        self._nsgsummary = None
        
        self.expose_attribute(local_name="vrsinfo", remote_name="vrsinfo", attribute_type=dict, is_required=False, is_unique=True)
        self.expose_attribute(local_name="vscs", remote_name="vscs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsginfo", remote_name="nsginfo", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsgstate", remote_name="nsgstate", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsgsummary", remote_name="nsgsummary", attribute_type=dict, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vrsinfo(self):
        """ Get vrsinfo value.

            Notes:
                information about VRS reported from sysmon in JSON format. Has info about cpu usage, memory usage, physical interfaces etc.

                
        """
        return self._vrsinfo

    @vrsinfo.setter
    def vrsinfo(self, value):
        """ Set vrsinfo value.

            Notes:
                information about VRS reported from sysmon in JSON format. Has info about cpu usage, memory usage, physical interfaces etc.

                
        """
        self._vrsinfo = value

    
    @property
    def vscs(self):
        """ Get vscs value.

            Notes:
                List of controllers associated with the nsg

                
        """
        return self._vscs

    @vscs.setter
    def vscs(self, value):
        """ Set vscs value.

            Notes:
                List of controllers associated with the nsg

                
        """
        self._vscs = value

    
    @property
    def nsginfo(self):
        """ Get nsginfo value.

            Notes:
                An embedded object from the nsinfo entity from VSD. Contains info such as software version, CPU type, BIOS version etc. The embedded object is returned in JSON format

                
        """
        return self._nsginfo

    @nsginfo.setter
    def nsginfo(self, value):
        """ Set nsginfo value.

            Notes:
                An embedded object from the nsinfo entity from VSD. Contains info such as software version, CPU type, BIOS version etc. The embedded object is returned in JSON format

                
        """
        self._nsginfo = value

    
    @property
    def nsgstate(self):
        """ Get nsgstate value.

            Notes:
                Information from the NSGState object in VSD in JSON format. Contains information about connection status, TPM status, operation mode etc.

                
        """
        return self._nsgstate

    @nsgstate.setter
    def nsgstate(self, value):
        """ Set nsgstate value.

            Notes:
                Information from the NSGState object in VSD in JSON format. Contains information about connection status, TPM status, operation mode etc.

                
        """
        self._nsgstate = value

    
    @property
    def nsgsummary(self):
        """ Get nsgsummary value.

            Notes:
                NSG summary in JSON format - contains alarm counts, locality, bootstrap info etc.

                
        """
        return self._nsgsummary

    @nsgsummary.setter
    def nsgsummary(self, value):
        """ Set nsgsummary value.

            Notes:
                NSG summary in JSON format - contains alarm counts, locality, bootstrap info etc.

                
        """
        self._nsgsummary = value

    

    