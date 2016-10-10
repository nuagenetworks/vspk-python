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

from setuptools import setup
import os

packages = ['vspk', 'vspk.cli']
resources = []
api_version_path = "./vspk"

for version_folder in os.listdir(api_version_path):

    if os.path.isfile("%s/%s" % (api_version_path, version_folder)):
        continue

    if version_folder == "cli":
        continue

    packages.append("vspk.%s" % version_folder)
    packages.append("vspk.%s.fetchers" % version_folder)

    if os.path.exists('vspk/%s/resources' % version_folder):
        resources.append(('vspk/%s/resources' % version_folder, ['vspk/%s/resources/attrs_defaults.ini' % version_folder]))

setup(
    name='vspk',
    version="4.0.5",
    url='http://nuagenetworks.net/',
    author='nuage networks',
    author_email='opensource@nuagenetworks.net',
    packages=packages,
    description='VSD Python SDK for API',
    long_description=open('README.md').read(),
    license='BSD-3',
    include_package_data=True,
    install_requires=[line for line in open('requirements.txt')],
    data_files=resources,
    entry_points={
        'console_scripts': [
            'vsd = vspk.cli.cli:main']
    }
)