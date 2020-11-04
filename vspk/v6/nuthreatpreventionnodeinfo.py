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


class NUThreatPreventionNodeInfo(NURESTObject):
    """ Represents a ThreatPreventionNodeInfo in the VSD

        Notes:
            Represents the Individual Threat Prevention Node object in cluster deployment
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a ThreatPreventionNodeInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> threatpreventionnodeinfo = NUThreatPreventionNodeInfo(id=u'xxxx-xxx-xxx-xxx', name=u'ThreatPreventionNodeInfo')
                >>> threatpreventionnodeinfo = NUThreatPreventionNodeInfo(data=my_dict)
        """

        super(NUThreatPreventionNodeInfo, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._additional_info = None
        self._status = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="additional_info", remote_name="additionalInfo", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the node

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the node

                
        """
        self._name = value

    
    @property
    def additional_info(self):
        """ Get additional_info value.

            Notes:
                Additional Info about the redundancy status

                
                This attribute is named `additionalInfo` in VSD API.
                
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, value):
        """ Set additional_info value.

            Notes:
                Additional Info about the redundancy status

                
                This attribute is named `additionalInfo` in VSD API.
                
        """
        self._additional_info = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Redundancy status 

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Redundancy status 

                
        """
        self._status = value

    

    