.. _nuavatar:

nuavatar
===========================================

.. class:: nuavatar.NUAvatar(bambou.nurest_object.NUMetaRESTObject,):

Avatar


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: The image type




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuuser.NUUser<nuuser>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

