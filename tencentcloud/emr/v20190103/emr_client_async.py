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
from tencentcloud.emr.v20190103 import models
from typing import Dict


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.intl.tencentcloudapi.com'
    _service = 'emr'

    async def AddMetricScaleStrategy(
            self,
            request: models.AddMetricScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.AddMetricScaleStrategyResponse:
        """
        This API is used to add scaling rules by load and time.
        """
        
        kwargs = {}
        kwargs["action"] = "AddMetricScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMetricScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNodeResourceConfig(
            self,
            request: models.AddNodeResourceConfigRequest,
            opts: Dict = None,
    ) -> models.AddNodeResourceConfigResponse:
        """
        This API is used to add node specifications of the current cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodeResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodeResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUsersForUserManager(
            self,
            request: models.AddUsersForUserManagerRequest,
            opts: Dict = None,
    ) -> models.AddUsersForUserManagerResponse:
        """
        This API is available for clusters with OpenLDAP components configured.
        This API is used to add user lists (user management).
        """
        
        kwargs = {}
        kwargs["action"] = "AddUsersForUserManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUsersForUserManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        This API is used to mount cloud disks.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConvertPreToPostCluster(
            self,
            request: models.ConvertPreToPostClusterRequest,
            opts: Dict = None,
    ) -> models.ConvertPreToPostClusterResponse:
        """
        This API is used to convert a monthly subscription cluster to a pay-as-you-go cluster (excluding cdb).
        """
        
        kwargs = {}
        kwargs["action"] = "ConvertPreToPostCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConvertPreToPostClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        This API is used to create an EMR cluster instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupsSTD(
            self,
            request: models.CreateGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.CreateGroupsSTDResponse:
        """
        This API is used to create user groups in batches under User Management.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        This API is used to create an EMR cluster instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSLInstance(
            self,
            request: models.CreateSLInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateSLInstanceResponse:
        """
        This API is used to create a Serverless HBase instance.- If the API call is successful, a Serverless HBase instance will be created. If the instance creation request is successful, the InstanceId of the created instance and the RequestID of the request will be returned.- This is an asynchronous API. The operation is not completed immediately when the API call returns. The instance operation result can be viewed by calling DescribeInstancesList to view the StatusDesc status of the current instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScaleStrategy(
            self,
            request: models.DeleteAutoScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScaleStrategyResponse:
        """
        This API is used to delete automatic scaling rules. Nodes scaled based on these rules are destroyed in the background.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroupsSTD(
            self,
            request: models.DeleteGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupsSTDResponse:
        """
        This API is used to delete user groups in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNodeResourceConfig(
            self,
            request: models.DeleteNodeResourceConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteNodeResourceConfigResponse:
        """
        This API is used to delete the node specifications of the current cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNodeResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNodeResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployYarnConf(
            self,
            request: models.DeployYarnConfRequest,
            opts: Dict = None,
    ) -> models.DeployYarnConfResponse:
        """
        This API is used to bring the configuration into effect in YARN resource scheduling after deployment.
        """
        
        kwargs = {}
        kwargs["action"] = "DeployYarnConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployYarnConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleGroupGlobalConf(
            self,
            request: models.DescribeAutoScaleGroupGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleGroupGlobalConfResponse:
        """
        This API is used to access the global configuration of automatic scaling.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleGroupGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleGroupGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleRecords(
            self,
            request: models.DescribeAutoScaleRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleRecordsResponse:
        """
        This API is used to inquiry detailed records of cluster autoscaling.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleStrategies(
            self,
            request: models.DescribeAutoScaleStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleStrategiesResponse:
        """
        This API is used to access automatic scaling rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterFlowStatusDetail(
            self,
            request: models.DescribeClusterFlowStatusDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterFlowStatusDetailResponse:
        """
        This API is used to query the EMR task running details status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterFlowStatusDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterFlowStatusDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodes(
            self,
            request: models.DescribeClusterNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodesResponse:
        """
        This API is used to query the information of nodes in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDAGInfo(
            self,
            request: models.DescribeDAGInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDAGInfoResponse:
        """
        This API is used to query DAG information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDAGInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDAGInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmrApplicationStatics(
            self,
            request: models.DescribeEmrApplicationStaticsRequest,
            opts: Dict = None,
    ) -> models.DescribeEmrApplicationStaticsResponse:
        """
        This API is used to query the YARN application statistics API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmrApplicationStatics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmrApplicationStaticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmrOverviewMetrics(
            self,
            request: models.DescribeEmrOverviewMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeEmrOverviewMetricsResponse:
        """
        This API is used to query the metric data on the monitoring overview page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmrOverviewMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmrOverviewMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalConfig(
            self,
            request: models.DescribeGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalConfigResponse:
        """
        This API is used to query the global configurations of YARN Resource Scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupsSTD(
            self,
            request: models.DescribeGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupsSTDResponse:
        """
        This API is used to query a user group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHBaseTableOverview(
            self,
            request: models.DescribeHBaseTableOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeHBaseTableOverviewResponse:
        """
        This API is used to access the overview of HBase table-level monitoring data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHBaseTableOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHBaseTableOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHDFSStorageInfo(
            self,
            request: models.DescribeHDFSStorageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHDFSStorageInfoResponse:
        """
        This API is used to query information of file(s) stored in HDFS.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHDFSStorageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHDFSStorageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHiveQueries(
            self,
            request: models.DescribeHiveQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeHiveQueriesResponse:
        """
        This API is used to inquiry Hive query data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHiveQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHiveQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsightList(
            self,
            request: models.DescribeInsightListRequest,
            opts: Dict = None,
    ) -> models.DescribeInsightListResponse:
        """
        This API is used to obtain insight result information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsightList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsightListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInspectionTaskResult(
            self,
            request: models.DescribeInspectionTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeInspectionTaskResultResponse:
        """
        This API is used to obtain the inspection task result list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInspectionTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInspectionTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the information of instances in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesList(
            self,
            request: models.DescribeInstancesListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesListResponse:
        """
        This API is used to query the cluster list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKyuubiQueryInfo(
            self,
            request: models.DescribeKyuubiQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeKyuubiQueryInfoResponse:
        """
        This API is used to query Kyuubi query information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKyuubiQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKyuubiQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeDataDisks(
            self,
            request: models.DescribeNodeDataDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeDataDisksResponse:
        """
        This API is used to query data disk information of nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeDataDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeDataDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeResourceConfigFast(
            self,
            request: models.DescribeNodeResourceConfigFastRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeResourceConfigFastResponse:
        """
        This API is used to quickly obtain node specifications of the current cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeResourceConfigFast"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeResourceConfigFastResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeSpec(
            self,
            request: models.DescribeNodeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeSpecResponse:
        """
        This API is used to query node specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceSchedule(
            self,
            request: models.DescribeResourceScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceScheduleResponse:
        """
        This API is used to query YARN resource scheduling information. It has been deprecated. You can use the DescribeYarnQueue API to query queue information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceScheduleDiffDetail(
            self,
            request: models.DescribeResourceScheduleDiffDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceScheduleDiffDetailResponse:
        """
        This API is used to query change details in YARN resource scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceScheduleDiffDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceScheduleDiffDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSLInstance(
            self,
            request: models.DescribeSLInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeSLInstanceResponse:
        """
        This API is used to query the basic information of Serverless HBase instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSLInstanceList(
            self,
            request: models.DescribeSLInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSLInstanceListResponse:
        """
        This API is used to query the detailed information of the Serverless HBase instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSLInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSLInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceConfGroupInfos(
            self,
            request: models.DescribeServiceConfGroupInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceConfGroupInfosResponse:
        """
        This API is used to describe service configuration group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceConfGroupInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceConfGroupInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceNodeInfos(
            self,
            request: models.DescribeServiceNodeInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceNodeInfosResponse:
        """
        This API is used to query service process information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceNodeInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceNodeInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkApplications(
            self,
            request: models.DescribeSparkApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkApplicationsResponse:
        """
        This API is used to obtain a Spark application list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkQueries(
            self,
            request: models.DescribeSparkQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkQueriesResponse:
        """
        This API is used to query the Spark query information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStarRocksQueryInfo(
            self,
            request: models.DescribeStarRocksQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeStarRocksQueryInfoResponse:
        """
        This API is used to query StarRocks information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStarRocksQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStarRocksQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrinoQueryInfo(
            self,
            request: models.DescribeTrinoQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTrinoQueryInfoResponse:
        """
        This API is used to query Trino(PrestoSQL) query information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrinoQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrinoQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsersForUserManager(
            self,
            request: models.DescribeUsersForUserManagerRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersForUserManagerResponse:
        """
        This API is available for clusters with OpenLDAP components configured.
        This API is used to export users in batches. For a Kerberos cluster, set `NeedKeytabInfo` to `true` to obtain the download link of the Keytab file. If `SupportDownLoadKeyTab` is `true`, but `DownLoadKeyTabUrl` is null, the Keytab file is not ready yet (being generated) in the backend.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsersForUserManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersForUserManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeYarnQueue(
            self,
            request: models.DescribeYarnQueueRequest,
            opts: Dict = None,
    ) -> models.DescribeYarnQueueResponse:
        """
        This API is used to obtain queue information in resource scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeYarnQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeYarnQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeYarnScheduleHistory(
            self,
            request: models.DescribeYarnScheduleHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeYarnScheduleHistoryResponse:
        """
        This API is used to view the YARN resource scheduling history. It has been deprecated. You can use the Process Center to view the history records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeYarnScheduleHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeYarnScheduleHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateInstance(
            self,
            request: models.InquiryPriceCreateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateInstanceResponse:
        """
        This API is used to query price of instance creation.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewInstance(
            self,
            request: models.InquiryPriceRenewInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewInstanceResponse:
        """
        This API is used to query the price for renewal.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceScaleOutInstance(
            self,
            request: models.InquiryPriceScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceScaleOutInstanceResponse:
        """
        This API is used to query price of scale-out.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpdateInstance(
            self,
            request: models.InquiryPriceUpdateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpdateInstanceResponse:
        """
        This API is used to query price of scaling.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpdateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpdateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        This API is used to introduce the prerequisite prepaid clusters.
        This API is used to enable or disable automatic renewal at the resource level.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScaleStrategy(
            self,
            request: models.ModifyAutoScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScaleStrategyResponse:
        """
        This API is used to modify automatic scaling rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalConfig(
            self,
            request: models.ModifyGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalConfigResponse:
        """
        This API is used to modify the global configuration of YARN Resource Scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInspectionSettings(
            self,
            request: models.ModifyInspectionSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyInspectionSettingsResponse:
        """
        This API is used to set inspection task configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInspectionSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInspectionSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceBasic(
            self,
            request: models.ModifyInstanceBasicRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceBasicResponse:
        """
        This API is used to modify a cluster name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceBasic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceBasicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResource(
            self,
            request: models.ModifyResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceResponse:
        """
        This API is used to resize an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceScheduleConfig(
            self,
            request: models.ModifyResourceScheduleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceScheduleConfigResponse:
        """
        This API is deprecated. Use ModifyYarnQueueV2 to modify queue configuration. No related logs exist in the past one year.

        This API is used to modify the resource configuration of YARN Resource Scheduling. It has been deprecated. Use the ModifyYarnQueueV2 API to modify the queue configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceScheduleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceScheduleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceScheduler(
            self,
            request: models.ModifyResourceSchedulerRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceSchedulerResponse:
        """
        This API is used to modify a YARN resource scheduler. After the modification, you can click Deploy to bring it into effect.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceScheduler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceSchedulerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcesTags(
            self,
            request: models.ModifyResourcesTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcesTagsResponse:
        """
        This API is used to forcibly modify tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcesTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcesTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySLInstance(
            self,
            request: models.ModifySLInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifySLInstanceResponse:
        """
        This API is used to resize a Serverless HBase instance.- If the API call is successful, a Serverless HBase instance will be created. If the instance creation request is successful, the RequestID of the request will be returned.- This is an asynchronous API. The operation is not completed immediately when the API call returns. The instance operation result can be viewed by calling DescribeInstancesList to view the StatusDesc status of the current instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySLInstanceBasic(
            self,
            request: models.ModifySLInstanceBasicRequest,
            opts: Dict = None,
    ) -> models.ModifySLInstanceBasicResponse:
        """
        This API is used to modify the Serverless HBase instance name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySLInstanceBasic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySLInstanceBasicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserGroup(
            self,
            request: models.ModifyUserGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserGroupResponse:
        """
        This API is used to modify user groups under User Management.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserManagerPwd(
            self,
            request: models.ModifyUserManagerPwdRequest,
            opts: Dict = None,
    ) -> models.ModifyUserManagerPwdResponse:
        """
        This API is used to change user password (user management).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserManagerPwd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserManagerPwdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsersOfGroupSTD(
            self,
            request: models.ModifyUsersOfGroupSTDRequest,
            opts: Dict = None,
    ) -> models.ModifyUsersOfGroupSTDResponse:
        """
        This API is used to change the user information of user groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsersOfGroupSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsersOfGroupSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyYarnDeploy(
            self,
            request: models.ModifyYarnDeployRequest,
            opts: Dict = None,
    ) -> models.ModifyYarnDeployResponse:
        """
        This API is deprecated. Use DeployYarnConf to bring configurations into effect after deployment.

        This API is used to bring configurations into effect after deployment. It has been deprecated. Use the DeployYarnConf API to bring configurations into effect after deployment.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyYarnDeploy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyYarnDeployResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyYarnQueueV2(
            self,
            request: models.ModifyYarnQueueV2Request,
            opts: Dict = None,
    ) -> models.ModifyYarnQueueV2Response:
        """
        This API is used to modify queue information in resource scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyYarnQueueV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyYarnQueueV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetYarnConfig(
            self,
            request: models.ResetYarnConfigRequest,
            opts: Dict = None,
    ) -> models.ResetYarnConfigResponse:
        """
        This API is used to modify the resource configuration of YARN resource scheduling.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetYarnConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetYarnConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDataDisks(
            self,
            request: models.ResizeDataDisksRequest,
            opts: Dict = None,
    ) -> models.ResizeDataDisksResponse:
        """
        This API is used to scale out the cloud data disk.
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDataDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDataDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutCluster(
            self,
            request: models.ScaleOutClusterRequest,
            opts: Dict = None,
    ) -> models.ScaleOutClusterResponse:
        """
        This API is used to scale out a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        This API is used to scale out instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNodeResourceConfigDefault(
            self,
            request: models.SetNodeResourceConfigDefaultRequest,
            opts: Dict = None,
    ) -> models.SetNodeResourceConfigDefaultResponse:
        """
        This API is used to set specifications for a node in the current cluster to default or not.
        """
        
        kwargs = {}
        kwargs["action"] = "SetNodeResourceConfigDefault"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNodeResourceConfigDefaultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStopServiceOrMonitor(
            self,
            request: models.StartStopServiceOrMonitorRequest,
            opts: Dict = None,
    ) -> models.StartStopServiceOrMonitorResponse:
        """
        This API is used to start, stop, or restart services.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStopServiceOrMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStopServiceOrMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateClusterNodes(
            self,
            request: models.TerminateClusterNodesRequest,
            opts: Dict = None,
    ) -> models.TerminateClusterNodesResponse:
        """
        This API is used to terminate cluster nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstance(
            self,
            request: models.TerminateInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateInstanceResponse:
        """
        This API is used to terminate EMR instances. It is only supported in the official paid edition of EMR.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateSLInstance(
            self,
            request: models.TerminateSLInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateSLInstanceResponse:
        """
        This API is used to terminate a Serverless HBase instance.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateTasks(
            self,
            request: models.TerminateTasksRequest,
            opts: Dict = None,
    ) -> models.TerminateTasksResponse:
        """
        This API is used to terminate a task node.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)