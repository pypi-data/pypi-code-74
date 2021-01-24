# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from ._enums import *

__all__ = ['PlacementGroup']


class PlacementGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[Union[str, 'PlacementStrategy']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an EC2 placement group. Read more about placement groups
        in [AWS Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        web = aws.ec2.PlacementGroup("web", strategy="cluster")
        ```

        ## Import

        Placement groups can be imported using the `name`, e.g.

        ```sh
         $ pulumi import aws:ec2/placementGroup:PlacementGroup prod_pg production-placement-group
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[Union[str, 'PlacementStrategy']] strategy: The placement strategy. Can be `"cluster"`, `"partition"` or `"spread"`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
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

            __props__['name'] = name
            if strategy is None and not opts.urn:
                raise TypeError("Missing required property 'strategy'")
            __props__['strategy'] = strategy
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['placement_group_id'] = None
        super(PlacementGroup, __self__).__init__(
            'aws:ec2/placementGroup:PlacementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            placement_group_id: Optional[pulumi.Input[str]] = None,
            strategy: Optional[pulumi.Input[Union[str, 'PlacementStrategy']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'PlacementGroup':
        """
        Get an existing PlacementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the placement group.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[str] placement_group_id: The ID of the placement group.
        :param pulumi.Input[Union[str, 'PlacementStrategy']] strategy: The placement strategy. Can be `"cluster"`, `"partition"` or `"spread"`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["placement_group_id"] = placement_group_id
        __props__["strategy"] = strategy
        __props__["tags"] = tags
        return PlacementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the placement group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the placement group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the placement group.
        """
        return pulumi.get(self, "placement_group_id")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[str]:
        """
        The placement strategy. Can be `"cluster"`, `"partition"` or `"spread"`.
        """
        return pulumi.get(self, "strategy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

