.. _nuwebdomainname:

nuwebdomainname
===========================================

.. class:: nuwebdomainname.NUWebDomainName(bambou.nurest_object.NUMetaRESTObject,):

A domain name is an identification string that defines a realm of administrative autonomy, authority or control within the Internet


Attributes
----------


- ``name`` (**Mandatory**): FQDN or FQDN with wildcard prefix

- ``last_updated_by``: ID of the user who last updated the object.

- ``web_category_identifier``: The unique identifier of a web category to be used by NSG

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuwebcategory.NUWebCategory<nuwebcategory>`                                                                                                                ``web_categories`` 
:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuwebcategory.NUWebCategory<nuwebcategory>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

