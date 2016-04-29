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


class StoragepoolStoragepool(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragepoolStoragepool - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'can_enable_l3': 'bool',
            'children': 'list[str]',
            'id': 'int',
            'l3': 'bool',
            'l3_status': 'str',
            'lnns': 'list[int]',
            'manual': 'bool',
            'name': 'str',
            'protection_policy': 'str',
            'type': 'str',
            'usage': 'StoragepoolTierUsage'
        }

        self.attribute_map = {
            'can_enable_l3': 'can_enable_l3',
            'children': 'children',
            'id': 'id',
            'l3': 'l3',
            'l3_status': 'l3_status',
            'lnns': 'lnns',
            'manual': 'manual',
            'name': 'name',
            'protection_policy': 'protection_policy',
            'type': 'type',
            'usage': 'usage'
        }

        self._can_enable_l3 = None
        self._children = None
        self._id = None
        self._l3 = None
        self._l3_status = None
        self._lnns = None
        self._manual = None
        self._name = None
        self._protection_policy = None
        self._type = None
        self._usage = None

    @property
    def can_enable_l3(self):
        """
        Gets the can_enable_l3 of this StoragepoolStoragepool.
        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.

        :return: The can_enable_l3 of this StoragepoolStoragepool.
        :rtype: bool
        """
        return self._can_enable_l3

    @can_enable_l3.setter
    def can_enable_l3(self, can_enable_l3):
        """
        Sets the can_enable_l3 of this StoragepoolStoragepool.
        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.

        :param can_enable_l3: The can_enable_l3 of this StoragepoolStoragepool.
        :type: bool
        """
        self._can_enable_l3 = can_enable_l3

    @property
    def children(self):
        """
        Gets the children of this StoragepoolStoragepool.
        The names or IDs of the pool's children.

        :return: The children of this StoragepoolStoragepool.
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this StoragepoolStoragepool.
        The names or IDs of the pool's children.

        :param children: The children of this StoragepoolStoragepool.
        :type: list[str]
        """
        self._children = children

    @property
    def id(self):
        """
        Gets the id of this StoragepoolStoragepool.
        The system ID given to the pool.

        :return: The id of this StoragepoolStoragepool.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoragepoolStoragepool.
        The system ID given to the pool.

        :param id: The id of this StoragepoolStoragepool.
        :type: int
        """
        self._id = id

    @property
    def l3(self):
        """
        Gets the l3 of this StoragepoolStoragepool.
        Use SSDs in this node pool for L3 cache.

        :return: The l3 of this StoragepoolStoragepool.
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """
        Sets the l3 of this StoragepoolStoragepool.
        Use SSDs in this node pool for L3 cache.

        :param l3: The l3 of this StoragepoolStoragepool.
        :type: bool
        """
        self._l3 = l3

    @property
    def l3_status(self):
        """
        Gets the l3_status of this StoragepoolStoragepool.
        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.

        :return: The l3_status of this StoragepoolStoragepool.
        :rtype: str
        """
        return self._l3_status

    @l3_status.setter
    def l3_status(self, l3_status):
        """
        Sets the l3_status of this StoragepoolStoragepool.
        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.

        :param l3_status: The l3_status of this StoragepoolStoragepool.
        :type: str
        """
        allowed_values = ["l3", "storage", "migrating"]
        if l3_status not in allowed_values:
            raise ValueError(
                "Invalid value for `l3_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._l3_status = l3_status

    @property
    def lnns(self):
        """
        Gets the lnns of this StoragepoolStoragepool.
        The nodes that are part of this pool.

        :return: The lnns of this StoragepoolStoragepool.
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """
        Sets the lnns of this StoragepoolStoragepool.
        The nodes that are part of this pool.

        :param lnns: The lnns of this StoragepoolStoragepool.
        :type: list[int]
        """
        self._lnns = lnns

    @property
    def manual(self):
        """
        Gets the manual of this StoragepoolStoragepool.
        Whether or not the node pool is manually managed.

        :return: The manual of this StoragepoolStoragepool.
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """
        Sets the manual of this StoragepoolStoragepool.
        Whether or not the node pool is manually managed.

        :param manual: The manual of this StoragepoolStoragepool.
        :type: bool
        """
        self._manual = manual

    @property
    def name(self):
        """
        Gets the name of this StoragepoolStoragepool.
        The pool name.

        :return: The name of this StoragepoolStoragepool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragepoolStoragepool.
        The pool name.

        :param name: The name of this StoragepoolStoragepool.
        :type: str
        """
        self._name = name

    @property
    def protection_policy(self):
        """
        Gets the protection_policy of this StoragepoolStoragepool.
        The underlying protection policy.

        :return: The protection_policy of this StoragepoolStoragepool.
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """
        Sets the protection_policy of this StoragepoolStoragepool.
        The underlying protection policy.

        :param protection_policy: The protection_policy of this StoragepoolStoragepool.
        :type: str
        """
        self._protection_policy = protection_policy

    @property
    def type(self):
        """
        Gets the type of this StoragepoolStoragepool.
        The pool type.

        :return: The type of this StoragepoolStoragepool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StoragepoolStoragepool.
        The pool type.

        :param type: The type of this StoragepoolStoragepool.
        :type: str
        """
        allowed_values = ["tier", "nodepool"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def usage(self):
        """
        Gets the usage of this StoragepoolStoragepool.
        Total pool usage.

        :return: The usage of this StoragepoolStoragepool.
        :rtype: StoragepoolTierUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this StoragepoolStoragepool.
        Total pool usage.

        :param usage: The usage of this StoragepoolStoragepool.
        :type: StoragepoolTierUsage
        """
        self._usage = usage

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
