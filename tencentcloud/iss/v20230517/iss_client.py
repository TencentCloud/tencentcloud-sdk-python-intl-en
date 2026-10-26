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
from tencentcloud.iss.v20230517 import models


class IssClient(AbstractClient):
    _apiVersion = '2023-05-17'
    _endpoint = 'iss.intl.tencentcloudapi.com'
    _service = 'iss'


    def AddOrganization(self, request):
        r"""Used to add an organization.

        :param request: Request instance for AddOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordBackupPlan(self, request):
        r"""Used to add a recording cloud migration plan (currently applicable only to devices/video channels connected via the GB28181 protocol and gateway).

        :param request: Request instance for AddRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordBackupTemplate(self, request):
        r"""This API is used to create a video recording cloud template.
        > The feature essentially pulls local device recording data to the cloud (i.e., recordings stored in the IPC camera memory card or NVR hard disk). When operating, first set the recording time period (i.e., the local device recording you want to upload to the cloud), then set the Cloud Upload Time Period and upload speed. The platform will pull the previous day's Time Period Data from the device at the specified speed during the Cloud Upload Time Period.

        > Set the Cloud Upload Time Period to at least meet (Cloud Upload Time Period = previous day's recording time period / cloud upload speed multiplication). It is advisable to set about 10% more time for the Cloud Upload Time Period to avoid incomplete data retrieval due to network fluctuations.

        :param request: Request instance for AddRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordPlan(self, request):
        r"""This API is used to create a real-time cloud migration plan.

        :param request: Request instance for AddRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordRetrieveTask(self, request):
        r"""This API is used to create a retrieval task.

        :param request: Request instance for AddRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddRecordTemplate(self, request):
        r"""Used to add a real-time cloud template.

        :param request: Request instance for AddRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddStreamAuth(self, request):
        r"""Used to set push/pull stream authentication configuration.

        :param request: Request instance for AddStreamAuth.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddStreamAuth", params, headers=headers)
            response = json.loads(body)
            model = models.AddStreamAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUserDevice(self, request):
        r"""This API is used to add a single device. After the device is added, configure it based on the returned results, then wait for device registration or stream pushing.

        :param request: Request instance for AddUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.AddUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AddUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchAddVideoSnapshotConfigChannel(self, request):
        r"""Add channels for screenshot configuration in batches.

        :param request: Request instance for BatchAddVideoSnapshotConfigChannel.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchAddVideoSnapshotConfigChannelRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchAddVideoSnapshotConfigChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchAddVideoSnapshotConfigChannel", params, headers=headers)
            response = json.loads(body)
            model = models.BatchAddVideoSnapshotConfigChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchAssignVLPlanChannels(self, request):
        r"""Batch associate visual understanding plan channels

        :param request: Request instance for BatchAssignVLPlanChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchAssignVLPlanChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchAssignVLPlanChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchAssignVLPlanChannels", params, headers=headers)
            response = json.loads(body)
            model = models.BatchAssignVLPlanChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteVideoDownloadTask(self, request):
        r"""This API is used to delete failed local recording download tasks in batches.

        :param request: Request instance for BatchDeleteVideoDownloadTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchDeleteVideoDownloadTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchDeleteVideoDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteVideoDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteVideoDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchGetVLPlanSourceFileURL(self, request):
        r"""This API is used to batch obtain source material URLs for visual understanding plans.

        :param request: Request instance for BatchGetVLPlanSourceFileURL.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchGetVLPlanSourceFileURLRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchGetVLPlanSourceFileURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchGetVLPlanSourceFileURL", params, headers=headers)
            response = json.loads(body)
            model = models.BatchGetVLPlanSourceFileURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchGetVideoSnapshotImageUrl(self, request):
        r"""Bulk gets screenshot image URLs

        :param request: Request instance for BatchGetVideoSnapshotImageUrl.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchGetVideoSnapshotImageUrlRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchGetVideoSnapshotImageUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchGetVideoSnapshotImageUrl", params, headers=headers)
            response = json.loads(body)
            model = models.BatchGetVideoSnapshotImageUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchOperateDevice(self, request):
        r"""Used for batch operations (enable, disable, delete) on devices.

        :param request: Request instance for BatchOperateDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchOperateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.BatchOperateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CallISAPI(self, request):
        r"""This API can be based on the Hikvision ISUP 5.0 protocol to pass through ISAPI request data. Before calling the API, ensure the device has successfully registered to this platform using the ISUP protocol.

        :param request: Request instance for CallISAPI.
        :type request: :class:`tencentcloud.iss.v20230517.models.CallISAPIRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallISAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallISAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CallISAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDevicePTZ(self, request):
        r"""Used for device channel panning control, including turn, zoom scale, zoom, and aperture.

        :param request: Request instance for ControlDevicePTZ.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDevicePTZRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDevicePTZResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevicePTZ", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDevicePTZResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDevicePreset(self, request):
        r"""Used to operate device preset positions, including settings, deletion, and calls.

        :param request: Request instance for ControlDevicePreset.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDevicePresetRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDevicePresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevicePreset", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDevicePresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDeviceSnapshot(self, request):
        r"""Control device capture (single). Currently only support national standard devices.

        :param request: Request instance for ControlDeviceSnapshot.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDeviceSnapshotRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDeviceSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDeviceSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDeviceSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDeviceStream(self, request):
        r"""This API is used to obtain the real-time streaming address of a device.

        :param request: Request instance for ControlDeviceStream.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDeviceStream", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDeviceStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlRecordTimeline(self, request):
        r"""This API is used to query the local recording timeline info of a device, which is stored locally on the NVR/IPC.

        :param request: Request instance for ControlRecordTimeline.
        :type request: :class:`tencentcloud.iss.v20230517.models.ControlRecordTimelineRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlRecordTimelineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlRecordTimeline", params, headers=headers)
            response = json.loads(body)
            model = models.ControlRecordTimelineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVLPlan(self, request):
        r"""Creates a vision understanding plan

        :param request: Request instance for CreateVLPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.CreateVLPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CreateVLPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVLPlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVLPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVLTemplate(self, request):
        r"""Create a visual understanding template.

        :param request: Request instance for CreateVLTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.CreateVLTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CreateVLTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVLTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVLTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoDownloadTask(self, request):
        r"""This API is used to create a local recording download task.

        :param request: Request instance for CreateVideoDownloadTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.CreateVideoDownloadTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CreateVideoDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoSnapshotConfig(self, request):
        r"""This API is used to create a screenshot configuration.

        :param request: Request instance for CreateVideoSnapshotConfig.
        :type request: :class:`tencentcloud.iss.v20230517.models.CreateVideoSnapshotConfigRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CreateVideoSnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoSnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoSnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoSnapshotTemplate(self, request):
        r"""Create a screenshot template.

        :param request: Request instance for CreateVideoSnapshotTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.CreateVideoSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.CreateVideoSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomain(self, request):
        r"""This API is used to delete domain names.

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganization(self, request):
        r"""This API is used to delete an organization.

        :param request: Request instance for DeleteOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordBackupPlan(self, request):
        r"""Used to delete a video recording cloud template.

        :param request: Request instance for DeleteRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordBackupTemplate(self, request):
        r"""This API is used to delete a video recording cloud template.

        :param request: Request instance for DeleteRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordPlan(self, request):
        r"""This API is used to delete a real-time cloud migration plan.

        :param request: Request instance for DeleteRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordRetrieveTask(self, request):
        r"""This API is used to delete a retrieval task.

        :param request: Request instance for DeleteRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordTemplate(self, request):
        r"""Used to delete a real-time cloud template.

        :param request: Request instance for DeleteRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        r"""Used to delete completed tasks.

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserDevice(self, request):
        r"""This API is used to delete added devices.

        :param request: Request instance for DeleteUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVLPlan(self, request):
        r"""Delete a vision understanding plan

        :param request: Request instance for DeleteVLPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteVLPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteVLPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVLPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVLPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVLTemplate(self, request):
        r"""Delete a visual understanding template.

        :param request: Request instance for DeleteVLTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteVLTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteVLTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVLTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVLTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVideoSnapshotConfig(self, request):
        r"""Deletes screenshot configuration

        :param request: Request instance for DeleteVideoSnapshotConfig.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteVideoSnapshotConfigRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteVideoSnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVideoSnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVideoSnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVideoSnapshotTemplate(self, request):
        r"""This API is used to delete a screenshot template.

        :param request: Request instance for DeleteVideoSnapshotTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DeleteVideoSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DeleteVideoSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVideoSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVideoSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCNAME(self, request):
        r"""This API is used to get the CNAME value based on the service node.

        :param request: Request instance for DescribeCNAME.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeCNAMERequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceChannel(self, request):
        r"""This API is used to query the channels of a device.

        :param request: Request instance for DescribeDeviceChannel.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceChannelRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDevicePreset(self, request):
        r"""This API is used to query preset position information of device channels.

        :param request: Request instance for DescribeDevicePreset.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDevicePresetRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDevicePresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePreset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDevicePresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomain(self, request):
        r"""This API is used to query the list of added domains.

        :param request: Request instance for DescribeDomain.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainRegion(self, request):
        r"""This API is used to query the service nodes that can be bound when a user adds a domain name. The result is all service nodes supported by the platform. Each service node can only be bound to one domain name.

        :param request: Request instance for DescribeDomainRegion.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRegionRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDomainRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGBDeviceAddr(self, request):
        r"""This API is used to obtain the public network address of a national standard device.

        :param request: Request instance for DescribeGBDeviceAddr.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeGBDeviceAddrRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeGBDeviceAddrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGBDeviceAddr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGBDeviceAddrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganization(self, request):
        r"""Used for querying organizations.

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordBackupPlan(self, request):
        r"""This API is used to query recording cloud migration plan details.

        :param request: Request instance for DescribeRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordBackupTemplate(self, request):
        r"""This API is used to query video recording cloud template details.

        :param request: Request instance for DescribeRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordFile(self, request):
        r"""This API is used to query the device cloud recording timeline information, which is the cloud storage video recording after setting a recording schedule for video upload to cloud.

        :param request: Request instance for DescribeRecordFile.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordPlan(self, request):
        r"""This API is used to query real-time cloud migration plan details.

        :param request: Request instance for DescribeRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordPlaybackUrl(self, request):
        r"""This API is used to obtain the cloud recording playback url address.

        :param request: Request instance for DescribeRecordPlaybackUrl.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlaybackUrlRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordPlaybackUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordPlaybackUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordPlaybackUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordRetrieveTask(self, request):
        r"""Used to query the details of a cloud recording retrieval task.

        :param request: Request instance for DescribeRecordRetrieveTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordRetrieveTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordRetrieveTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordTemplate(self, request):
        r"""This API is used to query real-time cloud migration template details.

        :param request: Request instance for DescribeRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamAuth(self, request):
        r"""Used to query push/pull stream authentication configuration.

        :param request: Request instance for DescribeStreamAuth.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTask(self, request):
        r"""This API is used to query task details.

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDevice(self, request):
        r"""This API is used to query detailed information of a device.

        :param request: Request instance for DescribeUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDeviceList(self, request):
        r"""This API is used to query device details in batches.

        :param request: Request instance for DescribeUserDeviceList.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceListRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeUserDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVLPlan(self, request):
        r"""Query the plan details of visual understanding.

        :param request: Request instance for DescribeVLPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVLPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVLPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVLPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVLPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVLPlanResult(self, request):
        r"""Query the result details of a vision understanding plan

        :param request: Request instance for DescribeVLPlanResult.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVLPlanResultRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVLPlanResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVLPlanResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVLPlanResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVLTemplate(self, request):
        r"""Query the details of a visual understanding template.

        :param request: Request instance for DescribeVLTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVLTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVLTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVLTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVLTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoBitRate(self, request):
        r"""This API is used to obtain the bitrate info of a video channel.

        :param request: Request instance for DescribeVideoBitRate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoBitRate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoBitRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoDownloadUrl(self, request):
        r"""This API is used to obtain the download url of cloud recordings.

        :param request: Request instance for DescribeVideoDownloadUrl.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoSnapshotConfig(self, request):
        r"""Queries screenshot configuration details

        :param request: Request instance for DescribeVideoSnapshotConfig.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoSnapshotConfigRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoSnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoSnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoSnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoSnapshotTemplate(self, request):
        r"""Get screenshot template details.

        :param request: Request instance for DescribeVideoSnapshotTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.DescribeVideoSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDeviceSnapshots(self, request):
        r"""Get device capture result list

        :param request: Request instance for ListDeviceSnapshots.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListDeviceSnapshotsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListDeviceSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDeviceSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.ListDeviceSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDevices(self, request):
        r"""This API is used to obtain the device list under the corresponding organization.

        :param request: Request instance for ListDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationChannels(self, request):
        r"""This API is used to query the channel list under the organizational unit directory.

        :param request: Request instance for ListOrganizationChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationChannels", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupPlanDevices(self, request):
        r"""This API is used to query the device channel list under a recording cloud migration plan.

        :param request: Request instance for ListRecordBackupPlanDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupPlanDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupPlanDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupPlans(self, request):
        r"""This API is used to query the recording cloud migration plan list.

        :param request: Request instance for ListRecordBackupPlans.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlansRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordBackupTemplates(self, request):
        r"""This API is used to query the video recording cloud template list.

        :param request: Request instance for ListRecordBackupTemplates.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupTemplatesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordBackupTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordBackupTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordPlanDevices(self, request):
        r"""This API is used to query the device channel list under a real-time cloud migration plan.

        :param request: Request instance for ListRecordPlanDevices.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordPlanDevices", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordPlanDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordPlans(self, request):
        r"""This API is used to query the real-time cloud migration plan list.

        :param request: Request instance for ListRecordPlans.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordPlansRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordPlans", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordRetrieveTasks(self, request):
        r"""This API is used to query the retrieval task list.

        :param request: Request instance for ListRecordRetrieveTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordRetrieveTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordRetrieveTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordRetrieveTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordRetrieveTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRecordTemplates(self, request):
        r"""This API is used to query the real-time cloud migration template list.

        :param request: Request instance for ListRecordTemplates.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRecordTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListRecordTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSubTasks(self, request):
        r"""This API is used to query the subtask list of a query task.

        :param request: Request instance for ListSubTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListSubTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListSubTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSubTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSubTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTasks(self, request):
        r"""This API is used to query the batch task and simple task list.

        :param request: Request instance for ListTasks.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListTasksRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVLPlans(self, request):
        r"""Get the visual understanding plan list.

        :param request: Request instance for ListVLPlans.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListVLPlansRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVLPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVLPlans", params, headers=headers)
            response = json.loads(body)
            model = models.ListVLPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVLTemplates(self, request):
        r"""Get a list of visual understanding templates.

        :param request: Request instance for ListVLTemplates.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListVLTemplatesRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVLTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVLTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListVLTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVideoDownloadTask(self, request):
        r"""This API is used to query the recording download task list in this store.

        :param request: Request instance for ListVideoDownloadTask.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListVideoDownloadTaskRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVideoDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVideoDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.ListVideoDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVideoSnapshotTemplate(self, request):
        r"""This API is used to search the screenshot template details list.

        :param request: Request instance for ListVideoSnapshotTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.ListVideoSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVideoSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVideoSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ListVideoSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVLPlan(self, request):
        r"""Modify a vision understanding plan

        :param request: Request instance for ModifyVLPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.ModifyVLPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ModifyVLPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVLPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVLPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVideoSnapshotConfig(self, request):
        r"""Update screenshot configuration

        :param request: Request instance for ModifyVideoSnapshotConfig.
        :type request: :class:`tencentcloud.iss.v20230517.models.ModifyVideoSnapshotConfigRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.ModifyVideoSnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVideoSnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVideoSnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PlayRecord(self, request):
        r"""This API is used to obtain the local device recording URL address.

        :param request: Request instance for PlayRecord.
        :type request: :class:`tencentcloud.iss.v20230517.models.PlayRecordRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.PlayRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PlayRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PlayRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryForbidPlayChannelList(self, request):
        r"""Query the disabled channel list

        :param request: Request instance for QueryForbidPlayChannelList.
        :type request: :class:`tencentcloud.iss.v20230517.models.QueryForbidPlayChannelListRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.QueryForbidPlayChannelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryForbidPlayChannelList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryForbidPlayChannelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshDeviceChannel(self, request):
        r"""This API is used to synchronize channels of national standard devices. After the API is called, a request is triggered to get the channel list from devices. Newly-added channels are stored, and channels deleted on devices need to be deleted manually and are not automatically deleted in the backend.

        :param request: Request instance for RefreshDeviceChannel.
        :type request: :class:`tencentcloud.iss.v20230517.models.RefreshDeviceChannelRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.RefreshDeviceChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshDeviceChannel", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshDeviceChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetForbidPlayChannels(self, request):
        r"""Forbid the live preview of video channels for root accounts and sub-accounts.

        :param request: Request instance for SetForbidPlayChannels.
        :type request: :class:`tencentcloud.iss.v20230517.models.SetForbidPlayChannelsRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.SetForbidPlayChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetForbidPlayChannels", params, headers=headers)
            response = json.loads(body)
            model = models.SetForbidPlayChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeviceOrganization(self, request):
        r"""Used to change the organization of devices in batches.

        :param request: Request instance for UpdateDeviceOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeviceStatus(self, request):
        r"""Used to enable or disable a device. After it is disabled, device registration is denied.

        :param request: Request instance for UpdateDeviceStatus.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceStatusRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganization(self, request):
        r"""Used to modify an organization.

        :param request: Request instance for UpdateOrganization.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateOrganizationRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordBackupPlan(self, request):
        r"""Used to modify the recording cloud migration plan.

        :param request: Request instance for UpdateRecordBackupPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordBackupTemplate(self, request):
        r"""Used to modify a video recording cloud template.

        :param request: Request instance for UpdateRecordBackupTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordBackupTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordBackupTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordPlan(self, request):
        r"""This API is used to modify a real-time cloud migration plan.

        :param request: Request instance for UpdateRecordPlan.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordPlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRecordTemplate(self, request):
        r"""Used to modify a real-time cloud template.

        :param request: Request instance for UpdateRecordTemplate.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserDevice(self, request):
        r"""This API is used to modify device configuration information.

        :param request: Request instance for UpdateUserDevice.
        :type request: :class:`tencentcloud.iss.v20230517.models.UpdateUserDeviceRequest`
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateUserDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserDevice", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))