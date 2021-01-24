# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


class Images(object):
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
        'available_source_list': 'list[ImagesAvailableSource]',
        'field_list': 'list[ImagesField]'
    }

    attribute_map = {
        'available_source_list': 'availableSourceList',
        'field_list': 'fieldList'
    }

    def __init__(self, available_source_list=None, field_list=None, local_vars_configuration=None):  # noqa: E501
        """Images - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._available_source_list = None
        self._field_list = None
        self.discriminator = None

        self.available_source_list = available_source_list
        self.field_list = field_list

    @property
    def available_source_list(self):
        """Gets the available_source_list of this Images.  # noqa: E501


        :return: The available_source_list of this Images.  # noqa: E501
        :rtype: list[ImagesAvailableSource]
        """
        return self._available_source_list

    @available_source_list.setter
    def available_source_list(self, available_source_list):
        """Sets the available_source_list of this Images.


        :param available_source_list: The available_source_list of this Images.  # noqa: E501
        :type available_source_list: list[ImagesAvailableSource]
        """
        if self.local_vars_configuration.client_side_validation and available_source_list is None:  # noqa: E501
            raise ValueError("Invalid value for `available_source_list`, must not be `None`")  # noqa: E501

        self._available_source_list = available_source_list

    @property
    def field_list(self):
        """Gets the field_list of this Images.  # noqa: E501


        :return: The field_list of this Images.  # noqa: E501
        :rtype: list[ImagesField]
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """Sets the field_list of this Images.


        :param field_list: The field_list of this Images.  # noqa: E501
        :type field_list: list[ImagesField]
        """
        if self.local_vars_configuration.client_side_validation and field_list is None:  # noqa: E501
            raise ValueError("Invalid value for `field_list`, must not be `None`")  # noqa: E501

        self._field_list = field_list

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
        if not isinstance(other, Images):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Images):
            return True

        return self.to_dict() != other.to_dict()
