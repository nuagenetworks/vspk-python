.. _nuethernetsegmentgroup:

nuethernetsegmentgroup
===========================================

.. class:: nuethernetsegmentgroup.NUEthernetSegmentGroup(bambou.nurest_object.NUMetaRESTObject,):

Group of Ethernet Segments with same ID.


Attributes
----------


- ``vlan_range``: VLAN Range of the EthernetSegment. Format must conform to a-b,c,d-f where a,b,c,d,f are integers from range 0 to 4094.

- ``name``: Name of the Ethernet Segment Group

- ``description``: Description of the Ethernet Segment Group

- ``virtual``: Indicates if Ethernet Segment is Virtual.

- ``port_type`` (**Mandatory**): Type of the Port.

- ``ethernet_segment_id``: Unique Identifier of the Ethernet Segment.




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nupermission.NUPermission<nupermission>`                                                                                                                   ``permissions`` 
:ref:`nuvlan.NUVLAN<nuvlan>`                                                                                                                                     ``vlans`` 
:ref:`nualarm.NUAlarm<nualarm>`                                                                                                                                  ``alarms`` 
:ref:`nuenterprisepermission.NUEnterprisePermission<nuenterprisepermission>`                                                                                     ``enterprise_permissions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuethernetsegmentgwgroup.NUEthernetSegmentGWGroup<nuethernetsegmentgwgroup>`

