.. _nutestdefinition:

nutestdefinition
===========================================

.. class:: nutestdefinition.NUTestDefinition(bambou.nurest_object.NUMetaRESTObject,):

A Test definition describes a command to run inside a diagnositcs container on an NSGateway. It represents a command with arguments that will be run in the container as part of a Test Suite run


Attributes
----------


- ``name`` (**Mandatory**): A descriptive name for the Test Definition instance.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A concise description of the Test Definition object.

- ``timeout``: Optional timeout value, in seconds, for the test until the system considers it as failed. Default is 60 s.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command`` (**Mandatory**): The Linux command that this test definition will use.

- ``arguments``: The arguments that will be appended to the test command field.

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

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

