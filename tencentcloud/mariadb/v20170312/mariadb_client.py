# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.mariadb.v20170312 import models


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.tencentcloudapi.com'
    _service = 'mariadb'


    def CloneAccount(self, request):
        """This API is used to clone an instance account.

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessResponse`

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
        Note: accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute.

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountResponse`

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


    def DeleteAccount(self, request):
        """This API is used to delete a TencentDB account, which is uniquely identified by username and host.

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsResponse`

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


    def DescribeBackupTime(self, request):
        """This API is used to get the backup time of a TencentDB instance. The backend system will perform instance backup regularly according to this configuration.

        :param request: Request instance for DescribeBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupTimeResponse()
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


    def DescribeDBInstances(self, request):
        """This API is used to query the TencentDB instance list. It supports filtering instances by project ID, instance ID, private address, and instance name.
        If no filter is specified, 20 instances will be returned by default. Up to 100 instances can be returned for a single request.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersResponse`

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


    def DescribeDBPerformance(self, request):
        """This API is used to view the current performance data of a database instance.

        :param request: Request instance for DescribeDBPerformance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceResponse()
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


    def DescribeDBPerformanceDetails(self, request):
        """This API is used to view the instance performance data details.

        :param request: Request instance for DescribeDBPerformanceDetails.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformanceDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceDetailsResponse()
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


    def DescribeDBResourceUsage(self, request):
        """This API is used to view the resource usage of a database instance.

        :param request: Request instance for DescribeDBResourceUsage.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageResponse()
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


    def DescribeDBResourceUsageDetails(self, request):
        """This API is used to view the current performance data of a database instance.

        :param request: Request instance for DescribeDBResourceUsageDetails.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsageDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageDetailsResponse()
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
        """This API is used to query the slow query log list.

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsResponse`

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


    def DescribeDatabases(self, request):
        """This API is used to query the list of databases of a TencentDB instance.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesResponse`

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


    def DescribeFlow(self, request):
        """This API is used to query flow status.

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowResponse`

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


    def DescribeLogFileRetentionPeriod(self, request):
        """This API is used to view the configured number of days for retention of database backup logs.

        :param request: Request instance for DescribeLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogFileRetentionPeriodResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesResponse`

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


    def InitDBInstances(self, request):
        """This API is used to initialize TencentDB instances, including setting the default character set and table name case sensitivity.

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionResponse`

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


    def ModifyBackupTime(self, request):
        """This API is used to set the backup time of a TencentDB instance. The backend system will perform instance backup regularly according to this configuration.

        :param request: Request instance for ModifyBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupTimeResponse()
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


    def ModifyDBInstanceName(self, request):
        """This API is used to rename a TencentDB instance.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersResponse`

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


    def ModifyLogFileRetentionPeriod(self, request):
        """This API is used to modify the number of days for retention of database backup logs.

        :param request: Request instance for ModifyLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogFileRetentionPeriodResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordResponse`

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