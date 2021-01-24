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

__all__ = ['AnalyticsApplication']


class AnalyticsApplication(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloudwatch_logging_options: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationCloudwatchLoggingOptionsArgs']]] = None,
                 code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inputs: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationInputsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyticsApplicationOutputArgs']]]]] = None,
                 reference_data_sources: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationReferenceDataSourcesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
        allows processing and analyzing streaming data using standard SQL.

        For more details, see the [Amazon Kinesis Analytics Documentation](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html).

        > **Note:** To manage Amazon Kinesis Data Analytics for Apache Flink applications, use the [`kinesisanalyticsv2.Application`](https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application.html) resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_stream = aws.kinesis.Stream("testStream", shard_count=1)
        test_application = aws.kinesis.AnalyticsApplication("testApplication", inputs=aws.kinesis.AnalyticsApplicationInputsArgs(
            name_prefix="test_prefix",
            kinesis_stream=aws.kinesis.AnalyticsApplicationInputsKinesisStreamArgs(
                resource_arn=test_stream.arn,
                role_arn=aws_iam_role["test"]["arn"],
            ),
            parallelism=aws.kinesis.AnalyticsApplicationInputsParallelismArgs(
                count=1,
            ),
            schema=aws.kinesis.AnalyticsApplicationInputsSchemaArgs(
                record_columns=[aws.kinesis.AnalyticsApplicationInputsSchemaRecordColumnArgs(
                    mapping="$.test",
                    name="test",
                    sql_type="VARCHAR(8)",
                )],
                record_encoding="UTF-8",
                record_format=aws.kinesis.AnalyticsApplicationInputsSchemaRecordFormatArgs(
                    mapping_parameters=aws.kinesis.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs(
                        json=aws.kinesis.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs(
                            record_row_path="$",
                        ),
                    ),
                ),
            ),
        ))
        ```

        ## Import

        Kinesis Analytics Application can be imported by using ARN, e.g.

        ```sh
         $ pulumi import aws:kinesis/analyticsApplication:AnalyticsApplication example arn:aws:kinesisanalytics:us-west-2:1234567890:application/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationCloudwatchLoggingOptionsArgs']] cloudwatch_logging_options: The CloudWatch log stream options to monitor application errors.
               See CloudWatch Logging Options below for more details.
        :param pulumi.Input[str] code: SQL Code to transform input data, and generate output.
        :param pulumi.Input[str] description: Description of the application.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationInputsArgs']] inputs: Input configuration of the application. See Inputs below for more details.
        :param pulumi.Input[str] name: Name of the Kinesis Analytics Application.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyticsApplicationOutputArgs']]]] outputs: Output destination configuration of the application. See Outputs below for more details.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationReferenceDataSourcesArgs']] reference_data_sources: An S3 Reference Data Source for the application.
               See Reference Data Sources below for more details.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Kinesis Analytics Application.
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

            __props__['cloudwatch_logging_options'] = cloudwatch_logging_options
            __props__['code'] = code
            __props__['description'] = description
            __props__['inputs'] = inputs
            __props__['name'] = name
            __props__['outputs'] = outputs
            __props__['reference_data_sources'] = reference_data_sources
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['create_timestamp'] = None
            __props__['last_update_timestamp'] = None
            __props__['status'] = None
            __props__['version'] = None
        super(AnalyticsApplication, __self__).__init__(
            'aws:kinesis/analyticsApplication:AnalyticsApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cloudwatch_logging_options: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationCloudwatchLoggingOptionsArgs']]] = None,
            code: Optional[pulumi.Input[str]] = None,
            create_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            inputs: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationInputsArgs']]] = None,
            last_update_timestamp: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            outputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyticsApplicationOutputArgs']]]]] = None,
            reference_data_sources: Optional[pulumi.Input[pulumi.InputType['AnalyticsApplicationReferenceDataSourcesArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'AnalyticsApplication':
        """
        Get an existing AnalyticsApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Kinesis Analytics Appliation.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationCloudwatchLoggingOptionsArgs']] cloudwatch_logging_options: The CloudWatch log stream options to monitor application errors.
               See CloudWatch Logging Options below for more details.
        :param pulumi.Input[str] code: SQL Code to transform input data, and generate output.
        :param pulumi.Input[str] create_timestamp: The Timestamp when the application version was created.
        :param pulumi.Input[str] description: Description of the application.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationInputsArgs']] inputs: Input configuration of the application. See Inputs below for more details.
        :param pulumi.Input[str] last_update_timestamp: The Timestamp when the application was last updated.
        :param pulumi.Input[str] name: Name of the Kinesis Analytics Application.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyticsApplicationOutputArgs']]]] outputs: Output destination configuration of the application. See Outputs below for more details.
        :param pulumi.Input[pulumi.InputType['AnalyticsApplicationReferenceDataSourcesArgs']] reference_data_sources: An S3 Reference Data Source for the application.
               See Reference Data Sources below for more details.
        :param pulumi.Input[str] status: The Status of the application.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the Kinesis Analytics Application.
        :param pulumi.Input[int] version: The Version of the application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["cloudwatch_logging_options"] = cloudwatch_logging_options
        __props__["code"] = code
        __props__["create_timestamp"] = create_timestamp
        __props__["description"] = description
        __props__["inputs"] = inputs
        __props__["last_update_timestamp"] = last_update_timestamp
        __props__["name"] = name
        __props__["outputs"] = outputs
        __props__["reference_data_sources"] = reference_data_sources
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["version"] = version
        return AnalyticsApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Kinesis Analytics Appliation.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> pulumi.Output[Optional['outputs.AnalyticsApplicationCloudwatchLoggingOptions']]:
        """
        The CloudWatch log stream options to monitor application errors.
        See CloudWatch Logging Options below for more details.
        """
        return pulumi.get(self, "cloudwatch_logging_options")

    @property
    @pulumi.getter
    def code(self) -> pulumi.Output[Optional[str]]:
        """
        SQL Code to transform input data, and generate output.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter(name="createTimestamp")
    def create_timestamp(self) -> pulumi.Output[str]:
        """
        The Timestamp when the application version was created.
        """
        return pulumi.get(self, "create_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the application.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Optional['outputs.AnalyticsApplicationInputs']]:
        """
        Input configuration of the application. See Inputs below for more details.
        """
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter(name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> pulumi.Output[str]:
        """
        The Timestamp when the application was last updated.
        """
        return pulumi.get(self, "last_update_timestamp")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Kinesis Analytics Application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Optional[Sequence['outputs.AnalyticsApplicationOutput']]]:
        """
        Output destination configuration of the application. See Outputs below for more details.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="referenceDataSources")
    def reference_data_sources(self) -> pulumi.Output[Optional['outputs.AnalyticsApplicationReferenceDataSources']]:
        """
        An S3 Reference Data Source for the application.
        See Reference Data Sources below for more details.
        """
        return pulumi.get(self, "reference_data_sources")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The Status of the application.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of tags for the Kinesis Analytics Application.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The Version of the application.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

