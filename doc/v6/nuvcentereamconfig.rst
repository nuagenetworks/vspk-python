.. _nuvcentereamconfig:

nuvcentereamconfig
===========================================

.. class:: nuvcentereamconfig.NUVCenterEAMConfig(bambou.nurest_object.NUMetaRESTObject,):

The EAM solution configuration.


Attributes
----------


- ``eam_server_ip`` (**Mandatory**): The EAM server IP

- ``eam_server_port_number`` (**Mandatory**): The EAM server port number

- ``eam_server_port_type`` (**Mandatory**): The EAM server port Type

- ``last_updated_by``: ID of the user who last updated the object.

- ``vib_url``: The url for the optional vib

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``ovf_url`` (**Mandatory**): The url for the ovf

- ``extension_key``: Key of the extension that the solution registers

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

