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


from .fetchers import NUQOSsFetcher

from bambou import NURESTObject


class NUPolicyDecision(NURESTObject):
    """ Represents a PolicyDecision in the VSD

        Notes:
            This object is a read only object that provides the policy decisions for a particular VM interface.
    """

    __rest_name__ = "policydecision"
    __resource_name__ = "policydecisions"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PolicyDecision instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> policydecision = NUPolicyDecision(id=u'xxxx-xxx-xxx-xxx', name=u'PolicyDecision')
                >>> policydecision = NUPolicyDecision(data=my_dict)
        """

        super(NUPolicyDecision, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._egress_acls = None
        self._egress_qos = None
        self._fip_acls = None
        self._ingress_acls = None
        self._ingress_adv_fwd = None
        self._ingress_external_service_acls = None
        self._entity_scope = None
        self._qos = None
        self._stats = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="egress_acls", remote_name="egressACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="egress_qos", remote_name="egressQos", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="fip_acls", remote_name="fipACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ingress_acls", remote_name="ingressACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ingress_adv_fwd", remote_name="ingressAdvFwd", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ingress_external_service_acls", remote_name="ingressExternalServiceACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="qos", remote_name="qos", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats", remote_name="stats", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
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
    def egress_acls(self):
        """ Get egress_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `egressACLs` in VSD API.
                
        """
        return self._egress_acls

    @egress_acls.setter
    def egress_acls(self, value):
        """ Set egress_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `egressACLs` in VSD API.
                
        """
        self._egress_acls = value

    
    @property
    def egress_qos(self):
        """ Get egress_qos value.

            Notes:
                Egress QoS primitive that was selected

                
                This attribute is named `egressQos` in VSD API.
                
        """
        return self._egress_qos

    @egress_qos.setter
    def egress_qos(self, value):
        """ Set egress_qos value.

            Notes:
                Egress QoS primitive that was selected

                
                This attribute is named `egressQos` in VSD API.
                
        """
        self._egress_qos = value

    
    @property
    def fip_acls(self):
        """ Get fip_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `fipACLs` in VSD API.
                
        """
        return self._fip_acls

    @fip_acls.setter
    def fip_acls(self, value):
        """ Set fip_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `fipACLs` in VSD API.
                
        """
        self._fip_acls = value

    
    @property
    def ingress_acls(self):
        """ Get ingress_acls value.

            Notes:
                List of actual Ingress ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressACLs` in VSD API.
                
        """
        return self._ingress_acls

    @ingress_acls.setter
    def ingress_acls(self, value):
        """ Set ingress_acls value.

            Notes:
                List of actual Ingress ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressACLs` in VSD API.
                
        """
        self._ingress_acls = value

    
    @property
    def ingress_adv_fwd(self):
        """ Get ingress_adv_fwd value.

            Notes:
                List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressAdvFwd` in VSD API.
                
        """
        return self._ingress_adv_fwd

    @ingress_adv_fwd.setter
    def ingress_adv_fwd(self, value):
        """ Set ingress_adv_fwd value.

            Notes:
                List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressAdvFwd` in VSD API.
                
        """
        self._ingress_adv_fwd = value

    
    @property
    def ingress_external_service_acls(self):
        """ Get ingress_external_service_acls value.

            Notes:
                List of actual Ingress External Service ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressExternalServiceACLs` in VSD API.
                
        """
        return self._ingress_external_service_acls

    @ingress_external_service_acls.setter
    def ingress_external_service_acls(self, value):
        """ Set ingress_external_service_acls value.

            Notes:
                List of actual Ingress External Service ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressExternalServiceACLs` in VSD API.
                
        """
        self._ingress_external_service_acls = value

    
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
    def qos(self):
        """ Get qos value.

            Notes:
                QoS primitive that was selected based on inheritance policies

                
        """
        return self._qos

    @qos.setter
    def qos(self, value):
        """ Set qos value.

            Notes:
                QoS primitive that was selected based on inheritance policies

                
        """
        self._qos = value

    
    @property
    def stats(self):
        """ Get stats value.

            Notes:
                Stats primitive that was selected based on inheritance policies

                
        """
        return self._stats

    @stats.setter
    def stats(self, value):
        """ Set stats value.

            Notes:
                Stats primitive that was selected based on inheritance policies

                
        """
        self._stats = value

    
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

    

    