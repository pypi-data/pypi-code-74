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

__all__ = ['Directory']


class Directory(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 ip_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 self_service_permissions: Optional[pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_access_properties: Optional[pulumi.Input[pulumi.InputType['DirectoryWorkspaceAccessPropertiesArgs']]] = None,
                 workspace_creation_properties: Optional[pulumi.Input[pulumi.InputType['DirectoryWorkspaceCreationPropertiesArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a WorkSpaces directory in AWS WorkSpaces Service.

        > **NOTE:** AWS WorkSpaces service requires [`workspaces_DefaultRole`](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role) IAM role to operate normally.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        workspaces = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="Service",
                identifiers=["workspaces.amazonaws.com"],
            )],
        )])
        workspaces_default = aws.iam.Role("workspacesDefault", assume_role_policy=workspaces.json)
        workspaces_default_service_access = aws.iam.RolePolicyAttachment("workspacesDefaultServiceAccess",
            role=workspaces_default.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonWorkSpacesServiceAccess")
        workspaces_default_self_service_access = aws.iam.RolePolicyAttachment("workspacesDefaultSelfServiceAccess",
            role=workspaces_default.name,
            policy_arn="arn:aws:iam::aws:policy/AmazonWorkSpacesSelfServiceAccess")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_c = aws.ec2.Subnet("exampleC",
            vpc_id=example_vpc.id,
            availability_zone="us-east-1c",
            cidr_block="10.0.2.0/24")
        example_d = aws.ec2.Subnet("exampleD",
            vpc_id=example_vpc.id,
            availability_zone="us-east-1d",
            cidr_block="10.0.3.0/24")
        example_directory = aws.workspaces.Directory("exampleDirectory",
            directory_id=example_directoryservice / directory_directory["id"],
            subnet_ids=[
                example_c.id,
                example_d.id,
            ],
            tags={
                "Example": "true",
            },
            self_service_permissions=aws.workspaces.DirectorySelfServicePermissionsArgs(
                change_compute_type=True,
                increase_volume_size=True,
                rebuild_workspace=True,
                restart_workspace=True,
                switch_running_mode=True,
            ),
            workspace_access_properties=aws.workspaces.DirectoryWorkspaceAccessPropertiesArgs(
                device_type_android="ALLOW",
                device_type_chromeos="ALLOW",
                device_type_ios="ALLOW",
                device_type_osx="ALLOW",
                device_type_web="DENY",
                device_type_windows="DENY",
                device_type_zeroclient="DENY",
            ),
            workspace_creation_properties=aws.workspaces.DirectoryWorkspaceCreationPropertiesArgs(
                custom_security_group_id=aws_security_group["example"]["id"],
                default_ou="OU=AWS,DC=Workgroup,DC=Example,DC=com",
                enable_internet_access=True,
                enable_maintenance_mode=True,
                user_enabled_as_local_administrator=True,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    workspaces_default_service_access,
                    workspaces_default_self_service_access,
                ]))
        example_a = aws.ec2.Subnet("exampleA",
            vpc_id=example_vpc.id,
            availability_zone="us-east-1a",
            cidr_block="10.0.0.0/24")
        example_b = aws.ec2.Subnet("exampleB",
            vpc_id=example_vpc.id,
            availability_zone="us-east-1b",
            cidr_block="10.0.1.0/24")
        example_directoryservice_directory_directory = aws.directoryservice.Directory("exampleDirectoryservice/directoryDirectory",
            name="corp.example.com",
            password="#S1ncerely",
            size="Small",
            vpc_settings=aws.directoryservice.DirectoryVpcSettingsArgs(
                vpc_id=example_vpc.id,
                subnet_ids=[
                    example_a.id,
                    example_b.id,
                ],
            ))
        ```
        ### IP Groups

        ```python
        import pulumi
        import pulumi_aws as aws

        example_ip_group = aws.workspaces.IpGroup("exampleIpGroup")
        example_directory = aws.workspaces.Directory("exampleDirectory",
            directory_id=aws_directory_service_directory["example"]["id"],
            ip_group_ids=[example_ip_group.id])
        ```

        ## Import

        Workspaces directory can be imported using the directory ID, e.g.

        ```sh
         $ pulumi import aws:workspaces/directory:Directory main d-4444444444
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_id: The directory identifier for registration in WorkSpaces service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_group_ids: The identifiers of the IP access control groups associated with the directory.
        :param pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']] self_service_permissions: Permissions to enable or disable self-service capabilities. Defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets where the directory resides.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the WorkSpaces directory.
        :param pulumi.Input[pulumi.InputType['DirectoryWorkspaceAccessPropertiesArgs']] workspace_access_properties: Specifies which devices and operating systems users can use to access their WorkSpaces. Defined below.
        :param pulumi.Input[pulumi.InputType['DirectoryWorkspaceCreationPropertiesArgs']] workspace_creation_properties: Default properties that are used for creating WorkSpaces. Defined below.
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

            if directory_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_id'")
            __props__['directory_id'] = directory_id
            __props__['ip_group_ids'] = ip_group_ids
            __props__['self_service_permissions'] = self_service_permissions
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['workspace_access_properties'] = workspace_access_properties
            __props__['workspace_creation_properties'] = workspace_creation_properties
            __props__['alias'] = None
            __props__['customer_user_name'] = None
            __props__['directory_name'] = None
            __props__['directory_type'] = None
            __props__['dns_ip_addresses'] = None
            __props__['iam_role_id'] = None
            __props__['registration_code'] = None
            __props__['workspace_security_group_id'] = None
        super(Directory, __self__).__init__(
            'aws:workspaces/directory:Directory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            customer_user_name: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            directory_name: Optional[pulumi.Input[str]] = None,
            directory_type: Optional[pulumi.Input[str]] = None,
            dns_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            iam_role_id: Optional[pulumi.Input[str]] = None,
            ip_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            registration_code: Optional[pulumi.Input[str]] = None,
            self_service_permissions: Optional[pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']]] = None,
            subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            workspace_access_properties: Optional[pulumi.Input[pulumi.InputType['DirectoryWorkspaceAccessPropertiesArgs']]] = None,
            workspace_creation_properties: Optional[pulumi.Input[pulumi.InputType['DirectoryWorkspaceCreationPropertiesArgs']]] = None,
            workspace_security_group_id: Optional[pulumi.Input[str]] = None) -> 'Directory':
        """
        Get an existing Directory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The directory alias.
        :param pulumi.Input[str] customer_user_name: The user name for the service account.
        :param pulumi.Input[str] directory_id: The directory identifier for registration in WorkSpaces service.
        :param pulumi.Input[str] directory_name: The name of the directory.
        :param pulumi.Input[str] directory_type: The directory type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_ip_addresses: The IP addresses of the DNS servers for the directory.
        :param pulumi.Input[str] iam_role_id: The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_group_ids: The identifiers of the IP access control groups associated with the directory.
        :param pulumi.Input[str] registration_code: The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        :param pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']] self_service_permissions: Permissions to enable or disable self-service capabilities. Defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets where the directory resides.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the WorkSpaces directory.
        :param pulumi.Input[pulumi.InputType['DirectoryWorkspaceAccessPropertiesArgs']] workspace_access_properties: Specifies which devices and operating systems users can use to access their WorkSpaces. Defined below.
        :param pulumi.Input[pulumi.InputType['DirectoryWorkspaceCreationPropertiesArgs']] workspace_creation_properties: Default properties that are used for creating WorkSpaces. Defined below.
        :param pulumi.Input[str] workspace_security_group_id: The identifier of the security group that is assigned to new WorkSpaces.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["alias"] = alias
        __props__["customer_user_name"] = customer_user_name
        __props__["directory_id"] = directory_id
        __props__["directory_name"] = directory_name
        __props__["directory_type"] = directory_type
        __props__["dns_ip_addresses"] = dns_ip_addresses
        __props__["iam_role_id"] = iam_role_id
        __props__["ip_group_ids"] = ip_group_ids
        __props__["registration_code"] = registration_code
        __props__["self_service_permissions"] = self_service_permissions
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["workspace_access_properties"] = workspace_access_properties
        __props__["workspace_creation_properties"] = workspace_creation_properties
        __props__["workspace_security_group_id"] = workspace_security_group_id
        return Directory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The directory alias.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> pulumi.Output[str]:
        """
        The user name for the service account.
        """
        return pulumi.get(self, "customer_user_name")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        """
        The directory identifier for registration in WorkSpaces service.
        """
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Output[str]:
        """
        The name of the directory.
        """
        return pulumi.get(self, "directory_name")

    @property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> pulumi.Output[str]:
        """
        The directory type.
        """
        return pulumi.get(self, "directory_type")

    @property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        The IP addresses of the DNS servers for the directory.
        """
        return pulumi.get(self, "dns_ip_addresses")

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> pulumi.Output[str]:
        """
        The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        """
        return pulumi.get(self, "iam_role_id")

    @property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The identifiers of the IP access control groups associated with the directory.
        """
        return pulumi.get(self, "ip_group_ids")

    @property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> pulumi.Output[str]:
        """
        The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        """
        return pulumi.get(self, "registration_code")

    @property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(self) -> pulumi.Output['outputs.DirectorySelfServicePermissions']:
        """
        Permissions to enable or disable self-service capabilities. Defined below.
        """
        return pulumi.get(self, "self_service_permissions")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The identifiers of the subnets where the directory resides.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags assigned to the WorkSpaces directory.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workspaceAccessProperties")
    def workspace_access_properties(self) -> pulumi.Output['outputs.DirectoryWorkspaceAccessProperties']:
        """
        Specifies which devices and operating systems users can use to access their WorkSpaces. Defined below.
        """
        return pulumi.get(self, "workspace_access_properties")

    @property
    @pulumi.getter(name="workspaceCreationProperties")
    def workspace_creation_properties(self) -> pulumi.Output['outputs.DirectoryWorkspaceCreationProperties']:
        """
        Default properties that are used for creating WorkSpaces. Defined below.
        """
        return pulumi.get(self, "workspace_creation_properties")

    @property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> pulumi.Output[str]:
        """
        The identifier of the security group that is assigned to new WorkSpaces.
        """
        return pulumi.get(self, "workspace_security_group_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

