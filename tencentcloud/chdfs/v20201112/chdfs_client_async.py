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
from tencentcloud.chdfs.v20201112 import models
from typing import Dict


class ChdfsClient(AbstractClient):
    _apiVersion = '2020-11-12'
    _endpoint = 'chdfs.intl.tencentcloudapi.com'
    _service = 'chdfs'

    async def AssociateAccessGroups(
            self,
            request: models.AssociateAccessGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateAccessGroupsResponse:
        """
        This API is used to bind multiple permission groups to a mount point.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateAccessGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateAccessGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessGroup(
            self,
            request: models.CreateAccessGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAccessGroupResponse:
        """
        This API is used to create a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessRules(
            self,
            request: models.CreateAccessRulesRequest,
            opts: Dict = None,
    ) -> models.CreateAccessRulesResponse:
        """
        This API is used to batch create permission rules. You don't need to enter the permission rule IDs and creation time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileSystem(
            self,
            request: models.CreateFileSystemRequest,
            opts: Dict = None,
    ) -> models.CreateFileSystemResponse:
        """
        This API is used to create a file system (asynchronously).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifeCycleRules(
            self,
            request: models.CreateLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.CreateLifeCycleRulesResponse:
        """
        This API is used to batch create lifecycle rules. You don't need to enter the lifecycle rule IDs and creation time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMountPoint(
            self,
            request: models.CreateMountPointRequest,
            opts: Dict = None,
    ) -> models.CreateMountPointResponse:
        """
        This API is used to create a mount point for a successfully created file system.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRestoreTasks(
            self,
            request: models.CreateRestoreTasksRequest,
            opts: Dict = None,
    ) -> models.CreateRestoreTasksResponse:
        """
        This API is used to batch create restoration tasks. You don't need to enter the restoration task IDs, status, and creation time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRestoreTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRestoreTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessGroup(
            self,
            request: models.DeleteAccessGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessGroupResponse:
        """
        This API is used to delete a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessRules(
            self,
            request: models.DeleteAccessRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessRulesResponse:
        """
        This API is used to batch delete permission rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileSystem(
            self,
            request: models.DeleteFileSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteFileSystemResponse:
        """
        This API is used to delete a file system. Non-empty file systems cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLifeCycleRules(
            self,
            request: models.DeleteLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteLifeCycleRulesResponse:
        """
        This API is used to batch delete lifecycle rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMountPoint(
            self,
            request: models.DeleteMountPointRequest,
            opts: Dict = None,
    ) -> models.DeleteMountPointResponse:
        """
        This API is used to delete a mount point.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessGroup(
            self,
            request: models.DescribeAccessGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessGroupResponse:
        """
        This API is used to view the details of a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessGroups(
            self,
            request: models.DescribeAccessGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessGroupsResponse:
        """
        This API is used to view the list of permission groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRules(
            self,
            request: models.DescribeAccessRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRulesResponse:
        """
        This API is used to view the list of permission rules by permission group ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystem(
            self,
            request: models.DescribeFileSystemRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemResponse:
        """
        This API is used to view the details of a file system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystems(
            self,
            request: models.DescribeFileSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemsResponse:
        """
        This API is used to view the list of file systems.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifeCycleRules(
            self,
            request: models.DescribeLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLifeCycleRulesResponse:
        """
        This API is used to view the list of lifecycle rules by file system ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountPoint(
            self,
            request: models.DescribeMountPointRequest,
            opts: Dict = None,
    ) -> models.DescribeMountPointResponse:
        """
        This API is used to view the details of a mount point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountPoints(
            self,
            request: models.DescribeMountPointsRequest,
            opts: Dict = None,
    ) -> models.DescribeMountPointsResponse:
        """
        This API is used to view the list of mount points.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTags(
            self,
            request: models.DescribeResourceTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsResponse:
        """
        This API is used to view the list of resource tags by file system ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTasks(
            self,
            request: models.DescribeRestoreTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTasksResponse:
        """
        This API is used to view the list of restoration tasks by file system ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateAccessGroups(
            self,
            request: models.DisassociateAccessGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateAccessGroupsResponse:
        """
        This API is used to unbind multiple permission groups from a mount point.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateAccessGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateAccessGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessGroup(
            self,
            request: models.ModifyAccessGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessGroupResponse:
        """
        This API is used to modify the attributes of a permission group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessRules(
            self,
            request: models.ModifyAccessRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessRulesResponse:
        """
        This API is used to batch modify the attributes of permission rules, such as address, access mode, and priority. You must specify the permission rule IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileSystem(
            self,
            request: models.ModifyFileSystemRequest,
            opts: Dict = None,
    ) -> models.ModifyFileSystemResponse:
        """
        This API is used to modify the attributes of a successfully created file system.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLifeCycleRules(
            self,
            request: models.ModifyLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyLifeCycleRulesResponse:
        """
        This API is used to batch modify the attributes of lifecycle rules, such as name, path, transition list, and status. You must specify the lifecycle rule IDs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMountPoint(
            self,
            request: models.ModifyMountPointRequest,
            opts: Dict = None,
    ) -> models.ModifyMountPointResponse:
        """
        This API is used to modify the attributes of a mount point.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceTags(
            self,
            request: models.ModifyResourceTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceTagsResponse:
        """
        This API is used to modify the list of resource tags by overwriting them all.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)