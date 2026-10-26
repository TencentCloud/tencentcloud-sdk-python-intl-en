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
from tencentcloud.iss.v20230517 import models
from typing import Dict


class IssClient(AbstractClient):
    _apiVersion = '2023-05-17'
    _endpoint = 'iss.intl.tencentcloudapi.com'
    _service = 'iss'

    async def AddOrganization(
            self,
            request: models.AddOrganizationRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationResponse:
        """
        Used to add an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordBackupPlan(
            self,
            request: models.AddRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.AddRecordBackupPlanResponse:
        """
        Used to add a recording cloud migration plan (currently applicable only to devices/video channels connected via the GB28181 protocol and gateway).
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordBackupTemplate(
            self,
            request: models.AddRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.AddRecordBackupTemplateResponse:
        """
        This API is used to create a video recording cloud template.
        > The feature essentially pulls local device recording data to the cloud (i.e., recordings stored in the IPC camera memory card or NVR hard disk). When operating, first set the recording time period (i.e., the local device recording you want to upload to the cloud), then set the Cloud Upload Time Period and upload speed. The platform will pull the previous day's Time Period Data from the device at the specified speed during the Cloud Upload Time Period.

        > Set the Cloud Upload Time Period to at least meet (Cloud Upload Time Period = previous day's recording time period / cloud upload speed multiplication). It is advisable to set about 10% more time for the Cloud Upload Time Period to avoid incomplete data retrieval due to network fluctuations.
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordPlan(
            self,
            request: models.AddRecordPlanRequest,
            opts: Dict = None,
    ) -> models.AddRecordPlanResponse:
        """
        This API is used to create a real-time cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordRetrieveTask(
            self,
            request: models.AddRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.AddRecordRetrieveTaskResponse:
        """
        This API is used to create a retrieval task.
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddRecordTemplate(
            self,
            request: models.AddRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.AddRecordTemplateResponse:
        """
        Used to add a real-time cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "AddRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddStreamAuth(
            self,
            request: models.AddStreamAuthRequest,
            opts: Dict = None,
    ) -> models.AddStreamAuthResponse:
        """
        Used to set push/pull stream authentication configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "AddStreamAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddStreamAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserDevice(
            self,
            request: models.AddUserDeviceRequest,
            opts: Dict = None,
    ) -> models.AddUserDeviceResponse:
        """
        This API is used to add a single device. After the device is added, configure it based on the returned results, then wait for device registration or stream pushing.
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchAddVideoSnapshotConfigChannel(
            self,
            request: models.BatchAddVideoSnapshotConfigChannelRequest,
            opts: Dict = None,
    ) -> models.BatchAddVideoSnapshotConfigChannelResponse:
        """
        Add channels for screenshot configuration in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchAddVideoSnapshotConfigChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchAddVideoSnapshotConfigChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchAssignVLPlanChannels(
            self,
            request: models.BatchAssignVLPlanChannelsRequest,
            opts: Dict = None,
    ) -> models.BatchAssignVLPlanChannelsResponse:
        """
        Batch associate visual understanding plan channels
        """
        
        kwargs = {}
        kwargs["action"] = "BatchAssignVLPlanChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchAssignVLPlanChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteVideoDownloadTask(
            self,
            request: models.BatchDeleteVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteVideoDownloadTaskResponse:
        """
        This API is used to delete failed local recording download tasks in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchGetVLPlanSourceFileURL(
            self,
            request: models.BatchGetVLPlanSourceFileURLRequest,
            opts: Dict = None,
    ) -> models.BatchGetVLPlanSourceFileURLResponse:
        """
        This API is used to batch obtain source material URLs for visual understanding plans.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchGetVLPlanSourceFileURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchGetVLPlanSourceFileURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchGetVideoSnapshotImageUrl(
            self,
            request: models.BatchGetVideoSnapshotImageUrlRequest,
            opts: Dict = None,
    ) -> models.BatchGetVideoSnapshotImageUrlResponse:
        """
        Bulk gets screenshot image URLs
        """
        
        kwargs = {}
        kwargs["action"] = "BatchGetVideoSnapshotImageUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchGetVideoSnapshotImageUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchOperateDevice(
            self,
            request: models.BatchOperateDeviceRequest,
            opts: Dict = None,
    ) -> models.BatchOperateDeviceResponse:
        """
        Used for batch operations (enable, disable, delete) on devices.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchOperateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchOperateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallISAPI(
            self,
            request: models.CallISAPIRequest,
            opts: Dict = None,
    ) -> models.CallISAPIResponse:
        """
        This API can be based on the Hikvision ISUP 5.0 protocol to pass through ISAPI request data. Before calling the API, ensure the device has successfully registered to this platform using the ISUP protocol.
        """
        
        kwargs = {}
        kwargs["action"] = "CallISAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallISAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevicePTZ(
            self,
            request: models.ControlDevicePTZRequest,
            opts: Dict = None,
    ) -> models.ControlDevicePTZResponse:
        """
        Used for device channel panning control, including turn, zoom scale, zoom, and aperture.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevicePTZ"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDevicePTZResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevicePreset(
            self,
            request: models.ControlDevicePresetRequest,
            opts: Dict = None,
    ) -> models.ControlDevicePresetResponse:
        """
        Used to operate device preset positions, including settings, deletion, and calls.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevicePreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDevicePresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDeviceSnapshot(
            self,
            request: models.ControlDeviceSnapshotRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceSnapshotResponse:
        """
        Control device capture (single). Currently only support national standard devices.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDeviceSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDeviceStream(
            self,
            request: models.ControlDeviceStreamRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceStreamResponse:
        """
        This API is used to obtain the real-time streaming address of a device.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDeviceStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlRecordTimeline(
            self,
            request: models.ControlRecordTimelineRequest,
            opts: Dict = None,
    ) -> models.ControlRecordTimelineResponse:
        """
        This API is used to query the local recording timeline info of a device, which is stored locally on the NVR/IPC.
        """
        
        kwargs = {}
        kwargs["action"] = "ControlRecordTimeline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlRecordTimelineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVLPlan(
            self,
            request: models.CreateVLPlanRequest,
            opts: Dict = None,
    ) -> models.CreateVLPlanResponse:
        """
        Creates a vision understanding plan
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVLPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVLPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVLTemplate(
            self,
            request: models.CreateVLTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateVLTemplateResponse:
        """
        Create a visual understanding template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVLTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVLTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoDownloadTask(
            self,
            request: models.CreateVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoDownloadTaskResponse:
        """
        This API is used to create a local recording download task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoSnapshotConfig(
            self,
            request: models.CreateVideoSnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.CreateVideoSnapshotConfigResponse:
        """
        This API is used to create a screenshot configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoSnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoSnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoSnapshotTemplate(
            self,
            request: models.CreateVideoSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateVideoSnapshotTemplateResponse:
        """
        Create a screenshot template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        This API is used to delete domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        This API is used to delete an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordBackupPlan(
            self,
            request: models.DeleteRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordBackupPlanResponse:
        """
        Used to delete a video recording cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordBackupTemplate(
            self,
            request: models.DeleteRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordBackupTemplateResponse:
        """
        This API is used to delete a video recording cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordPlan(
            self,
            request: models.DeleteRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordPlanResponse:
        """
        This API is used to delete a real-time cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordRetrieveTask(
            self,
            request: models.DeleteRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordRetrieveTaskResponse:
        """
        This API is used to delete a retrieval task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordTemplate(
            self,
            request: models.DeleteRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordTemplateResponse:
        """
        Used to delete a real-time cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        Used to delete completed tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserDevice(
            self,
            request: models.DeleteUserDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteUserDeviceResponse:
        """
        This API is used to delete added devices.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVLPlan(
            self,
            request: models.DeleteVLPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteVLPlanResponse:
        """
        Delete a vision understanding plan
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVLPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVLPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVLTemplate(
            self,
            request: models.DeleteVLTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteVLTemplateResponse:
        """
        Delete a visual understanding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVLTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVLTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVideoSnapshotConfig(
            self,
            request: models.DeleteVideoSnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteVideoSnapshotConfigResponse:
        """
        Deletes screenshot configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVideoSnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVideoSnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVideoSnapshotTemplate(
            self,
            request: models.DeleteVideoSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteVideoSnapshotTemplateResponse:
        """
        This API is used to delete a screenshot template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVideoSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVideoSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCNAME(
            self,
            request: models.DescribeCNAMERequest,
            opts: Dict = None,
    ) -> models.DescribeCNAMEResponse:
        """
        This API is used to get the CNAME value based on the service node.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceChannel(
            self,
            request: models.DescribeDeviceChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceChannelResponse:
        """
        This API is used to query the channels of a device.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePreset(
            self,
            request: models.DescribeDevicePresetRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePresetResponse:
        """
        This API is used to query preset position information of device channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomain(
            self,
            request: models.DescribeDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainResponse:
        """
        This API is used to query the list of added domains.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainRegion(
            self,
            request: models.DescribeDomainRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainRegionResponse:
        """
        This API is used to query the service nodes that can be bound when a user adds a domain name. The result is all service nodes supported by the platform. Each service node can only be bound to one domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGBDeviceAddr(
            self,
            request: models.DescribeGBDeviceAddrRequest,
            opts: Dict = None,
    ) -> models.DescribeGBDeviceAddrResponse:
        """
        This API is used to obtain the public network address of a national standard device.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGBDeviceAddr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGBDeviceAddrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganization(
            self,
            request: models.DescribeOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationResponse:
        """
        Used for querying organizations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordBackupPlan(
            self,
            request: models.DescribeRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordBackupPlanResponse:
        """
        This API is used to query recording cloud migration plan details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordBackupTemplate(
            self,
            request: models.DescribeRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordBackupTemplateResponse:
        """
        This API is used to query video recording cloud template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordFile(
            self,
            request: models.DescribeRecordFileRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordFileResponse:
        """
        This API is used to query the device cloud recording timeline information, which is the cloud storage video recording after setting a recording schedule for video upload to cloud.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordPlan(
            self,
            request: models.DescribeRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordPlanResponse:
        """
        This API is used to query real-time cloud migration plan details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordPlaybackUrl(
            self,
            request: models.DescribeRecordPlaybackUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordPlaybackUrlResponse:
        """
        This API is used to obtain the cloud recording playback url address.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordPlaybackUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordPlaybackUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordRetrieveTask(
            self,
            request: models.DescribeRecordRetrieveTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordRetrieveTaskResponse:
        """
        Used to query the details of a cloud recording retrieval task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordRetrieveTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordRetrieveTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordTemplate(
            self,
            request: models.DescribeRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTemplateResponse:
        """
        This API is used to query real-time cloud migration template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamAuth(
            self,
            request: models.DescribeStreamAuthRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamAuthResponse:
        """
        Used to query push/pull stream authentication configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        This API is used to query task details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDevice(
            self,
            request: models.DescribeUserDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDeviceResponse:
        """
        This API is used to query detailed information of a device.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDeviceList(
            self,
            request: models.DescribeUserDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDeviceListResponse:
        """
        This API is used to query device details in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVLPlan(
            self,
            request: models.DescribeVLPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeVLPlanResponse:
        """
        Query the plan details of visual understanding.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVLPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVLPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVLPlanResult(
            self,
            request: models.DescribeVLPlanResultRequest,
            opts: Dict = None,
    ) -> models.DescribeVLPlanResultResponse:
        """
        Query the result details of a vision understanding plan
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVLPlanResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVLPlanResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVLTemplate(
            self,
            request: models.DescribeVLTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeVLTemplateResponse:
        """
        Query the details of a visual understanding template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVLTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVLTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoBitRate(
            self,
            request: models.DescribeVideoBitRateRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoBitRateResponse:
        """
        This API is used to obtain the bitrate info of a video channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoBitRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoBitRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoDownloadUrl(
            self,
            request: models.DescribeVideoDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoDownloadUrlResponse:
        """
        This API is used to obtain the download url of cloud recordings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoSnapshotConfig(
            self,
            request: models.DescribeVideoSnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoSnapshotConfigResponse:
        """
        Queries screenshot configuration details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoSnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoSnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoSnapshotTemplate(
            self,
            request: models.DescribeVideoSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoSnapshotTemplateResponse:
        """
        Get screenshot template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDeviceSnapshots(
            self,
            request: models.ListDeviceSnapshotsRequest,
            opts: Dict = None,
    ) -> models.ListDeviceSnapshotsResponse:
        """
        Get device capture result list
        """
        
        kwargs = {}
        kwargs["action"] = "ListDeviceSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDeviceSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDevices(
            self,
            request: models.ListDevicesRequest,
            opts: Dict = None,
    ) -> models.ListDevicesResponse:
        """
        This API is used to obtain the device list under the corresponding organization.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationChannels(
            self,
            request: models.ListOrganizationChannelsRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationChannelsResponse:
        """
        This API is used to query the channel list under the organizational unit directory.
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupPlanDevices(
            self,
            request: models.ListRecordBackupPlanDevicesRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupPlanDevicesResponse:
        """
        This API is used to query the device channel list under a recording cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupPlanDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupPlanDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupPlans(
            self,
            request: models.ListRecordBackupPlansRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupPlansResponse:
        """
        This API is used to query the recording cloud migration plan list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordBackupTemplates(
            self,
            request: models.ListRecordBackupTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListRecordBackupTemplatesResponse:
        """
        This API is used to query the video recording cloud template list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordBackupTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordBackupTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordPlanDevices(
            self,
            request: models.ListRecordPlanDevicesRequest,
            opts: Dict = None,
    ) -> models.ListRecordPlanDevicesResponse:
        """
        This API is used to query the device channel list under a real-time cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordPlanDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordPlanDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordPlans(
            self,
            request: models.ListRecordPlansRequest,
            opts: Dict = None,
    ) -> models.ListRecordPlansResponse:
        """
        This API is used to query the real-time cloud migration plan list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordRetrieveTasks(
            self,
            request: models.ListRecordRetrieveTasksRequest,
            opts: Dict = None,
    ) -> models.ListRecordRetrieveTasksResponse:
        """
        This API is used to query the retrieval task list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordRetrieveTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordRetrieveTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRecordTemplates(
            self,
            request: models.ListRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListRecordTemplatesResponse:
        """
        This API is used to query the real-time cloud migration template list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSubTasks(
            self,
            request: models.ListSubTasksRequest,
            opts: Dict = None,
    ) -> models.ListSubTasksResponse:
        """
        This API is used to query the subtask list of a query task.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSubTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSubTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        This API is used to query the batch task and simple task list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVLPlans(
            self,
            request: models.ListVLPlansRequest,
            opts: Dict = None,
    ) -> models.ListVLPlansResponse:
        """
        Get the visual understanding plan list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListVLPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVLPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVLTemplates(
            self,
            request: models.ListVLTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListVLTemplatesResponse:
        """
        Get a list of visual understanding templates.
        """
        
        kwargs = {}
        kwargs["action"] = "ListVLTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVLTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVideoDownloadTask(
            self,
            request: models.ListVideoDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.ListVideoDownloadTaskResponse:
        """
        This API is used to query the recording download task list in this store.
        """
        
        kwargs = {}
        kwargs["action"] = "ListVideoDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVideoDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVideoSnapshotTemplate(
            self,
            request: models.ListVideoSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.ListVideoSnapshotTemplateResponse:
        """
        This API is used to search the screenshot template details list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListVideoSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVideoSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVLPlan(
            self,
            request: models.ModifyVLPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyVLPlanResponse:
        """
        Modify a vision understanding plan
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVLPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVLPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVideoSnapshotConfig(
            self,
            request: models.ModifyVideoSnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVideoSnapshotConfigResponse:
        """
        Update screenshot configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVideoSnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVideoSnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PlayRecord(
            self,
            request: models.PlayRecordRequest,
            opts: Dict = None,
    ) -> models.PlayRecordResponse:
        """
        This API is used to obtain the local device recording URL address.
        """
        
        kwargs = {}
        kwargs["action"] = "PlayRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PlayRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryForbidPlayChannelList(
            self,
            request: models.QueryForbidPlayChannelListRequest,
            opts: Dict = None,
    ) -> models.QueryForbidPlayChannelListResponse:
        """
        Query the disabled channel list
        """
        
        kwargs = {}
        kwargs["action"] = "QueryForbidPlayChannelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryForbidPlayChannelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshDeviceChannel(
            self,
            request: models.RefreshDeviceChannelRequest,
            opts: Dict = None,
    ) -> models.RefreshDeviceChannelResponse:
        """
        This API is used to synchronize channels of national standard devices. After the API is called, a request is triggered to get the channel list from devices. Newly-added channels are stored, and channels deleted on devices need to be deleted manually and are not automatically deleted in the backend.
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshDeviceChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshDeviceChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetForbidPlayChannels(
            self,
            request: models.SetForbidPlayChannelsRequest,
            opts: Dict = None,
    ) -> models.SetForbidPlayChannelsResponse:
        """
        Forbid the live preview of video channels for root accounts and sub-accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "SetForbidPlayChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetForbidPlayChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceOrganization(
            self,
            request: models.UpdateDeviceOrganizationRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceOrganizationResponse:
        """
        Used to change the organization of devices in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceStatus(
            self,
            request: models.UpdateDeviceStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceStatusResponse:
        """
        Used to enable or disable a device. After it is disabled, device registration is denied.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganization(
            self,
            request: models.UpdateOrganizationRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationResponse:
        """
        Used to modify an organization.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordBackupPlan(
            self,
            request: models.UpdateRecordBackupPlanRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordBackupPlanResponse:
        """
        Used to modify the recording cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordBackupTemplate(
            self,
            request: models.UpdateRecordBackupTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordBackupTemplateResponse:
        """
        Used to modify a video recording cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordBackupTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordBackupTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordPlan(
            self,
            request: models.UpdateRecordPlanRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordPlanResponse:
        """
        This API is used to modify a real-time cloud migration plan.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordTemplate(
            self,
            request: models.UpdateRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordTemplateResponse:
        """
        Used to modify a real-time cloud template.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserDevice(
            self,
            request: models.UpdateUserDeviceRequest,
            opts: Dict = None,
    ) -> models.UpdateUserDeviceResponse:
        """
        This API is used to modify device configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)