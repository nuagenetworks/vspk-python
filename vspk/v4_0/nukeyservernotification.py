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



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUKeyServerNotification(NURESTObject):
    """ Represents a KeyServerNotification in the VSD

        Notes:
            KeyServer Notification - Create one of these transient objects to push an event to the KeyServer
    """

    __rest_name__ = "keyservernotification"
    __resource_name__ = "keyservernotifications"

    
    ## Constants
    
    CONST_NOTIFICATION_TYPE_ENCRYPTION_DISABLED = "ENCRYPTION_DISABLED"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_NOTIFICATION_TYPE_ENCRYPTION_ENABLED = "ENCRYPTION_ENABLED"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_NOTIFICATION_TYPE_CONFIG_UPDATE = "CONFIG_UPDATE"
    
    CONST_NOTIFICATION_TYPE_TEST = "TEST"
    
    CONST_NOTIFICATION_TYPE_REKEY = "REKEY"
    
    

    def __init__(self, **kwargs):
        """ Initializes a KeyServerNotification instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservernotification = NUKeyServerNotification(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerNotification')
                >>> keyservernotification = NUKeyServerNotification(data=my_dict)
        """

        super(NUKeyServerNotification, self).__init__()

        # Read/Write Attributes
        
        self._base64_json_string = None
        self._message = None
        self._entity_scope = None
        self._notification_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="base64_json_string", remote_name="base64JSONString", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="message", remote_name="message", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="notification_type", remote_name="notificationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONFIG_UPDATE', u'ENCRYPTION_DISABLED', u'ENCRYPTION_ENABLED', u'REKEY', u'TEST'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def base64_json_string(self):
        """ Get base64_json_string value.

            Notes:
                The base 64 encoded JSON String of the message object

                
                This attribute is named `base64JSONString` in VSD API.
                
        """
        return self._base64_json_string

    @base64_json_string.setter
    def base64_json_string(self, value):
        """ Set base64_json_string value.

            Notes:
                The base 64 encoded JSON String of the message object

                
                This attribute is named `base64JSONString` in VSD API.
                
        """
        self._base64_json_string = value

    
    @property
    def message(self):
        """ Get message value.

            Notes:
                The message to send

                
        """
        return self._message

    @message.setter
    def message(self, value):
        """ Set message value.

            Notes:
                The message to send

                
        """
        self._message = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def notification_type(self):
        """ Get notification_type value.

            Notes:
                The notification type to trigger

                
                This attribute is named `notificationType` in VSD API.
                
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, value):
        """ Set notification_type value.

            Notes:
                The notification type to trigger

                
                This attribute is named `notificationType` in VSD API.
                
        """
        self._notification_type = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    