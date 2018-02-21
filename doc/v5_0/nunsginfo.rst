.. _nunsginfo:

nunsginfo
===========================================

.. class:: nunsginfo.NUNSGInfo(bambou.nurest_object.NUMetaRESTObject,):

Device information coming from the NSG


Attributes
----------


- ``mac_address``: MAC Address of the NSG.  May represent the MAC address of the first uplink that came operational during bootstrapping.

- ``bios_release_date``: Release Date of the NSG BiOS

- ``bios_version``: NSG BIOS Version as received from the NSG during bootstrap or a reboot.  If the information exeeds 255 characters, the extra characters will be truncated.

- ``sku``: The part number of the NSG

- ``tpm_status``: TPM status as reported by the NSG during bootstrapping.  This informate indicates if TPM is being used in securing the private key/certificate of an NSG.

- ``tpm_version``: TPM (Trusted Platform Module) version as reported by the NSG.

- ``cpu_type``: The NSG Processor Type based on information extracted during bootstrapping.  This may refer to a type of processor manufactured by Intel, ARM, AMD, Cyrix, VIA, or others.

- ``nsg_version``: The NSG Version as reported during a bootstrap or a reboot of the NSG. 

- ``uuid``: The Redhat/CentOS UUID of the NSG

- ``family``: The NSG Family type as it was returned by the NSG during bootstrapping.

- ``patches``: Patches that have been installed on the NSG.

- ``serial_number``: The NSG's serial number as it is stored in the system's CMOS (Motherboard)

- ``libraries``: Tracks RPM package installed for some libraries installed on the NSG.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``product_name``: NSG Product Name as reported when the device bootstraps.

- ``associated_ns_gateway_id``: The ID of the NSG from which the infomation was collected.

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

