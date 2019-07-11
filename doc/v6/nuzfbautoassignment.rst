.. _nuzfbautoassignment:

nuzfbautoassignment
===========================================

.. class:: nuzfbautoassignment.NUZFBAutoAssignment(bambou.nurest_object.NUMetaRESTObject,):

Pre-created matching criteria that allows CSPRoot to auto-assign incoming auto-bootstrapping requests to an Enterprise should a match occur.


Attributes
----------


- ``zfb_match_attribute`` (**Mandatory**): Attribute to auto match on

- ``zfb_match_attribute_values`` (**Mandatory**): Array of values to match on

- ``name`` (**Mandatory**): Name of the ZFB auto assignment criteria.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the ZFB auto assignment criteria.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority`` (**Mandatory**): Priority of the Auto Assignment

- ``associated_enterprise_id`` (**Mandatory**): Associated Enterprise ID

- ``associated_enterprise_name``: The name of the associated Enterprise

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nume.NUMe<nume>`

