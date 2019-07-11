# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
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



from bambou import NURESTObject


class NUDownloadProgress(NURESTObject):
    """ Represents a DownloadProgress in the VSD

        Notes:
            An object representing the progress of gateway image download
    """

    __rest_name__ = "None"
    __resource_name__ = "None"

    

    def __init__(self, **kwargs):
        """ Initializes a DownloadProgress instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> downloadprogress = NUDownloadProgress(id=u'xxxx-xxx-xxx-xxx', name=u'DownloadProgress')
                >>> downloadprogress = NUDownloadProgress(data=my_dict)
        """

        super(NUDownloadProgress, self).__init__()

        # Read/Write Attributes
        
        self._percentage = None
        self._time_left = None
        self._time_spent = None
        self._image_file_name = None
        self._image_version = None
        self._start_time = None
        self._current_speed = None
        self._average_speed = None
        
        self.expose_attribute(local_name="percentage", remote_name="percentage", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="time_left", remote_name="timeLeft", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="time_spent", remote_name="timeSpent", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="image_file_name", remote_name="imageFileName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="image_version", remote_name="imageVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="start_time", remote_name="startTime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="current_speed", remote_name="currentSpeed", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="average_speed", remote_name="averageSpeed", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def percentage(self):
        """ Get percentage value.

            Notes:
                The total percentage of image download transfer that was completed

                
        """
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        """ Set percentage value.

            Notes:
                The total percentage of image download transfer that was completed

                
        """
        self._percentage = value

    
    @property
    def time_left(self):
        """ Get time_left value.

            Notes:
                Time remaining (in HH:MM:SS) for the download of image

                
                This attribute is named `timeLeft` in VSD API.
                
        """
        return self._time_left

    @time_left.setter
    def time_left(self, value):
        """ Set time_left value.

            Notes:
                Time remaining (in HH:MM:SS) for the download of image

                
                This attribute is named `timeLeft` in VSD API.
                
        """
        self._time_left = value

    
    @property
    def time_spent(self):
        """ Get time_spent value.

            Notes:
                Time spent (in HH:MM:SS) for the download of image

                
                This attribute is named `timeSpent` in VSD API.
                
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, value):
        """ Set time_spent value.

            Notes:
                Time spent (in HH:MM:SS) for the download of image

                
                This attribute is named `timeSpent` in VSD API.
                
        """
        self._time_spent = value

    
    @property
    def image_file_name(self):
        """ Get image_file_name value.

            Notes:
                Name of the image file getting downloaded, as specified in upgrade meta-data file.

                
                This attribute is named `imageFileName` in VSD API.
                
        """
        return self._image_file_name

    @image_file_name.setter
    def image_file_name(self, value):
        """ Set image_file_name value.

            Notes:
                Name of the image file getting downloaded, as specified in upgrade meta-data file.

                
                This attribute is named `imageFileName` in VSD API.
                
        """
        self._image_file_name = value

    
    @property
    def image_version(self):
        """ Get image_version value.

            Notes:
                The version of image getting downloaded, as specified in upgrade meta-data file.

                
                This attribute is named `imageVersion` in VSD API.
                
        """
        return self._image_version

    @image_version.setter
    def image_version(self, value):
        """ Set image_version value.

            Notes:
                The version of image getting downloaded, as specified in upgrade meta-data file.

                
                This attribute is named `imageVersion` in VSD API.
                
        """
        self._image_version = value

    
    @property
    def start_time(self):
        """ Get start_time value.

            Notes:
                Time when the download of image was started

                
                This attribute is named `startTime` in VSD API.
                
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """ Set start_time value.

            Notes:
                Time when the download of image was started

                
                This attribute is named `startTime` in VSD API.
                
        """
        self._start_time = value

    
    @property
    def current_speed(self):
        """ Get current_speed value.

            Notes:
                Current speed in kilobyte per second (kB/s) of the image download

                
                This attribute is named `currentSpeed` in VSD API.
                
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        """ Set current_speed value.

            Notes:
                Current speed in kilobyte per second (kB/s) of the image download

                
                This attribute is named `currentSpeed` in VSD API.
                
        """
        self._current_speed = value

    
    @property
    def average_speed(self):
        """ Get average_speed value.

            Notes:
                Average speed in kilobyte per second (kB/s) of the image download

                
                This attribute is named `averageSpeed` in VSD API.
                
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, value):
        """ Set average_speed value.

            Notes:
                Average speed in kilobyte per second (kB/s) of the image download

                
                This attribute is named `averageSpeed` in VSD API.
                
        """
        self._average_speed = value

    

    