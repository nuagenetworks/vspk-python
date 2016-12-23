.. _nutier:

nutier
===========================================

.. class:: nutier.NUTier(bambou.nurest_object.NUMetaRESTObject,):

Tier represents a portion of an Application.


Attributes
----------


- ``name`` (**Mandatory**): Name of the application tier.

- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway``: The IP address of the gateway for this tier.

- ``address``: IP address of the tier defined.

- ``description``: Description of the application tier.

- ``metadata``: Metadata field to store tier related data.

- ``netmask``: Netmask for the tier.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_application_id``: The associated network macro ID.

- ``associated_floating_ip_pool_id``: The associated floating IP Pool ID.

- ``associated_network_macro_id``: The associated network macro ID.

- ``associated_network_object_id``: The associated network object id.

- ``associated_network_object_type``: The associated network object type. Refer to API section for supported types.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type`` (**Mandatory**): Type of the application tier.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nutca.NUTCA<nutca>`                                                                                                                                        ``tcas`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nuvport.NUVPort<nuvport>`                                                                                                                                  ``vports`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================


