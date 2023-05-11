.. _nudscpremarkingpolicytable:

nudscpremarkingpolicytable
===========================================

.. class:: nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of a table that holds multiple Forwarding class to  DSCP  mappings. Used in Egress QoS policies.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the fc- dscp remarking table.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the fc-dscp remarking table.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`                                                                                        ``dscp_remarking_policies`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

