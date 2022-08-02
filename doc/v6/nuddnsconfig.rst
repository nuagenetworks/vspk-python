.. _nuddnsconfig:

nuddnsconfig
===========================================

.. class:: nuddnsconfig.NUDdnsconfig(bambou.nurest_object.NUMetaRESTObject,):

The Dynamic DNS (DDNS) Configuration holds the information used to establish the connection with the provider


Attributes
----------


- ``password`` (**Mandatory**): Dynamic DNS provider password

- ``enable_ddns_config``: User can enable/disable the DDNS config using this flag

- ``connection_status``: Dynamic DNS connection status represents the status of the provider connection.

- ``hostname`` (**Mandatory**): Fully Qualified Domain Name to be used for NSG Uplink

- ``provider_name`` (**Mandatory**): Dynamic DNS Provider Name

- ``username`` (**Mandatory**): Dynamic DNS provider username

- ``assoc_gateway_id``: The associated parent NSGateway UUID to the Dynamic DNS Config




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuddnsconfigbinding.NUDdnsconfigbinding<nuddnsconfigbinding>`                                                                                              ``ddnsconfigbindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

