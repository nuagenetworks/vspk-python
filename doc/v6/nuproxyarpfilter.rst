.. _nuproxyarpfilter:

nuproxyarpfilter
===========================================

.. class:: nuproxyarpfilter.NUProxyARPFilter(bambou.nurest_object.NUMetaRESTObject,):

Proxy ARP filters represent black-list of address ranges for NSG acting as ARP proxy


Attributes
----------


- ``ip_type``: Describes the Address family

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``max_address`` (**Mandatory**): Highest address in the address range

- ``min_address`` (**Mandatory**): Lowest address in the address range

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nusubnet.NUSubnet<nusubnet>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

