.. _nunetconfsession:

nunetconfsession
===========================================

.. class:: nunetconfsession.NUNetconfSession(bambou.nurest_object.NUMetaRESTObject,):

Represents session between gateway and Netconf Manager, This can only be created by netconfmgr user


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_gateway_id``: UUID of the gateway associated to this Netconf session.

- ``associated_gateway_name``: Name of the gateway associated to this Netconf session.

- ``status``: The status of the NetConf session to a gateway.

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


- :ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`

