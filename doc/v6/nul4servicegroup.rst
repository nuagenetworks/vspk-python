.. _nul4servicegroup:

nul4servicegroup
===========================================

.. class:: nul4servicegroup.NUL4ServiceGroup(bambou.nurest_object.NUMetaRESTObject,):

Service Group is a set of Services that can be used in ACLs.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Service group

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: Describes the Service Group

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

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

- :ref:`nume.NUMe<nume>`

- :ref:`nul4service.NUL4Service<nul4service>`

