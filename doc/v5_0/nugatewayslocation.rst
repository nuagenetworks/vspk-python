.. _nugatewayslocation:

nugatewayslocation
===========================================

.. class:: nugatewayslocation.NUGatewaysLocation(bambou.nurest_object.NUMetaRESTObject,):

Gateway location details


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``latitude``: Latitude in decimal format.

- ``address``: Formatted address including property number, street name, suite or office number, ...

- ``ignore_geocode``: Request BSS to perform a geocode on the address - If no value passed, 'ignoreGeocode' will be set to true.

- ``time_zone_id`` (**Mandatory**): Time zone in which the Gateway is located.    This can be in the form of a UTC/GMT offset, continent/city location, or country/region.    The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.    Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.    URL :    http://www.iana.org/time-zones    Default value is UTC (translating to Etc/Zulu)

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``locality``: Locality, City, or County information about where the gateway is installed.

- ``longitude``: Longitude in decimal format.

- ``country``: Country in which the gateway is instantiated (VM) or installed (Physical).

- ``associated_entity_name``: The name of the Entity to which a Location instance is tied to.

- ``associated_entity_type``: Type of the gateway entity to which the Location instance is attached.

- ``state``: State, Province, or Region to which the locality in which the gateway is installed belongs.

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


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

