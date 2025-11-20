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
from tencentcloud.cdwpg.v20201230 import models
from typing import Dict


class CdwpgClient(AbstractClient):
    _apiVersion = '2020-12-30'
    _endpoint = 'cdwpg.intl.tencentcloudapi.com'
    _service = 'cdwpg'

    async def CreateInstanceByApi(
            self,
            request: models.CreateInstanceByApiRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceByApiResponse:
        """
        This API is used to create  instance
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to obtain the account list corresponding to the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBConfigHistory(
            self,
            request: models.DescribeDBConfigHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDBConfigHistoryResponse:
        """
        Describe DBConfig History
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBConfigHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBConfigHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParams(
            self,
            request: models.DescribeDBParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParamsResponse:
        """
        This API is used to describe instance configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorLog(
            self,
            request: models.DescribeErrorLogRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorLogResponse:
        """
        This API is used to query error logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        This API is used to query the instance information by an instance ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceInfo(
            self,
            request: models.DescribeInstanceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceInfoResponse:
        """
        This API is used to get instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodes(
            self,
            request: models.DescribeInstanceNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesResponse:
        """
        This API is used to list nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        This API is used to get operations of the instance .
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceState(
            self,
            request: models.DescribeInstanceStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStateResponse:
        """
        This API is used to display instance status, process progress, etc., in the instance details page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to get a list of  instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleInstances(
            self,
            request: models.DescribeSimpleInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleInstancesResponse:
        """
        This API is used to get a list of instance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLog(
            self,
            request: models.DescribeSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogResponse:
        """
        This API is used to query slow SQL logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeList(
            self,
            request: models.DescribeUpgradeListRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeListResponse:
        """
        This API is used to obtain instance upgrade records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserHbaConfig(
            self,
            request: models.DescribeUserHbaConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserHbaConfigResponse:
        """
        Describe User HbaConfig.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserHbaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserHbaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstanceByApi(
            self,
            request: models.DestroyInstanceByApiRequest,
            opts: Dict = None,
    ) -> models.DestroyInstanceByApiResponse:
        """
        This API is used to destroy instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstanceByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstanceByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        This API is used to modify instance configurations
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify instance information. Only the name of an instance can be modified currently.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserHba(
            self,
            request: models.ModifyUserHbaRequest,
            opts: Dict = None,
    ) -> models.ModifyUserHbaResponse:
        """
        This API is used to modify user Hba configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserHba"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserHbaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        This API is used to change account password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        This API is used by users to proactively restart instances in the console.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        This API is used to scale out instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpInstance(
            self,
            request: models.ScaleUpInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleUpInstanceResponse:
        """
        This API is used to scale up instance in the console.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        This API is used to upgrade Instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)