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

import sys
import json
from collections import OrderedDict
from colorama import init
init()
from colorama import Fore, Style
from tabulate import tabulate
from bambou import NURESTObject


class Printer(object):
    """ Print output for CLI

    """

    TABULATE_FORMAT = "psql"

    @classmethod
    def colorprint(cls, message, color=""):
        """ Print a messsage in a specific color

            Args:
                color: the color of the message
                message: the message to print

        """
        print(color + message + Style.RESET_ALL)

    @classmethod
    def raise_error(cls, message):
        """ Print an error message

            Args:
                message: the message to print

        """
        cls.colorprint("[Error] %s" % message, Fore.RED)
        sys.exit(1)

    @classmethod
    def success(cls, message):
        """ Print a succcess message

            Args:
                message: the message to print

        """
        cls.colorprint("[Success] %s" % message, Fore.GREEN)

    @classmethod
    def warn(cls, message):
        """ Print a warning message

            Args:
                message: the message to print
        """

        cls.colorprint("[WARNING] %s" % message, Fore.YELLOW)

    @classmethod
    def info(cls, message):
        """ Print a log message

            Args:
                message: the message to print
        """

        cls.colorprint("[INFO] %s" % message, Fore.CYAN)

    @classmethod
    def output(cls, data, fields=None, json=False, headers={}):
        """ Print either json or tabulate data

            Args:
                data: the data to display

        """
        if json:
            cls.json(data, fields)
        else:
            cls.tabulate(data, fields, headers)

    ### PRINTING METHODS

    @classmethod
    def json(cls, data, fields):
        """ Print a json version of data

            Args:
                data: something to display

        """
        if isinstance(data, str):
            print(data)

        elif isinstance(data, dict):
            print(json.dumps(data, indent=4))

        elif isinstance(data, list):
            results = []
            for obj in data:
                results.append(cls._object_to_dict(obj, fields))
            print(json.dumps(results, indent=4))

        else:
            print(json.dumps(cls._object_to_dict(data, fields), indent=4))

    @classmethod
    def tabulate(cls, data, fields, headers={}):
        """ Prints a tabulate version of data

            Args:
                data: something to disply

        """
        if isinstance(data, str):
            print tabulate([[data]], tablefmt=Printer.TABULATE_FORMAT)

        elif isinstance(data, dict):
            print tabulate([data], headers=headers, tablefmt=Printer.TABULATE_FORMAT)

        elif isinstance(data, list):
            results = []

            for obj in data:
                if isinstance(obj, NURESTObject):
                    results.append(cls._object_to_dict(obj, fields))
                else:
                    results.append([obj])

            print tabulate(results, headers=headers, tablefmt=Printer.TABULATE_FORMAT)

        else:
            dictionary = cls._object_to_dict(data, fields)
            result = [(key, value) for key, value in dictionary.iteritems()]
            print tabulate(result, headers=headers, tablefmt=Printer.TABULATE_FORMAT)

    @classmethod
    def _object_to_dict(cls, obj, fields=None):
        """ Get object dictionnary with filtered fields

        """
        default_dict = obj.to_dict()

        if fields is None or "ALL" in fields:
            return default_dict

        known_fields = default_dict.keys()
        ordered_dict = OrderedDict()

        for field in fields:
            if field in known_fields:
                ordered_dict[field] = default_dict[field]

        return ordered_dict