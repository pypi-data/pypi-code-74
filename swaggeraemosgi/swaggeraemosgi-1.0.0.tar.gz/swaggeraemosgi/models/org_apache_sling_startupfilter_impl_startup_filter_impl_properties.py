# coding: utf-8

"""
    Adobe Experience Manager OSGI config (AEM) API

    Swagger AEM OSGI is an OpenAPI specification for Adobe Experience Manager (AEM) OSGI Configurations API  # noqa: E501

    OpenAPI spec version: 1.0.0-pre.0
    Contact: opensource@shinesolutions.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OrgApacheSlingStartupfilterImplStartupFilterImplProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'active_by_default': 'ConfigNodePropertyBoolean',
        'default_message': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'active_by_default': 'active.by.default',
        'default_message': 'default.message'
    }

    def __init__(self, active_by_default=None, default_message=None):  # noqa: E501
        """OrgApacheSlingStartupfilterImplStartupFilterImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._active_by_default = None
        self._default_message = None
        self.discriminator = None

        if active_by_default is not None:
            self.active_by_default = active_by_default
        if default_message is not None:
            self.default_message = default_message

    @property
    def active_by_default(self):
        """Gets the active_by_default of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501


        :return: The active_by_default of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._active_by_default

    @active_by_default.setter
    def active_by_default(self, active_by_default):
        """Sets the active_by_default of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.


        :param active_by_default: The active_by_default of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._active_by_default = active_by_default

    @property
    def default_message(self):
        """Gets the default_message of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501


        :return: The default_message of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._default_message

    @default_message.setter
    def default_message(self, default_message):
        """Sets the default_message of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.


        :param default_message: The default_message of this OrgApacheSlingStartupfilterImplStartupFilterImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._default_message = default_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, OrgApacheSlingStartupfilterImplStartupFilterImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
