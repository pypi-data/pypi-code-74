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


class OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties(object):
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
        'org_apache_sling_commons_log_level': 'ConfigNodePropertyDropDown',
        'org_apache_sling_commons_log_file': 'ConfigNodePropertyString',
        'org_apache_sling_commons_log_pattern': 'ConfigNodePropertyString',
        'org_apache_sling_commons_log_names': 'ConfigNodePropertyArray',
        'org_apache_sling_commons_log_additiv': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'org_apache_sling_commons_log_level': 'org.apache.sling.commons.log.level',
        'org_apache_sling_commons_log_file': 'org.apache.sling.commons.log.file',
        'org_apache_sling_commons_log_pattern': 'org.apache.sling.commons.log.pattern',
        'org_apache_sling_commons_log_names': 'org.apache.sling.commons.log.names',
        'org_apache_sling_commons_log_additiv': 'org.apache.sling.commons.log.additiv'
    }

    def __init__(self, org_apache_sling_commons_log_level=None, org_apache_sling_commons_log_file=None, org_apache_sling_commons_log_pattern=None, org_apache_sling_commons_log_names=None, org_apache_sling_commons_log_additiv=None):  # noqa: E501
        """OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties - a model defined in OpenAPI"""  # noqa: E501

        self._org_apache_sling_commons_log_level = None
        self._org_apache_sling_commons_log_file = None
        self._org_apache_sling_commons_log_pattern = None
        self._org_apache_sling_commons_log_names = None
        self._org_apache_sling_commons_log_additiv = None
        self.discriminator = None

        if org_apache_sling_commons_log_level is not None:
            self.org_apache_sling_commons_log_level = org_apache_sling_commons_log_level
        if org_apache_sling_commons_log_file is not None:
            self.org_apache_sling_commons_log_file = org_apache_sling_commons_log_file
        if org_apache_sling_commons_log_pattern is not None:
            self.org_apache_sling_commons_log_pattern = org_apache_sling_commons_log_pattern
        if org_apache_sling_commons_log_names is not None:
            self.org_apache_sling_commons_log_names = org_apache_sling_commons_log_names
        if org_apache_sling_commons_log_additiv is not None:
            self.org_apache_sling_commons_log_additiv = org_apache_sling_commons_log_additiv

    @property
    def org_apache_sling_commons_log_level(self):
        """Gets the org_apache_sling_commons_log_level of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501


        :return: The org_apache_sling_commons_log_level of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyDropDown
        """
        return self._org_apache_sling_commons_log_level

    @org_apache_sling_commons_log_level.setter
    def org_apache_sling_commons_log_level(self, org_apache_sling_commons_log_level):
        """Sets the org_apache_sling_commons_log_level of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.


        :param org_apache_sling_commons_log_level: The org_apache_sling_commons_log_level of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyDropDown
        """

        self._org_apache_sling_commons_log_level = org_apache_sling_commons_log_level

    @property
    def org_apache_sling_commons_log_file(self):
        """Gets the org_apache_sling_commons_log_file of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501


        :return: The org_apache_sling_commons_log_file of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._org_apache_sling_commons_log_file

    @org_apache_sling_commons_log_file.setter
    def org_apache_sling_commons_log_file(self, org_apache_sling_commons_log_file):
        """Sets the org_apache_sling_commons_log_file of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.


        :param org_apache_sling_commons_log_file: The org_apache_sling_commons_log_file of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._org_apache_sling_commons_log_file = org_apache_sling_commons_log_file

    @property
    def org_apache_sling_commons_log_pattern(self):
        """Gets the org_apache_sling_commons_log_pattern of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501


        :return: The org_apache_sling_commons_log_pattern of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._org_apache_sling_commons_log_pattern

    @org_apache_sling_commons_log_pattern.setter
    def org_apache_sling_commons_log_pattern(self, org_apache_sling_commons_log_pattern):
        """Sets the org_apache_sling_commons_log_pattern of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.


        :param org_apache_sling_commons_log_pattern: The org_apache_sling_commons_log_pattern of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._org_apache_sling_commons_log_pattern = org_apache_sling_commons_log_pattern

    @property
    def org_apache_sling_commons_log_names(self):
        """Gets the org_apache_sling_commons_log_names of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501


        :return: The org_apache_sling_commons_log_names of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._org_apache_sling_commons_log_names

    @org_apache_sling_commons_log_names.setter
    def org_apache_sling_commons_log_names(self, org_apache_sling_commons_log_names):
        """Sets the org_apache_sling_commons_log_names of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.


        :param org_apache_sling_commons_log_names: The org_apache_sling_commons_log_names of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._org_apache_sling_commons_log_names = org_apache_sling_commons_log_names

    @property
    def org_apache_sling_commons_log_additiv(self):
        """Gets the org_apache_sling_commons_log_additiv of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501


        :return: The org_apache_sling_commons_log_additiv of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._org_apache_sling_commons_log_additiv

    @org_apache_sling_commons_log_additiv.setter
    def org_apache_sling_commons_log_additiv(self, org_apache_sling_commons_log_additiv):
        """Sets the org_apache_sling_commons_log_additiv of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.


        :param org_apache_sling_commons_log_additiv: The org_apache_sling_commons_log_additiv of this OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._org_apache_sling_commons_log_additiv = org_apache_sling_commons_log_additiv

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
        if not isinstance(other, OrgApacheSlingCommonsLogLogManagerFactoryConfigProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
