.. _nunetconfsession:

nunetconfsession
===========================================

.. class:: nunetconfsession.NUNetconfSession(bambou.nurest_object.NUMetaRESTObject,):

Represents session between gateway and Netconf Manager, This can only be created by netconfmgr user


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_model``: The model string of the gateway to which this session connected from Netconf Manager

- ``gateway_vendor``: Vendor of the gateway to which this session connected from Netconf Manager

- ``gateway_version``: Boot image version of gateway to which this session connected from Netconf Manager

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_gateway_id``: UUID of the gateway associated to this Netconf session.

- ``associated_gateway_name``: Name of the gateway associated to this Netconf session.

- ``status``: The status of the NetConf session to a gateway.

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


- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

