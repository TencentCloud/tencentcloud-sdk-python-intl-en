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
from tencentcloud.databuddy.v20260715 import models
from typing import Dict


class DatabuddyClient(AbstractClient):
    _apiVersion = '2026-07-15'
    _endpoint = 'databuddy.intl.tencentcloudapi.com'
    _service = 'databuddy'

    async def AddConsoleUsers(
            self,
            request: models.AddConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.AddConsoleUsersResponse:
        """
        Add a console user
        """
        
        kwargs = {}
        kwargs["action"] = "AddConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddWorkspaceGroups(
            self,
            request: models.AddWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.AddWorkspaceGroupsResponse:
        """
        This API is used to add a user group to a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "AddWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddWorkspaceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddWorkspaceUsers(
            self,
            request: models.AddWorkspaceUsersRequest,
            opts: Dict = None,
    ) -> models.AddWorkspaceUsersResponse:
        """
        This API is used to create user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "AddWorkspaceUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddWorkspaceUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCatalog(
            self,
            request: models.CreateCatalogRequest,
            opts: Dict = None,
    ) -> models.CreateCatalogResponse:
        """
        This API is used to create a data catalog.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsoleGroup(
            self,
            request: models.CreateConsoleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsoleGroupResponse:
        """
        Create a console user group
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsoleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsoleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFile(
            self,
            request: models.CreateFileRequest,
            opts: Dict = None,
    ) -> models.CreateFileResponse:
        """
        Create a new file (Notebook/SQL/Python, etc.) in the workspace file tree of Studio (unified development IDE), and return the complete meta-information of the file upon success.

        **Prerequisite**
        1. WorkspaceId corresponds to an existent workspace, and the caller is a space member of this workspace;
        2. The parent folder corresponding to ParentFolderPath must exist, and the caller must have write permission on it (pass `/` for the root directory);
        3. FileName must be unique under the same parent folder, including suffix comparison.
        4. The FileName suffix must be consistent with FileType (`.ipynb`↔`NOTEBOOK_FILE`, `.sql`↔`SQL_FILE`);
        5. To create with file content, pass it through Storage (large files are transferred via COS, and small files are placed in Storage.Content).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFolder(
            self,
            request: models.CreateFolderRequest,
            opts: Dict = None,
    ) -> models.CreateFolderResponse:
        """
        Create a folder
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchema(
            self,
            request: models.CreateSchemaRequest,
            opts: Dict = None,
    ) -> models.CreateSchemaResponse:
        """
        Create a schema
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        Create a workflow
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspace(
            self,
            request: models.CreateWorkspaceRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceResponse:
        """
        This API is used to create a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspaceRole(
            self,
            request: models.CreateWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspaceRoleResponse:
        """
        Creates a workspace role
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCatalog(
            self,
            request: models.DeleteCatalogRequest,
            opts: Dict = None,
    ) -> models.DeleteCatalogResponse:
        """
        Delete a catalog.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsoleGroups(
            self,
            request: models.DeleteConsoleGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteConsoleGroupsResponse:
        """
        Delete a console user group
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsoleGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsoleGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFile(
            self,
            request: models.DeleteFileRequest,
            opts: Dict = None,
    ) -> models.DeleteFileResponse:
        """
        Move the file to Recycle Bin (soft deletion) and clear its version history and execution result snapshots.

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
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFolder(
            self,
            request: models.DeleteFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteFolderResponse:
        """
        Delete folder
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSchema(
            self,
            request: models.DeleteSchemaRequest,
            opts: Dict = None,
    ) -> models.DeleteSchemaResponse:
        """
        Delete schema
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        Deletes a workflow
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkspace(
            self,
            request: models.DeleteWorkspaceRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkspaceResponse:
        """
        Delete a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkspaceRole(
            self,
            request: models.DeleteWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkspaceRoleResponse:
        """
        Delete a workspace role.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCatalog(
            self,
            request: models.GetCatalogRequest,
            opts: Dict = None,
    ) -> models.GetCatalogResponse:
        """
        Query catalog description
        """
        
        kwargs = {}
        kwargs["action"] = "GetCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFile(
            self,
            request: models.GetFileRequest,
            opts: Dict = None,
    ) -> models.GetFileResponse:
        """
        Get the file's metadata, optionally including file content, and read historical snapshots by version.

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
        """
        
        kwargs = {}
        kwargs["action"] = "GetFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFolder(
            self,
            request: models.GetFolderRequest,
            opts: Dict = None,
    ) -> models.GetFolderResponse:
        """
        Get folder details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflow(
            self,
            request: models.GetWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowResponse:
        """
        This API is used to query workflow details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflowRun(
            self,
            request: models.GetWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowRunResponse:
        """
        Queries workflow running details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflowTaskRun(
            self,
            request: models.GetWorkflowTaskRunRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowTaskRunResponse:
        """
        Query task execution details
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflowTaskRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowTaskRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkspace(
            self,
            request: models.GetWorkspaceRequest,
            opts: Dict = None,
    ) -> models.GetWorkspaceResponse:
        """
        Queries the details of a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillWorkflowRun(
            self,
            request: models.KillWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.KillWorkflowRunResponse:
        """
        Terminate the operation of a workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "KillWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCatalogs(
            self,
            request: models.ListCatalogsRequest,
            opts: Dict = None,
    ) -> models.ListCatalogsResponse:
        """
        Pagination fetch data catalog list
        """
        
        kwargs = {}
        kwargs["action"] = "ListCatalogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCatalogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleGroupUsers(
            self,
            request: models.ListConsoleGroupUsersRequest,
            opts: Dict = None,
    ) -> models.ListConsoleGroupUsersResponse:
        """
        Queries the console user group member list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleGroupUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleGroupUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleGroups(
            self,
            request: models.ListConsoleGroupsRequest,
            opts: Dict = None,
    ) -> models.ListConsoleGroupsResponse:
        """
        Queries the console user group list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleRoles(
            self,
            request: models.ListConsoleRolesRequest,
            opts: Dict = None,
    ) -> models.ListConsoleRolesResponse:
        """
        Queries the console role list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConsoleUsers(
            self,
            request: models.ListConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.ListConsoleUsersResponse:
        """
        Queries the console user list. This API is a console-level API and is only supported in the central region: use ap-guangzhou for the Chinese site and ap-singapore for the international site. Calls from other regions will return UnsupportedRegion.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFiles(
            self,
            request: models.ListFilesRequest,
            opts: Dict = None,
    ) -> models.ListFilesResponse:
        """
        Get the folder and file list
        """
        
        kwargs = {}
        kwargs["action"] = "ListFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSchemas(
            self,
            request: models.ListSchemasRequest,
            opts: Dict = None,
    ) -> models.ListSchemasResponse:
        """
        Get schema list
        """
        
        kwargs = {}
        kwargs["action"] = "ListSchemas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSchemasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowRuns(
            self,
            request: models.ListWorkflowRunsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowRunsResponse:
        """
        Workflow run list
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowTaskRuns(
            self,
            request: models.ListWorkflowTaskRunsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowTaskRunsResponse:
        """
        Query the historical operation list of workflow tasks
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowTaskRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowTaskRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflows(
            self,
            request: models.ListWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowsResponse:
        """
        This API is used to query the list of workflows.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaceGroups(
            self,
            request: models.ListWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.ListWorkspaceGroupsResponse:
        """
        This API is used to query the list of user groups in a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspaceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaceUsers(
            self,
            request: models.ListWorkspaceUsersRequest,
            opts: Dict = None,
    ) -> models.ListWorkspaceUsersResponse:
        """
        Queries the list of users in a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaceUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspaceUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkspaces(
            self,
            request: models.ListWorkspacesRequest,
            opts: Dict = None,
    ) -> models.ListWorkspacesResponse:
        """
        Queries the workspace list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveConsoleUsers(
            self,
            request: models.RemoveConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.RemoveConsoleUsersResponse:
        """
        <p>Batch remove console users (up to 10 at a time; pre-verification rejects the entire request if any fails; during the Execution Phase, a single failure does not interrupt subsequent deletion, and success or failure is determined by SuccessUins/FailItems)</p>
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWorkspaceGroups(
            self,
            request: models.RemoveWorkspaceGroupsRequest,
            opts: Dict = None,
    ) -> models.RemoveWorkspaceGroupsResponse:
        """
        Remove a user group from a workspace.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWorkspaceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWorkspaceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RerunWorkflowRun(
            self,
            request: models.RerunWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.RerunWorkflowRunResponse:
        """
        Rerun a workflow
        """
        
        kwargs = {}
        kwargs["action"] = "RerunWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RerunWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunWorkflow(
            self,
            request: models.RunWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunWorkflowResponse:
        """
        Runs the workflow
        """
        
        kwargs = {}
        kwargs["action"] = "RunWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCompute(
            self,
            request: models.StartComputeRequest,
            opts: Dict = None,
    ) -> models.StartComputeResponse:
        """
        Start up the computational resource.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCompute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartComputeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCompute(
            self,
            request: models.StopComputeRequest,
            opts: Dict = None,
    ) -> models.StopComputeResponse:
        """
        Terminate computational resources
        """
        
        kwargs = {}
        kwargs["action"] = "StopCompute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopComputeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindWorkflowBundle(
            self,
            request: models.UnbindWorkflowBundleRequest,
            opts: Dict = None,
    ) -> models.UnbindWorkflowBundleResponse:
        """
        Unbind workflow Bundle info
        Description: This interface is semantically equivalent to Detach in the standard verb list. The name Unbind is retained for compatibility with existing product forms.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindWorkflowBundle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindWorkflowBundleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConsoleGroup(
            self,
            request: models.UpdateConsoleGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateConsoleGroupResponse:
        """
        Modify a console user group
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConsoleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConsoleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConsoleUsers(
            self,
            request: models.UpdateConsoleUsersRequest,
            opts: Dict = None,
    ) -> models.UpdateConsoleUsersResponse:
        """
        Modify a console user role
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConsoleUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConsoleUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFile(
            self,
            request: models.UpdateFileRequest,
            opts: Dict = None,
    ) -> models.UpdateFileResponse:
        """
        Update file contents and running configuration (computational resource, default catalog/schema, parameters), and return the file metadata after the update.

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
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFolder(
            self,
            request: models.UpdateFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateFolderResponse:
        """
        Update folder (supports rename and move)
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflow(
            self,
            request: models.UpdateWorkflowRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowResponse:
        """
        Updating a Workflow
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspace(
            self,
            request: models.UpdateWorkspaceRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceResponse:
        """
        Modifies a workspace
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspaceRole(
            self,
            request: models.UpdateWorkspaceRoleRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceRoleResponse:
        """
        Updates a workspace role
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspaceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)