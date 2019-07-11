.. _nulocation:

nulocation
===========================================

.. class:: nulocation.NULocation(bambou.nurest_object.NUMetaRESTObject,):

Gateway location details.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``latitude``: Latitude in decimal format.

- ``address``: Formatted address including property number, street name, suite or office number, ...

- ``ignore_geocode``: Request BSS to perform a geocode on the address - If no value passed, requestGeocode will be set to true

- ``time_zone_id``: Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``locality``: Locality/City/County

- ``longitude``: Longitude in decimal format.

- ``country``: Country

- ``associated_entity_name``: Name of the associated entity.

- ``associated_entity_type``: Object type of the associated entity.

- ``state``: State/Province/Region

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugateway.NUGateway<nugateway>`

- :ref:`nunsgateway.NUNSGateway<nunsgateway>`

