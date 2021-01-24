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


class ComAdobeCqCommerceImplAssetVideoHandlerProperties(object):
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
        'cq_commerce_asset_handler_active': 'ConfigNodePropertyBoolean',
        'cq_commerce_asset_handler_name': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'cq_commerce_asset_handler_active': 'cq.commerce.asset.handler.active',
        'cq_commerce_asset_handler_name': 'cq.commerce.asset.handler.name'
    }

    def __init__(self, cq_commerce_asset_handler_active=None, cq_commerce_asset_handler_name=None):  # noqa: E501
        """ComAdobeCqCommerceImplAssetVideoHandlerProperties - a model defined in OpenAPI"""  # noqa: E501

        self._cq_commerce_asset_handler_active = None
        self._cq_commerce_asset_handler_name = None
        self.discriminator = None

        if cq_commerce_asset_handler_active is not None:
            self.cq_commerce_asset_handler_active = cq_commerce_asset_handler_active
        if cq_commerce_asset_handler_name is not None:
            self.cq_commerce_asset_handler_name = cq_commerce_asset_handler_name

    @property
    def cq_commerce_asset_handler_active(self):
        """Gets the cq_commerce_asset_handler_active of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501


        :return: The cq_commerce_asset_handler_active of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._cq_commerce_asset_handler_active

    @cq_commerce_asset_handler_active.setter
    def cq_commerce_asset_handler_active(self, cq_commerce_asset_handler_active):
        """Sets the cq_commerce_asset_handler_active of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.


        :param cq_commerce_asset_handler_active: The cq_commerce_asset_handler_active of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._cq_commerce_asset_handler_active = cq_commerce_asset_handler_active

    @property
    def cq_commerce_asset_handler_name(self):
        """Gets the cq_commerce_asset_handler_name of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501


        :return: The cq_commerce_asset_handler_name of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._cq_commerce_asset_handler_name

    @cq_commerce_asset_handler_name.setter
    def cq_commerce_asset_handler_name(self, cq_commerce_asset_handler_name):
        """Sets the cq_commerce_asset_handler_name of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.


        :param cq_commerce_asset_handler_name: The cq_commerce_asset_handler_name of this ComAdobeCqCommerceImplAssetVideoHandlerProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._cq_commerce_asset_handler_name = cq_commerce_asset_handler_name

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
        if not isinstance(other, ComAdobeCqCommerceImplAssetVideoHandlerProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
