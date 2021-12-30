.. _nuicmpechotestdefinition:

nuicmpechotestdefinition
===========================================

.. class:: nuicmpechotestdefinition.NUICMPEchoTestDefinition(bambou.nurest_object.NUMetaRESTObject,):

ICMP Echo Test Definition describes the ICMP ping command with parameters to run inside a namespace on NSGateway. This command will be run as per the schedule specified on the Scheduled Test Suite along with the other commands in that suite.


Attributes
----------


- ``packet_count``: Specifies the number of echo requests to be sent.

- ``packet_interval``: Delay in milliseconds between the probes.

- ``packet_size``: Specifies the number of data bytes to be sent.

- ``name`` (**Mandatory**): A descriptive name for the ICMP Echo Test Definition instance.

- ``description``: Description of the ICMP Echo Test Definition instance.

- ``threshold_average_round_trip_time``: The threshold average round trip time KPI in milliseconds that will be monitored when SLA monitoring is enabled.

- ``threshold_packet_loss``: The threshold packet loss percentage KPI to be monitored when SLA monitoring is enabled.

- ``timeout``: Timeout value, in seconds, for the test until the system considers it as failed.

- ``sla_monitoring``: Enables or disables the SLA monitoring.

- ``donot_fragment``: Sets the Don't Fragment flag when enabled. When an IP datagram has its DF flag set, intermediate devices are not allowed to fragment it so if it needs to travel across a network with a MTU smaller that datagram length, the datagram will be dropped.

- ``tos``: This field is used to carry information to provide quality of service features. It is normally used to support Differentiated Services.






Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

