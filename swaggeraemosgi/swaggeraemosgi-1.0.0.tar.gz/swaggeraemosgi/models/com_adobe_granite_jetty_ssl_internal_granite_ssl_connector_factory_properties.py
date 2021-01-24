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


class ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties(object):
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
        'com_adobe_granite_jetty_ssl_port': 'ConfigNodePropertyInteger',
        'com_adobe_granite_jetty_ssl_keystore_user': 'ConfigNodePropertyString',
        'com_adobe_granite_jetty_ssl_keystore_password': 'ConfigNodePropertyString',
        'com_adobe_granite_jetty_ssl_ciphersuites_excluded': 'ConfigNodePropertyArray',
        'com_adobe_granite_jetty_ssl_ciphersuites_included': 'ConfigNodePropertyArray',
        'com_adobe_granite_jetty_ssl_client_certificate': 'ConfigNodePropertyDropDown'
    }

    attribute_map = {
        'com_adobe_granite_jetty_ssl_port': 'com.adobe.granite.jetty.ssl.port',
        'com_adobe_granite_jetty_ssl_keystore_user': 'com.adobe.granite.jetty.ssl.keystore.user',
        'com_adobe_granite_jetty_ssl_keystore_password': 'com.adobe.granite.jetty.ssl.keystore.password',
        'com_adobe_granite_jetty_ssl_ciphersuites_excluded': 'com.adobe.granite.jetty.ssl.ciphersuites.excluded',
        'com_adobe_granite_jetty_ssl_ciphersuites_included': 'com.adobe.granite.jetty.ssl.ciphersuites.included',
        'com_adobe_granite_jetty_ssl_client_certificate': 'com.adobe.granite.jetty.ssl.client.certificate'
    }

    def __init__(self, com_adobe_granite_jetty_ssl_port=None, com_adobe_granite_jetty_ssl_keystore_user=None, com_adobe_granite_jetty_ssl_keystore_password=None, com_adobe_granite_jetty_ssl_ciphersuites_excluded=None, com_adobe_granite_jetty_ssl_ciphersuites_included=None, com_adobe_granite_jetty_ssl_client_certificate=None):  # noqa: E501
        """ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties - a model defined in OpenAPI"""  # noqa: E501

        self._com_adobe_granite_jetty_ssl_port = None
        self._com_adobe_granite_jetty_ssl_keystore_user = None
        self._com_adobe_granite_jetty_ssl_keystore_password = None
        self._com_adobe_granite_jetty_ssl_ciphersuites_excluded = None
        self._com_adobe_granite_jetty_ssl_ciphersuites_included = None
        self._com_adobe_granite_jetty_ssl_client_certificate = None
        self.discriminator = None

        if com_adobe_granite_jetty_ssl_port is not None:
            self.com_adobe_granite_jetty_ssl_port = com_adobe_granite_jetty_ssl_port
        if com_adobe_granite_jetty_ssl_keystore_user is not None:
            self.com_adobe_granite_jetty_ssl_keystore_user = com_adobe_granite_jetty_ssl_keystore_user
        if com_adobe_granite_jetty_ssl_keystore_password is not None:
            self.com_adobe_granite_jetty_ssl_keystore_password = com_adobe_granite_jetty_ssl_keystore_password
        if com_adobe_granite_jetty_ssl_ciphersuites_excluded is not None:
            self.com_adobe_granite_jetty_ssl_ciphersuites_excluded = com_adobe_granite_jetty_ssl_ciphersuites_excluded
        if com_adobe_granite_jetty_ssl_ciphersuites_included is not None:
            self.com_adobe_granite_jetty_ssl_ciphersuites_included = com_adobe_granite_jetty_ssl_ciphersuites_included
        if com_adobe_granite_jetty_ssl_client_certificate is not None:
            self.com_adobe_granite_jetty_ssl_client_certificate = com_adobe_granite_jetty_ssl_client_certificate

    @property
    def com_adobe_granite_jetty_ssl_port(self):
        """Gets the com_adobe_granite_jetty_ssl_port of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_port of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._com_adobe_granite_jetty_ssl_port

    @com_adobe_granite_jetty_ssl_port.setter
    def com_adobe_granite_jetty_ssl_port(self, com_adobe_granite_jetty_ssl_port):
        """Sets the com_adobe_granite_jetty_ssl_port of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_port: The com_adobe_granite_jetty_ssl_port of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._com_adobe_granite_jetty_ssl_port = com_adobe_granite_jetty_ssl_port

    @property
    def com_adobe_granite_jetty_ssl_keystore_user(self):
        """Gets the com_adobe_granite_jetty_ssl_keystore_user of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_keystore_user of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._com_adobe_granite_jetty_ssl_keystore_user

    @com_adobe_granite_jetty_ssl_keystore_user.setter
    def com_adobe_granite_jetty_ssl_keystore_user(self, com_adobe_granite_jetty_ssl_keystore_user):
        """Sets the com_adobe_granite_jetty_ssl_keystore_user of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_keystore_user: The com_adobe_granite_jetty_ssl_keystore_user of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._com_adobe_granite_jetty_ssl_keystore_user = com_adobe_granite_jetty_ssl_keystore_user

    @property
    def com_adobe_granite_jetty_ssl_keystore_password(self):
        """Gets the com_adobe_granite_jetty_ssl_keystore_password of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_keystore_password of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._com_adobe_granite_jetty_ssl_keystore_password

    @com_adobe_granite_jetty_ssl_keystore_password.setter
    def com_adobe_granite_jetty_ssl_keystore_password(self, com_adobe_granite_jetty_ssl_keystore_password):
        """Sets the com_adobe_granite_jetty_ssl_keystore_password of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_keystore_password: The com_adobe_granite_jetty_ssl_keystore_password of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._com_adobe_granite_jetty_ssl_keystore_password = com_adobe_granite_jetty_ssl_keystore_password

    @property
    def com_adobe_granite_jetty_ssl_ciphersuites_excluded(self):
        """Gets the com_adobe_granite_jetty_ssl_ciphersuites_excluded of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_ciphersuites_excluded of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._com_adobe_granite_jetty_ssl_ciphersuites_excluded

    @com_adobe_granite_jetty_ssl_ciphersuites_excluded.setter
    def com_adobe_granite_jetty_ssl_ciphersuites_excluded(self, com_adobe_granite_jetty_ssl_ciphersuites_excluded):
        """Sets the com_adobe_granite_jetty_ssl_ciphersuites_excluded of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_ciphersuites_excluded: The com_adobe_granite_jetty_ssl_ciphersuites_excluded of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._com_adobe_granite_jetty_ssl_ciphersuites_excluded = com_adobe_granite_jetty_ssl_ciphersuites_excluded

    @property
    def com_adobe_granite_jetty_ssl_ciphersuites_included(self):
        """Gets the com_adobe_granite_jetty_ssl_ciphersuites_included of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_ciphersuites_included of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._com_adobe_granite_jetty_ssl_ciphersuites_included

    @com_adobe_granite_jetty_ssl_ciphersuites_included.setter
    def com_adobe_granite_jetty_ssl_ciphersuites_included(self, com_adobe_granite_jetty_ssl_ciphersuites_included):
        """Sets the com_adobe_granite_jetty_ssl_ciphersuites_included of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_ciphersuites_included: The com_adobe_granite_jetty_ssl_ciphersuites_included of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._com_adobe_granite_jetty_ssl_ciphersuites_included = com_adobe_granite_jetty_ssl_ciphersuites_included

    @property
    def com_adobe_granite_jetty_ssl_client_certificate(self):
        """Gets the com_adobe_granite_jetty_ssl_client_certificate of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501


        :return: The com_adobe_granite_jetty_ssl_client_certificate of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :rtype: ConfigNodePropertyDropDown
        """
        return self._com_adobe_granite_jetty_ssl_client_certificate

    @com_adobe_granite_jetty_ssl_client_certificate.setter
    def com_adobe_granite_jetty_ssl_client_certificate(self, com_adobe_granite_jetty_ssl_client_certificate):
        """Sets the com_adobe_granite_jetty_ssl_client_certificate of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.


        :param com_adobe_granite_jetty_ssl_client_certificate: The com_adobe_granite_jetty_ssl_client_certificate of this ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties.  # noqa: E501
        :type: ConfigNodePropertyDropDown
        """

        self._com_adobe_granite_jetty_ssl_client_certificate = com_adobe_granite_jetty_ssl_client_certificate

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
        if not isinstance(other, ComAdobeGraniteJettySslInternalGraniteSslConnectorFactoryProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
