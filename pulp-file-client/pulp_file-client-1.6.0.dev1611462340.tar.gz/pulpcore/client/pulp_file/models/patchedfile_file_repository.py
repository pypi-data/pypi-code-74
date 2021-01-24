# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_file.configuration import Configuration


class PatchedfileFileRepository(object):
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
        'name': 'str',
        'description': 'str',
        'remote': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'remote': 'remote'
    }

    def __init__(self, name=None, description=None, remote=None, local_vars_configuration=None):  # noqa: E501
        """PatchedfileFileRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._remote = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.description = description
        self.remote = remote

    @property
    def name(self):
        """Gets the name of this PatchedfileFileRepository.  # noqa: E501

        A unique name for this repository.  # noqa: E501

        :return: The name of this PatchedfileFileRepository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedfileFileRepository.

        A unique name for this repository.  # noqa: E501

        :param name: The name of this PatchedfileFileRepository.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PatchedfileFileRepository.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this PatchedfileFileRepository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchedfileFileRepository.

        An optional description.  # noqa: E501

        :param description: The description of this PatchedfileFileRepository.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def remote(self):
        """Gets the remote of this PatchedfileFileRepository.  # noqa: E501


        :return: The remote of this PatchedfileFileRepository.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this PatchedfileFileRepository.


        :param remote: The remote of this PatchedfileFileRepository.  # noqa: E501
        :type: str
        """

        self._remote = remote

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
        if not isinstance(other, PatchedfileFileRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedfileFileRepository):
            return True

        return self.to_dict() != other.to_dict()
