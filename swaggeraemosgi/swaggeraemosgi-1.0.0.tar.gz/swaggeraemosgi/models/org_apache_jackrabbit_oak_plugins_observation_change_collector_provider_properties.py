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


class OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties(object):
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
        'max_items': 'ConfigNodePropertyInteger',
        'max_path_depth': 'ConfigNodePropertyInteger',
        'enabled': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'max_items': 'maxItems',
        'max_path_depth': 'maxPathDepth',
        'enabled': 'enabled'
    }

    def __init__(self, max_items=None, max_path_depth=None, enabled=None):  # noqa: E501
        """OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties - a model defined in OpenAPI"""  # noqa: E501

        self._max_items = None
        self._max_path_depth = None
        self._enabled = None
        self.discriminator = None

        if max_items is not None:
            self.max_items = max_items
        if max_path_depth is not None:
            self.max_path_depth = max_path_depth
        if enabled is not None:
            self.enabled = enabled

    @property
    def max_items(self):
        """Gets the max_items of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501


        :return: The max_items of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.


        :param max_items: The max_items of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._max_items = max_items

    @property
    def max_path_depth(self):
        """Gets the max_path_depth of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501


        :return: The max_path_depth of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._max_path_depth

    @max_path_depth.setter
    def max_path_depth(self, max_path_depth):
        """Sets the max_path_depth of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.


        :param max_path_depth: The max_path_depth of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._max_path_depth = max_path_depth

    @property
    def enabled(self):
        """Gets the enabled of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501


        :return: The enabled of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.


        :param enabled: The enabled of this OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._enabled = enabled

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
        if not isinstance(other, OrgApacheJackrabbitOakPluginsObservationChangeCollectorProviderProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
