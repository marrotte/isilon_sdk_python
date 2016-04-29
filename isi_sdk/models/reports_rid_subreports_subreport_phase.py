# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ReportsRidSubreportsSubreportPhase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportsRidSubreportsSubreportPhase - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_time': 'int',
            'phase': 'str',
            'start_time': 'int'
        }

        self.attribute_map = {
            'end_time': 'end_time',
            'phase': 'phase',
            'start_time': 'start_time'
        }

        self._end_time = None
        self._phase = None
        self._start_time = None

    @property
    def end_time(self):
        """
        Gets the end_time of this ReportsRidSubreportsSubreportPhase.
        The time the job ended this phase.

        :return: The end_time of this ReportsRidSubreportsSubreportPhase.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ReportsRidSubreportsSubreportPhase.
        The time the job ended this phase.

        :param end_time: The end_time of this ReportsRidSubreportsSubreportPhase.
        :type: int
        """
        self._end_time = end_time

    @property
    def phase(self):
        """
        Gets the phase of this ReportsRidSubreportsSubreportPhase.
        The phase that the job was in.

        :return: The phase of this ReportsRidSubreportsSubreportPhase.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this ReportsRidSubreportsSubreportPhase.
        The phase that the job was in.

        :param phase: The phase of this ReportsRidSubreportsSubreportPhase.
        :type: str
        """
        self._phase = phase

    @property
    def start_time(self):
        """
        Gets the start_time of this ReportsRidSubreportsSubreportPhase.
        The time the job began this phase.

        :return: The start_time of this ReportsRidSubreportsSubreportPhase.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ReportsRidSubreportsSubreportPhase.
        The time the job began this phase.

        :param start_time: The start_time of this ReportsRidSubreportsSubreportPhase.
        :type: int
        """
        self._start_time = start_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
