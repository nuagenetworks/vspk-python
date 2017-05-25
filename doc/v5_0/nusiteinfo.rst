.. _nusiteinfo:

nusiteinfo
===========================================

.. class:: nusiteinfo.NUSiteInfo(bambou.nurest_object.NUMetaRESTObject,):

Remote Site info.


Attributes
----------


- ``name`` (**Mandatory**): name of the Remote Site.

- ``last_updated_by``: ID of the user who last updated the object.

- ``address`` (**Mandatory**): unique fqdn/address of the remote site

- ``description``: Description of the Remote Site.

- ``site_identifier``: unique identifier of the remote site

- ``xmpp_domain`` (**Mandatory**): unique xmpp domain name of the remote site

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

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

