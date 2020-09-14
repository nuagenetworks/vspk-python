.. _nuallgateway:

nuallgateway
===========================================

.. class:: nuallgateway.NUAllGateway(bambou.nurest_object.NUMetaRESTObject,):

A read-only API to get all gateway objects in the VSD environment. Use the ID field to then actually manage the gateway using the gateway API entity.


Attributes
----------


- ``mac_address``: MAC Address of the first interface

- ``zfb_match_attribute``: The Zero Factor Bootstrapping (ZFB) Attribute that should be used to match the gateway on when it tries to bootstrap.

- ``zfb_match_value``: The Zero Factor Bootstrapping (ZFB) value that needs to match with the gateway during the bootstrap attempt. This value needs to match with the ZFB Match Attribute.

- ``bios_release_date``: Release Date of the BIOS.  The format can vary based on the manufacturer but normally includes year/month/day or year/week details (eg. 01/01/2011 or 2018/06/15 or 2018/22)

- ``bios_version``: BIOS Version (eg. 0.5.1)

- ``cpu_type``: The Processor Type as reported during bootstrapping.

- ``uuid``: UUID of the device

- ``name``: Name of the Gateway

- ``family``: The family type of the gateway based on common characteristics with other members of a particular variation of an NSG hardware or of a virtual deployment.

- ``management_id``: The identifier of this gateway's management interface.

- ``last_updated_by``: ID of the user who last updated the object.

- ``datapath_id``: Identifier of the Gateway, based on the systemID which is generated when the instance is created in VSD.

- ``patches``: Patches that have been installed on the NSG

- ``gateway_connected``: A boolean flag indicating the status of the gateway.

- ``gateway_version``: The Gateway Software Version as reported during bootstrapping.

- ``redundancy_group_id``: The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute

- ``peer``: The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

- ``template_id``: The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway

- ``pending``: Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.

- ``serial_number``: The device's serial number

- ``permitted_action``: The permitted  action to USE/EXTEND  this Gateway.

- ``personality``: Personality of the Gateway, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``libraries``: Versions of monitored libraries currently installed on the Gateway.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: The enterprise associated with this Gateway. This is a read only attribute

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location_id``: Association to an object which contains location information about this gateway instance.

- ``bootstrap_id``: The bootstrap details associated with this Gateway. NOTE: This is a read only property, it can only be set during creation of a gateway.

- ``bootstrap_status``: The bootstrap status of this Gateway. NOTE: This is a read only property.

- ``product_name``: Product Name as reported during bootstrapping.

- ``use_gateway_vlanvnid``: When set, VLAN-VNID mapping must be unique for all the vports of the gateway

- ``associated_gateway_security_id``: Read only ID of the associated gateway security object.

- ``associated_gateway_security_profile_id``: Readonly Id of the associated gateway security profile object

- ``associated_nsg_info_id``: Read only ID of the associated gateway information object

- ``associated_netconf_profile_id``: UUID of the Netconf Profile associated to this gateway.

- ``vtep``: Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

- ``auto_disc_gateway_id``: The Auto Discovered Gateway associated with this Gateway Instance

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the Gateway, cannot be modified after creation




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

