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
from tencentcloud.cdwdoris.v20211228 import models


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.intl.tencentcloudapi.com'
    _service = 'cdwdoris'


    def ActionAlterUser(self, request):
        """This API is used to add and modify a user.

        :param request: Request instance for ActionAlterUser.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ActionAlterUserRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ActionAlterUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActionAlterUser", params, headers=headers)
            response = json.loads(body)
            model = models.ActionAlterUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelBackupJob(self, request):
        """This API is used to cancel the corresponding backup instance task.

        :param request: Request instance for CancelBackupJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CancelBackupJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CancelBackupJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelBackupJob", params, headers=headers)
            response = json.loads(body)
            model = models.CancelBackupJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCoolDownWorkingVariableConfigCorrect(self, request):
        """This API is used to check whether variables and configurations for hot/cold data layering are correct.

        :param request: Request instance for CheckCoolDownWorkingVariableConfigCorrect.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CheckCoolDownWorkingVariableConfigCorrectRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CheckCoolDownWorkingVariableConfigCorrectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCoolDownWorkingVariableConfigCorrect", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCoolDownWorkingVariableConfigCorrectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyTableDatas(self, request):
        """This API is used to copy the source table to the target table.

        :param request: Request instance for CopyTableDatas.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CopyTableDatasRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CopyTableDatasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyTableDatas", params, headers=headers)
            response = json.loads(body)
            model = models.CopyTableDatasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackUpSchedule(self, request):
        """This API is used to create or modify backup policies.

        :param request: Request instance for CreateBackUpSchedule.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateBackUpScheduleRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateBackUpScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackUpSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackUpScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCoolDownPolicy(self, request):
        """This API is used to create a hot/cold data layering policy.

        :param request: Request instance for CreateCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatabase(self, request):
        """This API is used to create a TCHouse-D database.

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceNew(self, request):
        """This API is used to create clusters.

        :param request: Request instance for CreateInstanceNew.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTable(self, request):
        """This API is used to create a TCHouse-D table under the specified database.

        :param request: Request instance for CreateTable.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateTableRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkloadGroup(self, request):
        """This API is used to create resource groups.

        :param request: Request instance for CreateWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackUpData(self, request):
        """This API is used to delete backup data.

        :param request: Request instance for DeleteBackUpData.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteBackUpDataRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteBackUpDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackUpData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackUpDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTable(self, request):
        """This API is used to delete the specified table in the specified database.

        :param request: Request instance for DeleteTable.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteTableRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkloadGroup(self, request):
        """This API is used to delete resource groups.

        :param request: Request instance for DeleteWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaRegion(self, request):
        """This API is used to display region information and the total number of clusters in each region on the cluster list page.

        :param request: Request instance for DescribeAreaRegion.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeAreaRegionRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeAreaRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpJob(self, request):
        """This API is used to query the list of backup instances.

        :param request: Request instance for DescribeBackUpJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpJobDetail(self, request):
        """This API is used to query backup task details.

        :param request: Request instance for DescribeBackUpJobDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpJobDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpJobDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpSchedules(self, request):
        """This API is used to obtain the scheduled task information for the backup and migration.

        :param request: Request instance for DescribeBackUpSchedules.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpSchedulesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpSchedulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpSchedules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpSchedulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpTables(self, request):
        """This API is used to obtain the information of the table available for backup.

        :param request: Request instance for DescribeBackUpTables.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTablesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpTaskDetail(self, request):
        """This API is used to query the progress details of backup tasks.

        :param request: Request instance for DescribeBackUpTaskDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterConfigs(self, request):
        """This API is used to get the contents of the latest configuration files (config.xml, metrika.xml, and user.xml) of the cluster and display them to the user.

        :param request: Request instance for DescribeClusterConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterConfigsHistory(self, request):
        """This API is used to obtain the modification history of cluster configuration files.

        :param request: Request instance for DescribeClusterConfigsHistory.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsHistoryRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigsHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownBackends(self, request):
        """This API is used to query the list of backend nodes supporting hot/cold data layering.

        :param request: Request instance for DescribeCoolDownBackends.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownBackendsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownBackendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownBackends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownBackendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownPolicies(self, request):
        """This API is used to query the list of hot/cold data layering policies.

        :param request: Request instance for DescribeCoolDownPolicies.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownPoliciesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownTableData(self, request):
        """This API is used to query the layered hot and cold data in a table.

        :param request: Request instance for DescribeCoolDownTableData.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownTableDataRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownTableDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownTableData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownTableDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreateTablesDDL(self, request):
        """This API is used to batch obtain the table creation DDL.

        :param request: Request instance for DescribeCreateTablesDDL.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCreateTablesDDLRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCreateTablesDDLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreateTablesDDL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreateTablesDDLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabase(self, request):
        """This API is used to obtain the database information under a specific data source.

        :param request: Request instance for DescribeDatabase.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditDownload(self, request):
        """This API is used to download database audit logs.

        :param request: Request instance for DescribeDatabaseAuditDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditRecords(self, request):
        """This API is used to get database audit records.

        :param request: Request instance for DescribeDatabaseAuditRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """This API is used to query the specific information of a cluster based on the cluster ID.

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        """This API is used to get the list of cluster node information.

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodesInfo(self, request):
        """This API is used to get the BE/FE node roles.

        :param request: Request instance for DescribeInstanceNodesInfo.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodesRole(self, request):
        """This API is used to obtain cluster node roles.

        :param request: Request instance for DescribeInstanceNodesRole.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRoleRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodesRole", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperationHistory(self, request):
        """This API is used to pull the operation list of the cluster. The API supports pagination query and filtering operation records by time range.

        :param request: Request instance for DescribeInstanceOperationHistory.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationHistoryRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperations(self, request):
        """This API is used to pull operations of the cluster on the cluster details page.

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceState(self, request):
        """This API is used to display cluster status, process progress, etc. in the cluster details page.

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceUsedSubnets(self, request):
        """This API is used to obtain the information of subnets used by the cluster.

        :param request: Request instance for DescribeInstanceUsedSubnets.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceUsedSubnetsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceUsedSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceUsedSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceUsedSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to get the list of clusters.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesResponse`

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


    def DescribeInstancesHealthState(self, request):
        """This API is used to check cluster health

        :param request: Request instance for DescribeInstancesHealthState.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesHealthStateRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesHealthStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesHealthState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesHealthStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQueryAnalyse(self, request):
        """This API is used to obtain the SQL query details of the Doris user.

        :param request: Request instance for DescribeQueryAnalyse.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeQueryAnalyseRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeQueryAnalyseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQueryAnalyse", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQueryAnalyseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTaskDetail(self, request):
        """This API is used to query the progress details of the recovery task.

        :param request: Request instance for DescribeRestoreTaskDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeRestoreTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeRestoreTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryRecords(self, request):
        """This API is used to get the slow log list.

        :param request: Request instance for DescribeSlowQueryRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryRecordsDownload(self, request):
        """This API is used to download slow log files.

        :param request: Request instance for DescribeSlowQueryRecordsDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecordsDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpec(self, request):
        """This API is used to pull the specification list of data nodes and zookeeper nodes for the cluster on the purchase page.

        :param request: Request instance for DescribeSpec.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSpecRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSqlApis(self, request):
        """This API is used to query the cluster information by executing SQL commands.

        :param request: Request instance for DescribeSqlApis.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSqlApisRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSqlApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSqlApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTable(self, request):
        """This API is used to obtain the table information. It only supports querying table information in the TCHouse-D internal catalog.

        :param request: Request instance for DescribeTable.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableList(self, request):
        """This API is used to obtain the list of tables under the specified data source and database.

        :param request: Request instance for DescribeTableList.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableListRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserBindWorkloadGroup(self, request):
        """This API is used to obtain the resource information bound to each user in the current cluster.

        :param request: Request instance for DescribeUserBindWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserBindWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserBindWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserBindWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserBindWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserPolicy(self, request):
        """This API is used to obtain detailed information of Doris users, including account information, permission host, and permission configuration.

        :param request: Request instance for DescribeUserPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkloadGroup(self, request):
        """This API is used to obtain resource group information.

        :param request: Request instance for DescribeWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstance(self, request):
        """This API is used to terminate clusters.

        :param request: Request instance for DestroyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteParametrizedQuery(self, request):
        """This API is used to execute an SQL query statement with parameters and return the query results.

        :param request: Request instance for ExecuteParametrizedQuery.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ExecuteParametrizedQueryRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ExecuteParametrizedQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteParametrizedQuery", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteParametrizedQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteSelectQuery(self, request):
        """This API is used to query data according to the specified database and table name, and support field selection and pagination.

        :param request: Request instance for ExecuteSelectQuery.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ExecuteSelectQueryRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ExecuteSelectQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteSelectQuery", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteSelectQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InsertDatasToTable(self, request):
        """This API is used to insert data into TCHouse-D.

        :param request: Request instance for InsertDatasToTable.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.InsertDatasToTableRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.InsertDatasToTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InsertDatasToTable", params, headers=headers)
            response = json.loads(body)
            model = models.InsertDatasToTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterConfigs(self, request):
        """This API is used to modify the XML cluster configuration file on the cluster configuration page.

        :param request: Request instance for ModifyClusterConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCoolDownPolicy(self, request):
        """This API is used to modify the hot/cold data layering policy.

        :param request: Request instance for ModifyCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseTableAccess(self, request):
        """This API is used to GRANT and REVOKE the database and table in the Doris database.

        :param request: Request instance for ModifyDatabaseTableAccess.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyDatabaseTableAccessRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyDatabaseTableAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseTableAccess", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseTableAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """This API is used to modify the cluster's name.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceKeyValConfigs(self, request):
        """This API is used to modify configurations in the KV mode.

        :param request: Request instance for ModifyInstanceKeyValConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceKeyValConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceKeyValConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceKeyValConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceKeyValConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNodeStatus(self, request):
        """This API is used to change the node status.

        :param request: Request instance for ModifyNodeStatus.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyNodeStatusRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyNodeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNodeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroups(self, request):
        """This API is used to edit security groups.

        :param request: Request instance for ModifySecurityGroups.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifySecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifySecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserBindWorkloadGroup(self, request):
        """This API is used to modify the resource group bound to the user.

        :param request: Request instance for ModifyUserBindWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserBindWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserBindWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserBindWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserBindWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserPrivilegesV3(self, request):
        """This API is used to modify user permissions and support three permission setting categories: catalog, all db, and some db tables.

        :param request: Request instance for ModifyUserPrivilegesV3.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserPrivilegesV3Request`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserPrivilegesV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserPrivilegesV3", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserPrivilegesV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkloadGroup(self, request):
        """This API is used to modify the resource group information.

        :param request: Request instance for ModifyWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkloadGroupStatus(self, request):
        """This API is used to enable or disable resource groups.

        :param request: Request instance for ModifyWorkloadGroupStatus.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupStatusRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkloadGroupStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkloadGroupStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenCoolDown(self, request):
        """This API is used to enable hot/cold data layering.

        :param request: Request instance for OpenCoolDown.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenCoolDown", params, headers=headers)
            response = json.loads(body)
            model = models.OpenCoolDownResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenCoolDownPolicy(self, request):
        """This API is used to enable and describe the cold storage policy.

        :param request: Request instance for OpenCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.OpenCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryTableData(self, request):
        """This API is used to query data according to the specified database and table names, and support field selection and pagination.

        :param request: Request instance for QueryTableData.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.QueryTableDataRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.QueryTableDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTableData", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTableDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverBackUpJob(self, request):
        """This API is used to back up and recover.

        :param request: Request instance for RecoverBackUpJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RecoverBackUpJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RecoverBackUpJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverBackUpJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverBackUpJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReduceInstance(self, request):
        """This API is used to scale in clusters.

        :param request: Request instance for ReduceInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ReduceInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ReduceInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReduceInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ReduceInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisk(self, request):
        """This API is used to expand cloud disks.

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartClusterForConfigs(self, request):
        """This API is used to restart the cluster to make the configuration file take effect.

        :param request: Request instance for RestartClusterForConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterForConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterForConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartClusterForNode(self, request):
        """This API is used to indicate the rolling restart of the clusters.

        :param request: Request instance for RestartClusterForNode.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterForNode", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterForNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """This API is used to horizontally scale out nodes.

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceResponse`

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


    def ScaleUpInstance(self, request):
        """This API is used to scale up/down computing resources.

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCoolDown(self, request):
        """This API is used to update the hot/cold data layering information on a cluster.

        :param request: Request instance for UpdateCoolDown.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateCoolDownRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateCoolDownResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCoolDown", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCoolDownResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDatabase(self, request):
        """This API is used to modify the attributes of a specified database, including setting the data volume quota, renaming the database, setting the replica quantity quota, and modifying other attributes of the database.

        :param request: Request instance for UpdateDatabase.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateDatabaseRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTableSchema(self, request):
        """This API is used to modify the attributes of a specified table. The API parameters are consistent with those for creating a table.

        :param request: Request instance for UpdateTableSchema.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateTableSchemaRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateTableSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTableSchema", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTableSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))