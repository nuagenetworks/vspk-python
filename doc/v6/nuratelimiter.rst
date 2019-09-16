.. _nuratelimiter:

nuratelimiter
===========================================

.. class:: nuratelimiter.NURateLimiter(bambou.nurest_object.NUMetaRESTObject,):

Set of traffic management parameters describing a desired traffic profile. Rate-limiters are used by QoS policies to enforce per Class of Server rate-conformance.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the Rate Limiter object

- ``last_updated_by``: ID of the user who last updated the object.

- ``peak_burst_size`` (**Mandatory**): Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

- ``peak_information_rate`` (**Mandatory**): Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

- ``description``: A description of the Rate Limiter object

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``committed_information_rate`` (**Mandatory**): Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

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


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

