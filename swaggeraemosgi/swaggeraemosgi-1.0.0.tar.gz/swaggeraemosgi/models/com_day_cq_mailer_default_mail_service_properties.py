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


class ComDayCqMailerDefaultMailServiceProperties(object):
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
        'smtp_host': 'ConfigNodePropertyString',
        'smtp_port': 'ConfigNodePropertyInteger',
        'smtp_user': 'ConfigNodePropertyString',
        'smtp_password': 'ConfigNodePropertyString',
        'from_address': 'ConfigNodePropertyString',
        'smtp_ssl': 'ConfigNodePropertyBoolean',
        'smtp_starttls': 'ConfigNodePropertyBoolean',
        'debug_email': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'smtp_host': 'smtp.host',
        'smtp_port': 'smtp.port',
        'smtp_user': 'smtp.user',
        'smtp_password': 'smtp.password',
        'from_address': 'from.address',
        'smtp_ssl': 'smtp.ssl',
        'smtp_starttls': 'smtp.starttls',
        'debug_email': 'debug.email'
    }

    def __init__(self, smtp_host=None, smtp_port=None, smtp_user=None, smtp_password=None, from_address=None, smtp_ssl=None, smtp_starttls=None, debug_email=None):  # noqa: E501
        """ComDayCqMailerDefaultMailServiceProperties - a model defined in OpenAPI"""  # noqa: E501

        self._smtp_host = None
        self._smtp_port = None
        self._smtp_user = None
        self._smtp_password = None
        self._from_address = None
        self._smtp_ssl = None
        self._smtp_starttls = None
        self._debug_email = None
        self.discriminator = None

        if smtp_host is not None:
            self.smtp_host = smtp_host
        if smtp_port is not None:
            self.smtp_port = smtp_port
        if smtp_user is not None:
            self.smtp_user = smtp_user
        if smtp_password is not None:
            self.smtp_password = smtp_password
        if from_address is not None:
            self.from_address = from_address
        if smtp_ssl is not None:
            self.smtp_ssl = smtp_ssl
        if smtp_starttls is not None:
            self.smtp_starttls = smtp_starttls
        if debug_email is not None:
            self.debug_email = debug_email

    @property
    def smtp_host(self):
        """Gets the smtp_host of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_host of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._smtp_host

    @smtp_host.setter
    def smtp_host(self, smtp_host):
        """Sets the smtp_host of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_host: The smtp_host of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._smtp_host = smtp_host

    @property
    def smtp_port(self):
        """Gets the smtp_port of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_port of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """Sets the smtp_port of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_port: The smtp_port of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._smtp_port = smtp_port

    @property
    def smtp_user(self):
        """Gets the smtp_user of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_user of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._smtp_user

    @smtp_user.setter
    def smtp_user(self, smtp_user):
        """Sets the smtp_user of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_user: The smtp_user of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._smtp_user = smtp_user

    @property
    def smtp_password(self):
        """Gets the smtp_password of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_password of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_password: The smtp_password of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._smtp_password = smtp_password

    @property
    def from_address(self):
        """Gets the from_address of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The from_address of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this ComDayCqMailerDefaultMailServiceProperties.


        :param from_address: The from_address of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._from_address = from_address

    @property
    def smtp_ssl(self):
        """Gets the smtp_ssl of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_ssl of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._smtp_ssl

    @smtp_ssl.setter
    def smtp_ssl(self, smtp_ssl):
        """Sets the smtp_ssl of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_ssl: The smtp_ssl of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._smtp_ssl = smtp_ssl

    @property
    def smtp_starttls(self):
        """Gets the smtp_starttls of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The smtp_starttls of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._smtp_starttls

    @smtp_starttls.setter
    def smtp_starttls(self, smtp_starttls):
        """Sets the smtp_starttls of this ComDayCqMailerDefaultMailServiceProperties.


        :param smtp_starttls: The smtp_starttls of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._smtp_starttls = smtp_starttls

    @property
    def debug_email(self):
        """Gets the debug_email of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501


        :return: The debug_email of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._debug_email

    @debug_email.setter
    def debug_email(self, debug_email):
        """Sets the debug_email of this ComDayCqMailerDefaultMailServiceProperties.


        :param debug_email: The debug_email of this ComDayCqMailerDefaultMailServiceProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._debug_email = debug_email

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
        if not isinstance(other, ComDayCqMailerDefaultMailServiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
