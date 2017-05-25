.. _nuuser:

nuuser
===========================================

.. class:: nuuser.NUUser(bambou.nurest_object.NUMetaRESTObject,):

Object that identifies the user functions.


Attributes
----------


- ``management_mode``: Management mode of the user object - allows for override of external authorization and syncup

- ``password`` (**Mandatory**): User password stored as a hash (SHA-1 encrpted)

- ``last_name`` (**Mandatory**): Last name of the user

- ``last_updated_by``: ID of the user who last updated the object.

- ``first_name`` (**Mandatory**): First name of the user

- ``disabled``: Status of the user account; true=disabled, false=not disabled; default value = false

- ``email`` (**Mandatory**): Email address of the user

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``mobile_number``: Mobile Number of the user

- ``user_name`` (**Mandatory**): Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

- ``avatar_data``: URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

- ``avatar_type``: Avatar type.

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuvm.NUVM<nuvm>`                                                                                                                                           ``vms`` 
:ref:`nucontainer.NUContainer<nucontainer>`                                                                                                                      ``containers`` 
:ref:`nugroup.NUGroup<nugroup>`                                                                                                                                  ``groups`` 
:ref:`nuavatar.NUAvatar<nuavatar>`                                                                                                                               ``avatars`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nugroup.NUGroup<nugroup>`

- :ref:`nume.NUMe<nume>`

- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

