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
from tencentcloud.vod.v20240718 import models
from typing import Dict


class VodClient(AbstractClient):
    _apiVersion = '2024-07-18'
    _endpoint = 'vod.intl.tencentcloudapi.com'
    _service = 'vod'

    async def CreateIncrementalMigrationStrategy(
            self,
            request: models.CreateIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateIncrementalMigrationStrategyResponse:
        """
        Create an incremental migration strategy for the storage of the professional application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorage(
            self,
            request: models.CreateStorageRequest,
            opts: Dict = None,
    ) -> models.CreateStorageResponse:
        """
        This API is used to create storage for professional applications.

        Note:
        - This API is exclusively for professional applications.
        - When a customer creates a VOD professional application, the system automatically enables storage in certain regions by default. If the customer needs to enable storage in other regions, they can do so using this API.
        - All storage regions and the regions where storage have already been enabled can be queried using the [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorageCredentials(
            self,
            request: models.CreateStorageCredentialsRequest,
            opts: Dict = None,
    ) -> models.CreateStorageCredentialsResponse:
        """
        The API is used to generate access credentials for VOD professional applications, such as generating credentials for client uploads.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorageCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIncrementalMigrationStrategy(
            self,
            request: models.DeleteIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteIncrementalMigrationStrategyResponse:
        """
        Delete the incremental migration strategy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIncrementalMigrationStrategyInfos(
            self,
            request: models.DescribeIncrementalMigrationStrategyInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIncrementalMigrationStrategyInfosResponse:
        """
        Describe the information of the incremental migration strategy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIncrementalMigrationStrategyInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIncrementalMigrationStrategyInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorage(
            self,
            request: models.DescribeStorageRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageResponse:
        """
        This API is used to query bucket information in the professional application, and it also supports paginated queries.
        Note:
        - This API is exclusively for use in the professional application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIncrementalMigrationStrategy(
            self,
            request: models.ModifyIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyIncrementalMigrationStrategyResponse:
        """
        Modify the information of incremental migration strategy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)