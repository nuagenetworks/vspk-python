.. _nuenterprisesecurity:

nuenterprisesecurity
===========================================

.. class:: nuenterprisesecurity.NUEnterpriseSecurity(bambou.nurest_object.NUMetaRESTObject,):

This object represents the enterprise security


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``gateway_security_revision``: change revision number for the gateway security data

- ``revision``: revision number for the enterprise security data

- ``enterprise_id``: The enterprise associated with this object. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisesecureddata.NUEnterpriseSecuredData<nuenterprisesecureddata>`                                                                                  ``enterprise_secured_datas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

