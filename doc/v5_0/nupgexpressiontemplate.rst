.. _nupgexpressiontemplate:

nupgexpressiontemplate
===========================================

.. class:: nupgexpressiontemplate.NUPGExpressionTemplate(bambou.nurest_object.NUMetaRESTObject,):

Policy Group Expression Template is an expression consisting of policy groups defined at Domain Template or L2 Domain Template


Attributes
----------


- ``name`` (**Mandatory**): Name  of the Policy Group Expression Template

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the  Policy Group Expression Template

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``expression`` (**Mandatory**): Actual Policy Group Expression like (PG1 || PG2) && !PG3. Allowed operators are && (AND), ! (NOT), II (OR) and ( )

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nul2domaintemplate.NUL2DomainTemplate<nul2domaintemplate>`

- :ref:`nudomaintemplate.NUDomainTemplate<nudomaintemplate>`

