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
from tencentcloud.cdb.v20170320 import models


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.intl.tencentcloudapi.com'
    _service = 'cdb'


    def AddTimeWindow(self, request):
        r"""This API is used to add a maintenance time window for cloud database instances to specify which time periods allow automatic execution of access operations.

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
        r"""This API is used to adjust database proxy configuration.

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
        r"""This API is used to adjust the database proxy address configuration.

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
        r"""This API is used to perform aggregation statistics on specified data columns in audit log result sets with different filter criteria.

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
        r"""This API (AssociateSecurityGroups) is used to bind security groups to instances in batches.

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
        r"""This API is used to rebalance the loads of instances in an RO group. Please note that the database connections to those instances will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.

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


    def CloseAuditService(self, request):
        r"""This API is used to disable the audit service for an instance.

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseCDBProxy(self, request):
        r"""This API is used to disable the database proxy.

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
        r"""This API is used to disable database proxy.

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


    def CloseSSL(self, request):
        r"""This API is used to close the SSL connectivity function.

        :param request: Request instance for CloseSSL.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseSSLRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseSSL", params, headers=headers)
            response = json.loads(body)
            model = models.CloseSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWanService(self, request):
        r"""This API (CloseWanService) is used to disable public network access for TencentDB instance, which will make public IP addresses inaccessible.

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
        r"""This API is used to create cloud database accounts. It requires specifying a new account name and domain name as well as the corresponding password. You can also set the account's remark information and maximum number of available connections.

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


    def CreateAuditLogFile(self, request):
        r"""This API is used to create an audit log file for a TencentDB instance.

        :param request: Request instance for CreateAuditLogFile.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditPolicy(self, request):
        r"""This API is used to create an audit policy for a TencentDB instance by associating an audit rule with the TencentDB instance.

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


    def CreateAuditRuleTemplate(self, request):
        r"""This API is used to create an audit rule template.

        :param request: Request instance for CreateAuditRuleTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        r"""This API is used to create a database backup.

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
        r"""This API is used to create a database proxy for the primary instance.

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
        r"""This API is used to add a proxy address for database proxy.

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
        r"""This API is used to create a clone instance from the source instance. You can specify a physical backup file or a rollback time point for the clone instance.

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
        r"""This API is used to create a cloud database data import task.
        Note that the file for the data import task must be uploaded to Tencent Cloud in advance. The user must perform file import on the console.

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
        r"""This API is used to create a cloud database instance with an annual/monthly subscription, including primary instance, disaster recovery instance, and read-only instance. You can create a cloud database instance by importing instance specification, MySQL version number, purchase period, and quantity information.

        This API is an asynchronous API. You can also use the query instance list API (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) to query the instance details. When the Status of the instance is 1 and TaskStatus is 0, it means the instance has been delivered successfully.

        1. First, please use the API for the query (https://www.tencentcloud.com/document/api/236/17229?from_cn_redirect=1) to obtain the purchasable specifications of cloud databases, then please use the API for the query (https://www.tencentcloud.com/document/api/236/18566?from_cn_redirect=1) to query database price.
        2. You can create up to 100 instances at a time, with a maximum instance duration of 36 months.
        3. Support creating MySQL 5.5, MySQL 5.6, MySQL 5.7, and MySQL 8.0 versions.
        4. Support creating primary instance, read-only instance, disaster recovery instance.
        5. When ParamTemplateId or AlarmPolicyList is specified in the input parameters, you need to upgrade the SDK to the latest version to support it.

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
        r"""This API is used to create pay-as-you-go instances. You can create a cloud database instance by inputting the instance specification, MySQL version number, quantity, etc. It supports the creation of primary instances, disaster recovery instances, and read-only instances.

        This API is an async API. You can also use the API for the query (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) to check the instance details. When the instance Status is 1 and TaskStatus is 0, it means the instance has been delivered successfully.

        1. First, please use the API for the query (https://www.tencentcloud.com/document/api/236/17229?from_cn_redirect=1) to obtain the purchasable specifications of cloud databases, then please use the API for the query (https://www.tencentcloud.com/document/api/236/18566?from_cn_redirect=1) to query the instance selling price.
        2. Supports a maximum of 100 instances created at a time, with a maximum duration of 36 months;
        3. Support creating MySQL 5.5, MySQL 5.6, MySQL 5.7, and MySQL 8.0 versions.
        4. Support creating primary instances, disaster recovery instances, and read-only instances.

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
        r"""This API is used to create a database in a TencentDB instance.

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
        r"""This API is used to create a parameter template.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.

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
        r"""This API is used to create a VIP exclusive to a TencentDB read-only instance.

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


    def CreateRotationPassword(self, request):
        r"""This API is used to enable password rotation.

        :param request: Request instance for CreateRotationPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateRotationPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateRotationPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRotationPassword", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRotationPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccounts(self, request):
        r"""This API is used to delete CDB accounts.

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


    def DeleteAuditLogFile(self, request):
        r"""This API is used to delete an audit log file of a TencentDB instance.

        :param request: Request instance for DeleteAuditLogFile.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditPolicy(self, request):
        r"""This API is used to delete an audit policy.

        :param request: Request instance for DeleteAuditPolicy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditPolicyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditRuleTemplates(self, request):
        r"""This API is used to delete audit rule templates.

        :param request: Request instance for DeleteAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackup(self, request):
        r"""This API is used to delete database backups. It only supports deleting manually initiated backups.

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


    def DeleteDatabase(self, request):
        r"""This API is used to delete a database in a cloud database instance.

        :param request: Request instance for DeleteDatabase.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteDatabaseRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        r"""This API is used to delete parameter template.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.

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


    def DeleteRotationPassword(self, request):
        r"""This API is used to close instance account password rotation.

        :param request: Request instance for DeleteRotationPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteRotationPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteRotationPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRotationPassword", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRotationPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTimeWindow(self, request):
        r"""This API is used to delete the maintenance time window of a cloud database instance. After deleting the instance maintenance window, the default maintenance period is 03:00-04:00 daily with a data validation delay threshold of 10 seconds. When switching to a new instance during the maintenance time window, the switch is performed by default at 03:00-04:00.

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
        r"""This API is used to query the permission information supported by a cloud database account.

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
        r"""This API is used to query ALL account information of the cloud database.

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
        r"""This API (DescribeAsyncRequestInfo) is used to query the async task execution result of a TencentDB instance.

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


    def DescribeAuditConfig(self, request):
        r"""This API is used to query the service configurations for a TencentDB audit policy, including the audit log retention period.

        :param request: Request instance for DescribeAuditConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditInstanceList(self, request):
        r"""This API is used to obtain the list of audit instances.

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogFiles(self, request):
        r"""This API is used to query the audit log files of a TencentDB instance.

        :param request: Request instance for DescribeAuditLogFiles.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogFilesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogs(self, request):
        r"""This API is used to query database audit logs.

        :param request: Request instance for DescribeAuditLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditPolicies(self, request):
        r"""This API is used to query audit policies of cloud database instances.

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


    def DescribeAuditRuleTemplateModifyHistory(self, request):
        r"""This API is used to query the change history of rule templates.

        :param request: Request instance for DescribeAuditRuleTemplateModifyHistory.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplateModifyHistoryRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplateModifyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleTemplateModifyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleTemplateModifyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRuleTemplates(self, request):
        r"""This API is used to query the information of audit rule templates.

        :param request: Request instance for DescribeAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRules(self, request):
        r"""This API is used to create audit rules no longer supported.

        This API is used to query audit rules in current region.

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
        r"""This API is used to query database backup configuration info.

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
        r"""This API is used to query the decryption key of a backup file.

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
        r"""This API is used to query the restrictions of downloading backups in a region.

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
        r"""This API is used to query the default encryption status of an instance backup.

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
        r"""This API is used to query the backup overview of a user. It will return the user's current total number of backups, total capacity used by backups, capacity in the free tier, and paid capacity (all capacity values are in bytes).

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
        r"""This API is used to query backup statistics, return the occupied capacity of backups by instance as well as the count and capacity of data backup and log backup for each instance (in bytes).

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
        r"""This API (DescribeBackups) is used to query the backups of a TencentDB instance.

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
        r"""This API is used to query the log backup overview of a user in the current region.

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
        r"""This API is used to query the list of binlog files of a TencentDB instance.

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


    def DescribeCPUExpandStrategyInfo(self, request):
        r"""This API is used to query the CPU Elastic Scaling information of an instance.

        :param request: Request instance for DescribeCPUExpandStrategyInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCPUExpandStrategyInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCPUExpandStrategyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCPUExpandStrategyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCPUExpandStrategyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdbProxyInfo(self, request):
        r"""This API is used to query database proxy detailed information.

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
        r"""This API is used to query the purchasable specifications of TencentDB instances in a region.

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
        r"""This API is used to query the clone task list of a user instance.

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
        r"""This API is used to query cloud database version attributes, including whether database encryption and database audit are supported, and other features.

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
        r"""This API (DescribeDBImportRecords) is used to query the records of import tasks in a TencentDB instance.

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
        r"""This API (DescribeDBInstanceCharset) is used to query the character set and its name of a TencentDB instance.

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
        r"""This API is used to query the configuration message of a cloud database instance, including sync mode and deployment mode.

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
        r"""This API (DescribeDBInstanceGTID) is used to query whether GTID is activated for a TencentDB instance. Instances on or below version 5.5 are not supported.

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
        r"""This API is used to query the basic information of an instance, including instance ID, instance name, and whether encryption is enabled. Querying read-only instances is not supported.

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


    def DescribeDBInstanceLogToCLS(self, request):
        r"""This API is used to query the configuration of slow log and error log delivery to CLS for an instance. It filters out the present instance log delivery configuration to CLS by AppId, Region, and instance ID.

        :param request: Request instance for DescribeDBInstanceLogToCLS.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceLogToCLSRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceLogToCLSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceLogToCLS", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceLogToCLSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceRebootTime(self, request):
        r"""This API is used to query the expected time required to restart a cloud database instance.

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
        r"""This API is used to query the list of TencentDB for MySQL instances. It supports filtering instances by conditions such as project ID, instance ID, access address, and instance status. It also supports querying the list of information about primary instances, disaster recovery instances, and read-only instances.
        This API is used to return the availability zone (AZ) status during purchase, which does not change along with the proactive HA switch. If you want to know the AZ status in real time, query through the [DescribeDBInstanceConfig](https://www.tencentcloud.com/document/product/236/17491?from_cn_redirect=1) API.

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
        r"""This API is used to query the price of purchasing or renewing a cloud database instance. It supports querying the price of pay-as-you-go or yearly/monthly subscription. You can input instance type, purchase period, purchase quantity, memory size, disk capacity and availability zone information to query instance price. You can input instance name to query instance renewal price.

        Note: To request a price for a certain region, please use the access point of the corresponding region. For access point information, please refer to the <a href="https://www.tencentcloud.com/document/api/236/15832?from_cn_redirect=1">service address</a> document. For example, to request a price for the Guangzhou region, send the request to: cdb.ap-guangzhou.tencentcloudapi.com. Likewise, for the Shanghai region, send the request to: cdb.ap-shanghai.tencentcloudapi.com.

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
        r"""This API (DescribeDBSecurityGroups) is used to query the security group details of an instance.

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
        r"""This API (DescribeDBSwitchRecords) is used to query the instance switch records.

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
        r"""This API is used to query the data backup overview of a user in the current region.

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
        r"""This API is used to query the information of databases in a TencentDB instance which must be a source or disaster recovery instance.

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
        r"""This API (DescribeDefaultParams) is used to query the list of default configurable parameters.

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
        r"""This API (DescribeDeviceMonitorInfo) is used to query the monitoring information of a TencentDB physical machine on the day. Currently, it only supports instances with 488 GB memory and 6 TB disk.

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
        r"""This API is used to query the error logs of an instance over the past month by search criteria.
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


    def DescribeInstanceAlarmEvents(self, request):
        r"""This API is used to query event information of instance occurrence.

        :param request: Request instance for DescribeInstanceAlarmEvents.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceAlarmEventsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        r"""This API (DescribeInstanceParamRecords) is used to query the parameter modification records of an instance.

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
        r"""This API (DescribeInstanceParams) is used to query the list of parameters for an instance.

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


    def DescribeInstancePasswordComplexity(self, request):
        r"""This API is used to query the password complexity parameter list of the instance.

        :param request: Request instance for DescribeInstancePasswordComplexity.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstancePasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstancePasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancePasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancePasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceUpgradeCheckJob(self, request):
        r"""This API is used to query the instance version upgrade validation task.

        :param request: Request instance for DescribeInstanceUpgradeCheckJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceUpgradeCheckJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceUpgradeCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceUpgradeCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceUpgradeCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceUpgradeType(self, request):
        r"""This API is used to query the upgrade type of a database instance.

        :param request: Request instance for DescribeInstanceUpgradeType.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceUpgradeTypeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceUpgradeTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceUpgradeType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceUpgradeTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalBinlogConfig(self, request):
        r"""This API is used to query the retention policy of local binlog of an instance.

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
        r"""This API is used to query parameter template details.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.

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
        r"""This API is used to query the parameter template list.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.

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
        r"""This API (DescribeProjectSecurityGroups) is used to query the security group details of a project.

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


    def DescribeProxyCustomConf(self, request):
        r"""This API is used to query the proxy configuration.

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
        r"""This API is used to query instance support proxy version and parameters.

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
        r"""This API is used to query the configuration information of a remote TencentDB instance backup.

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
        r"""This API is used to query all RO groups of a cloud database instance.

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
        r"""This API is used to query the minimum specification of a read-only instance that can be purchased or upgraded to.

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
        r"""This API (DescribeRollbackRangeTime) is used to query the time range available for instance rollback.

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
        r"""This API is used to query the rollback task detail of a cloud database instance.

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


    def DescribeSSLStatus(self, request):
        r"""This API is used to query SSL activation status. If SSL has been enabled, it will synchronously return the certificate download URL.

        :param request: Request instance for DescribeSSLStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSSLStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSSLStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSSLStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSSLStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogData(self, request):
        r"""This API is used to search for instance slow logs under usage conditions. Only allow viewing slow logs within one month.
        During use, pay attention: a single slow log may be too large, causing the entire http request return content to be too large, furthermore leading to API timeout. Once timed out, narrow down the Limit parameter value when querying, thereby reducing the size and enabling the API to return content promptly.

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
        r"""This API is used to obtain the slow query log of a cloud database instance.
        Description: If the data volume is too large in a single query, it may lead to response timeout. We recommend shortening the query time range per request, such as one hour, to avoid timeout.

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
        r"""This API (DescribeSupportedPrivileges) is used to query the information of TencentDB account permissions, including global permissions, database permissions, table permissions, and column permissions.

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


    def DescribeTableColumns(self, request):
        r"""This API is used to query table column information of a designated database in a cloud database instance. It only supports primary instance and disaster recovery instance.

        :param request: Request instance for DescribeTableColumns.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTableColumnsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTableColumnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableColumns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableColumnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        r"""This API is used to query the information of database tables in a TencentDB instance. It only supports source or disaster recovery instances.

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
        r"""This API is used to access tag information of the instance for cloud databases.

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
        r"""This API (DescribeTasks) is used to query the list of tasks for a TencentDB instance.

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
        r"""This API (DescribeTimeWindow) is used to query the maintenance time window of a TencentDB instance.

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
        r"""This API is used to query the list of SQL files imported by users. The common request parameter `Region` must be `ap-shanghai`.

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
        r"""This API (DisassociateSecurityGroups) is used to unbind security groups from instances in batches.

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


    def IsolateDBInstance(self, request):
        r"""This API is used to isolate a cloud database instance. After an instance is isolated, you cannot access the database via IP and port. The isolated instance can be started in the recycle bin. If the instance is isolated due to arrears, please recharge as soon as possible.

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
        r"""This API (ModifyAccountDescription) is used to modify the remarks of a TencentDB instance account.

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
        r"""This API is used to modify the maximum number of available connections for a cloud database account.

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
        r"""This API (ModifyAccountPassword) is used to modify the password of a TencentDB instance account.

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
        r"""This API is used to modify the permissions of a TencentDB instance account.

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


    def ModifyAuditConfig(self, request):
        r"""This API is used to modify the service configurations for a TencentDB audit policy, including the audit log retention period.

        :param request: Request instance for ModifyAuditConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditRuleTemplates(self, request):
        r"""This API is used to modify audit rule templates.

        :param request: Request instance for ModifyAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        r"""This API is used to modify the service configurations for a TencentDB instance, including the audit log retention period and the audit rules.

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoRenewFlag(self, request):
        r"""This API is used to modify the auto-renewal flag of a TencentDB instance.

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
        r"""This API is used to modify database backup configuration.

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
        r"""This API is used to modify the restrictions of downloading backups in a region. You can specify which types of networks (private, or both private and public), VPCs, and IPs to download backups.

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
        r"""This API is used to set the encryption status of an instance backup.

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


    def ModifyCdbProxyAddressDesc(self, request):
        r"""This API is used to modify the proxy address description.

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
        r"""This API is used to modify the database proxy address VPC information.

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
        r"""This API is used to configure database proxy parameters.

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


    def ModifyDBInstanceLogToCLS(self, request):
        r"""This API is used to enable or disable the feature of sending CDB slow and error logs to CLS.

        :param request: Request instance for ModifyDBInstanceLogToCLS.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceLogToCLSRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceLogToCLSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceLogToCLS", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceLogToCLSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceModes(self, request):
        r"""This API is used to change the mode of a cloud database.

        :param request: Request instance for ModifyDBInstanceModes.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceModesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceModesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceModes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceModesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        r"""This API (ModifyDBInstanceName) is used to rename a TencentDB instance.

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
        r"""This API (ModifyDBInstanceProject) is used to modify the project to which a TencentDB instance belongs.

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
        r"""This API (ModifyDBInstanceSecurityGroups) is used to modify the security groups bound to a TencentDB instance.

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
        r"""This API is used to modify the IP and port number of a cloud database instance. It can also perform basic network to VPC network and subnet change under VPC network.

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
        r"""This API (ModifyInstanceParam) is used to modify instance parameters.

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
        r"""This API is used to modify the password complexity of a cloud database instance.

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
        r"""This API (ModifyInstanceTag) is used to add, modify, or delete an instance tag.

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
        r"""This API is used to modify the local binlog retention policy of an instance.

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
        r"""This API is used to modify the name or description of a placement group.

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
        r"""This API is used to modify parameter templates.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.

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


    def ModifyProtectMode(self, request):
        r"""This API is used to modify the sync method of an instance.
        Description: This API can be called only by an exclusive cluster. This API is about to go offline.

        :param request: Request instance for ModifyProtectMode.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyProtectModeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyProtectModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRemoteBackupConfig(self, request):
        r"""This API is used to modify the configuration information of a remote TencentDB instance backup.

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
        r"""This API is used to update the information of a TencentDB RO group, such as configuring a read-only instance removal policy in case of excessive delay, setting read weights of read-only instances, and setting the replication delay.

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


    def ModifyRoGroupVipVport(self, request):
        r"""This API is used to modify the vip and vport of a Ro group.

        :param request: Request instance for ModifyRoGroupVipVport.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupVipVportRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoGroupVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoGroupVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTimeWindow(self, request):
        r"""This API (ModifyTimeWindow) is used to update the maintenance time window of a TencentDB instance.

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
        r"""This api is used to deactivate cloud database instances in quarantined state now. The instance Status for row operations must be quarantined state, such as instances with Status value 5 queried through the query instance list api.

        This API is used to perform asynchronous operation, and delays may occur when reclaiming partial resources. You can query by using the query instance list API (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) with specified instance InstanceId and status Status as [5,6,7]. Among them, 5 represents isolated, 6 represents offline, and 7 represents Offline. If the return instance is empty, all instance resources have been released.

        Note that after the instance goes offline, relevant resources and data cannot be recovered. Proceed with caution.

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
        r"""This API is used to activate audit service for CDB instance.

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
        r"""This API is used to enable data storage encryption for instance and support users to specify custom keys.

        Note that before enabling data storage encryption for instance, perform the following operations:

        1. Perform instance initialization (https://www.tencentcloud.com/document/api/236/15873?from_cn_redirect=1).

        2. Enable the KMS service (https://console.cloud.tencent.com/kms2).

        3. Grant the cloud database (MySQL) permission to access the KMS key (https://console.cloud.tencent.com/cam/role). The role name is MySQL_QCSRole and the preset policy name is QcloudAccessForMySQLRole.
        4. Closing is not allowed after encryption being enabled.

        This API may take up to 10s, and the client may timeout. If the API call returns InternalError, please call [DescribeDBInstanceInfo](https://www.tencentcloud.com/document/product/236/44160?from_cn_redirect=1) to confirm whether backend encryption is successfully enabled. After calling, if the parameter Encryption is YES, it means activation is successful.

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
        r"""This API (OpenDBInstanceGTID) is used to enable GTID for a TencentDB instance. Only instances on or above version 5.6 are supported.

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


    def OpenSSL(self, request):
        r"""This API is used to enable SSL connectivity function.

        :param request: Request instance for OpenSSL.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenSSLRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenSSL", params, headers=headers)
            response = json.loads(body)
            model = models.OpenSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWanService(self, request):
        r"""This API (OpenWanService) is used to enable public network access for an instance.

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


    def ReleaseIsolatedDBInstances(self, request):
        r"""This API is used to restore isolated cloud database instances. It is only used for de-isolating pay-as-you-go instances. For monthly subscription instances, please use RenewDBInstance.

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
        r"""This API is used to rebalance the load on database proxy.

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
        r"""This API is used to renew cloud database instances. It supports yearly/monthly subscription instances. Pay-as-you-go instances can be renewed as yearly/monthly subscription instances through this API.

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


    def ResetPassword(self, request):
        r"""Manually refresh rotation passwords

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRootAccount(self, request):
        r"""This API is used to reset the root account and initialize the account permissions.

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
        r"""This API is used to restart cloud database instances.

        Note:
        This API supports performing a restart operation on primary instances, read-only instances, and disaster recovery instances.
        2. The instance status must be normal and no other async tasks are in progress.

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
        r"""This API (StartBatchRollback) is used to roll back the tables of a TencentDB instance in batches.

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


    def StartCpuExpand(self, request):
        r"""This API is used to enable CPU Elastic Scaling, including one-time manual scale-out and automatic elastic scaling.

        :param request: Request instance for StartCpuExpand.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartCpuExpandRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartCpuExpandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCpuExpand", params, headers=headers)
            response = json.loads(body)
            model = models.StartCpuExpandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartReplication(self, request):
        r"""This API is used to enable RO replication and sync data from the primary instance.

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


    def StopCpuExpand(self, request):
        r"""This API is used to disable elastic CPU expansion.

        :param request: Request instance for StopCpuExpand.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopCpuExpandRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopCpuExpandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCpuExpand", params, headers=headers)
            response = json.loads(body)
            model = models.StopCpuExpandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDBImportJob(self, request):
        r"""This API is used to terminate a data import task.
        Description: Only incomplete import jobs support termination, and the executed SQL part is retained after termination.

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
        r"""This API is used to stop RO replication and interrupt data sync from the primary instance.

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
        r"""This api is used to revoke an ongoing rollback task of an instance. The api response returns an Asynchronous Task ID. The revocation result can be queried through [DescribeAsyncRequestInfo](https://www.tencentcloud.com/document/api/236/20410?from_cn_redirect=1) for task execution.

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


    def SubmitInstanceUpgradeCheckJob(self, request):
        r"""This API is used to submit an instance version upgrade validation task.

        :param request: Request instance for SubmitInstanceUpgradeCheckJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SubmitInstanceUpgradeCheckJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SubmitInstanceUpgradeCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitInstanceUpgradeCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitInstanceUpgradeCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchCDBProxy(self, request):
        r"""This API is used to manually initiate an immediate switch after database proxy configuration modification or edition upgrade.

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
        r"""This API is used for source-to-replica switch.

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
        r"""This API is used to switch a cloud database disaster recovery instance to primary instance. Note that the request must be sent to the region where the disaster recovery instance is located.

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
        r"""This API (SwitchForUpgrade) is used to switch to a new instance. You can initiate this process when the primary instance being upgraded is pending switch.

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
        r"""This API is used to upgrade the database proxy version.

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
        r"""This API is used to upgrade or downgrade the configuration of a cloud database instance. Supported instance types include primary instance, disaster recovery instance and read-only instance. If you need to migrate business, fill in the instance specification (CPU, memory), otherwise the system will use the minimum allowed specification by default.

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
        r"""This API is used to upgrade the version of a cloud database instance. Supported instance types include primary instance, disaster recovery instance, and read-only instance. Before upgrade, submit an upgrade check task via SubmitInstanceUpgradeCheckJob (https://www.tencentcloud.com/document/product/236/110468?from_cn_redirect=1).

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