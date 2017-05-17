.. _nuvlantemplate:

nuvlantemplate
===========================================

.. class:: nuvlantemplate.NUVLANTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents VLAN Template under a Port Template object.


Attributes
----------


- ``value``: value of VLAN

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Port

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this Vlan.

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


- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

