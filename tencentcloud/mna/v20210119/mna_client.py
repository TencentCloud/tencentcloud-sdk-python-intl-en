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
from tencentcloud.mna.v20210119 import models


class MnaClient(AbstractClient):
    _apiVersion = '2021-01-19'
    _endpoint = 'mna.intl.tencentcloudapi.com'
    _service = 'mna'


    def ActivateHardware(self, request):
        r"""Activate hardware device

        :param request: Request instance for ActivateHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.ActivateHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ActivateHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateHardware", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddApplication(self, request):
        r"""This API is used to create an application

        :param request: Request instance for AddApplication.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddApplicationRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddApplication", params, headers=headers)
            response = json.loads(body)
            model = models.AddApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDevice(self, request):
        r"""Create new device records

        :param request: Request instance for AddDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDevice", params, headers=headers)
            response = json.loads(body)
            model = models.AddDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddGroup(self, request):
        r"""Create group

        :param request: Request instance for AddGroup.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddGroupRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddHardware(self, request):
        r"""Add hardware devices, generate inactive hardware devices, and support batch addition

        :param request: Request instance for AddHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddHardware", params, headers=headers)
            response = json.loads(body)
            model = models.AddHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddL3Conn(self, request):
        r"""Create an interconnection rule

        :param request: Request instance for AddL3Conn.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddL3ConnRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddL3ConnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddL3Conn", params, headers=headers)
            response = json.loads(body)
            model = models.AddL3ConnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEncryptedKey(self, request):
        r"""This API is used to configure and refresh preset keys.

        :param request: Request instance for CreateEncryptedKey.
        :type request: :class:`tencentcloud.mna.v20210119.models.CreateEncryptedKeyRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.CreateEncryptedKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEncryptedKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEncryptedKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplication(self, request):
        r"""This API is used to delete applications

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDevice(self, request):
        r"""Delete device info

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        r"""Delete group

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL3Conn(self, request):
        r"""Delete an interconnection rule

        :param request: Request instance for DeleteL3Conn.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteL3ConnRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteL3ConnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL3Conn", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL3ConnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessRegions(self, request):
        r"""Query the access region list.

        :param request: Request instance for DescribeAccessRegions.
        :type request: :class:`tencentcloud.mna.v20210119.models.DescribeAccessRegionsRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DescribeAccessRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadActiveDeviceCount(self, request):
        r"""Download the number of active devices statistics

        :param request: Request instance for DownloadActiveDeviceCount.
        :type request: :class:`tencentcloud.mna.v20210119.models.DownloadActiveDeviceCountRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DownloadActiveDeviceCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadActiveDeviceCount", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadActiveDeviceCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetActiveDeviceCount(self, request):
        r"""Number of active devices statistics

        :param request: Request instance for GetActiveDeviceCount.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetActiveDeviceCountRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetActiveDeviceCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetActiveDeviceCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetActiveDeviceCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetApplication(self, request):
        r"""This API is used to query applications.

        :param request: Request instance for GetApplication.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetApplicationRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetApplication", params, headers=headers)
            response = json.loads(body)
            model = models.GetApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDestIPByName(self, request):
        r"""Statistics of a single device accessing the target IP address

        :param request: Request instance for GetDestIPByName.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDestIPByNameRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDestIPByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDestIPByName", params, headers=headers)
            response = json.loads(body)
            model = models.GetDestIPByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevice(self, request):
        r"""This API is used to search device details by specified device ID.

        :param request: Request instance for GetDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevice", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevicePayMode(self, request):
        r"""This API is used to obtain the payment mode of a device.

        :param request: Request instance for GetDevicePayMode.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDevicePayModeRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDevicePayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevicePayMode", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicePayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevices(self, request):
        r"""This API is used to get device information list.

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevices", params, headers=headers)
            response = json.loads(body)
            model = models.GetDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowAlarmInfo(self, request):
        r"""This API is used to query user traffic alarm settings based on AppId, including threshold, callback url and key.

        :param request: Request instance for GetFlowAlarmInfo.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowAlarmInfoRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowAlarmInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowAlarmInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowAlarmInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowPackages(self, request):
        r"""Retrieve the data transfer plan list

        :param request: Request instance for GetFlowPackages.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowPackagesRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowPackages", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowStatistic(self, request):
        r"""Retrieve traffic usage data for a specified device Id at a specified time point.

        :param request: Request instance for GetFlowStatistic.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowStatisticByGroup(self, request):
        r"""Retrieve traffic usage data for the specified group and time period

        :param request: Request instance for GetFlowStatisticByGroup.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByGroupRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatisticByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowStatisticByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowStatisticByName(self, request):
        r"""Retrieve traffic usage data for a specified device Id at a specified time point.

        :param request: Request instance for GetFlowStatisticByName.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByNameRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatisticByName", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowStatisticByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFlowStatisticByRegion(self, request):
        r"""Retrieve traffic usage data for the specified region and time point

        :param request: Request instance for GetFlowStatisticByRegion.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByRegionRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatisticByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.GetFlowStatisticByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupDetail(self, request):
        r"""View group details

        :param request: Request instance for GetGroupDetail.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetGroupDetailRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupList(self, request):
        r"""This API is used to obtain a group list.

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetHardwareInfo(self, request):
        r"""This API is used to get hardware device information.

        :param request: Request instance for GetHardwareInfo.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetHardwareInfoRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetHardwareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetHardwareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetHardwareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetHardwareList(self, request):
        r"""This API is used to get the hardware list of the manufacturer.

        :param request: Request instance for GetHardwareList.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetHardwareListRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetHardwareListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetHardwareList", params, headers=headers)
            response = json.loads(body)
            model = models.GetHardwareListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetL3ConnList(self, request):
        r"""Retrieve the list of interconnection rules

        :param request: Request instance for GetL3ConnList.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetL3ConnListRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetL3ConnListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetL3ConnList", params, headers=headers)
            response = json.loads(body)
            model = models.GetL3ConnListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMonitorDataByName(self, request):
        r"""This API is used to obtain the download file URL for all monitoring metrics of a single device.

        :param request: Request instance for GetMonitorDataByName.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetMonitorDataByNameRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetMonitorDataByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMonitorDataByName", params, headers=headers)
            response = json.loads(body)
            model = models.GetMonitorDataByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMultiFlowStatistic(self, request):
        r"""Obtain batch device traffic statistics curves

        :param request: Request instance for GetMultiFlowStatistic.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetMultiFlowStatisticRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetMultiFlowStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMultiFlowStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.GetMultiFlowStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetNetMonitor(self, request):
        r"""This API is used to obtain real-time traffic statistics per device.

        :param request: Request instance for GetNetMonitor.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetNetMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.GetNetMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetNetMonitorByName(self, request):
        r"""This API is used to obtain real-time traffic statistics per device.

        :param request: Request instance for GetNetMonitorByName.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorByNameRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetNetMonitorByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetNetMonitorByName", params, headers=headers)
            response = json.loads(body)
            model = models.GetNetMonitorByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPublicKey(self, request):
        r"""This API is used to access the public key for signature verification.

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStatisticData(self, request):
        r"""Download traffic data on the usage statistics page

        :param request: Request instance for GetStatisticData.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticData", params, headers=headers)
            response = json.loads(body)
            model = models.GetStatisticDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStatisticDataByName(self, request):
        r"""Download traffic data on the usage statistics page

        :param request: Request instance for GetStatisticDataByName.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataByNameRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticDataByName", params, headers=headers)
            response = json.loads(body)
            model = models.GetStatisticDataByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetVendorHardware(self, request):
        r"""This API is used to get the hardware device list of the manufacturer.

        :param request: Request instance for GetVendorHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetVendorHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetVendorHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVendorHardware", params, headers=headers)
            response = json.loads(body)
            model = models.GetVendorHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupAddDevice(self, request):
        r"""Add device to already exist group

        :param request: Request instance for GroupAddDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.GroupAddDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GroupAddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupAddDevice", params, headers=headers)
            response = json.loads(body)
            model = models.GroupAddDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupDeleteDevice(self, request):
        r"""Delete devices in the group

        :param request: Request instance for GroupDeleteDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.GroupDeleteDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GroupDeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupDeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.GroupDeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceAccessRegions(self, request):
        r"""This API is used to modify device connectivity regions.

        :param request: Request instance for ModifyDeviceAccessRegions.
        :type request: :class:`tencentcloud.mna.v20210119.models.ModifyDeviceAccessRegionsRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ModifyDeviceAccessRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceAccessRegions", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceAccessRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPackageRenewFlag(self, request):
        r"""Auto renewal of data transfer plans can be enabled or disabled, unaffected by ongoing effective plans in the current cycle.

        :param request: Request instance for ModifyPackageRenewFlag.
        :type request: :class:`tencentcloud.mna.v20210119.models.ModifyPackageRenewFlagRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ModifyPackageRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPackageRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPackageRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OrderFlowPackage(self, request):
        r"""Purchase a Prepaid Traffic Package

        :param request: Request instance for OrderFlowPackage.
        :type request: :class:`tencentcloud.mna.v20210119.models.OrderFlowPackageRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.OrderFlowPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OrderFlowPackage", params, headers=headers)
            response = json.loads(body)
            model = models.OrderFlowPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OrderPerLicense(self, request):
        r"""Purchase a single-use License

        :param request: Request instance for OrderPerLicense.
        :type request: :class:`tencentcloud.mna.v20210119.models.OrderPerLicenseRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.OrderPerLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OrderPerLicense", params, headers=headers)
            response = json.loads(body)
            model = models.OrderPerLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportOrder(self, request):
        r"""Users report custom order information, and the Multiple Network Acceleration service saves the information related to.

        :param request: Request instance for ReportOrder.
        :type request: :class:`tencentcloud.mna.v20210119.models.ReportOrderRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.ReportOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ReportOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNotifyUrl(self, request):
        r"""This API is used to set user traffic alarm information. Use this API setting to configure the data transfer plan alarm threshold as well as the callback url and key when an alarm is generated.

        :param request: Request instance for SetNotifyUrl.
        :type request: :class:`tencentcloud.mna.v20210119.models.SetNotifyUrlRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.SetNotifyUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNotifyUrl", params, headers=headers)
            response = json.loads(body)
            model = models.SetNotifyUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApplicationInfo(self, request):
        r"""Update application information

        :param request: Request instance for UpdateApplicationInfo.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateApplicationInfoRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApplicationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApplicationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApplicationKey(self, request):
        r"""Update application key

        :param request: Request instance for UpdateApplicationKey.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateApplicationKeyRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateApplicationKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApplicationKey", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApplicationKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDevice(self, request):
        r"""Update device information

        :param request: Request instance for UpdateDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGroup(self, request):
        r"""Update group remark

        :param request: Request instance for UpdateGroup.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateGroupRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateHardware(self, request):
        r"""Refresh hardware info

        :param request: Request instance for UpdateHardware.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateHardwareRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateHardwareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateHardware", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateHardwareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateL3Cidr(self, request):
        r"""Update the interconnection rule CIDR

        :param request: Request instance for UpdateL3Cidr.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateL3CidrRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateL3CidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateL3Cidr", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateL3CidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateL3Conn(self, request):
        r"""Update the interconnection rule remark

        :param request: Request instance for UpdateL3Conn.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateL3ConnRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateL3ConnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateL3Conn", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateL3ConnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateL3Switch(self, request):
        r"""Update the interconnection rule switch

        :param request: Request instance for UpdateL3Switch.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateL3SwitchRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateL3SwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateL3Switch", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateL3SwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))