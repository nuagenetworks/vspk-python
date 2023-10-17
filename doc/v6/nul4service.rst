.. _nul4service:

nul4service
===========================================

.. class:: nul4service.NUL4Service(bambou.nurest_object.NUMetaRESTObject,):

Service is a port range and protocol combination that can be used in ACLs


Attributes
----------


- ``icmp_code``: The ICMP Code when protocol selected is ICMP.

- ``icmp_type``: The ICMP Type when protocol selected is ICMP.

- ``name`` (**Mandatory**): Name of the service

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``default_service``: Flag to identify default service

- ``description``: Description of the service

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``ports``: The port ranges for the l4 service. Must be matched if protocol is UDP or TCP. Value can be either * or single port number (1, 2 etc.) or a port range (1-10)

- ``creation_date``: Time stamp when this object was created.

- ``protocol``: Protocol number that must be matched

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nul4servicegroup.NUL4ServiceGroup<nul4servicegroup>`                                                                                                       ``l4_service_groups`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nul4servicegroup.NUL4ServiceGroup<nul4servicegroup>`

- :ref:`nume.NUMe<nume>`

