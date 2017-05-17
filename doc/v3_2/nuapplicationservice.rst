.. _nuapplicationservice:

nuapplicationservice
===========================================

.. class:: nuapplicationservice.NUApplicationService(bambou.nurest_object.NUMetaRESTObject,):

Represents a networking communication service.


Attributes
----------


- ``dscp``: DSCP match condition to be set in the rule. It is either * or from 0-63. Required for etherType 0x0800

- ``name`` (**Mandatory**): Name of the application service.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the application service.

- ``destination_port`` (**Mandatory**): The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range.

- ``direction`` (**Mandatory**): Direction of the service. Default is UNIDIRECTIONAL.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``source_port`` (**Mandatory**): Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range.

- ``protocol`` (**Mandatory**): Protocol that must be matched.  Needs to be 6 (TCP) or 17 (UDP)

- ``ether_type`` (**Mandatory**): Ether type of the packet to be matched. Ether type can be * or a valid hexadecimal value

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

