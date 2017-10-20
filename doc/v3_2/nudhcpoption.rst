.. _nudhcpoption:

nudhcpoption
===========================================

.. class:: nudhcpoption.NUDHCPOption(bambou.nurest_object.NUMetaRESTObject,):

Allows the definition of one or more DHCP options that will be provided to all VMs that are associated with a given domain. DHCP options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application.


Attributes
----------


- ``value`` (**Mandatory**): DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

- ``last_updated_by``: ID of the user who last updated the object.

- ``actual_type``: This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

- ``actual_values``: This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

- ``length`` (**Mandatory**): DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')




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


- :ref:`nusharednetworkresource.NUSharedNetworkResource<nusharednetworkresource>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

