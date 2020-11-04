.. _nuautodiscoveredgateway:

nuautodiscoveredgateway
===========================================

.. class:: nuautodiscoveredgateway.NUAutoDiscoveredGateway(bambou.nurest_object.NUMetaRESTObject,):

Represents Auto discovered Gateway.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Gateway

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_id``: The Gateway associated with this Auto Discovered Gateway. This is a read only attribute

- ``peer``: The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.

- ``personality`` (**Mandatory**): Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation.

- ``description``: A description of the Gateway

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``controllers``: Controllers to which this gateway instance is associated with.

- ``creation_date``: Time stamp when this object was created.

- ``vtep``: Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: Identifier of the Gateway




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nuwanservice.NUWANService<nuwanservice>`                                                                                                                   ``wan_services`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`                                                                                                             ``wireless_ports`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuport.NUPort<nuport>`                                                                                                                                     ``ports`` 
:ref:`nunsport.NUNSPort<nunsport>`                                                                                                                               ``ns_ports`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

