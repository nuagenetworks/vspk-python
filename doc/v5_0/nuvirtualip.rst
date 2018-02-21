.. _nuvirtualip:

nuvirtualip
===========================================

.. class:: nuvirtualip.NUVirtualIP(bambou.nurest_object.NUMetaRESTObject,):

Virtual IP address.


Attributes
----------


- ``mac``: The MAC address of the virtual port

- ``ip_type``: Specify if the virtualIP attribute value is in IPv4 or IPv6 format

- ``last_updated_by``: ID of the user who last updated the object.

- ``virtual_ip`` (**Mandatory**): Virtual IP address

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_floating_ip_id``: Id of Floating IP address associated to this virtual ip

- ``subnet_id``: Id of subnet to which this ip address belongs

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


- :ref:`nuredirectiontarget.NURedirectionTarget<nuredirectiontarget>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

