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


class ComDayCqWcmCoreImplLanguageManagerImplProperties(object):
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
        'langmgr_list_path': 'ConfigNodePropertyString',
        'langmgr_country_default': 'ConfigNodePropertyArray'
    }

    attribute_map = {
        'langmgr_list_path': 'langmgr.list.path',
        'langmgr_country_default': 'langmgr.country.default'
    }

    def __init__(self, langmgr_list_path=None, langmgr_country_default=None):  # noqa: E501
        """ComDayCqWcmCoreImplLanguageManagerImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._langmgr_list_path = None
        self._langmgr_country_default = None
        self.discriminator = None

        if langmgr_list_path is not None:
            self.langmgr_list_path = langmgr_list_path
        if langmgr_country_default is not None:
            self.langmgr_country_default = langmgr_country_default

    @property
    def langmgr_list_path(self):
        """Gets the langmgr_list_path of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501


        :return: The langmgr_list_path of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._langmgr_list_path

    @langmgr_list_path.setter
    def langmgr_list_path(self, langmgr_list_path):
        """Sets the langmgr_list_path of this ComDayCqWcmCoreImplLanguageManagerImplProperties.


        :param langmgr_list_path: The langmgr_list_path of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._langmgr_list_path = langmgr_list_path

    @property
    def langmgr_country_default(self):
        """Gets the langmgr_country_default of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501


        :return: The langmgr_country_default of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._langmgr_country_default

    @langmgr_country_default.setter
    def langmgr_country_default(self, langmgr_country_default):
        """Sets the langmgr_country_default of this ComDayCqWcmCoreImplLanguageManagerImplProperties.


        :param langmgr_country_default: The langmgr_country_default of this ComDayCqWcmCoreImplLanguageManagerImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._langmgr_country_default = langmgr_country_default

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
        if not isinstance(other, ComDayCqWcmCoreImplLanguageManagerImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
