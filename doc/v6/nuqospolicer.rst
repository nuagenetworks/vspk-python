.. _nuqospolicer:

nuqospolicer
===========================================

.. class:: nuqospolicer.NUQosPolicer(bambou.nurest_object.NUMetaRESTObject,):

QoS Policer ensures that traffic adheres to the stipulated QoS defined in your network. Contains Rate and Burst configurations and can be associated to VLANs.


Attributes
----------


- ``name`` (**Mandatory**): Name of the QoS Policer

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``rate``: Rate: Bandwidth that is allowed in Mb/s; only whole values supported.

- ``description``: Description of the QoS Policer

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``burst``: Burst Size: The maximum burst size associated with the QoS Policer in kilo-bits; only whole values are supported.

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

