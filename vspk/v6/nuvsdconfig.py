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


class NUVSDConfig(NURESTObject):
    """ Represents a VSDConfig in the VSD

        Notes:
            The VSD Configuration which can be dynamically managed using REST Api.
    """

    __rest_name__ = "vsdconfig"
    __resource_name__ = "vsdconfigs"

    

    def __init__(self, **kwargs):
        """ Initializes a VSDConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vsdconfig = NUVSDConfig(id=u'xxxx-xxx-xxx-xxx', name=u'VSDConfig')
                >>> vsdconfig = NUVSDConfig(data=my_dict)
        """

        super(NUVSDConfig, self).__init__()

        # Read/Write Attributes
        
        self._id = None
        self._attribute_value = None
        
        self.expose_attribute(local_name="id", remote_name="id", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="attribute_value", remote_name="attributeValue", attribute_type=str, is_required=True, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def id(self):
        """ Get id value.

            Notes:
                This Attribute defines the VSD config attribute name.

                
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Set id value.

            Notes:
                This Attribute defines the VSD config attribute name.

                
        """
        self._id = value

    
    @property
    def attribute_value(self):
        """ Get attribute_value value.

            Notes:
                This Attribute defines the VSD config attribute value

                
                This attribute is named `attributeValue` in VSD API.
                
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, value):
        """ Set attribute_value value.

            Notes:
                This Attribute defines the VSD config attribute value

                
                This attribute is named `attributeValue` in VSD API.
                
        """
        self._attribute_value = value

    

    