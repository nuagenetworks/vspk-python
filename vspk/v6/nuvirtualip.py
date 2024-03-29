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




from .fetchers import NUPermissionsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUEventLogsFetcher

from bambou import NURESTObject


class NUVirtualIP(NURESTObject):
    """ Represents a VirtualIP in the VSD

        Notes:
            Virtual IPs are IP addresses owned by one or more vports that can move among those vports. VSP will track the owner of a virtual IP and steer traffic accordingly. Virtual IPs can be used as next-hops for static routes and other re-direction purposes.
    """

    __rest_name__ = "virtualip"
    __resource_name__ = "virtualips"

    
    ## Constants
    
    CONST_IP_TYPE_IPV6 = "IPV6"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VirtualIP instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> virtualip = NUVirtualIP(id=u'xxxx-xxx-xxx-xxx', name=u'VirtualIP')
                >>> virtualip = NUVirtualIP(data=my_dict)
        """

        super(NUVirtualIP, self).__init__()

        # Read/Write Attributes
        
        self._mac = None
        self._ip_type = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._virtual_ip = None
        self._embedded_metadata = None
        self._entity_scope = None
        self._creation_date = None
        self._associated_floating_ip_id = None
        self._associated_secondary_floating_ip_id = None
        self._subnet_id = None
        self._owner = None
        self._external_id = None
        
        self.expose_attribute(local_name="mac", remote_name="MAC", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_date", remote_name="lastUpdatedDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="virtual_ip", remote_name="virtualIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="embedded_metadata", remote_name="embeddedMetadata", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="creation_date", remote_name="creationDate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_floating_ip_id", remote_name="associatedFloatingIPID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_secondary_floating_ip_id", remote_name="associatedSecondaryFloatingIPID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="subnet_id", remote_name="subnetID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="owner", remote_name="owner", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.permissions = NUPermissionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def mac(self):
        """ Get mac value.

            Notes:
                The MAC address of the virtual port

                
                This attribute is named `MAC` in VSD API.
                
        """
        return self._mac

    @mac.setter
    def mac(self, value):
        """ Set mac value.

            Notes:
                The MAC address of the virtual port

                
                This attribute is named `MAC` in VSD API.
                
        """
        self._mac = value

    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                Specify if the virtualIP attribute value is in IPv4 or IPv6 format

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                Specify if the virtualIP attribute value is in IPv4 or IPv6 format

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
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
    def last_updated_date(self):
        """ Get last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, value):
        """ Set last_updated_date value.

            Notes:
                Time stamp when this object was last updated.

                
                This attribute is named `lastUpdatedDate` in VSD API.
                
        """
        self._last_updated_date = value

    
    @property
    def virtual_ip(self):
        """ Get virtual_ip value.

            Notes:
                Virtual IP address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, value):
        """ Set virtual_ip value.

            Notes:
                Virtual IP address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        self._virtual_ip = value

    
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
    def creation_date(self):
        """ Get creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        """ Set creation_date value.

            Notes:
                Time stamp when this object was created.

                
                This attribute is named `creationDate` in VSD API.
                
        """
        self._creation_date = value

    
    @property
    def associated_floating_ip_id(self):
        """ Get associated_floating_ip_id value.

            Notes:
                ID of Floating IP address associated to this virtual IP

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        return self._associated_floating_ip_id

    @associated_floating_ip_id.setter
    def associated_floating_ip_id(self, value):
        """ Set associated_floating_ip_id value.

            Notes:
                ID of Floating IP address associated to this virtual IP

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        self._associated_floating_ip_id = value

    
    @property
    def associated_secondary_floating_ip_id(self):
        """ Get associated_secondary_floating_ip_id value.

            Notes:
                ID of Secondary Floating IP address associated to this virtual IP

                
                This attribute is named `associatedSecondaryFloatingIPID` in VSD API.
                
        """
        return self._associated_secondary_floating_ip_id

    @associated_secondary_floating_ip_id.setter
    def associated_secondary_floating_ip_id(self, value):
        """ Set associated_secondary_floating_ip_id value.

            Notes:
                ID of Secondary Floating IP address associated to this virtual IP

                
                This attribute is named `associatedSecondaryFloatingIPID` in VSD API.
                
        """
        self._associated_secondary_floating_ip_id = value

    
    @property
    def subnet_id(self):
        """ Get subnet_id value.

            Notes:
                ID of subnet to which this IP address belongs

                
                This attribute is named `subnetID` in VSD API.
                
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, value):
        """ Set subnet_id value.

            Notes:
                ID of subnet to which this IP address belongs

                
                This attribute is named `subnetID` in VSD API.
                
        """
        self._subnet_id = value

    
    @property
    def owner(self):
        """ Get owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """ Set owner value.

            Notes:
                Identifies the user that has created this object.

                
        """
        self._owner = value

    
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

    

    