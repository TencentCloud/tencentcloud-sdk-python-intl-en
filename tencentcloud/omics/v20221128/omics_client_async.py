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
from tencentcloud.omics.v20221128 import models
from typing import Dict


class OmicsClient(AbstractClient):
    _apiVersion = '2022-11-28'
    _endpoint = 'omics.intl.tencentcloudapi.com'
    _service = 'omics'

    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        This API is used to create an environment for Tencent Healthcare Omics Platform.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVolume(
            self,
            request: models.CreateVolumeRequest,
            opts: Dict = None,
    ) -> models.CreateVolumeResponse:
        """
        This API is used to create a volume.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironment(
            self,
            request: models.DeleteEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentResponse:
        """
        This API is used to delete the environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVolume(
            self,
            request: models.DeleteVolumeRequest,
            opts: Dict = None,
    ) -> models.DeleteVolumeResponse:
        """
        This API is used to delete the volume.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVolumeData(
            self,
            request: models.DeleteVolumeDataRequest,
            opts: Dict = None,
    ) -> models.DeleteVolumeDataResponse:
        """
        This API is used to delete the volume data.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVolumeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVolumeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        This API is used to query the environment list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRunGroups(
            self,
            request: models.DescribeRunGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRunGroupsResponse:
        """
        This API is used to query the run group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRunGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuns(
            self,
            request: models.DescribeRunsRequest,
            opts: Dict = None,
    ) -> models.DescribeRunsResponse:
        """
        This API is used to query the run list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        This API is used to query the table.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesRows(
            self,
            request: models.DescribeTablesRowsRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesRowsResponse:
        """
        This API is used to query the table row data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesRows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesRowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVolumes(
            self,
            request: models.DescribeVolumesRequest,
            opts: Dict = None,
    ) -> models.DescribeVolumesResponse:
        """
        This API is used to query the volume list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVolumes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVolumesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunCalls(
            self,
            request: models.GetRunCallsRequest,
            opts: Dict = None,
    ) -> models.GetRunCallsResponse:
        """
        This API is used to query job details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunCalls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunCallsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunMetadataFile(
            self,
            request: models.GetRunMetadataFileRequest,
            opts: Dict = None,
    ) -> models.GetRunMetadataFileResponse:
        """
        This API is used to get the run details file.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunMetadataFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunMetadataFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRunStatus(
            self,
            request: models.GetRunStatusRequest,
            opts: Dict = None,
    ) -> models.GetRunStatusResponse:
        """
        This API is used to query run details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRunStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRunStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportTableFile(
            self,
            request: models.ImportTableFileRequest,
            opts: Dict = None,
    ) -> models.ImportTableFileResponse:
        """
        This API is used to import the table file.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportTableFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportTableFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVolume(
            self,
            request: models.ModifyVolumeRequest,
            opts: Dict = None,
    ) -> models.ModifyVolumeResponse:
        """
        This API is used to modify the volume.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVolume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVolumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRuns(
            self,
            request: models.RetryRunsRequest,
            opts: Dict = None,
    ) -> models.RetryRunsResponse:
        """
        This API is used to retry the run.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunApplication(
            self,
            request: models.RunApplicationRequest,
            opts: Dict = None,
    ) -> models.RunApplicationResponse:
        """
        This API is used to run the application.
        """
        
        kwargs = {}
        kwargs["action"] = "RunApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunWorkflow(
            self,
            request: models.RunWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunWorkflowResponse:
        """
        This API is used to run the workflow.
        """
        
        kwargs = {}
        kwargs["action"] = "RunWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateRunGroup(
            self,
            request: models.TerminateRunGroupRequest,
            opts: Dict = None,
    ) -> models.TerminateRunGroupResponse:
        """
        This API is used to terminate the run group.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateRunGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateRunGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)