# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AccountAssignment']


class AccountAssignment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permission_set_arn: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Single Sign-On (SSO) Account Assignment resource

        ## Import

        SSO Account Assignments can be imported using the `principal_id`, `principal_type`, `target_id`, `target_type`, `permission_set_arn`, `instance_arn` separated by commas (`,`) e.g.

        ```sh
         $ pulumi import aws:ssoadmin/accountAssignment:AccountAssignment example f81d4fae-7dec-11d0-a765-00a0c91e6bf6,GROUP,1234567890,AWS_ACCOUNT,arn:aws:sso:::permissionSet/ssoins-0123456789abcdef/ps-0123456789abcdef,arn:aws:sso:::instance/ssoins-0123456789abcdef
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
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

            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__['instance_arn'] = instance_arn
            if permission_set_arn is None and not opts.urn:
                raise TypeError("Missing required property 'permission_set_arn'")
            __props__['permission_set_arn'] = permission_set_arn
            if principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_id'")
            __props__['principal_id'] = principal_id
            if principal_type is None and not opts.urn:
                raise TypeError("Missing required property 'principal_type'")
            __props__['principal_type'] = principal_type
            if target_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_id'")
            __props__['target_id'] = target_id
            __props__['target_type'] = target_type
        super(AccountAssignment, __self__).__init__(
            'aws:ssoadmin/accountAssignment:AccountAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_arn: Optional[pulumi.Input[str]] = None,
            permission_set_arn: Optional[pulumi.Input[str]] = None,
            principal_id: Optional[pulumi.Input[str]] = None,
            principal_type: Optional[pulumi.Input[str]] = None,
            target_id: Optional[pulumi.Input[str]] = None,
            target_type: Optional[pulumi.Input[str]] = None) -> 'AccountAssignment':
        """
        Get an existing AccountAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_arn"] = instance_arn
        __props__["permission_set_arn"] = permission_set_arn
        __props__["principal_id"] = principal_id
        __props__["principal_type"] = principal_type
        __props__["target_id"] = target_id
        __props__["target_type"] = target_type
        return AccountAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the SSO Instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        """
        return pulumi.get(self, "permission_set_arn")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[str]:
        """
        The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[str]:
        """
        An AWS account identifier, typically a 10-12 digit string.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[str]]:
        """
        The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        return pulumi.get(self, "target_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

