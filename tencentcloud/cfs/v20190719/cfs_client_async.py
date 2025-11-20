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
from tencentcloud.cfs.v20190719 import models
from typing import Dict


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.intl.tencentcloudapi.com'
    _service = 'cfs'

    async def BindAutoSnapshotPolicy(
            self,
            request: models.BindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.BindAutoSnapshotPolicyResponse:
        """
        This API is used to bind one or multiple file systems to a snapshot policy. A file system can be bound to only one policy.
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoSnapshotPolicy(
            self,
            request: models.CreateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoSnapshotPolicyResponse:
        """
        This API is used to create a scheduled snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsFileSystem(
            self,
            request: models.CreateCfsFileSystemRequest,
            opts: Dict = None,
    ) -> models.CreateCfsFileSystemResponse:
        """
        This API is used to create a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsPGroup(
            self,
            request: models.CreateCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCfsPGroupResponse:
        """
        This API is used to create a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsRule(
            self,
            request: models.CreateCfsRuleRequest,
            opts: Dict = None,
    ) -> models.CreateCfsRuleResponse:
        """
        This API is used to create a permission group rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsSnapshot(
            self,
            request: models.CreateCfsSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateCfsSnapshotResponse:
        """
        This API is used to create a file system snapshot.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrationTask(
            self,
            request: models.CreateMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationTaskResponse:
        """
        This API is used to create a migration task.
        To use this API, submit a ticket for us to add you to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoSnapshotPolicy(
            self,
            request: models.DeleteAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoSnapshotPolicyResponse:
        """
        This API is used to delete a scheduled snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsFileSystem(
            self,
            request: models.DeleteCfsFileSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsFileSystemResponse:
        """
        This API is used to delete a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsPGroup(
            self,
            request: models.DeleteCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsPGroupResponse:
        """
        This API is used to delete a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsRule(
            self,
            request: models.DeleteCfsRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsRuleResponse:
        """
        This API is used to delete a permission group rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsSnapshot(
            self,
            request: models.DeleteCfsSnapshotRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsSnapshotResponse:
        """
        This API is used to delete a file system snapshot.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigrationTask(
            self,
            request: models.DeleteMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrationTaskResponse:
        """
        This API is used to delete a migration task.
        To use this API, submit a ticket for us to add you to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMountTarget(
            self,
            request: models.DeleteMountTargetRequest,
            opts: Dict = None,
    ) -> models.DeleteMountTargetResponse:
        """
        This API is used to delete a mount target.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMountTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMountTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoSnapshotPolicies(
            self,
            request: models.DescribeAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoSnapshotPoliciesResponse:
        """
        This API is used to query the list of scheduled snapshot policies of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableZoneInfo(
            self,
            request: models.DescribeAvailableZoneInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableZoneInfoResponse:
        """
        This API is used to query the availability of a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableZoneInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableZoneInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBucketList(
            self,
            request: models.DescribeBucketListRequest,
            opts: Dict = None,
    ) -> models.DescribeBucketListResponse:
        """
        This API is used to get the list of data source buckets.
        To use this API, submit a ticket for us to add you to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBucketList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBucketListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsFileSystemClients(
            self,
            request: models.DescribeCfsFileSystemClientsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsFileSystemClientsResponse:
        """
        This API is used to query clients on which this file system is mounted. To do so, the client needs to have the CFS monitoring plugin installed.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsFileSystemClients"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsFileSystemClientsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsFileSystems(
            self,
            request: models.DescribeCfsFileSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsFileSystemsResponse:
        """
        This API is used to query file systems.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsFileSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsFileSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsPGroups(
            self,
            request: models.DescribeCfsPGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsPGroupsResponse:
        """
        This API is used to query the list of permission groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsPGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsPGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsRules(
            self,
            request: models.DescribeCfsRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsRulesResponse:
        """
        This API is used to query the list of permission group rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsServiceStatus(
            self,
            request: models.DescribeCfsServiceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsServiceStatusResponse:
        """
        This API is used to query the status of the CFS service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsSnapshotOverview(
            self,
            request: models.DescribeCfsSnapshotOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsSnapshotOverviewResponse:
        """
        This API is used to get the snapshot overview of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsSnapshotOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsSnapshotOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsSnapshots(
            self,
            request: models.DescribeCfsSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsSnapshotsResponse:
        """
        This API is used to query the list of snapshots of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationTasks(
            self,
            request: models.DescribeMigrationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationTasksResponse:
        """
        This API is used to get the list of migration tasks.
        To use this API, submit a ticket for us to add you to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountTargets(
            self,
            request: models.DescribeMountTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeMountTargetsResponse:
        """
        This API is used to query the mount targets of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotOperationLogs(
            self,
            request: models.DescribeSnapshotOperationLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotOperationLogsResponse:
        """
        This API is used to query the operation logs of a snapshot.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotOperationLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotOperationLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileSystemAutoScaleUpRule(
            self,
            request: models.ModifyFileSystemAutoScaleUpRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFileSystemAutoScaleUpRuleResponse:
        """
        This API is used to modify the scaling policy of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileSystemAutoScaleUpRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileSystemAutoScaleUpRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpFileSystem(
            self,
            request: models.ScaleUpFileSystemRequest,
            opts: Dict = None,
    ) -> models.ScaleUpFileSystemResponse:
        """
        This API is used to scale up a Turbo file system.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignUpCfsService(
            self,
            request: models.SignUpCfsServiceRequest,
            opts: Dict = None,
    ) -> models.SignUpCfsServiceResponse:
        """
        This API is used to activate the CFS service.
        """
        
        kwargs = {}
        kwargs["action"] = "SignUpCfsService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignUpCfsServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrationTask(
            self,
            request: models.StopMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.StopMigrationTaskResponse:
        """
        This API is used to stop a migration task.
        To use this API, submit a ticket for us to add you to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoSnapshotPolicy(
            self,
            request: models.UnbindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoSnapshotPolicyResponse:
        """
        This API is used to unbind a snapshot policy from a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAutoSnapshotPolicy(
            self,
            request: models.UpdateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateAutoSnapshotPolicyResponse:
        """
        This API is used to update a scheduled snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemName(
            self,
            request: models.UpdateCfsFileSystemNameRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemNameResponse:
        """
        This API is used to update a file system name.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemPGroup(
            self,
            request: models.UpdateCfsFileSystemPGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemPGroupResponse:
        """
        This API is used to update the permission group used by a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemSizeLimit(
            self,
            request: models.UpdateCfsFileSystemSizeLimitRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemSizeLimitResponse:
        """
        This API is used to update the capacity limit of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemSizeLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemSizeLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsPGroup(
            self,
            request: models.UpdateCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsPGroupResponse:
        """
        This API is used to update the information of a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsRule(
            self,
            request: models.UpdateCfsRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsRuleResponse:
        """
        This API is used to update a permission rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsSnapshotAttribute(
            self,
            request: models.UpdateCfsSnapshotAttributeRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsSnapshotAttributeResponse:
        """
        This API is used to update the name and retention period of a file system snapshot.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsSnapshotAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsSnapshotAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)