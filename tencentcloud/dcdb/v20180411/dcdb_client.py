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
from tencentcloud.dcdb.v20180411 import models


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'
    _service = 'dcdb'


    def ActiveHourDCDBInstance(self, request):
        """This API is used to remove the isolation of pay-as-you-go TDSQL for MySQL instances.

        :param request: Request instance for ActiveHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ActiveHourDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActiveHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateSecurityGroups(self, request):
        """This API is used to associate security groups with Tencent Cloud resources in batches.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelDcnJob(self, request):
        """This API is used to cancel DCN synchronization.

        :param request: Request instance for CancelDcnJob.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelDcnJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelDcnJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloneAccount(self, request):
        """This API is used to clone an instance account.

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseDBExtranetAccess(self, request):
        """This API is used to disable public network access for a TencentDB instance, which will make the public IP address inaccessible. The `DescribeDCDBInstances` API will not return the public domain name and port information of the corresponding instance.

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CopyAccountPrivileges(self, request):
        """This API is used to copy the permissions of a TencentDB account.
        Note: Accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute.

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccount(self, request):
        """This API is used to create a TencentDB account. Multiple accounts can be created for one instance. Accounts with the same username but different hosts are different accounts.

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHourDCDBInstance(self, request):
        """This API is used to create pay-as-you-go TDSQL for MySQL instances.

        :param request: Request instance for CreateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHourDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccount(self, request):
        """This API is used to delete a TencentDB account, which is uniquely identified by username and host.

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountPrivileges(self, request):
        """This API is used to query the permissions of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """This API is used to query the list of accounts of a specified TencentDB instance.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBLogFiles(self, request):
        """This API is used to get the list of various logs of a database, including cold backups, binlogs, errlogs, and slowlogs.

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBLogFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBLogFilesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBParameters(self, request):
        """This API is used to get the current parameter settings of a database.

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBParametersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group details of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSlowLogs(self, request):
        """This API is used to query the list of slow query logs.

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSyncMode(self, request):
        """This API is used to query the sync mode of a TencentDB instance.

        :param request: Request instance for DescribeDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSyncModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBInstanceNodeInfo(self, request):
        """This API is used to query the information of instance nodes.

        :param request: Request instance for DescribeDCDBInstanceNodeInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBInstanceNodeInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstanceNodeInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBInstances(self, request):
        """This API is used to query the list of TencentDB instances. It supports filtering instances by project ID, instance ID, private network address, and instance name.
        If no filter is specified, 10 instances will be returned by default. Up to 100 instances can be returned for a single request.

        :param request: Request instance for DescribeDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDCDBShards(self, request):
        """This API is used to query the information of shards of a TencentDB instance.

        :param request: Request instance for DescribeDCDBShards.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBShardsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseObjects(self, request):
        """This API is used to query the list of database objects in a TencentDB instance, including tables, stored procedures, views, and functions.

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseObjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseObjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseTable(self, request):
        """This API is used to query the table information of a TencentDB instance.

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabases(self, request):
        """This API is used to query the list of databases of a TencentDB instance.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDcnDetail(self, request):
        """This API is used to query the disaster recovery details of an instance.

        :param request: Request instance for DescribeDcnDetail.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDcnDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDcnDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileDownloadUrl(self, request):
        """This API is used to get the download URL of a specific backup or log file of a database.

        :param request: Request instance for DescribeFileDownloadUrl.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileDownloadUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileDownloadUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlow(self, request):
        """This API is used to query task status.

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query the security group details of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjects(self, request):
        """This API is used to query the project list.

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyDCDBInstance(self, request):
        """This API is used to terminate an isolated monthly-subscribed instance.

        :param request: Request instance for DestroyDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyHourDCDBInstance(self, request):
        """This API is used to terminate a pay-as-you-go instance.

        :param request: Request instance for DestroyHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyHourDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateSecurityGroups(self, request):
        """This API is used to unassociate security groups from instances in batches.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GrantAccountPrivileges(self, request):
        """This API is used to grant permissions to a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitDCDBInstances(self, request):
        """This API is used to initialize instances, including setting the default character set and table name case sensitivity.

        :param request: Request instance for InitDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDCDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateHourDCDBInstance(self, request):
        """This API is used to isolate pay-as-you-go TDSQL for MySQL instances.

        :param request: Request instance for IsolateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateHourDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateHourDCDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountDescription(self, request):
        """This API is used to modify the remarks of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the security groups associated with TencentDB.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstancesProject(self, request):
        """This API is used to modify the project to which TencentDB instances belong.

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBParameters(self, request):
        """This API is used to modify database parameters.

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBParametersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBSyncMode(self, request):
        """This API is used to modify the sync mode of a TencentDB instance.

        :param request: Request instance for ModifyDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBSyncModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenDBExtranetAccess(self, request):
        """This API is used to enable public network access for a TencentDB instance. After that, you can access the instance with the public domain name and port obtained through the `DescribeDCDBInstances` API.

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAccountPassword(self, request):
        """This API is used to reset the password of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchDBInstanceHA(self, request):
        """This API is used to start a source-replica switch of instances.

        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHARequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHAResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchDBInstanceHA", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchDBInstanceHAResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)