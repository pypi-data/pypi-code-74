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


class ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties(object):
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
        'filepattern': 'ConfigNodePropertyString',
        'device_groups': 'ConfigNodePropertyArray',
        'build_page_nodes': 'ConfigNodePropertyBoolean',
        'build_client_libs': 'ConfigNodePropertyBoolean',
        'build_canvas_component': 'ConfigNodePropertyBoolean'
    }

    attribute_map = {
        'filepattern': 'filepattern',
        'device_groups': 'device.groups',
        'build_page_nodes': 'build.page.nodes',
        'build_client_libs': 'build.client.libs',
        'build_canvas_component': 'build.canvas.component'
    }

    def __init__(self, filepattern=None, device_groups=None, build_page_nodes=None, build_client_libs=None, build_canvas_component=None):  # noqa: E501
        """ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._filepattern = None
        self._device_groups = None
        self._build_page_nodes = None
        self._build_client_libs = None
        self._build_canvas_component = None
        self.discriminator = None

        if filepattern is not None:
            self.filepattern = filepattern
        if device_groups is not None:
            self.device_groups = device_groups
        if build_page_nodes is not None:
            self.build_page_nodes = build_page_nodes
        if build_client_libs is not None:
            self.build_client_libs = build_client_libs
        if build_canvas_component is not None:
            self.build_canvas_component = build_canvas_component

    @property
    def filepattern(self):
        """Gets the filepattern of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501


        :return: The filepattern of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._filepattern

    @filepattern.setter
    def filepattern(self, filepattern):
        """Sets the filepattern of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.


        :param filepattern: The filepattern of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._filepattern = filepattern

    @property
    def device_groups(self):
        """Gets the device_groups of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501


        :return: The device_groups of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        """Sets the device_groups of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.


        :param device_groups: The device_groups of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._device_groups = device_groups

    @property
    def build_page_nodes(self):
        """Gets the build_page_nodes of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501


        :return: The build_page_nodes of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._build_page_nodes

    @build_page_nodes.setter
    def build_page_nodes(self, build_page_nodes):
        """Sets the build_page_nodes of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.


        :param build_page_nodes: The build_page_nodes of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._build_page_nodes = build_page_nodes

    @property
    def build_client_libs(self):
        """Gets the build_client_libs of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501


        :return: The build_client_libs of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._build_client_libs

    @build_client_libs.setter
    def build_client_libs(self, build_client_libs):
        """Sets the build_client_libs of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.


        :param build_client_libs: The build_client_libs of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._build_client_libs = build_client_libs

    @property
    def build_canvas_component(self):
        """Gets the build_canvas_component of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501


        :return: The build_canvas_component of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyBoolean
        """
        return self._build_canvas_component

    @build_canvas_component.setter
    def build_canvas_component(self, build_canvas_component):
        """Sets the build_canvas_component of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.


        :param build_canvas_component: The build_canvas_component of this ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties.  # noqa: E501
        :type: ConfigNodePropertyBoolean
        """

        self._build_canvas_component = build_canvas_component

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
        if not isinstance(other, ComDayCqWcmDesignimporterImplMobileCanvasBuilderImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
