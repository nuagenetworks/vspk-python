.. _nuinfrastructurevscprofile:

nuinfrastructurevscprofile
===========================================

.. class:: nuinfrastructurevscprofile.NUInfrastructureVscProfile(bambou.nurest_object.NUMetaRESTObject,):

Represents an Infrastructure VSC Profile.


Attributes
----------


- ``name`` (**Mandatory**): Name of the Infrastructure VSC Profile

- ``last_updated_by``: ID of the user who last updated the object.

- ``second_controller``: Second VSC Controller :  IP Address of the secondary VSC system NSG instances associated to this profile will be reaching for.

- ``description``: A description of the VSC Profile instance created.

- ``first_controller``: First VSC Controller :  IP Address of the first VSC system NSG instances associated to this profile will be reaching for.

- ``enterprise_id``: Enterprise/Organisation associated with this Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``probe_interval``: Openflow echo timer in milliseconds.

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

