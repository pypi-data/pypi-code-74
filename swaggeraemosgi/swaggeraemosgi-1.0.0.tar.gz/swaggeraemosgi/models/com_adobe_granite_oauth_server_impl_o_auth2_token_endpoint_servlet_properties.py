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


class ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties(object):
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
        'oauth_issuer': 'ConfigNodePropertyString',
        'oauth_access_token_expires_in': 'ConfigNodePropertyString',
        'osgi_http_whiteboard_servlet_pattern': 'ConfigNodePropertyString',
        'osgi_http_whiteboard_context_select': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'oauth_issuer': 'oauth.issuer',
        'oauth_access_token_expires_in': 'oauth.access.token.expires.in',
        'osgi_http_whiteboard_servlet_pattern': 'osgi.http.whiteboard.servlet.pattern',
        'osgi_http_whiteboard_context_select': 'osgi.http.whiteboard.context.select'
    }

    def __init__(self, oauth_issuer=None, oauth_access_token_expires_in=None, osgi_http_whiteboard_servlet_pattern=None, osgi_http_whiteboard_context_select=None):  # noqa: E501
        """ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties - a model defined in OpenAPI"""  # noqa: E501

        self._oauth_issuer = None
        self._oauth_access_token_expires_in = None
        self._osgi_http_whiteboard_servlet_pattern = None
        self._osgi_http_whiteboard_context_select = None
        self.discriminator = None

        if oauth_issuer is not None:
            self.oauth_issuer = oauth_issuer
        if oauth_access_token_expires_in is not None:
            self.oauth_access_token_expires_in = oauth_access_token_expires_in
        if osgi_http_whiteboard_servlet_pattern is not None:
            self.osgi_http_whiteboard_servlet_pattern = osgi_http_whiteboard_servlet_pattern
        if osgi_http_whiteboard_context_select is not None:
            self.osgi_http_whiteboard_context_select = osgi_http_whiteboard_context_select

    @property
    def oauth_issuer(self):
        """Gets the oauth_issuer of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501


        :return: The oauth_issuer of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._oauth_issuer

    @oauth_issuer.setter
    def oauth_issuer(self, oauth_issuer):
        """Sets the oauth_issuer of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.


        :param oauth_issuer: The oauth_issuer of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._oauth_issuer = oauth_issuer

    @property
    def oauth_access_token_expires_in(self):
        """Gets the oauth_access_token_expires_in of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501


        :return: The oauth_access_token_expires_in of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._oauth_access_token_expires_in

    @oauth_access_token_expires_in.setter
    def oauth_access_token_expires_in(self, oauth_access_token_expires_in):
        """Sets the oauth_access_token_expires_in of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.


        :param oauth_access_token_expires_in: The oauth_access_token_expires_in of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._oauth_access_token_expires_in = oauth_access_token_expires_in

    @property
    def osgi_http_whiteboard_servlet_pattern(self):
        """Gets the osgi_http_whiteboard_servlet_pattern of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501


        :return: The osgi_http_whiteboard_servlet_pattern of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._osgi_http_whiteboard_servlet_pattern

    @osgi_http_whiteboard_servlet_pattern.setter
    def osgi_http_whiteboard_servlet_pattern(self, osgi_http_whiteboard_servlet_pattern):
        """Sets the osgi_http_whiteboard_servlet_pattern of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.


        :param osgi_http_whiteboard_servlet_pattern: The osgi_http_whiteboard_servlet_pattern of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._osgi_http_whiteboard_servlet_pattern = osgi_http_whiteboard_servlet_pattern

    @property
    def osgi_http_whiteboard_context_select(self):
        """Gets the osgi_http_whiteboard_context_select of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501


        :return: The osgi_http_whiteboard_context_select of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._osgi_http_whiteboard_context_select

    @osgi_http_whiteboard_context_select.setter
    def osgi_http_whiteboard_context_select(self, osgi_http_whiteboard_context_select):
        """Sets the osgi_http_whiteboard_context_select of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.


        :param osgi_http_whiteboard_context_select: The osgi_http_whiteboard_context_select of this ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._osgi_http_whiteboard_context_select = osgi_http_whiteboard_context_select

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
        if not isinstance(other, ComAdobeGraniteOauthServerImplOAuth2TokenEndpointServletProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
