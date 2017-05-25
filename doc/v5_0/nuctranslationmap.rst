.. _nuctranslationmap:

nuctranslationmap
===========================================

.. class:: nuctranslationmap.NUCTranslationMap(bambou.nurest_object.NUMetaRESTObject,):

1:1 mapping of customer private IPs in customer domain to customer alias (public) IPs in provider domain and N:1 mapping to customer alias SPAT IP in the provider domain.


Attributes
----------


- ``mapping_type`` (**Mandatory**): NAT for 1:1 mapping or PAT for *:1 mappings.

- ``customer_alias_ip`` (**Mandatory**): Customer public IP in the provider domain.

- ``customer_ip`` (**Mandatory**): Customer private IP in the customer domain.






Parents
--------


- :ref:`nucsnatpool.NUCSNATPool<nucsnatpool>`

