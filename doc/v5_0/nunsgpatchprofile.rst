.. _nunsgpatchprofile:

nunsgpatchprofile
===========================================

.. class:: nunsgpatchprofile.NUNSGPatchProfile(bambou.nurest_object.NUMetaRESTObject,):

An NSG Patch Profile contains upgrade information that can be given to an NSG Instance.  The profile contains details on where the NSG can retrieve the image to upgrade to, and some criteria related to when the upgrade is to happen once the NSG device has received the information for upgrading.


Attributes
----------


- ``name`` (**Mandatory**): A unique name identifying this patch profile.

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

