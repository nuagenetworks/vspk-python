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


class NUSupplementalInfraConfig(NURESTObject):
    """ Represents a SupplementalInfraConfig in the VSD

        Notes:
            Supplemental infrastructure configuration which includes information in addition to the existing infrastructure configuration. Encapsulates properties with large data or those properties for which the existing infraconfig work-flow is not to be disturbed.
    """

    __rest_name__ = "supplementalinfraconfig"
    __resource_name__ = "supplementalinfraconfig"

    

    def __init__(self, **kwargs):
        """ Initializes a SupplementalInfraConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> supplementalinfraconfig = NUSupplementalInfraConfig(id=u'xxxx-xxx-xxx-xxx', name=u'SupplementalInfraConfig')
                >>> supplementalinfraconfig = NUSupplementalInfraConfig(data=my_dict)
        """

        super(NUSupplementalInfraConfig, self).__init__()

        # Read/Write Attributes
        
        self._supplemental_config = None
        
        self.expose_attribute(local_name="supplemental_config", remote_name="supplementalConfig", attribute_type=dict, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def supplemental_config(self):
        """ Get supplemental_config value.

            Notes:
                Supplemental infrastructure configuration object having supplemental information required by NSG e.g. blockedPageText, avatar, avatarType etc.

                
                This attribute is named `supplementalConfig` in VSD API.
                
        """
        return self._supplemental_config

    @supplemental_config.setter
    def supplemental_config(self, value):
        """ Set supplemental_config value.

            Notes:
                Supplemental infrastructure configuration object having supplemental information required by NSG e.g. blockedPageText, avatar, avatarType etc.

                
                This attribute is named `supplementalConfig` in VSD API.
                
        """
        self._supplemental_config = value

    

    