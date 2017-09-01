.. _nul4servicegroup:

nul4servicegroup
===========================================

.. class:: nul4servicegroup.NUL4ServiceGroup(bambou.nurest_object.NUMetaRESTObject,):

L4 Service Group is a set of L4 Services that can be used in ACLs.


Attributes
----------


- ``name`` (**Mandatory**): Name of the L4 Services group

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Describes the L4 Service Group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul4service.NUL4Service<nul4service>`                                                                                                                      ``l4_services`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

