.. _nuinfrastructureevdfprofile:

nuinfrastructureevdfprofile
===========================================

.. class:: nuinfrastructureevdfprofile.NUInfrastructureEVDFProfile(bambou.nurest_object.NUMetaRESTObject,):

An Infrastructure eVDF Profile instance contains common parameters used to bootstrap instances of eVDF (encryption enabled virtual distributed firewall).


Attributes
----------


- ``ntp_server_key``: If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

- ``ntp_server_key_id``: Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).

- ``name`` (**Mandatory**): The name of the profile instance.

- ``last_updated_by``: ID of the user who last updated the object.

- ``active_controller`` (**Mandatory**): The IP address of the active Controller (VSC)

- ``service_ipv4_subnet``: K8 Service IPv4 Subnet

- ``description``: A brief description of the infrastructure profile.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: Enterprise/Organisation associated with this Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``proxy_dns_name`` (**Mandatory**): The DNS name of the proxy device acting as an entry point of eVDF instances to contact VSD.

- ``use_two_factor``: A flag that indicates if two-factor is enabled or not when gateway instances inheriting from this profile are bootstrapped.

- ``standby_controller``: The IP address of the standby Controller (VSC)

- ``nuage_platform``: The Hypervisor Platform

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

