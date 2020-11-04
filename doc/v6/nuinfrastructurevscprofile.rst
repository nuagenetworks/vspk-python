.. _nuinfrastructurevscprofile:

nuinfrastructurevscprofile
===========================================

.. class:: nuinfrastructurevscprofile.NUInfrastructureVscProfile(bambou.nurest_object.NUMetaRESTObject,):

Infrastructure VSC Profiles identify a set of controllers which will be used to connect bootstrapped NSGs.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Infrastructure VSC Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``address_family``: The type of IP address used in the identification of the active and standby controllers.

- ``second_controller``: Second VSC Controller :  IP Address of the secondary VSC system NSG instances associated to this profile will be reaching for.

- ``second_controller_v6``: Second VSC Controller:  IPv6 address of the secondary VSC system NSG instances associated to this profile will be reaching for.

- ``description``: A description of the VSC Profile instance created.

- ``first_controller``: First VSC Controller :  IP Address of the first VSC system NSG instances associated to this profile will be reaching for.

- ``first_controller_v6``: First VSC Controller: IPv6 address of the first VSC system NSG instances associated to this profile will be reaching for.

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``enterprise_id``: Enterprise/Organisation associated with this Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``probe_interval``: Openflow echo timer in milliseconds.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

