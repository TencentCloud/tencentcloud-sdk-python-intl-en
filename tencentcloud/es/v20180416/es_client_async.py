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
from tencentcloud.es.v20180416 import models
from typing import Dict


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.intl.tencentcloudapi.com'
    _service = 'es'

    async def CreateAutoBackUpStrategy(
            self,
            request: models.CreateAutoBackUpStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoBackUpStrategyResponse:
        """
        This API is used to create an auto backup snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoBackUpStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoBackUpStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIndex(
            self,
            request: models.CreateIndexRequest,
            opts: Dict = None,
    ) -> models.CreateIndexResponse:
        """
        Create an index
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        Create an ES cluster instance with the specified specification.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoBackUpStrategy(
            self,
            request: models.DeleteAutoBackUpStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoBackUpStrategyResponse:
        """
        This API is used to delete an auto backup snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoBackUpStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoBackUpStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIndex(
            self,
            request: models.DeleteIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteIndexResponse:
        """
        Delete an index
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        Terminate cluster instances
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoBackUpStrategy(
            self,
            request: models.DescribeAutoBackUpStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoBackUpStrategyResponse:
        """
        This API is used to obtain an auto backup snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoBackUpStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoBackUpStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexList(
            self,
            request: models.DescribeIndexListRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexListResponse:
        """
        This API is used to obtain the index list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexMeta(
            self,
            request: models.DescribeIndexMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexMetaResponse:
        """
        This API is used to retrieve index metadata.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogs(
            self,
            request: models.DescribeInstanceLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogsResponse:
        """
        Query the logs of eligible ES clusters in that region for the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        Query the operation records of an instance under specified conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        Query all instances meeting conditions for the user in that region
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeViews(
            self,
            request: models.DescribeViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeViewsResponse:
        """
        Query view data of a cluster, including cluster-level, node, and Kibana dimensions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRequestTargetNodeTypes(
            self,
            request: models.GetRequestTargetNodeTypesRequest,
            opts: Dict = None,
    ) -> models.GetRequestTargetNodeTypesResponse:
        """
        Get the node type that receives client requests.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestTargetNodeTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestTargetNodeTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackUpCommonInfo(
            self,
            request: models.ModifyAutoBackUpCommonInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackUpCommonInfoResponse:
        """
        This API is used to modify the common information of an auto backup snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackUpCommonInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackUpCommonInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackUpStrategy(
            self,
            request: models.ModifyAutoBackUpStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackUpStrategyResponse:
        """
        This API is used to modify an auto backup snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackUpStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackUpStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        Restart ES cluster instances for system version update.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartKibana(
            self,
            request: models.RestartKibanaRequest,
            opts: Dict = None,
    ) -> models.RestartKibanaResponse:
        """
        Restart Kibana
        """
        
        kwargs = {}
        kwargs["action"] = "RestartKibana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartKibanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartNodes(
            self,
            request: models.RestartNodesRequest,
            opts: Dict = None,
    ) -> models.RestartNodesResponse:
        """
        Used to restart cluster nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDictionaries(
            self,
            request: models.UpdateDictionariesRequest,
            opts: Dict = None,
    ) -> models.UpdateDictionariesResponse:
        """
        Update the ES cluster dictionary
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDictionaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDictionariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateIndex(
            self,
            request: models.UpdateIndexRequest,
            opts: Dict = None,
    ) -> models.UpdateIndexResponse:
        """
        Updates an index
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateInstance(
            self,
            request: models.UpdateInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateInstanceResponse:
        """
        Perform operations on the cluster, such as node specification change, instance name modification, configuration modification, password resetting, and Kibana blocklist/allowlist addition. InstanceId is a required parameter, while ForceRestart is optional. The remaining parameter combinations and their meanings are as follows:
        - InstanceName: Modify the instance name (only used to identify the instance)
        -NodeInfoList: Modify node configuration (horizontally scale nodes, vertically scale nodes, add primary nodes, add cold nodes, etc.)
        -EsConfig: modify cluster configuration
        -Password: Modify the password of the default user elastic
        -EsAcl: Modify an ACL
        -CosBackUp: Set cluster COS auto backup information
        Only one of the above parameters can be passed. Passing more or fewer will cause request failure.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePlugins(
            self,
            request: models.UpdatePluginsRequest,
            opts: Dict = None,
    ) -> models.UpdatePluginsResponse:
        """
        Update the plug-in list
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRequestTargetNodeTypes(
            self,
            request: models.UpdateRequestTargetNodeTypesRequest,
            opts: Dict = None,
    ) -> models.UpdateRequestTargetNodeTypesResponse:
        """
        This API is used to update the node type that receives client requests.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRequestTargetNodeTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRequestTargetNodeTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        Upgrades the edition of an ES cluster
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLicense(
            self,
            request: models.UpgradeLicenseRequest,
            opts: Dict = None,
    ) -> models.UpgradeLicenseResponse:
        """
        Upgrade ES commercial features
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)