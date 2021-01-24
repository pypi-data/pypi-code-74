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


class OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties(object):
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
        'dav_root': 'ConfigNodePropertyString',
        'dav_create_absolute_uri': 'ConfigNodePropertyBoolean',
        'dav_realm': 'ConfigNodePropertyString',
        'collection_types': 'ConfigNodePropertyArray',
        'filter_prefixes': 'ConfigNodePropertyArray',
        'filter_types': 'ConfigNodePropertyString',
        'filter_uris': 'ConfigNodePropertyString',
        'type_collections': 'ConfigNodePropertyString',
        'type_noncollections': 'ConfigNodePropertyString',
        'type_content': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'dav_root': 'dav.root',
        'dav_create_absolute_uri': 'dav.create-absolute-uri',
        'dav_realm': 'dav.realm',
        'collection_types': 'collection.types',
        'filter_prefixes': 'filter.prefixes',
        'filter_types': 'filter.types',
        'filter_uris': 'filter.uris',
        'type_collections': 'type.collections',
        'type_noncollections': 'type.noncollections',
        'type_content': 'type.content'
    }

    def __init__(self, dav_root=None, dav_create_absolute_uri=None, dav_realm=None, collection_types=None, filter_prefixes=None, filter_types=None, filter_uris=None, type_collections=None, type_noncollections=None, type_content=None):  # noqa: E501
        """OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties - a model defined in OpenAPI"""  # noqa: E501

        self._dav_root = None
        self._dav_create_absolute_uri = None
        self._dav_realm = None
        self._collection_types = None
        self._filter_prefixes = None
        self._filter_types = None
        self._filter_uris = None
        self._type_collections = None
        self._type_noncollections = None
        self._type_content = None
        self.discriminator = None

        if dav_root is not None:
            self.dav_root = dav_root
        if dav_create_absolute_uri is not None:
            self.dav_create_absolute_uri = dav_create_absolute_uri
        if dav_realm is not None:
            self.dav_realm = dav_realm
        if collection_types is not None:
            self.collection_types = collection_types
        if filter_prefixes is not None:
            self.filter_prefixes = filter_prefixes
        if filter_types is not None:
            self.filter_types = filter_types
        if filter_uris is not None:
            self.filter_uris = filter_uris
        if type_collections is not None:
            self.type_collections = type_collections
        if type_noncollections is not None:
            self.type_noncollections = type_noncollections
        if type_content is not None:
            self.type_content = type_content

    @property
    def dav_root(self):
        """Gets the dav_root of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The dav_root of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._dav_root

    @dav_root.setter
    def dav_root(self, dav_root):
        """Sets the dav_root of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param dav_root: The dav_root of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._dav_root = dav_root

    @property
    def dav_create_absolute_uri(self):
        """Gets the dav_create_absolute_uri of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The dav_create_absolute_uri of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._dav_create_absolute_uri

    @dav_create_absolute_uri.setter
    def dav_create_absolute_uri(self, dav_create_absolute_uri):
        """Sets the dav_create_absolute_uri of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param dav_create_absolute_uri: The dav_create_absolute_uri of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._dav_create_absolute_uri = dav_create_absolute_uri

    @property
    def dav_realm(self):
        """Gets the dav_realm of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The dav_realm of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._dav_realm

    @dav_realm.setter
    def dav_realm(self, dav_realm):
        """Sets the dav_realm of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param dav_realm: The dav_realm of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._dav_realm = dav_realm

    @property
    def collection_types(self):
        """Gets the collection_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The collection_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._collection_types

    @collection_types.setter
    def collection_types(self, collection_types):
        """Sets the collection_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param collection_types: The collection_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._collection_types = collection_types

    @property
    def filter_prefixes(self):
        """Gets the filter_prefixes of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The filter_prefixes of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._filter_prefixes

    @filter_prefixes.setter
    def filter_prefixes(self, filter_prefixes):
        """Sets the filter_prefixes of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param filter_prefixes: The filter_prefixes of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._filter_prefixes = filter_prefixes

    @property
    def filter_types(self):
        """Gets the filter_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The filter_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._filter_types

    @filter_types.setter
    def filter_types(self, filter_types):
        """Sets the filter_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param filter_types: The filter_types of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._filter_types = filter_types

    @property
    def filter_uris(self):
        """Gets the filter_uris of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The filter_uris of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._filter_uris

    @filter_uris.setter
    def filter_uris(self, filter_uris):
        """Sets the filter_uris of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param filter_uris: The filter_uris of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._filter_uris = filter_uris

    @property
    def type_collections(self):
        """Gets the type_collections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The type_collections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._type_collections

    @type_collections.setter
    def type_collections(self, type_collections):
        """Sets the type_collections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param type_collections: The type_collections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._type_collections = type_collections

    @property
    def type_noncollections(self):
        """Gets the type_noncollections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The type_noncollections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._type_noncollections

    @type_noncollections.setter
    def type_noncollections(self, type_noncollections):
        """Sets the type_noncollections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param type_noncollections: The type_noncollections of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._type_noncollections = type_noncollections

    @property
    def type_content(self):
        """Gets the type_content of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501


        :return: The type_content of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._type_content

    @type_content.setter
    def type_content(self, type_content):
        """Sets the type_content of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.


        :param type_content: The type_content of this OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._type_content = type_content

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
        if not isinstance(other, OrgApacheSlingJcrWebdavImplServletsSimpleWebDavServletProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
