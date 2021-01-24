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

__all__ = ['Mesh']


class Mesh(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['MeshSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AWS App Mesh service mesh resource.

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        simple = aws.appmesh.Mesh("simple")
        ```
        ### Egress Filter

        ```python
        import pulumi
        import pulumi_aws as aws

        simple = aws.appmesh.Mesh("simple", spec=aws.appmesh.MeshSpecArgs(
            egress_filter=aws.appmesh.MeshSpecEgressFilterArgs(
                type="ALLOW_ALL",
            ),
        ))
        ```

        ## Import

        App Mesh service meshes can be imported using the `name`, e.g.

        ```sh
         $ pulumi import aws:appmesh/mesh:Mesh simple simpleapp
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name to use for the service mesh. Must be between 1 and 255 characters in length.
        :param pulumi.Input[pulumi.InputType['MeshSpecArgs']] spec: The service mesh specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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
            __props__['spec'] = spec
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['created_date'] = None
            __props__['last_updated_date'] = None
            __props__['mesh_owner'] = None
            __props__['resource_owner'] = None
        super(Mesh, __self__).__init__(
            'aws:appmesh/mesh:Mesh',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_date: Optional[pulumi.Input[str]] = None,
            last_updated_date: Optional[pulumi.Input[str]] = None,
            mesh_owner: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_owner: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['MeshSpecArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Mesh':
        """
        Get an existing Mesh resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the service mesh.
        :param pulumi.Input[str] created_date: The creation date of the service mesh.
        :param pulumi.Input[str] last_updated_date: The last update date of the service mesh.
        :param pulumi.Input[str] mesh_owner: The AWS account ID of the service mesh's owner.
        :param pulumi.Input[str] name: The name to use for the service mesh. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] resource_owner: The resource owner's AWS account ID.
        :param pulumi.Input[pulumi.InputType['MeshSpecArgs']] spec: The service mesh specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["created_date"] = created_date
        __props__["last_updated_date"] = last_updated_date
        __props__["mesh_owner"] = mesh_owner
        __props__["name"] = name
        __props__["resource_owner"] = resource_owner
        __props__["spec"] = spec
        __props__["tags"] = tags
        return Mesh(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the service mesh.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the service mesh.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[str]:
        """
        The last update date of the service mesh.
        """
        return pulumi.get(self, "last_updated_date")

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> pulumi.Output[str]:
        """
        The AWS account ID of the service mesh's owner.
        """
        return pulumi.get(self, "mesh_owner")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name to use for the service mesh. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Output[str]:
        """
        The resource owner's AWS account ID.
        """
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional['outputs.MeshSpec']]:
        """
        The service mesh specification to apply.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

