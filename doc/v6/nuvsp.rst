.. _nuvsp:

nuvsp
===========================================

.. class:: nuvsp.NUVSP(bambou.nurest_object.NUMetaRESTObject,):

System Monitoring details for VSP.


Attributes
----------


- ``name``: Name of the VSP

- ``last_updated_by``: ID of the user who last updated the object.

- ``description``: Description of the VSP

- ``embedded_metadata``: Metadata objects associated with this entity. This will contain a list of Metadata objects if the API request is made using the special flag to enable the embedded Metadata feature. Only a maximum of Metadata objects is returned based on the value set in the system configuration.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``location``: Installed location of the VSP product

- ``product_version``: Product version number for VSP

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nunetconfmanager.NUNetconfManager<nunetconfmanager>`                                                                                                       ``netconf_managers`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nuhsc.NUHSC<nuhsc>`                                                                                                                                        ``hscs`` 
:ref:`nuvsc.NUVSC<nuvsc>`                                                                                                                                        ``vscs`` 
:ref:`nueventlog.NUEventLog<nueventlog>`                                                                                                                         ``event_logs`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nume.NUMe<nume>`

