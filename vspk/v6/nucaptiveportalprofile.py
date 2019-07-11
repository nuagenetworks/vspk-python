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


class NUCaptivePortalProfile(NURESTObject):
    """ Represents a CaptivePortalProfile in the VSD

        Notes:
            Object representing a Wireless Access Captive Portal Profile which can be associated with SSID entities from which end users may be presented with instructions and condition of use when connecting to an open wireless access point.
    """

    __rest_name__ = "captiveportalprofile"
    __resource_name__ = "captiveportalprofiles"

    
    ## Constants
    
    CONST_PORTAL_TYPE_CLICK_THROUGH = "CLICK_THROUGH"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a CaptivePortalProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> captiveportalprofile = NUCaptivePortalProfile(id=u'xxxx-xxx-xxx-xxx', name=u'CaptivePortalProfile')
                >>> captiveportalprofile = NUCaptivePortalProfile(data=my_dict)
        """

        super(NUCaptivePortalProfile, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._captive_page = None
        self._last_updated_by = None
        self._description = None
        self._entity_scope = None
        self._portal_type = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=True)
        self.expose_attribute(local_name="captive_page", remote_name="captivePage", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="portal_type", remote_name="portalType", attribute_type=str, is_required=True, is_unique=False, choices=[u'CLICK_THROUGH'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the captive portal profile.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the captive portal profile.

                
        """
        self._name = value

    
    @property
    def captive_page(self):
        """ Get captive_page value.

            Notes:
                Attribute having the contents of captive portal page displayed to end user. User can possibly include very basic HTML tags like <p>, <ul> etc. in order to fomat the text displayed to the user.

                
                This attribute is named `captivePage` in VSD API.
                
        """
        return self._captive_page

    @captive_page.setter
    def captive_page(self, value):
        """ Set captive_page value.

            Notes:
                Attribute having the contents of captive portal page displayed to end user. User can possibly include very basic HTML tags like <p>, <ul> etc. in order to fomat the text displayed to the user.

                
                This attribute is named `captivePage` in VSD API.
                
        """
        self._captive_page = value

    
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
    def description(self):
        """ Get description value.

            Notes:
                Description for the captive portal profile.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description for the captive portal profile.

                
        """
        self._description = value

    
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
    def portal_type(self):
        """ Get portal_type value.

            Notes:
                Type of the portal page.  Will decide if the NSG rendering the page will have a strict rendering of the welcoming page based on what is given by VSD, or if the information can be made customisable by an operator to include animations, videos, images, and other types of more complex scripts.

                
                This attribute is named `portalType` in VSD API.
                
        """
        return self._portal_type

    @portal_type.setter
    def portal_type(self, value):
        """ Set portal_type value.

            Notes:
                Type of the portal page.  Will decide if the NSG rendering the page will have a strict rendering of the welcoming page based on what is given by VSD, or if the information can be made customisable by an operator to include animations, videos, images, and other types of more complex scripts.

                
                This attribute is named `portalType` in VSD API.
                
        """
        self._portal_type = value

    
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

    

    