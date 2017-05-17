.. _nupublicnetworkmacro:

nupublicnetworkmacro
===========================================

.. class:: nupublicnetworkmacro.NUPublicNetworkMacro(bambou.nurest_object.NUMetaRESTObject,):

Similar to the enterprise macros, the public network macro allows an administrator of an enterprise to define range of subnets that can be used by users in the ACL definition


Attributes
----------


- ``ip_type``: IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

- ``name`` (**Mandatory**): Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``address`` (**Mandatory**): IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

- ``netmask`` (**Mandatory**): Netmask of the subnet defined

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================


