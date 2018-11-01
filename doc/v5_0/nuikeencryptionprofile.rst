.. _nuikeencryptionprofile:

nuikeencryptionprofile
===========================================

.. class:: nuikeencryptionprofile.NUIKEEncryptionprofile(bambou.nurest_object.NUMetaRESTObject,):

Represents an IKE Profile


Attributes
----------


- ``dpd_interval``: ISAKMP Keep Alive Interval.

- ``dpd_mode``: DPD Mode.

- ``dpd_timeout``: DPD Timeout.

- ``ipsec_authentication_algorithm``: IPsec Authentication Algorithm.

- ``ipsec_dont_fragment``: IPsec Don't Fragment

- ``ipsec_enable_pfs``: IPsec Enable PFS

- ``ipsec_encryption_algorithm``: IPsec Encryption Algorithm.

- ``ipsec_pre_fragment``: IPsec PreFragment

- ``ipsec_sa_lifetime``: IPsec SA Lifetime in Seconds.

- ``ipsec_sa_replay_window_size``: IPsec Replay Window Size in Packets.

- ``ipsec_sa_replay_window_size_value``: IPsec Replay Window Size in Packets.

- ``isakmp_authentication_mode``: ISAKMP Authentication Algorithm.

- ``isakmp_diffie_helman_group_identifier``: ISAKMP Diffie-Helman Group Identifier.

- ``isakmp_encryption_algorithm``: ISAKMP Encryption Algorithm.

- ``isakmp_encryption_key_lifetime``: ISAKMP Encryption Key Lifetime in Seconds

- ``isakmp_hash_algorithm``: ISAKMP Hash Algorithm.

- ``name``: Name of the Encryption Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``sequence``: None

- ``description``: A description of the Profile instance created.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_enterprise_id``: The ID of the associated Enterprise

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

