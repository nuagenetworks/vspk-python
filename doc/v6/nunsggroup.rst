.. _nunsggroup:

nunsggroup
===========================================

.. class:: nunsggroup.NUNSGGroup(bambou.nurest_object.NUMetaRESTObject,):

A logical group of NSG and NSG-BR instances that can be used to assign NSG-UBRs to all NSGs in the group, to provide connectivity to NSGs in disjoint underlays.


Attributes
----------


- ``name``: Name of the NSG Group

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: Description of the NSG Group

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``nsg_group_id``: The NSG Group 12 bit identifier.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`                                                                                                    ``duc_group_bindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

