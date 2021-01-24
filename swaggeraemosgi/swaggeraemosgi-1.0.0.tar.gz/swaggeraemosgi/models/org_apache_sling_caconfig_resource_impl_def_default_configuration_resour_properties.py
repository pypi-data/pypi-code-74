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


class OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties(object):
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
        'enabled': 'ConfigNodePropertyBoolean',
        'config_path': 'ConfigNodePropertyString',
        'fallback_paths': 'ConfigNodePropertyArray',
        'config_collection_inheritance_property_names': 'ConfigNodePropertyArray'
    }

    attribute_map = {
        'enabled': 'enabled',
        'config_path': 'configPath',
        'fallback_paths': 'fallbackPaths',
        'config_collection_inheritance_property_names': 'configCollectionInheritancePropertyNames'
    }

    def __init__(self, enabled=None, config_path=None, fallback_paths=None, config_collection_inheritance_property_names=None):  # noqa: E501
        """OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties - a model defined in OpenAPI"""  # noqa: E501

        self._enabled = None
        self._config_path = None
        self._fallback_paths = None
        self._config_collection_inheritance_property_names = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if config_path is not None:
            self.config_path = config_path
        if fallback_paths is not None:
            self.fallback_paths = fallback_paths
        if config_collection_inheritance_property_names is not None:
            self.config_collection_inheritance_property_names = config_collection_inheritance_property_names

    @property
    def enabled(self):
        """Gets the enabled of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501


        :return: The enabled of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.


        :param enabled: The enabled of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._enabled = enabled

    @property
    def config_path(self):
        """Gets the config_path of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501


        :return: The config_path of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._config_path

    @config_path.setter
    def config_path(self, config_path):
        """Sets the config_path of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.


        :param config_path: The config_path of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._config_path = config_path

    @property
    def fallback_paths(self):
        """Gets the fallback_paths of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501


        :return: The fallback_paths of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._fallback_paths

    @fallback_paths.setter
    def fallback_paths(self, fallback_paths):
        """Sets the fallback_paths of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.


        :param fallback_paths: The fallback_paths of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._fallback_paths = fallback_paths

    @property
    def config_collection_inheritance_property_names(self):
        """Gets the config_collection_inheritance_property_names of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501


        :return: The config_collection_inheritance_property_names of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._config_collection_inheritance_property_names

    @config_collection_inheritance_property_names.setter
    def config_collection_inheritance_property_names(self, config_collection_inheritance_property_names):
        """Sets the config_collection_inheritance_property_names of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.


        :param config_collection_inheritance_property_names: The config_collection_inheritance_property_names of this OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._config_collection_inheritance_property_names = config_collection_inheritance_property_names

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
        if not isinstance(other, OrgApacheSlingCaconfigResourceImplDefDefaultConfigurationResourProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
