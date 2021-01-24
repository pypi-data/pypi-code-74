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


class ComDayCqDamCoreImplUnzipUnzipConfigProperties(object):
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
        'cq_dam_config_unzip_maxuncompressedsize': 'ConfigNodePropertyInteger',
        'cq_dam_config_unzip_encoding': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'cq_dam_config_unzip_maxuncompressedsize': 'cq.dam.config.unzip.maxuncompressedsize',
        'cq_dam_config_unzip_encoding': 'cq.dam.config.unzip.encoding'
    }

    def __init__(self, cq_dam_config_unzip_maxuncompressedsize=None, cq_dam_config_unzip_encoding=None):  # noqa: E501
        """ComDayCqDamCoreImplUnzipUnzipConfigProperties - a model defined in OpenAPI"""  # noqa: E501

        self._cq_dam_config_unzip_maxuncompressedsize = None
        self._cq_dam_config_unzip_encoding = None
        self.discriminator = None

        if cq_dam_config_unzip_maxuncompressedsize is not None:
            self.cq_dam_config_unzip_maxuncompressedsize = cq_dam_config_unzip_maxuncompressedsize
        if cq_dam_config_unzip_encoding is not None:
            self.cq_dam_config_unzip_encoding = cq_dam_config_unzip_encoding

    @property
    def cq_dam_config_unzip_maxuncompressedsize(self):
        """Gets the cq_dam_config_unzip_maxuncompressedsize of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501


        :return: The cq_dam_config_unzip_maxuncompressedsize of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyInteger
        """
        return self._cq_dam_config_unzip_maxuncompressedsize

    @cq_dam_config_unzip_maxuncompressedsize.setter
    def cq_dam_config_unzip_maxuncompressedsize(self, cq_dam_config_unzip_maxuncompressedsize):
        """Sets the cq_dam_config_unzip_maxuncompressedsize of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.


        :param cq_dam_config_unzip_maxuncompressedsize: The cq_dam_config_unzip_maxuncompressedsize of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyInteger
        """

        self._cq_dam_config_unzip_maxuncompressedsize = cq_dam_config_unzip_maxuncompressedsize

    @property
    def cq_dam_config_unzip_encoding(self):
        """Gets the cq_dam_config_unzip_encoding of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501


        :return: The cq_dam_config_unzip_encoding of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._cq_dam_config_unzip_encoding

    @cq_dam_config_unzip_encoding.setter
    def cq_dam_config_unzip_encoding(self, cq_dam_config_unzip_encoding):
        """Sets the cq_dam_config_unzip_encoding of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.


        :param cq_dam_config_unzip_encoding: The cq_dam_config_unzip_encoding of this ComDayCqDamCoreImplUnzipUnzipConfigProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._cq_dam_config_unzip_encoding = cq_dam_config_unzip_encoding

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
        if not isinstance(other, ComDayCqDamCoreImplUnzipUnzipConfigProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
