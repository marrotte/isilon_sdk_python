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


class GroupnetsGroupnetSubnetCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GroupnetsGroupnetSubnetCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'vlan_id': 'int',
            'addr_family': 'str',
            'name': 'str',
            'sc_service_addr': 'str',
            'description': 'str',
            'prefixlen': 'int',
            'gateway_priority': 'int',
            'dsr_addrs': 'list[str]',
            'vlan_enabled': 'bool',
            'gateway': 'str',
            'mtu': 'int'
        }

        self.attribute_map = {
            'vlan_id': 'vlan_id',
            'addr_family': 'addr_family',
            'name': 'name',
            'sc_service_addr': 'sc_service_addr',
            'description': 'description',
            'prefixlen': 'prefixlen',
            'gateway_priority': 'gateway_priority',
            'dsr_addrs': 'dsr_addrs',
            'vlan_enabled': 'vlan_enabled',
            'gateway': 'gateway',
            'mtu': 'mtu'
        }

        self._vlan_id = None
        self._addr_family = None
        self._name = None
        self._sc_service_addr = None
        self._description = None
        self._prefixlen = None
        self._gateway_priority = None
        self._dsr_addrs = None
        self._vlan_enabled = None
        self._gateway = None
        self._mtu = None

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this GroupnetsGroupnetSubnetCreateParams.
        VLAN ID for all interfaces in the subnet.

        :return: The vlan_id of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this GroupnetsGroupnetSubnetCreateParams.
        VLAN ID for all interfaces in the subnet.

        :param vlan_id: The vlan_id of this GroupnetsGroupnetSubnetCreateParams.
        :type: int
        """
        self._vlan_id = vlan_id

    @property
    def addr_family(self):
        """
        Gets the addr_family of this GroupnetsGroupnetSubnetCreateParams.
        IP address format.

        :return: The addr_family of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._addr_family

    @addr_family.setter
    def addr_family(self, addr_family):
        """
        Sets the addr_family of this GroupnetsGroupnetSubnetCreateParams.
        IP address format.

        :param addr_family: The addr_family of this GroupnetsGroupnetSubnetCreateParams.
        :type: str
        """
        allowed_values = ["ipv4", "ipv6"]
        if addr_family not in allowed_values:
            raise ValueError(
                "Invalid value for `addr_family`, must be one of {0}"
                .format(allowed_values)
            )
        self._addr_family = addr_family

    @property
    def name(self):
        """
        Gets the name of this GroupnetsGroupnetSubnetCreateParams.
        The name of the subnet.

        :return: The name of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupnetsGroupnetSubnetCreateParams.
        The name of the subnet.

        :param name: The name of this GroupnetsGroupnetSubnetCreateParams.
        :type: str
        """
        self._name = name

    @property
    def sc_service_addr(self):
        """
        Gets the sc_service_addr of this GroupnetsGroupnetSubnetCreateParams.
        The address that SmartConnect listens for DNS requests.

        :return: The sc_service_addr of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._sc_service_addr

    @sc_service_addr.setter
    def sc_service_addr(self, sc_service_addr):
        """
        Sets the sc_service_addr of this GroupnetsGroupnetSubnetCreateParams.
        The address that SmartConnect listens for DNS requests.

        :param sc_service_addr: The sc_service_addr of this GroupnetsGroupnetSubnetCreateParams.
        :type: str
        """
        self._sc_service_addr = sc_service_addr

    @property
    def description(self):
        """
        Gets the description of this GroupnetsGroupnetSubnetCreateParams.
        A description of the subnet.

        :return: The description of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupnetsGroupnetSubnetCreateParams.
        A description of the subnet.

        :param description: The description of this GroupnetsGroupnetSubnetCreateParams.
        :type: str
        """
        self._description = description

    @property
    def prefixlen(self):
        """
        Gets the prefixlen of this GroupnetsGroupnetSubnetCreateParams.
        Subnet Prefix Length.

        :return: The prefixlen of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """
        Sets the prefixlen of this GroupnetsGroupnetSubnetCreateParams.
        Subnet Prefix Length.

        :param prefixlen: The prefixlen of this GroupnetsGroupnetSubnetCreateParams.
        :type: int
        """
        self._prefixlen = prefixlen

    @property
    def gateway_priority(self):
        """
        Gets the gateway_priority of this GroupnetsGroupnetSubnetCreateParams.
        Gateway priority.

        :return: The gateway_priority of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._gateway_priority

    @gateway_priority.setter
    def gateway_priority(self, gateway_priority):
        """
        Sets the gateway_priority of this GroupnetsGroupnetSubnetCreateParams.
        Gateway priority.

        :param gateway_priority: The gateway_priority of this GroupnetsGroupnetSubnetCreateParams.
        :type: int
        """
        self._gateway_priority = gateway_priority

    @property
    def dsr_addrs(self):
        """
        Gets the dsr_addrs of this GroupnetsGroupnetSubnetCreateParams.
        List of Direct Server Return addresses.

        :return: The dsr_addrs of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: list[str]
        """
        return self._dsr_addrs

    @dsr_addrs.setter
    def dsr_addrs(self, dsr_addrs):
        """
        Sets the dsr_addrs of this GroupnetsGroupnetSubnetCreateParams.
        List of Direct Server Return addresses.

        :param dsr_addrs: The dsr_addrs of this GroupnetsGroupnetSubnetCreateParams.
        :type: list[str]
        """
        self._dsr_addrs = dsr_addrs

    @property
    def vlan_enabled(self):
        """
        Gets the vlan_enabled of this GroupnetsGroupnetSubnetCreateParams.
        VLAN tagging enabled or disabled.

        :return: The vlan_enabled of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: bool
        """
        return self._vlan_enabled

    @vlan_enabled.setter
    def vlan_enabled(self, vlan_enabled):
        """
        Sets the vlan_enabled of this GroupnetsGroupnetSubnetCreateParams.
        VLAN tagging enabled or disabled.

        :param vlan_enabled: The vlan_enabled of this GroupnetsGroupnetSubnetCreateParams.
        :type: bool
        """
        self._vlan_enabled = vlan_enabled

    @property
    def gateway(self):
        """
        Gets the gateway of this GroupnetsGroupnetSubnetCreateParams.
        Gateway IP address.

        :return: The gateway of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this GroupnetsGroupnetSubnetCreateParams.
        Gateway IP address.

        :param gateway: The gateway of this GroupnetsGroupnetSubnetCreateParams.
        :type: str
        """
        self._gateway = gateway

    @property
    def mtu(self):
        """
        Gets the mtu of this GroupnetsGroupnetSubnetCreateParams.
        MTU of the subnet.

        :return: The mtu of this GroupnetsGroupnetSubnetCreateParams.
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """
        Sets the mtu of this GroupnetsGroupnetSubnetCreateParams.
        MTU of the subnet.

        :param mtu: The mtu of this GroupnetsGroupnetSubnetCreateParams.
        :type: int
        """
        self._mtu = mtu

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
