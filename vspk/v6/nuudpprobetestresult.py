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


class NUUDPProbeTestResult(NURESTObject):
    """ Represents a UDPProbeTestResult in the VSD

        Notes:
            UDP Probe Test Result
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a UDPProbeTestResult instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> udpprobetestresult = NUUDPProbeTestResult(id=u'xxxx-xxx-xxx-xxx', name=u'UDPProbeTestResult')
                >>> udpprobetestresult = NUUDPProbeTestResult(data=my_dict)
        """

        super(NUUDPProbeTestResult, self).__init__()

        # Read/Write Attributes
        
        self._packet_loss_percent = None
        self._packets_lost = None
        self._packets_received = None
        self._packets_transmitted = None
        
        self.expose_attribute(local_name="packet_loss_percent", remote_name="packetLossPercent", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="packets_lost", remote_name="packetsLost", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="packets_received", remote_name="packetsReceived", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="packets_transmitted", remote_name="packetsTransmitted", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def packet_loss_percent(self):
        """ Get packet_loss_percent value.

            Notes:
                Percentage of packets lost

                
                This attribute is named `packetLossPercent` in VSD API.
                
        """
        return self._packet_loss_percent

    @packet_loss_percent.setter
    def packet_loss_percent(self, value):
        """ Set packet_loss_percent value.

            Notes:
                Percentage of packets lost

                
                This attribute is named `packetLossPercent` in VSD API.
                
        """
        self._packet_loss_percent = value

    
    @property
    def packets_lost(self):
        """ Get packets_lost value.

            Notes:
                The number of packets lost

                
                This attribute is named `packetsLost` in VSD API.
                
        """
        return self._packets_lost

    @packets_lost.setter
    def packets_lost(self, value):
        """ Set packets_lost value.

            Notes:
                The number of packets lost

                
                This attribute is named `packetsLost` in VSD API.
                
        """
        self._packets_lost = value

    
    @property
    def packets_received(self):
        """ Get packets_received value.

            Notes:
                The number of packets received

                
                This attribute is named `packetsReceived` in VSD API.
                
        """
        return self._packets_received

    @packets_received.setter
    def packets_received(self, value):
        """ Set packets_received value.

            Notes:
                The number of packets received

                
                This attribute is named `packetsReceived` in VSD API.
                
        """
        self._packets_received = value

    
    @property
    def packets_transmitted(self):
        """ Get packets_transmitted value.

            Notes:
                The number of packets transmitted

                
                This attribute is named `packetsTransmitted` in VSD API.
                
        """
        return self._packets_transmitted

    @packets_transmitted.setter
    def packets_transmitted(self, value):
        """ Set packets_transmitted value.

            Notes:
                The number of packets transmitted

                
                This attribute is named `packetsTransmitted` in VSD API.
                
        """
        self._packets_transmitted = value

    

    