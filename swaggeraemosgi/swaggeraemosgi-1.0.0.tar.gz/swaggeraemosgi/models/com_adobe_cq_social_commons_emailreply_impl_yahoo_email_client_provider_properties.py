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


class ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties(object):
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
        'priority_order': 'ConfigNodePropertyInteger',
        'reply_email_patterns': 'ConfigNodePropertyArray'
    }

    attribute_map = {
        'priority_order': 'priorityOrder',
        'reply_email_patterns': 'replyEmailPatterns'
    }

    def __init__(self, priority_order=None, reply_email_patterns=None):  # noqa: E501
        """ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties - a model defined in OpenAPI"""  # noqa: E501

        self._priority_order = None
        self._reply_email_patterns = None
        self.discriminator = None

        if priority_order is not None:
            self.priority_order = priority_order
        if reply_email_patterns is not None:
            self.reply_email_patterns = reply_email_patterns

    @property
    def priority_order(self):
        """Gets the priority_order of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501


        :return: The priority_order of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._priority_order

    @priority_order.setter
    def priority_order(self, priority_order):
        """Sets the priority_order of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.


        :param priority_order: The priority_order of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._priority_order = priority_order

    @property
    def reply_email_patterns(self):
        """Gets the reply_email_patterns of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501


        :return: The reply_email_patterns of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._reply_email_patterns

    @reply_email_patterns.setter
    def reply_email_patterns(self, reply_email_patterns):
        """Sets the reply_email_patterns of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.


        :param reply_email_patterns: The reply_email_patterns of this ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._reply_email_patterns = reply_email_patterns

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
        if not isinstance(other, ComAdobeCqSocialCommonsEmailreplyImplYahooEmailClientProviderProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
