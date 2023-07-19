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
from tencentcloud.mariadb.v20170312 import models


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.tencentcloudapi.com'
    _service = 'mariadb'


    def AssociateSecurityGroups(self, request):
        """This API is used to associate security groups with Tencent Cloud resources in batches.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.AssociateSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CancelDcnJobResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessResponse`

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
        Note: accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute.

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountResponse`

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


    def CreateDBInstance(self, request):
        """This API is used to create a monthly subscribed TencentDB for MariaDB instance by passing in information such as instance specifications, database version number, validity period, and quantity.

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHourDBInstance(self, request):
        """This API is used to create a pay-as-you-go TencentDB for MariaDB instance.

        :param request: Request instance for CreateHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHourDBInstanceResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountResponse`

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
        Note: Accounts with the same username but different hosts are different accounts.

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupFilesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBEncryptAttributesResponse`

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


    def DescribeDBInstanceDetail(self, request):
        """This API is used to query the details of a specified instance.

        :param request: Request instance for DescribeDBInstanceDetail.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceDetailRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """This API is used to query the TencentDB instance list. It supports filtering instances by project ID, instance ID, private address, and instance name.
        If no filter is specified, 20 instances will be returned by default. Up to 100 instances can be returned for a single request.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersResponse`

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
        """This API is used to query the security group details of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsResponse`

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


    def DescribeDatabaseObjects(self, request):
        """This API is used to query the list of database objects in a TencentDB instance, including tables, stored procedures, views, and functions.

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseObjectsResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseTableResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDcnDetailResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeFileDownloadUrlResponse`

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


    def DescribeInstanceNodeInfo(self, request):
        """This API is used to query the information of primary and replica nodes of an instance.

        :param request: Request instance for DescribeInstanceNodeInfo.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodeInfoResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodResponse`

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
        """This API is used to query TencentDB order information. You can pass in an order ID to query the TencentDB instance associated with the order and the corresponding task process ID.

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersResponse`

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


    def DescribePrice(self, request):
        """This API is used to query the instance price before you purchase it.

        :param request: Request instance for DescribePrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePriceResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeProjectSecurityGroupsResponse`

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


    def DestroyDBInstance(self, request):
        """This API is used to terminate an isolated monthly subscribed instance.

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DestroyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyHourDBInstance(self, request):
        """This API is used to terminate a pay-as-you-go TencentDB for MariaDB instance.

        :param request: Request instance for DestroyHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DestroyHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DestroyHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyHourDBInstanceResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DisassociateSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesResponse`

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


    def IsolateDBInstance(self, request):
        """This API is used to isolate a monthly subscribed TencentDB for MariaDB instance, which will no longer be accessible via IP and port.  The isolated instance can be started up in the recycle bin.  If it is isolated due to overdue payments, top up your account as soon as possible.

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstanceResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.IsolateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.IsolateDedicatedDBInstanceResponse`

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


    def KillSession(self, request):
        """This API is used to kill the specified session.

        :param request: Request instance for KillSession.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.KillSessionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.KillSessionResponse`

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


    def ModifyAccountDescription(self, request):
        """This API is used to modify the remarks of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionResponse`

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
        """This API is used to modify the permissions of a TencentDB instance account. \n\n**Note**\n-Only the SELECT permission (that is, set the permission parameter to `["SELECT"]`) of the system database `mysql` can be granted.An error will be reported if read-write permissions are granted to a read-only account. If the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted view permissions, set `Privileges` to an empty array.

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBEncryptAttributesResponse`

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


    def ModifyDBInstancesProject(self, request):
        """This API is used to modify the project to which TencentDB instances belong.

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBSyncModeResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceNetworkResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVipRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVipResponse`

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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVportRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVportResponse`

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


    def ModifySyncTaskAttribute(self, request):
        """This API is used to modify sync task attributes (currently, only the task name can be modified).

        :param request: Request instance for ModifySyncTaskAttribute.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifySyncTaskAttributeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifySyncTaskAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySyncTaskAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySyncTaskAttributeResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordResponse`

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


    def TerminateDedicatedDBInstance(self, request):
        """This API is used to terminate the isolated dedicated TencentDB instance.

        :param request: Request instance for TerminateDedicatedDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.TerminateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.TerminateDedicatedDBInstanceResponse`

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


    def UpgradeDedicatedDBInstance(self, request):
        """This API is used to expand the dedicated TencentDB instance.

        :param request: Request instance for UpgradeDedicatedDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))