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


class NUSysmonUplinkConnection(NURESTObject):
    """ Represents a SysmonUplinkConnection in the VSD

        Notes:
            Models the connection between a VRS and the controller.
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    
    ## Constants
    
    CONST_JSON_STATE_NONE = "NONE"
    
    CONST_JSON_STATE_DOWN = "DOWN"
    
    CONST_IPSEC_DTLS_STATE_DOWN = "DOWN"
    
    CONST_VXLAN_DTLS_STATE_NONE = "NONE"
    
    CONST_IPSEC_DTLS_STATE_UP = "UP"
    
    CONST_IPSEC_DTLS_STATE_NONE = "NONE"
    
    CONST_OPENFLOW_STATE_DOWN = "DOWN"
    
    CONST_OPENFLOW_STATE_NONE = "NONE"
    
    CONST_IPSEC_DTLS_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_JSON_STATE_UP = "UP"
    
    CONST_VXLAN_DTLS_STATE_UP = "UP"
    
    CONST_OPENFLOW_STATE_UP = "UP"
    
    CONST_OPENFLOW_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_VXLAN_DTLS_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_JSON_STATE_ADMIN_DOWN = "ADMIN_DOWN"
    
    CONST_VXLAN_DTLS_STATE_DOWN = "DOWN"
    
    

    def __init__(self, **kwargs):
        """ Initializes a SysmonUplinkConnection instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> sysmonuplinkconnection = NUSysmonUplinkConnection(id=u'xxxx-xxx-xxx-xxx', name=u'SysmonUplinkConnection')
                >>> sysmonuplinkconnection = NUSysmonUplinkConnection(data=my_dict)
        """

        super(NUSysmonUplinkConnection, self).__init__()

        # Read/Write Attributes
        
        self._datapath_uplink_id = None
        self._openflow_state = None
        self._ipsec_dtls_state = None
        self._private_ip = None
        self._json_state = None
        self._public_ip = None
        self._vxlan_dtls_state = None
        
        self.expose_attribute(local_name="datapath_uplink_id", remote_name="datapathUplinkId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="openflow_state", remote_name="openflowState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'NONE', u'UP'])
        self.expose_attribute(local_name="ipsec_dtls_state", remote_name="ipsecDtlsState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'NONE', u'UP'])
        self.expose_attribute(local_name="private_ip", remote_name="privateIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="json_state", remote_name="jsonState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'NONE', u'UP'])
        self.expose_attribute(local_name="public_ip", remote_name="publicIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vxlan_dtls_state", remote_name="vxlanDtlsState", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'NONE', u'UP'])
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def datapath_uplink_id(self):
        """ Get datapath_uplink_id value.

            Notes:
                Datapath Uplink ID

                
                This attribute is named `datapathUplinkId` in VSD API.
                
        """
        return self._datapath_uplink_id

    @datapath_uplink_id.setter
    def datapath_uplink_id(self, value):
        """ Set datapath_uplink_id value.

            Notes:
                Datapath Uplink ID

                
                This attribute is named `datapathUplinkId` in VSD API.
                
        """
        self._datapath_uplink_id = value

    
    @property
    def openflow_state(self):
        """ Get openflow_state value.

            Notes:
                Openflow Connection Status

                
                This attribute is named `openflowState` in VSD API.
                
        """
        return self._openflow_state

    @openflow_state.setter
    def openflow_state(self, value):
        """ Set openflow_state value.

            Notes:
                Openflow Connection Status

                
                This attribute is named `openflowState` in VSD API.
                
        """
        self._openflow_state = value

    
    @property
    def ipsec_dtls_state(self):
        """ Get ipsec_dtls_state value.

            Notes:
                IPSec DTLS Connection State

                
                This attribute is named `ipsecDtlsState` in VSD API.
                
        """
        return self._ipsec_dtls_state

    @ipsec_dtls_state.setter
    def ipsec_dtls_state(self, value):
        """ Set ipsec_dtls_state value.

            Notes:
                IPSec DTLS Connection State

                
                This attribute is named `ipsecDtlsState` in VSD API.
                
        """
        self._ipsec_dtls_state = value

    
    @property
    def private_ip(self):
        """ Get private_ip value.

            Notes:
                Private IP of connection

                
                This attribute is named `privateIP` in VSD API.
                
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, value):
        """ Set private_ip value.

            Notes:
                Private IP of connection

                
                This attribute is named `privateIP` in VSD API.
                
        """
        self._private_ip = value

    
    @property
    def json_state(self):
        """ Get json_state value.

            Notes:
                JSON Connection Status

                
                This attribute is named `jsonState` in VSD API.
                
        """
        return self._json_state

    @json_state.setter
    def json_state(self, value):
        """ Set json_state value.

            Notes:
                JSON Connection Status

                
                This attribute is named `jsonState` in VSD API.
                
        """
        self._json_state = value

    
    @property
    def public_ip(self):
        """ Get public_ip value.

            Notes:
                Public IP of connection

                
                This attribute is named `publicIP` in VSD API.
                
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, value):
        """ Set public_ip value.

            Notes:
                Public IP of connection

                
                This attribute is named `publicIP` in VSD API.
                
        """
        self._public_ip = value

    
    @property
    def vxlan_dtls_state(self):
        """ Get vxlan_dtls_state value.

            Notes:
                VXLAN DTLS Connection State

                
                This attribute is named `vxlanDtlsState` in VSD API.
                
        """
        return self._vxlan_dtls_state

    @vxlan_dtls_state.setter
    def vxlan_dtls_state(self, value):
        """ Set vxlan_dtls_state value.

            Notes:
                VXLAN DTLS Connection State

                
                This attribute is named `vxlanDtlsState` in VSD API.
                
        """
        self._vxlan_dtls_state = value

    

    