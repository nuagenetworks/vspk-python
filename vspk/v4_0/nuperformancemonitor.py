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



from .fetchers import NUApplicationperformancemanagementsFetcher

from bambou import NURESTObject


class NUPerformanceMonitor(NURESTObject):
    """ Represents a PerformanceMonitor in the VSD

        Notes:
            None
    """

    __rest_name__ = "performancemonitor"
    __resource_name__ = "performancemonitors"

    
    ## Constants
    
    CONST_SERVICE_CLASS_H = "H"
    
    CONST_SERVICE_CLASS_A = "A"
    
    CONST_SERVICE_CLASS_B = "B"
    
    CONST_SERVICE_CLASS_C = "C"
    
    CONST_SERVICE_CLASS_D = "D"
    
    CONST_SERVICE_CLASS_E = "E"
    
    CONST_SERVICE_CLASS_F = "F"
    
    CONST_SERVICE_CLASS_G = "G"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PerformanceMonitor instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> performancemonitor = NUPerformanceMonitor(id=u'xxxx-xxx-xxx-xxx', name=u'PerformanceMonitor')
                >>> performancemonitor = NUPerformanceMonitor(data=my_dict)
        """

        super(NUPerformanceMonitor, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._payload_size = None
        self._read_only = None
        self._service_class = None
        self._description = None
        self._interval = None
        self._number_of_packets = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="payload_size", remote_name="payloadSize", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_class", remote_name="serviceClass", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H'])
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interval", remote_name="interval", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name="number_of_packets", remote_name="numberOfPackets", attribute_type=int, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.applicationperformancemanagements = NUApplicationperformancemanagementsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the application group probe

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the application group probe

                
        """
        self._name = value

    
    @property
    def payload_size(self):
        """ Get payload_size value.

            Notes:
                Payload size

                
                This attribute is named `payloadSize` in VSD API.
                
        """
        return self._payload_size

    @payload_size.setter
    def payload_size(self, value):
        """ Set payload_size value.

            Notes:
                Payload size

                
                This attribute is named `payloadSize` in VSD API.
                
        """
        self._payload_size = value

    
    @property
    def read_only(self):
        """ Get read_only value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """ Set read_only value.

            Notes:
                Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        self._read_only = value

    
    @property
    def service_class(self):
        """ Get service_class value.

            Notes:
                Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        return self._service_class

    @service_class.setter
    def service_class(self, value):
        """ Set service_class value.

            Notes:
                Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        self._service_class = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of application group probe

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of application group probe

                
        """
        self._description = value

    
    @property
    def interval(self):
        """ Get interval value.

            Notes:
                interval in seconds

                
        """
        return self._interval

    @interval.setter
    def interval(self, value):
        """ Set interval value.

            Notes:
                interval in seconds

                
        """
        self._interval = value

    
    @property
    def number_of_packets(self):
        """ Get number_of_packets value.

            Notes:
                number of packets

                
                This attribute is named `numberOfPackets` in VSD API.
                
        """
        return self._number_of_packets

    @number_of_packets.setter
    def number_of_packets(self, value):
        """ Set number_of_packets value.

            Notes:
                number of packets

                
                This attribute is named `numberOfPackets` in VSD API.
                
        """
        self._number_of_packets = value

    

    