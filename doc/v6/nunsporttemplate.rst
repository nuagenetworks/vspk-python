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

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the NSG Port Template

- ``physical_name`` (**Mandatory**): Identifier of the Port

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_type`` (**Mandatory**): Type of the Ports that will be instantiated from this template.

- ``speed``: Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate

- ``creation_date``: Time stamp when this object was created.

- ``associated_egress_qos_policy_id``: ID of the Egress QoS Policy associated with this NSG Port Template.

- ``mtu``: Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit hat the layer can pass on.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlantemplate.NUVLANTemplate<nuvlantemplate>`                                                                                                             ``vlan_templates`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsgatewaytemplate.NUNSGatewayTemplate<nunsgatewaytemplate>`

