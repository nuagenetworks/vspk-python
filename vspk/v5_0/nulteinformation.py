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


class NULTEInformation(NURESTObject):
    """ Represents a LTEInformation in the VSD

        Notes:
            Contains information about the LTE dongle plugged in USB port on NSG. This would have information like - Modem Manufacturer, Model Number, Subscriber Number, Operator etc. This information could vary from vendor to vendor.
    """

    __rest_name__ = "lteinformation"
    __resource_name__ = "lteinformations"

    

    def __init__(self, **kwargs):
        """ Initializes a LTEInformation instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> lteinformation = NULTEInformation(id=u'xxxx-xxx-xxx-xxx', name=u'LTEInformation')
                >>> lteinformation = NULTEInformation(data=my_dict)
        """

        super(NULTEInformation, self).__init__()

        # Read/Write Attributes
        
        self._lte_connection_info = None
        
        self.expose_attribute(local_name="lte_connection_info", remote_name="LTEConnectionInfo", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def lte_connection_info(self):
        """ Get lte_connection_info value.

            Notes:
                This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.

                
                This attribute is named `LTEConnectionInfo` in VSD API.
                
        """
        return self._lte_connection_info

    @lte_connection_info.setter
    def lte_connection_info(self, value):
        """ Set lte_connection_info value.

            Notes:
                This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.

                
                This attribute is named `LTEConnectionInfo` in VSD API.
                
        """
        self._lte_connection_info = value

    

    