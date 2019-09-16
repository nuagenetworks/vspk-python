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


from .fetchers import NUVRSsFetcher


from .fetchers import NUHSCsFetcher


from .fetchers import NUVSCsFetcher

from bambou import NURESTObject


class NUControllerVRSLink(NURESTObject):
    """ Represents a ControllerVRSLink in the VSD

        Notes:
            System Monitoring details for VRS connected to VSC or HSC
    """

    __rest_name__ = "controllervrslink"
    __resource_name__ = "controllervrslinks"

    
    ## Constants
    
    CONST_VSC_CONFIG_STATE_PRIMARY = "PRIMARY"
    
    CONST_STATUS_DOWN = "DOWN"
    
    CONST_VRS_PERSONALITY_NSGDUC = "NSGDUC"
    
    CONST_JSONRPC_CONNECTION_STATE_NONE = "NONE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_VRS_PERSONALITY_VRS = "VRS"
    
    CONST_CLUSTER_NODE_ROLE_NONE = "NONE"
    
    CONST_CLUSTER_NODE_ROLE_SECONDARY = "SECONDARY"
    
    CONST_ROLE_MASTER = "MASTER"
    
    CONST_STATUS_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_VRS_PERSONALITY_HARDWARE_VTEP = "HARDWARE_VTEP"
    
    CONST_ROLE_SLAVE = "SLAVE"
    
    CONST_VRS_PERSONALITY_NONE = "NONE"
    
    CONST_JSONRPC_CONNECTION_STATE_UP = "UP"
    
    CONST_JSONRPC_CONNECTION_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_VRS_PERSONALITY_NUAGE_210_WBX_48_S = "NUAGE_210_WBX_48_S"
    
    CONST_STATUS_UP = "UP"
    
    CONST_CLUSTER_NODE_ROLE_PRIMARY = "PRIMARY"
    
    CONST_VSC_CONFIG_STATE_SECONDARY = "SECONDARY"
    
    CONST_CONTROLLER_TYPE_VSC = "VSC"
    
    CONST_VRS_PERSONALITY_NSG = "NSG"
    
    CONST_JSONRPC_CONNECTION_STATE_DOWN = "DOWN"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_VRS_PERSONALITY_NSGBR = "NSGBR"
    
    CONST_VRS_PERSONALITY_NUAGE_210_WBX_32_Q = "NUAGE_210_WBX_32_Q"
    
    CONST_ROLE_NONE = "NONE"
    
    CONST_VSC_CURRENT_STATE_SECONDARY = "SECONDARY"
    
    CONST_VSC_CURRENT_STATE_PRIMARY = "PRIMARY"
    
    CONST_VRS_PERSONALITY_VRSG = "VRSG"
    
    CONST_VRS_PERSONALITY_VRSB = "VRSB"
    
    CONST_CONTROLLER_TYPE_HSC = "HSC"
    
    

    def __init__(self, **kwargs):
        """ Initializes a ControllerVRSLink instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> controllervrslink = NUControllerVRSLink(id=u'xxxx-xxx-xxx-xxx', name=u'ControllerVRSLink')
                >>> controllervrslink = NUControllerVRSLink(data=my_dict)
        """

        super(NUControllerVRSLink, self).__init__()

        # Read/Write Attributes
        
        self._vrsid = None
        self._vrs_personality = None
        self._vsc_config_state = None
        self._vsc_current_state = None
        self._jsonrpc_connection_state = None
        self._name = None
        self._last_updated_by = None
        self._peer = None
        self._cluster_node_role = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._role = None
        self._connections = None
        self._controller_id = None
        self._controller_type = None
        self._status = None
        self._external_id = None
        self._dynamic = None
        
        self.expose_attribute(local_name="vrsid", remote_name="VRSID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vrs_personality", remote_name="VRSPersonality", attribute_type=str, is_required=False, is_unique=False, choices=[u'HARDWARE_VTEP', u'NONE', u'NSG', u'NSGBR', u'NSGDUC', u'NUAGE_210_WBX_32_Q', u'NUAGE_210_WBX_48_S', u'VRS', u'VRSB', u'VRSG'])
        self.expose_attribute(local_name="vsc_config_state", remote_name="VSCConfigState", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'SECONDARY'])
        self.expose_attribute(local_name="vsc_current_state", remote_name="VSCCurrentState", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'SECONDARY'])
        self.expose_attribute(local_name="jsonrpc_connection_state", remote_name="JSONRPCConnectionState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'NONE', u'UP'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer", remote_name="peer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="cluster_node_role", remote_name="clusterNodeRole", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PRIMARY', u'SECONDARY'])
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=True, choices=[u'MASTER', u'NONE', u'SLAVE'])
        self.expose_attribute(local_name="connections", remote_name="connections", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_id", remote_name="controllerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_type", remote_name="controllerType", attribute_type=str, is_required=False, is_unique=False, choices=[u'HSC', u'VSC'])
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="dynamic", remote_name="dynamic", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.hscs = NUHSCsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vscs = NUVSCsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def vrsid(self):
        """ Get vrsid value.

            Notes:
                ID of associated VRS

                
                This attribute is named `VRSID` in VSD API.
                
        """
        return self._vrsid

    @vrsid.setter
    def vrsid(self, value):
        """ Set vrsid value.

            Notes:
                ID of associated VRS

                
                This attribute is named `VRSID` in VSD API.
                
        """
        self._vrsid = value

    
    @property
    def vrs_personality(self):
        """ Get vrs_personality value.

            Notes:
                Personality of associated VRS.

                
                This attribute is named `VRSPersonality` in VSD API.
                
        """
        return self._vrs_personality

    @vrs_personality.setter
    def vrs_personality(self, value):
        """ Set vrs_personality value.

            Notes:
                Personality of associated VRS.

                
                This attribute is named `VRSPersonality` in VSD API.
                
        """
        self._vrs_personality = value

    
    @property
    def vsc_config_state(self):
        """ Get vsc_config_state value.

            Notes:
                Indicates the configured state of the VSC.

                
                This attribute is named `VSCConfigState` in VSD API.
                
        """
        return self._vsc_config_state

    @vsc_config_state.setter
    def vsc_config_state(self, value):
        """ Set vsc_config_state value.

            Notes:
                Indicates the configured state of the VSC.

                
                This attribute is named `VSCConfigState` in VSD API.
                
        """
        self._vsc_config_state = value

    
    @property
    def vsc_current_state(self):
        """ Get vsc_current_state value.

            Notes:
                Indicates the current state of the VSC, which may or maybe not be same as the configured state.

                
                This attribute is named `VSCCurrentState` in VSD API.
                
        """
        return self._vsc_current_state

    @vsc_current_state.setter
    def vsc_current_state(self, value):
        """ Set vsc_current_state value.

            Notes:
                Indicates the current state of the VSC, which may or maybe not be same as the configured state.

                
                This attribute is named `VSCCurrentState` in VSD API.
                
        """
        self._vsc_current_state = value

    
    @property
    def jsonrpc_connection_state(self):
        """ Get jsonrpc_connection_state value.

            Notes:
                The current JSON RPC connection status.

                
                This attribute is named `JSONRPCConnectionState` in VSD API.
                
        """
        return self._jsonrpc_connection_state

    @jsonrpc_connection_state.setter
    def jsonrpc_connection_state(self, value):
        """ Set jsonrpc_connection_state value.

            Notes:
                The current JSON RPC connection status.

                
                This attribute is named `JSONRPCConnectionState` in VSD API.
                
        """
        self._jsonrpc_connection_state = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Controller-VRS link

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Controller-VRS link

                
        """
        self._name = value

    
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
    def peer(self):
        """ Get peer value.

            Notes:
                The redundant peer id for the current VRS.

                
        """
        return self._peer

    @peer.setter
    def peer(self, value):
        """ Set peer value.

            Notes:
                The redundant peer id for the current VRS.

                
        """
        self._peer = value

    
    @property
    def cluster_node_role(self):
        """ Get cluster_node_role value.

            Notes:
                Indicate that the controller associated is primary, secondary or unknown.

                
                This attribute is named `clusterNodeRole` in VSD API.
                
        """
        return self._cluster_node_role

    @cluster_node_role.setter
    def cluster_node_role(self, value):
        """ Set cluster_node_role value.

            Notes:
                Indicate that the controller associated is primary, secondary or unknown.

                
                This attribute is named `clusterNodeRole` in VSD API.
                
        """
        self._cluster_node_role = value

    
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
    def role(self):
        """ Get role value.

            Notes:
                Flag to indicate the VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                Flag to indicate the VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

                
        """
        self._role = value

    
    @property
    def connections(self):
        """ Get connections value.

            Notes:
                List of Connections for Controller VRS Link

                
        """
        return self._connections

    @connections.setter
    def connections(self, value):
        """ Set connections value.

            Notes:
                List of Connections for Controller VRS Link

                
        """
        self._connections = value

    
    @property
    def controller_id(self):
        """ Get controller_id value.

            Notes:
                ID of associated Controller

                
                This attribute is named `controllerID` in VSD API.
                
        """
        return self._controller_id

    @controller_id.setter
    def controller_id(self, value):
        """ Set controller_id value.

            Notes:
                ID of associated Controller

                
                This attribute is named `controllerID` in VSD API.
                
        """
        self._controller_id = value

    
    @property
    def controller_type(self):
        """ Get controller_type value.

            Notes:
                Type of associated Controller

                
                This attribute is named `controllerType` in VSD API.
                
        """
        return self._controller_type

    @controller_type.setter
    def controller_type(self, value):
        """ Set controller_type value.

            Notes:
                Type of associated Controller

                
                This attribute is named `controllerType` in VSD API.
                
        """
        self._controller_type = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Computed status of the entity.

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Computed status of the entity.

                
        """
        self._status = value

    
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

    
    @property
    def dynamic(self):
        """ Get dynamic value.

            Notes:
                Flag to indicate it is dynamically configured or not.

                
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, value):
        """ Set dynamic value.

            Notes:
                Flag to indicate it is dynamically configured or not.

                
        """
        self._dynamic = value

    

    