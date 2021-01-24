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


class ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties(object):
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
        'com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path': 'ConfigNodePropertyArray',
        'com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency': 'ConfigNodePropertyString'
    }

    attribute_map = {
        'com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path': 'com.adobe.cq.screens.offlinecontent.impl.BulkOfflineUpdateServiceImpl.projectPath',
        'com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency': 'com.adobe.cq.screens.offlinecontent.impl.BulkOfflineUpdateServiceImpl.scheduleFrequency'
    }

    def __init__(self, com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path=None, com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency=None):  # noqa: E501
        """ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties - a model defined in OpenAPI"""  # noqa: E501

        self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path = None
        self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency = None
        self.discriminator = None

        if com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path is not None:
            self.com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path = com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path
        if com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency is not None:
            self.com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency = com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency

    @property
    def com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path(self):
        """Gets the com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501


        :return: The com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyArray
        """
        return self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path

    @com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path.setter
    def com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path(self, com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path):
        """Sets the com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.


        :param com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path: The com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501
        :type: ConfigNodePropertyArray
        """

        self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path = com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_project_path

    @property
    def com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency(self):
        """Gets the com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501


        :return: The com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501
        :rtype: ConfigNodePropertyString
        """
        return self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency

    @com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency.setter
    def com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency(self, com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency):
        """Sets the com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.


        :param com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency: The com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency of this ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties.  # noqa: E501
        :type: ConfigNodePropertyString
        """

        self._com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency = com_adobe_cq_screens_offlinecontent_impl_bulk_offline_update_service_impl_schedule_frequency

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
        if not isinstance(other, ComAdobeCqScreensOfflinecontentImplBulkOfflineUpdateServiceImplProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
