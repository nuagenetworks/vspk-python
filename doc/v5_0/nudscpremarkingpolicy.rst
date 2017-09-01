.. _nudscpremarkingpolicy:

nudscpremarkingpolicy
===========================================

.. class:: nudscpremarkingpolicy.NUDSCPRemarkingPolicy(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of a single Forwarding class to DSCP mapping that is part of a DSCP Remarking table used in Egress QoS policies.


Attributes
----------


- ``dscp``: DSCP value range from enumeration of 65 values: *, 0, 1, ..., 63

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``forwarding_class``: Class of service to be used.Service classes in order of priority are A, B, C, D, E, F, G, and H.

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


- :ref:`nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable<nudscpremarkingpolicytable>`

