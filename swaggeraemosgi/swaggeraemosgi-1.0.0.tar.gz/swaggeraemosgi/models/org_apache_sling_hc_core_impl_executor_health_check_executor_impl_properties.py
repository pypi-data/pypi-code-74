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


class OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties(object):
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
        'timeout_in_ms': 'ConfigNodePropertyInteger',
        'long_running_future_threshold_for_critical_ms': 'ConfigNodePropertyInteger',
        'result_cache_ttl_in_ms': 'ConfigNodePropertyInteger'
    }

    attribute_map = {
        'timeout_in_ms': 'timeoutInMs',
        'long_running_future_threshold_for_critical_ms': 'longRunningFutureThresholdForCriticalMs',
        'result_cache_ttl_in_ms': 'resultCacheTtlInMs'
    }

    def __init__(self, timeout_in_ms=None, long_running_future_threshold_for_critical_ms=None, result_cache_ttl_in_ms=None):  # noqa: E501
        """OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._timeout_in_ms = None
        self._long_running_future_threshold_for_critical_ms = None
        self._result_cache_ttl_in_ms = None
        self.discriminator = None

        if timeout_in_ms is not None:
            self.timeout_in_ms = timeout_in_ms
        if long_running_future_threshold_for_critical_ms is not None:
            self.long_running_future_threshold_for_critical_ms = long_running_future_threshold_for_critical_ms
        if result_cache_ttl_in_ms is not None:
            self.result_cache_ttl_in_ms = result_cache_ttl_in_ms

    @property
    def timeout_in_ms(self):
        """Gets the timeout_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501


        :return: The timeout_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._timeout_in_ms

    @timeout_in_ms.setter
    def timeout_in_ms(self, timeout_in_ms):
        """Sets the timeout_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.


        :param timeout_in_ms: The timeout_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._timeout_in_ms = timeout_in_ms

    @property
    def long_running_future_threshold_for_critical_ms(self):
        """Gets the long_running_future_threshold_for_critical_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501


        :return: The long_running_future_threshold_for_critical_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._long_running_future_threshold_for_critical_ms

    @long_running_future_threshold_for_critical_ms.setter
    def long_running_future_threshold_for_critical_ms(self, long_running_future_threshold_for_critical_ms):
        """Sets the long_running_future_threshold_for_critical_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.


        :param long_running_future_threshold_for_critical_ms: The long_running_future_threshold_for_critical_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._long_running_future_threshold_for_critical_ms = long_running_future_threshold_for_critical_ms

    @property
    def result_cache_ttl_in_ms(self):
        """Gets the result_cache_ttl_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501


        :return: The result_cache_ttl_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._result_cache_ttl_in_ms

    @result_cache_ttl_in_ms.setter
    def result_cache_ttl_in_ms(self, result_cache_ttl_in_ms):
        """Sets the result_cache_ttl_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.


        :param result_cache_ttl_in_ms: The result_cache_ttl_in_ms of this OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._result_cache_ttl_in_ms = result_cache_ttl_in_ms

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
        if not isinstance(other, OrgApacheSlingHcCoreImplExecutorHealthCheckExecutorImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
