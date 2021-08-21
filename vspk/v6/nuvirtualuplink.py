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




from .fetchers import NUIKEGatewayConnectionsFetcher

from bambou import NURESTObject


class NUVirtualUplink(NURESTObject):
    """ Represents a VirtualUplink in the VSD

        Notes:
            Virtual Uplinks are entities that represent on an NSG the properties that are set for corresponding control uplink instances that are residing on the NSG RG Peer when tied together by a Shunt Link.
    """

    __rest_name__ = "virtualuplink"
    __resource_name__ = "virtualuplinks"

    
    ## Constants
    
    CONST_FEC_ENABLED_PASSIVE = "PASSIVE"
    
    CONST_ROLE_UNKNOWN = "UNKNOWN"
    
    CONST_ROLE_NONE = "NONE"
    
    CONST_ROLE_SECONDARY = "SECONDARY"
    
    CONST_AUX_MODE_COLD = "COLD"
    
    CONST_FEC_ENABLED_ACTIVE = "ACTIVE"
    
    CONST_AUX_MODE_NONE = "NONE"
    
    CONST_ROLE_TERTIARY = "TERTIARY"
    
    CONST_FEC_ENABLED_DISABLED = "DISABLED"
    
    CONST_ROLE_PRIMARY = "PRIMARY"
    
    CONST_AUX_MODE_HOT = "HOT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VirtualUplink instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> virtualuplink = NUVirtualUplink(id=u'xxxx-xxx-xxx-xxx', name=u'VirtualUplink')
                >>> virtualuplink = NUVirtualUplink(data=my_dict)
        """

        super(NUVirtualUplink, self).__init__()

        # Read/Write Attributes
        
        self._fec_enabled = None
        self._peer_endpoint = None
        self._peer_gateway_id = None
        self._peer_gateway_name = None
        self._peer_gateway_system_id = None
        self._peer_port_id = None
        self._peer_uplink_id = None
        self._peer_vlanid = None
        self._shunt_endpoint = None
        self._shunt_port_id = None
        self._shunt_vlanid = None
        self._virtual_uplink_datapath_id = None
        self._enable_nat_probes = None
        self._underlay_id = None
        self._underlay_nat = None
        self._underlay_name = None
        self._underlay_routing = None
        self._role = None
        self._role_order = None
        self._traffic_through_ubr_only = None
        self._associated_egress_qo_s_policy_id = None
        self._associated_ingress_overlay_qo_s_policer_id = None
        self._associated_ingress_qo_s_policy_id = None
        self._associated_ingress_underlay_qo_s_policer_id = None
        self._associated_uplink_connection_id = None
        self._associated_vsc_profile_id = None
        self._aux_mode = None
        
        self.expose_attribute(local_name="fec_enabled", remote_name="fecEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'DISABLED', u'PASSIVE'])
        self.expose_attribute(local_name="peer_endpoint", remote_name="peerEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_gateway_id", remote_name="peerGatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_gateway_name", remote_name="peerGatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_gateway_system_id", remote_name="peerGatewaySystemID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_port_id", remote_name="peerPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_uplink_id", remote_name="peerUplinkID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="peer_vlanid", remote_name="peerVLANID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="shunt_endpoint", remote_name="shuntEndpoint", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="shunt_port_id", remote_name="shuntPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="shunt_vlanid", remote_name="shuntVLANID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual_uplink_datapath_id", remote_name="virtualUplinkDatapathID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enable_nat_probes", remote_name="enableNATProbes", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_id", remote_name="underlayID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_nat", remote_name="underlayNAT", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_name", remote_name="underlayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_routing", remote_name="underlayRouting", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="role", remote_name="role", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'PRIMARY', u'SECONDARY', u'TERTIARY', u'UNKNOWN'])
        self.expose_attribute(local_name="role_order", remote_name="roleOrder", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="traffic_through_ubr_only", remote_name="trafficThroughUBROnly", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_egress_qo_s_policy_id", remote_name="associatedEgressQoSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_overlay_qo_s_policer_id", remote_name="associatedIngressOverlayQoSPolicerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_qo_s_policy_id", remote_name="associatedIngressQoSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_ingress_underlay_qo_s_policer_id", remote_name="associatedIngressUnderlayQoSPolicerID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_uplink_connection_id", remote_name="associatedUplinkConnectionID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_vsc_profile_id", remote_name="associatedVSCProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aux_mode", remote_name="auxMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'COLD', u'HOT', u'NONE'])
        

        # Fetchers
        
        
        self.ike_gateway_connections = NUIKEGatewayConnectionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def fec_enabled(self):
        """ Get fec_enabled value.

            Notes:
                Indicates the FEC (Forward Error Correction) setting on this Virtual Uplink. Possible values are Active(Encode & Decode on all paths over this uplink), Passive(Encode & Decode only to uplinks with FEC Active) and Disabled(do not Encode or Decode, do not detect or report loss).

                
                This attribute is named `fecEnabled` in VSD API.
                
        """
        return self._fec_enabled

    @fec_enabled.setter
    def fec_enabled(self, value):
        """ Set fec_enabled value.

            Notes:
                Indicates the FEC (Forward Error Correction) setting on this Virtual Uplink. Possible values are Active(Encode & Decode on all paths over this uplink), Passive(Encode & Decode only to uplinks with FEC Active) and Disabled(do not Encode or Decode, do not detect or report loss).

                
                This attribute is named `fecEnabled` in VSD API.
                
        """
        self._fec_enabled = value

    
    @property
    def peer_endpoint(self):
        """ Get peer_endpoint value.

            Notes:
                The physical port and VLAN endpoint hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link in a redundant gateway group.

                
                This attribute is named `peerEndpoint` in VSD API.
                
        """
        return self._peer_endpoint

    @peer_endpoint.setter
    def peer_endpoint(self, value):
        """ Set peer_endpoint value.

            Notes:
                The physical port and VLAN endpoint hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link in a redundant gateway group.

                
                This attribute is named `peerEndpoint` in VSD API.
                
        """
        self._peer_endpoint = value

    
    @property
    def peer_gateway_id(self):
        """ Get peer_gateway_id value.

            Notes:
                The UUID of the peer NSG in the redundant gateway group part of the Shunt Link.

                
                This attribute is named `peerGatewayID` in VSD API.
                
        """
        return self._peer_gateway_id

    @peer_gateway_id.setter
    def peer_gateway_id(self, value):
        """ Set peer_gateway_id value.

            Notes:
                The UUID of the peer NSG in the redundant gateway group part of the Shunt Link.

                
                This attribute is named `peerGatewayID` in VSD API.
                
        """
        self._peer_gateway_id = value

    
    @property
    def peer_gateway_name(self):
        """ Get peer_gateway_name value.

            Notes:
                The name of the peer NSG in the redundant gateway group part of the Shunt Link.

                
                This attribute is named `peerGatewayName` in VSD API.
                
        """
        return self._peer_gateway_name

    @peer_gateway_name.setter
    def peer_gateway_name(self, value):
        """ Set peer_gateway_name value.

            Notes:
                The name of the peer NSG in the redundant gateway group part of the Shunt Link.

                
                This attribute is named `peerGatewayName` in VSD API.
                
        """
        self._peer_gateway_name = value

    
    @property
    def peer_gateway_system_id(self):
        """ Get peer_gateway_system_id value.

            Notes:
                IP format of system generated identifier of the peer NSG.

                
                This attribute is named `peerGatewaySystemID` in VSD API.
                
        """
        return self._peer_gateway_system_id

    @peer_gateway_system_id.setter
    def peer_gateway_system_id(self, value):
        """ Set peer_gateway_system_id value.

            Notes:
                IP format of system generated identifier of the peer NSG.

                
                This attribute is named `peerGatewaySystemID` in VSD API.
                
        """
        self._peer_gateway_system_id = value

    
    @property
    def peer_port_id(self):
        """ Get peer_port_id value.

            Notes:
                The UUID of the port hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

                
                This attribute is named `peerPortID` in VSD API.
                
        """
        return self._peer_port_id

    @peer_port_id.setter
    def peer_port_id(self, value):
        """ Set peer_port_id value.

            Notes:
                The UUID of the port hosting the peer control uplink that this virtual uplink mirrors. This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

                
                This attribute is named `peerPortID` in VSD API.
                
        """
        self._peer_port_id = value

    
    @property
    def peer_uplink_id(self):
        """ Get peer_uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink. This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

                
                This attribute is named `peerUplinkID` in VSD API.
                
        """
        return self._peer_uplink_id

    @peer_uplink_id.setter
    def peer_uplink_id(self, value):
        """ Set peer_uplink_id value.

            Notes:
                ID that unqiuely identifies the uplink. This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

                
                This attribute is named `peerUplinkID` in VSD API.
                
        """
        self._peer_uplink_id = value

    
    @property
    def peer_vlanid(self):
        """ Get peer_vlanid value.

            Notes:
                The UUID of the VLAN in the control uplink that this virtual uplink mirrors.This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

                
                This attribute is named `peerVLANID` in VSD API.
                
        """
        return self._peer_vlanid

    @peer_vlanid.setter
    def peer_vlanid(self, value):
        """ Set peer_vlanid value.

            Notes:
                The UUID of the VLAN in the control uplink that this virtual uplink mirrors.This is derived from the peer NSG of the Shunt Link on a redundant gateway group.

                
                This attribute is named `peerVLANID` in VSD API.
                
        """
        self._peer_vlanid = value

    
    @property
    def shunt_endpoint(self):
        """ Get shunt_endpoint value.

            Notes:
                The physical port and VLAN endpoint hosting the shunt endpoint on this Gateway.

                
                This attribute is named `shuntEndpoint` in VSD API.
                
        """
        return self._shunt_endpoint

    @shunt_endpoint.setter
    def shunt_endpoint(self, value):
        """ Set shunt_endpoint value.

            Notes:
                The physical port and VLAN endpoint hosting the shunt endpoint on this Gateway.

                
                This attribute is named `shuntEndpoint` in VSD API.
                
        """
        self._shunt_endpoint = value

    
    @property
    def shunt_port_id(self):
        """ Get shunt_port_id value.

            Notes:
                The UUID of the shunt port on the NSG hosting the Virtual Uplink.

                
                This attribute is named `shuntPortID` in VSD API.
                
        """
        return self._shunt_port_id

    @shunt_port_id.setter
    def shunt_port_id(self, value):
        """ Set shunt_port_id value.

            Notes:
                The UUID of the shunt port on the NSG hosting the Virtual Uplink.

                
                This attribute is named `shuntPortID` in VSD API.
                
        """
        self._shunt_port_id = value

    
    @property
    def shunt_vlanid(self):
        """ Get shunt_vlanid value.

            Notes:
                The UUID of the shunt VLAN on the NSG hosting the Virtual Uplink.

                
                This attribute is named `shuntVLANID` in VSD API.
                
        """
        return self._shunt_vlanid

    @shunt_vlanid.setter
    def shunt_vlanid(self, value):
        """ Set shunt_vlanid value.

            Notes:
                The UUID of the shunt VLAN on the NSG hosting the Virtual Uplink.

                
                This attribute is named `shuntVLANID` in VSD API.
                
        """
        self._shunt_vlanid = value

    
    @property
    def virtual_uplink_datapath_id(self):
        """ Get virtual_uplink_datapath_id value.

            Notes:
                IP format of system generated identifier of an uplink on NSG.

                
                This attribute is named `virtualUplinkDatapathID` in VSD API.
                
        """
        return self._virtual_uplink_datapath_id

    @virtual_uplink_datapath_id.setter
    def virtual_uplink_datapath_id(self, value):
        """ Set virtual_uplink_datapath_id value.

            Notes:
                IP format of system generated identifier of an uplink on NSG.

                
                This attribute is named `virtualUplinkDatapathID` in VSD API.
                
        """
        self._virtual_uplink_datapath_id = value

    
    @property
    def enable_nat_probes(self):
        """ Get enable_nat_probes value.

            Notes:
                If enabled, probes will be sent to other NSGs and DTLS sessions for IPSEC and VXLAN will be set up to the VSCs. If disabled, no NAT probes are sent on that uplink and no DTLS sessions are set up to the VSCs.

                
                This attribute is named `enableNATProbes` in VSD API.
                
        """
        return self._enable_nat_probes

    @enable_nat_probes.setter
    def enable_nat_probes(self, value):
        """ Set enable_nat_probes value.

            Notes:
                If enabled, probes will be sent to other NSGs and DTLS sessions for IPSEC and VXLAN will be set up to the VSCs. If disabled, no NAT probes are sent on that uplink and no DTLS sessions are set up to the VSCs.

                
                This attribute is named `enableNATProbes` in VSD API.
                
        """
        self._enable_nat_probes = value

    
    @property
    def underlay_id(self):
        """ Get underlay_id value.

            Notes:
                Underlay Identifier of underlay associated with the uplink mirrored by this Virtual Uplink.

                
                This attribute is named `underlayID` in VSD API.
                
        """
        return self._underlay_id

    @underlay_id.setter
    def underlay_id(self, value):
        """ Set underlay_id value.

            Notes:
                Underlay Identifier of underlay associated with the uplink mirrored by this Virtual Uplink.

                
                This attribute is named `underlayID` in VSD API.
                
        """
        self._underlay_id = value

    
    @property
    def underlay_nat(self):
        """ Get underlay_nat value.

            Notes:
                Indicates whether PAT is enabled on the underlay for this uplink connection. Inherits the PATEnabled attribute from remote uplink connection.

                
                This attribute is named `underlayNAT` in VSD API.
                
        """
        return self._underlay_nat

    @underlay_nat.setter
    def underlay_nat(self, value):
        """ Set underlay_nat value.

            Notes:
                Indicates whether PAT is enabled on the underlay for this uplink connection. Inherits the PATEnabled attribute from remote uplink connection.

                
                This attribute is named `underlayNAT` in VSD API.
                
        """
        self._underlay_nat = value

    
    @property
    def underlay_name(self):
        """ Get underlay_name value.

            Notes:
                Name of the underlay associated with the uplink mirrored by this Virtual Uplink.

                
                This attribute is named `underlayName` in VSD API.
                
        """
        return self._underlay_name

    @underlay_name.setter
    def underlay_name(self, value):
        """ Set underlay_name value.

            Notes:
                Name of the underlay associated with the uplink mirrored by this Virtual Uplink.

                
                This attribute is named `underlayName` in VSD API.
                
        """
        self._underlay_name = value

    
    @property
    def underlay_routing(self):
        """ Get underlay_routing value.

            Notes:
                Indicates whether route to underlay is enabled on the uplink connection that this Virtual uplink mirrors.

                
                This attribute is named `underlayRouting` in VSD API.
                
        """
        return self._underlay_routing

    @underlay_routing.setter
    def underlay_routing(self, value):
        """ Set underlay_routing value.

            Notes:
                Indicates whether route to underlay is enabled on the uplink connection that this Virtual uplink mirrors.

                
                This attribute is named `underlayRouting` in VSD API.
                
        """
        self._underlay_routing = value

    
    @property
    def role(self):
        """ Get role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

                
        """
        return self._role

    @role.setter
    def role(self, value):
        """ Set role value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, This attribute represents the configuration on the remote uplink connection that this virtual uplink mirrors.

                
        """
        self._role = value

    
    @property
    def role_order(self):
        """ Get role_order value.

            Notes:
                Determines the order in which uplinks are configured on NSG. It also determines the priority for an Uplink for management traffic. This value will be auto-generated based on the order of creation of Virtual Uplink.

                
                This attribute is named `roleOrder` in VSD API.
                
        """
        return self._role_order

    @role_order.setter
    def role_order(self, value):
        """ Set role_order value.

            Notes:
                Determines the order in which uplinks are configured on NSG. It also determines the priority for an Uplink for management traffic. This value will be auto-generated based on the order of creation of Virtual Uplink.

                
                This attribute is named `roleOrder` in VSD API.
                
        """
        self._role_order = value

    
    @property
    def traffic_through_ubr_only(self):
        """ Get traffic_through_ubr_only value.

            Notes:
                If enabled, cuts down the number of probes to just the number of provisioned UBRs. This attribute represents "             + "the configuration on the remote uplink connection that this virtual uplink mirrors.

                
                This attribute is named `trafficThroughUBROnly` in VSD API.
                
        """
        return self._traffic_through_ubr_only

    @traffic_through_ubr_only.setter
    def traffic_through_ubr_only(self, value):
        """ Set traffic_through_ubr_only value.

            Notes:
                If enabled, cuts down the number of probes to just the number of provisioned UBRs. This attribute represents "             + "the configuration on the remote uplink connection that this virtual uplink mirrors.

                
                This attribute is named `trafficThroughUBROnly` in VSD API.
                
        """
        self._traffic_through_ubr_only = value

    
    @property
    def associated_egress_qo_s_policy_id(self):
        """ Get associated_egress_qo_s_policy_id value.

            Notes:
                ID of the Egress QoS Policy associated with remote VlLAN.

                
                This attribute is named `associatedEgressQoSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qo_s_policy_id

    @associated_egress_qo_s_policy_id.setter
    def associated_egress_qo_s_policy_id(self, value):
        """ Set associated_egress_qo_s_policy_id value.

            Notes:
                ID of the Egress QoS Policy associated with remote VlLAN.

                
                This attribute is named `associatedEgressQoSPolicyID` in VSD API.
                
        """
        self._associated_egress_qo_s_policy_id = value

    
    @property
    def associated_ingress_overlay_qo_s_policer_id(self):
        """ Get associated_ingress_overlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Overlay QoS Policer associated with the remote VlLAN.

                
                This attribute is named `associatedIngressOverlayQoSPolicerID` in VSD API.
                
        """
        return self._associated_ingress_overlay_qo_s_policer_id

    @associated_ingress_overlay_qo_s_policer_id.setter
    def associated_ingress_overlay_qo_s_policer_id(self, value):
        """ Set associated_ingress_overlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Overlay QoS Policer associated with the remote VlLAN.

                
                This attribute is named `associatedIngressOverlayQoSPolicerID` in VSD API.
                
        """
        self._associated_ingress_overlay_qo_s_policer_id = value

    
    @property
    def associated_ingress_qo_s_policy_id(self):
        """ Get associated_ingress_qo_s_policy_id value.

            Notes:
                ID of the Ingress QoS Policy / Tunnel Shaper associated with the remote VLAN.

                
                This attribute is named `associatedIngressQoSPolicyID` in VSD API.
                
        """
        return self._associated_ingress_qo_s_policy_id

    @associated_ingress_qo_s_policy_id.setter
    def associated_ingress_qo_s_policy_id(self, value):
        """ Set associated_ingress_qo_s_policy_id value.

            Notes:
                ID of the Ingress QoS Policy / Tunnel Shaper associated with the remote VLAN.

                
                This attribute is named `associatedIngressQoSPolicyID` in VSD API.
                
        """
        self._associated_ingress_qo_s_policy_id = value

    
    @property
    def associated_ingress_underlay_qo_s_policer_id(self):
        """ Get associated_ingress_underlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Underlay QoS Policer associated with the remote VLAN.

                
                This attribute is named `associatedIngressUnderlayQoSPolicerID` in VSD API.
                
        """
        return self._associated_ingress_underlay_qo_s_policer_id

    @associated_ingress_underlay_qo_s_policer_id.setter
    def associated_ingress_underlay_qo_s_policer_id(self, value):
        """ Set associated_ingress_underlay_qo_s_policer_id value.

            Notes:
                ID of the Ingress Underlay QoS Policer associated with the remote VLAN.

                
                This attribute is named `associatedIngressUnderlayQoSPolicerID` in VSD API.
                
        """
        self._associated_ingress_underlay_qo_s_policer_id = value

    
    @property
    def associated_uplink_connection_id(self):
        """ Get associated_uplink_connection_id value.

            Notes:
                UUID of the uplink connection from the peer NSG that this virtual uplink mirrors.

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        return self._associated_uplink_connection_id

    @associated_uplink_connection_id.setter
    def associated_uplink_connection_id(self, value):
        """ Set associated_uplink_connection_id value.

            Notes:
                UUID of the uplink connection from the peer NSG that this virtual uplink mirrors.

                
                This attribute is named `associatedUplinkConnectionID` in VSD API.
                
        """
        self._associated_uplink_connection_id = value

    
    @property
    def associated_vsc_profile_id(self):
        """ Get associated_vsc_profile_id value.

            Notes:
                The associated VSC profile of remote control uplink.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        return self._associated_vsc_profile_id

    @associated_vsc_profile_id.setter
    def associated_vsc_profile_id(self, value):
        """ Set associated_vsc_profile_id value.

            Notes:
                The associated VSC profile of remote control uplink.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        self._associated_vsc_profile_id = value

    
    @property
    def aux_mode(self):
        """ Get aux_mode value.

            Notes:
                Type of redundancy offered by the Uplink that is mirrored by this Virtual uplink when marked as auxiliary.

                
                This attribute is named `auxMode` in VSD API.
                
        """
        return self._aux_mode

    @aux_mode.setter
    def aux_mode(self, value):
        """ Set aux_mode value.

            Notes:
                Type of redundancy offered by the Uplink that is mirrored by this Virtual uplink when marked as auxiliary.

                
                This attribute is named `auxMode` in VSD API.
                
        """
        self._aux_mode = value

    

    