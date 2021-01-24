# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['HostedPrivateVirtualInterface']


class HostedPrivateVirtualInterface(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input[str]] = None,
                 amazon_address: Optional[pulumi.Input[str]] = None,
                 bgp_asn: Optional[pulumi.Input[int]] = None,
                 bgp_auth_key: Optional[pulumi.Input[str]] = None,
                 connection_id: Optional[pulumi.Input[str]] = None,
                 customer_address: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_account_id: Optional[pulumi.Input[str]] = None,
                 vlan: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
        A hosted virtual interface is a virtual interface that is owned by another AWS account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.directconnect.HostedPrivateVirtualInterface("foo",
            address_family="ipv4",
            bgp_asn=65352,
            connection_id="dxcon-zzzzzzzz",
            vlan=4094)
        ```

        ## Import

        Direct Connect hosted private virtual interfaces can be imported using the `vif id`, e.g.

        ```sh
         $ pulumi import aws:directconnect/hostedPrivateVirtualInterface:HostedPrivateVirtualInterface test dxvif-33cc44dd
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
        :param pulumi.Input[int] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] connection_id: The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
        :param pulumi.Input[int] mtu: The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
        :param pulumi.Input[str] name: The name for the virtual interface.
        :param pulumi.Input[str] owner_account_id: The AWS account that will own the new virtual interface.
        :param pulumi.Input[int] vlan: The VLAN ID.
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

            if address_family is None and not opts.urn:
                raise TypeError("Missing required property 'address_family'")
            __props__['address_family'] = address_family
            __props__['amazon_address'] = amazon_address
            if bgp_asn is None and not opts.urn:
                raise TypeError("Missing required property 'bgp_asn'")
            __props__['bgp_asn'] = bgp_asn
            __props__['bgp_auth_key'] = bgp_auth_key
            if connection_id is None and not opts.urn:
                raise TypeError("Missing required property 'connection_id'")
            __props__['connection_id'] = connection_id
            __props__['customer_address'] = customer_address
            __props__['mtu'] = mtu
            __props__['name'] = name
            if owner_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'owner_account_id'")
            __props__['owner_account_id'] = owner_account_id
            if vlan is None and not opts.urn:
                raise TypeError("Missing required property 'vlan'")
            __props__['vlan'] = vlan
            __props__['amazon_side_asn'] = None
            __props__['arn'] = None
            __props__['aws_device'] = None
            __props__['jumbo_frame_capable'] = None
        super(HostedPrivateVirtualInterface, __self__).__init__(
            'aws:directconnect/hostedPrivateVirtualInterface:HostedPrivateVirtualInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_family: Optional[pulumi.Input[str]] = None,
            amazon_address: Optional[pulumi.Input[str]] = None,
            amazon_side_asn: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            aws_device: Optional[pulumi.Input[str]] = None,
            bgp_asn: Optional[pulumi.Input[int]] = None,
            bgp_auth_key: Optional[pulumi.Input[str]] = None,
            connection_id: Optional[pulumi.Input[str]] = None,
            customer_address: Optional[pulumi.Input[str]] = None,
            jumbo_frame_capable: Optional[pulumi.Input[bool]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner_account_id: Optional[pulumi.Input[str]] = None,
            vlan: Optional[pulumi.Input[int]] = None) -> 'HostedPrivateVirtualInterface':
        """
        Get an existing HostedPrivateVirtualInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
        :param pulumi.Input[str] arn: The ARN of the virtual interface.
        :param pulumi.Input[str] aws_device: The Direct Connect endpoint on which the virtual interface terminates.
        :param pulumi.Input[int] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] connection_id: The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
        :param pulumi.Input[bool] jumbo_frame_capable: Indicates whether jumbo frames (9001 MTU) are supported.
        :param pulumi.Input[int] mtu: The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
        :param pulumi.Input[str] name: The name for the virtual interface.
        :param pulumi.Input[str] owner_account_id: The AWS account that will own the new virtual interface.
        :param pulumi.Input[int] vlan: The VLAN ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address_family"] = address_family
        __props__["amazon_address"] = amazon_address
        __props__["amazon_side_asn"] = amazon_side_asn
        __props__["arn"] = arn
        __props__["aws_device"] = aws_device
        __props__["bgp_asn"] = bgp_asn
        __props__["bgp_auth_key"] = bgp_auth_key
        __props__["connection_id"] = connection_id
        __props__["customer_address"] = customer_address
        __props__["jumbo_frame_capable"] = jumbo_frame_capable
        __props__["mtu"] = mtu
        __props__["name"] = name
        __props__["owner_account_id"] = owner_account_id
        __props__["vlan"] = vlan
        return HostedPrivateVirtualInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[str]:
        """
        The address family for the BGP peer. `ipv4 ` or `ipv6`.
        """
        return pulumi.get(self, "address_family")

    @property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> pulumi.Output[str]:
        """
        The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
        """
        return pulumi.get(self, "amazon_address")

    @property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "amazon_side_asn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the virtual interface.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[str]:
        """
        The Direct Connect endpoint on which the virtual interface terminates.
        """
        return pulumi.get(self, "aws_device")

    @property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[int]:
        """
        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        """
        return pulumi.get(self, "bgp_asn")

    @property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> pulumi.Output[str]:
        """
        The authentication key for BGP configuration.
        """
        return pulumi.get(self, "bgp_auth_key")

    @property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[str]:
        """
        The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
        """
        return pulumi.get(self, "connection_id")

    @property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> pulumi.Output[str]:
        """
        The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
        """
        return pulumi.get(self, "customer_address")

    @property
    @pulumi.getter(name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> pulumi.Output[bool]:
        """
        Indicates whether jumbo frames (9001 MTU) are supported.
        """
        return pulumi.get(self, "jumbo_frame_capable")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the virtual interface.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[str]:
        """
        The AWS account that will own the new virtual interface.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter
    def vlan(self) -> pulumi.Output[int]:
        """
        The VLAN ID.
        """
        return pulumi.get(self, "vlan")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

