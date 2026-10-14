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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.databuddy.v20260715 import models


class DatabuddyClient(AbstractClient):
    _apiVersion = '2026-07-15'
    _endpoint = 'databuddy.intl.tencentcloudapi.com'
    _service = 'databuddy'


    def AddConsoleUsers(self, request):
        r"""Add a console user

        :param request: Request instance for AddConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AddConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.AddConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddWorkspaceGroups(self, request):
        r"""This API is used to add a user group to a workspace.

        :param request: Request instance for AddWorkspaceGroups.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.AddWorkspaceGroupsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AddWorkspaceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddWorkspaceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AddWorkspaceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddWorkspaceUsers(self, request):
        r"""This API is used to create user groups.

        :param request: Request instance for AddWorkspaceUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.AddWorkspaceUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.AddWorkspaceUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddWorkspaceUsers", params, headers=headers)
            response = json.loads(body)
            model = models.AddWorkspaceUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCatalog(self, request):
        r"""This API is used to create a data catalog.

        :param request: Request instance for CreateCatalog.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateCatalogRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateCatalogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCatalog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCatalogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsoleGroup(self, request):
        r"""Create a console user group

        :param request: Request instance for CreateConsoleGroup.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateConsoleGroupRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateConsoleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFile(self, request):
        r"""Create a new file (Notebook/SQL/Python, etc.) in the workspace file tree of Studio (unified development IDE), and return the complete meta-information of the file upon success.

        **Prerequisite**
        1. WorkspaceId corresponds to an existent workspace, and the caller is a space member of this workspace;
        2. The parent folder corresponding to ParentFolderPath must exist, and the caller must have write permission on it (pass `/` for the root directory);
        3. FileName must be unique under the same parent folder, including suffix comparison.
        4. The FileName suffix must be consistent with FileType (`.ipynb`↔`NOTEBOOK_FILE`, `.sql`↔`SQL_FILE`);
        5. To create with file content, pass it through Storage (large files are transferred via COS, and small files are placed in Storage.Content).

        :param request: Request instance for CreateFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFolder(self, request):
        r"""Create a folder

        :param request: Request instance for CreateFolder.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateFolderRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSchema(self, request):
        r"""Create a schema

        :param request: Request instance for CreateSchema.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateSchemaRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchema", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflow(self, request):
        r"""Create a workflow

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkspace(self, request):
        r"""This API is used to create a workspace.

        :param request: Request instance for CreateWorkspace.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkspaceRole(self, request):
        r"""Creates a workspace role

        :param request: Request instance for CreateWorkspaceRole.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRoleRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.CreateWorkspaceRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCatalog(self, request):
        r"""Delete a catalog.

        :param request: Request instance for DeleteCatalog.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteCatalogRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteCatalogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCatalog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCatalogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsoleGroups(self, request):
        r"""Delete a console user group

        :param request: Request instance for DeleteConsoleGroups.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteConsoleGroupsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteConsoleGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsoleGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsoleGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFile(self, request):
        r"""Move the file to Recycle Bin (soft deletion) and clear its version history and execution result snapshots.

        **Prerequisite**
        1. The file corresponding to FileId must exist and be in active status;
        2. The caller has permission to delete the file;
        3. The file hasn't been referenced by a workflow task.

        **Error codes (Module are all `Studio`)**

        | Error Code (Code) | InnerCode | Description | Handling Suggestion |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | lack of WorkspaceId | Please input WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | lack of FileId | Please import FileId |
        | `InvalidParameterValue.FileType` | 1030102 | FileType value not supported | FileType takes FILE/NOTEBOOK_FILE/SQL_FILE |
        | `ResourceNotFound.FileNotFound` | 1030203 | File does not exist or has been deleted | Please confirm the FileId |
        | `ResourceInUse.FileReferencedByTask` | 1030204 | The file is referenced by a workflow task and cannot be deleted. | Disassociate the task reference first. |
        | `UnauthorizedOperation.FileDeleteDenied` | 1030303 | No deletion permission for this file | Contact the file owner or space admin for authorization |
        | `InternalError` | 1030900 | Internal service error | Please carry the RequestId and contact support |

        :param request: Request instance for DeleteFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFolder(self, request):
        r"""Delete folder

        :param request: Request instance for DeleteFolder.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteFolderRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSchema(self, request):
        r"""Delete schema

        :param request: Request instance for DeleteSchema.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteSchemaRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSchema", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflow(self, request):
        r"""Deletes a workflow

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkspace(self, request):
        r"""Delete a workspace.

        :param request: Request instance for DeleteWorkspace.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkspaceRole(self, request):
        r"""Delete a workspace role.

        :param request: Request instance for DeleteWorkspaceRole.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRoleRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.DeleteWorkspaceRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkspaceRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkspaceRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCatalog(self, request):
        r"""Query catalog description

        :param request: Request instance for GetCatalog.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetCatalogRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetCatalogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCatalog", params, headers=headers)
            response = json.loads(body)
            model = models.GetCatalogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFile(self, request):
        r"""Get the file's metadata, optionally including file content, and read historical snapshots by version.

        **Prerequisite**
        1. Pass at least one of FileId and FilePath. If both are passed, FileId takes precedence.
        2. The corresponding file must exist, and the caller must have read permission for the file;
        3. If VersionId is passed, the version must exist.

        **Error codes (Module: `Studio`)**

        | Error Code | Inner Code | Description | Handling Suggestion |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | Lack of WorkspaceId | Please input WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | FileId and FilePath cannot be empty at the same time | Pass at least one of FileId and FilePath |
        | `InvalidParameterValue.FileType` | 1030102 | FileType value unsupported | FileType takes FILE/NOTEBOOK_FILE/SQL_FILE |
        | `ResourceNotFound.FileNotFound` | 1030203 | File does not exist or has been deleted | Confirm the FileId or FilePath |
        | `ResourceNotFound.FileVersionNotFound` | 1030205 | The specified file version does not exist | Confirm the VersionId or call ListFileVersions to retrieve |
        | `UnauthorizedOperation.FileReadDenied` | 1030304 | No read permission for this file | Contact the file owner or space admin for authorization |
        | `InternalError` | 1030900 | Internal service error | Please carry the RequestId and contact support |

        :param request: Request instance for GetFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFolder(self, request):
        r"""Get folder details.

        :param request: Request instance for GetFolder.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetFolderRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFolder", params, headers=headers)
            response = json.loads(body)
            model = models.GetFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflow(self, request):
        r"""This API is used to query workflow details.

        :param request: Request instance for GetWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflowRun(self, request):
        r"""Queries workflow running details.

        :param request: Request instance for GetWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkflowTaskRun(self, request):
        r"""Query task execution details

        :param request: Request instance for GetWorkflowTaskRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkflowTaskRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkflowTaskRun", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkflowTaskRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWorkspace(self, request):
        r"""Queries the details of a workspace.

        :param request: Request instance for GetWorkspace.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.GetWorkspaceRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.GetWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.GetWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillWorkflowRun(self, request):
        r"""Terminate the operation of a workflow.

        :param request: Request instance for KillWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.KillWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.KillWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.KillWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCatalogs(self, request):
        r"""Pagination fetch data catalog list

        :param request: Request instance for ListCatalogs.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListCatalogsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListCatalogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCatalogs", params, headers=headers)
            response = json.loads(body)
            model = models.ListCatalogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConsoleGroupUsers(self, request):
        r"""Queries the console user group member list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.

        :param request: Request instance for ListConsoleGroupUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConsoleGroupUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListConsoleGroupUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConsoleGroups(self, request):
        r"""Queries the console user group list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.

        :param request: Request instance for ListConsoleGroups.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConsoleGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListConsoleGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConsoleRoles(self, request):
        r"""Queries the console role list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.

        :param request: Request instance for ListConsoleRoles.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleRolesRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConsoleRoles", params, headers=headers)
            response = json.loads(body)
            model = models.ListConsoleRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConsoleUsers(self, request):
        r"""Queries the console user list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.

        :param request: Request instance for ListConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFiles(self, request):
        r"""Get the folder and file list

        :param request: Request instance for ListFiles.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListFilesRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ListFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSchemas(self, request):
        r"""Get schema list

        :param request: Request instance for ListSchemas.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListSchemasRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListSchemasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSchemas", params, headers=headers)
            response = json.loads(body)
            model = models.ListSchemasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowRuns(self, request):
        r"""Workflow run list

        :param request: Request instance for ListWorkflowRuns.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowTaskRuns(self, request):
        r"""Query the historical operation list of workflow tasks

        :param request: Request instance for ListWorkflowTaskRuns.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowTaskRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowTaskRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowTaskRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflows(self, request):
        r"""This API is used to query the list of workflows.

        :param request: Request instance for ListWorkflows.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkspaceGroups(self, request):
        r"""This API is used to query the list of user groups in a workspace.

        :param request: Request instance for ListWorkspaceGroups.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspaceGroupsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspaceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkspaceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkspaceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkspaceUsers(self, request):
        r"""Queries the list of users in a workspace.

        :param request: Request instance for ListWorkspaceUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspaceUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspaceUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkspaceUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkspaceUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkspaces(self, request):
        r"""Queries the workspace list.

        :param request: Request instance for ListWorkspaces.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspacesRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.ListWorkspacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkspaces", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkspacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveConsoleUsers(self, request):
        r"""<p>Batch remove console users (up to 10 at a time; pre-verification rejects the entire request if any fails; during the Execution Phase, a single failure does not interrupt subsequent deletion, and success or failure is determined by SuccessUins/FailItems)</p>

        :param request: Request instance for RemoveConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RemoveConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWorkspaceGroups(self, request):
        r"""Remove a user group from a workspace.

        :param request: Request instance for RemoveWorkspaceGroups.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RemoveWorkspaceGroupsRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RemoveWorkspaceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWorkspaceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWorkspaceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunWorkflowRun(self, request):
        r"""Rerun a workflow

        :param request: Request instance for RerunWorkflowRun.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RerunWorkflowRunRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RerunWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.RerunWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunWorkflow(self, request):
        r"""Runs the workflow

        :param request: Request instance for RunWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.RunWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.RunWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.RunWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCompute(self, request):
        r"""Start up the computational resource.

        :param request: Request instance for StartCompute.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.StartComputeRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.StartComputeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCompute", params, headers=headers)
            response = json.loads(body)
            model = models.StartComputeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCompute(self, request):
        r"""Terminate computational resources

        :param request: Request instance for StopCompute.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.StopComputeRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.StopComputeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCompute", params, headers=headers)
            response = json.loads(body)
            model = models.StopComputeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindWorkflowBundle(self, request):
        r"""Unbind workflow Bundle info
        Description: This interface is semantically equivalent to Detach in the standard verb list. The name Unbind is retained for compatibility with existing product forms.

        :param request: Request instance for UnbindWorkflowBundle.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UnbindWorkflowBundleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindWorkflowBundle", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindWorkflowBundleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConsoleGroup(self, request):
        r"""Modify a console user group

        :param request: Request instance for UpdateConsoleGroup.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleGroupRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConsoleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConsoleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConsoleUsers(self, request):
        r"""Modify a console user role

        :param request: Request instance for UpdateConsoleUsers.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateConsoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConsoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConsoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFile(self, request):
        r"""Update file contents and running configuration (computational resource, default catalog/schema, parameters), and return the file metadata after the update.

        **Prerequisite**
        1. The file corresponding to FileId must exist and be in active status;
        2. The caller has write permission on the file;
        3. To update only the configuration, do not pass in Storage. To update only the content, do not pass in FileConfig.
        4. If FileConfig.ResourceId is not empty, the match between the resource type and file type will be validated.

        **Error codes (Module: `Studio`)**

        | Error Code (Code) | InnerCode | Description | Handling Suggestions |
        | --- | --- | --- | --- |
        | `MissingParameter.WorkspaceId` | 1030001 | lack of WorkspaceId | Please input WorkspaceId |
        | `MissingParameter.FileId` | 1030003 | lack of FileId | Please import FileId |
        | `InvalidParameterValue.FileType` | 1030102 | FileType value not supported | FileType takes FILE/NOTEBOOK_FILE/SQL_FILE |
        | `InvalidParameterValue.ResourceId` | 1030104 | Compute resource type and file type mismatch | Select a computational resource for Python/Notebook and a data analysis resource for SQL |
        | `ResourceNotFound.FileNotFound` | 1030203 | File does not exist or has been deleted | confirm the FileId or call GetFile to check the file status |
        | `UnauthorizedOperation.FileWriteDenied` | 1030302 | No write permission for this file | Contact the file owner or space admin for authorization |
        | `FailedOperation.FileStorageUpdateFailed` | 1030401 | Failed to write file content to storage | Try again later. If the failure persists, contact support with the RequestId. |
        | `InternalError` | 1030900 | Internal service error | Please carry the RequestId and contact support |

        :param request: Request instance for UpdateFile.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateFileRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFolder(self, request):
        r"""Update folder (supports rename and move)

        :param request: Request instance for UpdateFolder.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateFolderRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFolder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflow(self, request):
        r"""Updating a Workflow

        :param request: Request instance for UpdateWorkflow.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkspace(self, request):
        r"""Modifies a workspace

        :param request: Request instance for UpdateWorkspace.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkspaceRole(self, request):
        r"""Updates a workspace role

        :param request: Request instance for UpdateWorkspaceRole.
        :type request: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRoleRequest`
        :rtype: :class:`tencentcloud.databuddy.v20260715.models.UpdateWorkspaceRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkspaceRole", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkspaceRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))