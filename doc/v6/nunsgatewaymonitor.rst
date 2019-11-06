.. _nunsgatewaymonitor:

nunsgatewaymonitor
===========================================

.. class:: nunsgatewaymonitor.NUNSGatewayMonitor(bambou.nurest_object.NUMetaRESTObject,):

This API can be used to gather read-only information about an NSG, including information on its state, system metrics, alarm counts, location and version. It is a single view of the full data available for an NSG.


Attributes
----------


- ``controllervrslinks``: List of Controller-VRS links associated with the nsg

- ``vrsinfo``: information about VRS reported from sysmon in JSON format. Has info about cpu usage, memory usage, physical interfaces etc.

- ``vscs``: List of controllers associated with the nsg

- ``nsginfo``: An embedded object from the nsinfo entity from VSD. Contains info such as software version, CPU type, BIOS version etc. The embedded object is returned in JSON format

- ``nsgstate``: Information from the NSGState object in VSD in JSON format. Contains information about connection status, TPM status, operation mode etc.

- ``nsgsummary``: NSG summary in JSON format - contains alarm counts, locality, bootstrap info etc.






Parents
--------


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

