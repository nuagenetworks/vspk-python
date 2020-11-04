.. _nunatmapentry:

nunatmapentry
===========================================

.. class:: nunatmapentry.NUNATMapEntry(bambou.nurest_object.NUMetaRESTObject,):

Defines a MAP between the private ip and public ip.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``private_ip`` (**Mandatory**): Private IP address of the interface

- ``private_port``: Private port identification

- ``associated_patnat_pool_id``: Indicates which PATNATPool this entry belongs to

- ``public_ip`` (**Mandatory**): Public IP address of the interface

- ``public_port``: Public port identification

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): The type of address mapping this instance is.




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


- :ref:`nupatnatpool.NUPATNATPool<nupatnatpool>`

