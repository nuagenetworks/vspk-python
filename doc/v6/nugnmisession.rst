.. _nugnmisession:

nugnmisession
===========================================

.. class:: nugnmisession.NUGNMISession(bambou.nurest_object.NUMetaRESTObject,):

Represents GNMI session between gateway and Config Manager, This can only be created by netconfmgr user


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_model``: The model string of the gateway to which this session connected from Config Manager

- ``gateway_vendor``: Vendor of the gateway to which this session connected from Config Manager

- ``gateway_version``: Boot image version of gateway to which this session connected from Config Manager

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``associated_gateway_id``: UUID of the gateway associated to this GNMI session.

- ``associated_gateway_name``: Name of the gateway associated to this GNMI session.

- ``status``: The status of the GNMI session to a gateway.

- ``subscription_error``: Last subscription error reported

- ``subscription_failure_reason``: Detailed subscription error message

- ``subscription_failure_retry_count``: Number of times subscription has been attempted since first failure

- ``subscription_state``: Status of gnmi subscriptions to device from Netconf Manager

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

