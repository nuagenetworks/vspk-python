.. _nucommand:

nucommand
===========================================

.. class:: nucommand.NUCommand(bambou.nurest_object.NUMetaRESTObject,):

A Command represents an operation that needs to be executed on an entity (NSG, Gateway, ...) which requires little processing by VSD, but may result in a long activity on the external entity.  An example would be to trigger an action on VSD so that a Gateway download a new image.  VSDs handling of the request is limited to generating a message to be sent to the device on which the download process is expected.  The device then acts on the request and proceeds with the download...  That may be a long process.  The commands API is similar to the Jobs API with regards to triggering operations on objects.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``detail``: Details about the command execution as reported directly from the NSG independent of status codes.

- ``detailed_status``: A string representing the detailed status of the operation that was triggered by the execution of the Command instance.

- ``detailed_status_code``: A numerical code mapping to a list of detailed statuses that can apply to a Command instance.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``command`` (**Mandatory**): Specifies the type of command that is stated for execution on the system receiving the operation request.  A request for download, a request for upgrade, a request for revocation, ...

- ``command_information``: Informative details on what command is to be executed.  It complements the commandType attribute.  An example of a value could be a URL, a version number, a UUID of another object, ...

- ``progress``: JSON string detailing the progress of the command execution on Gateway.

- ``assoc_entity_type``: Managed Object Type of the entity on which this Command is associated.

- ``associated_param``: Parameters to be supplied for execution of this command. This should be the ID of the object supplying parameters.

- ``associated_param_type``: Type of the object which supplies parameters for this command. For NSG_APPLY_PATCH command this should be NSG_PATCH_PROFILE. For NSG_DELETE_PATCH it should be PATCH

- ``status``: The status of the Command from a VSD perspective.

- ``full_command``: Full command including parameters that is to be executed.

- ``summary`` (**Mandatory**): A generated summary for the action giving some general context on the command executed.

- ``override``: Operator specified action which overrides the normal life cycle of a command.

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

