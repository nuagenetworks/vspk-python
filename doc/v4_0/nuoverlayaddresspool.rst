.. _nuoverlayaddresspool:

nuoverlayaddresspool
===========================================

.. class:: nuoverlayaddresspool.NUOverlayAddressPool(bambou.nurest_object.NUMetaRESTObject,):

The address pool the public IP of the PAT/NAT entries belong too.


Attributes
----------


- ``name``: Name for the PAT NAT pool

- ``description``: addresspool description

- ``end_address_range``: The end address for the pool range.

- ``associated_domain_id``: The ID of the associated l3-domain.

- ``start_address_range``: Start address for the pool range




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuoverlaypatnatentry.NUOverlayPATNATEntry<nuoverlaypatnatentry>`                                                                                           ``overlay_patnat_entries`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

