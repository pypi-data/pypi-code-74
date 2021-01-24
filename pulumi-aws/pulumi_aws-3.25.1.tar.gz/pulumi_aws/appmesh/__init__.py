# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .gateway_route import *
from .mesh import *
from .route import *
from .virtual_gateway import *
from .virtual_node import *
from .virtual_router import *
from .virtual_service import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:appmesh/gatewayRoute:GatewayRoute":
                return GatewayRoute(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/mesh:Mesh":
                return Mesh(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/route:Route":
                return Route(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/virtualGateway:VirtualGateway":
                return VirtualGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/virtualNode:VirtualNode":
                return VirtualNode(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/virtualRouter:VirtualRouter":
                return VirtualRouter(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:appmesh/virtualService:VirtualService":
                return VirtualService(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "appmesh/gatewayRoute", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/mesh", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/route", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/virtualGateway", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/virtualNode", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/virtualRouter", _module_instance)
    pulumi.runtime.register_resource_module("aws", "appmesh/virtualService", _module_instance)

_register_module()
