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

    async def CreateIndex(
            self,
            request: models.CreateIndexRequest,
            opts: Dict = None,
    ) -> models.CreateIndexResponse:
        """
        This API is used to create indices.
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
        This API is used to create an ES cluster instance with the specified specification.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIndex(
            self,
            request: models.DeleteIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteIndexResponse:
        """
        This API is used to delete indices.
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
        This API is used to terminate a cluster instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
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
        This API is used to obtain index metadata.
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
        This API is used to query the eligible ES cluster logs in the current region.
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
        This API is used to query the operation history of an instance by specified criteria.
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
        This API is used to query all eligible instances in the current region under the current account.
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
        This API is used to query view data from three dimensions: cluster, node, and Kibana.
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
        This API is used to get the node types used to receive client requests.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestTargetNodeTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestTargetNodeTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        This API is used to restart an ES cluster instance (for operations such as system update).
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
        This API is used to restart Kibana.
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
        This API is used to restart cluster nodes.
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
        This API is used to update ES cluster dictionaries.
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
        This API is used to update indices.
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
        This API is used for operations such as modifying node specification, renaming an instance, modifying configuration, resetting password, and setting Kibana blocklist/allowlist. `InstanceId` is required, while `ForceRestart` is optional. Other parameters or parameter combinations and their meanings are as follows:
        - InstanceName: renames an instance (only for instance identification)
        - NodeInfoList: modifies node configuration (horizontally scaling nodes, vertically scaling nodes, adding primary nodes, adding cold nodes, etc.)
        - EsConfig: modifies cluster configuration
        - Password: changes the password of the default user "elastic"
        - EsAcl: modifies the ACL
        - CosBackUp: sets auto-backup to COS for a cluster
        Only one of the parameters or parameter combinations above can be passed in at a time, while passing fewer or more ones will cause the request to fail.
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
        This API is used to change the list of plugins.
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
        This API is used to update the node types used to receive client requests.
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
        This API is used to upgrade ES cluster version
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
        This API is used to upgrade ES X-Pack.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)