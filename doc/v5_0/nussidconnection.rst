.. _nussidconnection:

nussidconnection
===========================================

.. class:: nussidconnection.NUSSIDConnection(bambou.nurest_object.NUMetaRESTObject,):

An SSID Connection instance represents an SSID defined on a WiFi interface.  One SSID Connection is required per SSID created on a WiFi Card/Port.


Attributes
----------


- ``name`` (**Mandatory**): The name associated to the SSID instance.  Has to be unique within an NSG.

- ``passphrase``: Password or passphrase associated to an SSID instance.  Based on the authenticationMode selected.

- ``redirect_option``: Redirection action to exercise once the connecting user has accepted the use policy presented on the Wireless Captive Portal.

- ``redirect_url``: URL to have a newly connected user redirected to once the use policy defined on the Wireless Captive Portal has been accepted by the user.

- ``generic_config``: Blob type attribute that serves to define non-mandatory properties that can be defined in the WiFi Card configuration file.

- ``description``: Brief description of the SSID.

- ``white_list``: List of all white listed MAC Addresses for a particular SSID.

- ``black_list``: List of all the black listed MAC Addresses for a particular SSID.

- ``interface_name``: A read-only attribute that represents the generated interface name for the SSID connection to be provisioned on the NSG.

- ``vport_id``: The Vport associated with this SSID connection.  The attribute can't be modified directly from the SSID Connection.

- ``broadcast_ssid``: Boolean that defines if the SSID name is to be broadcasted or not.

- ``associated_captive_portal_profile_id``: Identification of the Captive Portal Profile that is associated with this instance of SSID connection.

- ``associated_egress_qos_policy_id``: Identification of the Egress QoS policy that is associated with this instance of an SSID Connection.

- ``authentication_mode``: Which mode of authentication is defined for a particular SSID Connection instance.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nucaptiveportalprofile.NUCaptivePortalProfile<nucaptiveportalprofile>`                                                                                     ``captive_portal_profiles`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

