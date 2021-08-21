.. _nudscpremarkingpolicytable:

nudscpremarkingpolicytable
===========================================

.. class:: nudscpremarkingpolicytable.NUDSCPRemarkingPolicyTable(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of a table that holds multiple Forwarding class to  DSCP  mappings. Used in Egress QoS policies.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the fc- dscp remarking table.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the fc-dscp remarking table.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nudscpremarkingpolicy.NUDSCPRemarkingPolicy<nudscpremarkingpolicy>`                                                                                        ``dscp_remarking_policies`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

