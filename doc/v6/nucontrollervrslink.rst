.. _nucontrollervrslink:

nucontrollervrslink
===========================================

.. class:: nucontrollervrslink.NUControllerVRSLink(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for VRS connected to VSC or HSC


Attributes
----------


- ``vrsid``: ID of associated VRS

- ``vrsissu_failure_reason``: ISSU (In-Service Software Upgrade) failure reason of the associated VRS.

- ``vrsissu_state``: ISSU (In-Service Software Upgrade) state of the associated VRS.

- ``vrs_last_issu_state``: Last ISSU (In-Service Software Upgrade) state of the associated VRS.

- ``vrs_personality``: Personality of associated VRS.

- ``vrs_system_id``: System ID of associated VRS

- ``vsc_config_state``: Indicates the configured state of the VSC.

- ``vsc_current_state``: Indicates the current state of the VSC, which may or maybe not be same as the configured state.

- ``jsonrpc_connection_state``: The current JSON RPC connection status.

- ``name``: Name of the Controller-VRS link

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``peer``: The redundant peer id for the current VRS.

- ``cluster_node_role``: Indicate that the controller associated is primary, secondary or unknown.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``role``: Flag to indicate the VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways.

- ``connections``: List of Connections for Controller VRS Link

- ``controller_id``: ID of associated Controller

- ``controller_type``: Type of associated Controller

- ``creation_date``: Time stamp when this object was created.

- ``status``: Computed status of the entity.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``dynamic``: Flag to indicate it is dynamically configured or not.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvrs.NUVRS<nuvrs>`                                                                                                                                        ``vrss`` 
:ref:`nuhsc.NUHSC<nuhsc>`                                                                                                                                        ``hscs`` 
:ref:`nuvsc.NUVSC<nuvsc>`                                                                                                                                        ``vscs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuvrs.NUVRS<nuvrs>`

- :ref:`nuhsc.NUHSC<nuhsc>`

- :ref:`nuvsc.NUVSC<nuvsc>`

