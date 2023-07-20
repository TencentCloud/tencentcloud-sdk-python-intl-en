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
from tencentcloud.cdb.v20170320 import models


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.tencentcloudapi.com'
    _service = 'cdb'


    def AddTimeWindow(self, request):
        """This API (AddTimeWindow) is used to add a maintenance time window for a TencentDB instance, so as to specify when the instance can automatically perform access switch operations.

        :param request: Request instance for AddTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.AddTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustCdbProxy(self, request):
        """This API is used to adjust the configuration of database proxy.

        :param request: Request instance for AdjustCdbProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustCdbProxy", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustCdbProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustCdbProxyAddress(self, request):
        """This API is used to adjust the database proxy address.

        :param request: Request instance for AdjustCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AnalyzeAuditLogs(self, request):
        """This API is used to aggregate the audit logs filtered by different conditions and aggregate the statistics of the specified data rows.

        :param request: Request instance for AnalyzeAuditLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AnalyzeAuditLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AnalyzeAuditLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AnalyzeAuditLogs", params, headers=headers)
            response = json.loads(body)
            model = models.AnalyzeAuditLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """This API (AssociateSecurityGroups) is used to bind security groups to instances in batches.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsResponse`

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


    def BalanceRoGroupLoad(self, request):
        """This API is used to rebalance the loads of instances in an RO group. Please note that the database connections to those instances will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.

        :param request: Request instance for BalanceRoGroupLoad.
        :type request: :class:`tencentcloud.cdb.v20170320.models.BalanceRoGroupLoadRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.BalanceRoGroupLoadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BalanceRoGroupLoad", params, headers=headers)
            response = json.loads(body)
            model = models.BalanceRoGroupLoadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseCDBProxy(self, request):
        """This API is used to disable database proxy.

        :param request: Request instance for CloseCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CloseCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseCdbProxyAddress(self, request):
        """This API is used to disable the database proxy address.

        :param request: Request instance for CloseCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CloseCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWanService(self, request):
        """This API (CloseWanService) is used to disable public network access for TencentDB instance, which will make public IP addresses inaccessible.

        :param request: Request instance for CloseWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWanService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWanServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccounts(self, request):
        """This API is used to create a TencentDB account. The account name, host address, and password are required. Account remarks and maximum connections can also be configured.

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditPolicy(self, request):
        """This API is used to create an audit policy for a TencentDB instance by associating an audit rule with the TencentDB instance.

        :param request: Request instance for CreateAuditPolicy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditPolicyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """This API (CreateBackup) is used to create a TencentDB instance backup.

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdbProxy(self, request):
        """This API is used create a database proxy for a source instance.

        :param request: Request instance for CreateCdbProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdbProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdbProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdbProxyAddress(self, request):
        """This API is used to create a database proxy address.

        :param request: Request instance for CreateCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloneInstance(self, request):
        """This API is used to create a clone of a specific instance, and roll back the clone by using a physical backup file of the instance or roll back the clone to a point in time.

        :param request: Request instance for CreateCloneInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCloneInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCloneInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloneInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloneInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBImportJob(self, request):
        """This API (CreateDBImportJob) is used to create a data import task for a TencentDB instance.

        Note that the files for a data import task must be uploaded to Tencent Cloud in advance. You need to do so in the console.

        :param request: Request instance for CreateDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBImportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBImportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstance(self, request):
        """This API is used to create a monthly subscribed TencentDB instance (which can be a source, disaster recovery, or read-only instance) by passing in information such as instance specifications, MySQL version number, purchased duration, and quantity.

        This is an asynchronous API. You can also use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance details. If the output parameter `Status` is `1` and the output parameter `TaskStatus` is `0`, the instance has been successfully delivered.

        1. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the purchasable instance specifications, and then use the [DescribeDBPrice](https://intl.cloud.tencent.com/document/api/236/18566?from_cn_redirect=1) API to query the prices of the purchasable instances.
        2. You can create up to 100 instances at a time, with an instance validity period of up to 36 months.
        3. MySQL v5.5, v5.6, v5.7, and v8.0 are supported.
        4. Source instances, read-only instances, and disaster recovery instances can be created.
        5. If `Port`, `ParamList`, or `Password` is specified in the input parameters, the instance (excluding basic instances) will be initialized.
        6. If `Port`, `ParamTemplateId`, or `AlarmPolicyList` is specified in the input parameters, you need to update your SDK to the latest version.

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceResponse`

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


    def CreateDBInstanceHour(self, request):
        """This API is used to create a pay-as-you-go TencentDB instance (which can be a source, disaster recovery, or read-only instance) by passing in information such as instance specifications, MySQL version number, and quantity.

        This is an async API. You can also use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance details. If the `Status` value of an instance is `1` and `TaskStatus` is `0`, the instance has been successfully delivered.

        1. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the purchasable instance specifications, and then use the [DescribeDBPrice](https://intl.cloud.tencent.com/document/api/236/18566?from_cn_redirect=1) API to query the prices of the purchasable instances.
        2. You can create up to 100 instances at a time, with an instance validity period of up to 36 months.
        3. MySQL 5.5, 5.6, 5.7, and 8.0 are supported.
        4. Source instances, disaster recovery instances, and read-only instances can be created.
        5. If `Port`, `ParamList`, or `Password` is specified in the input parameters, the instance will be initialized.

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceHour", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceHourResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatabase(self, request):
        """This API is used to create a database in a TencentDB instance.

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDatabaseResponse`

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


    def CreateParamTemplate(self, request):
        """This API is used to create a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoInstanceIp(self, request):
        """This API is used to create a VIP exclusive to a TencentDB read-only instance.

        :param request: Request instance for CreateRoInstanceIp.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateRoInstanceIpRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateRoInstanceIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoInstanceIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoInstanceIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccounts(self, request):
        """This API (DeleteAccounts) is used to delete TencentDB accounts.

        :param request: Request instance for DeleteAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackup(self, request):
        """This API is used to delete a database backup. It can only delete manually initiated backups.

        :param request: Request instance for DeleteBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        """This API is used to delete a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTimeWindow(self, request):
        """This API (DeleteTimeWindow) is used to delete a maintenance time window for a TencentDB instance. After it is deleted, the default maintenance time window will be 03:00-04:00, i.e., switch to a new instance will be performed during 03:00-04:00 by default.

        :param request: Request instance for DeleteTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """This API (DescribeAccountPrivileges) is used to query the information of TencentDB account permissions.

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesResponse`

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
        """This API is used to query information of all TencentDB accounts.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsResponse`

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


    def DescribeAsyncRequestInfo(self, request):
        """This API (DescribeAsyncRequestInfo) is used to query the async task execution result of a TencentDB instance.

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRequestInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRequestInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditPolicies(self, request):
        """This API is used to query the audit policies of a TencentDB instance.

        :param request: Request instance for DescribeAuditPolicies.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditPoliciesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRules(self, request):
        """This API is used to query the audit rules in the current region.

        :param request: Request instance for DescribeAuditRules.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRulesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupConfig(self, request):
        """This API (DescribeBackupConfig) is used to query the configuration information of a TencentDB instance backup.

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDecryptionKey(self, request):
        """This API is used to query the decryption key of a backup file.

        :param request: Request instance for DescribeBackupDecryptionKey.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDecryptionKeyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDecryptionKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDecryptionKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDecryptionKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadRestriction(self, request):
        """This API is used to query the restrictions of downloading backups in a region.

        :param request: Request instance for DescribeBackupDownloadRestriction.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupEncryptionStatus(self, request):
        """This API is used to query the default encryption status of an instance backup.

        :param request: Request instance for DescribeBackupEncryptionStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupEncryptionStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupEncryptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupEncryptionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupEncryptionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupOverview(self, request):
        """This API is used to query the backup overview of a user. It will return the user's current total number of backups, total capacity used by backups, capacity in the free tier, and paid capacity (all capacity values are in bytes).

        :param request: Request instance for DescribeBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummaries(self, request):
        """This API is used to query the statistics of backups. It will return the capacity used by backups at the instance level and the number and used capacity of data backups and log backups of each instance (all capacity values are in bytes).

        :param request: Request instance for DescribeBackupSummaries.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupSummariesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupSummariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackups(self, request):
        """This API (DescribeBackups) is used to query the backups of a TencentDB instance.

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogBackupOverview(self, request):
        """This API is used to query the log backup overview of a user in the current region.

        :param request: Request instance for DescribeBinlogBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogs(self, request):
        """This API is used to query the list of binlog files of a TencentDB instance.

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCDBProxy(self, request):
        """接口已经废弃，请使用+DescribeCdbProxyInfo+进行替换。

        This API is deprecated and replaced by the `DescribeCdbProxyInfo` API.

        This API is used to query database proxy. It will be deprecated and replaced by the `QueryCDBProxy` API.

        :param request: Request instance for DescribeCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdbProxyInfo(self, request):
        """This API is used to query the details of a database proxy.

        :param request: Request instance for DescribeCdbProxyInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbProxyInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbProxyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdbProxyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdbProxyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdbZoneConfig(self, request):
        """This API is used to query the purchasable specifications of TencentDB instances in a region.

        :param request: Request instance for DescribeCdbZoneConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbZoneConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdbZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdbZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloneList(self, request):
        """This API is used to query the clone task list of an instance.

        :param request: Request instance for DescribeCloneList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCloneListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCloneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBFeatures(self, request):
        """This API is used to query database version attributes, including supported features such as database encryption and audit.

        :param request: Request instance for DescribeDBFeatures.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBFeaturesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBFeaturesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBFeatures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBFeaturesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBImportRecords(self, request):
        """This API (DescribeDBImportRecords) is used to query the records of import tasks in a TencentDB instance.

        :param request: Request instance for DescribeDBImportRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBImportRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBImportRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceCharset(self, request):
        """This API (DescribeDBInstanceCharset) is used to query the character set and its name of a TencentDB instance.

        :param request: Request instance for DescribeDBInstanceCharset.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceCharset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceCharsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceConfig(self, request):
        """This API (DescribeDBInstanceConfig) is used to query the configuration information of a TencentDB instance, such as its synchronization mode and deployment mode.

        :param request: Request instance for DescribeDBInstanceConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceGTID(self, request):
        """This API (DescribeDBInstanceGTID) is used to query whether GTID is activated for a TencentDB instance. Instances on or below version 5.5 are not supported.

        :param request: Request instance for DescribeDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceGTID", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceGTIDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceInfo(self, request):
        """This API is used to query the basic information of an instance (instance ID, instance name, and whether encryption is enabled).

        :param request: Request instance for DescribeDBInstanceInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceRebootTime(self, request):
        """This API (DescribeDBInstanceRebootTime) is used to query the estimated time needed for a TencentDB instance to restart.

        :param request: Request instance for DescribeDBInstanceRebootTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceRebootTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceRebootTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """This API (DescribeDBInstances) is used to query the list of TencentDB instances (which can be primary, disaster recovery, or read-only instances). It supports filtering instances by project ID, instance ID, access address, and instance status.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesResponse`

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


    def DescribeDBPrice(self, request):
        """This API is used to query the purchase or renewal price of a pay-as-you-go or monthly subscribed TencentDB instance by passing in information such as instance type, purchase duration, number of instances to purchase, memory size, disk size, and AZ. For the price of instance renewal, you can pass in instance name to query.

        Note: To query prices in a specific region, you need to use the access point of the region. For more information on access points, see <a href="https://www.tencentcloud.com/document/product/236/15832">Service Address</a>. For example, to query prices in Guangzhou, send a request to: cdb.ap-guangzhou.tencentcloudapi.com. Likewise, to query prices in Shanghai, send a request to: cdb.ap-shanghai.tencentcloudapi.com.

        :param request: Request instance for DescribeDBPrice.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """This API (DescribeDBSecurityGroups) is used to query the security group details of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeDBSwitchRecords(self, request):
        """This API (DescribeDBSwitchRecords) is used to query the instance switch records.

        :param request: Request instance for DescribeDBSwitchRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSwitchRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSwitchRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataBackupOverview(self, request):
        """This API is used to query the data backup overview of a user in the current region.

        :param request: Request instance for DescribeDataBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDataBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDataBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """This API is used to query the information of databases in a TencentDB instance which must be a source or disaster recovery instance.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesResponse`

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


    def DescribeDefaultParams(self, request):
        """This API (DescribeDefaultParams) is used to query the list of default configurable parameters.

        :param request: Request instance for DescribeDefaultParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceMonitorInfo(self, request):
        """This API (DescribeDeviceMonitorInfo) is used to query the monitoring information of a TencentDB physical machine on the day. Currently, it only supports instances with 488 GB memory and 6 TB disk.

        :param request: Request instance for DescribeDeviceMonitorInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceMonitorInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceMonitorInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeErrorLogData(self, request):
        """This API is used to query the error logs of an instance over the past month by search criteria.
        Note: the HTTP response packet will be very large if it contain a single large error log, which causes the API call to time out. If this happens, we recommend you lower the value of the input parameter `Limit` to reduce the packet size so that the API can respond timely.

        :param request: Request instance for DescribeErrorLogData.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeErrorLogDataRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeErrorLogDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeErrorLogData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorLogDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        """This API (DescribeInstanceParamRecords) is used to query the parameter modification records of an instance.

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParamRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        """This API (DescribeInstanceParams) is used to query the list of parameters for an instance.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalBinlogConfig(self, request):
        """This API is used to query the retention policy of local binlog of an instance.

        :param request: Request instance for DescribeLocalBinlogConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeLocalBinlogConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeLocalBinlogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalBinlogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalBinlogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplateInfo(self, request):
        """This API is used to query parameter template details. The common request parameter `Region` can only be set to `ap-guangzhou`.

        :param request: Request instance for DescribeParamTemplateInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplates(self, request):
        """This API is used to query the parameter template list. The common request parameter `Region` can only be set to `ap-guangzhou`.

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """This API (DescribeProjectSecurityGroups) is used to query the security group details of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeProxyConnectionPoolConf(self, request):
        """当前接口已经废弃，请使用+DescribeCdbProxyInfo+替代。

        This API has been deprecated and replaced by the `DescribeCdbProxyInfo` API.

        This API is used to query the connection pool configuration of a database proxy.

        :param request: Request instance for DescribeProxyConnectionPoolConf.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyConnectionPoolConfRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyConnectionPoolConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyConnectionPoolConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyConnectionPoolConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyCustomConf(self, request):
        """This API is used to query the proxy configuration.

        :param request: Request instance for DescribeProxyCustomConf.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyCustomConfRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyCustomConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyCustomConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyCustomConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySupportParam(self, request):
        """This API is used to query the supported proxy versions and parameters for an instance.

        :param request: Request instance for DescribeProxySupportParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProxySupportParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProxySupportParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySupportParam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySupportParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRemoteBackupConfig(self, request):
        """This API is used to query the configuration information of a remote TencentDB instance backup.

        :param request: Request instance for DescribeRemoteBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRemoteBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRemoteBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRemoteBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRemoteBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoGroups(self, request):
        """This API is used to query the information of all RO groups of a TencentDB instance.

        :param request: Request instance for DescribeRoGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRoGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRoGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoMinScale(self, request):
        """This API is used to query the minimum specification of a read-only instance that can be purchased or upgraded to.

        :param request: Request instance for DescribeRoMinScale.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRoMinScaleRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRoMinScaleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoMinScale", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoMinScaleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackRangeTime(self, request):
        """This API (DescribeRollbackRangeTime) is used to query the time range available for instance rollback.

        :param request: Request instance for DescribeRollbackRangeTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackRangeTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackRangeTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTaskDetail(self, request):
        """This API is used to query the details of a TencentDB instance rollback task.

        :param request: Request instance for DescribeRollbackTaskDetail.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogData(self, request):
        """This API is used to query the slow logs of an instance over the past month by search criteria.
        Note: the HTTP response packet will be very large if it contain a single large slow log, which causes the API call to time out. If this happens, we recommend you lower the value of the input parameter `Limit` to reduce the packet size so that the API can respond timely.

        :param request: Request instance for DescribeSlowLogData.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogDataRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        """This API (DescribeSlowLogs) is used to query the slow logs of a TencentDB instance.

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportedPrivileges(self, request):
        """This API (DescribeSupportedPrivileges) is used to query the information of TencentDB account permissions, including global permissions, database permissions, table permissions, and column permissions.

        :param request: Request instance for DescribeSupportedPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportedPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportedPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        """This API is used to query the information of database tables in a TencentDB instance. It only supports source or disaster recovery instances.

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagsOfInstanceIds(self, request):
        """This API (DescribeTagsOfInstanceIds) is used to query the tag information of a TencentDB instance.

        :param request: Request instance for DescribeTagsOfInstanceIds.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagsOfInstanceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsOfInstanceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """This API (DescribeTasks) is used to query the list of tasks for a TencentDB instance.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeWindow(self, request):
        """This API (DescribeTimeWindow) is used to query the maintenance time window of a TencentDB instance.

        :param request: Request instance for DescribeTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadedFiles(self, request):
        """This API is used to query the list of SQL files imported by users. The common request parameter `Region` must be `ap-shanghai`.

        :param request: Request instance for DescribeUploadedFiles.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadedFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadedFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API (DisassociateSecurityGroups) is used to unbind security groups from instances in batches.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsResponse`

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


    def InitDBInstances(self, request):
        """该接口不再维护，参考CreateDBInstance+API文档，在发货时即可完成初始化。

        This API was disused. You can refer to the CreateDBInstance API, and initialize the instance when creating it.

        This API is used to initialize a TencentDB instance, including initial password, default character set, and instance port number. But it is disused and not recommended. You can now set the instance information by using the parameter `Password`, `ParamList`, and `Port` respectively in the `CreateDBInstance` and `CreateDBInstanceHour` APIs.

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBInstance(self, request):
        """This API is used to isolate a TencentDB instance, which will no longer be accessible via IP and port. The isolated instance can be started up in the recycle bin. If it is isolated due to arrears, please top up your account as soon as possible.

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceResponse`

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


    def ModifyAccountDescription(self, request):
        """This API (ModifyAccountDescription) is used to modify the remarks of a TencentDB instance account.

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionResponse`

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


    def ModifyAccountMaxUserConnections(self, request):
        """This API is used to modify the maximum connections of one or more TencentDB instance accounts.

        :param request: Request instance for ModifyAccountMaxUserConnections.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountMaxUserConnectionsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountMaxUserConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountMaxUserConnections", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountMaxUserConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPassword(self, request):
        """This API (ModifyAccountPassword) is used to modify the password of a TencentDB instance account.

        :param request: Request instance for ModifyAccountPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """This API is used to modify the permissions of a TencentDB instance account.

        Note that when modifying account permissions, you need to pass in the full permission information of the account. You can [query the account permission information
        ](https://intl.cloud.tencent.com/document/api/236/17500?from_cn_redirect=1) first before modifying permissions.

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPrivilegesResponse`

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


    def ModifyAutoRenewFlag(self, request):
        """This API is used to modify the auto-renewal flag of a TencentDB instance.

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagResponse`

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


    def ModifyBackupConfig(self, request):
        """This API (ModifyBackupConfig) is used to modify the database backup configuration.

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupDownloadRestriction(self, request):
        """This API is used to modify the restrictions of downloading backups in a region. You can specify which types of networks (private, or both private and public), VPCs, and IPs to download backups.

        :param request: Request instance for ModifyBackupDownloadRestriction.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupEncryptionStatus(self, request):
        """This API is used to set the encryption status of an instance backup.

        :param request: Request instance for ModifyBackupEncryptionStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupEncryptionStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupEncryptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupEncryptionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupEncryptionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCDBProxyConnectionPool(self, request):
        """当前接口已经废弃，请使用+AdjustCdbProxyAddress+进行替代。

        This API has been deprecated and replaced with `AdjustCdbProxyAddress`.

        This API is used to configure the connection pool of database proxy. The supported configurations can be obtained by the `DescribeProxyConnectionPoolConf` API.

        :param request: Request instance for ModifyCDBProxyConnectionPool.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyConnectionPoolRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyConnectionPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCDBProxyConnectionPool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCDBProxyConnectionPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCDBProxyDesc(self, request):
        """当前接口已经废弃，请使用+ModifyCdbProxyAddressDesc+进行替代。

        This API has been deprecated and replaced with `ModifyCdbProxyAddressDesc`.

        This API is used to modify the description of a database proxy.

        :param request: Request instance for ModifyCDBProxyDesc.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyDescRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCDBProxyDesc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCDBProxyDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCDBProxyVipVPort(self, request):
        """当前接口已经废弃，请使用+ModifyCdbProxyAddressVipAndVPort+进行替代。

        This API has been deprecated and replaced with `ModifyCdbProxyAddressVipAndVPort`.

        This API is used to modify the VIP or the port of a database proxy.

        :param request: Request instance for ModifyCDBProxyVipVPort.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyVipVPortRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCDBProxyVipVPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCDBProxyVipVPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCDBProxyVipVPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyAddressDesc(self, request):
        """This API is used to modify the description of a proxy address.

        :param request: Request instance for ModifyCdbProxyAddressDesc.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressDescRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyAddressDesc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyAddressDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyAddressVipAndVPort(self, request):
        """This API is used to modify the VPC of the database proxy address.

        :param request: Request instance for ModifyCdbProxyAddressVipAndVPort.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressVipAndVPortRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressVipAndVPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyAddressVipAndVPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyAddressVipAndVPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyParam(self, request):
        """This API is used to configure the database proxy parameters.

        :param request: Request instance for ModifyCdbProxyParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """This API (ModifyDBInstanceName) is used to rename a TencentDB instance.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceProject(self, request):
        """This API (ModifyDBInstanceProject) is used to modify the project to which a TencentDB instance belongs.

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API (ModifyDBInstanceSecurityGroups) is used to modify the security groups bound to a TencentDB instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstanceVipVport(self, request):
        """This API is used to modify the IP and port number of a TencentDB instance, switch from classic network to VPC, or change VPC subnets.

        :param request: Request instance for ModifyDBInstanceVipVport.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """This API (ModifyInstanceParam) is used to modify instance parameters.

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancePasswordComplexity(self, request):
        """This API is used to modify the password complexity of a TencentDB instance.

        :param request: Request instance for ModifyInstancePasswordComplexity.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstancePasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstancePasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancePasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancePasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceTag(self, request):
        """This API (ModifyInstanceTag) is used to add, modify, or delete an instance tag.

        :param request: Request instance for ModifyInstanceTag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLocalBinlogConfig(self, request):
        """This API is used to modify the retention policy of local binlog of an instance.

        :param request: Request instance for ModifyLocalBinlogConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyLocalBinlogConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyLocalBinlogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLocalBinlogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLocalBinlogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNameOrDescByDpId(self, request):
        """This API is used to modify the name or description of a placement group.

        :param request: Request instance for ModifyNameOrDescByDpId.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNameOrDescByDpId", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNameOrDescByDpIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParamTemplate(self, request):
        """This API is used to modify a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRemoteBackupConfig(self, request):
        """This API is used to modify the configuration information of a remote TencentDB instance backup.

        :param request: Request instance for ModifyRemoteBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyRemoteBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyRemoteBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRemoteBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRemoteBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoGroupInfo(self, request):
        """This API is used to update the information of a TencentDB RO group, such as configuring a read-only instance removal policy in case of excessive delay, setting read weights of read-only instances, and setting the replication delay.

        :param request: Request instance for ModifyRoGroupInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTimeWindow(self, request):
        """This API (ModifyTimeWindow) is used to update the maintenance time window of a TencentDB instance.

        :param request: Request instance for ModifyTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineIsolatedInstances(self, request):
        """This API (OfflineIsolatedInstances) is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status, i.e., their `Status` value is 5 in the return of the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1).

        This is an asynchronous API. There may be a delay in repossessing some resources. You can query the details by using the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) and specifying the InstanceId and the `Status` value as [5, 6, 7]. If the returned instance is empty, then all its resources have been released.

        Note that once an instance is deactivated, its resources and data will not be recoverable. Please do so with caution.

        :param request: Request instance for OfflineIsolatedInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OfflineIsolatedInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OfflineIsolatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineIsolatedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineIsolatedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """This API is used to enable the audit service.

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBInstanceEncryption(self, request):
        """This API is used to enable the encryption feature for instance data storage, and custom keys are supported.

        Note: Before enabling data storage encryption for an instance, you need to perform the following operations:

        1. [Initialize an instance](https://intl.cloud.tencent.com/document/api/236/15873?from_cn_redirect=1).

        2. Enable [KMS service](https://console.cloud.tencent.com/kms2)

        3. [Grant permission to access KMS](https://console.cloud.tencent.com/cam/role) for TencentDB for MySQL. The role name is `MySQL_QCSRole`, and the preset policy name is `QcloudAccessForMySQLRole`.

        This API calling may take up to 10 seconds, causing the client to time out. If it returns `InternalError`, call `DescribeDBInstanceInfo` to confirm whether the backend encryption is enabled successfully.

        :param request: Request instance for OpenDBInstanceEncryption.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceEncryptionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceEncryptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBInstanceEncryption", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBInstanceEncryptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBInstanceGTID(self, request):
        """This API (OpenDBInstanceGTID) is used to enable GTID for a TencentDB instance. Only instances on or above version 5.6 are supported.

        :param request: Request instance for OpenDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBInstanceGTID", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBInstanceGTIDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWanService(self, request):
        """This API (OpenWanService) is used to enable public network access for an instance.

        Note that before enabling public network access, you need to first [initialize the instance](https://intl.cloud.tencent.com/document/api/236/15873?from_cn_redirect=1).

        :param request: Request instance for OpenWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWanService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWanServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCDBProxy(self, request):
        """当前接口已经废弃，请使用+DescribeCdbProxyInfo+进行替代。

        This API has been deprecated and replaced with `DescribeCdbProxyInfo`.

        This API is used to query the proxy details.

        :param request: Request instance for QueryCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.QueryCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.QueryCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIsolatedDBInstances(self, request):
        """This API is used to deisolate an isolated TencentDB instance.

        :param request: Request instance for ReleaseIsolatedDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ReleaseIsolatedDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ReleaseIsolatedDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIsolatedDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIsolatedDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReloadBalanceProxyNode(self, request):
        """This API is used to rebalance the load on database proxy.

        :param request: Request instance for ReloadBalanceProxyNode.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ReloadBalanceProxyNodeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ReloadBalanceProxyNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReloadBalanceProxyNode", params, headers=headers)
            response = json.loads(body)
            model = models.ReloadBalanceProxyNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBInstance(self, request):
        """This API is used to renew a monthly subscribed TencentDB instance, and a pay-as-you-go instance can be renewed as a monthly subscribed one by this API.

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRootAccount(self, request):
        """This API is used to reset the root account and initialize the account permissions.

        :param request: Request instance for ResetRootAccount.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ResetRootAccountRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ResetRootAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRootAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRootAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDBInstances(self, request):
        """This API (RestartDBInstances) is used to restart TencentDB instances.

        Note:
        1. This API only supports restarting primary instances.
        2. The instance status must be normal, and no other async tasks are in progress.

        :param request: Request instance for RestartDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.RestartDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.RestartDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBatchRollback(self, request):
        """This API (StartBatchRollback) is used to roll back the tables of a TencentDB instance in batches.

        :param request: Request instance for StartBatchRollback.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBatchRollback", params, headers=headers)
            response = json.loads(body)
            model = models.StartBatchRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartReplication(self, request):
        """This API is used to start the data replication from the source instance to the read-only instance.

        :param request: Request instance for StartReplication.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartReplicationRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartReplication", params, headers=headers)
            response = json.loads(body)
            model = models.StartReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDBImportJob(self, request):
        """This API (StopDBImportJob) is used to stop a data import task.

        :param request: Request instance for StopDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDBImportJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopDBImportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopReplication(self, request):
        """This API is used to stop the data replication from the source instance to the read-only instance.

        :param request: Request instance for StopReplication.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopReplicationRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopReplication", params, headers=headers)
            response = json.loads(body)
            model = models.StopReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRollback(self, request):
        """This API is used to cancel a rollback task in progress, and returns an async task ID. You can use the `DescribeAsyncRequestInfo` API to query the result of cancellation.

        :param request: Request instance for StopRollback.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopRollbackRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRollback", params, headers=headers)
            response = json.loads(body)
            model = models.StopRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchCDBProxy(self, request):
        """This API is used to switch database proxy after the proxy configuration is modified or the proxy version is upgraded.

        :param request: Request instance for SwitchCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstanceMasterSlave(self, request):
        """This API is used for source-to-replica switch.

        :param request: Request instance for SwitchDBInstanceMasterSlave.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchDBInstanceMasterSlaveRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchDBInstanceMasterSlaveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstanceMasterSlave", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstanceMasterSlaveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDrInstanceToMaster(self, request):
        """This API is used to promote a disaster recovery instance to source instance. The request parameter `Region` must be the region of the disaster recovery instance.

        :param request: Request instance for SwitchDrInstanceToMaster.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchDrInstanceToMasterRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchDrInstanceToMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDrInstanceToMaster", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDrInstanceToMasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchForUpgrade(self, request):
        """This API (SwitchForUpgrade) is used to switch to a new instance. You can initiate this process when the primary instance being upgraded is pending switch.

        :param request: Request instance for SwitchForUpgrade.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchForUpgrade", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchForUpgradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeCDBProxyVersion(self, request):
        """This API is used to upgrade the version of database proxy.

        :param request: Request instance for UpgradeCDBProxyVersion.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeCDBProxyVersionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeCDBProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeCDBProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeCDBProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """This API is used to upgrade or downgrade a TencentDB instance, which can be a primary instance, disaster recovery instance, or read-only instance.

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstanceEngineVersion(self, request):
        """This API (UpgradeDBInstanceEngineVersion) is used to upgrade the version of a TencentDB instance, which can be a primary instance, disaster recovery instance, or read-only instance.

        :param request: Request instance for UpgradeDBInstanceEngineVersion.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceEngineVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceEngineVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))