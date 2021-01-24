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


class ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo(object):
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
        'pid': 'str',
        'title': 'str',
        'description': 'str',
        'properties': 'ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplProperties'
    }

    attribute_map = {
        'pid': 'pid',
        'title': 'title',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, pid=None, title=None, description=None, properties=None):  # noqa: E501
        """ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo - a model defined in OpenAPI"""  # noqa: E501

        self._pid = None
        self._title = None
        self._description = None
        self._properties = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def pid(self):
        """Gets the pid of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501


        :return: The pid of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.


        :param pid: The pid of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def title(self):
        """Gets the title of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501


        :return: The title of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.


        :param title: The title of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501


        :return: The description of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.


        :param description: The description of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501


        :return: The properties of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :rtype: ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.


        :param properties: The properties of this ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo.  # noqa: E501
        :type: ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplProperties
        """

        self._properties = properties

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
        if not isinstance(other, ComAdobeGraniteRestImplApiEndpointResourceProviderFactoryImplInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
