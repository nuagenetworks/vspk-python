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


class NUNSGatewaySummary(NURESTObject):
    """ Represents a NSGatewaySummary in the VSD

        Notes:
            Summary information such as alarm counts, location, version, boostrap status for Network Services Gateway
    """

    __rest_name__ = "nsgatewayssummary"
    __resource_name__ = "nsgatewayssummaries"

    
    ## Constants
    
    CONST_BOOTSTRAP_STATUS_ACTIVE = "ACTIVE"
    
    CONST_BOOTSTRAP_STATUS_INACTIVE = "INACTIVE"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_SENT = "NOTIFICATION_APP_REQ_SENT"
    
    CONST_BOOTSTRAP_STATUS_CERTIFICATE_REQUIRED = "CERTIFICATE_REQUIRED"
    
    CONST_BOOTSTRAP_STATUS_NOTIFICATION_APP_REQ_ACK = "NOTIFICATION_APP_REQ_ACK"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSGatewaySummary instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgatewaysummary = NUNSGatewaySummary(id=u'xxxx-xxx-xxx-xxx', name=u'NSGatewaySummary')
                >>> nsgatewaysummary = NUNSGatewaySummary(data=my_dict)
        """

        super(NUNSGatewaySummary, self).__init__()

        # Read/Write Attributes
        
        self._major_alarms_count = None
        self._gateway_id = None
        self._gateway_name = None
        self._latitude = None
        self._address = None
        self._time_zone_id = None
        self._minor_alarms_count = None
        self._info_alarms_count = None
        self._enterprise_id = None
        self._locality = None
        self._longitude = None
        self._bootstrap_status = None
        self._country = None
        self._critical_alarms_count = None
        self._nsg_version = None
        self._state = None
        self._system_id = None
        
        self.expose_attribute(local_name="major_alarms_count", remote_name="majorAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_id", remote_name="gatewayID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_name", remote_name="gatewayName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="latitude", remote_name="latitude", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="time_zone_id", remote_name="timeZoneID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="minor_alarms_count", remote_name="minorAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="info_alarms_count", remote_name="infoAlarmsCount", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="locality", remote_name="locality", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="longitude", remote_name="longitude", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="bootstrap_status", remote_name="bootstrapStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACTIVE', u'CERTIFICATE_REQUIRED', u'INACTIVE', u'NOTIFICATION_APP_REQ_ACK', u'NOTIFICATION_APP_REQ_SENT'])
        self.expose_attribute(local_name="country", remote_name="country", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="critical_alarms_count", remote_name="criticalAlarmsCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="nsg_version", remote_name="nsgVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="state", remote_name="state", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_id", remote_name="systemID", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def major_alarms_count(self):
        """ Get major_alarms_count value.

            Notes:
                Total number of alarms with MAJOR severity

                
                This attribute is named `majorAlarmsCount` in VSD API.
                
        """
        return self._major_alarms_count

    @major_alarms_count.setter
    def major_alarms_count(self, value):
        """ Set major_alarms_count value.

            Notes:
                Total number of alarms with MAJOR severity

                
                This attribute is named `majorAlarmsCount` in VSD API.
                
        """
        self._major_alarms_count = value

    
    @property
    def gateway_id(self):
        """ Get gateway_id value.

            Notes:
                The ID of the NSG from which the infomation was collected.

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, value):
        """ Set gateway_id value.

            Notes:
                The ID of the NSG from which the infomation was collected.

                
                This attribute is named `gatewayID` in VSD API.
                
        """
        self._gateway_id = value

    
    @property
    def gateway_name(self):
        """ Get gateway_name value.

            Notes:
                The name of the gateway

                
                This attribute is named `gatewayName` in VSD API.
                
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, value):
        """ Set gateway_name value.

            Notes:
                The name of the gateway

                
                This attribute is named `gatewayName` in VSD API.
                
        """
        self._gateway_name = value

    
    @property
    def latitude(self):
        """ Get latitude value.

            Notes:
                The latitude of the location of the NSG

                
        """
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """ Set latitude value.

            Notes:
                The latitude of the location of the NSG

                
        """
        self._latitude = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                Formatted address including property number, street name, suite or office number of the NSG

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                Formatted address including property number, street name, suite or office number of the NSG

                
        """
        self._address = value

    
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
    def minor_alarms_count(self):
        """ Get minor_alarms_count value.

            Notes:
                Total number of alarms with MINOR severity

                
                This attribute is named `minorAlarmsCount` in VSD API.
                
        """
        return self._minor_alarms_count

    @minor_alarms_count.setter
    def minor_alarms_count(self, value):
        """ Set minor_alarms_count value.

            Notes:
                Total number of alarms with MINOR severity

                
                This attribute is named `minorAlarmsCount` in VSD API.
                
        """
        self._minor_alarms_count = value

    
    @property
    def info_alarms_count(self):
        """ Get info_alarms_count value.

            Notes:
                Total number of alarms with INFO severity

                
                This attribute is named `infoAlarmsCount` in VSD API.
                
        """
        return self._info_alarms_count

    @info_alarms_count.setter
    def info_alarms_count(self, value):
        """ Set info_alarms_count value.

            Notes:
                Total number of alarms with INFO severity

                
                This attribute is named `infoAlarmsCount` in VSD API.
                
        """
        self._info_alarms_count = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                The enterprise associated with this NSG

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                The enterprise associated with this NSG

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def locality(self):
        """ Get locality value.

            Notes:
                Locality/City/County of the NSG

                
        """
        return self._locality

    @locality.setter
    def locality(self, value):
        """ Set locality value.

            Notes:
                Locality/City/County of the NSG

                
        """
        self._locality = value

    
    @property
    def longitude(self):
        """ Get longitude value.

            Notes:
                The longitude of the location of the NSG

                
        """
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """ Set longitude value.

            Notes:
                The longitude of the location of the NSG

                
        """
        self._longitude = value

    
    @property
    def bootstrap_status(self):
        """ Get bootstrap_status value.

            Notes:
                Bootstrap status of the NSG

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        return self._bootstrap_status

    @bootstrap_status.setter
    def bootstrap_status(self, value):
        """ Set bootstrap_status value.

            Notes:
                Bootstrap status of the NSG

                
                This attribute is named `bootstrapStatus` in VSD API.
                
        """
        self._bootstrap_status = value

    
    @property
    def country(self):
        """ Get country value.

            Notes:
                Country in which the NSG is located

                
        """
        return self._country

    @country.setter
    def country(self, value):
        """ Set country value.

            Notes:
                Country in which the NSG is located

                
        """
        self._country = value

    
    @property
    def critical_alarms_count(self):
        """ Get critical_alarms_count value.

            Notes:
                Total number of alarms with CRITICAL severity

                
                This attribute is named `criticalAlarmsCount` in VSD API.
                
        """
        return self._critical_alarms_count

    @critical_alarms_count.setter
    def critical_alarms_count(self, value):
        """ Set critical_alarms_count value.

            Notes:
                Total number of alarms with CRITICAL severity

                
                This attribute is named `criticalAlarmsCount` in VSD API.
                
        """
        self._critical_alarms_count = value

    
    @property
    def nsg_version(self):
        """ Get nsg_version value.

            Notes:
                The NSG Version (software) as reported during bootstrapping or following an upgrade.

                
                This attribute is named `nsgVersion` in VSD API.
                
        """
        return self._nsg_version

    @nsg_version.setter
    def nsg_version(self, value):
        """ Set nsg_version value.

            Notes:
                The NSG Version (software) as reported during bootstrapping or following an upgrade.

                
                This attribute is named `nsgVersion` in VSD API.
                
        """
        self._nsg_version = value

    
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
    def system_id(self):
        """ Get system_id value.

            Notes:
                Identifier of the gateway

                
                This attribute is named `systemID` in VSD API.
                
        """
        return self._system_id

    @system_id.setter
    def system_id(self, value):
        """ Set system_id value.

            Notes:
                Identifier of the gateway

                
                This attribute is named `systemID` in VSD API.
                
        """
        self._system_id = value

    

    