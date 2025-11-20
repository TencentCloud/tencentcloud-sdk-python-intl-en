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
from tencentcloud.trro.v20220325 import models
from typing import Dict


class TrroClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'trro.intl.tencentcloudapi.com'
    _service = 'trro'

    async def BatchDeleteDevices(
            self,
            request: models.BatchDeleteDevicesRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteDevicesResponse:
        """
        This API is used to delete devices in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeletePolicy(
            self,
            request: models.BatchDeletePolicyRequest,
            opts: Dict = None,
    ) -> models.BatchDeletePolicyResponse:
        """
        This API is used to batch delete and modify permission configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeletePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeletePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        This API is used to create a device.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
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
        
    async def DescribeDeviceInfo(
            self,
            request: models.DescribeDeviceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceInfoResponse:
        """
        This API is used to get specified device information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceSessionList(
            self,
            request: models.DescribeDeviceSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceSessionListResponse:
        """
        Getting the device session list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectInfo(
            self,
            request: models.DescribeProjectInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectInfoResponse:
        """
        This API is used to get project information.
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
        This API is used to get project lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecentSessionList(
            self,
            request: models.DescribeRecentSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecentSessionListResponse:
        """
        Get the latest device session list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecentSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecentSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionStatistics(
            self,
            request: models.DescribeSessionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionStatisticsResponse:
        """
        Get session statistical values
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionStatisticsByInterval(
            self,
            request: models.DescribeSessionStatisticsByIntervalRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionStatisticsByIntervalResponse:
        """
        Getting session statistics for each time period
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionStatisticsByInterval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionStatisticsByIntervalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeviceLicense(
            self,
            request: models.GetDeviceLicenseRequest,
            opts: Dict = None,
    ) -> models.GetDeviceLicenseResponse:
        """
        Obtain the quantity of available authorizations already bound to the device
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeviceLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeviceLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDevices(
            self,
            request: models.GetDevicesRequest,
            opts: Dict = None,
    ) -> models.GetDevicesResponse:
        """
        Query the authorization binding status of user devices
        """
        
        kwargs = {}
        kwargs["action"] = "GetDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLicenseStat(
            self,
            request: models.GetLicenseStatRequest,
            opts: Dict = None,
    ) -> models.GetLicenseStatResponse:
        """
        Statistics of license types and quantities
        """
        
        kwargs = {}
        kwargs["action"] = "GetLicenseStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLicenseStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLicenses(
            self,
            request: models.GetLicensesRequest,
            opts: Dict = None,
    ) -> models.GetLicensesResponse:
        """
        View the license list by authorization
        """
        
        kwargs = {}
        kwargs["action"] = "GetLicenses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLicensesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDevice(
            self,
            request: models.ModifyDeviceRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceResponse:
        """
        This API is used to modify device information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPolicy(
            self,
            request: models.ModifyPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPolicyResponse:
        """
        This API is used to modify permission configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPolicyResponse
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