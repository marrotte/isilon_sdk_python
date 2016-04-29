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


class NodesLnnDrivesPurposelistNodePurpose(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodesLnnDrivesPurposelistNodePurpose - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'purpose': 'str',
            'purpose_description': 'str'
        }

        self.attribute_map = {
            'purpose': 'purpose',
            'purpose_description': 'purpose_description'
        }

        self._purpose = None
        self._purpose_description = None

    @property
    def purpose(self):
        """
        Gets the purpose of this NodesLnnDrivesPurposelistNodePurpose.
        String representation of this purpose for API use.

        :return: The purpose of this NodesLnnDrivesPurposelistNodePurpose.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this NodesLnnDrivesPurposelistNodePurpose.
        String representation of this purpose for API use.

        :param purpose: The purpose of this NodesLnnDrivesPurposelistNodePurpose.
        :type: str
        """
        self._purpose = purpose

    @property
    def purpose_description(self):
        """
        Gets the purpose_description of this NodesLnnDrivesPurposelistNodePurpose.
        A description of this purpose.

        :return: The purpose_description of this NodesLnnDrivesPurposelistNodePurpose.
        :rtype: str
        """
        return self._purpose_description

    @purpose_description.setter
    def purpose_description(self, purpose_description):
        """
        Sets the purpose_description of this NodesLnnDrivesPurposelistNodePurpose.
        A description of this purpose.

        :param purpose_description: The purpose_description of this NodesLnnDrivesPurposelistNodePurpose.
        :type: str
        """
        self._purpose_description = purpose_description

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
