.. _nupgexpression:

nupgexpression
===========================================

.. class:: nupgexpression.NUPGExpression(bambou.nurest_object.NUMetaRESTObject,):

Policy Group Expression is an expression consisting of policy groups defined at Domain or L2 Domain Instance.


Attributes
----------


- ``name`` (**Mandatory**): Name  of the Policy Group Expression

- ``last_updated_by``: ID of the user who last updated the object.

- ``last_updated_date``: Time stamp when this object was last updated.

- ``template_id``: Indicates the Policy Group Expression Template from which the Policy Group Expression has been created, it will be empty in case this Policy Group Expression does not come from a template

- ``description``: Description of the  Policy Group Expression

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``creation_date``: Time stamp when this object was created.

- ``owner``: Identifies the user that has created this object.

- ``expression`` (**Mandatory**): Actual Policy Group Expression like (PG1 || PG2) && !PG3. Allowed operators are && (AND), ! (NOT), || (OR) and ( )

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

- :ref:`nuaggregateddomain.NUAggregatedDomain<nuaggregateddomain>`

