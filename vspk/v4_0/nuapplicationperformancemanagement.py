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



from .fetchers import NUApplicationBindingsFetcher

from bambou import NURESTObject


class NUApplicationperformancemanagement(NURESTObject):
    """ Represents a Applicationperformancemanagement in the VSD

        Notes:
            Application Group is a container for group of applications 
    """

    __rest_name__ = "applicationperformancemanagement"
    __resource_name__ = "applicationperformancemanagements"

    
    ## Constants
    
    CONST_APPLICATION_GROUP_TYPE_MONITOR_PATH = "MONITOR_PATH"
    
    CONST_APPLICATION_GROUP_TYPE_DISCOVERY = "DISCOVERY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Applicationperformancemanagement instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> applicationperformancemanagement = NUApplicationperformancemanagement(id=u'xxxx-xxx-xxx-xxx', name=u'Applicationperformancemanagement')
                >>> applicationperformancemanagement = NUApplicationperformancemanagement(data=my_dict)
        """

        super(NUApplicationperformancemanagement, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._read_only = None
        self._description = None
        self._application_group_type = None
        self._associated_performance_monitor_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="read_only", remote_name="readOnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="application_group_type", remote_name="applicationGroupType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISCOVERY', u'MONITOR_PATH'])
        self.expose_attribute(local_name="associated_performance_monitor_id", remote_name="associatedPerformanceMonitorID", attribute_type=str, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.application_bindings = NUApplicationBindingsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                name of the application group

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                name of the application group

                
        """
        self._name = value

    
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
    def description(self):
        """ Get description value.

            Notes:
                Description of Application Group

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of Application Group

                
        """
        self._description = value

    
    @property
    def application_group_type(self):
        """ Get application_group_type value.

            Notes:
                with values  MONITOR_PATH,DISCOVERY

                
                This attribute is named `applicationGroupType` in VSD API.
                
        """
        return self._application_group_type

    @application_group_type.setter
    def application_group_type(self, value):
        """ Set application_group_type value.

            Notes:
                with values  MONITOR_PATH,DISCOVERY

                
                This attribute is named `applicationGroupType` in VSD API.
                
        """
        self._application_group_type = value

    
    @property
    def associated_performance_monitor_id(self):
        """ Get associated_performance_monitor_id value.

            Notes:
                associated Probe ID

                
                This attribute is named `associatedPerformanceMonitorID` in VSD API.
                
        """
        return self._associated_performance_monitor_id

    @associated_performance_monitor_id.setter
    def associated_performance_monitor_id(self, value):
        """ Set associated_performance_monitor_id value.

            Notes:
                associated Probe ID

                
                This attribute is named `associatedPerformanceMonitorID` in VSD API.
                
        """
        self._associated_performance_monitor_id = value

    

    