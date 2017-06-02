.. _nuenterpriseprofile:

nuenterpriseprofile
===========================================

.. class:: nuenterpriseprofile.NUEnterpriseProfile(bambou.nurest_object.NUMetaRESTObject,):

Enterprise profile, used to store an enterprise's policies, quota etc.


Attributes
----------


- ``bgp_enabled``: Enable BGP for this enterprise profile

- ``dhcp_lease_interval``: DHCP Lease Interval (in hours) to be used by an enterprise.

- ``name`` (**Mandatory**): The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``receive_multi_cast_list_id``: Readonly ID of the auto generated receive multicast list associated with this enterprise profile

- ``send_multi_cast_list_id``: Readonly ID of the auto generated send multicast list associated with this enterprise profile

- ``description``: A description of the enterprise/organisation profile.

- ``allow_advanced_qos_configuration``: Controls whether this enterprise has access to advanced QoS settings.

- ``allow_gateway_management``: If set to true lets the enterprise admin create gateway templates and instances.

- ``allow_trusted_forwarding_class``: Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

- ``allowed_forwarding_classes``: Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

- ``floating_ips_quota``: Quota set for the number of floating IPs to be used by an enterprise.

- ``enable_application_performance_management``: Enable DPI for this enterprise

- ``encryption_management_mode``: encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuenterprise.NUEnterprise<nuenterprise>`                                                                                                                   ``enterprises`` 
:ref:`numulticastlist.NUMultiCastList<numulticastlist>`                                                                                                          ``multi_cast_lists`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
:ref:`nuexternalservice.NUExternalService<nuexternalservice>`                                                                                                    ``external_services`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

