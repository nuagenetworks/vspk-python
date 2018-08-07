.. _nudeploymentfailure:

nudeploymentfailure
===========================================

.. class:: nudeploymentfailure.NUDeploymentFailure(bambou.nurest_object.NUMetaRESTObject,):

A deployment failure represents a deployment operation initiated by the VSD that resulted in a failure.


Attributes
----------


- ``last_failure_reason``: A detailed description of the last deployment failure.

- ``last_known_error``: A string reporting the last reported deployment error condition.

- ``affected_entity_id``: UUID of the entity on which deployment failed.

- ``affected_entity_type``: Managed object type corresponding to the entity on which deployment failed.

- ``error_condition``: A numerical code mapping to the deployment error condition.

- ``number_of_occurences``: A count of failed deployment attempts.

- ``event_type``: Event type corresponding to the deployment failure






Parents
--------


- :ref:`nuredundancygroup.NURedundancyGroup<nuredundancygroup>`

- :ref:`nugateway.NUGateway<nugateway>`

