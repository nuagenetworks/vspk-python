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




from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUOSPFInterface(NURESTObject):
    """ Represents a OSPFInterface in the VSD

        Notes:
            The OSPF interface represents the connection of a router to the OSPF network. The OSPF interface defines the protocol metrics and security parameters for OSPF traffic on a V-Port on the specified subnet. An OSPF interface can exist in only one OSPF area.
    """

    __rest_name__ = "ospfinterface"
    __resource_name__ = "ospfinterfaces"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_INTERFACE_TYPE_POINT_TO_POINT = "POINT_TO_POINT"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ADMIN_STATE_DOWN = "DOWN"
    
    CONST_AUTHENTICATION_TYPE_MESSAGE_DIGEST = "MESSAGE_DIGEST"
    
    CONST_ADMIN_STATE_UP = "UP"
    
    CONST_INTERFACE_TYPE_BROADCAST = "BROADCAST"
    
    CONST_AUTHENTICATION_TYPE_PASSWORD = "PASSWORD"
    
    CONST_AUTHENTICATION_TYPE_NONE = "NONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a OSPFInterface instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ospfinterface = NUOSPFInterface(id=u'xxxx-xxx-xxx-xxx', name=u'OSPFInterface')
                >>> ospfinterface = NUOSPFInterface(data=my_dict)
        """

        super(NUOSPFInterface, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._passive_enabled = None
        self._last_updated_by = None
        self._admin_state = None
        self._dead_interval = None
        self._hello_interval = None
        self._description = None
        self._message_digest_keys = None
        self._metric = None
        self._embedded_metadata = None
        self._interface_type = None
        self._entity_scope = None
        self._priority = None
        self._associated_subnet_id = None
        self._mtu = None
        self._authentication_key = None
        self._authentication_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="passive_enabled", remote_name="passiveEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="admin_state", remote_name="adminState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOWN', u'UP'])
        self.expose_attribute(local_name="dead_interval", remote_name="deadInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="hello_interval", remote_name="helloInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="message_digest_keys", remote_name="messageDigestKeys", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metric", remote_name="metric", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="interface_type", remote_name="interfaceType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BROADCAST', u'POINT_TO_POINT'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="priority", remote_name="priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_subnet_id", remote_name="associatedSubnetID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="mtu", remote_name="mtu", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="authentication_key", remote_name="authenticationKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="authentication_type", remote_name="authenticationType", attribute_type=str, is_required=False, is_unique=False, choices=[u'MESSAGE_DIGEST', u'NONE', u'PASSWORD'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the OSPF Interface. The name has to be unique within the OSPFArea.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the OSPF Interface. The name has to be unique within the OSPFArea.

                
        """
        self._name = value

    
    @property
    def passive_enabled(self):
        """ Get passive_enabled value.

            Notes:
                Enable the passive property of the interface.

                
                This attribute is named `passiveEnabled` in VSD API.
                
        """
        return self._passive_enabled

    @passive_enabled.setter
    def passive_enabled(self, value):
        """ Set passive_enabled value.

            Notes:
                Enable the passive property of the interface.

                
                This attribute is named `passiveEnabled` in VSD API.
                
        """
        self._passive_enabled = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def admin_state(self):
        """ Get admin_state value.

            Notes:
                Admin state of this OSPF interface

                
                This attribute is named `adminState` in VSD API.
                
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, value):
        """ Set admin_state value.

            Notes:
                Admin state of this OSPF interface

                
                This attribute is named `adminState` in VSD API.
                
        """
        self._admin_state = value

    
    @property
    def dead_interval(self):
        """ Get dead_interval value.

            Notes:
                Time OSPF waits without receiving hello packets before declaring a neighbor down. If specified, it must be at least twice as long as 'helloInterval'.

                
                This attribute is named `deadInterval` in VSD API.
                
        """
        return self._dead_interval

    @dead_interval.setter
    def dead_interval(self, value):
        """ Set dead_interval value.

            Notes:
                Time OSPF waits without receiving hello packets before declaring a neighbor down. If specified, it must be at least twice as long as 'helloInterval'.

                
                This attribute is named `deadInterval` in VSD API.
                
        """
        self._dead_interval = value

    
    @property
    def hello_interval(self):
        """ Get hello_interval value.

            Notes:
                Time interval between OSPF hellos issued on the interface.

                
                This attribute is named `helloInterval` in VSD API.
                
        """
        return self._hello_interval

    @hello_interval.setter
    def hello_interval(self, value):
        """ Set hello_interval value.

            Notes:
                Time interval between OSPF hellos issued on the interface.

                
                This attribute is named `helloInterval` in VSD API.
                
        """
        self._hello_interval = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of this OSPF Interface.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of this OSPF Interface.

                
        """
        self._description = value

    
    @property
    def message_digest_keys(self):
        """ Get message_digest_keys value.

            Notes:
                This attribute applies only when 'authenticationType' is 'MESSAGE_DIGEST'. In that case, this attribute is a list of pairs of key ID/password used for MD5 authentication. The key ID must by an integer between 1 and 255, and the value is a password (of 16 charachters maximum) used to generate an MD5 hash. The MD5 has is then used as authentication data in the OSPF packets. No duplicate key IDs are allowed. The format for each pair is 'keyID:password' (e.g. '1:foobar')

                
                This attribute is named `messageDigestKeys` in VSD API.
                
        """
        return self._message_digest_keys

    @message_digest_keys.setter
    def message_digest_keys(self, value):
        """ Set message_digest_keys value.

            Notes:
                This attribute applies only when 'authenticationType' is 'MESSAGE_DIGEST'. In that case, this attribute is a list of pairs of key ID/password used for MD5 authentication. The key ID must by an integer between 1 and 255, and the value is a password (of 16 charachters maximum) used to generate an MD5 hash. The MD5 has is then used as authentication data in the OSPF packets. No duplicate key IDs are allowed. The format for each pair is 'keyID:password' (e.g. '1:foobar')

                
                This attribute is named `messageDigestKeys` in VSD API.
                
        """
        self._message_digest_keys = value

    
    @property
    def metric(self):
        """ Get metric value.

            Notes:
                Configure an explicit route cost metric for the interface.

                
        """
        return self._metric

    @metric.setter
    def metric(self, value):
        """ Set metric value.

            Notes:
                Configure an explicit route cost metric for the interface.

                
        """
        self._metric = value

    
    @property
    def embedded_metadata(self):
        """ Get embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        return self._embedded_metadata

    @embedded_metadata.setter
    def embedded_metadata(self, value):
        """ Set embedded_metadata value.

            Notes:
                Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

                
                This attribute is named `embeddedMetadata` in VSD API.
                
        """
        self._embedded_metadata = value

    
    @property
    def interface_type(self):
        """ Get interface_type value.

            Notes:
                Can be BROADCAST or POINT_TO_POINT

                
                This attribute is named `interfaceType` in VSD API.
                
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, value):
        """ Set interface_type value.

            Notes:
                Can be BROADCAST or POINT_TO_POINT

                
                This attribute is named `interfaceType` in VSD API.
                
        """
        self._interface_type = value

    
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
    def priority(self):
        """ Get priority value.

            Notes:
                Determines which routers are selected as the designated router and backup designated router of the area.

                
        """
        return self._priority

    @priority.setter
    def priority(self, value):
        """ Set priority value.

            Notes:
                Determines which routers are selected as the designated router and backup designated router of the area.

                
        """
        self._priority = value

    
    @property
    def associated_subnet_id(self):
        """ Get associated_subnet_id value.

            Notes:
                ID of the Subnet which is associated to the current OSPFInterface. Once the OSPF interface is created, the associated subnet ID cannot be updated. The interface must be deleted and re-created with a different subnet ID.

                
                This attribute is named `associatedSubnetID` in VSD API.
                
        """
        return self._associated_subnet_id

    @associated_subnet_id.setter
    def associated_subnet_id(self, value):
        """ Set associated_subnet_id value.

            Notes:
                ID of the Subnet which is associated to the current OSPFInterface. Once the OSPF interface is created, the associated subnet ID cannot be updated. The interface must be deleted and re-created with a different subnet ID.

                
                This attribute is named `associatedSubnetID` in VSD API.
                
        """
        self._associated_subnet_id = value

    
    @property
    def mtu(self):
        """ Get mtu value.

            Notes:
                MTU to be used by OSPF for this logical interface

                
        """
        return self._mtu

    @mtu.setter
    def mtu(self, value):
        """ Set mtu value.

            Notes:
                MTU to be used by OSPF for this logical interface

                
        """
        self._mtu = value

    
    @property
    def authentication_key(self):
        """ Get authentication_key value.

            Notes:
                The authentication key that is used on the interface.

                
                This attribute is named `authenticationKey` in VSD API.
                
        """
        return self._authentication_key

    @authentication_key.setter
    def authentication_key(self, value):
        """ Set authentication_key value.

            Notes:
                The authentication key that is used on the interface.

                
                This attribute is named `authenticationKey` in VSD API.
                
        """
        self._authentication_key = value

    
    @property
    def authentication_type(self):
        """ Get authentication_type value.

            Notes:
                Authentication Type used for this OSPFInterface

                
                This attribute is named `authenticationType` in VSD API.
                
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        """ Set authentication_type value.

            Notes:
                Authentication Type used for this OSPFInterface

                
                This attribute is named `authenticationType` in VSD API.
                
        """
        self._authentication_type = value

    
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

    

    