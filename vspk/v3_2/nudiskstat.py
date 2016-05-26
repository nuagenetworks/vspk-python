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


class NUDiskStat(NURESTObject):
    """ Represents a DiskStat in the VSD

        Notes:
            Encapsulates the disk usage metrics for system monitor entity.
    """

    __rest_name__ = "diskstat"
    __resource_name__ = "diskstats"

    
    ## Constants
    
    CONST_UNIT_KB = "KB"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_UNIT_MB = "MB"
    
    CONST_UNIT_YB = "YB"
    
    CONST_UNIT_BYTES = "Bytes"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_UNIT_ZB = "ZB"
    
    CONST_UNIT_EB = "EB"
    
    CONST_UNIT_PB = "PB"
    
    CONST_UNIT_GB = "GB"
    
    CONST_UNIT_TB = "TB"
    
    

    def __init__(self, **kwargs):
        """ Initializes a DiskStat instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> diskstat = NUDiskStat(id=u'xxxx-xxx-xxx-xxx', name=u'DiskStat')
                >>> diskstat = NUDiskStat(data=my_dict)
        """

        super(NUDiskStat, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._size = None
        self._unit = None
        self._entity_scope = None
        self._used = None
        self._available = None
        self._external_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="size", remote_name="size", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="unit", remote_name="unit", attribute_type=str, is_required=False, is_unique=False, choices=[u'Bytes', u'EB', u'GB', u'KB', u'MB', u'PB', u'TB', u'YB', u'ZB'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="used", remote_name="used", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="available", remote_name="available", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the disk.

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the disk.

                
        """
        self._name = value

    
    @property
    def size(self):
        """ Get size value.

            Notes:
                Total disk space.

                
        """
        return self._size

    @size.setter
    def size(self, value):
        """ Set size value.

            Notes:
                Total disk space.

                
        """
        self._size = value

    
    @property
    def unit(self):
        """ Get unit value.

            Notes:
                Storage unit type (example: bytes, KB, MB, etc.,).

                
        """
        return self._unit

    @unit.setter
    def unit(self, value):
        """ Set unit value.

            Notes:
                Storage unit type (example: bytes, KB, MB, etc.,).

                
        """
        self._unit = value

    
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
    def used(self):
        """ Get used value.

            Notes:
                Disk space used.

                
        """
        return self._used

    @used.setter
    def used(self, value):
        """ Set used value.

            Notes:
                Disk space used.

                
        """
        self._used = value

    
    @property
    def available(self):
        """ Get available value.

            Notes:
                Available disk space.

                
        """
        return self._available

    @available.setter
    def available(self, value):
        """ Set available value.

            Notes:
                Available disk space.

                
        """
        self._available = value

    
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

    

    