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


class ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties(object):
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
        'event_topics': 'ConfigNodePropertyString',
        'event_filter': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'event_topics': 'event.topics',
        'event_filter': 'event.filter'
    }

    def __init__(self, event_topics=None, event_filter=None):  # noqa: E501
        """ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties - a model defined in OpenAPI"""  # noqa: E501

        self._event_topics = None
        self._event_filter = None
        self.discriminator = None

        if event_topics is not None:
            self.event_topics = event_topics
        if event_filter is not None:
            self.event_filter = event_filter

    @property
    def event_topics(self):
        """Gets the event_topics of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501


        :return: The event_topics of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._event_topics

    @event_topics.setter
    def event_topics(self, event_topics):
        """Sets the event_topics of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.


        :param event_topics: The event_topics of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._event_topics = event_topics

    @property
    def event_filter(self):
        """Gets the event_filter of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501


        :return: The event_filter of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._event_filter

    @event_filter.setter
    def event_filter(self, event_filter):
        """Sets the event_filter of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.


        :param event_filter: The event_filter of this ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._event_filter = event_filter

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
        if not isinstance(other, ComAdobeCqSocialActivitystreamsListenerImplEventListenerHandlerProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
