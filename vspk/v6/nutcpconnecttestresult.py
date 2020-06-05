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


class NUTCPConnectTestResult(NURESTObject):
    """ Represents a TCPConnectTestResult in the VSD

        Notes:
            TCP Connect Test Result
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a TCPConnectTestResult instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> tcpconnecttestresult = NUTCPConnectTestResult(id=u'xxxx-xxx-xxx-xxx', name=u'TCPConnectTestResult')
                >>> tcpconnecttestresult = NUTCPConnectTestResult(data=my_dict)
        """

        super(NUTCPConnectTestResult, self).__init__()

        # Read/Write Attributes
        
        self._failed_attempts = None
        self._failed_percent = None
        self._maximum_round_trip_time = None
        self._minimum_round_trip_time = None
        self._connection_attempts = None
        self._successful_connections = None
        self._average_round_trip_time = None
        
        self.expose_attribute(local_name="failed_attempts", remote_name="failedAttempts", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="failed_percent", remote_name="failedPercent", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maximum_round_trip_time", remote_name="maximumRoundTripTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="minimum_round_trip_time", remote_name="minimumRoundTripTime", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="connection_attempts", remote_name="connectionAttempts", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="successful_connections", remote_name="successfulConnections", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_round_trip_time", remote_name="averageRoundTripTime", attribute_type=float, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def failed_attempts(self):
        """ Get failed_attempts value.

            Notes:
                The number of failed connection attempts

                
                This attribute is named `failedAttempts` in VSD API.
                
        """
        return self._failed_attempts

    @failed_attempts.setter
    def failed_attempts(self, value):
        """ Set failed_attempts value.

            Notes:
                The number of failed connection attempts

                
                This attribute is named `failedAttempts` in VSD API.
                
        """
        self._failed_attempts = value

    
    @property
    def failed_percent(self):
        """ Get failed_percent value.

            Notes:
                The percentage of failed connections

                
                This attribute is named `failedPercent` in VSD API.
                
        """
        return self._failed_percent

    @failed_percent.setter
    def failed_percent(self, value):
        """ Set failed_percent value.

            Notes:
                The percentage of failed connections

                
                This attribute is named `failedPercent` in VSD API.
                
        """
        self._failed_percent = value

    
    @property
    def maximum_round_trip_time(self):
        """ Get maximum_round_trip_time value.

            Notes:
                The maximum round trip time seen

                
                This attribute is named `maximumRoundTripTime` in VSD API.
                
        """
        return self._maximum_round_trip_time

    @maximum_round_trip_time.setter
    def maximum_round_trip_time(self, value):
        """ Set maximum_round_trip_time value.

            Notes:
                The maximum round trip time seen

                
                This attribute is named `maximumRoundTripTime` in VSD API.
                
        """
        self._maximum_round_trip_time = value

    
    @property
    def minimum_round_trip_time(self):
        """ Get minimum_round_trip_time value.

            Notes:
                The lowest round trip time seen

                
                This attribute is named `minimumRoundTripTime` in VSD API.
                
        """
        return self._minimum_round_trip_time

    @minimum_round_trip_time.setter
    def minimum_round_trip_time(self, value):
        """ Set minimum_round_trip_time value.

            Notes:
                The lowest round trip time seen

                
                This attribute is named `minimumRoundTripTime` in VSD API.
                
        """
        self._minimum_round_trip_time = value

    
    @property
    def connection_attempts(self):
        """ Get connection_attempts value.

            Notes:
                The number of connection attempts

                
                This attribute is named `connectionAttempts` in VSD API.
                
        """
        return self._connection_attempts

    @connection_attempts.setter
    def connection_attempts(self, value):
        """ Set connection_attempts value.

            Notes:
                The number of connection attempts

                
                This attribute is named `connectionAttempts` in VSD API.
                
        """
        self._connection_attempts = value

    
    @property
    def successful_connections(self):
        """ Get successful_connections value.

            Notes:
                Total number of successful connections

                
                This attribute is named `successfulConnections` in VSD API.
                
        """
        return self._successful_connections

    @successful_connections.setter
    def successful_connections(self, value):
        """ Set successful_connections value.

            Notes:
                Total number of successful connections

                
                This attribute is named `successfulConnections` in VSD API.
                
        """
        self._successful_connections = value

    
    @property
    def average_round_trip_time(self):
        """ Get average_round_trip_time value.

            Notes:
                Average Round Trip Time in milliseconds

                
                This attribute is named `averageRoundTripTime` in VSD API.
                
        """
        return self._average_round_trip_time

    @average_round_trip_time.setter
    def average_round_trip_time(self, value):
        """ Set average_round_trip_time value.

            Notes:
                Average Round Trip Time in milliseconds

                
                This attribute is named `averageRoundTripTime` in VSD API.
                
        """
        self._average_round_trip_time = value

    

    