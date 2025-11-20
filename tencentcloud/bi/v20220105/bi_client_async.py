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
from tencentcloud.bi.v20220105 import models
from typing import Dict


class BiClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'bi.intl.tencentcloudapi.com'
    _service = 'bi'

    async def ApplyEmbedInterval(
            self,
            request: models.ApplyEmbedIntervalRequest,
            opts: Dict = None,
    ) -> models.ApplyEmbedIntervalResponse:
        """
        This API is used to extend the available time of a token with strong authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyEmbedInterval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyEmbedIntervalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatasource(
            self,
            request: models.CreateDatasourceRequest,
            opts: Dict = None,
    ) -> models.CreateDatasourceResponse:
        """
        This API is used to create a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatasourceCloud(
            self,
            request: models.CreateDatasourceCloudRequest,
            opts: Dict = None,
    ) -> models.CreateDatasourceCloudResponse:
        """
        This API is used to create a cloud database.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatasourceCloud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatasourceCloudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmbedToken(
            self,
            request: models.CreateEmbedTokenRequest,
            opts: Dict = None,
    ) -> models.CreateEmbedTokenResponse:
        """
        This API is used to create an embedded report with strong authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmbedToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmbedTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        This API is used to create a project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserRole(
            self,
            request: models.CreateUserRoleRequest,
            opts: Dict = None,
    ) -> models.CreateUserRoleResponse:
        """
        This API is used to create a user role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserRoleProject(
            self,
            request: models.CreateUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.CreateUserRoleProjectResponse:
        """
        This API is used to create a user role in the project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatasource(
            self,
            request: models.DeleteDatasourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDatasourceResponse:
        """
        This API is used to delete a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        This API is used to delete a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserRole(
            self,
            request: models.DeleteUserRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteUserRoleResponse:
        """
        This API is used to remove a user role, which will result in user deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserRoleProject(
            self,
            request: models.DeleteUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteUserRoleProjectResponse:
        """
        This API is used to delete a user role in the project.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasourceList(
            self,
            request: models.DescribeDatasourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasourceListResponse:
        """
        This API is used to query a data source list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePageWidgetList(
            self,
            request: models.DescribePageWidgetListRequest,
            opts: Dict = None,
    ) -> models.DescribePageWidgetListResponse:
        """
        This API is used to query component information on the page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePageWidgetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePageWidgetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectInfo(
            self,
            request: models.DescribeProjectInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectInfoResponse:
        """
        This API is used to obtain project details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectList(
            self,
            request: models.DescribeProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectListResponse:
        """
        This API is used to obtain project information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserProjectList(
            self,
            request: models.DescribeUserProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserProjectListResponse:
        """
        This API is used to obtain the user interface in the project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoleList(
            self,
            request: models.DescribeUserRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRoleListResponse:
        """
        This API is used to obtain the user role list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoleProjectList(
            self,
            request: models.DescribeUserRoleProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRoleProjectListResponse:
        """
        This API is used to obtain the user role list in the project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoleProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRoleProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportScreenPage(
            self,
            request: models.ExportScreenPageRequest,
            opts: Dict = None,
    ) -> models.ExportScreenPageResponse:
        """
        This API is used to export a screenshot.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportScreenPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportScreenPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatasource(
            self,
            request: models.ModifyDatasourceRequest,
            opts: Dict = None,
    ) -> models.ModifyDatasourceResponse:
        """
        This API is used to update a data source.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatasourceCloud(
            self,
            request: models.ModifyDatasourceCloudRequest,
            opts: Dict = None,
    ) -> models.ModifyDatasourceCloudResponse:
        """
        This API is used to update a cloud database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatasourceCloud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatasourceCloudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        This API is used to modify project information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserRole(
            self,
            request: models.ModifyUserRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyUserRoleResponse:
        """
        This API is used to modify user role info.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserRoleProject(
            self,
            request: models.ModifyUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyUserRoleProjectResponse:
        """
        This API is used to modify the user role info in the project.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)