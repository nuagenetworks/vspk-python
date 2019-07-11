.. _nubootstrapactivation:

nubootstrapactivation
===========================================

.. class:: nubootstrapactivation.NUBootstrapActivation(bambou.nurest_object.NUMetaRESTObject,):

NSG Gateway initiated Bootstrap Activation


Attributes
----------


- ``cacert``: The CA Certificate Chain

- ``hash``: The authentication hash of this request

- ``last_updated_by``: ID of the user who last updated the object.

- ``action``: The bootstrap action to perform.

- ``seed``: The random seed for this request

- ``cert``: The signed Certificate

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``config_url``: The configuration URL

- ``tpm_owner_password``: TPM owner passphrase

- ``tpm_state``: Gateway TPM Status reported by the device when generating CSR.

- ``srk_password``: TPM SRK passphrase

- ``vsd_time``: VSD Server time when an NSG is initiating a Bootstrapping request

- ``csr``: The CSR of the request

- ``associated_entity_type``: Object type of the associated entity.

- ``status``: The agent status for the request

- ``auto_bootstrap``: Indicates whether auto bootstrap is being used to bootstrap this NSG

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


- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

