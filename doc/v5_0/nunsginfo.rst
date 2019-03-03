.. _nunsginfo:

nunsginfo
===========================================

.. class:: nunsginfo.NUNSGInfo(bambou.nurest_object.NUMetaRESTObject,):

Device information coming from the NSG


Attributes
----------


- ``mac_address``: A comma separated list of MAC Addresses associated to the NSG's interfaces (eg, port1, port2, port3).

- ``aar_application_release_date``: Release Date of the AAR Application

- ``aar_application_version``: The AAR Application Version

- ``bios_release_date``: Release Date of the NSG BiOS

- ``bios_version``: NSG BIOS Version as received from the NSG during bootstrap or a reboot.  If the information exeeds 255 characters, the extra characters will be truncated.

- ``sku``: The part number of the NSG

- ``tpm_status``: TPM status code as reported by the NSG during bootstrapping. This informate indicates if TPM is being used in securing the private key/certificate of an NSG. Possible values are 0(Unknown), 1(Enabled_Not_Operational), 2(Enabled_Operational), 3(Disabled).

- ``tpm_version``: TPM (Trusted Platform Module) version as reported by the NSG.

- ``cpu_type``: The NSG Processor Type based on information extracted during bootstrapping.  This may refer to a type of processor manufactured by Intel, ARM, AMD, Cyrix, VIA, or others.

- ``nsg_version``: The NSG Version as reported during a bootstrap or a reboot of the NSG. 

- ``uuid``: The Redhat/CentOS UUID of the NSG

- ``name``: Name of the Gateway.

- ``family``: The NSG Family type as it was returned by the NSG during bootstrapping.

- ``patches_detail``: Base64 Encoded JSON String of the extra details pertaining to each successfully installed patch

- ``serial_number``: The NSG's serial number as it is stored in the system's CMOS (Motherboard)

- ``personality``: Personality of the Gateway.

- ``libraries``: Tracks RPM package installed for some libraries installed on the NSG.

- ``cmd_detailed_status``: Detailed status of the current running or last run command.

- ``cmd_detailed_status_code``: Numerical value representing the code mapping to detailed status of the current or last command operation.

- ``cmd_download_progress``: DownloadProgress object representing the progress of Gateway image download.

- ``cmd_id``: Identifier of the running or last Command.

- ``cmd_last_updated_date``: Time stamp when the command was last updated.

- ``cmd_status``: Status of the current or last command.

- ``cmd_type``: Specifies the type of command that is stated for execution on the system. A request for download or a request for upgrade.

- ``enterprise_id``: The enterprise associated with this Gateway.

- ``enterprise_name``: Name of the Enterprise associated with this Gateway.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``bootstrap_status``: The bootstrap status of the NSG from which the infomation was collected.

- ``product_name``: NSG Product Name as reported when the device bootstraps.

- ``associated_entity_type``: Object type of the associated entity.

- ``associated_ns_gateway_id``: The ID of the NSG from which the infomation was collected.

- ``external_id``: External object ID. Used for integration with third party systems

- ``system_id``: System identifier of the Gateway.






Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

