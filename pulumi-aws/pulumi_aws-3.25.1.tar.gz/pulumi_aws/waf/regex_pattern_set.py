# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RegexPatternSet']


class RegexPatternSet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a WAF Regex Pattern Set Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.waf.RegexPatternSet("example", regex_pattern_strings=[
            "one",
            "two",
        ])
        ```

        ## Import

        AWS WAF Regex Pattern Set can be imported using their ID, e.g.

        ```sh
         $ pulumi import aws:waf/regexPatternSet:RegexPatternSet example a1b2c3d4-d5f6-7777-8888-9999aaaabbbbcccc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
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
            __props__['regex_pattern_strings'] = regex_pattern_strings
            __props__['arn'] = None
        super(RegexPatternSet, __self__).__init__(
            'aws:waf/regexPatternSet:RegexPatternSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'RegexPatternSet':
        """
        Get an existing RegexPatternSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN)
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["regex_pattern_strings"] = regex_pattern_strings
        return RegexPatternSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN)
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the Regex Pattern Set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        return pulumi.get(self, "regex_pattern_strings")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

