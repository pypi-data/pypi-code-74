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


class ComAdobeCqScheduledExporterImplScheduledExporterImplProperties(object):
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
        'include_paths': 'ConfigNodePropertyArray',
        'exporter_user': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'include_paths': 'include.paths',
        'exporter_user': 'exporter.user'
    }

    def __init__(self, include_paths=None, exporter_user=None):  # noqa: E501
        """ComAdobeCqScheduledExporterImplScheduledExporterImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._include_paths = None
        self._exporter_user = None
        self.discriminator = None

        if include_paths is not None:
            self.include_paths = include_paths
        if exporter_user is not None:
            self.exporter_user = exporter_user

    @property
    def include_paths(self):
        """Gets the include_paths of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501


        :return: The include_paths of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._include_paths

    @include_paths.setter
    def include_paths(self, include_paths):
        """Sets the include_paths of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.


        :param include_paths: The include_paths of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._include_paths = include_paths

    @property
    def exporter_user(self):
        """Gets the exporter_user of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501


        :return: The exporter_user of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._exporter_user

    @exporter_user.setter
    def exporter_user(self, exporter_user):
        """Sets the exporter_user of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.


        :param exporter_user: The exporter_user of this ComAdobeCqScheduledExporterImplScheduledExporterImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._exporter_user = exporter_user

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
        if not isinstance(other, ComAdobeCqScheduledExporterImplScheduledExporterImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
