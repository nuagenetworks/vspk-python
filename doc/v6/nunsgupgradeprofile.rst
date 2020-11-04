.. _nunsgupgradeprofile:

nunsgupgradeprofile
===========================================

.. class:: nunsgupgradeprofile.NUNSGUpgradeProfile(bambou.nurest_object.NUMetaRESTObject,):

An NSG Upgrade Profile contains upgrade information that can be given to an NSG Instance.  The profile contains details on where the NSG can retrieve the image to upgrade to, and some criteria related to when the upgrade is to happen once the NSG device has received the information for upgrading.


Attributes
----------


- ``name`` (**Mandatory**): A unique name set by an operator identifying the NSG Upgrade Profile.

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``description``: A concise description of the NSG Upgrade Profile that gives a small preview of its use.

- ``metadata_upgrade_path`` (**Mandatory**): Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.

- ``enterprise_id``: Enterprise/Organisation associated with this Upgrade Profile instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``download_rate_limit``: Download rate limit used for download of Gateway image in kilobyte per second (KB/s).

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nume.NUMe<nume>`

