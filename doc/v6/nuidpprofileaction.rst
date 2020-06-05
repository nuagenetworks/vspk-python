.. _nuidpprofileaction:

nuidpprofileaction
===========================================

.. class:: nuidpprofileaction.NUIDPProfileAction(bambou.nurest_object.NUMetaRESTObject,):

An IDP Profile/Rule Action specifies what signatures to search for in the network traffic, and what action to take if those signatures are found.


Attributes
----------


- ``idp_signatures``: IDP Signatures to search in network traffic

- ``action``: Specifies what action to take if given signatures is found

- ``priority``: The priority determines the order of IDP action

- ``associated_idp_profile_id``: The ID of the associated IDP Profile






Parents
--------


- :ref:`nuidpprofile.NUIDPProfile<nuidpprofile>`

