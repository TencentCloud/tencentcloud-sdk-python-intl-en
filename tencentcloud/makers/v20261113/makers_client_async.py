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
from tencentcloud.makers.v20261113 import models
from typing import Dict


class MakersClient(AbstractClient):
    _apiVersion = '2026-11-13'
    _endpoint = 'makers.intl.tencentcloudapi.com'
    _service = 'makers'

    async def CreateDeployment(
            self,
            request: models.CreateDeploymentRequest,
            opts: Dict = None,
    ) -> models.CreateDeploymentResponse:
        """
        This API is used to create a deployment. When uploading an artifact, pass Upload for ViaMeta and Provider, and pass the path of the uploaded object for TempBucketPath.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        This API is used to create a project. When uploading an artifact, pass Upload for Provider and Custom for Channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateZoneCustomDomain(
            self,
            request: models.CreateZoneCustomDomainRequest,
            opts: Dict = None,
    ) -> models.CreateZoneCustomDomainResponse:
        """
        Bind a custom domain name to a specified environment of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateZoneCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateZoneCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        Delete a project. In-progress builds prevent deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectCustomDomains(
            self,
            request: models.DeleteProjectCustomDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectCustomDomainsResponse:
        """
        Unbind a custom domain name from a project by domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectCustomDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectCustomDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectEnvs(
            self,
            request: models.DeleteProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectEnvsResponse:
        """
        Delete environment variables by EnvVars. Match by Id or Key. Value is required but not used for matching. You can pass any value.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosTempToken(
            self,
            request: models.DescribeCosTempTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeCosTempTokenResponse:
        """
        Get the COS bucket, region, target path, and temporary key for uploading artifacts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosTempToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosTempTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeploymentLog(
            self,
            request: models.DescribeDeploymentLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentLogResponse:
        """
        Return the access address of the build log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeploymentLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployments(
            self,
            request: models.DescribeDeploymentsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentsResponse:
        """
        Query deployment records of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        Query environments in a project, including built-in Production, Preview, and custom environments.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectEnvs(
            self,
            request: models.DescribeProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectEnvsResponse:
        """
        Query project environment variables. If Env is not specified, return all application scopes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        This API is used to query projects under a site by page. Offset is the page number offset, and the backend skips Offset * Limit items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneCustomDomains(
            self,
            request: models.DescribeZoneCustomDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneCustomDomainsResponse:
        """
        Queries the custom and preset domain names of a project under a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneCustomDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneCustomDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        Modify the project name and build configuration. Fields not passed retain their original values.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectEnvs(
            self,
            request: models.ModifyProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectEnvsResponse:
        """
        Write environment variables based on the passed-in EnvVars.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneCustomDomainEnv(
            self,
            request: models.ModifyZoneCustomDomainEnvRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneCustomDomainEnvResponse:
        """
        Switch a bound custom domain name to another environment.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneCustomDomainEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneCustomDomainEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)