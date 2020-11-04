.. _numirrordestination:

numirrordestination
===========================================

.. class:: numirrordestination.NUMirrorDestination(bambou.nurest_object.NUMetaRESTObject,):

Mirror Destinations are underlay-reachable IP addresses to which the mirrored traffic will be sent. On the server identified by the IP, a tool like Wireshark can be used to capture and analyse the traffic going through a VPort. The mirrored traffic is sent to the collector using GRE encapsulation.


Attributes
----------


- ``name`` (**Mandatory**): Name of the mirror destination. Valid characters are alphabets, numbers, space and hyphen( - ).

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``service_id``: Service ID of the mirror destination.

- ``destination_ip`` (**Mandatory**): IP address of the destination server where you want your traffic to be mirrored.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuegressaclentrytemplate.NUEgressACLEntryTemplate<nuegressaclentrytemplate>`                                                                               ``egress_acl_entry_templates`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuingressaclentrytemplate.NUIngressACLEntryTemplate<nuingressaclentrytemplate>`                                                                            ``ingress_acl_entry_templates`` 
:ref:`nuingressadvfwdentrytemplate.NUIngressAdvFwdEntryTemplate<nuingressadvfwdentrytemplate>`                                                                   ``ingress_adv_fwd_entry_templates`` 
:ref:`nuvportmirror.NUVPortMirror<nuvportmirror>`                                                                                                                ``vport_mirrors`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`numirrordestinationgroup.NUMirrorDestinationGroup<numirrordestinationgroup>`

