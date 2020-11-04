.. _numonitoringport:

numonitoringport
===========================================

.. class:: numonitoringport.NUMonitoringPort(bambou.nurest_object.NUMetaRESTObject,):

Encapsulates the port information for system monitoring entity.


Attributes
----------


- ``name``: Name for the port.

- ``last_state_change``: Last port state change timestamp.

- ``access``: Flag to indicate that it is a access port or network port.

- ``description``: Optional port description.

- ``resiliency_state``: None

- ``resilient``: Flag to indicate if an ACCESS port is resilient or not.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``dpdk_enabled``: Flag to indicate if an ACCESS port is DPDK Enabled or not.

- ``uplink``: Flag to indicate that is an uplink or downlink port.

- ``state``: The current state of the port.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsc.NUVSC<nuvsc>`

