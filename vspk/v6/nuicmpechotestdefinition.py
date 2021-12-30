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


class NUICMPEchoTestDefinition(NURESTObject):
    """ Represents a ICMPEchoTestDefinition in the VSD

        Notes:
            ICMP Echo Test Definition describes the ICMP ping command with parameters to run inside a namespace on NSGateway. This command will be run as per the schedule specified on the Scheduled Test Suite along with the other commands in that suite.
    """

    __rest_name__ = "icmpechotestdefinition"
    __resource_name__ = "icmpechotestdefinitions"

    

    def __init__(self, **kwargs):
        """ Initializes a ICMPEchoTestDefinition instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> icmpechotestdefinition = NUICMPEchoTestDefinition(id=u'xxxx-xxx-xxx-xxx', name=u'ICMPEchoTestDefinition')
                >>> icmpechotestdefinition = NUICMPEchoTestDefinition(data=my_dict)
        """

        super(NUICMPEchoTestDefinition, self).__init__()

        # Read/Write Attributes
        
        self._packet_count = None
        self._packet_interval = None
        self._packet_size = None
        self._name = None
        self._description = None
        self._threshold_average_round_trip_time = None
        self._threshold_packet_loss = None
        self._timeout = None
        self._sla_monitoring = None
        self._donot_fragment = None
        self._tos = None
        
        self.expose_attribute(local_name="packet_count", remote_name="packetCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="packet_interval", remote_name="packetInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="packet_size", remote_name="packetSize", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="threshold_average_round_trip_time", remote_name="thresholdAverageRoundTripTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="threshold_packet_loss", remote_name="thresholdPacketLoss", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="timeout", remote_name="timeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="sla_monitoring", remote_name="slaMonitoring", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="donot_fragment", remote_name="donotFragment", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="tos", remote_name="tos", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def packet_count(self):
        """ Get packet_count value.

            Notes:
                Specifies the number of echo requests to be sent.

                
                This attribute is named `packetCount` in VSD API.
                
        """
        return self._packet_count

    @packet_count.setter
    def packet_count(self, value):
        """ Set packet_count value.

            Notes:
                Specifies the number of echo requests to be sent.

                
                This attribute is named `packetCount` in VSD API.
                
        """
        self._packet_count = value

    
    @property
    def packet_interval(self):
        """ Get packet_interval value.

            Notes:
                Delay in milliseconds between the probes.

                
                This attribute is named `packetInterval` in VSD API.
                
        """
        return self._packet_interval

    @packet_interval.setter
    def packet_interval(self, value):
        """ Set packet_interval value.

            Notes:
                Delay in milliseconds between the probes.

                
                This attribute is named `packetInterval` in VSD API.
                
        """
        self._packet_interval = value

    
    @property
    def packet_size(self):
        """ Get packet_size value.

            Notes:
                Specifies the number of data bytes to be sent.

                
                This attribute is named `packetSize` in VSD API.
                
        """
        return self._packet_size

    @packet_size.setter
    def packet_size(self, value):
        """ Set packet_size value.

            Notes:
                Specifies the number of data bytes to be sent.

                
                This attribute is named `packetSize` in VSD API.
                
        """
        self._packet_size = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A descriptive name for the ICMP Echo Test Definition instance.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A descriptive name for the ICMP Echo Test Definition instance.

                
        """
        self._name = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the ICMP Echo Test Definition instance.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the ICMP Echo Test Definition instance.

                
        """
        self._description = value

    
    @property
    def threshold_average_round_trip_time(self):
        """ Get threshold_average_round_trip_time value.

            Notes:
                The threshold average round trip time KPI in milliseconds that will be monitored when SLA monitoring is enabled.

                
                This attribute is named `thresholdAverageRoundTripTime` in VSD API.
                
        """
        return self._threshold_average_round_trip_time

    @threshold_average_round_trip_time.setter
    def threshold_average_round_trip_time(self, value):
        """ Set threshold_average_round_trip_time value.

            Notes:
                The threshold average round trip time KPI in milliseconds that will be monitored when SLA monitoring is enabled.

                
                This attribute is named `thresholdAverageRoundTripTime` in VSD API.
                
        """
        self._threshold_average_round_trip_time = value

    
    @property
    def threshold_packet_loss(self):
        """ Get threshold_packet_loss value.

            Notes:
                The threshold packet loss percentage KPI to be monitored when SLA monitoring is enabled.

                
                This attribute is named `thresholdPacketLoss` in VSD API.
                
        """
        return self._threshold_packet_loss

    @threshold_packet_loss.setter
    def threshold_packet_loss(self, value):
        """ Set threshold_packet_loss value.

            Notes:
                The threshold packet loss percentage KPI to be monitored when SLA monitoring is enabled.

                
                This attribute is named `thresholdPacketLoss` in VSD API.
                
        """
        self._threshold_packet_loss = value

    
    @property
    def timeout(self):
        """ Get timeout value.

            Notes:
                Timeout value, in seconds, for the test until the system considers it as failed.

                
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """ Set timeout value.

            Notes:
                Timeout value, in seconds, for the test until the system considers it as failed.

                
        """
        self._timeout = value

    
    @property
    def sla_monitoring(self):
        """ Get sla_monitoring value.

            Notes:
                Enables or disables the SLA monitoring.

                
                This attribute is named `slaMonitoring` in VSD API.
                
        """
        return self._sla_monitoring

    @sla_monitoring.setter
    def sla_monitoring(self, value):
        """ Set sla_monitoring value.

            Notes:
                Enables or disables the SLA monitoring.

                
                This attribute is named `slaMonitoring` in VSD API.
                
        """
        self._sla_monitoring = value

    
    @property
    def donot_fragment(self):
        """ Get donot_fragment value.

            Notes:
                Sets the Don't Fragment flag when enabled. When an IP datagram has its DF flag set, intermediate devices are not allowed to fragment it so if it needs to travel across a network with a MTU smaller that datagram length, the datagram will be dropped.

                
                This attribute is named `donotFragment` in VSD API.
                
        """
        return self._donot_fragment

    @donot_fragment.setter
    def donot_fragment(self, value):
        """ Set donot_fragment value.

            Notes:
                Sets the Don't Fragment flag when enabled. When an IP datagram has its DF flag set, intermediate devices are not allowed to fragment it so if it needs to travel across a network with a MTU smaller that datagram length, the datagram will be dropped.

                
                This attribute is named `donotFragment` in VSD API.
                
        """
        self._donot_fragment = value

    
    @property
    def tos(self):
        """ Get tos value.

            Notes:
                This field is used to carry information to provide quality of service features. It is normally used to support Differentiated Services.

                
        """
        return self._tos

    @tos.setter
    def tos(self, value):
        """ Set tos value.

            Notes:
                This field is used to carry information to provide quality of service features. It is normally used to support Differentiated Services.

                
        """
        self._tos = value

    

    