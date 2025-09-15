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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.intl.tencentcloudapi.com'
    _service = 'emr'


    def AddMetricScaleStrategy(self, request):
        r"""This API is used to add scaling rules by load and time.

        :param request: Request instance for AddMetricScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddMetricScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddMetricScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMetricScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.AddMetricScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNodeResourceConfig(self, request):
        r"""This API is used to add node specifications of the current cluster.

        :param request: Request instance for AddNodeResourceConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddNodeResourceConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddNodeResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodeResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.AddNodeResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUsersForUserManager(self, request):
        r"""This API is available for clusters with OpenLDAP components configured.
        This API is used to add user lists (user management).

        :param request: Request instance for AddUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        r"""This API is used to mount cloud disks.

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConvertPreToPostCluster(self, request):
        r"""This API is used to convert a monthly subscription cluster to a pay-as-you-go cluster (excluding cdb).

        :param request: Request instance for ConvertPreToPostCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.ConvertPreToPostClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ConvertPreToPostClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConvertPreToPostCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ConvertPreToPostClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        r"""This API is used to create an EMR cluster instance.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroupsSTD(self, request):
        r"""This API is used to create user groups in batches under User Management.

        :param request: Request instance for CreateGroupsSTD.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateGroupsSTDRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateGroupsSTDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroupsSTD", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupsSTDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        r"""This API is used to create an EMR cluster instance.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSLInstance(self, request):
        r"""This API is used to create a Serverless HBase instance.- If the API call is successful, a Serverless HBase instance will be created. If the instance creation request is successful, the InstanceId of the created instance and the RequestID of the request will be returned.- This is an asynchronous API. The operation is not completed immediately when the API call returns. The instance operation result can be viewed by calling DescribeInstancesList to view the StatusDesc status of the current instance.

        :param request: Request instance for CreateSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoScaleStrategy(self, request):
        r"""This API is used to delete automatic scaling rules. Nodes scaled based on these rules are destroyed in the background.

        :param request: Request instance for DeleteAutoScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteAutoScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteAutoScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroupsSTD(self, request):
        r"""This API is used to delete user groups in batches.

        :param request: Request instance for DeleteGroupsSTD.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteGroupsSTDRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteGroupsSTDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroupsSTD", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupsSTDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNodeResourceConfig(self, request):
        r"""This API is used to delete the node specifications of the current cluster.

        :param request: Request instance for DeleteNodeResourceConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteNodeResourceConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteNodeResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodeResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNodeResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployYarnConf(self, request):
        r"""This API is used to bring the configuration into effect in YARN resource scheduling after deployment.

        :param request: Request instance for DeployYarnConf.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeployYarnConfRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeployYarnConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployYarnConf", params, headers=headers)
            response = json.loads(body)
            model = models.DeployYarnConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleGroupGlobalConf(self, request):
        r"""This API is used to access the global configuration of automatic scaling.

        :param request: Request instance for DescribeAutoScaleGroupGlobalConf.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleGroupGlobalConfRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleGroupGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleGroupGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleGroupGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleRecords(self, request):
        r"""This API is used to inquiry detailed records of cluster autoscaling.

        :param request: Request instance for DescribeAutoScaleRecords.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleStrategies(self, request):
        r"""This API is used to access automatic scaling rules.

        :param request: Request instance for DescribeAutoScaleStrategies.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleStrategiesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterFlowStatusDetail(self, request):
        r"""This API is used to query the EMR task running details status.

        :param request: Request instance for DescribeClusterFlowStatusDetail.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterFlowStatusDetailRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterFlowStatusDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterFlowStatusDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterFlowStatusDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodes(self, request):
        r"""This API is used to query the information of nodes in a cluster.

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDAGInfo(self, request):
        r"""This API is used to query DAG information.

        :param request: Request instance for DescribeDAGInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeDAGInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeDAGInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDAGInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDAGInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrApplicationStatics(self, request):
        r"""This API is used to query the YARN application statistics API.

        :param request: Request instance for DescribeEmrApplicationStatics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrApplicationStatics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrApplicationStaticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrOverviewMetrics(self, request):
        r"""This API is used to query the metric data on the monitoring overview page.

        :param request: Request instance for DescribeEmrOverviewMetrics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrOverviewMetricsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrOverviewMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrOverviewMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrOverviewMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalConfig(self, request):
        r"""This API is used to query the global configurations of YARN Resource Scheduling.

        :param request: Request instance for DescribeGlobalConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeGlobalConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupsSTD(self, request):
        r"""This API is used to query a user group.

        :param request: Request instance for DescribeGroupsSTD.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeGroupsSTDRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeGroupsSTDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupsSTD", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupsSTDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHBaseTableOverview(self, request):
        r"""This API is used to access the overview of HBase table-level monitoring data.

        :param request: Request instance for DescribeHBaseTableOverview.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHBaseTableOverviewRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHBaseTableOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHBaseTableOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHBaseTableOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHDFSStorageInfo(self, request):
        r"""This API is used to query information of file(s) stored in HDFS.

        :param request: Request instance for DescribeHDFSStorageInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHDFSStorageInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHDFSStorageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHDFSStorageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHDFSStorageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHiveQueries(self, request):
        r"""This API is used to inquiry Hive query data.

        :param request: Request instance for DescribeHiveQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHiveQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHiveQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInsightList(self, request):
        r"""This API is used to obtain insight result information.

        :param request: Request instance for DescribeInsightList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInsightListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInsightListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInsightList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInsightListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInspectionTaskResult(self, request):
        r"""This API is used to obtain the inspection task result list.

        :param request: Request instance for DescribeInspectionTaskResult.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInspectionTaskResultRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInspectionTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInspectionTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInspectionTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""This API is used to query the information of instances in a cluster.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesList(self, request):
        r"""This API is used to query the cluster list.

        :param request: Request instance for DescribeInstancesList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKyuubiQueryInfo(self, request):
        r"""This API is used to query Kyuubi query information.

        :param request: Request instance for DescribeKyuubiQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeKyuubiQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeKyuubiQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKyuubiQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKyuubiQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeDataDisks(self, request):
        r"""This API is used to query data disk information of nodes.

        :param request: Request instance for DescribeNodeDataDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeNodeDataDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeNodeDataDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeDataDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeDataDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeResourceConfigFast(self, request):
        r"""This API is used to quickly obtain node specifications of the current cluster.

        :param request: Request instance for DescribeNodeResourceConfigFast.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeNodeResourceConfigFastRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeNodeResourceConfigFastResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeResourceConfigFast", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeResourceConfigFastResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeSpec(self, request):
        r"""This API is used to query node specifications.

        :param request: Request instance for DescribeNodeSpec.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeNodeSpecRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeNodeSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceSchedule(self, request):
        r"""This API is used to query YARN resource scheduling information. It has been deprecated. You can use the DescribeYarnQueue API to query queue information.

        :param request: Request instance for DescribeResourceSchedule.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceScheduleDiffDetail(self, request):
        r"""This API is used to query change details in YARN resource scheduling.

        :param request: Request instance for DescribeResourceScheduleDiffDetail.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleDiffDetailRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleDiffDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceScheduleDiffDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleDiffDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSLInstance(self, request):
        r"""This API is used to query the basic information of Serverless HBase instances.

        :param request: Request instance for DescribeSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSLInstanceList(self, request):
        r"""This API is used to query the detailed information of the Serverless HBase instance list.

        :param request: Request instance for DescribeSLInstanceList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSLInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSLInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSLInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceConfGroupInfos(self, request):
        r"""This API is used to describe service configuration group information.

        :param request: Request instance for DescribeServiceConfGroupInfos.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeServiceConfGroupInfosRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeServiceConfGroupInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceConfGroupInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceConfGroupInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceNodeInfos(self, request):
        r"""This API is used to query service process information.

        :param request: Request instance for DescribeServiceNodeInfos.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeServiceNodeInfosRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeServiceNodeInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceNodeInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceNodeInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkApplications(self, request):
        r"""This API is used to obtain a Spark application list.

        :param request: Request instance for DescribeSparkApplications.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSparkApplicationsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSparkApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkQueries(self, request):
        r"""This API is used to query the Spark query information list.

        :param request: Request instance for DescribeSparkQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeSparkQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeSparkQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStarRocksQueryInfo(self, request):
        r"""This API is used to query StarRocks information.

        :param request: Request instance for DescribeStarRocksQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeStarRocksQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeStarRocksQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStarRocksQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStarRocksQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrinoQueryInfo(self, request):
        r"""This API is used to query Trino(PrestoSQL) query information.

        :param request: Request instance for DescribeTrinoQueryInfo.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeTrinoQueryInfoRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeTrinoQueryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrinoQueryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrinoQueryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersForUserManager(self, request):
        r"""This API is available for clusters with OpenLDAP components configured.
        This API is used to export users in batches. For a Kerberos cluster, set `NeedKeytabInfo` to `true` to obtain the download link of the Keytab file. If `SupportDownLoadKeyTab` is `true`, but `DownLoadKeyTabUrl` is null, the Keytab file is not ready yet (being generated) in the backend.

        :param request: Request instance for DescribeUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnQueue(self, request):
        r"""This API is used to obtain queue information in resource scheduling.

        :param request: Request instance for DescribeYarnQueue.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnQueueRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnScheduleHistory(self, request):
        r"""This API is used to view the YARN resource scheduling history. It has been deprecated. You can use the Process Center to view the history records.

        :param request: Request instance for DescribeYarnScheduleHistory.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnScheduleHistoryRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnScheduleHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnScheduleHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnScheduleHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateInstance(self, request):
        r"""This API is used to query price of instance creation.

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewInstance(self, request):
        r"""This API is used to query the price for renewal.

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceScaleOutInstance(self, request):
        r"""This API is used to query price of scale-out.

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpdateInstance(self, request):
        r"""This API is used to query price of scaling.

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoRenewFlag(self, request):
        r"""This API is used to introduce the prerequisite prepaid clusters.
        This API is used to enable or disable automatic renewal at the resource level.

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoScaleStrategy(self, request):
        r"""This API is used to modify automatic scaling rules.

        :param request: Request instance for ModifyAutoScaleStrategy.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyAutoScaleStrategyRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyAutoScaleStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoScaleStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoScaleStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalConfig(self, request):
        r"""This API is used to modify the global configuration of YARN Resource Scheduling.

        :param request: Request instance for ModifyGlobalConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyGlobalConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInspectionSettings(self, request):
        r"""This API is used to set inspection task configurations.

        :param request: Request instance for ModifyInspectionSettings.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyInspectionSettingsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyInspectionSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInspectionSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInspectionSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceBasic(self, request):
        r"""This API is used to modify a cluster name.

        :param request: Request instance for ModifyInstanceBasic.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyInstanceBasicRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyInstanceBasicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceBasic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceBasicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResource(self, request):
        r"""This API is used to resize an instance.

        :param request: Request instance for ModifyResource.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduleConfig(self, request):
        r"""This API is deprecated. Use ModifyYarnQueueV2 to modify queue configuration. No related logs exist in the past one year.

        This API is used to modify the resource configuration of YARN Resource Scheduling. It has been deprecated. Use the ModifyYarnQueueV2 API to modify the queue configuration.

        :param request: Request instance for ModifyResourceScheduleConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceScheduleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduler(self, request):
        r"""This API is used to modify a YARN resource scheduler. After the modification, you can click Deploy to bring it into effect.

        :param request: Request instance for ModifyResourceScheduler.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduler", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceSchedulerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcesTags(self, request):
        r"""This API is used to forcibly modify tags.

        :param request: Request instance for ModifyResourcesTags.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcesTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcesTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySLInstance(self, request):
        r"""This API is used to resize a Serverless HBase instance.- If the API call is successful, a Serverless HBase instance will be created. If the instance creation request is successful, the RequestID of the request will be returned.- This is an asynchronous API. The operation is not completed immediately when the API call returns. The instance operation result can be viewed by calling DescribeInstancesList to view the StatusDesc status of the current instance.

        :param request: Request instance for ModifySLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySLInstanceBasic(self, request):
        r"""This API is used to modify the Serverless HBase instance name.

        :param request: Request instance for ModifySLInstanceBasic.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceBasicRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifySLInstanceBasicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySLInstanceBasic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySLInstanceBasicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserGroup(self, request):
        r"""This API is used to modify user groups under User Management.

        :param request: Request instance for ModifyUserGroup.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUserGroupRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserManagerPwd(self, request):
        r"""This API is used to change user password (user management).

        :param request: Request instance for ModifyUserManagerPwd.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserManagerPwd", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserManagerPwdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUsersOfGroupSTD(self, request):
        r"""This API is used to change the user information of user groups.

        :param request: Request instance for ModifyUsersOfGroupSTD.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUsersOfGroupSTDRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUsersOfGroupSTDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUsersOfGroupSTD", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUsersOfGroupSTDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyYarnDeploy(self, request):
        r"""This API is deprecated. Use DeployYarnConf to bring configurations into effect after deployment.

        This API is used to bring configurations into effect after deployment. It has been deprecated. Use the DeployYarnConf API to bring configurations into effect after deployment.

        :param request: Request instance for ModifyYarnDeploy.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyYarnDeployRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyYarnDeployResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyYarnDeploy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyYarnDeployResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyYarnQueueV2(self, request):
        r"""This API is used to modify queue information in resource scheduling.

        :param request: Request instance for ModifyYarnQueueV2.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyYarnQueueV2Request`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyYarnQueueV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyYarnQueueV2", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyYarnQueueV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetYarnConfig(self, request):
        r"""This API is used to modify the resource configuration of YARN resource scheduling.

        :param request: Request instance for ResetYarnConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ResetYarnConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ResetYarnConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetYarnConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ResetYarnConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDataDisks(self, request):
        r"""This API is used to scale out the cloud data disk.

        :param request: Request instance for ResizeDataDisks.
        :type request: :class:`tencentcloud.emr.v20190103.models.ResizeDataDisksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ResizeDataDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDataDisks", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDataDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutCluster(self, request):
        r"""This API is used to scale out a cluster.

        :param request: Request instance for ScaleOutCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        r"""This API is used to scale out instances.

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNodeResourceConfigDefault(self, request):
        r"""This API is used to set specifications for a node in the current cluster to default or not.

        :param request: Request instance for SetNodeResourceConfigDefault.
        :type request: :class:`tencentcloud.emr.v20190103.models.SetNodeResourceConfigDefaultRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.SetNodeResourceConfigDefaultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNodeResourceConfigDefault", params, headers=headers)
            response = json.loads(body)
            model = models.SetNodeResourceConfigDefaultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStopServiceOrMonitor(self, request):
        r"""This API is used to start, stop, or restart services.

        :param request: Request instance for StartStopServiceOrMonitor.
        :type request: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStopServiceOrMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StartStopServiceOrMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateClusterNodes(self, request):
        r"""This API is used to terminate cluster nodes.

        :param request: Request instance for TerminateClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstance(self, request):
        r"""This API is used to terminate EMR instances. It is only supported in the official paid edition of EMR.

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateSLInstance(self, request):
        r"""This API is used to terminate a Serverless HBase instance.

        :param request: Request instance for TerminateSLInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateSLInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateSLInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateSLInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateSLInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTasks(self, request):
        r"""This API is used to terminate a task node.

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))