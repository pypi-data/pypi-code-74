# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2514
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertInstrumentPropertyRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'identifier_type': 'str',
        'identifier': 'str',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'identifier_type': 'identifierType',
        'identifier': 'identifier',
        'properties': 'properties'
    }

    required_map = {
        'identifier_type': 'required',
        'identifier': 'required',
        'properties': 'optional'
    }

    def __init__(self, identifier_type=None, identifier=None, properties=None):  # noqa: E501
        """
        UpsertInstrumentPropertyRequest - a model defined in OpenAPI

        :param identifier_type:  The instrument identifier type. (required)
        :type identifier_type: str
        :param identifier:  The unique instrument identifier of the instrument to update or insert properties on. (required)
        :type identifier: str
        :param properties:  Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.
        :type properties: list[lusid.ModelProperty]

        """  # noqa: E501

        self._identifier_type = None
        self._identifier = None
        self._properties = None
        self.discriminator = None

        self.identifier_type = identifier_type
        self.identifier = identifier
        self.properties = properties

    @property
    def identifier_type(self):
        """Gets the identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501

        The instrument identifier type.  # noqa: E501

        :return: The identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this UpsertInstrumentPropertyRequest.

        The instrument identifier type.  # noqa: E501

        :param identifier_type: The identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type: str
        """
        if identifier_type is None:
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def identifier(self):
        """Gets the identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501

        The unique instrument identifier of the instrument to update or insert properties on.  # noqa: E501

        :return: The identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UpsertInstrumentPropertyRequest.

        The unique instrument identifier of the instrument to update or insert properties on.  # noqa: E501

        :param identifier: The identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def properties(self):
        """Gets the properties of this UpsertInstrumentPropertyRequest.  # noqa: E501

        Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpsertInstrumentPropertyRequest.

        Set of unique instrument properties and associated values to store with the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type: list[ModelProperty]
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
        if not isinstance(other, UpsertInstrumentPropertyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
