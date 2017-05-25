.. _nuducgroupbinding:

nuducgroupbinding
===========================================

.. class:: nuducgroupbinding.NUDUCGroupBinding(bambou.nurest_object.NUMetaRESTObject,):

None


Attributes
----------


- ``one_way_delay``: SLA delay value in milliseconds that is tolerated between NSG instances and NSG-UBR (DUC) instances being bound through this binding instance.  If delay is to be ignored, then the value of -1 is to be entered.  Value 0 is not permitted.

- ``priority``: The priority for NSG Group to UBR Group relationship.

- ``associated_duc_group_id``: Identification of the UBR Group associated to this group binding instance.






Parents
--------


- :ref:`nunsggroup.NUNSGGroup<nunsggroup>`

