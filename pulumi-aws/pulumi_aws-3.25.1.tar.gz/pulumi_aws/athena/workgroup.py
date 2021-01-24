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

__all__ = ['Workgroup']


class Workgroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['WorkgroupConfigurationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Athena Workgroup.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.athena.Workgroup("example", configuration=aws.athena.WorkgroupConfigurationArgs(
            enforce_workgroup_configuration=True,
            publish_cloudwatch_metrics_enabled=True,
            result_configuration=aws.athena.WorkgroupConfigurationResultConfigurationArgs(
                output_location=f"s3://{aws_s3_bucket['example']['bucket']}/output/",
                encryption_configuration={
                    "encryptionOption": "SSE_KMS",
                    "kms_key_arn": aws_kms_key["example"]["arn"],
                },
            ),
        ))
        ```

        ## Import

        Athena Workgroups can be imported using their name, e.g.

        ```sh
         $ pulumi import aws:athena/workgroup:Workgroup example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['WorkgroupConfigurationArgs']] configuration: Configuration block with various settings for the workgroup. Documented below.
        :param pulumi.Input[str] description: Description of the workgroup.
        :param pulumi.Input[bool] force_destroy: The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        :param pulumi.Input[str] name: Name of the workgroup.
        :param pulumi.Input[str] state: State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags for the workgroup.
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

            __props__['configuration'] = configuration
            __props__['description'] = description
            __props__['force_destroy'] = force_destroy
            __props__['name'] = name
            __props__['state'] = state
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Workgroup, __self__).__init__(
            'aws:athena/workgroup:Workgroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            configuration: Optional[pulumi.Input[pulumi.InputType['WorkgroupConfigurationArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Workgroup':
        """
        Get an existing Workgroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the workgroup
        :param pulumi.Input[pulumi.InputType['WorkgroupConfigurationArgs']] configuration: Configuration block with various settings for the workgroup. Documented below.
        :param pulumi.Input[str] description: Description of the workgroup.
        :param pulumi.Input[bool] force_destroy: The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        :param pulumi.Input[str] name: Name of the workgroup.
        :param pulumi.Input[str] state: State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags for the workgroup.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["configuration"] = configuration
        __props__["description"] = description
        __props__["force_destroy"] = force_destroy
        __props__["name"] = name
        __props__["state"] = state
        __props__["tags"] = tags
        return Workgroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the workgroup
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.WorkgroupConfiguration']]:
        """
        Configuration block with various settings for the workgroup. Documented below.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the workgroup.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the workgroup.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags for the workgroup.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

