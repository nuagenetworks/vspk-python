.. _nuroleentry:

nuroleentry
===========================================

.. class:: nuroleentry.NURoleentry(bambou.nurest_object.NUMetaRESTObject,):

Entry for each end point with assoicatiated permissions.


Attributes
----------


- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``end_point_rest_name`` (**Mandatory**): Rest name of the end point

- ``end_point_type``: Managed Object Type or end point

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``role_access_type_list`` (**Mandatory**): List of Access like READ, READ_CHILDREN, CREATE, MODIFY, DELETE, CUD_CHILDREN, NO_ACCESS, NO_ACCESS_CHILDREN, USE

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nurole.NURole<nurole>`

