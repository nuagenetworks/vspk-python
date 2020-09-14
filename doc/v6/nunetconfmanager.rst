.. _nunetconfmanager:

nunetconfmanager
===========================================

.. class:: nunetconfmanager.NUNetconfManager(bambou.nurest_object.NUMetaRESTObject,):

Identifies Netconf Manager communicating with VSD, This can only be created by netconfmgr user


Attributes
----------


- ``name``: A unique name of the Netconf Manager entity.

- ``last_updated_by``: ID of the user who last updated the object.

- ``release``: Netconf Manager RPM release version

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``assoc_entity_type``: Type of parent entity

- ``status``: VSD connection status with this Netconf Manager

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetconfsession.NUNetconfSession<nunetconfsession>`                                                                                                       ``netconf_sessions`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvsp.NUVSP<nuvsp>`

