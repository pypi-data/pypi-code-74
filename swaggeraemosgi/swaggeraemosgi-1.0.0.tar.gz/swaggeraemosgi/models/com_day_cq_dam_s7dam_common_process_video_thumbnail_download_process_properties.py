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


class ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties(object):
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
        'process_label': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'process_label': 'process.label'
    }

    def __init__(self, process_label=None):  # noqa: E501
        """ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties - a model defined in OpenAPI"""  # noqa: E501

        self._process_label = None
        self.discriminator = None

        if process_label is not None:
            self.process_label = process_label

    @property
    def process_label(self):
        """Gets the process_label of this ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties.  # noqa: E501


        :return: The process_label of this ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._process_label

    @process_label.setter
    def process_label(self, process_label):
        """Sets the process_label of this ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties.


        :param process_label: The process_label of this ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._process_label = process_label

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
        if not isinstance(other, ComDayCqDamS7damCommonProcessVideoThumbnailDownloadProcessProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
