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
        """This API is used to remove a pay-as-you-go TDSQL instance from isolation.

        :param request: Request instance for ActiveHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActiveHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ActiveHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """This API is used to associate security groups with Tencent Cloud resources in batches.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelDcnJob(self, request):
        """This API is used to cancel DCN synchronization.

        :param request: Request instance for CancelDcnJob.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDcnJob", params, headers=headers)
            response = json.loads(body)
            model = models.CancelDcnJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneAccount(self, request):
        """This API is used to clone an instance account.

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CloneAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseDBExtranetAccess(self, request):
        """This API is used to disable public network access for a TencentDB instance, which will make the public IP address inaccessible. The `DescribeDCDBInstances` API will not return the public domain name and port information of the corresponding instance.

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CloseDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyAccountPrivileges(self, request):
        """This API is used to copy the permissions of a TencentDB account.
        Note: Accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute.

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """This API is used to create a TencentDB account. Multiple accounts can be created for one instance. Accounts with the same username but different hosts are different accounts.

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDCDBInstance(self, request):
        """This API is used to create a monthly subscribed TDSQL instance by passing in information such as instance specifications, database version number, and purchased duration.

        :param request: Request instance for CreateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterDCDBInstance(self, request):
        """This API is used to create a dedicated TDSQL cluster instance.

        :param request: Request instance for CreateDedicatedClusterDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDedicatedClusterDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDedicatedClusterDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHourDCDBInstance(self, request):
        """This API is used to create a pay-as-you-go TDSQL instance.

        :param request: Request instance for CreateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """This API is used to delete a TencentDB account, which is uniquely identified by username and host.

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """This API is used to query the permissions of a TencentDB account.
        Note: Accounts with the same username but different hosts are considered as different accounts.

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """This API is used to query the list of accounts of a specified TencentDB instance.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupFiles(self, request):
        """This API is used to query the list of backup files.

        :param request: Request instance for DescribeBackupFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeBackupFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBEncryptAttributes(self, request):
        """This API is used to query the encryption status of the instance data.

        :param request: Request instance for DescribeDBEncryptAttributes.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBLogFiles(self, request):
        """This API is used to get the list of various logs of a database, including cold backups, binlogs, errlogs, and slowlogs.

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBLogFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBLogFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBParameters(self, request):
        """This API is used to get the current parameter settings of a database.

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group information of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSlowLogs(self, request):
        """This API is used to query the list of slow query logs.

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSyncMode(self, request):
        """This API is used to query the sync mode of a TencentDB instance.

        :param request: Request instance for DescribeDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSyncMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSyncModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBTmpInstances(self, request):
        """This API is used to obtain a temp rollback instance.

        :param request: Request instance for DescribeDBTmpInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBTmpInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBTmpInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBTmpInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBTmpInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBInstanceDetail(self, request):
        """This API is used to get the details of a TDSQL instance.

        :param request: Request instance for DescribeDCDBInstanceDetail.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBInstanceNodeInfo(self, request):
        """This API is used to query the information of instance nodes.

        :param request: Request instance for DescribeDCDBInstanceNodeInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBInstances(self, request):
        """This API is used to query the list of TencentDB instances. It supports filtering instances by project ID, instance ID, private network address, and instance name.
        If no filter is specified, 10 instances will be returned by default. Up to 100 instances can be returned for a single request.

        :param request: Request instance for DescribeDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBPrice(self, request):
        """This API is used to query the price of an instance before you purchase it.

        :param request: Request instance for DescribeDCDBPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBShards(self, request):
        """This API is used to query the information of shards of a TencentDB instance.

        :param request: Request instance for DescribeDCDBShards.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBShards", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBShardsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseObjects(self, request):
        """This API is used to query the list of database objects in a TencentDB instance, including tables, stored procedures, views, and functions.

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseTable(self, request):
        """This API is used to query the table information of a TencentDB instance.

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """This API is used to query the database list of a TencentDB instance.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDcnDetail(self, request):
        """This API is used to query the disaster recovery details of an instance.

        :param request: Request instance for DescribeDcnDetail.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDcnDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDcnDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileDownloadUrl(self, request):
        """This API is used to get the download URL of a specific backup or log file of a database.

        :param request: Request instance for DescribeFileDownloadUrl.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlow(self, request):
        """This API is used to query task status.

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogFileRetentionPeriod(self, request):
        """This API is used to view the backup log retention days.

        :param request: Request instance for DescribeLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogFileRetentionPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogFileRetentionPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """This API is used to query TDSQL order information. You can pass in an order ID to query the TDSQL instance associated with the order and the corresponding task process ID.

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query the security group details of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyDCDBInstance(self, request):
        """This API is used to terminate an isolated monthly subscribed TDSQL instance.

        :param request: Request instance for DestroyDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyHourDCDBInstance(self, request):
        """This API is used to terminate a pay-as-you-go TDSQL instance.

        :param request: Request instance for DestroyHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API is used to unassociate security groups from instances in batches.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantAccountPrivileges(self, request):
        """This API is used to grant permissions to a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.GrantAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitDCDBInstances(self, request):
        """This API is used to initialize instances, including setting the default character set and table name case sensitivity.

        :param request: Request instance for InitDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDCDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDCDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDCDBInstance(self, request):
        """This API is used to isolate a monthly subscribed TDSQL instance, which will no longer be accessible via IP and port.  The isolated instance can be started up in the recycle bin.  If it is isolated due to overdue payments, top up your account as soon as possible.

        :param request: Request instance for IsolateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDedicatedDBInstance(self, request):
        """This API is used to isolate a dedicated TencentDB instance.

        :param request: Request instance for IsolateDedicatedDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateHourDCDBInstance(self, request):
        """This API is used to isolate a pay-as-you-go TDSQL instance.

        :param request: Request instance for IsolateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillSession(self, request):
        """This API is used to kill the specified session.

        :param request: Request instance for KillSession.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.KillSessionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.KillSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillSession", params, headers=headers)
            response = json.loads(body)
            model = models.KillSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountConfig(self, request):
        """This API is used to modify the configurations of an account, such as `max_user_connections`.

        :param request: Request instance for ModifyAccountConfig.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountConfigRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountDescription(self, request):
        """This API is used to modify the remarks of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """This API is used to modify the permissions of a TencentDB instance account. \n\n**Note**\n-Only the SELECT permission (that is, set the permission parameter to `["SELECT"]`) of the system database `mysql` can be granted. An error will be reported if read-write permissions are granted to a read-only account. If the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted view permissions, set `Privileges` to an empty array.

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBEncryptAttributes(self, request):
        """This API is used to modify the instance data encryption.

        :param request: Request instance for ModifyDBEncryptAttributes.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """This API is used to modify instance name.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the security groups associated with TencentDB.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstancesProject(self, request):
        """This API is used to modify the project to which TencentDB instances belong.

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstancesProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstancesProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBParameters(self, request):
        """This API is used to modify database parameters.

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBSyncMode(self, request):
        """This API is used to modify the sync mode of a TencentDB instance.

        :param request: Request instance for ModifyDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBSyncMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBSyncModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceNetwork(self, request):
        """This API is used to modify instance network.

        :param request: Request instance for ModifyInstanceNetwork.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceVip(self, request):
        """This API is used to modify instance VIP.

        :param request: Request instance for ModifyInstanceVip.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVip", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceVport(self, request):
        """This API is used to modify instance Vport.

        :param request: Request instance for ModifyInstanceVport.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """This API is used to reset the password of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstanceHA(self, request):
        """This API is used to start a source-replica switch of instances.

        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHARequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstanceHA", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstanceHAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDedicatedDBInstance(self, request):
        """This API is used to terminate the isolated dedicated TDSQL instance.

        :param request: Request instance for TerminateDedicatedDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDedicatedDCDBInstance(self, request):
        """This API is used to upgrade a dedicated TDSQL cluster instance.

        :param request: Request instance for UpgradeDedicatedDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDedicatedDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDedicatedDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDedicatedDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDedicatedDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeHourDCDBInstance(self, request):
        """This API is used to upgrade a pay-as-you-go TDSQL instance.

        :param request: Request instance for UpgradeHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))