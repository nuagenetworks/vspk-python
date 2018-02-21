.. _nunsgpatchprofile:

nunsgpatchprofile
===========================================

.. class:: nunsgpatchprofile.NUNSGPatchProfile(bambou.nurest_object.NUMetaRESTObject,):

This profile represents the patch information to be used by an NSG for applying a patch.


Attributes
----------


- ``name``: A unique name identifying this patch profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``patch_tag``: A unique brief name and version of the patch derived from Patch URL.

- ``patch_url`` (**Mandatory**): URL to retrieve the patch bundle for this particular patch.

- ``description``: A brief description of this patch profile.

- ``enterprise_id``: Enterprise/Organisation that this patch profile belongs to.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nume.NUMe<nume>`

