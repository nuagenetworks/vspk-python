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


class NUMTUDiscoveryTestResult(NURESTObject):
    """ Represents a MTUDiscoveryTestResult in the VSD

        Notes:
            MTU Discovery Test Result
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a MTUDiscoveryTestResult instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> mtudiscoverytestresult = NUMTUDiscoveryTestResult(id=u'xxxx-xxx-xxx-xxx', name=u'MTUDiscoveryTestResult')
                >>> mtudiscoverytestresult = NUMTUDiscoveryTestResult(data=my_dict)
        """

        super(NUMTUDiscoveryTestResult, self).__init__()

        # Read/Write Attributes
        
        self._discovered_mtu = None
        
        self.expose_attribute(local_name="discovered_mtu", remote_name="discoveredMTU", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def discovered_mtu(self):
        """ Get discovered_mtu value.

            Notes:
                The discovered MTU

                
                This attribute is named `discoveredMTU` in VSD API.
                
        """
        return self._discovered_mtu

    @discovered_mtu.setter
    def discovered_mtu(self, value):
        """ Set discovered_mtu value.

            Notes:
                The discovered MTU

                
                This attribute is named `discoveredMTU` in VSD API.
                
        """
        self._discovered_mtu = value

    

    