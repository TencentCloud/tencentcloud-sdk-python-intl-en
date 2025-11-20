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
from tencentcloud.mdp.v20200527 import models
from typing import Dict


class MdpClient(AbstractClient):
    _apiVersion = '2020-05-27'
    _endpoint = 'mdp.intl.tencentcloudapi.com'
    _service = 'mdp'

    async def BindLinearAssemblyCDNDomainWithChannel(
            self,
            request: models.BindLinearAssemblyCDNDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.BindLinearAssemblyCDNDomainWithChannelResponse:
        """
        Linear Assembly channel is bound to CDN playback domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "BindLinearAssemblyCDNDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindLinearAssemblyCDNDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindNewLVBDomainWithChannel(
            self,
            request: models.BindNewLVBDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.BindNewLVBDomainWithChannelResponse:
        """
        This API is used to bind an LVB domain name to a channel.
        """
        
        kwargs = {}
        kwargs["action"] = "BindNewLVBDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindNewLVBDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSSAICDNDomainWithChannel(
            self,
            request: models.BindSSAICDNDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.BindSSAICDNDomainWithChannelResponse:
        """
        This API is used to bind a CDN playback domain to a channel.
        """
        
        kwargs = {}
        kwargs["action"] = "BindSSAICDNDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSSAICDNDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageChannel(
            self,
            request: models.CreateStreamPackageChannelRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageChannelResponse:
        """
        This API is used to create a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageChannelEndpoint(
            self,
            request: models.CreateStreamPackageChannelEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageChannelEndpointResponse:
        """
        This API is used to create an endpoint on a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageChannelEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageChannelEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageHarvestJob(
            self,
            request: models.CreateStreamPackageHarvestJobRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageHarvestJobResponse:
        """
        Create HarvestJob.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageHarvestJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageHarvestJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageLinearAssemblyChannel(
            self,
            request: models.CreateStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageLinearAssemblyChannelResponse:
        """
        Create a linear assembly channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageLinearAssemblyProgram(
            self,
            request: models.CreateStreamPackageLinearAssemblyProgramRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageLinearAssemblyProgramResponse:
        """
        Create a linear assembly program.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageLinearAssemblyProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageLinearAssemblyProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageSSAIChannel(
            self,
            request: models.CreateStreamPackageSSAIChannelRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageSSAIChannelResponse:
        """
        CreateStreamPackageSSAIChannel
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageSSAIChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageSSAIChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageSource(
            self,
            request: models.CreateStreamPackageSourceRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageSourceResponse:
        """
        Create channel linear assembly Source.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageSourceLocation(
            self,
            request: models.CreateStreamPackageSourceLocationRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageSourceLocationResponse:
        """
        Create Linear Assembly SourceLocation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageSourceLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageSourceLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamPackageVodRemuxTask(
            self,
            request: models.CreateStreamPackageVodRemuxTaskRequest,
            opts: Dict = None,
    ) -> models.CreateStreamPackageVodRemuxTaskResponse:
        """
        Create VodRemuxTask
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamPackageVodRemuxTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamPackageVodRemuxTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageChannelEndpoints(
            self,
            request: models.DeleteStreamPackageChannelEndpointsRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageChannelEndpointsResponse:
        """
        This API is used to delete endpoints from a StreamPackage channel in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageChannelEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageChannelEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageChannels(
            self,
            request: models.DeleteStreamPackageChannelsRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageChannelsResponse:
        """
        This API is used to delete StreamPackage channels in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageHarvestJob(
            self,
            request: models.DeleteStreamPackageHarvestJobRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageHarvestJobResponse:
        """
        Delete HarvestJob.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageHarvestJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageHarvestJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageHarvestJobs(
            self,
            request: models.DeleteStreamPackageHarvestJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageHarvestJobsResponse:
        """
        Deleting HarvestJobs in Batch.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageHarvestJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageHarvestJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageLinearAssemblyChannel(
            self,
            request: models.DeleteStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageLinearAssemblyChannelResponse:
        """
        Delete channel linear assemblyChannel.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageLinearAssemblyChannels(
            self,
            request: models.DeleteStreamPackageLinearAssemblyChannelsRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageLinearAssemblyChannelsResponse:
        """
        Delete channels in batches and linearly assemble channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageLinearAssemblyChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageLinearAssemblyChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageLinearAssemblyProgram(
            self,
            request: models.DeleteStreamPackageLinearAssemblyProgramRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageLinearAssemblyProgramResponse:
        """
        Delete Channel Linear Assembly Program.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageLinearAssemblyProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageLinearAssemblyProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageLinearAssemblyPrograms(
            self,
            request: models.DeleteStreamPackageLinearAssemblyProgramsRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageLinearAssemblyProgramsResponse:
        """
        Batch deletion of channels linear assembly program.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageLinearAssemblyPrograms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageLinearAssemblyProgramsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageSSAIChannel(
            self,
            request: models.DeleteStreamPackageSSAIChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageSSAIChannelResponse:
        """
        DeleteStreamPackageSSAIChannel
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageSSAIChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageSSAIChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageSource(
            self,
            request: models.DeleteStreamPackageSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageSourceResponse:
        """
        Delete channel linear assembly Source.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageSourceLocation(
            self,
            request: models.DeleteStreamPackageSourceLocationRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageSourceLocationResponse:
        """
        Batch delete media packaging SourceLocation.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageSourceLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageSourceLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageVodRemuxTask(
            self,
            request: models.DeleteStreamPackageVodRemuxTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageVodRemuxTaskResponse:
        """
        Delete Vod remux task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageVodRemuxTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageVodRemuxTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamPackageVodRemuxTasks(
            self,
            request: models.DeleteStreamPackageVodRemuxTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamPackageVodRemuxTasksResponse:
        """
        Delete VOD remux tasks in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamPackageVodRemuxTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamPackageVodRemuxTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLinearAssemblyCDNDomainWithChannel(
            self,
            request: models.DescribeLinearAssemblyCDNDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeLinearAssemblyCDNDomainWithChannelResponse:
        """
        Query the CDN domain name associated with the LinearAssembly channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLinearAssemblyCDNDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLinearAssemblyCDNDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLinearAssemblyCDNDomainWithChannels(
            self,
            request: models.DescribeLinearAssemblyCDNDomainWithChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeLinearAssemblyCDNDomainWithChannelsResponse:
        """
        Query the CDN domain names associated with all LinearAssembly channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLinearAssemblyCDNDomainWithChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLinearAssemblyCDNDomainWithChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageChannel(
            self,
            request: models.DescribeStreamPackageChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageChannelResponse:
        """
        This API is used to query the information of a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageChannels(
            self,
            request: models.DescribeStreamPackageChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageChannelsResponse:
        """
        This API is used to query the information of multiple StreamPackage channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageHarvestJob(
            self,
            request: models.DescribeStreamPackageHarvestJobRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageHarvestJobResponse:
        """
        Query HarvestJob.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageHarvestJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageHarvestJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageHarvestJobs(
            self,
            request: models.DescribeStreamPackageHarvestJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageHarvestJobsResponse:
        """
        Batch query HarvestJob.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageHarvestJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageHarvestJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyChannel(
            self,
            request: models.DescribeStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyChannelResponse:
        """
        Query channel linear assembly Channel information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyChannelAlerts(
            self,
            request: models.DescribeStreamPackageLinearAssemblyChannelAlertsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyChannelAlertsResponse:
        """
        Query linear assembly channel alarm information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyChannelAlerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyChannelAlertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyChannels(
            self,
            request: models.DescribeStreamPackageLinearAssemblyChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyChannelsResponse:
        """
        Query channel linear assembly Channel information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyProgram(
            self,
            request: models.DescribeStreamPackageLinearAssemblyProgramRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyProgramResponse:
        """
        Query channel linear assembly program information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyProgramSchedules(
            self,
            request: models.DescribeStreamPackageLinearAssemblyProgramSchedulesRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyProgramSchedulesResponse:
        """
        Query channel linear assembly Programl assembly scheduling information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyProgramSchedules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyProgramSchedulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageLinearAssemblyPrograms(
            self,
            request: models.DescribeStreamPackageLinearAssemblyProgramsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageLinearAssemblyProgramsResponse:
        """
        Query channel linear assembly Programl information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageLinearAssemblyPrograms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageLinearAssemblyProgramsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSSAIChannel(
            self,
            request: models.DescribeStreamPackageSSAIChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSSAIChannelResponse:
        """
        DescribeStreamPackageSSAIChannel
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSSAIChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSSAIChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSSAIChannels(
            self,
            request: models.DescribeStreamPackageSSAIChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSSAIChannelsResponse:
        """
        DescribeStreamPackageSSAIChannels
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSSAIChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSSAIChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSSAIUsage(
            self,
            request: models.DescribeStreamPackageSSAIUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSSAIUsageResponse:
        """
        This API is used to query SSAI ad replacement usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSSAIUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSSAIUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSource(
            self,
            request: models.DescribeStreamPackageSourceRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourceResponse:
        """
        Query channel linear assembly Source information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSourceAlerts(
            self,
            request: models.DescribeStreamPackageSourceAlertsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourceAlertsResponse:
        """
        Query channel linear assembly Source alarm information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSourceAlerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourceAlertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSourceLocation(
            self,
            request: models.DescribeStreamPackageSourceLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourceLocationResponse:
        """
        Query channel linear assembly sourceLocation information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSourceLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourceLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSourceLocationAlerts(
            self,
            request: models.DescribeStreamPackageSourceLocationAlertsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourceLocationAlertsResponse:
        """
        Query channel linear assembly Location alarm information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSourceLocationAlerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourceLocationAlertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSourceLocations(
            self,
            request: models.DescribeStreamPackageSourceLocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourceLocationsResponse:
        """
        Query channel linear assembly SourceLocation information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSourceLocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourceLocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageSources(
            self,
            request: models.DescribeStreamPackageSourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageSourcesResponse:
        """
        Query channel linear assembly Source information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageVodRemuxTask(
            self,
            request: models.DescribeStreamPackageVodRemuxTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageVodRemuxTaskResponse:
        """
        Query VOD remux task information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageVodRemuxTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageVodRemuxTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPackageVodRemuxTasks(
            self,
            request: models.DescribeStreamPackageVodRemuxTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPackageVodRemuxTasksResponse:
        """
        Query VOD remux tasks informations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPackageVodRemuxTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPackageVodRemuxTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageChannel(
            self,
            request: models.ModifyStreamPackageChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageChannelResponse:
        """
        This API is used to modify a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageChannelEndpoint(
            self,
            request: models.ModifyStreamPackageChannelEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageChannelEndpointResponse:
        """
        This API is used to modify an endpoint of a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageChannelEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageChannelEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageChannelInputAuthInfo(
            self,
            request: models.ModifyStreamPackageChannelInputAuthInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageChannelInputAuthInfoResponse:
        """
        This API is used to modify the input authentication information of a StreamPackage channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageChannelInputAuthInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageChannelInputAuthInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageLinearAssemblyChannel(
            self,
            request: models.ModifyStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageLinearAssemblyChannelResponse:
        """
        Modify channel linear assembly Channel configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageLinearAssemblyProgram(
            self,
            request: models.ModifyStreamPackageLinearAssemblyProgramRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageLinearAssemblyProgramResponse:
        """
        Modify channel linear assembly Program configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageLinearAssemblyProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageLinearAssemblyProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageSSAIChannel(
            self,
            request: models.ModifyStreamPackageSSAIChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageSSAIChannelResponse:
        """
        ModifyStreamPackageSSAIChannel
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageSSAIChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageSSAIChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageSource(
            self,
            request: models.ModifyStreamPackageSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageSourceResponse:
        """
        Modify channel linear assembly Source configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamPackageSourceLocation(
            self,
            request: models.ModifyStreamPackageSourceLocationRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamPackageSourceLocationResponse:
        """
        Modify channel linear assembly SourceLocation configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamPackageSourceLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamPackageSourceLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamPackageLinearAssemblyChannel(
            self,
            request: models.StartStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.StartStreamPackageLinearAssemblyChannelResponse:
        """
        Start Linear Assembly Channel.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamPackageVodRemuxTask(
            self,
            request: models.StartStreamPackageVodRemuxTaskRequest,
            opts: Dict = None,
    ) -> models.StartStreamPackageVodRemuxTaskResponse:
        """
        Start VOD remux task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamPackageVodRemuxTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamPackageVodRemuxTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopStreamPackageLinearAssemblyChannel(
            self,
            request: models.StopStreamPackageLinearAssemblyChannelRequest,
            opts: Dict = None,
    ) -> models.StopStreamPackageLinearAssemblyChannelResponse:
        """
        Stop linear assembly channel.
        """
        
        kwargs = {}
        kwargs["action"] = "StopStreamPackageLinearAssemblyChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopStreamPackageLinearAssemblyChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCdnDomainWithChannel(
            self,
            request: models.UnbindCdnDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.UnbindCdnDomainWithChannelResponse:
        """
        This API is used to unbind a CDN playback domain name from a channel.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCdnDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCdnDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindLinearAssemblyCDNDomainWithChannel(
            self,
            request: models.UnbindLinearAssemblyCDNDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.UnbindLinearAssemblyCDNDomainWithChannelResponse:
        """
        Unbind LinearAssembly channel with CDN domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindLinearAssemblyCDNDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindLinearAssemblyCDNDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindSSAICDNDomainWithChannel(
            self,
            request: models.UnbindSSAICDNDomainWithChannelRequest,
            opts: Dict = None,
    ) -> models.UnbindSSAICDNDomainWithChannelResponse:
        """
        This API is used to cancel the correlation between a channel and a CDN playback domain.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindSSAICDNDomainWithChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindSSAICDNDomainWithChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)