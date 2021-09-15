.. _nunsgmigrationprofile:

nunsgmigrationprofile
===========================================

.. class:: nunsgmigrationprofile.NUNSGMigrationProfile(bambou.nurest_object.NUMetaRESTObject,):

The profile represents the migration information used by an NSG when it migrates from one VSD to another.


Attributes
----------


- ``name`` (**Mandatory**): A unique name set by an operator identifying the NSG Migration Profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A description of the NSG Migration Profile instance.

- ``destination_proxy_fqdn`` (**Mandatory**): FQDN of the system acting as a proxy between the NSG instances and the destination VSD.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

