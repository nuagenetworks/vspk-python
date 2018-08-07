.. _nunsggroup:

nunsggroup
===========================================

.. class:: nunsggroup.NUNSGGroup(bambou.nurest_object.NUMetaRESTObject,):

A logical group of NSG and NSG-BR instances that can be used to assign NSG-UBRs to all NSGs in the group, to provide connectivity to NSGs in disjoint underlays.


Attributes
----------


- ``name``: Name of the NSG Group

- ``description``: Description of the NSG Group




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nunsgateway.NUNSGateway<nunsgateway>`                                                                                                                      ``ns_gateways`` 
:ref:`nuducgroupbinding.NUDUCGroupBinding<nuducgroupbinding>`                                                                                                    ``duc_group_bindings`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

