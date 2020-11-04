.. _nusiteinfo:

nusiteinfo
===========================================

.. class:: nusiteinfo.NUSiteInfo(bambou.nurest_object.NUMetaRESTObject,):

Remote Site info.


Attributes
----------


- ``name`` (**Mandatory**): name of the Remote Site.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address`` (**Mandatory**): unique fqdn/address of the remote site

- ``description``: Description of the Remote Site.

- ``site_identifier``: unique identifier of the remote site

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``xmpp_domain`` (**Mandatory**): unique xmpp domain name of the remote site

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

