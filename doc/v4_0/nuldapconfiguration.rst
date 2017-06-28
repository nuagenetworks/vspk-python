.. _nuldapconfiguration:

nuldapconfiguration
===========================================

.. class:: nuldapconfiguration.NULDAPConfiguration(bambou.nurest_object.NUMetaRESTObject,):

Configuration of LDAP parameters associated with an enterprise. This will enable authentication through an external LDAP server for this enterprise.


Attributes
----------


- ``ssl_enabled``: Enable SSL for communication with the LDAP server

- ``password``: This attribute is a mandatory field for LDAP authorization. Password that will be used to verify the integrity of groups and users in LDAP server for the enterprise.

- ``last_updated_by``: ID of the user who last updated the object.

- ``accept_all_certificates``: Accept all certificates from the LDAP server

- ``certificate``: The certificate to authenticate with the LDAP server

- ``server`` (**Mandatory**): The LDAP server IP or FQDN

- ``enabled``: To enable LDAP authentication for an enterprise, set this attribute to true. If enabled is set to false, authorizationEnabled attribute is ignored and LDAP is not used for authentication as well as authorization. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port`` (**Mandatory**): Port to be used for the LDAP server

- ``group_dn`` (**Mandatory**): This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the group DN will be used to get the list of VSD specific groups in LDAP server for the enterprise. For example, OU=VSDGroups,DC=company,DC=com

- ``group_name_prefix``: If this is specified, Prefix+Pre-definedGroupName will be used to look for users.

- ``group_name_suffix``: If this is specified, Pre-definedGroupName+Suffix will be used to look for users.

- ``user_dn_template``: The DN template to be used for authentication. The template needs to have a string _USERID_ in it. This will be replaced by  the userId of the user who makes the REST API call. For example, template UID=_USERID_,OU=company,DC=com will converted to  UID=admin,OU=company,DC=com and this will be used as DN for LDAP authentication.

- ``authorization_enabled``: To enable LDAP authorization for an enterprise, both authorizationEnabled and enabled attributes must be set to true. If enabled attribute is not set, this attribute is ignored. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication. enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.

- ``authorizing_user_dn`` (**Mandatory**): This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the user DN that will be used to verify the integrity of groups and users in LDAP server for the enterprise. For example, CN=groupAdmin,OU=VSD_USERS,OU=Personal,OU=Domain Users,DC=company,DC=com

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

