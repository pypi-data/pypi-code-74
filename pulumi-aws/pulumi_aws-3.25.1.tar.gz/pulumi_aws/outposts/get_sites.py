# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetSitesResult',
    'AwaitableGetSitesResult',
    'get_sites',
]

@pulumi.output_type
class GetSitesResult:
    """
    A collection of values returned by getSites.
    """
    def __init__(__self__, id=None, ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        Set of Outposts Site identifiers.
        """
        return pulumi.get(self, "ids")


class AwaitableGetSitesResult(GetSitesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSitesResult(
            id=self.id,
            ids=self.ids)


def get_sites(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSitesResult:
    """
    Provides details about multiple Outposts Sites.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    all = aws.outposts.get_sites()
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:outposts/getSites:getSites', __args__, opts=opts, typ=GetSitesResult).value

    return AwaitableGetSitesResult(
        id=__ret__.id,
        ids=__ret__.ids)
