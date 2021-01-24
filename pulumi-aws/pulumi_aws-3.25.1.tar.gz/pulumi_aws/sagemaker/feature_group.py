# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['FeatureGroup']


class FeatureGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 event_time_feature_name: Optional[pulumi.Input[str]] = None,
                 feature_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureGroupFeatureDefinitionArgs']]]]] = None,
                 feature_group_name: Optional[pulumi.Input[str]] = None,
                 offline_store_config: Optional[pulumi.Input[pulumi.InputType['FeatureGroupOfflineStoreConfigArgs']]] = None,
                 online_store_config: Optional[pulumi.Input[pulumi.InputType['FeatureGroupOnlineStoreConfigArgs']]] = None,
                 record_identifier_feature_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a SageMaker Feature Group resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.sagemaker.FeatureGroup("example",
            feature_group_name="example",
            record_identifier_feature_name="example",
            event_time_feature_name="example",
            role_arn=aws_iam_role["test"]["arn"],
            feature_definitions=[aws.sagemaker.FeatureGroupFeatureDefinitionArgs(
                feature_name="example",
                feature_type="String",
            )],
            online_store_config=aws.sagemaker.FeatureGroupOnlineStoreConfigArgs(
                enable_online_store=True,
            ))
        ```

        ## Import

        Feature Groups can be imported using the `name`, e.g.

        ```sh
         $ pulumi import aws:sagemaker/featureGroup:FeatureGroup test_feature_group feature_group-foo
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A free-form description of a Feature Group.
        :param pulumi.Input[str] event_time_feature_name: The name of the feature that stores the EventTime of a Record in a Feature Group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureGroupFeatureDefinitionArgs']]]] feature_definitions: A list of Feature names and types. See Feature Definition Below.
        :param pulumi.Input[str] feature_group_name: The name of the Feature Group. The name must be unique within an AWS Region in an AWS account.
        :param pulumi.Input[pulumi.InputType['FeatureGroupOfflineStoreConfigArgs']] offline_store_config: The Offline Feature Store Configuration. See Offline Store Config Below.
        :param pulumi.Input[pulumi.InputType['FeatureGroupOnlineStoreConfigArgs']] online_store_config: The Online Feature Store Configuration. See Online Store Config Below.
        :param pulumi.Input[str] record_identifier_feature_name: The name of the Feature whose value uniquely identifies a Record defined in the Feature Store. Only the latest record per identifier value will be stored in the Online Store.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the Offline Store if an `offline_store_config` is provided.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['description'] = description
            if event_time_feature_name is None and not opts.urn:
                raise TypeError("Missing required property 'event_time_feature_name'")
            __props__['event_time_feature_name'] = event_time_feature_name
            if feature_definitions is None and not opts.urn:
                raise TypeError("Missing required property 'feature_definitions'")
            __props__['feature_definitions'] = feature_definitions
            if feature_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'feature_group_name'")
            __props__['feature_group_name'] = feature_group_name
            __props__['offline_store_config'] = offline_store_config
            __props__['online_store_config'] = online_store_config
            if record_identifier_feature_name is None and not opts.urn:
                raise TypeError("Missing required property 'record_identifier_feature_name'")
            __props__['record_identifier_feature_name'] = record_identifier_feature_name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['tags'] = tags
            __props__['arn'] = None
        super(FeatureGroup, __self__).__init__(
            'aws:sagemaker/featureGroup:FeatureGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            event_time_feature_name: Optional[pulumi.Input[str]] = None,
            feature_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureGroupFeatureDefinitionArgs']]]]] = None,
            feature_group_name: Optional[pulumi.Input[str]] = None,
            offline_store_config: Optional[pulumi.Input[pulumi.InputType['FeatureGroupOfflineStoreConfigArgs']]] = None,
            online_store_config: Optional[pulumi.Input[pulumi.InputType['FeatureGroupOnlineStoreConfigArgs']]] = None,
            record_identifier_feature_name: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'FeatureGroup':
        """
        Get an existing FeatureGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this feature_group.
        :param pulumi.Input[str] description: A free-form description of a Feature Group.
        :param pulumi.Input[str] event_time_feature_name: The name of the feature that stores the EventTime of a Record in a Feature Group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FeatureGroupFeatureDefinitionArgs']]]] feature_definitions: A list of Feature names and types. See Feature Definition Below.
        :param pulumi.Input[str] feature_group_name: The name of the Feature Group. The name must be unique within an AWS Region in an AWS account.
        :param pulumi.Input[pulumi.InputType['FeatureGroupOfflineStoreConfigArgs']] offline_store_config: The Offline Feature Store Configuration. See Offline Store Config Below.
        :param pulumi.Input[pulumi.InputType['FeatureGroupOnlineStoreConfigArgs']] online_store_config: The Online Feature Store Configuration. See Online Store Config Below.
        :param pulumi.Input[str] record_identifier_feature_name: The name of the Feature whose value uniquely identifies a Record defined in the Feature Store. Only the latest record per identifier value will be stored in the Online Store.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the Offline Store if an `offline_store_config` is provided.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["event_time_feature_name"] = event_time_feature_name
        __props__["feature_definitions"] = feature_definitions
        __props__["feature_group_name"] = feature_group_name
        __props__["offline_store_config"] = offline_store_config
        __props__["online_store_config"] = online_store_config
        __props__["record_identifier_feature_name"] = record_identifier_feature_name
        __props__["role_arn"] = role_arn
        __props__["tags"] = tags
        return FeatureGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this feature_group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A free-form description of a Feature Group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventTimeFeatureName")
    def event_time_feature_name(self) -> pulumi.Output[str]:
        """
        The name of the feature that stores the EventTime of a Record in a Feature Group.
        """
        return pulumi.get(self, "event_time_feature_name")

    @property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> pulumi.Output[Sequence['outputs.FeatureGroupFeatureDefinition']]:
        """
        A list of Feature names and types. See Feature Definition Below.
        """
        return pulumi.get(self, "feature_definitions")

    @property
    @pulumi.getter(name="featureGroupName")
    def feature_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Feature Group. The name must be unique within an AWS Region in an AWS account.
        """
        return pulumi.get(self, "feature_group_name")

    @property
    @pulumi.getter(name="offlineStoreConfig")
    def offline_store_config(self) -> pulumi.Output[Optional['outputs.FeatureGroupOfflineStoreConfig']]:
        """
        The Offline Feature Store Configuration. See Offline Store Config Below.
        """
        return pulumi.get(self, "offline_store_config")

    @property
    @pulumi.getter(name="onlineStoreConfig")
    def online_store_config(self) -> pulumi.Output[Optional['outputs.FeatureGroupOnlineStoreConfig']]:
        """
        The Online Feature Store Configuration. See Online Store Config Below.
        """
        return pulumi.get(self, "online_store_config")

    @property
    @pulumi.getter(name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> pulumi.Output[str]:
        """
        The name of the Feature whose value uniquely identifies a Record defined in the Feature Store. Only the latest record per identifier value will be stored in the Online Store.
        """
        return pulumi.get(self, "record_identifier_feature_name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the Offline Store if an `offline_store_config` is provided.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

