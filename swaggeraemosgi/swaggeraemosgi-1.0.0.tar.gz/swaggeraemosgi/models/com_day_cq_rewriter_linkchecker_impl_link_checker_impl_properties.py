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


class ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties(object):
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
        'scheduler_period': 'ConfigNodePropertyInteger',
        'scheduler_concurrent': 'ConfigNodePropertyBoolean',
        'service_bad_link_tolerance_interval': 'ConfigNodePropertyInteger',
        'service_check_override_patterns': 'ConfigNodePropertyArray',
        'service_cache_broken_internal_links': 'ConfigNodePropertyBoolean',
        'service_special_link_prefix': 'ConfigNodePropertyArray',
        'service_special_link_patterns': 'ConfigNodePropertyArray'
    }

    attribute_map = {
        'scheduler_period': 'scheduler.period',
        'scheduler_concurrent': 'scheduler.concurrent',
        'service_bad_link_tolerance_interval': 'service.bad_link_tolerance_interval',
        'service_check_override_patterns': 'service.check_override_patterns',
        'service_cache_broken_internal_links': 'service.cache_broken_internal_links',
        'service_special_link_prefix': 'service.special_link_prefix',
        'service_special_link_patterns': 'service.special_link_patterns'
    }

    def __init__(self, scheduler_period=None, scheduler_concurrent=None, service_bad_link_tolerance_interval=None, service_check_override_patterns=None, service_cache_broken_internal_links=None, service_special_link_prefix=None, service_special_link_patterns=None):  # noqa: E501
        """ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._scheduler_period = None
        self._scheduler_concurrent = None
        self._service_bad_link_tolerance_interval = None
        self._service_check_override_patterns = None
        self._service_cache_broken_internal_links = None
        self._service_special_link_prefix = None
        self._service_special_link_patterns = None
        self.discriminator = None

        if scheduler_period is not None:
            self.scheduler_period = scheduler_period
        if scheduler_concurrent is not None:
            self.scheduler_concurrent = scheduler_concurrent
        if service_bad_link_tolerance_interval is not None:
            self.service_bad_link_tolerance_interval = service_bad_link_tolerance_interval
        if service_check_override_patterns is not None:
            self.service_check_override_patterns = service_check_override_patterns
        if service_cache_broken_internal_links is not None:
            self.service_cache_broken_internal_links = service_cache_broken_internal_links
        if service_special_link_prefix is not None:
            self.service_special_link_prefix = service_special_link_prefix
        if service_special_link_patterns is not None:
            self.service_special_link_patterns = service_special_link_patterns

    @property
    def scheduler_period(self):
        """Gets the scheduler_period of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The scheduler_period of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._scheduler_period

    @scheduler_period.setter
    def scheduler_period(self, scheduler_period):
        """Sets the scheduler_period of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param scheduler_period: The scheduler_period of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._scheduler_period = scheduler_period

    @property
    def scheduler_concurrent(self):
        """Gets the scheduler_concurrent of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The scheduler_concurrent of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._scheduler_concurrent

    @scheduler_concurrent.setter
    def scheduler_concurrent(self, scheduler_concurrent):
        """Sets the scheduler_concurrent of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param scheduler_concurrent: The scheduler_concurrent of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._scheduler_concurrent = scheduler_concurrent

    @property
    def service_bad_link_tolerance_interval(self):
        """Gets the service_bad_link_tolerance_interval of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The service_bad_link_tolerance_interval of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._service_bad_link_tolerance_interval

    @service_bad_link_tolerance_interval.setter
    def service_bad_link_tolerance_interval(self, service_bad_link_tolerance_interval):
        """Sets the service_bad_link_tolerance_interval of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param service_bad_link_tolerance_interval: The service_bad_link_tolerance_interval of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._service_bad_link_tolerance_interval = service_bad_link_tolerance_interval

    @property
    def service_check_override_patterns(self):
        """Gets the service_check_override_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The service_check_override_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._service_check_override_patterns

    @service_check_override_patterns.setter
    def service_check_override_patterns(self, service_check_override_patterns):
        """Sets the service_check_override_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param service_check_override_patterns: The service_check_override_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._service_check_override_patterns = service_check_override_patterns

    @property
    def service_cache_broken_internal_links(self):
        """Gets the service_cache_broken_internal_links of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The service_cache_broken_internal_links of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._service_cache_broken_internal_links

    @service_cache_broken_internal_links.setter
    def service_cache_broken_internal_links(self, service_cache_broken_internal_links):
        """Sets the service_cache_broken_internal_links of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param service_cache_broken_internal_links: The service_cache_broken_internal_links of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._service_cache_broken_internal_links = service_cache_broken_internal_links

    @property
    def service_special_link_prefix(self):
        """Gets the service_special_link_prefix of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The service_special_link_prefix of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._service_special_link_prefix

    @service_special_link_prefix.setter
    def service_special_link_prefix(self, service_special_link_prefix):
        """Sets the service_special_link_prefix of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param service_special_link_prefix: The service_special_link_prefix of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._service_special_link_prefix = service_special_link_prefix

    @property
    def service_special_link_patterns(self):
        """Gets the service_special_link_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501


        :return: The service_special_link_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._service_special_link_patterns

    @service_special_link_patterns.setter
    def service_special_link_patterns(self, service_special_link_patterns):
        """Sets the service_special_link_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.


        :param service_special_link_patterns: The service_special_link_patterns of this ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._service_special_link_patterns = service_special_link_patterns

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
        if not isinstance(other, ComDayCqRewriterLinkcheckerImplLinkCheckerImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
