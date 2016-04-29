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


class NodesLnnPartitionsNodePartition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodesLnnPartitionsNodePartition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'block_size': 'int',
            'capacity': 'int',
            'component_devices': 'str',
            'mount_point': 'str',
            'percent_used': 'str',
            'statfs': 'NodesLnnPartitionsNodePartitionStatfs',
            'used': 'int'
        }

        self.attribute_map = {
            'block_size': 'block_size',
            'capacity': 'capacity',
            'component_devices': 'component_devices',
            'mount_point': 'mount_point',
            'percent_used': 'percent_used',
            'statfs': 'statfs',
            'used': 'used'
        }

        self._block_size = None
        self._capacity = None
        self._component_devices = None
        self._mount_point = None
        self._percent_used = None
        self._statfs = None
        self._used = None

    @property
    def block_size(self):
        """
        Gets the block_size of this NodesLnnPartitionsNodePartition.
        The block size used for the reported partition information.

        :return: The block_size of this NodesLnnPartitionsNodePartition.
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """
        Sets the block_size of this NodesLnnPartitionsNodePartition.
        The block size used for the reported partition information.

        :param block_size: The block_size of this NodesLnnPartitionsNodePartition.
        :type: int
        """
        self._block_size = block_size

    @property
    def capacity(self):
        """
        Gets the capacity of this NodesLnnPartitionsNodePartition.
        Total blocks on this file system partition.

        :return: The capacity of this NodesLnnPartitionsNodePartition.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this NodesLnnPartitionsNodePartition.
        Total blocks on this file system partition.

        :param capacity: The capacity of this NodesLnnPartitionsNodePartition.
        :type: int
        """
        self._capacity = capacity

    @property
    def component_devices(self):
        """
        Gets the component_devices of this NodesLnnPartitionsNodePartition.
        Comma separated list of devices used for this file system partition.

        :return: The component_devices of this NodesLnnPartitionsNodePartition.
        :rtype: str
        """
        return self._component_devices

    @component_devices.setter
    def component_devices(self, component_devices):
        """
        Sets the component_devices of this NodesLnnPartitionsNodePartition.
        Comma separated list of devices used for this file system partition.

        :param component_devices: The component_devices of this NodesLnnPartitionsNodePartition.
        :type: str
        """
        self._component_devices = component_devices

    @property
    def mount_point(self):
        """
        Gets the mount_point of this NodesLnnPartitionsNodePartition.
        Directory on which this partition is mounted.

        :return: The mount_point of this NodesLnnPartitionsNodePartition.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this NodesLnnPartitionsNodePartition.
        Directory on which this partition is mounted.

        :param mount_point: The mount_point of this NodesLnnPartitionsNodePartition.
        :type: str
        """
        self._mount_point = mount_point

    @property
    def percent_used(self):
        """
        Gets the percent_used of this NodesLnnPartitionsNodePartition.
        Used blocks on this file system partition, expressed as a percentage.

        :return: The percent_used of this NodesLnnPartitionsNodePartition.
        :rtype: str
        """
        return self._percent_used

    @percent_used.setter
    def percent_used(self, percent_used):
        """
        Sets the percent_used of this NodesLnnPartitionsNodePartition.
        Used blocks on this file system partition, expressed as a percentage.

        :param percent_used: The percent_used of this NodesLnnPartitionsNodePartition.
        :type: str
        """
        self._percent_used = percent_used

    @property
    def statfs(self):
        """
        Gets the statfs of this NodesLnnPartitionsNodePartition.
        System partition details as provided by statfs(2).

        :return: The statfs of this NodesLnnPartitionsNodePartition.
        :rtype: NodesLnnPartitionsNodePartitionStatfs
        """
        return self._statfs

    @statfs.setter
    def statfs(self, statfs):
        """
        Sets the statfs of this NodesLnnPartitionsNodePartition.
        System partition details as provided by statfs(2).

        :param statfs: The statfs of this NodesLnnPartitionsNodePartition.
        :type: NodesLnnPartitionsNodePartitionStatfs
        """
        self._statfs = statfs

    @property
    def used(self):
        """
        Gets the used of this NodesLnnPartitionsNodePartition.
        Used blocks on this file system partition.

        :return: The used of this NodesLnnPartitionsNodePartition.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this NodesLnnPartitionsNodePartition.
        Used blocks on this file system partition.

        :param used: The used of this NodesLnnPartitionsNodePartition.
        :type: int
        """
        self._used = used

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
