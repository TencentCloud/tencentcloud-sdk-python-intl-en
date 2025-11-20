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
from tencentcloud.car.v20220110 import models
from typing import Dict


class CarClient(AbstractClient):
    _apiVersion = '2022-01-10'
    _endpoint = 'car.intl.tencentcloudapi.com'
    _service = 'car'

    async def ApplyConcurrent(
            self,
            request: models.ApplyConcurrentRequest,
            opts: Dict = None,
    ) -> models.ApplyConcurrentResponse:
        """
        This API is used to request concurrency quota. The timeout period of the API is 20 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyConcurrent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyConcurrentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindConcurrentPackagesToProject(
            self,
            request: models.BindConcurrentPackagesToProjectRequest,
            opts: Dict = None,
    ) -> models.BindConcurrentPackagesToProjectResponse:
        """
        This API is used to bind a concurrency pack to a project.
        """
        
        kwargs = {}
        kwargs["action"] = "BindConcurrentPackagesToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindConcurrentPackagesToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        This API is used to create an application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProject(
            self,
            request: models.CreateApplicationProjectRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProjectResponse:
        """
        This API is used to create a cloud application project.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationSnapshot(
            self,
            request: models.CreateApplicationSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationSnapshotResponse:
        """
        This API is used to create a cloud application version snapshot.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationVersion(
            self,
            request: models.CreateApplicationVersionRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationVersionResponse:
        """
        This API is used to create a cloud application version.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSession(
            self,
            request: models.CreateSessionRequest,
            opts: Dict = None,
    ) -> models.CreateSessionResponse:
        """
        This API is used to create a session. The timeout period of the API is 5 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplication(
            self,
            request: models.DeleteApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationResponse:
        """
        This API is used to delete a cloud application.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProjects(
            self,
            request: models.DeleteApplicationProjectsRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProjectsResponse:
        """
        This API is used to delete cloud application projects in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationVersion(
            self,
            request: models.DeleteApplicationVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationVersionResponse:
        """
        This API is used to delete a cloud application version.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationFileInfo(
            self,
            request: models.DescribeApplicationFileInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationFileInfoResponse:
        """
        This API is used to query application file information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationFileInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationFileInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationList(
            self,
            request: models.DescribeApplicationListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationListResponse:
        """
        This API is used to query the cloud application list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationPathList(
            self,
            request: models.DescribeApplicationPathListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationPathListResponse:
        """
        This API is used to query the cloud application startup path list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationPathList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationPathListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProjectAdvancedConfig(
            self,
            request: models.DescribeApplicationProjectAdvancedConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProjectAdvancedConfigResponse:
        """
        This API is used to obtain the advanced configuration information of a cloud application project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProjectAdvancedConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProjectAdvancedConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProjects(
            self,
            request: models.DescribeApplicationProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProjectsResponse:
        """
        This API is used to obtain the cloud application project list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationStatus(
            self,
            request: models.DescribeApplicationStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationStatusResponse:
        """
        This API is used to query the running status of a cloud application and update status information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationVersion(
            self,
            request: models.DescribeApplicationVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationVersionResponse:
        """
        This API is used to query the version information of a cloud application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrentCount(
            self,
            request: models.DescribeConcurrentCountRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrentCountResponse:
        """
        This API is used to obtain the concurrency count.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrentCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrentCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrentPackages(
            self,
            request: models.DescribeConcurrentPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrentPackagesResponse:
        """
        This API is used to obtain the cloud application concurrency pack list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrentPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrentPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrentSummary(
            self,
            request: models.DescribeConcurrentSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrentSummaryResponse:
        """
        This API is used to query the concurrency overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrentSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrentSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosCredential(
            self,
            request: models.DescribeCosCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeCosCredentialResponse:
        """
        This API is used to query COS key information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroySession(
            self,
            request: models.DestroySessionRequest,
            opts: Dict = None,
    ) -> models.DestroySessionResponse:
        """
        This API is used to terminate a session. If cloud-based streaming has been enabled for this session, the cloud-based streaming will end upon session termination.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroySession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroySessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationBaseInfo(
            self,
            request: models.ModifyApplicationBaseInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationBaseInfoResponse:
        """
        This API is used to modify basic information of a cloud application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProject(
            self,
            request: models.ModifyApplicationProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProjectResponse:
        """
        This API is used to modify a cloud application project.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationVersion(
            self,
            request: models.ModifyApplicationVersionRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationVersionResponse:
        """
        This API is used to modify the version information of a cloud application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConcurrentPackage(
            self,
            request: models.ModifyConcurrentPackageRequest,
            opts: Dict = None,
    ) -> models.ModifyConcurrentPackageResponse:
        """
        This API is used to modify a cloud application concurrency pack.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConcurrentPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConcurrentPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMobileApplicationInfo(
            self,
            request: models.ModifyMobileApplicationInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyMobileApplicationInfoResponse:
        """
        This API is used to modify the mobile application data.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMobileApplicationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMobileApplicationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConcurrentPackages(
            self,
            request: models.ResetConcurrentPackagesRequest,
            opts: Dict = None,
    ) -> models.ResetConcurrentPackagesResponse:
        """
        This API is used to reset a concurrency pack and disconnect all user connections.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConcurrentPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConcurrentPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetApplicationVersionOnline(
            self,
            request: models.SetApplicationVersionOnlineRequest,
            opts: Dict = None,
    ) -> models.SetApplicationVersionOnlineResponse:
        """
        This API is used to launch an application version.
        """
        
        kwargs = {}
        kwargs["action"] = "SetApplicationVersionOnline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetApplicationVersionOnlineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStream(
            self,
            request: models.StartPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamResponse:
        """
        This API is used to start pushing your cloud application's video streams in real time to CSS. The codec for the streaming is automatically selected based on the client's (SDK) capabilities, with a default order of H.265, H.264, VP8, and VP9.
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStreamWithURL(
            self,
            request: models.StartPublishStreamWithURLRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamWithURLResponse:
        """
        This API is used to start pushing your cloud application's video streams to a specified URL. The codec for the streaming is automatically selected based on the client's (SDK) capabilities, with a default order of H.265, H.264, VP8, and VP9. This streaming method will be billed separately. For details about the billing method, see [Charging for Streaming to Specified URL](https://intl.cloud.tencent.com/document/product/1547/72168?from_cn_redirect=1#98ac188a-d122-4caf-88be-05268ecefdf6).
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStreamWithURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamWithURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPublishStream(
            self,
            request: models.StopPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StopPublishStreamResponse:
        """
        This API is used to stop pushing streams.
        """
        
        kwargs = {}
        kwargs["action"] = "StopPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindConcurrentPackagesFromProject(
            self,
            request: models.UnbindConcurrentPackagesFromProjectRequest,
            opts: Dict = None,
    ) -> models.UnbindConcurrentPackagesFromProjectResponse:
        """
        This API is used to unbind a concurrency pack from a project.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindConcurrentPackagesFromProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindConcurrentPackagesFromProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)