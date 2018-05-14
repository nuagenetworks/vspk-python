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


class NUDUCGroupBinding(NURESTObject):
    """ Represents a DUCGroupBinding in the VSD

        Notes:
            None
    """

    __rest_name__ = "ducgroupbinding"
    __resource_name__ = "ducgroupbindings"

    

    def __init__(self, **kwargs):
        """ Initializes a DUCGroupBinding instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ducgroupbinding = NUDUCGroupBinding(id=u'xxxx-xxx-xxx-xxx', name=u'DUCGroupBinding')
                >>> ducgroupbinding = NUDUCGroupBinding(data=my_dict)
        """

        super(NUDUCGroupBinding, self).__init__()

        # Read/Write Attributes
        
        self._one_way_delay = None
        self._priority = None
        self._associated_duc_group_id = None
        
        self.expose_attribute(local_name="one_way_delay", remote_name="oneWayDelay", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_duc_group_id", remote_name="associatedDUCGroupID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def one_way_delay(self):
        """ Get one_way_delay value.

            Notes:
                SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

                
                This attribute is named `oneWayDelay` in VSD API.
                
        """
        return self._one_way_delay

    @one_way_delay.setter
    def one_way_delay(self, value):
        """ Set one_way_delay value.

            Notes:
                SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

                
                This attribute is named `oneWayDelay` in VSD API.
                
        """
        self._one_way_delay = value

    
    @property
    def priority(self):
        """ Get priority value.

            Notes:
                The priority for NSG Group to UBR Group relationship.

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                The priority for NSG Group to UBR Group relationship.

                
        """
        self._priority = value

    
    @property
    def associated_duc_group_id(self):
        """ Get associated_duc_group_id value.

            Notes:
                Identification of the UBR Group associated to this group binding instance.

                
                This attribute is named `associatedDUCGroupID` in VSD API.
                
        """
        return self._associated_duc_group_id

    @associated_duc_group_id.setter
    def associated_duc_group_id(self, value):
        """ Set associated_duc_group_id value.

            Notes:
                Identification of the UBR Group associated to this group binding instance.

                
                This attribute is named `associatedDUCGroupID` in VSD API.
                
        """
        self._associated_duc_group_id = value

    

    