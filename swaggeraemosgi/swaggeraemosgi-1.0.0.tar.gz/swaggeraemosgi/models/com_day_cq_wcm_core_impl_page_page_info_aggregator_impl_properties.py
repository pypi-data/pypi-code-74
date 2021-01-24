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


class ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties(object):
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
        'page_info_provider_property_regex_default': 'ConfigNodePropertyString',
        'page_info_provider_property_name': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'page_info_provider_property_regex_default': 'page.info.provider.property.regex.default',
        'page_info_provider_property_name': 'page.info.provider.property.name'
    }

    def __init__(self, page_info_provider_property_regex_default=None, page_info_provider_property_name=None):  # noqa: E501
        """ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._page_info_provider_property_regex_default = None
        self._page_info_provider_property_name = None
        self.discriminator = None

        if page_info_provider_property_regex_default is not None:
            self.page_info_provider_property_regex_default = page_info_provider_property_regex_default
        if page_info_provider_property_name is not None:
            self.page_info_provider_property_name = page_info_provider_property_name

    @property
    def page_info_provider_property_regex_default(self):
        """Gets the page_info_provider_property_regex_default of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501


        :return: The page_info_provider_property_regex_default of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._page_info_provider_property_regex_default

    @page_info_provider_property_regex_default.setter
    def page_info_provider_property_regex_default(self, page_info_provider_property_regex_default):
        """Sets the page_info_provider_property_regex_default of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.


        :param page_info_provider_property_regex_default: The page_info_provider_property_regex_default of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._page_info_provider_property_regex_default = page_info_provider_property_regex_default

    @property
    def page_info_provider_property_name(self):
        """Gets the page_info_provider_property_name of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501


        :return: The page_info_provider_property_name of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._page_info_provider_property_name

    @page_info_provider_property_name.setter
    def page_info_provider_property_name(self, page_info_provider_property_name):
        """Sets the page_info_provider_property_name of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.


        :param page_info_provider_property_name: The page_info_provider_property_name of this ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._page_info_provider_property_name = page_info_provider_property_name

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
        if not isinstance(other, ComDayCqWcmCoreImplPagePageInfoAggregatorImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
