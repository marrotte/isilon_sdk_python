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


class CloudPoolCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudPoolCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'accounts': 'list[str]',
            'birth_cluster_id': 'str',
            'type': 'str',
            'vendor': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'accounts': 'accounts',
            'birth_cluster_id': 'birth_cluster_id',
            'type': 'type',
            'vendor': 'vendor'
        }

        self._name = None
        self._description = None
        self._accounts = None
        self._birth_cluster_id = None
        self._type = None
        self._vendor = None

    @property
    def name(self):
        """
        Gets the name of this CloudPoolCreateParams.
        A unique name for this pool

        :return: The name of this CloudPoolCreateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudPoolCreateParams.
        A unique name for this pool

        :param name: The name of this CloudPoolCreateParams.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CloudPoolCreateParams.
        A brief description of this pool

        :return: The description of this CloudPoolCreateParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CloudPoolCreateParams.
        A brief description of this pool

        :param description: The description of this CloudPoolCreateParams.
        :type: str
        """
        self._description = description

    @property
    def accounts(self):
        """
        Gets the accounts of this CloudPoolCreateParams.
        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.

        :return: The accounts of this CloudPoolCreateParams.
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """
        Sets the accounts of this CloudPoolCreateParams.
        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.

        :param accounts: The accounts of this CloudPoolCreateParams.
        :type: list[str]
        """
        self._accounts = accounts

    @property
    def birth_cluster_id(self):
        """
        Gets the birth_cluster_id of this CloudPoolCreateParams.
        The guid of the cluster where this pool was created

        :return: The birth_cluster_id of this CloudPoolCreateParams.
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """
        Sets the birth_cluster_id of this CloudPoolCreateParams.
        The guid of the cluster where this pool was created

        :param birth_cluster_id: The birth_cluster_id of this CloudPoolCreateParams.
        :type: str
        """
        self._birth_cluster_id = birth_cluster_id

    @property
    def type(self):
        """
        Gets the type of this CloudPoolCreateParams.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :return: The type of this CloudPoolCreateParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudPoolCreateParams.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :param type: The type of this CloudPoolCreateParams.
        :type: str
        """
        allowed_values = ["isilon", "ecs", "ecs2", "azure", "s3", "ran"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def vendor(self):
        """
        Gets the vendor of this CloudPoolCreateParams.
        A string identifier of the cloud services vendor

        :return: The vendor of this CloudPoolCreateParams.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this CloudPoolCreateParams.
        A string identifier of the cloud services vendor

        :param vendor: The vendor of this CloudPoolCreateParams.
        :type: str
        """
        self._vendor = vendor

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
