# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.trro.v20220325 import models


class TrroClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'trro.intl.tencentcloudapi.com'
    _service = 'trro'


    def BatchDeleteDevices(self, request):
        """This API is used to delete devices in batches.

        :param request: Request instance for BatchDeleteDevices.
        :type request: :class:`tencentcloud.trro.v20220325.models.BatchDeleteDevicesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.BatchDeleteDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteDevices", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeletePolicy(self, request):
        """This API is used to batch delete and modify permission configurations.

        :param request: Request instance for BatchDeletePolicy.
        :type request: :class:`tencentcloud.trro.v20220325.models.BatchDeletePolicyRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.BatchDeletePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeletePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeletePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDevice(self, request):
        """This API is used to create a device.

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.trro.v20220325.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """This API is used to create a project.

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        """This API is used to delete a project.

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceInfo(self, request):
        """This API is used to get specified device information.

        :param request: Request instance for DescribeDeviceInfo.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceInfoRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceSessionList(self, request):
        """Getting the device session list

        :param request: Request instance for DescribeDeviceSessionList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeDeviceSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectInfo(self, request):
        """This API is used to get project information.

        :param request: Request instance for DescribeProjectInfo.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeProjectInfoRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeProjectInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectList(self, request):
        """This API is used to get project lists.

        :param request: Request instance for DescribeProjectList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeProjectListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecentSessionList(self, request):
        """Get the latest device session list

        :param request: Request instance for DescribeRecentSessionList.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeRecentSessionListRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeRecentSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecentSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecentSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionStatistics(self, request):
        """Get session statistical values

        :param request: Request instance for DescribeSessionStatistics.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionStatisticsByInterval(self, request):
        """Getting session statistics for each time period

        :param request: Request instance for DescribeSessionStatisticsByInterval.
        :type request: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsByIntervalRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.DescribeSessionStatisticsByIntervalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionStatisticsByInterval", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionStatisticsByIntervalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeviceLicense(self, request):
        """Obtain the quantity of available authorizations already bound to the device

        :param request: Request instance for GetDeviceLicense.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetDeviceLicenseRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetDeviceLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeviceLicense", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeviceLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDevices(self, request):
        """Query the authorization binding status of user devices

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetDevicesResponse`

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


    def GetLicenseStat(self, request):
        """Statistics of license types and quantities

        :param request: Request instance for GetLicenseStat.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetLicenseStatRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetLicenseStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLicenseStat", params, headers=headers)
            response = json.loads(body)
            model = models.GetLicenseStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLicenses(self, request):
        """View the license list by authorization

        :param request: Request instance for GetLicenses.
        :type request: :class:`tencentcloud.trro.v20220325.models.GetLicensesRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.GetLicensesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLicenses", params, headers=headers)
            response = json.loads(body)
            model = models.GetLicensesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDevice(self, request):
        """This API is used to modify device information.

        :param request: Request instance for ModifyDevice.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyDeviceRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPolicy(self, request):
        """This API is used to modify permission configuration.

        :param request: Request instance for ModifyPolicy.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyPolicyRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        """This API is used to modify project information.

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.trro.v20220325.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.trro.v20220325.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))