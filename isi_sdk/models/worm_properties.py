# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WormProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'autocommit_delay': 'int',
        'domain_id': 'int',
        'domain_path': 'str',
        'worm_committed': 'bool',
        'worm_ctime': 'int',
        'worm_override_retention_date': 'str',
        'worm_override_retention_date_val': 'int',
        'worm_retention_date': 'str',
        'worm_retention_date_val': 'int'
    }

    attribute_map = {
        'autocommit_delay': 'autocommit_delay',
        'domain_id': 'domain_id',
        'domain_path': 'domain_path',
        'worm_committed': 'worm_committed',
        'worm_ctime': 'worm_ctime',
        'worm_override_retention_date': 'worm_override_retention_date',
        'worm_override_retention_date_val': 'worm_override_retention_date_val',
        'worm_retention_date': 'worm_retention_date',
        'worm_retention_date_val': 'worm_retention_date_val'
    }

    def __init__(self, autocommit_delay=None, domain_id=None, domain_path=None, worm_committed=None, worm_ctime=None, worm_override_retention_date=None, worm_override_retention_date_val=None, worm_retention_date=None, worm_retention_date_val=None):  # noqa: E501
        """WormProperties - a model defined in Swagger"""  # noqa: E501

        self._autocommit_delay = None
        self._domain_id = None
        self._domain_path = None
        self._worm_committed = None
        self._worm_ctime = None
        self._worm_override_retention_date = None
        self._worm_override_retention_date_val = None
        self._worm_retention_date = None
        self._worm_retention_date_val = None
        self.discriminator = None

        if autocommit_delay is not None:
            self.autocommit_delay = autocommit_delay
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_path is not None:
            self.domain_path = domain_path
        if worm_committed is not None:
            self.worm_committed = worm_committed
        if worm_ctime is not None:
            self.worm_ctime = worm_ctime
        if worm_override_retention_date is not None:
            self.worm_override_retention_date = worm_override_retention_date
        if worm_override_retention_date_val is not None:
            self.worm_override_retention_date_val = worm_override_retention_date_val
        if worm_retention_date is not None:
            self.worm_retention_date = worm_retention_date
        if worm_retention_date_val is not None:
            self.worm_retention_date_val = worm_retention_date_val

    @property
    def autocommit_delay(self):
        """Gets the autocommit_delay of this WormProperties.  # noqa: E501

        Autocommit delay.  # noqa: E501

        :return: The autocommit_delay of this WormProperties.  # noqa: E501
        :rtype: int
        """
        return self._autocommit_delay

    @autocommit_delay.setter
    def autocommit_delay(self, autocommit_delay):
        """Sets the autocommit_delay of this WormProperties.

        Autocommit delay.  # noqa: E501

        :param autocommit_delay: The autocommit_delay of this WormProperties.  # noqa: E501
        :type: int
        """

        self._autocommit_delay = autocommit_delay

    @property
    def domain_id(self):
        """Gets the domain_id of this WormProperties.  # noqa: E501

        WORM domain ID.  # noqa: E501

        :return: The domain_id of this WormProperties.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this WormProperties.

        WORM domain ID.  # noqa: E501

        :param domain_id: The domain_id of this WormProperties.  # noqa: E501
        :type: int
        """

        self._domain_id = domain_id

    @property
    def domain_path(self):
        """Gets the domain_path of this WormProperties.  # noqa: E501

        WORM domain path.  # noqa: E501

        :return: The domain_path of this WormProperties.  # noqa: E501
        :rtype: str
        """
        return self._domain_path

    @domain_path.setter
    def domain_path(self, domain_path):
        """Sets the domain_path of this WormProperties.

        WORM domain path.  # noqa: E501

        :param domain_path: The domain_path of this WormProperties.  # noqa: E501
        :type: str
        """

        self._domain_path = domain_path

    @property
    def worm_committed(self):
        """Gets the worm_committed of this WormProperties.  # noqa: E501

        Indicates whether the file was committed to the WORM state.  # noqa: E501

        :return: The worm_committed of this WormProperties.  # noqa: E501
        :rtype: bool
        """
        return self._worm_committed

    @worm_committed.setter
    def worm_committed(self, worm_committed):
        """Sets the worm_committed of this WormProperties.

        Indicates whether the file was committed to the WORM state.  # noqa: E501

        :param worm_committed: The worm_committed of this WormProperties.  # noqa: E501
        :type: bool
        """

        self._worm_committed = worm_committed

    @property
    def worm_ctime(self):
        """Gets the worm_ctime of this WormProperties.  # noqa: E501

        WORM change time.  # noqa: E501

        :return: The worm_ctime of this WormProperties.  # noqa: E501
        :rtype: int
        """
        return self._worm_ctime

    @worm_ctime.setter
    def worm_ctime(self, worm_ctime):
        """Sets the worm_ctime of this WormProperties.

        WORM change time.  # noqa: E501

        :param worm_ctime: The worm_ctime of this WormProperties.  # noqa: E501
        :type: int
        """

        self._worm_ctime = worm_ctime

    @property
    def worm_override_retention_date(self):
        """Gets the worm_override_retention_date of this WormProperties.  # noqa: E501

        Provides the override retention date that is set on the SmartLock directory where the file resides.  # noqa: E501

        :return: The worm_override_retention_date of this WormProperties.  # noqa: E501
        :rtype: str
        """
        return self._worm_override_retention_date

    @worm_override_retention_date.setter
    def worm_override_retention_date(self, worm_override_retention_date):
        """Sets the worm_override_retention_date of this WormProperties.

        Provides the override retention date that is set on the SmartLock directory where the file resides.  # noqa: E501

        :param worm_override_retention_date: The worm_override_retention_date of this WormProperties.  # noqa: E501
        :type: str
        """

        self._worm_override_retention_date = worm_override_retention_date

    @property
    def worm_override_retention_date_val(self):
        """Gets the worm_override_retention_date_val of this WormProperties.  # noqa: E501

        Provides the override retention date in seconds from UNIX Epoch or UTC.  # noqa: E501

        :return: The worm_override_retention_date_val of this WormProperties.  # noqa: E501
        :rtype: int
        """
        return self._worm_override_retention_date_val

    @worm_override_retention_date_val.setter
    def worm_override_retention_date_val(self, worm_override_retention_date_val):
        """Sets the worm_override_retention_date_val of this WormProperties.

        Provides the override retention date in seconds from UNIX Epoch or UTC.  # noqa: E501

        :param worm_override_retention_date_val: The worm_override_retention_date_val of this WormProperties.  # noqa: E501
        :type: int
        """

        self._worm_override_retention_date_val = worm_override_retention_date_val

    @property
    def worm_retention_date(self):
        """Gets the worm_retention_date of this WormProperties.  # noqa: E501

        Provides the retention expiration date in Coordinated Universal Time (such as UTC/GMT).  # noqa: E501

        :return: The worm_retention_date of this WormProperties.  # noqa: E501
        :rtype: str
        """
        return self._worm_retention_date

    @worm_retention_date.setter
    def worm_retention_date(self, worm_retention_date):
        """Sets the worm_retention_date of this WormProperties.

        Provides the retention expiration date in Coordinated Universal Time (such as UTC/GMT).  # noqa: E501

        :param worm_retention_date: The worm_retention_date of this WormProperties.  # noqa: E501
        :type: str
        """

        self._worm_retention_date = worm_retention_date

    @property
    def worm_retention_date_val(self):
        """Gets the worm_retention_date_val of this WormProperties.  # noqa: E501

        Provides the retention expiration date in seconds from UNIX Epoch or UTC.  # noqa: E501

        :return: The worm_retention_date_val of this WormProperties.  # noqa: E501
        :rtype: int
        """
        return self._worm_retention_date_val

    @worm_retention_date_val.setter
    def worm_retention_date_val(self, worm_retention_date_val):
        """Sets the worm_retention_date_val of this WormProperties.

        Provides the retention expiration date in seconds from UNIX Epoch or UTC.  # noqa: E501

        :param worm_retention_date_val: The worm_retention_date_val of this WormProperties.  # noqa: E501
        :type: int
        """

        self._worm_retention_date_val = worm_retention_date_val

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WormProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
