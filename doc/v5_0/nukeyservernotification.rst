.. _nukeyservernotification:

nukeyservernotification
===========================================

.. class:: nukeyservernotification.NUKeyServerNotification(bambou.nurest_object.NUMetaRESTObject,):

KeyServer Notification - Create one of these transient objects to push an event to the KeyServer


Attributes
----------


- ``base64_json_string``: The base 64 encoded JSON String of the message object

- ``message``: The message to send

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``notification_type``: The notification type to trigger

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================


