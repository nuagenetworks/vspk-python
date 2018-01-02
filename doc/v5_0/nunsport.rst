.. _nunsport:

nunsport
===========================================

.. class:: nunsport.NUNSPort(bambou.nurest_object.NUMetaRESTObject,):

Represents a Port of a particular NS Gateway object.


Attributes
----------


- ``nat_traversal``: Enum value that states the type of NAT Traversal the NSG instance will use to talk to other NSGs and the Internet.  (This field is deprecated in 5.0)

- ``vlan_range``: VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

- ``name`` (**Mandatory**): Name of the Port

- ``last_updated_by``: ID of the user who last updated the object.

- ``template_id``: The ID of the template that this Port was created from

- ``permitted_action``: The permitted action to USE/EXTEND this NSG Port.

- ``description``: A description of the Port

- ``physical_name`` (**Mandatory**): Identifier of the Port

- ``enable_nat_probes``: If enabled, probes will be sent to other NSGs and DTLS sessions for IPSEC and VXLAN will be set up to the VSCs. If disabled, no NAT probes are sent on that uplink and no DTLS sessions are set up to the VSCs.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``port_type`` (**Mandatory**): Type of the Port.

- ``speed``: Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate.

- ``traffic_through_ubr_only``: If enabled, cuts down the number of probes to just the number of provisioned UBRs.

- ``use_user_mnemonic``: determines whether to use user mnemonic of the Port

- ``user_mnemonic``: user mnemonic of the Port

- ``associated_egress_qos_policy_id``: ID of the Egress QoS Policy associated with this NSG Port.

- ``associated_redundant_port_id``: ID of the redundant port to which the Port is associated to.

- ``status``: Status of the port.

- ``mtu``: Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuvlan.NUVLAN<nuvlan>`                                                                                                                                     ``vlans`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
:ref:`nustatistics.NUStatistics<nustatistics>`                                                                                                                   ``statistics`` 
:ref:`nustatisticspolicy.NUStatisticsPolicy<nustatisticspolicy>`                                                                                                 ``statistics_policies`` 
:ref:`nulteinformation.NULTEInformation<nulteinformation>`                                                                                                       ``lte_informations`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuredundantport.NURedundantPort<nuredundantport>`

- :ref:`nuautodiscoveredgateway.NUAutoDiscoveredGateway<nuautodiscoveredgateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

