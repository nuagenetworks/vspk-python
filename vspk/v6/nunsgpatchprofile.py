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


class NUNSGPatchProfile(NURESTObject):
    """ Represents a NSGPatchProfile in the VSD

        Notes:
            An NSG Patch Profile contains upgrade information that can be given to an NSG Instance.  The profile contains details on where the NSG can retrieve the image to upgrade to, and some criteria related to when the upgrade is to happen once the NSG device has received the information for upgrading.
    """

    __rest_name__ = "nsgpatchprofile"
    __resource_name__ = "nsgpatchprofiles"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGPatchProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgpatchprofile = NUNSGPatchProfile(id=u'xxxx-xxx-xxx-xxx', name=u'NSGPatchProfile')
                >>> nsgpatchprofile = NUNSGPatchProfile(data=my_dict)
        """

        super(NUNSGPatchProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._last_updated_by = None
        self._patch_tag = None
        self._patch_url = None
        self._description = None
        self._enterprise_id = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_tag", remote_name="patchTag", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="patch_url", remote_name="patchURL", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                A unique name identifying this patch profile.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                A unique name identifying this patch profile.

                
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
    def patch_tag(self):
        """ Get patch_tag value.

            Notes:
                A unique brief name and version of the patch derived from Patch URL.

                
                This attribute is named `patchTag` in VSD API.
                
        """
        return self._patch_tag

    @patch_tag.setter
    def patch_tag(self, value):
        """ Set patch_tag value.

            Notes:
                A unique brief name and version of the patch derived from Patch URL.

                
                This attribute is named `patchTag` in VSD API.
                
        """
        self._patch_tag = value

    
    @property
    def patch_url(self):
        """ Get patch_url value.

            Notes:
                URL to retrieve the patch bundle for this particular patch.

                
                This attribute is named `patchURL` in VSD API.
                
        """
        return self._patch_url

    @patch_url.setter
    def patch_url(self, value):
        """ Set patch_url value.

            Notes:
                URL to retrieve the patch bundle for this particular patch.

                
                This attribute is named `patchURL` in VSD API.
                
        """
        self._patch_url = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A brief description of this patch profile.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A brief description of this patch profile.

                
        """
        self._description = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise/Organisation that this patch profile belongs to.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise/Organisation that this patch profile belongs to.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
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

    

    