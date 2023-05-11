.. _nuflowstatisticsaggregationrule:

nuflowstatisticsaggregationrule
===========================================

.. class:: nuflowstatisticsaggregationrule.NUFlowstatisticsaggregationrule(bambou.nurest_object.NUMetaRESTObject,):

Provides the definition of the flow statistics Aggregation Rule.


Attributes
----------


- ``name`` (**Mandatory**): The name of the flow statistics aggregation rule.

- ``matching_criteria`` (**Mandatory**): This property reflects the type of traffic associated to flow statistics aggregation rule. Supported values are L4_SERVICE, L4_SERVICE_GROUP.

- ``description``: Desription of the flow statistics aggregation rule.

- ``aggregation_criteria`` (**Mandatory**): Indicates the criteria for statistics aggregation.

- ``associated_traffic_type_id`` (**Mandatory**): Associated Service/Service Group ID.






Parents
--------


- :ref:`nustatisticsprofile.NUStatisticsprofile<nustatisticsprofile>`

