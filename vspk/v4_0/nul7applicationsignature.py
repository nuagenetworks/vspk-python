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



from .fetchers import NUApplicationsFetcher

from bambou import NURESTObject


class NUL7applicationsignature(NURESTObject):
    """ Represents a L7applicationsignature in the VSD

        Notes:
            Layer 7 ApplicationType , these are auto created as part of VSD bringup
    """

    __rest_name__ = "l7applicationsignature"
    __resource_name__ = "l7applicationsignatures"

    

    def __init__(self, **kwargs):
        """ Initializes a L7applicationsignature instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> l7applicationsignature = NUL7applicationsignature(id=u'xxxx-xxx-xxx-xxx', name=u'L7applicationsignature')
                >>> l7applicationsignature = NUL7applicationsignature(data=my_dict)
        """

        super(NUL7applicationsignature, self).__init__()

        # Read/Write Attributes
        
        self._guid = None
        self._name = None
        self._category = None
        self._description = None
        self._dictionary_version = None
        
        self.expose_attribute(local_name="guid", remote_name="GUID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="category", remote_name="category", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dictionary_version", remote_name="dictionaryVersion", attribute_type=int, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.applications = NUApplicationsFetcher.fetcher_with_object(parent_object=self, relationship="member")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def guid(self):
        """ Get guid value.

            Notes:
                GUID of the Application

                
                This attribute is named `GUID` in VSD API.
                
        """
        return self._guid

    @guid.setter
    def guid(self, value):
        """ Set guid value.

            Notes:
                GUID of the Application

                
                This attribute is named `GUID` in VSD API.
                
        """
        self._guid = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                 name of the L7 App

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                 name of the L7 App

                
        """
        self._name = value

    
    @property
    def category(self):
        """ Get category value.

            Notes:
                Category of this application

                
        """
        return self._category

    @category.setter
    def category(self, value):
        """ Set category value.

            Notes:
                Category of this application

                
        """
        self._category = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                description for L7 App

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                description for L7 App

                
        """
        self._description = value

    
    @property
    def dictionary_version(self):
        """ Get dictionary_version value.

            Notes:
                Version of the L7 Application Type

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        return self._dictionary_version

    @dictionary_version.setter
    def dictionary_version(self, value):
        """ Set dictionary_version value.

            Notes:
                Version of the L7 Application Type

                
                This attribute is named `dictionaryVersion` in VSD API.
                
        """
        self._dictionary_version = value

    

    