.. _nuvlantemplate:

nuvlantemplate
===========================================

.. class:: nuvlantemplate.NUVLANTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents VLAN Template under a Port Template object.


Attributes
----------


- ``value`` (**Mandatory**): Value of VLAN

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Port

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``is_uplink``: Indicates that this VLAN Template should be considered as being used for uplink connection.

- ``associated_connection_type``: States the managed object type of the uplink connection associated to this VLAN Template instance.

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this Vlan.

- ``associated_ingress_qos_policy_id``: ID of the Ingress QoS Policy associated with this VLAN Template.

- ``associated_uplink_connection_id``: ID of the uplink connection making use of this VLAN Template instance.

- ``associated_vsc_profile_id``: The ID of the infrastructure VSC profile this is associated with this instance of a vlan or vlan template.

- ``duc_vlan``: When set to true, this specifies that this VLAN template instance serves as an underlay connection endpoint on an NSG-UBR gateway.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: This type marks a VLAN for its utility.




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

