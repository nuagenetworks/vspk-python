# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging
import importlib
import re
import pkg_resources

from bambou.exceptions import BambouHTTPError
from .printer import Printer


class Utils(object):
    """ Utils """

    # TODO: remove that custom thing
    INVARIANT_RESOURCES = ["qos", "vrs", "cms", "statistics"]

    @classmethod
    def _clean_name(cls, string):
        """ String cleaning for specific cases

            This is very specific and is used to force
            some underscore while using get_python_name.

            Args:
                string: the string to clean

            Returns:
                Returns a clean string
        """
        rep = {
            "VPort": "Vport",
            "IPID": "IpID"
        }

        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

    @classmethod
    def get_python_name(cls, name):
        """ Transform a given name to python name """
        first_cap_re = re.compile("(.)([A-Z](?!s([A-Z])*)[a-z]+)")
        all_cap_re = re.compile("([a-z0-9])([A-Z])")

        s1 = first_cap_re.sub(r"\1_\2", Utils._clean_name(name))
        return all_cap_re.sub(r"\1_\2", s1).lower()

    @classmethod
    def get_singular_name(cls, entity_name_plural):
        """ Returns the singular name of the plural name """

        if entity_name_plural in Utils.INVARIANT_RESOURCES:
            return entity_name_plural

        if entity_name_plural[-3:] == "ies":
            return entity_name_plural[:-3] + "y"

        if entity_name_plural[-1] == "s":
            return entity_name_plural[:-1]

        return entity_name_plural

    @classmethod
    def get_entity_name_plural(cls, singular_name):
        """ Returns the plural name of the singular name """

        if singular_name in Utils.INVARIANT_RESOURCES:
            return singular_name

        vowels = ["a", "e", "i", "o", "u", "y"]
        if singular_name[-1:] == "y" and singular_name[-2] not in vowels:
            return singular_name[:-1] + "ies"

        if singular_name[-1:] == "s":
            return singular_name

        return singular_name + "s"

    @classmethod
    def get_vspk_version(cls, version):
        """ Get the vspk version according to the given version

            Args:
                version (int): the version

            Returns:
                version as string

            Example:
                get_vspk_version(3.1)
                >>> v3_1

        """
        return ("v%s" % version).replace(".", "_")


class SDKInspector(object):
    """ Utils to access SDK objects

    """

    def __init__(self, version=None):
        """ Initializes

        """
        if version:
            self._version = Utils.get_vspk_version(version)

        self._objects_mapping = {}
        self._ignored_resources = []
        self._sdk = None
        self._logger = None

        self._load_objects()

    def _load_objects(self):
        """ Load objects in a temporary database

        """
        self._get_package()

        object_names = [name for name in dir(self._sdk) if name != "NUVSDSession" and name != "SDKInfo" and name.startswith("NU") and not name.endswith("Fetcher")]

        for object_name in object_names:
            obj = getattr(self._sdk, object_name)
            self._objects_mapping[obj.rest_name] = object_name

    def _get_package(self):
        """ Returns sdk package

        """
        if self._sdk is None:
            try:
                self._sdk = importlib.import_module("vspk.%s" % self._version)
                self._logger = importlib.import_module("vspk.utils").set_log_level
                self._ignored_resources = [self._sdk.SDKInfo.root_object_class().rest_name]

                # Printer.info("Imported vspk.%s." % self._version)
            except ImportError:
                self._sdk = importlib.import_module("vspk")
            except ImportError as error:
                Printer.raise_error("Please install requirements using command line 'pip install -r requirements.txt'.\n%s" % error)

        return self._sdk

    def get_all_objects(self):
        """ Returns all objects available

        """
        resources = self._objects_mapping.keys()
        resources = [Utils.get_entity_name_plural(name) for name in resources if name not in self._ignored_resources]

        return resources

    def get_class(self, name):
        """ Get a SDK class object
            Args:
                name: the name of the object
            Returns:
                a SDK class object
        """
        if name in self._objects_mapping:
            classname = self._objects_mapping[name]

            klass = None
            try:
                klass = getattr(self._sdk, classname)
            except:
                Printer.raise_error('Unknown class %s' % classname)

            return klass

        Printer.raise_error('Unknown object named %s' % name)

    def get_instance(self, name):
        """ Get SDK object instance according to a given name

            Args:
                name: the name of the object

            Returns:
                A SDK object or raise an exception
        """
        klass = self.get_class(name)
        return klass()

    def get_parent(self, parent_infos, root_object):
        """ Get SDK parent object if possible
            Otherwise it will take the user

            Args:
                parent_infos: a list composed of (parent_name, uuid)

            Returns:
                A parent if possible otherwise the user in session

        """
        if parent_infos and len(parent_infos) == 2:
            name = parent_infos[0]
            uuid = parent_infos[1]

            singular_name = Utils.get_singular_name(name)
            parent = self.get_instance(singular_name)
            parent.id = uuid

            try:
                (parent, connection) = parent.fetch()
            except Exception, ex:
                Printer.raise_error("Failed fetching parent %s with uuid %s\n%s" % (name, uuid, ex))

            return parent

        return root_object

    def get_user_session(self, args):
        """ Get api key

            Args:
                username: username to get an api key
                password: password to get an api key
                api: URL of the API endpoint
                enterprise: Name of the enterprise to connect

            Returns:
                Returns an API Key if everything works fine
        """
        self._set_verbose_mode(args.verbose)
        session = self._sdk.NUVSDSession(username=args.username, password=args.password, enterprise=args.enterprise, api_url=args.api)
        try:
            session.start()
        except BambouHTTPError as error:
            status_code = error.connection.response.status_code
            if status_code == 401:
                Printer.raise_error("Could not log on %s (API %s) with username=%s password=%s enterprise=%s" % (args.api, args.version, args.username, args.password, args.enterprise))
            else:
                Printer.raise_error("Cannot access %s [HTTP %s]. Current vspk version tried to connect to the Server API %s" % (args.api, status_code, args.version))

        root_object = session.root_object

        if root_object.api_key is None:
            Printer.raise_error("Could not get a valid API key. Activate verbose mode for more information")

        return session

    def _set_verbose_mode(self, verbose):
        """ Defines verbosity

            Args:
                verbose: Boolean to activate or deactivate DEBUG mode

        """
        pass
        if verbose:
            Printer.info("Verbose mode is now activated.")
            self._logger(logging.DEBUG)
        else:
            self._logger(logging.ERROR)