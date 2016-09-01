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


class NUMonitorscope(NURESTObject):
    """ Represents a Monitorscope in the VSD

        Notes:
            This class tries to define the scope of probe (the NSGs between which the probe needs) to run.
    """

    __rest_name__ = "monitorscope"
    __resource_name__ = "monitorscopes"

    

    def __init__(self, **kwargs):
        """ Initializes a Monitorscope instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> monitorscope = NUMonitorscope(id=u'xxxx-xxx-xxx-xxx', name=u'Monitorscope')
                >>> monitorscope = NUMonitorscope(data=my_dict)
        """

        super(NUMonitorscope, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._read_only = None
        self._destination_nsgs = None
        self._source_nsgs = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="destination_nsgs", remote_name="destinationNSGs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="source_nsgs", remote_name="sourceNSGs", attribute_type=list, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name for the given scope

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name for the given scope

                
        """
        self._name = value

    
    @property
    def read_only(self):
        """ Get read_only value.

            Notes:
                Determines whether this entity is read only. Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """ Set read_only value.

            Notes:
                Determines whether this entity is read only. Read only objects cannot be modified or deleted.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        self._read_only = value

    
    @property
    def destination_nsgs(self):
        """ Get destination_nsgs value.

            Notes:
                List of destination NSGs to which the probe needs to run

                
                This attribute is named `destinationNSGs` in VSD API.
                
        """
        return self._destination_nsgs

    @destination_nsgs.setter
    def destination_nsgs(self, value):
        """ Set destination_nsgs value.

            Notes:
                List of destination NSGs to which the probe needs to run

                
                This attribute is named `destinationNSGs` in VSD API.
                
        """
        self._destination_nsgs = value

    
    @property
    def source_nsgs(self):
        """ Get source_nsgs value.

            Notes:
                List of source NSGs from which the probe needs to be started.

                
                This attribute is named `sourceNSGs` in VSD API.
                
        """
        return self._source_nsgs

    @source_nsgs.setter
    def source_nsgs(self, value):
        """ Set source_nsgs value.

            Notes:
                List of source NSGs from which the probe needs to be started.

                
                This attribute is named `sourceNSGs` in VSD API.
                
        """
        self._source_nsgs = value

    

    