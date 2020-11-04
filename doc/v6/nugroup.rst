.. _nugroup:

nugroup
===========================================

.. class:: nugroup.NUGroup(bambou.nurest_object.NUMetaRESTObject,):

Identifies a group within an enterprise


Attributes
----------


- ``ldap_group_dn``: The LDAP distinguished name (DN) for the group.

- ``name`` (**Mandatory**): A unique name of the group

- ``management_mode``: Management mode of the user object - allows for override of external authorization and syncup

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``account_restrictions``: Determines whether group is disabled or not.

- ``description``: Description of the group

- ``restriction_date``: When the group was disabled.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``role``: The role associated with this group.

- ``creation_date``: Time stamp when this object was created.

- ``private``: A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuuser.NUUser<nuuser>`                                                                                                                                     ``users`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nuuser.NUUser<nuuser>`

