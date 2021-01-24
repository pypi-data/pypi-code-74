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


class ComDayCqWcmCoreStatsPageViewStatisticsImplProperties(object):
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
        'pageviewstatistics_trackingurl': 'ConfigNodePropertyString',
        'pageviewstatistics_trackingscript_enabled': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'pageviewstatistics_trackingurl': 'pageviewstatistics.trackingurl',
        'pageviewstatistics_trackingscript_enabled': 'pageviewstatistics.trackingscript.enabled'
    }

    def __init__(self, pageviewstatistics_trackingurl=None, pageviewstatistics_trackingscript_enabled=None):  # noqa: E501
        """ComDayCqWcmCoreStatsPageViewStatisticsImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._pageviewstatistics_trackingurl = None
        self._pageviewstatistics_trackingscript_enabled = None
        self.discriminator = None

        if pageviewstatistics_trackingurl is not None:
            self.pageviewstatistics_trackingurl = pageviewstatistics_trackingurl
        if pageviewstatistics_trackingscript_enabled is not None:
            self.pageviewstatistics_trackingscript_enabled = pageviewstatistics_trackingscript_enabled

    @property
    def pageviewstatistics_trackingurl(self):
        """Gets the pageviewstatistics_trackingurl of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501


        :return: The pageviewstatistics_trackingurl of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._pageviewstatistics_trackingurl

    @pageviewstatistics_trackingurl.setter
    def pageviewstatistics_trackingurl(self, pageviewstatistics_trackingurl):
        """Sets the pageviewstatistics_trackingurl of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.


        :param pageviewstatistics_trackingurl: The pageviewstatistics_trackingurl of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._pageviewstatistics_trackingurl = pageviewstatistics_trackingurl

    @property
    def pageviewstatistics_trackingscript_enabled(self):
        """Gets the pageviewstatistics_trackingscript_enabled of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501


        :return: The pageviewstatistics_trackingscript_enabled of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._pageviewstatistics_trackingscript_enabled

    @pageviewstatistics_trackingscript_enabled.setter
    def pageviewstatistics_trackingscript_enabled(self, pageviewstatistics_trackingscript_enabled):
        """Sets the pageviewstatistics_trackingscript_enabled of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.


        :param pageviewstatistics_trackingscript_enabled: The pageviewstatistics_trackingscript_enabled of this ComDayCqWcmCoreStatsPageViewStatisticsImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._pageviewstatistics_trackingscript_enabled = pageviewstatistics_trackingscript_enabled

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
        if not isinstance(other, ComDayCqWcmCoreStatsPageViewStatisticsImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
