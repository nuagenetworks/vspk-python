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

- ``associated_vsc_profile_id``: The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

- ``duc_vlan``: When set to true, this specifies that this VLAN template instance serves as an underlay connection endpoint on an NSG-UBR gateway.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuuplinkconnection.NUUplinkConnection<nuuplinkconnection>`                                                                                                 ``uplink_connections`` 
:ref:`nubrconnection.NUBRConnection<nubrconnection>`                                                                                                             ``br_connections`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuporttemplate.NUPortTemplate<nuporttemplate>`

- :ref:`nunsporttemplate.NUNSPortTemplate<nunsporttemplate>`

