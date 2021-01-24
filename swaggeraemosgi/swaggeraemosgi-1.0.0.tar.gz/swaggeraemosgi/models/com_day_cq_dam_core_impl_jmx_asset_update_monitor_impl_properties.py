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


class ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties(object):
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
        'jmx_objectname': 'ConfigNodePropertyString',
        'active': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'jmx_objectname': 'jmx.objectname',
        'active': 'active'
    }

    def __init__(self, jmx_objectname=None, active=None):  # noqa: E501
        """ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._jmx_objectname = None
        self._active = None
        self.discriminator = None

        if jmx_objectname is not None:
            self.jmx_objectname = jmx_objectname
        if active is not None:
            self.active = active

    @property
    def jmx_objectname(self):
        """Gets the jmx_objectname of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501


        :return: The jmx_objectname of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._jmx_objectname

    @jmx_objectname.setter
    def jmx_objectname(self, jmx_objectname):
        """Sets the jmx_objectname of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.


        :param jmx_objectname: The jmx_objectname of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._jmx_objectname = jmx_objectname

    @property
    def active(self):
        """Gets the active of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501


        :return: The active of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.


        :param active: The active of this ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._active = active

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
        if not isinstance(other, ComDayCqDamCoreImplJmxAssetUpdateMonitorImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
