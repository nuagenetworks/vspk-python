.. _nunsporttemplate:

nunsporttemplate
===========================================

.. class:: nunsporttemplate.NUNSPortTemplate(bambou.nurest_object.NUMetaRESTObject,):

Represents Port Template object under a given gateway template object.


Attributes
----------


- ``vlan_range``: VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``name`` (**Mandatory**): Name of the Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: A description of the Port

- ``network_acceleration_enabled``: Flag to enable/disable network throughput acceleration on this port. All port instantiated from this template will inherit this flag.If a particular port instance needs to have a different setting then overwrite the flag for that port instance.

- ``physical_name`` (**Mandatory**): Identifier of the Port

- ``infrastructure_profile_id``: The ID of the infrastructure profile this instance is associated with.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_type`` (**Mandatory**): Type of the Port.

- ``speed``: Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate

- ``associated_egress_qos_policy_id``: ID of the Egress QOS Policy associated with this Vlan.

- ``mtu``: Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit hat the layer can pass on.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`                                                                                                             ``vlan_templates`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

