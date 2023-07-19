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
from tencentcloud.chdfs.v20201112 import models


class ChdfsClient(AbstractClient):
    _apiVersion = '2020-11-12'
    _endpoint = 'chdfs.tencentcloudapi.com'
    _service = 'chdfs'


    def AssociateAccessGroups(self, request):
        """This API is used to bind multiple permission groups to a mount point.

        :param request: Request instance for AssociateAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.AssociateAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.AssociateAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateAccessGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateAccessGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessGroup(self, request):
        """This API is used to create a permission group.

        :param request: Request instance for CreateAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessRules(self, request):
        """This API is used to batch create permission rules. You don't need to enter the permission rule IDs and creation time.

        :param request: Request instance for CreateAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileSystem(self, request):
        """This API is used to create a file system (asynchronously).

        :param request: Request instance for CreateFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLifeCycleRules(self, request):
        """This API is used to batch create lifecycle rules. You don't need to enter the lifecycle rule IDs and creation time.

        :param request: Request instance for CreateLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLifeCycleRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLifeCycleRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMountPoint(self, request):
        """This API is used to create a mount point for a successfully created file system.

        :param request: Request instance for CreateMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateMountPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMountPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMountPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRestoreTasks(self, request):
        """This API is used to batch create restoration tasks. You don't need to enter the restoration task IDs, status, and creation time.

        :param request: Request instance for CreateRestoreTasks.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateRestoreTasksRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateRestoreTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRestoreTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRestoreTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccessGroup(self, request):
        """This API is used to delete a permission group.

        :param request: Request instance for DeleteAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DeleteAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DeleteAccessGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccessGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccessRules(self, request):
        """This API is used to batch delete permission rules.

        :param request: Request instance for DeleteAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DeleteAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DeleteAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFileSystem(self, request):
        """This API is used to delete a file system. Non-empty file systems cannot be deleted.

        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DeleteFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DeleteFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLifeCycleRules(self, request):
        """This API is used to batch delete lifecycle rules.

        :param request: Request instance for DeleteLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DeleteLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DeleteLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLifeCycleRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLifeCycleRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMountPoint(self, request):
        """This API is used to delete a mount point.

        :param request: Request instance for DeleteMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DeleteMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DeleteMountPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMountPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMountPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessGroup(self, request):
        """This API is used to view the details of a permission group.

        :param request: Request instance for DescribeAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessGroups(self, request):
        """This API is used to view the list of permission groups.

        :param request: Request instance for DescribeAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessRules(self, request):
        """This API is used to view the list of permission rules by permission group ID.

        :param request: Request instance for DescribeAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileSystem(self, request):
        """This API is used to view the details of a file system.

        :param request: Request instance for DescribeFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileSystems(self, request):
        """This API is used to view the list of file systems.

        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLifeCycleRules(self, request):
        """This API is used to view the list of lifecycle rules by file system ID.

        :param request: Request instance for DescribeLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLifeCycleRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLifeCycleRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountPoint(self, request):
        """This API is used to view the details of a mount point.

        :param request: Request instance for DescribeMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountPoints(self, request):
        """This API is used to view the list of mount points.

        :param request: Request instance for DescribeMountPoints.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountPoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountPointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTags(self, request):
        """This API is used to view the list of resource tags by file system ID.

        :param request: Request instance for DescribeResourceTags.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeResourceTagsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeResourceTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTasks(self, request):
        """This API is used to view the list of restoration tasks by file system ID.

        :param request: Request instance for DescribeRestoreTasks.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeRestoreTasksRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeRestoreTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateAccessGroups(self, request):
        """This API is used to unbind multiple permission groups from a mount point.

        :param request: Request instance for DisassociateAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DisassociateAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DisassociateAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateAccessGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateAccessGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessGroup(self, request):
        """This API is used to modify the attributes of a permission group.

        :param request: Request instance for ModifyAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessRules(self, request):
        """This API is used to batch modify the attributes of permission rules, such as address, access mode, and priority. You must specify the permission rule IDs.

        :param request: Request instance for ModifyAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileSystem(self, request):
        """This API is used to modify the attributes of a successfully created file system.

        :param request: Request instance for ModifyFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLifeCycleRules(self, request):
        """This API is used to batch modify the attributes of lifecycle rules, such as name, path, transition list, and status. You must specify the lifecycle rule IDs.

        :param request: Request instance for ModifyLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLifeCycleRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLifeCycleRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMountPoint(self, request):
        """This API is used to modify the attributes of a mount point.

        :param request: Request instance for ModifyMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyMountPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMountPoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMountPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceTags(self, request):
        """This API is used to modify the list of resource tags by overwriting them all.

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyResourceTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))