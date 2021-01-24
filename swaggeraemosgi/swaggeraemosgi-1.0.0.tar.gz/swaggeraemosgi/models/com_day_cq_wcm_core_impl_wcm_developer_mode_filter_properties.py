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


class ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties(object):
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
        'wcmdevmodefilter_enabled': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'wcmdevmodefilter_enabled': 'wcmdevmodefilter.enabled'
    }

    def __init__(self, wcmdevmodefilter_enabled=None):  # noqa: E501
        """ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties - a model defined in OpenAPI"""  # noqa: E501

        self._wcmdevmodefilter_enabled = None
        self.discriminator = None

        if wcmdevmodefilter_enabled is not None:
            self.wcmdevmodefilter_enabled = wcmdevmodefilter_enabled

    @property
    def wcmdevmodefilter_enabled(self):
        """Gets the wcmdevmodefilter_enabled of this ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties.  # noqa: E501


        :return: The wcmdevmodefilter_enabled of this ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._wcmdevmodefilter_enabled

    @wcmdevmodefilter_enabled.setter
    def wcmdevmodefilter_enabled(self, wcmdevmodefilter_enabled):
        """Sets the wcmdevmodefilter_enabled of this ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties.


        :param wcmdevmodefilter_enabled: The wcmdevmodefilter_enabled of this ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._wcmdevmodefilter_enabled = wcmdevmodefilter_enabled

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
        if not isinstance(other, ComDayCqWcmCoreImplWCMDeveloperModeFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
