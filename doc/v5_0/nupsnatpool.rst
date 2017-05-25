.. _nupsnatpool:

nupsnatpool
===========================================

.. class:: nupsnatpool.NUPSNATPool(bambou.nurest_object.NUMetaRESTObject,):

Provider alias IP range to map provider private IPs from provider domain to provider public IPs in the customer domain.


Attributes
----------


- ``end_address`` (**Mandatory**): The last IP address in the range.

- ``start_address`` (**Mandatory**): The first IP address in the range.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupspatmap.NUPSPATMap<nupspatmap>`                                                                                                                         ``pspat_maps`` 
:ref:`nuptranslationmap.NUPTranslationMap<nuptranslationmap>`                                                                                                    ``p_translation_maps`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

