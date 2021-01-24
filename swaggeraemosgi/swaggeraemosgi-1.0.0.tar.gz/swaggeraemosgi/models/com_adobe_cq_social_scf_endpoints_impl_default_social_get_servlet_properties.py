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


class ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties(object):
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
        'sling_servlet_selectors': 'ConfigNodePropertyArray',
        'sling_servlet_extensions': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'sling_servlet_selectors': 'sling.servlet.selectors',
        'sling_servlet_extensions': 'sling.servlet.extensions'
    }

    def __init__(self, sling_servlet_selectors=None, sling_servlet_extensions=None):  # noqa: E501
        """ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties - a model defined in OpenAPI"""  # noqa: E501

        self._sling_servlet_selectors = None
        self._sling_servlet_extensions = None
        self.discriminator = None

        if sling_servlet_selectors is not None:
            self.sling_servlet_selectors = sling_servlet_selectors
        if sling_servlet_extensions is not None:
            self.sling_servlet_extensions = sling_servlet_extensions

    @property
    def sling_servlet_selectors(self):
        """Gets the sling_servlet_selectors of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501


        :return: The sling_servlet_selectors of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._sling_servlet_selectors

    @sling_servlet_selectors.setter
    def sling_servlet_selectors(self, sling_servlet_selectors):
        """Sets the sling_servlet_selectors of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.


        :param sling_servlet_selectors: The sling_servlet_selectors of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._sling_servlet_selectors = sling_servlet_selectors

    @property
    def sling_servlet_extensions(self):
        """Gets the sling_servlet_extensions of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501


        :return: The sling_servlet_extensions of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._sling_servlet_extensions

    @sling_servlet_extensions.setter
    def sling_servlet_extensions(self, sling_servlet_extensions):
        """Sets the sling_servlet_extensions of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.


        :param sling_servlet_extensions: The sling_servlet_extensions of this ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._sling_servlet_extensions = sling_servlet_extensions

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
        if not isinstance(other, ComAdobeCqSocialScfEndpointsImplDefaultSocialGetServletProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
