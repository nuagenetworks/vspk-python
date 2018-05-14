.. _nucsnatpool:

nucsnatpool
===========================================

.. class:: nucsnatpool.NUCSNATPool(bambou.nurest_object.NUMetaRESTObject,):

Customer Alias IP range to be used in provider domain. This pool is used to map customer private IPs from customer domain to customer public IPs in provider domain.


Attributes
----------


- ``name`` (**Mandatory**): The Customer to Provider NAT Pool

- ``end_address`` (**Mandatory**): The last IP address in the range.

- ``start_address`` (**Mandatory**): The first IP in the range.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuctranslationmap.NUCTranslationMap<nuctranslationmap>`                                                                                                    ``c_translation_maps`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

