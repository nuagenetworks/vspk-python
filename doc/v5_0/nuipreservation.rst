.. _nuipreservation:

nuipreservation
===========================================

.. class:: nuipreservation.NUIPReservation(bambou.nurest_object.NUMetaRESTObject,):

You can reserve and allocate IP addresses according to the host MAC address


Attributes
----------


- ``mac`` (**Mandatory**): MAC Address

- ``ip_address`` (**Mandatory**): Static IP Address

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic_allocation_enabled``: Binding is static or dynamic




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


- :ref:`nusubnet.NUSubnet<nusubnet>`

