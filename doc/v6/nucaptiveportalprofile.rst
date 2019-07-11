.. _nucaptiveportalprofile:

nucaptiveportalprofile
===========================================

.. class:: nucaptiveportalprofile.NUCaptivePortalProfile(bambou.nurest_object.NUMetaRESTObject,):

Object representing a Wireless Access Captive Portal Profile which can be associated with SSID entities from which end users may be presented with instructions and condition of use when connecting to an open wireless access point.


Attributes
----------


- ``name`` (**Mandatory**): Name of the captive portal profile.

- ``captive_page`` (**Mandatory**): Attribute having the contents of captive portal page displayed to end user. User can possibly include very basic HTML tags like <p>, <ul> etc. in order to fomat the text displayed to the user.

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description for the captive portal profile.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``portal_type`` (**Mandatory**): Type of the portal page.  Will decide if the NSG rendering the page will have a strict rendering of the welcoming page based on what is given by VSD, or if the information can be made customisable by an operator to include animations, videos, images, and other types of more complex scripts.

- ``external_id``: External object ID. Used for integration with third party systems






Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

