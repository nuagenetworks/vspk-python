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

import os

from .printer import Printer
from .utils import Utils, SDKInspector


class CLICommand(object):
    """ CLI commands

    """
    @classmethod
    def execute(cls, args):
        """ Execute CLI command """

        func = getattr(cls, args.command)
        cls._check_arguments(args)
        func(args)

    ### Commands

    @classmethod
    def list(cls, args):
        """ List all objects

        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        session = inspector.get_user_session(args)
        parent = inspector.get_parent(args.parent_infos, session.root_object)

        classname = instance.__class__.__name__[2:]
        plural_classname = Utils.get_entity_name_plural(classname)
        fetcher_name = Utils.get_python_name(plural_classname)
        query_parameters = cls._get_attributes(args.query_parameters)

        try:
            fetcher = getattr(parent, fetcher_name)
        except:

            if parent.rest_name == inspector._get_package().SDKInfo.root_object_class().rest_name:
                error_message = "Failed to found root objects '%s'. Maybe you forgot to specify the parent using '--in [parent] [ID]' syntax ?" % (fetcher_name)
            else:
                error_message = "'%s' failed to found children '%s'. You can use command 'vsd objects -c %s' to list all possible parents" % (parent.rest_name, fetcher_name, fetcher_name)

            Printer.raise_error(error_message)

        (fetcher, parent, objects) = fetcher.fetch(filter=args.filter, query_parameters=query_parameters)

        if objects is None:
            Printer.raise_error("Could not retrieve. Activate verbose mode for more information")

        Printer.success("%s %s have been retrieved" % (len(objects), instance.resource_name))
        Printer.output(objects, fields=args.fields, json=args.json)

    @classmethod
    def count(cls, args):
        """ Count all objects

        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        session = inspector.get_user_session(args)
        parent = inspector.get_parent(args.parent_infos, session.root_object)

        classname = instance.__class__.__name__[2:]
        plural_classname = Utils.get_entity_name_plural(classname)
        fetcher_name = Utils.get_python_name(plural_classname)
        query_parameters = cls._get_attributes(args.query_parameters)

        try:
            fetcher = getattr(parent, fetcher_name)
        except:

            if parent.rest_name == inspector._get_package().SDKInfo.root_object_class().rest_name:
                error_message = "Failed to found root object '%s'. Maybe you forgot to specify the parent using '--in [parent] [ID]' syntax ?" % (fetcher_name)
            else:
                error_message = "'%s' failed to found children '%s'. You can use command 'vsd objects -c %s' to list all possible parents" % (parent.rest_name, fetcher_name, fetcher_name)

            Printer.raise_error(error_message)

        (fetcher, parent, count) = fetcher.count(filter=args.filter, query_parameters=query_parameters)

        Printer.success("%s %s have been retrieved" % (count, instance.resource_name))
        Printer.output({instance.resource_name: count}, fields=[instance.resource_name], json=args.json)

    @classmethod
    def show(cls, args):
        """ Show object details

            Args:
                uuid: Identifier of the object to show
        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        instance.id = args.id
        inspector.get_user_session(args)

        try:
            (instance, connection) = instance.fetch()
        except Exception, e:
            Printer.raise_error("Could not find '%s' with id '%s'. Activate verbose mode for more information:\n%s" % (name, args.id, e))

        Printer.success("%s with id %s has been retrieved" % (name, args.id))
        Printer.output(instance, fields=args.fields, json=args.json, headers={"Attribute", "Value"})

    @classmethod
    def create(cls, args):
        """ Create an object

        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        session = inspector.get_user_session(args)
        parent = inspector.get_parent(args.parent_infos, session.root_object)
        attributes = cls._get_attributes(args.params)

        cls._fill_instance_with_attributes(instance, attributes)

        try:
            (instance, connection) = parent.create_child(instance)
        except Exception, e:
            Printer.raise_error("Cannot create %s:\n%s" % (name, e))

        Printer.success("%s has been created with ID=%s" % (name, instance.id))
        Printer.output(instance, json=args.json)

    @classmethod
    def update(cls, args):
        """ Update an existing object


        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        instance.id = args.id
        attributes = cls._get_attributes(args.params)

        inspector.get_user_session(args)

        try:
            (instance, connection) = instance.fetch()
        except Exception, e:
            Printer.raise_error("Could not find '%s' with id '%s'. Activate verbose mode for more information:\n%s" % (name, args.id, e))

        cls._fill_instance_with_attributes(instance, attributes)

        try:
            (instance, connection) = instance.save()
        except Exception, e:
            Printer.raise_error("Cannot update %s:\n%s" % (name, e))

        Printer.success("%s with ID=%s has been updated" % (name, instance.id))
        Printer.output(instance, json=args.json)

    @classmethod
    def assign(cls, args):
        """ Assign one or multiple new objects
            Already assigned objects will be ignored.
        """
        def internal_method(object_class, ids, current_objects):
            """ Returns final objects and nb_affected_objects """

            nb_affected_objects = 0
            final_objects = current_objects
            known_ids = [current_object.id for current_object in current_objects]

            for id in ids:
                if id not in known_ids:
                    nb_affected_objects = nb_affected_objects + 1
                    obj = object_class(id=id)
                    final_objects.append(obj)

            return (final_objects, nb_affected_objects)

        Printer.success('%s %s with IDs=%s have been assigned to %s with ID=%s' % cls._internal_assign(args, method=internal_method))

    @classmethod
    def unassign(cls, args):
        """ Unassign one or multiple new objects
            Already unassigned objects will be ignored.
        """

        def internal_method(object_class, ids, current_objects):
            """ Returns final objects and nb_affected_objects """
            nb_affected_objects = 0
            final_objects = []
            for current_object in current_objects:
                if current_object.id in ids:
                    nb_affected_objects = nb_affected_objects + 1
                else:
                    final_objects.append(current_object)

            return (final_objects, nb_affected_objects)

        Printer.success('%s %s with IDs=%s have been unassigned from %s with ID=%s' % cls._internal_assign(args, method=internal_method))

    @classmethod
    def reassign(cls, args):
        """ Change all assignations
            Previous assignations will be removed
        """
        def internal_method(object_class, ids, current_objects):
            """ Returns final objects and nb_affected_objects """

            nb_affected_objects = 0
            final_objects = []

            if ids:
                for id in ids:
                    nb_affected_objects = nb_affected_objects + 1
                    obj = object_class(id=id)
                    final_objects.append(obj)

            return (final_objects, nb_affected_objects)

        Printer.success('%s %s with IDs=%s have been reassigned to %s with ID=%s' % cls._internal_assign(args, method=internal_method))

    @classmethod
    def delete(cls, args):
        """ Delete an existing object


        """
        inspector = SDKInspector(args.version)
        name = Utils.get_singular_name(args.name)
        instance = inspector.get_instance(name)
        instance.id = args.id

        inspector.get_user_session(args)

        try:
            (instance, connection) = instance.delete()
        except Exception, e:
            Printer.raise_error("Could not delete '%s' with id '%s'. Activate verbose mode for more information:\n%s" % (name, args.id, e))

        Printer.success("%s with ID=%s has been deleted" % (name, instance.id))

    @classmethod
    def objects(cls, args):
        """ List all objects available

        """
        inspector = SDKInspector(args.version)
        objects = []

        if args.parent:
            name = Utils.get_singular_name(args.parent)
            instance = inspector.get_instance(name)

            objects = [Utils.get_entity_name_plural(name) for name in instance.children_rest_names]
        else:
            objects = inspector.get_all_objects()

        if args.child:
            child = Utils.get_singular_name(args.child)
            parents = []
            for name in objects:
                singular_name = Utils.get_singular_name(name)
                instance = inspector.get_instance(singular_name)

                if child in instance.children_rest_names:
                    parents.append(name)

            objects = parents

        if args.filter:
            objects = [name for name in objects if args.filter in name]

        objects.sort()

        Printer.success("%s objects found." % len(objects))
        Printer.output(objects, json=args.json, headers={"Name"})

    ### General methods

    @classmethod
    def _check_arguments(cls, args):
        """ Check arguments and environment variables

        """

        args.username = args.username if args.username else os.environ.get("VSD_USERNAME", None)
        args.password = args.password if args.password else os.environ.get("VSD_PASSWORD", None)
        args.api = args.api if args.api else os.environ.get("VSD_API_URL", None)
        args.version = args.version if args.version else os.environ.get("VSD_API_VERSION", None)
        args.enterprise = args.enterprise if args.enterprise else os.environ.get("VSD_ENTERPRISE", None)
        args.json = True if os.environ.get("VSD_JSON_OUTPUT") == "True" else args.json

        if args.username is None or len(args.username) == 0:
            Printer.raise_error("Please provide a username using option --username or VSD_USERNAME environment variable")

        if args.password is None or len(args.password) == 0:
            Printer.raise_error("Please provide a password using option --password or VSD_PASSWORD environment variable")

        if args.api is None or len(args.api) == 0:
            Printer.raise_error("Please provide an API URL using option --api or VSD_API_URL environment variable")

        if args.enterprise is None or len(args.enterprise) == 0:
            Printer.raise_error("Please provide an enterprise using option --enterprise or VSD_ENTERPRISE environment variable")

        setattr(args, "name", getattr(args, args.command, None))
        del(args.command)

    @classmethod
    def _get_attributes(cls, params):
        """ Transforms a list of Key=Value
            to a dictionary of attributes

            Args:
                params: list of Key=Value

            Returns:
                A dict

        """
        if not params:
            return None

        attributes = dict()

        for param in params:
            infos = param.split("=", 1)

            if len(infos) != 2:
                Printer.raise_error("Parameter %s is not in key=value format" % param)

            attribute_name = Utils.get_python_name(infos[0])
            attributes[attribute_name] = infos[1]

        return attributes

    @classmethod
    def _internal_assign(cls, args, method):
        """ Execute method to list final assignation
            Returns:
                (nb_affected_objects, assigned_objects_name, assigned_objects_ids, parent_name, parent_id)
        """
        inspector = SDKInspector(args.version)

        name = Utils.get_singular_name(args.name)
        object_class = inspector.get_class(name)
        object_type = object_class()

        session = inspector.get_user_session(args)
        resource = inspector.get_parent(args.parent_infos, session.root_object)

        classname = object_class.__name__[2:]
        plural_classname = Utils.get_entity_name_plural(classname)
        fetcher_name = Utils.get_python_name(plural_classname)

        try:
            fetcher = getattr(resource, fetcher_name)
        except:

            if resource.rest_name == 'me':
                resource_name = 'Root'

            error_message = '%s failed to found children %s.' % (resource_name, fetcher_name)
            Printer.raise_error(error_message)

        (fetcher, resource, current_objects) = fetcher.fetch()

        if current_objects is None:
            current_objects = []

        (final_objects, nb_affected_objects) = method(object_class, args.ids, current_objects)

        try:
            (references, connection) = resource.assign(final_objects, object_class)
        except Exception, e:
            Printer.raise_error('Cannot assign %s:\n%s' % (name, e))

        if args.ids is None:
            args.ids = []

        return (nb_affected_objects, args.name, args.ids, resource.rest_name, resource.id)

    @classmethod
    def _fill_instance_with_attributes(cls, instance, attributes):
        """ Fill the given instance with attributes

            Args:
                instance: the instance to fill
                attributes: the dictionary of attributes

            Returns:
                The instance filled or throw an exception

        """
        for attribute_name, attribute_value in attributes.iteritems():

            attribute = instance.get_attribute_infos(attribute_name)
            if attribute is None:
                Printer.raise_error("Attribute %s could not be found in %s" % (attribute_name, instance.rest_name))

            try:
                if attribute.attribute_type is bool:
                    value = cls._parse_bool(attribute_value)
                else:
                    value = attribute.attribute_type(attribute_value)
                setattr(instance, attribute_name, value)
            except Exception, e:
                Printer.raise_error("Attribute %s could not be set with value %s\n%s" % (attribute_name, attribute_value, e))

        # TODO-CS: Remove validation when we will have all attribute information from Swagger...
        # if not instance.validate():
        #     Printer.raise_error("Cannot validate %s for creation due to following errors\n%s" % (instance.rest_name, instance.errors))

    @classmethod
    def _parse_bool(cls, value):
        """
            Verify if a string contains a true boolean value

            Args:
                value (string): the string to check

            Returns:
                (bool): True is the string is one of "true", "t", "yes", "y", "1"
        """
        return value.lower() in ("true", "t", "yes", "y", "1")