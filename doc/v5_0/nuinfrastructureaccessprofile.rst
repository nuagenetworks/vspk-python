.. _nuinfrastructureaccessprofile:

nuinfrastructureaccessprofile
===========================================

.. class:: nuinfrastructureaccessprofile.NUInfrastructureAccessProfile(bambou.nurest_object.NUMetaRESTObject,):

Represents an Infrastructure Access Profile


Attributes
----------


- ``ssh_auth_mode``: Indicates the authentication method used during an SSH session.

- ``name`` (**Mandatory**): Name of the Infrastructure Access Profile

- ``password`` (**Mandatory**): Password of the default user associated to the access profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Profile instance created.

- ``enterprise_id``: Enterprise/Organisation associated with this Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_ip_filter``: Indicates if source based IP filtering is enabled for this access profile.

- ``user_name``: Default user name which is associated to the access profile.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuconnectionendpoint.NUConnectionendpoint<nuconnectionendpoint>`                                                                                           ``connectionendpoints`` 
:ref:`nusshkey.NUSSHKey<nusshkey>`                                                                                                                               ``ssh_keys`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

