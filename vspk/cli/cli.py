#!/usr/bin/env python
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

import argparse
import sys

sys.path.append("../")

class _HelpAction(argparse._HelpAction):

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()

        subparsers_actions = [
            action for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)]

        for subparsers_action in subparsers_actions:

            for choice, subparser in subparsers_action.choices.items():
                print("\n{}:\n{}".format(choice.upper(), "-" * (len(choice) + 1)))
                print(subparser.format_help())

        parser.exit()


def main(argv=sys.argv):

    default_parser = argparse.ArgumentParser(description="CLI for VSD", add_help=False)
    default_parser.add_argument("-v", "--verbose", help="Activate verbose mode", action="store_true")
    default_parser.add_argument("--username", help="Username to get an api key or set 'VSD_USERNAME' in your variable environment")
    default_parser.add_argument("--password", help="Password to get an api key or set 'VSD_PASSWORD' in your variable environment")
    default_parser.add_argument("--api", help="URL of the API endpoint or set 'VSD_API_URL' in your variable environment")
    default_parser.add_argument("--version", help="Version of the API or set 'VSD_API_VERSION' in your variable environment")
    default_parser.add_argument("--enterprise", help="Name of the enterprise to connect or set 'VSD_ENTERPRISE' in your variable environment")
    default_parser.add_argument("--json", help="Add this option get a JSON output or set VSD_JSON_OUTPUT=True", action="store_true")

    parser = argparse.ArgumentParser(description="CLI for VSD Software Development Kit", add_help=False)
    parser.add_argument("-h", "--help", action=_HelpAction, help="help for help if you need some help")

    subparsers = parser.add_subparsers(dest="command",
                                       title="All available commands")

    # List Command
    list_parser = subparsers.add_parser("list", description="List all objects", parents=[default_parser])
    list_parser.add_argument("list", help="Name of the object (See command 'objects' to list all objects name)")
    list_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the PARENT_NAME and PARENT_UUID")
    list_parser.add_argument("-f", "--filter", dest="filter", help="Specify a filter predicate")
    list_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)
    list_parser.add_argument("-q", "--query", dest="query_parameters", nargs="*", help="List of Key=Value that will be sent as query parameters", required=False)

    # Count Command
    count_parser = subparsers.add_parser("count", description="Count all objects", parents=[default_parser])
    count_parser.add_argument("count", help="Name of the object (See command 'objects' to list all objects name)")
    count_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the parent name and its uuid")
    count_parser.add_argument("-f", "--filter", dest="filter", help="Specify a filter predicate")
    count_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)
    count_parser.add_argument("-q", "--query", dest="query_parameters", nargs="*", help="List of Key=Value that will be sent as query parameters", required=False)

    # Show Command
    show_parser = subparsers.add_parser("show", description="Show a specific object", parents=[default_parser])
    show_parser.add_argument("show", help="Name of the object to show (See command 'objects' to list all objects name)")
    show_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)
    show_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)

    # Create Command
    create_parser = subparsers.add_parser("create", description="Create a new object", parents=[default_parser])
    create_parser.add_argument("create", help="Name of the object to create (See command 'objects' to list all objects name)")
    create_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the parent name and its uuid")
    create_parser.add_argument("-p", "--params", dest="params", nargs="*", help="List of Key=Value parameters", required=True)

    # Update Command
    update_parser = subparsers.add_parser("update", description="Update an existing object", parents=[default_parser])
    update_parser.add_argument("update", help="Name of the object to update (See command 'objects' to list all objects name)")
    update_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)
    update_parser.add_argument("-p", "--params", dest="params", nargs="*", help="List of Key=Value parameters", required=True)

    # Delete Command
    delete_parser = subparsers.add_parser("delete", description="Delete an existing object", parents=[default_parser])
    delete_parser.add_argument("delete", help="Name of the object to update (See command 'objects' to list all objects name)")
    delete_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)

    # Assign Command
    assign_parser = subparsers.add_parser('assign', description="Assign a set of new objects according to their identifier", parents=[default_parser])
    assign_parser.add_argument('assign', help='Name of the object to assign (See command `objects` to list all objects name)')
    assign_parser.add_argument('--ids', dest='ids', nargs='*', help='Identifier of the object to assign', required=True)
    assign_parser.add_argument('--to', dest='parent_infos', nargs=2, help="Specify the resource name and its uuid", required=True)

    # Unassign Command
    unassign_parser = subparsers.add_parser('unassign', description="Unassign a set of new objects according to their identifier", parents=[default_parser])
    unassign_parser.add_argument('unassign', help='Name of the object to unassign (See command `objects` to list all objects name)')
    unassign_parser.add_argument('--ids', dest='ids', nargs='*', help='Identifier of the object to unassign', required=True)
    unassign_parser.add_argument('--from', dest='parent_infos', nargs=2, help="Specify the resource name and its uuid", required=True)

    # Reassign Command
    reassign_parser = subparsers.add_parser('reassign', description="Reassign all objects according to their identifier", parents=[default_parser])
    reassign_parser.add_argument('reassign', help='Name of the object to reassign (See command `objects` to list all objects name)')
    reassign_parser.add_argument('--ids', dest='ids', nargs='*', help='Identifier of the object to reassign. If --ids is not specified, it will remove all assigned objects')
    reassign_parser.add_argument('--to', dest='parent_infos', nargs=2, help="Specify the resource name and its uuid", required=True)

    # Resources Command
    objects_parser = subparsers.add_parser("objects", description="Explore all objects", parents=[default_parser])
    objects_parser.add_argument("-f", "--filter", dest="filter", help="Filter by name (ex: -f nsg)")
    objects_parser.add_argument("-p", "--parent", dest="parent", help="Filter by parent (ex -p enterprise)")
    objects_parser.add_argument("-c", "--child", dest="child", help="Filter by children (ex: -c domain)")

    args = parser.parse_args()

    from commands import CLICommand
    CLICommand.execute(args)


if __name__ == "__main__":
    main()