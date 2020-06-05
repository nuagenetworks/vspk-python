.. _nuidpprofile:

nuidpprofile
===========================================

.. class:: nuidpprofile.NUIDPProfile(bambou.nurest_object.NUMetaRESTObject,):

IDP Profile/Rules are used to detect intrusion attempts and/or inspect network traffic and take appropriate action.


Attributes
----------


- ``name`` (**Mandatory**): Symbolic name of the IDP Rule

- ``description``: Descriptive text for IDP Profile

- ``protect_against_insertion_evasion``: Enable protection against insertion/evasion attacks.

- ``associated_enterprise_id``: The ID of the associated Enterprise




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`nuidpprofileaction.NUIDPProfileAction<nuidpprofileaction>`                                                                                                 ``idp_profile_actions`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

