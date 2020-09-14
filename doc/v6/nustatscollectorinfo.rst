.. _nustatscollectorinfo:

nustatscollectorinfo
===========================================

.. class:: nustatscollectorinfo.NUStatsCollectorInfo(bambou.nurest_object.NUMetaRESTObject,):

Identifies the IP address of the stats collector entity that must be used.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``address_type``: Type for stats collector address Possible values are ip, fqdn, .

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port``: Port(s) of the stats collector process

- ``ip_address``: IP address(es) of the stats collector process

- ``proto_buf_port``: Protobuf Port(s) of the stats collector process

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

