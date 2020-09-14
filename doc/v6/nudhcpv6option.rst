.. _nudhcpv6option:

nudhcpv6option
===========================================

.. class:: nudhcpv6option.NUDHCPv6Option(bambou.nurest_object.NUMetaRESTObject,):

Allows the definition of one or more DHCPv6 options that will be provided to all VMs that are associated with a given domain. DHCPv6 options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application.


Attributes
----------


- ``value``: DHCPv6 option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

- ``last_updated_by``: ID of the user who last updated the object.

- ``actual_type``: This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

- ``actual_values``: This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

- ``length``: DHCPv6 option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: DHCPv6 option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nucontainerinterface.NUContainerInterface<nucontainerinterface>`

- :ref:`nuzone.NUZone<nuzone>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nuvport.NUVPort<nuvport>`

- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nuvminterface.NUVMInterface<nuvminterface>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuhostinterface.NUHostInterface<nuhostinterface>`

- :ref:`nubridgeinterface.NUBridgeInterface<nubridgeinterface>`

