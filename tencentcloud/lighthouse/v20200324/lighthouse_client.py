# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.lighthouse.v20200324 import models


class LighthouseClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'lighthouse.intl.tencentcloudapi.com'
    _service = 'lighthouse'


    def ApplyInstanceSnapshot(self, request):
        """This API is used to roll back the system disk snapshot of the specified instance.
        <li>Only rollback to the original system disk is supported. </li>
        <li>Only snapshots in `NORMAL` status can be used for rollback. To query the status of a snapshot, you can call the `DescribeSnapshots` API and see the `SnapshotState` field in the response.</li>
        <li>When a snapshot is rolled back, the status of the instance must be `STOPPED` or `RUNNING`. You can call the `DescribeInstances` API to query the instance status. Instances in `RUNNING` status will be forcibly shut down before snapshot rollback. </li>

        :param request: Request instance for ApplyInstanceSnapshot.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ApplyInstanceSnapshotRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ApplyInstanceSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyInstanceSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyInstanceSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateInstancesKeyPairs(self, request):
        """This API is used to bind a user-specified key pair to an instance.
        * Only instances on LINUX_UNIX in [RUNNING, STOPPED] status are supported. Instances in `RUNNING` status will be forcibly shut down before binding.
        * If the public key of a key pair is written to the SSH configuration of the instance, you will be able to log in to the instance with the private key of the key pair.
        * If the instance is already associated with a key, the old key will become invalid.
        * If you currently use a password to log in, you will no longer be able to do so after you associate the instance with a key.
        * Batch operations are supported. The maximum number of instances in each request is 100. If instances not available for the operation are selected, you will get an error code.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for AssociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AssociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AssociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachCcn(self, request):
        """This API is used to associate a CCN instance.

        :param request: Request instance for AttachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AttachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AttachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        """This API is used to attach one or more cloud disks.

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlueprint(self, request):
        """This API is used to create an image.

        :param request: Request instance for CreateBlueprint.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateBlueprintRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateBlueprintResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlueprint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlueprintResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisks(self, request):
        """This API is used to create one or more cloud disks.

        :param request: Request instance for CreateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFirewallRules(self, request):
        """This API is used to add a firewall rule on an instance.


        * `FirewallVersion` is the firewall version number. Every time you update the firewall rule version, it will be automatically increased by 1 to prevent the updated rule from expiring. If it is left empty, conflicts will not be considered.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.

        :param request: Request instance for CreateFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceSnapshot(self, request):
        """This API is used to create a system disk snapshot of the specified instance.

        :param request: Request instance for CreateInstanceSnapshot.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstanceSnapshotRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstanceSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        """This API is used to create one or more Lighthouse instances.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKeyPair(self, request):
        """This API is used to create a key pair.

        :param request: Request instance for CreateKeyPair.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlueprints(self, request):
        """This API is used to delete an image.

        :param request: Request instance for DeleteBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFirewallRules(self, request):
        """This API is used to delete a firewall rule of an instance.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the specified rule will be deleted directly.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.

        :param request: Request instance for DeleteFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKeyPairs(self, request):
        """This API is used to delete a key pair.

        :param request: Request instance for DeleteKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """This API is used to delete a snapshot.
        The snapshot must be in `NORMAL` status. To query the status of a snapshot, you can call the `DescribeSnapshots` API and see the `SnapshotState` field in the response.

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllScenes(self, request):
        """This API is used to query the list of scenes in all regions.

        :param request: Request instance for DescribeAllScenes.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeAllScenesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeAllScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlueprintInstances(self, request):
        """This API is used to query the information of an image instance.

        :param request: Request instance for DescribeBlueprintInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlueprintInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlueprintInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlueprints(self, request):
        """This API is used to query the information of an image.

        :param request: Request instance for DescribeBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBundleDiscount(self, request):
        """This API is used to query the discount information of a package.

        :param request: Request instance for DescribeBundleDiscount.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundleDiscountRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundleDiscountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBundleDiscount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBundleDiscountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBundles(self, request):
        """This API is used to query the information of a package.

        :param request: Request instance for DescribeBundles.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBundles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBundlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnAttachedInstances(self, request):
        """This API is used to query the information of instances associated with CCN.

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskConfigs(self, request):
        """This API is used to query the cloud disk configuration.

        :param request: Request instance for DescribeDiskConfigs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskConfigsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskDiscount(self, request):
        """This API is used to query the discount information of a cloud disk.

        :param request: Request instance for DescribeDiskDiscount.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskDiscountRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskDiscountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskDiscount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskDiscountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisks(self, request):
        """This API is used to query the information of one or more cloud disks.

        :param request: Request instance for DescribeDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisksDeniedActions(self, request):
        """This API is used to query the list of operation limits of one or more cloud disks.

        :param request: Request instance for DescribeDisksDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisksDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisksReturnable(self, request):
        """This API is used to query whether the specified cloud disk can be returned.

        :param request: Request instance for DescribeDisksReturnable.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksReturnableRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksReturnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisksReturnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksReturnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallRules(self, request):
        """This API is used to query the firewall rules of an instance.

        :param request: Request instance for DescribeFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallRulesTemplate(self, request):
        """This API is used to query a firewall rule template.

        :param request: Request instance for DescribeFirewallRulesTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallRulesTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallRulesTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralResourceQuotas(self, request):
        """This API is used to query the quota information of general resources.

        :param request: Request instance for DescribeGeneralResourceQuotas.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeGeneralResourceQuotasRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeGeneralResourceQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralResourceQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralResourceQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLoginKeyPairAttribute(self, request):
        """This API is used to query the attributes of the default login key of an instance.

        :param request: Request instance for DescribeInstanceLoginKeyPairAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceLoginKeyPairAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceLoginKeyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLoginKeyPairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLoginKeyPairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceVncUrl(self, request):
        """This API is used to query the URL for VNC login.

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

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceVncUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceVncUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query the details of one or multiple instances.

        * You can query the details of an instance according to its ID, name, or private IP.
        * For more information on filters, please see [Filters](https://intl.cloud.tencent.com/document/product/1207/47576?from_cn_redirect=1#Filter).
        * If no parameter is defined, the status of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        * The latest operation (LatestOperation) and the latest operation status (LatestOperationState) of the instance can be queried.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDeniedActions(self, request):
        """This API is used to query the list of operation limits of one or more instances.

        :param request: Request instance for DescribeInstancesDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDiskNum(self, request):
        """This API is used to query the number of cloud disks attached to instances.

        :param request: Request instance for DescribeInstancesDiskNum.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDiskNumRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDiskNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDiskNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDiskNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesReturnable(self, request):
        """This API is used to query whether the specified instance can be returned.

        :param request: Request instance for DescribeInstancesReturnable.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesReturnableRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesReturnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesReturnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesReturnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesTrafficPackages(self, request):
        """This API is used to query the traffic package details of one or more instances.

        :param request: Request instance for DescribeInstancesTrafficPackages.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeyPairs(self, request):
        """This API is used to query key pairs.

        :param request: Request instance for DescribeKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyInstanceBundles(self, request):
        """This API is used to query the list of package options of an instance.

        :param request: Request instance for DescribeModifyInstanceBundles.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeModifyInstanceBundlesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeModifyInstanceBundlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyInstanceBundles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyInstanceBundlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to query the information of regions.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResetInstanceBlueprints(self, request):
        """This API is used to query the image information of a reset instance.

        :param request: Request instance for DescribeResetInstanceBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeResetInstanceBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeResetInstanceBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResetInstanceBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResetInstanceBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenes(self, request):
        """This API is used to query the list of scenes.

        :param request: Request instance for DescribeScenes.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeScenesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """This API is used to query the list of snapshots.

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotsDeniedActions(self, request):
        """This API is used to query the list of operation limits of one or more snapshots.

        :param request: Request instance for DescribeSnapshotsDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query the list of AZs in a region.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCcn(self, request):
        """This API is used to disassociate with a CCN instance.

        :param request: Request instance for DetachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DetachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DetachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachDisks(self, request):
        """This API is used to detach one or more cloud disks.

        :param request: Request instance for DetachDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DetachDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DetachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateInstancesKeyPairs(self, request):
        """This API is used to unbind an instance from the specified key pair.

        * Only instances on LINUX_UNIX in [RUNNING, STOPPED] status are supported. Instances in `RUNNING` status will be forcibly shut down before unbinding.
        * After a key pair is unassociated from an instance, you can log in to the instance with password.
        * If no password was set, you cannot log in to the instance with SSH after unbinding. You can call the ResetInstancesPassword API to set a login password.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for DisassociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportKeyPair(self, request):
        """This API is used to import the specified key pair.

        :param request: Request instance for ImportKeyPair.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ImportKeyPairRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.ImportKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateBlueprint(self, request):
        """This API is used to query the price of a created image.

        :param request: Request instance for InquirePriceCreateBlueprint.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateBlueprintRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateBlueprintResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateBlueprint", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateBlueprintResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDisks(self, request):
        """This API is used to query the price of purchasing cloud disks.

        :param request: Request instance for InquirePriceCreateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateInstances(self, request):
        """This API is used to query the price of a created instance.

        :param request: Request instance for InquirePriceCreateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewDisks(self, request):
        """This API is used to query the price of renewing cloud disks.

        :param request: Request instance for InquirePriceRenewDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewInstances(self, request):
        """This API is used to query the price of renewing one or more instances.

        :param request: Request instance for InquirePriceRenewInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDisks(self, request):
        """This API is used to return one or more Lighthouse cloud disks.

        You can only perform this operation on `UNATTACHED` disks.
        After the successful call of the API, the cloud disk goes to the SHUTDOWN state.
        Up to 20 instances are supported at one time.
        This API is async. After the request is sent, a `RequestId` is returned. At this time, the operation is not completed yet. To check the result, you need to call  [DescribeDisks](https://intl.cloud.tencent.com/document/product/1207/66093?from_cn_redirect=1). If the latest operation status (LatestOperationState) of the disk is `SUCCESS`, the operation is successful.

        :param request: Request instance for IsolateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.IsolateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.IsolateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateInstances(self, request):
        """This API is used to return one or more Lighthouse instances.
        * Only `RUNNING` and `STOPPED` instances can be returned.
        * The instance status goes to `SHUTDOWN` after the API is called successfully.
        * Batch operations are supported. Up to 20 resources (including instances and data disks) can be returned in each request.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for IsolateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.IsolateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.IsolateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlueprintAttribute(self, request):
        """This API is used to modify an image attribute.

        :param request: Request instance for ModifyBlueprintAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyBlueprintAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyBlueprintAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlueprintAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlueprintAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisksAttribute(self, request):
        """This API is used to modify cloud disk attributes.

        :param request: Request instance for ModifyDisksAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisksAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisksAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisksRenewFlag(self, request):
        """This API is used to modify the configuration of auto-renewal of cloud disks.

        :param request: Request instance for ModifyDisksRenewFlag.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksRenewFlagRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisksRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisksRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFirewallRuleDescription(self, request):
        """This API is used to modify the description of a single firewall rule.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the description of the specified rule will be modified directly.

        In the `FirewallRule` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.

        :param request: Request instance for ModifyFirewallRuleDescription.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRuleDescriptionRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRuleDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFirewallRuleDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFirewallRuleDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFirewallRules(self, request):
        """This API is used to reset the firewall rules of an instance.

        This API deletes all firewall rules of the current instance first and then adds new rules.

        * `FirewallVersion` is used to specify the version of the firewall to be manipulated. If the `FirewallVersion` value passed in is not equal to the current latest version of the firewall, a failure will be returned. If `FirewallVersion` is not passed in, the specified rule will be reset directly.

        In the `FirewallRules` parameter:
        * Valid values of the `Protocol` field include `TCP`, `UDP`, `ICMP`, and `ALL`.
        * For the `Port` field, you can enter only `ALL`, a single port number, several port numbers separated by commas, or a port range indicated by two port numbers separated by a minus sign. If `Port` is a range, the port number on the left of the minus sign must be smaller than the one on the right. If `Protocol` is not `TCP` or `UDP`, `Port` can only be empty or `ALL`. The length of the `Port` field cannot exceed 64 characters.
        * For the `CidrBlock` field, you can enter any string that conforms to the CIDR format standard. Multi-Tenant network isolation rules take precedence over private network rules in the firewall.
        * For the `Action` field, you can enter only `ACCEPT` or `DROP`.
        * The length of the `FirewallRuleDescription` field cannot exceed 64 characters.

        :param request: Request instance for ModifyFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesAttribute(self, request):
        """This API is used to modify an instance attribute.
        * The instance name is used only for users’ convenience.
        * Batch operations are supported. The maximum number of instances in each request is 100.

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesBundle(self, request):
        """This API is used change one or more Lighthouse instance bundles.
        * Only `RUNNING` and `STOPPED` instances can be changed.
        * Batch operations are supported. The maximum number of instances in each request is 30.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for ModifyInstancesBundle.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesBundleRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesBundleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesBundle", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesBundleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesLoginKeyPairAttribute(self, request):
        """This API is used to set the attributes of the default login key pair of an instance.


        :param request: Request instance for ModifyInstancesLoginKeyPairAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesLoginKeyPairAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesLoginKeyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesLoginKeyPairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesLoginKeyPairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesRenewFlag(self, request):
        """This API is used to change the auto-renewal setting of monthly-subscribed instances.

        * Instances with auto-renewal enabled are automatically renewed on a monthly basis upon the expiration.
        * Batch operations are supported. Up to 100 instances per request is allowed.

        :param request: Request instance for ModifyInstancesRenewFlag.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesRenewFlagRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotAttribute(self, request):
        """This API is used to modify the attributes of a snapshot.
        <li>The snapshot name is used only for users’ convenience.</li>

        :param request: Request instance for ModifySnapshotAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifySnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifySnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootInstances(self, request):
        """This API is used to restart instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `REBOOTING` when the API is called successfully and will become `RUNNING` when the instance is successfully restarted.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDisks(self, request):
        """This API is used to renew one or more Lighthouse cloud disks.

        This operation can only be performed on data disks with the status of `ATTACHED`, `UNATTACHED` or `SHUTDOWN`.
        Up to 50 cloud disks are supported at one time.
        This API is async. After the request is sent, a `RequestId` is returned. At this time, the operation is not completed yet. To check the result, you need to call  [DescribeDisks](https://intl.cloud.tencent.com/document/product/1207/66093?from_cn_redirect=1). If the latest operation status (LatestOperationState) of the disk is `SUCCESS`, the operation is successful.

        :param request: Request instance for RenewDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RenewDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDisks", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstances(self, request):
        """This API is used to renew one or more Lighthouse instances.
        * You can only perform this operation on instances whose status is `RUNNING`, `STOPPED` and `SHUTDOWN`.
        * Batch operations are supported. Up to 100 instances are supported in each request.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for RenewInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RenewInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAttachCcn(self, request):
        """This API is used to apply for association again after a CCN instance association application expires.

        :param request: Request instance for ResetAttachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetAttachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetAttachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAttachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAttachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstance(self, request):
        """This API is used to reinstall the image on the specified instance.

        * If you specify a `BlueprintId`, the specified image is used; otherwise, the image used by the current instance is used.
        * The system disk will be formatted and reset. Therefore, make sure that no important files are stored on the system disk.
        * Currently, this API does not support switching the operating system between `LINUX_UNIX` and `WINDOWS` for instances.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for ResetInstance.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstancesPassword(self, request):
        """This API is used to reset the password of the instance OS to a user-specified password.
        * You can only use this API to modify the password of the admin account. The name of the admin account varies by OS (on Windows, it is `Administrator`; on Ubuntu, it is `ubuntu`; on other systems, it is `root`).
        * Batch operations are supported. You can reset the passwords of multiple instances to the same one. The maximum number of instances in each request is 100.
        * It’s recommended to shut down the instance first and then reset the password. If the instance is running, this API will try to shut it down normally. If the attempt fails, it will force to instance to shut down.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.
        Note: Just like powering off a physical PC, a forced shutdown may cause data loss or the corruption of file system.

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstancesPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstances(self, request):
        """This API is used to start one or more instances.

        * You can only perform this operation on instances whose status is `STOPPED`.
        * The instance status will become `STARTING` when the API is called successfully and will become `RUNNING` when the instance is successfully started.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstances(self, request):
        """This API is used to shut down one or more instances.
        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `STOPPING` when the API is called successfully and will become `STOPPED` when the instance is successfully shut down.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDisks(self, request):
        """This API is used to terminate one or more cloud disk.

        :param request: Request instance for TerminateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.TerminateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.TerminateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        """This API is used to terminate one or more instances.

        * Instances in `SHUTDOWN` status can be terminated through this API and cannot be recovered.
        * Batch operations are supported. The allowed maximum number of instances in each request is 100.
        * This API is async. After the request is sent successfully, a `RequestId` will be returned. At this time, the operation is not completed immediately. The result of the instance operation can be queried by calling the `DescribeInstances` API. If the latest operation status (LatestOperationState) of the instance is `SUCCESS`, the operation is successful.

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))