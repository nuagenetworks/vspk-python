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


class NUApplicationBinding(NURESTObject):
    """ Represents a ApplicationBinding in the VSD

        Notes:
            None
    """

    __rest_name__ = "applicationbinding"
    __resource_name__ = "applicationbindings"

    

    def __init__(self, **kwargs):
        """ Initializes a ApplicationBinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> applicationbinding = NUApplicationBinding(id=u'xxxx-xxx-xxx-xxx', name=u'ApplicationBinding')
                >>> applicationbinding = NUApplicationBinding(data=my_dict)
        """

        super(NUApplicationBinding, self).__init__()

        # Read/Write Attributes
        
        self._read_only = None
        self._priority = None
        self._associated_application_id = None
        
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=True)
        self.expose_attribute(local_name="associated_application_id", remote_name="associatedApplicationID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def read_only(self):
        """ Get read_only value.

            Notes:
                Determines whether this entity is read only.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """ Set read_only value.

            Notes:
                Determines whether this entity is read only.

                
                This attribute is named `readOnly` in VSD API.
                
        """
        self._read_only = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                Priority of the Application within an Application Group

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Priority of the Application within an Application Group

                
        """
        self._priority = value

    
    @property
    def associated_application_id(self):
        """ Get associated_application_id value.

            Notes:
                Associated software application ID

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        return self._associated_application_id

    @associated_application_id.setter
    def associated_application_id(self, value):
        """ Set associated_application_id value.

            Notes:
                Associated software application ID

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        self._associated_application_id = value

    

    