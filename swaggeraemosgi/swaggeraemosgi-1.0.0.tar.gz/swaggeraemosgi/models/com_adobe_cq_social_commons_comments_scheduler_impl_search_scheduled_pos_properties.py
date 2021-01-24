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


class ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties(object):
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
        'enable_scheduled_posts_search': 'ConfigNodePropertyBoolean',
        'number_of_minutes': 'ConfigNodePropertyInteger',
        'max_search_limit': 'ConfigNodePropertyInteger'
    }

    attribute_map = {
        'enable_scheduled_posts_search': 'enableScheduledPostsSearch',
        'number_of_minutes': 'numberOfMinutes',
        'max_search_limit': 'maxSearchLimit'
    }

    def __init__(self, enable_scheduled_posts_search=None, number_of_minutes=None, max_search_limit=None):  # noqa: E501
        """ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties - a model defined in OpenAPI"""  # noqa: E501

        self._enable_scheduled_posts_search = None
        self._number_of_minutes = None
        self._max_search_limit = None
        self.discriminator = None

        if enable_scheduled_posts_search is not None:
            self.enable_scheduled_posts_search = enable_scheduled_posts_search
        if number_of_minutes is not None:
            self.number_of_minutes = number_of_minutes
        if max_search_limit is not None:
            self.max_search_limit = max_search_limit

    @property
    def enable_scheduled_posts_search(self):
        """Gets the enable_scheduled_posts_search of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501


        :return: The enable_scheduled_posts_search of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._enable_scheduled_posts_search

    @enable_scheduled_posts_search.setter
    def enable_scheduled_posts_search(self, enable_scheduled_posts_search):
        """Sets the enable_scheduled_posts_search of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.


        :param enable_scheduled_posts_search: The enable_scheduled_posts_search of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._enable_scheduled_posts_search = enable_scheduled_posts_search

    @property
    def number_of_minutes(self):
        """Gets the number_of_minutes of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501


        :return: The number_of_minutes of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._number_of_minutes

    @number_of_minutes.setter
    def number_of_minutes(self, number_of_minutes):
        """Sets the number_of_minutes of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.


        :param number_of_minutes: The number_of_minutes of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._number_of_minutes = number_of_minutes

    @property
    def max_search_limit(self):
        """Gets the max_search_limit of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501


        :return: The max_search_limit of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._max_search_limit

    @max_search_limit.setter
    def max_search_limit(self, max_search_limit):
        """Sets the max_search_limit of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.


        :param max_search_limit: The max_search_limit of this ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._max_search_limit = max_search_limit

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
        if not isinstance(other, ComAdobeCqSocialCommonsCommentsSchedulerImplSearchScheduledPosProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
