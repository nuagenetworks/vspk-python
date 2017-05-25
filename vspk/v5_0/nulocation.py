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


class NULocation(NURESTObject):
    """ Represents a Location in the VSD

        Notes:
            Gateway location details.
    """

    __rest_name__ = "location"
    __resource_name__ = "locations"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Location instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> location = NULocation(id=u'xxxx-xxx-xxx-xxx', name=u'Location')
                >>> location = NULocation(data=my_dict)
        """

        super(NULocation, self).__init__()

        # Read/Write Attributes
        
        self._last_updated_by = None
        self._latitude = None
        self._address = None
        self._ignore_geocode = None
        self._time_zone_id = None
        self._entity_scope = None
        self._locality = None
        self._longitude = None
        self._country = None
        self._state = None
        self._external_id = None
        
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="latitude", remote_name="latitude", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ignore_geocode", remote_name="ignoreGeocode", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="time_zone_id", remote_name="timeZoneID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="locality", remote_name="locality", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="longitude", remote_name="longitude", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="country", remote_name="country", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="state", remote_name="state", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

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
    def latitude(self):
        """ Get latitude value.

            Notes:
                Latitude in decimal format.

                
        """
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """ Set latitude value.

            Notes:
                Latitude in decimal format.

                
        """
        self._latitude = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                Formatted address including property number, street name, suite or office number, ...

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                Formatted address including property number, street name, suite or office number, ...

                
        """
        self._address = value

    
    @property
    def ignore_geocode(self):
        """ Get ignore_geocode value.

            Notes:
                Request BSS to perform a geocode on the address - If no value passed, requestGeocode will be set to true

                
                This attribute is named `ignoreGeocode` in VSD API.
                
        """
        return self._ignore_geocode

    @ignore_geocode.setter
    def ignore_geocode(self, value):
        """ Set ignore_geocode value.

            Notes:
                Request BSS to perform a geocode on the address - If no value passed, requestGeocode will be set to true

                
                This attribute is named `ignoreGeocode` in VSD API.
                
        """
        self._ignore_geocode = value

    
    @property
    def time_zone_id(self):
        """ Get time_zone_id value.

            Notes:
                Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

                
                This attribute is named `timeZoneID` in VSD API.
                
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, value):
        """ Set time_zone_id value.

            Notes:
                Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

                
                This attribute is named `timeZoneID` in VSD API.
                
        """
        self._time_zone_id = value

    
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
    def locality(self):
        """ Get locality value.

            Notes:
                Locality/City/County

                
        """
        return self._locality

    @locality.setter
    def locality(self, value):
        """ Set locality value.

            Notes:
                Locality/City/County

                
        """
        self._locality = value

    
    @property
    def longitude(self):
        """ Get longitude value.

            Notes:
                Longitude in decimal format.

                
        """
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """ Set longitude value.

            Notes:
                Longitude in decimal format.

                
        """
        self._longitude = value

    
    @property
    def country(self):
        """ Get country value.

            Notes:
                Country

                
        """
        return self._country

    @country.setter
    def country(self, value):
        """ Set country value.

            Notes:
                Country

                
        """
        self._country = value

    
    @property
    def state(self):
        """ Get state value.

            Notes:
                State/Province/Region

                
        """
        return self._state

    @state.setter
    def state(self, value):
        """ Set state value.

            Notes:
                State/Province/Region

                
        """
        self._state = value

    
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

    

    