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

__all__ = ['EventDestination']


class EventDestination(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]]] = None,
                 configuration_set_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 kinesis_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']]] = None,
                 matching_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sns_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an SES event destination

        ## Example Usage
        ### CloudWatch Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        cloudwatch = aws.ses.EventDestination("cloudwatch",
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            matching_types=[
                "bounce",
                "send",
            ],
            cloudwatch_destinations=[aws.ses.EventDestinationCloudwatchDestinationArgs(
                default_value="default",
                dimension_name="dimension",
                value_source="emailHeader",
            )])
        ```
        ### Kinesis Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        kinesis = aws.ses.EventDestination("kinesis",
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            matching_types=[
                "bounce",
                "send",
            ],
            kinesis_destination=aws.ses.EventDestinationKinesisDestinationArgs(
                stream_arn=aws_kinesis_firehose_delivery_stream["example"]["arn"],
                role_arn=aws_iam_role["example"]["arn"],
            ))
        ```
        ### SNS Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        sns = aws.ses.EventDestination("sns",
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            matching_types=[
                "bounce",
                "send",
            ],
            sns_destination=aws.ses.EventDestinationSnsDestinationArgs(
                topic_arn=aws_sns_topic["example"]["arn"],
            ))
        ```

        ## Import

        SES event destinations can be imported using `configuration_set_name` together with the event destination's `name`, e.g.

        ```sh
         $ pulumi import aws:ses/eventDestination:EventDestination sns some-configuration-set-test/event-destination-sns
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]] cloudwatch_destinations: CloudWatch destination for the events
        :param pulumi.Input[str] configuration_set_name: The name of the configuration set
        :param pulumi.Input[bool] enabled: If true, the event destination will be enabled
        :param pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']] kinesis_destination: Send the events to a kinesis firehose destination
        :param pulumi.Input[Sequence[pulumi.Input[str]]] matching_types: A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        :param pulumi.Input[str] name: The name of the event destination
        :param pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']] sns_destination: Send the events to an SNS Topic destination
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

            __props__['cloudwatch_destinations'] = cloudwatch_destinations
            if configuration_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'configuration_set_name'")
            __props__['configuration_set_name'] = configuration_set_name
            __props__['enabled'] = enabled
            __props__['kinesis_destination'] = kinesis_destination
            if matching_types is None and not opts.urn:
                raise TypeError("Missing required property 'matching_types'")
            __props__['matching_types'] = matching_types
            __props__['name'] = name
            __props__['sns_destination'] = sns_destination
        super(EventDestination, __self__).__init__(
            'aws:ses/eventDestination:EventDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloudwatch_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]]] = None,
            configuration_set_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            kinesis_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']]] = None,
            matching_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sns_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']]] = None) -> 'EventDestination':
        """
        Get an existing EventDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]] cloudwatch_destinations: CloudWatch destination for the events
        :param pulumi.Input[str] configuration_set_name: The name of the configuration set
        :param pulumi.Input[bool] enabled: If true, the event destination will be enabled
        :param pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']] kinesis_destination: Send the events to a kinesis firehose destination
        :param pulumi.Input[Sequence[pulumi.Input[str]]] matching_types: A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        :param pulumi.Input[str] name: The name of the event destination
        :param pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']] sns_destination: Send the events to an SNS Topic destination
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloudwatch_destinations"] = cloudwatch_destinations
        __props__["configuration_set_name"] = configuration_set_name
        __props__["enabled"] = enabled
        __props__["kinesis_destination"] = kinesis_destination
        __props__["matching_types"] = matching_types
        __props__["name"] = name
        __props__["sns_destination"] = sns_destination
        return EventDestination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudwatchDestinations")
    def cloudwatch_destinations(self) -> pulumi.Output[Optional[Sequence['outputs.EventDestinationCloudwatchDestination']]]:
        """
        CloudWatch destination for the events
        """
        return pulumi.get(self, "cloudwatch_destinations")

    @property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Output[str]:
        """
        The name of the configuration set
        """
        return pulumi.get(self, "configuration_set_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the event destination will be enabled
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="kinesisDestination")
    def kinesis_destination(self) -> pulumi.Output[Optional['outputs.EventDestinationKinesisDestination']]:
        """
        Send the events to a kinesis firehose destination
        """
        return pulumi.get(self, "kinesis_destination")

    @property
    @pulumi.getter(name="matchingTypes")
    def matching_types(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        """
        return pulumi.get(self, "matching_types")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the event destination
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="snsDestination")
    def sns_destination(self) -> pulumi.Output[Optional['outputs.EventDestinationSnsDestination']]:
        """
        Send the events to an SNS Topic destination
        """
        return pulumi.get(self, "sns_destination")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

