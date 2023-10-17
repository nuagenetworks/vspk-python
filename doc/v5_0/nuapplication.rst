.. _nuapplication:

nuapplication
===========================================

.. class:: nuapplication.NUApplication(bambou.nurest_object.NUMetaRESTObject,):

represents a application with L4/L7 classification


Attributes
----------


- ``dscp``: DSCP match condition to be set in the rule. It is either * or from 0-63.

- ``name`` (**Mandatory**): name of the application

- ``bandwidth``: Minimum Failover Bandwidth of the application.

- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``performance_monitor_type``: Describes the trigger for the application.

- ``certificate_common_name``: Describes the certificate common name

- ``description``: description of Application

- ``destination_ip``: destination IP in CIDR format

- ``destination_port``: value should be either * or single port number 

- ``network_symmetry``: Network symmetry flag

- ``enable_pps``: Enable the performance probe for this application

- ``one_way_delay``: one way Delay

- ``one_way_jitter``: one way Jitter

- ``one_way_loss``: one way loss

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``post_classification_path``: default set to any , possible values primary/secondary/any

- ``source_ip``: source IP address

- ``source_port``: source Port ,value should be either * or single port number 

- ``app_id``: a unique 2 byte id generated when a application is created and used by VRS  for probing.

- ``optimize_path_selection``: with values being Latency, Jitter, PacketLoss

- ``pre_classification_path``: default set to primary , possible values primary/secondary

- ``protocol``: Protocol number that must be matched

- ``associated_l7_application_signature_id``: associated Layer7 Application Type ID

- ``ether_type``: Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

- ``external_id``: External object ID. Used for integration with third party systems

- ``symmetry``: Maintain path symmetry during SLA violation




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`numonitorscope.NUMonitorscope<numonitorscope>`                                                                                                             ``monitorscopes`` 
:ref:`nuapplicationbinding.NUApplicationBinding<nuapplicationbinding>`                                                                                           ``application_bindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

- :ref:`nume.NUMe<nume>`

- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nul7applicationsignature.NUL7applicationsignature<nul7applicationsignature>`

