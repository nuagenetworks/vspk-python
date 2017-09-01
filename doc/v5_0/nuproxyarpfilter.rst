.. _nuproxyarpfilter:

nuproxyarpfilter
===========================================

.. class:: nuproxyarpfilter.NUProxyARPFilter(bambou.nurest_object.NUMetaRESTObject,):

Black list of ranges for which NSG will act as ARP Proxy


Attributes
----------


- ``ip_type``: Describes the Address family

- ``last_updated_by``: ID of the user who last updated the object.

- ``max_address`` (**Mandatory**): Highest address in the address range

- ``min_address`` (**Mandatory**): Lowest address in the address range

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nusubnet.NUSubnet<nusubnet>`

