.. _nucosremarkingpolicy:

nucosremarkingpolicy
===========================================

.. class:: nucosremarkingpolicy.NUCOSRemarkingPolicy(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of a single Forwarding class to CoS mapping that is part of a COS Remarking Policy Table used in QoS policies.


Attributes
----------


- ``dscp`` (**Mandatory**): DSCP value range from enumeration of 8 values: 0, 1, ..., 7

- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``forwarding_class`` (**Mandatory**): Class of service to be used. Service classes in order of priority are A, B, C, D, E, F, G, and H.

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


- :ref:`nucosremarkingpolicytable.NUCOSRemarkingPolicyTable<nucosremarkingpolicytable>`

