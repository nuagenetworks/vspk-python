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


class NUForwardingClass(NURESTObject):
    """ Represents a ForwardingClass in the VSD

        Notes:
            Contains the Forwarding Class and its usage for load balancing.
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    
    ## Constants
    
    CONST_FORWARDING_CLASS_E = "E"
    
    CONST_FORWARDING_CLASS_D = "D"
    
    CONST_FORWARDING_CLASS_G = "G"
    
    CONST_FORWARDING_CLASS_F = "F"
    
    CONST_FORWARDING_CLASS_A = "A"
    
    CONST_FORWARDING_CLASS_C = "C"
    
    CONST_FORWARDING_CLASS_B = "B"
    
    CONST_FORWARDING_CLASS_H = "H"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ForwardingClass instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> forwardingclass = NUForwardingClass(id=u'xxxx-xxx-xxx-xxx', name=u'ForwardingClass')
                >>> forwardingclass = NUForwardingClass(data=my_dict)
        """

        super(NUForwardingClass, self).__init__()

        # Read/Write Attributes
        
        self._load_balancing = None
        self._forwarding_class = None
        
        self.expose_attribute(local_name="load_balancing", remote_name="loadBalancing", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="forwarding_class", remote_name="forwardingClass", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def load_balancing(self):
        """ Get load_balancing value.

            Notes:
                Indicates whether the Service Class is used to used for load balancing in the forwarding path.

                
                This attribute is named `loadBalancing` in VSD API.
                
        """
        return self._load_balancing

    @load_balancing.setter
    def load_balancing(self, value):
        """ Set load_balancing value.

            Notes:
                Indicates whether the Service Class is used to used for load balancing in the forwarding path.

                
                This attribute is named `loadBalancing` in VSD API.
                
        """
        self._load_balancing = value

    
    @property
    def forwarding_class(self):
        """ Get forwarding_class value.

            Notes:
                Class of service to be used.Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `forwardingClass` in VSD API.
                
        """
        return self._forwarding_class

    @forwarding_class.setter
    def forwarding_class(self, value):
        """ Set forwarding_class value.

            Notes:
                Class of service to be used.Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `forwardingClass` in VSD API.
                
        """
        self._forwarding_class = value

    

    