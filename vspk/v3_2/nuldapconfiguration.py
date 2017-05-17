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


class NULDAPConfiguration(NURESTObject):
    """ Represents a LDAPConfiguration in the VSD

        Notes:
            Configuration of LDAP parameters associated with an enterprise. This will enable authentication through an external LDAP server for this enterprise.
    """

    __rest_name__ = "ldapconfiguration"
    __resource_name__ = "ldapconfigurations"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a LDAPConfiguration instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ldapconfiguration = NULDAPConfiguration(id=u'xxxx-xxx-xxx-xxx', name=u'LDAPConfiguration')
                >>> ldapconfiguration = NULDAPConfiguration(data=my_dict)
        """

        super(NULDAPConfiguration, self).__init__()

        # Read/Write Attributes
        
        self._ssl_enabled = None
        self._password = None
        self._last_updated_by = None
        self._accept_all_certificates = None
        self._certificate = None
        self._server = None
        self._enabled = None
        self._entity_scope = None
        self._port = None
        self._group_dn = None
        self._user_dn_template = None
        self._authorization_enabled = None
        self._authorizing_user_dn = None
        self._external_id = None
        
        self.expose_attribute(local_name="ssl_enabled", remote_name="SSLEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="password", remote_name="password", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="accept_all_certificates", remote_name="acceptAllCertificates", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="certificate", remote_name="certificate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="server", remote_name="server", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="enabled", remote_name="enabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="port", remote_name="port", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="group_dn", remote_name="groupDN", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="user_dn_template", remote_name="userDNTemplate", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="authorization_enabled", remote_name="authorizationEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="authorizing_user_dn", remote_name="authorizingUserDN", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ssl_enabled(self):
        """ Get ssl_enabled value.

            Notes:
                Enable SSL for communication with the LDAP server

                
                This attribute is named `SSLEnabled` in VSD API.
                
        """
        return self._ssl_enabled

    @ssl_enabled.setter
    def ssl_enabled(self, value):
        """ Set ssl_enabled value.

            Notes:
                Enable SSL for communication with the LDAP server

                
                This attribute is named `SSLEnabled` in VSD API.
                
        """
        self._ssl_enabled = value

    
    @property
    def password(self):
        """ Get password value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. Password that will be used to verify the integrity of groups and users in LDAP server for the enterprise.

                
        """
        return self._password

    @password.setter
    def password(self, value):
        """ Set password value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. Password that will be used to verify the integrity of groups and users in LDAP server for the enterprise.

                
        """
        self._password = value

    
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
    def accept_all_certificates(self):
        """ Get accept_all_certificates value.

            Notes:
                Accept all certificates from the LDAP server

                
                This attribute is named `acceptAllCertificates` in VSD API.
                
        """
        return self._accept_all_certificates

    @accept_all_certificates.setter
    def accept_all_certificates(self, value):
        """ Set accept_all_certificates value.

            Notes:
                Accept all certificates from the LDAP server

                
                This attribute is named `acceptAllCertificates` in VSD API.
                
        """
        self._accept_all_certificates = value

    
    @property
    def certificate(self):
        """ Get certificate value.

            Notes:
                The certificate to authenticate with the LDAP server

                
        """
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        """ Set certificate value.

            Notes:
                The certificate to authenticate with the LDAP server

                
        """
        self._certificate = value

    
    @property
    def server(self):
        """ Get server value.

            Notes:
                The LDAP server IP or FQDN

                
        """
        return self._server

    @server.setter
    def server(self, value):
        """ Set server value.

            Notes:
                The LDAP server IP or FQDN

                
        """
        self._server = value

    
    @property
    def enabled(self):
        """ Get enabled value.

            Notes:
                To enable LDAP authentication for an enterprise, set this attribute to true. If enabled is set to false, authorizationEnabled attribute is ignored and LDAP is not used for authentication as well as authorization. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

                
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """ Set enabled value.

            Notes:
                To enable LDAP authentication for an enterprise, set this attribute to true. If enabled is set to false, authorizationEnabled attribute is ignored and LDAP is not used for authentication as well as authorization. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

                
        """
        self._enabled = value

    
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
    def port(self):
        """ Get port value.

            Notes:
                Port to be used for the LDAP server

                
        """
        return self._port

    @port.setter
    def port(self, value):
        """ Set port value.

            Notes:
                Port to be used for the LDAP server

                
        """
        self._port = value

    
    @property
    def group_dn(self):
        """ Get group_dn value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the group DN will be used to get the list of VSD specific groups in LDAP server for the enterprise. For example, OU=VSDGroups,DC=company,DC=com

                
                This attribute is named `groupDN` in VSD API.
                
        """
        return self._group_dn

    @group_dn.setter
    def group_dn(self, value):
        """ Set group_dn value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the group DN will be used to get the list of VSD specific groups in LDAP server for the enterprise. For example, OU=VSDGroups,DC=company,DC=com

                
                This attribute is named `groupDN` in VSD API.
                
        """
        self._group_dn = value

    
    @property
    def user_dn_template(self):
        """ Get user_dn_template value.

            Notes:
                The DN template to be used for authentication. The template needs to have a string _USERID_ in it. This will be replaced by  the userId of the user who makes the REST API call. For example, template UID=_USERID_,OU=company,DC=com will converted to  UID=admin,OU=company,DC=com and this will be used as DN for LDAP authentication.

                
                This attribute is named `userDNTemplate` in VSD API.
                
        """
        return self._user_dn_template

    @user_dn_template.setter
    def user_dn_template(self, value):
        """ Set user_dn_template value.

            Notes:
                The DN template to be used for authentication. The template needs to have a string _USERID_ in it. This will be replaced by  the userId of the user who makes the REST API call. For example, template UID=_USERID_,OU=company,DC=com will converted to  UID=admin,OU=company,DC=com and this will be used as DN for LDAP authentication.

                
                This attribute is named `userDNTemplate` in VSD API.
                
        """
        self._user_dn_template = value

    
    @property
    def authorization_enabled(self):
        """ Get authorization_enabled value.

            Notes:
                To enable LDAP authorization for an enterprise, both authorizationEnabled and enabled attributes must be set to true. If enabled attribute is not set, this attribute is ignored. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication. enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

                
                This attribute is named `authorizationEnabled` in VSD API.
                
        """
        return self._authorization_enabled

    @authorization_enabled.setter
    def authorization_enabled(self, value):
        """ Set authorization_enabled value.

            Notes:
                To enable LDAP authorization for an enterprise, both authorizationEnabled and enabled attributes must be set to true. If enabled attribute is not set, this attribute is ignored. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication. enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

                
                This attribute is named `authorizationEnabled` in VSD API.
                
        """
        self._authorization_enabled = value

    
    @property
    def authorizing_user_dn(self):
        """ Get authorizing_user_dn value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the user DN that will be used to verify the integrity of groups and users in LDAP server for the enterprise. For example, CN=groupAdmin,OU=VSD_USERS,OU=Personal,OU=Domain Users,DC=company,DC=com

                
                This attribute is named `authorizingUserDN` in VSD API.
                
        """
        return self._authorizing_user_dn

    @authorizing_user_dn.setter
    def authorizing_user_dn(self, value):
        """ Set authorizing_user_dn value.

            Notes:
                This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the user DN that will be used to verify the integrity of groups and users in LDAP server for the enterprise. For example, CN=groupAdmin,OU=VSD_USERS,OU=Personal,OU=Domain Users,DC=company,DC=com

                
                This attribute is named `authorizingUserDN` in VSD API.
                
        """
        self._authorizing_user_dn = value

    
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

    

    