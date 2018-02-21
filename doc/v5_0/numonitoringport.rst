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

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``uplink``: Flag to indicate that is an uplink or downlink port.

- ``state``: The current state of the port.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsc.NUVSC<nuvsc>`

