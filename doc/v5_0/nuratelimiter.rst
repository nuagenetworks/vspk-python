.. _nuratelimiter:

nuratelimiter
===========================================

.. class:: nuratelimiter.NURateLimiter(bambou.nurest_object.NUMetaRESTObject,):

Rate Limiter object that contains peak, burst and cir. It can be associated with Egress QOS policy objects.


Attributes
----------


- ``name`` (**Mandatory**): A unique name of the Rate Limiter object

- ``last_updated_by``: ID of the user who last updated the object.

- ``peak_burst_size``: Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

- ``peak_information_rate``: Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

- ``description``: A description of the Rate Limiter object

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``committed_information_rate``: Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

