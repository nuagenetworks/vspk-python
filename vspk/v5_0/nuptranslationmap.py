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


class NUPTranslationMap(NURESTObject):
    """ Represents a PTranslationMap in the VSD

        Notes:
            1:1 mappings of private IPs in provider domain to the provider  alias (public) IPs in customer domain and N:1 mappings of a collection of provider private IPs to a provider alias IP into the customer domain.
    """

    __rest_name__ = "ptranslationmap"
    __resource_name__ = "ptranslationmaps"

    
    ## Constants
    
    CONST_MAPPING_TYPE_PAT = "PAT"
    
    CONST_MAPPING_TYPE_NAT = "NAT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a PTranslationMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ptranslationmap = NUPTranslationMap(id=u'xxxx-xxx-xxx-xxx', name=u'PTranslationMap')
                >>> ptranslationmap = NUPTranslationMap(data=my_dict)
        """

        super(NUPTranslationMap, self).__init__()

        # Read/Write Attributes
        
        self._spat_source_list = None
        self._mapping_type = None
        self._provider_alias_ip = None
        self._provider_ip = None
        
        self.expose_attribute(local_name="spat_source_list", remote_name="SPATSourceList", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name="mapping_type", remote_name="mappingType", attribute_type=str, is_required=True, is_unique=False, choices=[u'NAT', u'PAT'])
        self.expose_attribute(local_name="provider_alias_ip", remote_name="providerAliasIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="provider_ip", remote_name="providerIP", attribute_type=str, is_required=True, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def spat_source_list(self):
        """ Get spat_source_list value.

            Notes:
                The list of provider source IPs to be SPAT'd.

                
                This attribute is named `SPATSourceList` in VSD API.
                
        """
        return self._spat_source_list

    @spat_source_list.setter
    def spat_source_list(self, value):
        """ Set spat_source_list value.

            Notes:
                The list of provider source IPs to be SPAT'd.

                
                This attribute is named `SPATSourceList` in VSD API.
                
        """
        self._spat_source_list = value

    
    @property
    def mapping_type(self):
        """ Get mapping_type value.

            Notes:
                1:1 NATmapping, or *:1 PAT mappings

                
                This attribute is named `mappingType` in VSD API.
                
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, value):
        """ Set mapping_type value.

            Notes:
                1:1 NATmapping, or *:1 PAT mappings

                
                This attribute is named `mappingType` in VSD API.
                
        """
        self._mapping_type = value

    
    @property
    def provider_alias_ip(self):
        """ Get provider_alias_ip value.

            Notes:
                Provider public IP in Customer Domain

                
                This attribute is named `providerAliasIP` in VSD API.
                
        """
        return self._provider_alias_ip

    @provider_alias_ip.setter
    def provider_alias_ip(self, value):
        """ Set provider_alias_ip value.

            Notes:
                Provider public IP in Customer Domain

                
                This attribute is named `providerAliasIP` in VSD API.
                
        """
        self._provider_alias_ip = value

    
    @property
    def provider_ip(self):
        """ Get provider_ip value.

            Notes:
                Provider private IP in Provider Domain.

                
                This attribute is named `providerIP` in VSD API.
                
        """
        return self._provider_ip

    @provider_ip.setter
    def provider_ip(self, value):
        """ Set provider_ip value.

            Notes:
                Provider private IP in Provider Domain.

                
                This attribute is named `providerIP` in VSD API.
                
        """
        self._provider_ip = value

    

    