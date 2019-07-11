.. _nuducgroupbinding:

nuducgroupbinding
===========================================

.. class:: nuducgroupbinding.NUDUCGroupBinding(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``one_way_delay``: SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority``: The priority for NSG Group to UBR Group relationship.

- ``associated_duc_group_id``: Identification of the UBR Group associated to this group binding instance.

- ``associated_ubr_group_function``: NSG Function supported by the associated UBR group.

- ``associated_ubr_group_name``: Name of the associated UBR Group.

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


- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

