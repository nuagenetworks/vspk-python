.. _nusyslogdestination:

nusyslogdestination
===========================================

.. class:: nusyslogdestination.NUSyslogDestination(bambou.nurest_object.NUMetaRESTObject,):

Syslog Destination provides the definition for a Syslog Server Destination


Attributes
----------


- ``ip_address`` (**Mandatory**): The IP Address of the syslog server

- ``ip_type``: IP Type of the syslog IP Address. Supported values: 'IPV4'

- ``name`` (**Mandatory**): Name of the syslog server

- ``description``: A detailed description of the syslog server

- ``port`` (**Mandatory**): The port the syslog server is configured on

- ``type``: The protocol type of the syslog server. Supported values: 'UDP'






Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

