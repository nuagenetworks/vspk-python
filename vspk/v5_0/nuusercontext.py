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


from bambou import NURESTObject


class NUUserContext(NURESTObject):
    """ Represents a UserContext in the VSD

        Notes:
            This defines a proxy class to expose some of the configuration parameters which are required by UI
    """

    __rest_name__ = "usercontext"
    __resource_name__ = "usercontexts"

    

    def __init__(self, **kwargs):
        """ Initializes a UserContext instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> usercontext = NUUserContext(id=u'xxxx-xxx-xxx-xxx', name=u'UserContext')
                >>> usercontext = NUUserContext(data=my_dict)
        """

        super(NUUserContext, self).__init__()

        # Read/Write Attributes
        
        self._aar_flow_stats_interval = None
        self._aar_probe_stats_interval = None
        self._vss_stats_interval = None
        self._flow_collection_enabled = None
        self._statistics_enabled = None
        self._stats_tsdb_server_address = None
        
        self.expose_attribute(local_name="aar_flow_stats_interval", remote_name="AARFlowStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="aar_probe_stats_interval", remote_name="AARProbeStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="vss_stats_interval", remote_name="VSSStatsInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="flow_collection_enabled", remote_name="flowCollectionEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="statistics_enabled", remote_name="statisticsEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_tsdb_server_address", remote_name="statsTSDBServerAddress", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def aar_flow_stats_interval(self):
        """ Get aar_flow_stats_interval value.

            Notes:
                Interval for AAR flow stats

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        return self._aar_flow_stats_interval

    @aar_flow_stats_interval.setter
    def aar_flow_stats_interval(self, value):
        """ Set aar_flow_stats_interval value.

            Notes:
                Interval for AAR flow stats

                
                This attribute is named `AARFlowStatsInterval` in VSD API.
                
        """
        self._aar_flow_stats_interval = value

    
    @property
    def aar_probe_stats_interval(self):
        """ Get aar_probe_stats_interval value.

            Notes:
                Interval for AAR probe stats

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        return self._aar_probe_stats_interval

    @aar_probe_stats_interval.setter
    def aar_probe_stats_interval(self, value):
        """ Set aar_probe_stats_interval value.

            Notes:
                Interval for AAR probe stats

                
                This attribute is named `AARProbeStatsInterval` in VSD API.
                
        """
        self._aar_probe_stats_interval = value

    
    @property
    def vss_stats_interval(self):
        """ Get vss_stats_interval value.

            Notes:
                Interval for VSS stats

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        return self._vss_stats_interval

    @vss_stats_interval.setter
    def vss_stats_interval(self, value):
        """ Set vss_stats_interval value.

            Notes:
                Interval for VSS stats

                
                This attribute is named `VSSStatsInterval` in VSD API.
                
        """
        self._vss_stats_interval = value

    
    @property
    def flow_collection_enabled(self):
        """ Get flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        return self._flow_collection_enabled

    @flow_collection_enabled.setter
    def flow_collection_enabled(self, value):
        """ Set flow_collection_enabled value.

            Notes:
                Enables flow statistics collection. It is needed for the VSS feature, and requires a valid VSS license. This option requires 'statisticsEnabled'.

                
                This attribute is named `flowCollectionEnabled` in VSD API.
                
        """
        self._flow_collection_enabled = value

    
    @property
    def statistics_enabled(self):
        """ Get statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        return self._statistics_enabled

    @statistics_enabled.setter
    def statistics_enabled(self, value):
        """ Set statistics_enabled value.

            Notes:
                This flag is used to indicate if statistics is enabled in the system. CSProot is expected to activate this through the enable statistics script.

                
                This attribute is named `statisticsEnabled` in VSD API.
                
        """
        self._statistics_enabled = value

    
    @property
    def stats_tsdb_server_address(self):
        """ Get stats_tsdb_server_address value.

            Notes:
                ip address(es) of the elastic machine

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        return self._stats_tsdb_server_address

    @stats_tsdb_server_address.setter
    def stats_tsdb_server_address(self, value):
        """ Set stats_tsdb_server_address value.

            Notes:
                ip address(es) of the elastic machine

                
                This attribute is named `statsTSDBServerAddress` in VSD API.
                
        """
        self._stats_tsdb_server_address = value

    

    