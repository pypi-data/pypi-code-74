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


class ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties(object):
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
        'cache_enable': 'ConfigNodePropertyBoolean',
        'cache_root_paths': 'ConfigNodePropertyArray',
        'cache_max_size': 'ConfigNodePropertyInteger',
        'cache_max_entries': 'ConfigNodePropertyInteger'
    }

    attribute_map = {
        'cache_enable': 'cache.enable',
        'cache_root_paths': 'cache.rootPaths',
        'cache_max_size': 'cache.maxSize',
        'cache_max_entries': 'cache.maxEntries'
    }

    def __init__(self, cache_enable=None, cache_root_paths=None, cache_max_size=None, cache_max_entries=None):  # noqa: E501
        """ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties - a model defined in OpenAPI"""  # noqa: E501

        self._cache_enable = None
        self._cache_root_paths = None
        self._cache_max_size = None
        self._cache_max_entries = None
        self.discriminator = None

        if cache_enable is not None:
            self.cache_enable = cache_enable
        if cache_root_paths is not None:
            self.cache_root_paths = cache_root_paths
        if cache_max_size is not None:
            self.cache_max_size = cache_max_size
        if cache_max_entries is not None:
            self.cache_max_entries = cache_max_entries

    @property
    def cache_enable(self):
        """Gets the cache_enable of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501


        :return: The cache_enable of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._cache_enable

    @cache_enable.setter
    def cache_enable(self, cache_enable):
        """Sets the cache_enable of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.


        :param cache_enable: The cache_enable of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._cache_enable = cache_enable

    @property
    def cache_root_paths(self):
        """Gets the cache_root_paths of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501


        :return: The cache_root_paths of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._cache_root_paths

    @cache_root_paths.setter
    def cache_root_paths(self, cache_root_paths):
        """Sets the cache_root_paths of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.


        :param cache_root_paths: The cache_root_paths of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._cache_root_paths = cache_root_paths

    @property
    def cache_max_size(self):
        """Gets the cache_max_size of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501


        :return: The cache_max_size of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._cache_max_size

    @cache_max_size.setter
    def cache_max_size(self, cache_max_size):
        """Sets the cache_max_size of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.


        :param cache_max_size: The cache_max_size of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._cache_max_size = cache_max_size

    @property
    def cache_max_entries(self):
        """Gets the cache_max_entries of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501


        :return: The cache_max_entries of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._cache_max_entries

    @cache_max_entries.setter
    def cache_max_entries(self, cache_max_entries):
        """Sets the cache_max_entries of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.


        :param cache_max_entries: The cache_max_entries of this ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._cache_max_entries = cache_max_entries

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
        if not isinstance(other, ComAdobeCqDamS7imagingImplPsPlatformServerServletProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
