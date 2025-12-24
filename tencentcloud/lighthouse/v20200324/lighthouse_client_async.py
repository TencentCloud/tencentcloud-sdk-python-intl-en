# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.lighthouse.v20200324 import models
from typing import Dict


class LighthouseClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'lighthouse.intl.tencentcloudapi.com'
    _service = 'lighthouse'

    async def ApplyInstanceSnapshot(
            self,
            request: models.ApplyInstanceSnapshotRequest,
            opts: Dict = None,
    ) -> models.ApplyInstanceSnapshotResponse:
        """
        This API is used to roll back the system disk snapshot of the specified instance.
        <li>Only rollback to the original system disk is supported. </li>
        <li>Only snapshots in `NORMAL` status can be used for rollback. To query the status of a snapshot, you can call the `DescribeSnapshots` API and see the `SnapshotState` field in the response.</li>
        <li>When a snapshot is rolled back, the status of the instance must be `STOPPED` or `RUNNING`. You can call the `DescribeInstances` API to query the instance status. Instances in `RUNNING` status will be forcibly shut down before snapshot rollback. </li>
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyInstanceSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyInstanceSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateInstancesKeyPairs(
            self,
            request: models.AssociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.AssociateInstancesKeyPairsResponse:
        """
        This API is used to bind a user-specified key pair to an instance.
        * Only instances on LINUX_UNIX in [RUNNING, STOPPED] status are supported. Instances in `RUNNING` status will be forcibly shut down before binding.
        * If the public key of a key pair is written to the SSH configuration of the instance, you will be able to log in to the instance with the private key of the key pair.
        * If the instance is already associated with a key, the old key will become invalid.
        * If you currently use a password to log in, you will no longer be able to do so after you associate the instance with a key.
        * Batch operations are supported. The maximum number of instances in each request is 100. If instances not available for the operation are selected, you will get an error code.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachCcn(
            self,
            request: models.AttachCcnRequest,
            opts: Dict = None,
    ) -> models.AttachCcnResponse:
        """
        This API is used to associate a CCN instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        This API is used to attach one or more cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelShareBlueprintAcrossAccounts(
            self,
            request: models.CancelShareBlueprintAcrossAccountsRequest,
            opts: Dict = None,
    ) -> models.CancelShareBlueprintAcrossAccountsResponse:
        """
        This API is used to cancel image sharing across accounts.
        An image to be canceled sharing must be a custom image that is originally shared from another account to your account.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelShareBlueprintAcrossAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelShareBlueprintAcrossAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlueprint(
            self,
            request: models.CreateBlueprintRequest,
            opts: Dict = None,
    ) -> models.CreateBlueprintResponse:
        """
        This API is used to create an image.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlueprint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlueprintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisks(
            self,
            request: models.CreateDisksRequest,
            opts: Dict = None,
    ) -> models.CreateDisksResponse:
        """
        This API is used to create one or more cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFirewallRules(
            self,
            request: models.CreateFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.CreateFirewallRulesResponse:
        """
        This API is used to add a firewall rule on an instance.


        * `FirewallVersion` is the firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the updated rule from expiring. If it is left empty, conflicts will not be considered.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceSnapshot(
            self,
            request: models.CreateInstanceSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceSnapshotResponse:
        """
        This API is used to create a system disk snapshot of the specified instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        This API is used to create one or more Lighthouse instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKeyPair(
            self,
            request: models.CreateKeyPairRequest,
            opts: Dict = None,
    ) -> models.CreateKeyPairResponse:
        """
        This API is used to create a key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlueprints(
            self,
            request: models.DeleteBlueprintsRequest,
            opts: Dict = None,
    ) -> models.DeleteBlueprintsResponse:
        """
        This API is used to delete an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlueprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlueprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFirewallRules(
            self,
            request: models.DeleteFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteFirewallRulesResponse:
        """
        This API is used to delete a firewall rule of an instance.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the specified rule will be deleted directly.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKeyPairs(
            self,
            request: models.DeleteKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DeleteKeyPairsResponse:
        """
        This API is used to delete a key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        This API is used to delete a snapshot.
        The snapshot must be in `NORMAL` status. To query the status of a snapshot, you can call the `DescribeSnapshots` API and see the `SnapshotState` field in the response.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllScenes(
            self,
            request: models.DescribeAllScenesRequest,
            opts: Dict = None,
    ) -> models.DescribeAllScenesResponse:
        """
        This API is used to query the list of scenes in all regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllScenes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllScenesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlueprintInstances(
            self,
            request: models.DescribeBlueprintInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeBlueprintInstancesResponse:
        """
        This API is used to query the information of an image instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlueprintInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlueprintInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlueprints(
            self,
            request: models.DescribeBlueprintsRequest,
            opts: Dict = None,
    ) -> models.DescribeBlueprintsResponse:
        """
        This API is used to query the information of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlueprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlueprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBundleDiscount(
            self,
            request: models.DescribeBundleDiscountRequest,
            opts: Dict = None,
    ) -> models.DescribeBundleDiscountResponse:
        """
        This API is used to query the discount information of a package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBundleDiscount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBundleDiscountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBundles(
            self,
            request: models.DescribeBundlesRequest,
            opts: Dict = None,
    ) -> models.DescribeBundlesResponse:
        """
        This API is used to query the information of a package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBundles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBundlesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnAttachedInstances(
            self,
            request: models.DescribeCcnAttachedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnAttachedInstancesResponse:
        """
        This API is used to query the information of instances associated with CCN.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnAttachedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnAttachedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskConfigs(
            self,
            request: models.DescribeDiskConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskConfigsResponse:
        """
        This API is used to query the cloud disk configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiskDiscount(
            self,
            request: models.DescribeDiskDiscountRequest,
            opts: Dict = None,
    ) -> models.DescribeDiskDiscountResponse:
        """
        This API is used to query the discount information of a cloud disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiskDiscount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiskDiscountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisks(
            self,
            request: models.DescribeDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksResponse:
        """
        This API is used to query the information of one or more cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisksDeniedActions(
            self,
            request: models.DescribeDisksDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksDeniedActionsResponse:
        """
        This API is used to query the list of operation limits of one or more cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisksDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisksReturnable(
            self,
            request: models.DescribeDisksReturnableRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksReturnableResponse:
        """
        This API is used to query whether the specified cloud disk can be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisksReturnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksReturnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirewallRules(
            self,
            request: models.DescribeFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFirewallRulesResponse:
        """
        This API is used to query the firewall rules of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFirewallRulesTemplate(
            self,
            request: models.DescribeFirewallRulesTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeFirewallRulesTemplateResponse:
        """
        This API is used to query a firewall rule template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFirewallRulesTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFirewallRulesTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralResourceQuotas(
            self,
            request: models.DescribeGeneralResourceQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralResourceQuotasResponse:
        """
        This API is used to query the quota information of general resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralResourceQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralResourceQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImagesToShare(
            self,
            request: models.DescribeImagesToShareRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesToShareResponse:
        """
        This API is used to query the list of Cloud Virtual Machine (CVM) custom images and share the images to Tencent Cloud Lighthouse (Lighthouse).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImagesToShare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesToShareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLoginKeyPairAttribute(
            self,
            request: models.DescribeInstanceLoginKeyPairAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLoginKeyPairAttributeResponse:
        """
        This API is used to query the attributes of the default login key of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLoginKeyPairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLoginKeyPairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceVncUrl(
            self,
            request: models.DescribeInstanceVncUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceVncUrlResponse:
        """
        This API is used to query the URL for VNC login.

        * It does not support `STOPPED` CVMs.
        * A VNC URL is only valid for 15 seconds. If you do not access the URL within 15 seconds, you will need to query another one.
        * The VNC URL can be used once only. You need to query a new one if you want to log in again.
        * Up to 30 re-connection attempts allowed in one minute.
        * `InstanceVncUrl`: Its value will be returned after the API is successfully called.
        After you get the value of `InstanceVncUrl`, you need to append `InstanceVncUrl=xxxx` to the end of the link `https://img.qcloud.com/qcloud/app/active_vnc/index.html?`.
         The final URL can be in the following formats:

        ```
        https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceVncUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceVncUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the details of one or multiple instances.

        * You can query the details of an instance according to its ID, name, or private IP.
        * For more information on filters, please see [Filters](https://intl.cloud.tencent.com/document/product/1207/47576?from_cn_redirect=1#Filter).
        * If no parameter is defined, the status of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        * The latest operation (LatestOperation) and the latest operation status (LatestOperationState) of the instance can be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDeniedActions(
            self,
            request: models.DescribeInstancesDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDeniedActionsResponse:
        """
        This API is used to query the list of operation limits of one or more instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDiskNum(
            self,
            request: models.DescribeInstancesDiskNumRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDiskNumResponse:
        """
        This API is used to query the number of cloud disks attached to instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDiskNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDiskNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesReturnable(
            self,
            request: models.DescribeInstancesReturnableRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesReturnableResponse:
        """
        This API is used to query whether the specified instance can be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesReturnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesReturnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesTrafficPackages(
            self,
            request: models.DescribeInstancesTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesTrafficPackagesResponse:
        """
        This API is used to query the traffic package details of one or more instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeyPairs(
            self,
            request: models.DescribeKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DescribeKeyPairsResponse:
        """
        This API is used to query key pairs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyInstanceBundles(
            self,
            request: models.DescribeModifyInstanceBundlesRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyInstanceBundlesResponse:
        """
        This API is used to query the list of package options of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyInstanceBundles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyInstanceBundlesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query the information of regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResetInstanceBlueprints(
            self,
            request: models.DescribeResetInstanceBlueprintsRequest,
            opts: Dict = None,
    ) -> models.DescribeResetInstanceBlueprintsResponse:
        """
        This API is used to query the image information of a reset instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResetInstanceBlueprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResetInstanceBlueprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenes(
            self,
            request: models.DescribeScenesRequest,
            opts: Dict = None,
    ) -> models.DescribeScenesResponse:
        """
        This API is used to query the list of scenes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        This API is used to query the list of snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotsDeniedActions(
            self,
            request: models.DescribeSnapshotsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsDeniedActionsResponse:
        """
        This API is used to query the list of operation limits of one or more snapshots.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query the list of AZs in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachCcn(
            self,
            request: models.DetachCcnRequest,
            opts: Dict = None,
    ) -> models.DetachCcnResponse:
        """
        This API is used to disassociate with a CCN instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachDisks(
            self,
            request: models.DetachDisksRequest,
            opts: Dict = None,
    ) -> models.DetachDisksResponse:
        """
        This API is used to detach one or more cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateInstancesKeyPairs(
            self,
            request: models.DisassociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DisassociateInstancesKeyPairsResponse:
        """
        This API is used to unbind an instance from the specified key pair.

        * Only instances on LINUX_UNIX in [RUNNING, STOPPED] status are supported. Instances in `RUNNING` status will be forcibly shut down before unbinding.
        * After a key pair is unassociated from an instance, you can log in to the instance with password.
        * If no password was set, you cannot log in to the instance with SSH after unbinding. You can call the ResetInstancesPassword API to set a login password.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportKeyPair(
            self,
            request: models.ImportKeyPairRequest,
            opts: Dict = None,
    ) -> models.ImportKeyPairResponse:
        """
        This API is used to import the specified key pair.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateBlueprint(
            self,
            request: models.InquirePriceCreateBlueprintRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateBlueprintResponse:
        """
        This API is used to query the price of a created image.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateBlueprint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateBlueprintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateDisks(
            self,
            request: models.InquirePriceCreateDisksRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateDisksResponse:
        """
        This API is used to query the price of purchasing cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateInstances(
            self,
            request: models.InquirePriceCreateInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateInstancesResponse:
        """
        This API is used to query the price of a created instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewDisks(
            self,
            request: models.InquirePriceRenewDisksRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewDisksResponse:
        """
        This API is used to query the price of renewing cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewInstances(
            self,
            request: models.InquirePriceRenewInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewInstancesResponse:
        """
        This API is used to query the price of renewing one or more instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDisks(
            self,
            request: models.IsolateDisksRequest,
            opts: Dict = None,
    ) -> models.IsolateDisksResponse:
        """
        This API is used to return one or more Lighthouse cloud disks.

        You can only perform this operation on `UNATTACHED` disks.
        After the successful call of the API, the cloud disk goes to the SHUTDOWN state.
        Up to 20 instances are supported at one time.
        This API is async. After the request is sent, a `RequestId` is returned. At this time, the operation is not completed yet. To check the result, you need to call  [DescribeDisks](https://intl.cloud.tencent.com/document/product/1207/66093?from_cn_redirect=1). If the latest operation status (LatestOperationState) of the disk is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateInstances(
            self,
            request: models.IsolateInstancesRequest,
            opts: Dict = None,
    ) -> models.IsolateInstancesResponse:
        """
        This API is used to return one or more Lighthouse instances.
        * Only `RUNNING` and `STOPPED` instances can be returned.
        * The instance status goes to `SHUTDOWN` after the API is called successfully.
        * Batch operations are supported. Up to 20 resources (including instances and data disks) can be returned in each request.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlueprintAttribute(
            self,
            request: models.ModifyBlueprintAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyBlueprintAttributeResponse:
        """
        This API is used to modify an image attribute.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlueprintAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlueprintAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDisksAttribute(
            self,
            request: models.ModifyDisksAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDisksAttributeResponse:
        """
        This API is used to modify cloud disk attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDisksAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDisksAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDisksRenewFlag(
            self,
            request: models.ModifyDisksRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyDisksRenewFlagResponse:
        """
        This API is used to modify the configuration of auto-renewal of cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDisksRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDisksRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFirewallRuleDescription(
            self,
            request: models.ModifyFirewallRuleDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyFirewallRuleDescriptionResponse:
        """
        This API is used to modify the description of a single firewall rule.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the description of the specified rule will be modified directly.

        In the `FirewallRule` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFirewallRuleDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFirewallRuleDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFirewallRules(
            self,
            request: models.ModifyFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyFirewallRulesResponse:
        """
        This API is used to reset the firewall rules of an instance.

        This API deletes all firewall rules of the current instance first and then adds new rules.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the specified rule will be reset directly.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageSharePermission(
            self,
            request: models.ModifyImageSharePermissionRequest,
            opts: Dict = None,
    ) -> models.ModifyImageSharePermissionResponse:
        """
        This API is used to share and cancel sharing of CVM custom images to the Lighthouse service.
        Sharing CVM images to Lighthouse requires the following conditions to be met:
        1. Images that have been shared cannot be shared again.
        2. Images imported from external sources are not supported for sharing.
        3. Full-instance images are not supported for sharing.
        4. Images need to support CloudInit to be eligible for sharing.
        5. The Platform and OsName of the images must meet the sharing conditions before the images are eligible for sharing.
        6. Only images in the NORMAL status are supported for sharing.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesAttribute(
            self,
            request: models.ModifyInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesAttributeResponse:
        """
        This API is used to modify an instance attribute.
        * The instance name is used only for users’ convenience.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesBundle(
            self,
            request: models.ModifyInstancesBundleRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesBundleResponse:
        """
        This API is used change one or more Lighthouse instance bundles.
        * Only `RUNNING` and `STOPPED` instances can be changed.
        * Batch operations are supported. The maximum number of instances in each request is 30.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesBundle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesBundleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesLoginKeyPairAttribute(
            self,
            request: models.ModifyInstancesLoginKeyPairAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesLoginKeyPairAttributeResponse:
        """
        This API is used to set the attributes of the default login key pair of an instance.

        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesLoginKeyPairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesLoginKeyPairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesRenewFlag(
            self,
            request: models.ModifyInstancesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesRenewFlagResponse:
        """
        This API is used to change the auto-renewal setting of monthly-subscribed instances.

        * Instances with auto-renewal enabled are automatically renewed on a monthly basis upon the expiration.
        * Batch operations are supported. Up to 100 instances per request is allowed.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotAttribute(
            self,
            request: models.ModifySnapshotAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotAttributeResponse:
        """
        This API is used to modify the attributes of a snapshot.
        <li>The snapshot name is used only for users’ convenience.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootInstances(
            self,
            request: models.RebootInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootInstancesResponse:
        """
        This API is used to restart instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `REBOOTING` when the API is called successfully and will become `RUNNING` when the instance is successfully restarted.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RebootInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDisks(
            self,
            request: models.RenewDisksRequest,
            opts: Dict = None,
    ) -> models.RenewDisksResponse:
        """
        This API is used to renew one or more Lighthouse cloud disks.

        This operation can only be performed on data disks with the status of `ATTACHED`, `UNATTACHED` or `SHUTDOWN`.
        Up to 50 cloud disks are supported at one time.
        This API is async. After the request is sent, a `RequestId` is returned. At this time, the operation is not completed yet. To check the result, you need to call  [DescribeDisks](https://intl.cloud.tencent.com/document/product/1207/66093?from_cn_redirect=1). If the latest operation status (LatestOperationState) of the disk is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstances(
            self,
            request: models.RenewInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewInstancesResponse:
        """
        This API is used to renew one or more Lighthouse instances.
        * You can only perform this operation on instances whose status is `RUNNING`, `STOPPED` and `SHUTDOWN`.
        * Batch operations are supported. Up to 100 instances are supported in each request.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAttachCcn(
            self,
            request: models.ResetAttachCcnRequest,
            opts: Dict = None,
    ) -> models.ResetAttachCcnResponse:
        """
        This API is used to apply for association again after a CCN instance association application expires.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAttachCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAttachCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstance(
            self,
            request: models.ResetInstanceRequest,
            opts: Dict = None,
    ) -> models.ResetInstanceResponse:
        """
        This API is used to reinstall the image on the specified instance.

        * If you specify a `BlueprintId`, the specified image is used; otherwise, the image used by the current instance is used.
        * The system disk will be formatted and reset. Therefore, make sure that no important files are stored on the system disk.
        * Currently, this API does not support switching the operating system between `LINUX_UNIX` and `WINDOWS` for instances.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesPassword(
            self,
            request: models.ResetInstancesPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesPasswordResponse:
        """
        This API is used to reset the password of the instance OS to a user-specified password.
        * You can only use this API to modify the password of the admin account. The name of the admin account varies by OS (on Windows, it is `Administrator`; on Ubuntu, it is `ubuntu`; on other systems, it is `root`).
        * Batch operations are supported. You can reset the passwords of multiple instances to the same one. The maximum number of instances in each request is 100.
        * It’s recommended to shut down the instance first and then reset the password. If the instance is running, this API will try to shut it down normally. If the attempt fails, it will force to instance to shut down.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        Note: Just like powering off a physical PC, a forced shutdown may cause data loss or the corruption of file system.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDisks(
            self,
            request: models.ResizeDisksRequest,
            opts: Dict = None,
    ) -> models.ResizeDisksResponse:
        """
        This API is used to scale out a cloud disk. The operation currently only supports cloud disks of the data disk type that are in the ATTACHED or UNATTACHED status.
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ShareBlueprintAcrossAccounts(
            self,
            request: models.ShareBlueprintAcrossAccountsRequest,
            opts: Dict = None,
    ) -> models.ShareBlueprintAcrossAccountsResponse:
        """
        This API is used to share an image across accounts.
        This API is used to share custom images only, and the status of the shared image must be NORMAL.
        The account receiving the shared image must be a root account.
        """
        
        kwargs = {}
        kwargs["action"] = "ShareBlueprintAcrossAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ShareBlueprintAcrossAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstances(
            self,
            request: models.StartInstancesRequest,
            opts: Dict = None,
    ) -> models.StartInstancesResponse:
        """
        This API is used to start one or more instances.

        * You can only perform this operation on instances whose status is `STOPPED`.
        * The instance status will become `STARTING` when the API is called successfully and will become `RUNNING` when the instance is successfully started.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstances(
            self,
            request: models.StopInstancesRequest,
            opts: Dict = None,
    ) -> models.StopInstancesResponse:
        """
        This API is used to shut down one or more instances.
        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `STOPPING` when the API is called successfully and will become `STOPPED` when the instance is successfully shut down.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncBlueprint(
            self,
            request: models.SyncBlueprintRequest,
            opts: Dict = None,
    ) -> models.SyncBlueprintResponse:
        """
        This API is used to synchronize a custom image to other regions.

        * Synchronization to multiple regions is supported. Up to 10 regions are supported.
        * Synchronization to the source region is not supported.
        * Only images in the NORMAL status are supported for synchronization.
        * Synchronization between Chinese mainland regions and regions outside the Chinese mainland is not supported.
         * You can use the [DescribeBlueprints](https://www.tencentcloud.comom/document/api/1207/47689?from_cn_redirect=1) API to query the image status. When the status is NORMAL, it indicates that the source region synchronization ends.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncBlueprint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncBlueprintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDisks(
            self,
            request: models.TerminateDisksRequest,
            opts: Dict = None,
    ) -> models.TerminateDisksResponse:
        """
        This API is used to terminate one or more cloud disk.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        This API is used to terminate one or more instances.

        * Instances in `SHUTDOWN` status can be terminated through this API and cannot be recovered.
        * Batch operations are supported. The allowed maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)