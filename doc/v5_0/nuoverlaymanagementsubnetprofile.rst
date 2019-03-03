.. _nuoverlaymanagementsubnetprofile:

nuoverlaymanagementsubnetprofile
===========================================

.. class:: nuoverlaymanagementsubnetprofile.NUOverlayManagementSubnetProfile(bambou.nurest_object.NUMetaRESTObject,):

The Overlay Management Subnet profile that maps to a DNA subnet and contains the syslog destinations. Where DNS means Do Not Advertise (Advertise=False)


Attributes
----------


- ``name`` (**Mandatory**): The name of the profile

- ``description``: A description of the profile

- ``associated_dna_subnet_id`` (**Mandatory**): The DNA Subnet ID associated with this profile. Where DNS means Do Not Advertise (Advertise=False)

- ``syslog_destination_ids``: JSON list of strings, each being a Syslog Destination ID which needs to be attached to this profile. Can be 0 to 2 IDs in the list






Parents
--------


- :ref:`nuoverlaymanagementprofile.NUOverlayManagementProfile<nuoverlaymanagementprofile>`

