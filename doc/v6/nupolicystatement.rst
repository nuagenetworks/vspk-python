.. _nupolicystatement:

nupolicystatement
===========================================

.. class:: nupolicystatement.NUPolicyStatement(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``name``: name of the policy statement

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the policy statement

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicyentry.NUPolicyEntry<nupolicyentry>`                                                                                                                ``policy_entries`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

