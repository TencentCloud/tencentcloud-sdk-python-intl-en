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
from tencentcloud.smh.v20210712 import models
from typing import Dict


class SmhClient(AbstractClient):
    _apiVersion = '2021-07-12'
    _endpoint = 'smh.intl.tencentcloudapi.com'
    _service = 'smh'

    async def CreateLibrary(
            self,
            request: models.CreateLibraryRequest,
            opts: Dict = None,
    ) -> models.CreateLibraryResponse:
        """
        This API is used to create a PaaS service media library.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLibrary(
            self,
            request: models.DeleteLibraryRequest,
            opts: Dict = None,
    ) -> models.DeleteLibraryResponse:
        """
        This API is used to delete a PaaS service media library.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLibraries(
            self,
            request: models.DescribeLibrariesRequest,
            opts: Dict = None,
    ) -> models.DescribeLibrariesResponse:
        """
        This API is used to query the PaaS service repository list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLibraries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLibrariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLibrarySecret(
            self,
            request: models.DescribeLibrarySecretRequest,
            opts: Dict = None,
    ) -> models.DescribeLibrarySecretResponse:
        """
        This API is used to query the PaaS service Media Library Key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLibrarySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLibrarySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfficialInstances(
            self,
            request: models.DescribeOfficialInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeOfficialInstancesResponse:
        """
        This API is used to query official cloud disk instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfficialInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfficialInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfficialOverview(
            self,
            request: models.DescribeOfficialOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeOfficialOverviewResponse:
        """
        This API is used to query overview data of official cloud disk instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfficialOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfficialOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficPackages(
            self,
            request: models.DescribeTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficPackagesResponse:
        """
        This API is used to query traffic packages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLibrary(
            self,
            request: models.ModifyLibraryRequest,
            opts: Dict = None,
    ) -> models.ModifyLibraryResponse:
        """
        This API is used to modify the configuration items of a PaaS service media library.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLibrary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLibraryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSmsCode(
            self,
            request: models.SendSmsCodeRequest,
            opts: Dict = None,
    ) -> models.SendSmsCodeResponse:
        """
        This API is used to send SMS verification codes for changing the admin account of a super official cloud disk instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SendSmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifySmsCode(
            self,
            request: models.VerifySmsCodeRequest,
            opts: Dict = None,
    ) -> models.VerifySmsCodeResponse:
        """
        This API is used to verify the SMS verification code for rebinding the super administrator account of an official cloud disk instance.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifySmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifySmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)