# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetLoadBalancerResult',
    'AwaitableGetLoadBalancerResult',
    'get_load_balancer',
]

warnings.warn("""aws.elasticloadbalancing.getLoadBalancer has been deprecated in favor of aws.elb.getLoadBalancer""", DeprecationWarning)

@pulumi.output_type
class GetLoadBalancerResult:
    """
    A collection of values returned by getLoadBalancer.
    """
    def __init__(__self__, access_logs=None, arn=None, availability_zones=None, connection_draining=None, connection_draining_timeout=None, cross_zone_load_balancing=None, dns_name=None, health_check=None, id=None, idle_timeout=None, instances=None, internal=None, listeners=None, name=None, security_groups=None, source_security_group=None, source_security_group_id=None, subnets=None, tags=None, zone_id=None):
        if access_logs and not isinstance(access_logs, dict):
            raise TypeError("Expected argument 'access_logs' to be a dict")
        pulumi.set(__self__, "access_logs", access_logs)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if connection_draining and not isinstance(connection_draining, bool):
            raise TypeError("Expected argument 'connection_draining' to be a bool")
        pulumi.set(__self__, "connection_draining", connection_draining)
        if connection_draining_timeout and not isinstance(connection_draining_timeout, int):
            raise TypeError("Expected argument 'connection_draining_timeout' to be a int")
        pulumi.set(__self__, "connection_draining_timeout", connection_draining_timeout)
        if cross_zone_load_balancing and not isinstance(cross_zone_load_balancing, bool):
            raise TypeError("Expected argument 'cross_zone_load_balancing' to be a bool")
        pulumi.set(__self__, "cross_zone_load_balancing", cross_zone_load_balancing)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if health_check and not isinstance(health_check, dict):
            raise TypeError("Expected argument 'health_check' to be a dict")
        pulumi.set(__self__, "health_check", health_check)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idle_timeout and not isinstance(idle_timeout, int):
            raise TypeError("Expected argument 'idle_timeout' to be a int")
        pulumi.set(__self__, "idle_timeout", idle_timeout)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if internal and not isinstance(internal, bool):
            raise TypeError("Expected argument 'internal' to be a bool")
        pulumi.set(__self__, "internal", internal)
        if listeners and not isinstance(listeners, list):
            raise TypeError("Expected argument 'listeners' to be a list")
        pulumi.set(__self__, "listeners", listeners)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        pulumi.set(__self__, "security_groups", security_groups)
        if source_security_group and not isinstance(source_security_group, str):
            raise TypeError("Expected argument 'source_security_group' to be a str")
        pulumi.set(__self__, "source_security_group", source_security_group)
        if source_security_group_id and not isinstance(source_security_group_id, str):
            raise TypeError("Expected argument 'source_security_group_id' to be a str")
        pulumi.set(__self__, "source_security_group_id", source_security_group_id)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> 'outputs.GetLoadBalancerAccessLogsResult':
        return pulumi.get(self, "access_logs")

    @property
    @pulumi.getter
    def arn(self) -> str:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[str]:
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> bool:
        return pulumi.get(self, "connection_draining")

    @property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> int:
        return pulumi.get(self, "connection_draining_timeout")

    @property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> bool:
        return pulumi.get(self, "cross_zone_load_balancing")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> 'outputs.GetLoadBalancerHealthCheckResult':
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> int:
        return pulumi.get(self, "idle_timeout")

    @property
    @pulumi.getter
    def instances(self) -> Sequence[str]:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def internal(self) -> bool:
        return pulumi.get(self, "internal")

    @property
    @pulumi.getter
    def listeners(self) -> Sequence['outputs.GetLoadBalancerListenerResult']:
        return pulumi.get(self, "listeners")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[str]:
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> str:
        return pulumi.get(self, "source_security_group")

    @property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> str:
        return pulumi.get(self, "source_security_group_id")

    @property
    @pulumi.getter
    def subnets(self) -> Sequence[str]:
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            access_logs=self.access_logs,
            arn=self.arn,
            availability_zones=self.availability_zones,
            connection_draining=self.connection_draining,
            connection_draining_timeout=self.connection_draining_timeout,
            cross_zone_load_balancing=self.cross_zone_load_balancing,
            dns_name=self.dns_name,
            health_check=self.health_check,
            id=self.id,
            idle_timeout=self.idle_timeout,
            instances=self.instances,
            internal=self.internal,
            listeners=self.listeners,
            name=self.name,
            security_groups=self.security_groups,
            source_security_group=self.source_security_group,
            source_security_group_id=self.source_security_group_id,
            subnets=self.subnets,
            tags=self.tags,
            zone_id=self.zone_id)


def get_load_balancer(name: Optional[str] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerResult:
    """
    Provides information about a "classic" Elastic Load Balancer (ELB).
    See `LB` Data Source if you are looking for "v2"
    Application Load Balancer (ALB) or Network Load Balancer (NLB).

    This data source can prove useful when a module accepts an LB as an input
    variable and needs to, for example, determine the security groups associated
    with it, etc.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    lb_name = config.get("lbName")
    if lb_name is None:
        lb_name = ""
    test = aws.elb.get_load_balancer(name=lb_name)
    ```


    :param str name: The unique name of the load balancer.
    """
    pulumi.log.warn("get_load_balancer is deprecated: aws.elasticloadbalancing.getLoadBalancer has been deprecated in favor of aws.elb.getLoadBalancer")
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elasticloadbalancing/getLoadBalancer:getLoadBalancer', __args__, opts=opts, typ=GetLoadBalancerResult).value

    return AwaitableGetLoadBalancerResult(
        access_logs=__ret__.access_logs,
        arn=__ret__.arn,
        availability_zones=__ret__.availability_zones,
        connection_draining=__ret__.connection_draining,
        connection_draining_timeout=__ret__.connection_draining_timeout,
        cross_zone_load_balancing=__ret__.cross_zone_load_balancing,
        dns_name=__ret__.dns_name,
        health_check=__ret__.health_check,
        id=__ret__.id,
        idle_timeout=__ret__.idle_timeout,
        instances=__ret__.instances,
        internal=__ret__.internal,
        listeners=__ret__.listeners,
        name=__ret__.name,
        security_groups=__ret__.security_groups,
        source_security_group=__ret__.source_security_group,
        source_security_group_id=__ret__.source_security_group_id,
        subnets=__ret__.subnets,
        tags=__ret__.tags,
        zone_id=__ret__.zone_id)
