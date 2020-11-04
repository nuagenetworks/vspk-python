.. _nussidconnection:

nussidconnection
===========================================

.. class:: nussidconnection.NUSSIDConnection(bambou.nurest_object.NUMetaRESTObject,):

An SSID Connection instance represents an SSID defined on a WiFi interface. One SSID Connection is required per SSID created on a WiFi Card/Port.


Attributes
----------


- ``name`` (**Mandatory**): The name associated to the SSID instance. Has to be unique within an NSG.

- ``passphrase``: Password or passphrase associated to an SSID instance. Based on the authenticationMode selected.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``gateway_id``: The Gateway (NSG) associated with this SSID. This is a read only attribute

- ``readonly``: Determines whether this entity is read only. Read only objects cannot be modified or deleted.

- ``redirect_option``: Redirection action to exercise once the connecting user has accepted the use policy presented on the Wireless Captive Portal.

- ``redirect_url``: URL to have a newly connected user redirected to once the use policy defined on the Wireless Captive Portal has been accepted by the user.

- ``generic_config``: Blob type attribute that serves to define non-mandatory properties that can be defined in the WiFi Card configuration file.

- ``permitted_action``: The permitted action to USE/EXTEND this SSID Connection

- ``description``: Brief description of the SSID.

- ``restricted``: Determines whether this entity can be used in associations with other properties.

- ``white_list``: List of all white listed MAC Addresses for a particular SSID.

- ``black_list``: List of all the black listed MAC Addresses for a particular SSID.

- ``vlan_id``: A VLAN representation of the SSID ordering on a Wireless Card/Port.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``interface_name``: A read-only attribute that represents the generated interface name for the SSID connection to be provisioned on the NSG.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``vport_id``: The Vport associated with this SSID connection. The attribute can't be modified directly from the SSID Connection.

- ``creation_date``: Time stamp when this object was created.

- ``broadcast_ssid``: Boolean that defines if the SSID name is to be broadcasted or not.

- ``associated_captive_portal_profile_id``: Identification of the Captive Portal Profile that is associated with this instance of SSID connection.

- ``associated_egress_qos_policy_id``: Identification of the Egress QoS policy that is associated with this instance of an SSID Connection.

- ``status``: Status of the SSID/VLAN. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH

- ``authentication_mode``: Which mode of authentication is defined for a particular SSID Connection instance.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuwirelessport.NUWirelessPort<nuwirelessport>`

