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
from tencentcloud.cdb.v20170320 import models
from typing import Dict


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.intl.tencentcloudapi.com'
    _service = 'cdb'

    async def AddTimeWindow(
            self,
            request: models.AddTimeWindowRequest,
            opts: Dict = None,
    ) -> models.AddTimeWindowResponse:
        """
        This API is used to add a maintenance time window for cloud database instances to specify which time periods allow automatic execution of access operations.
        """
        
        kwargs = {}
        kwargs["action"] = "AddTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustCdbProxy(
            self,
            request: models.AdjustCdbProxyRequest,
            opts: Dict = None,
    ) -> models.AdjustCdbProxyResponse:
        """
        This API is used to adjust database proxy configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustCdbProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustCdbProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustCdbProxyAddress(
            self,
            request: models.AdjustCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.AdjustCdbProxyAddressResponse:
        """
        This API is used to adjust the database proxy address configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AnalyzeAuditLogs(
            self,
            request: models.AnalyzeAuditLogsRequest,
            opts: Dict = None,
    ) -> models.AnalyzeAuditLogsResponse:
        """
        This API is used to perform aggregation statistics on specified data columns in audit log result sets with different filter criteria.
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeAuditLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeAuditLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API (AssociateSecurityGroups) is used to bind security groups to instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BalanceRoGroupLoad(
            self,
            request: models.BalanceRoGroupLoadRequest,
            opts: Dict = None,
    ) -> models.BalanceRoGroupLoadResponse:
        """
        This API is used to rebalance the loads of instances in an RO group. Please note that the database connections to those instances will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "BalanceRoGroupLoad"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BalanceRoGroupLoadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        This API is used to disable the audit service for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseCDBProxy(
            self,
            request: models.CloseCDBProxyRequest,
            opts: Dict = None,
    ) -> models.CloseCDBProxyResponse:
        """
        This API is used to disable the database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCDBProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCDBProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseCdbProxyAddress(
            self,
            request: models.CloseCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.CloseCdbProxyAddressResponse:
        """
        This API is used to disable database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        This API is used to close the SSL connectivity function.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWanService(
            self,
            request: models.CloseWanServiceRequest,
            opts: Dict = None,
    ) -> models.CloseWanServiceResponse:
        """
        This API (CloseWanService) is used to disable public network access for TencentDB instance, which will make public IP addresses inaccessible.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWanService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWanServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccounts(
            self,
            request: models.CreateAccountsRequest,
            opts: Dict = None,
    ) -> models.CreateAccountsResponse:
        """
        This API is used to create cloud database accounts. It requires specifying a new account name and domain name as well as the corresponding password. You can also set the account's remark information and maximum number of available connections.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditLogFile(
            self,
            request: models.CreateAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.CreateAuditLogFileResponse:
        """
        This API is used to create an audit log file for a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditPolicy(
            self,
            request: models.CreateAuditPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAuditPolicyResponse:
        """
        This API is used to create an audit policy for a TencentDB instance by associating an audit rule with the TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditRuleTemplate(
            self,
            request: models.CreateAuditRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAuditRuleTemplateResponse:
        """
        This API is used to create an audit rule template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        This API is used to create a database backup.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdbProxy(
            self,
            request: models.CreateCdbProxyRequest,
            opts: Dict = None,
    ) -> models.CreateCdbProxyResponse:
        """
        This API is used to create a database proxy for the primary instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdbProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdbProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdbProxyAddress(
            self,
            request: models.CreateCdbProxyAddressRequest,
            opts: Dict = None,
    ) -> models.CreateCdbProxyAddressResponse:
        """
        This API is used to add a proxy address for database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdbProxyAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloneInstance(
            self,
            request: models.CreateCloneInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCloneInstanceResponse:
        """
        This API is used to create a clone instance from the source instance. You can specify a physical backup file or a rollback time point for the clone instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloneInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloneInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBImportJob(
            self,
            request: models.CreateDBImportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDBImportJobResponse:
        """
        This API is used to create a cloud database data import task.
        Note that the file for the data import task must be uploaded to Tencent Cloud in advance. The user must perform file import on the console.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBImportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBImportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        This API is used to create a cloud database instance with an annual/monthly subscription, including primary instance, disaster recovery instance, and read-only instance. You can create a cloud database instance by importing instance specification, MySQL version number, purchase period, and quantity information.

        This API is an asynchronous API. You can also use the query instance list API (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) to query the instance details. When the Status of the instance is 1 and TaskStatus is 0, it means the instance has been delivered successfully.

        1. First, please use the API for the query (https://www.tencentcloud.com/document/api/236/17229?from_cn_redirect=1) to obtain the purchasable specifications of cloud databases, then please use the API for the query (https://www.tencentcloud.com/document/api/236/18566?from_cn_redirect=1) to query database price.
        2. You can create up to 100 instances at a time, with a maximum instance duration of 36 months.
        3. Support creating MySQL 5.5, MySQL 5.6, MySQL 5.7, and MySQL 8.0 versions.
        4. Support creating primary instance, read-only instance, disaster recovery instance.
        5. When ParamTemplateId or AlarmPolicyList is specified in the input parameters, you need to upgrade the SDK to the latest version to support it.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceHour(
            self,
            request: models.CreateDBInstanceHourRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceHourResponse:
        """
        This API is used to create pay-as-you-go instances. You can create a cloud database instance by inputting the instance specification, MySQL version number, quantity, etc. It supports the creation of primary instances, disaster recovery instances, and read-only instances.

        This API is an async API. You can also use the API for the query (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) to check the instance details. When the instance Status is 1 and TaskStatus is 0, it means the instance has been delivered successfully.

        1. First, please use the API for the query (https://www.tencentcloud.com/document/api/236/17229?from_cn_redirect=1) to obtain the purchasable specifications of cloud databases, then please use the API for the query (https://www.tencentcloud.com/document/api/236/18566?from_cn_redirect=1) to query the instance selling price.
        2. Supports a maximum of 100 instances created at a time, with a maximum duration of 36 months;
        3. Support creating MySQL 5.5, MySQL 5.6, MySQL 5.7, and MySQL 8.0 versions.
        4. Support creating primary instances, disaster recovery instances, and read-only instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabase(
            self,
            request: models.CreateDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseResponse:
        """
        This API is used to create a database in a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParamTemplate(
            self,
            request: models.CreateParamTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParamTemplateResponse:
        """
        This API is used to create a parameter template.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoInstanceIp(
            self,
            request: models.CreateRoInstanceIpRequest,
            opts: Dict = None,
    ) -> models.CreateRoInstanceIpResponse:
        """
        This API is used to create a VIP exclusive to a TencentDB read-only instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoInstanceIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoInstanceIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRotationPassword(
            self,
            request: models.CreateRotationPasswordRequest,
            opts: Dict = None,
    ) -> models.CreateRotationPasswordResponse:
        """
        This API is used to enable password rotation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRotationPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRotationPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccounts(
            self,
            request: models.DeleteAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountsResponse:
        """
        This API is used to delete CDB accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditLogFile(
            self,
            request: models.DeleteAuditLogFileRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditLogFileResponse:
        """
        This API is used to delete an audit log file of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditPolicy(
            self,
            request: models.DeleteAuditPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditPolicyResponse:
        """
        This API is used to delete an audit policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditRuleTemplates(
            self,
            request: models.DeleteAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditRuleTemplatesResponse:
        """
        This API is used to delete audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackup(
            self,
            request: models.DeleteBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupResponse:
        """
        This API is used to delete database backups. It only supports deleting manually initiated backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatabase(
            self,
            request: models.DeleteDatabaseRequest,
            opts: Dict = None,
    ) -> models.DeleteDatabaseResponse:
        """
        This API is used to delete a database in a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        This API is used to delete parameter template.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRotationPassword(
            self,
            request: models.DeleteRotationPasswordRequest,
            opts: Dict = None,
    ) -> models.DeleteRotationPasswordResponse:
        """
        This API is used to close instance account password rotation.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRotationPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRotationPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTimeWindow(
            self,
            request: models.DeleteTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DeleteTimeWindowResponse:
        """
        This API is used to delete the maintenance time window of a cloud database instance. After deleting the instance maintenance window, the default maintenance period is 03:00-04:00 daily with a data validation delay threshold of 10 seconds. When switching to a new instance during the maintenance time window, the switch is performed by default at 03:00-04:00.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        This API is used to query the permission information supported by a cloud database account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to query ALL account information of the cloud database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        This API (DescribeAsyncRequestInfo) is used to query the async task execution result of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditConfig(
            self,
            request: models.DescribeAuditConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditConfigResponse:
        """
        This API is used to query the service configurations for a TencentDB audit policy, including the audit log retention period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        This API is used to obtain the list of audit instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogFiles(
            self,
            request: models.DescribeAuditLogFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogFilesResponse:
        """
        This API is used to query the audit log files of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLogs(
            self,
            request: models.DescribeAuditLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogsResponse:
        """
        This API is used to query database audit logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditPolicies(
            self,
            request: models.DescribeAuditPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditPoliciesResponse:
        """
        This API is used to query audit policies of cloud database instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleTemplateModifyHistory(
            self,
            request: models.DescribeAuditRuleTemplateModifyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleTemplateModifyHistoryResponse:
        """
        This API is used to query the change history of rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleTemplateModifyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleTemplateModifyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleTemplates(
            self,
            request: models.DescribeAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleTemplatesResponse:
        """
        This API is used to query the information of audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRules(
            self,
            request: models.DescribeAuditRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRulesResponse:
        """
        This API is used to create audit rules no longer supported.

        This API is used to query audit rules in current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupConfig(
            self,
            request: models.DescribeBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupConfigResponse:
        """
        This API is used to query database backup configuration info.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDecryptionKey(
            self,
            request: models.DescribeBackupDecryptionKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDecryptionKeyResponse:
        """
        This API is used to query the decryption key of a backup file.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDecryptionKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDecryptionKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        This API is used to query the restrictions of downloading backups in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupEncryptionStatus(
            self,
            request: models.DescribeBackupEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupEncryptionStatusResponse:
        """
        This API is used to query the default encryption status of an instance backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupOverview(
            self,
            request: models.DescribeBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupOverviewResponse:
        """
        This API is used to query the backup overview of a user. It will return the user's current total number of backups, total capacity used by backups, capacity in the free tier, and paid capacity (all capacity values are in bytes).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummaries(
            self,
            request: models.DescribeBackupSummariesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummariesResponse:
        """
        This API is used to query backup statistics, return the occupied capacity of backups by instance as well as the count and capacity of data backup and log backup for each instance (in bytes).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackups(
            self,
            request: models.DescribeBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupsResponse:
        """
        This API (DescribeBackups) is used to query the backups of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogBackupOverview(
            self,
            request: models.DescribeBinlogBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogBackupOverviewResponse:
        """
        This API is used to query the log backup overview of a user in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogs(
            self,
            request: models.DescribeBinlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogsResponse:
        """
        This API is used to query the list of binlog files of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCPUExpandStrategyInfo(
            self,
            request: models.DescribeCPUExpandStrategyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCPUExpandStrategyInfoResponse:
        """
        This API is used to query the CPU Elastic Scaling information of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCPUExpandStrategyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCPUExpandStrategyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdbProxyInfo(
            self,
            request: models.DescribeCdbProxyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCdbProxyInfoResponse:
        """
        This API is used to query database proxy detailed information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdbProxyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdbProxyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdbZoneConfig(
            self,
            request: models.DescribeCdbZoneConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCdbZoneConfigResponse:
        """
        This API is used to query the purchasable specifications of TencentDB instances in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdbZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdbZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloneList(
            self,
            request: models.DescribeCloneListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloneListResponse:
        """
        This API is used to query the clone task list of a user instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInfo(
            self,
            request: models.DescribeClusterInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInfoResponse:
        """
        This API is used to query cloud disk edition instance info.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBFeatures(
            self,
            request: models.DescribeDBFeaturesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBFeaturesResponse:
        """
        This API is used to query cloud database version attributes, including whether database encryption and database audit are supported, and other features.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBFeatures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBFeaturesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBImportRecords(
            self,
            request: models.DescribeDBImportRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBImportRecordsResponse:
        """
        This API (DescribeDBImportRecords) is used to query the records of import tasks in a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBImportRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBImportRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceCharset(
            self,
            request: models.DescribeDBInstanceCharsetRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceCharsetResponse:
        """
        This API (DescribeDBInstanceCharset) is used to query the character set and its name of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceCharset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceCharsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceConfig(
            self,
            request: models.DescribeDBInstanceConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceConfigResponse:
        """
        This API is used to query the configuration message of a cloud database instance, including sync mode and deployment mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceGTID(
            self,
            request: models.DescribeDBInstanceGTIDRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceGTIDResponse:
        """
        This API (DescribeDBInstanceGTID) is used to query whether GTID is activated for a TencentDB instance. Instances on or below version 5.5 are not supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceGTID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceGTIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceInfo(
            self,
            request: models.DescribeDBInstanceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceInfoResponse:
        """
        This API is used to query the basic information of an instance, including instance ID, instance name, and whether encryption is enabled. Querying read-only instances is not supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceLogToCLS(
            self,
            request: models.DescribeDBInstanceLogToCLSRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceLogToCLSResponse:
        """
        This API is used to query the configuration of slow log and error log delivery to CLS for an instance. It filters out the present instance log delivery configuration to CLS by AppId, Region, and instance ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceLogToCLS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceLogToCLSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceRebootTime(
            self,
            request: models.DescribeDBInstanceRebootTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceRebootTimeResponse:
        """
        This API is used to query the expected time required to restart a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceRebootTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceRebootTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query the list of TencentDB for MySQL instances. It supports filtering instances by conditions such as project ID, instance ID, access address, and instance status. It also supports querying the list of information about primary instances, disaster recovery instances, and read-only instances.
        This API is used to return the availability zone (AZ) status during purchase, which does not change along with the proactive HA switch. If you want to know the AZ status in real time, query through the [DescribeDBInstanceConfig](https://www.tencentcloud.com/document/product/236/17491?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBPrice(
            self,
            request: models.DescribeDBPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeDBPriceResponse:
        """
        This API is used to query the price of purchasing or renewing a cloud database instance. It supports querying the price of pay-as-you-go or yearly/monthly subscription. You can input instance type, purchase period, purchase quantity, memory size, disk capacity and availability zone information to query instance price. You can input instance name to query instance renewal price.

        Note: To request a price for a certain region, please use the access point of the corresponding region. For access point information, please refer to the <a href="https://www.tencentcloud.com/document/api/236/15832?from_cn_redirect=1">service address</a> document. For example, to request a price for the Guangzhou region, send the request to: cdb.ap-guangzhou.tencentcloudapi.com. Likewise, for the Shanghai region, send the request to: cdb.ap-shanghai.tencentcloudapi.com.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API (DescribeDBSecurityGroups) is used to query the security group details of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSwitchRecords(
            self,
            request: models.DescribeDBSwitchRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSwitchRecordsResponse:
        """
        This API (DescribeDBSwitchRecords) is used to query the instance switch records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSwitchRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSwitchRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataBackupOverview(
            self,
            request: models.DescribeDataBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDataBackupOverviewResponse:
        """
        This API is used to query the data backup overview of a user in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        This API is used to query the information of databases in a TencentDB instance which must be a source or disaster recovery instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultParams(
            self,
            request: models.DescribeDefaultParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultParamsResponse:
        """
        This API (DescribeDefaultParams) is used to query the list of default configurable parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceMonitorInfo(
            self,
            request: models.DescribeDeviceMonitorInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceMonitorInfoResponse:
        """
        This API (DescribeDeviceMonitorInfo) is used to query the monitoring information of a TencentDB physical machine on the day. Currently, it only supports instances with 488 GB memory and 6 TB disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceMonitorInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceMonitorInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorLogData(
            self,
            request: models.DescribeErrorLogDataRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorLogDataResponse:
        """
        This API is used to query the error logs of an instance over the past month by search criteria.
        Note: the HTTP response packet will be very large if it contain a single large error log, which causes the API call to time out. If this happens, we recommend you lower the value of the input parameter `Limit` to reduce the packet size so that the API can respond timely.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorLogData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorLogDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAlarmEvents(
            self,
            request: models.DescribeInstanceAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAlarmEventsResponse:
        """
        This API is used to query event information of instance occurrence.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAlarmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        This API (DescribeInstanceParamRecords) is used to query the parameter modification records of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParamRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        This API (DescribeInstanceParams) is used to query the list of parameters for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancePasswordComplexity(
            self,
            request: models.DescribeInstancePasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancePasswordComplexityResponse:
        """
        This API is used to query the password complexity parameter list of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancePasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancePasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUpgradeCheckJob(
            self,
            request: models.DescribeInstanceUpgradeCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUpgradeCheckJobResponse:
        """
        This API is used to query the instance version upgrade validation task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUpgradeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUpgradeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUpgradeType(
            self,
            request: models.DescribeInstanceUpgradeTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUpgradeTypeResponse:
        """
        This API is used to query the upgrade type of a database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUpgradeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUpgradeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLocalBinlogConfig(
            self,
            request: models.DescribeLocalBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLocalBinlogConfigResponse:
        """
        This API is used to query the retention policy of local binlog of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLocalBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLocalBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateInfo(
            self,
            request: models.DescribeParamTemplateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateInfoResponse:
        """
        This API is used to query parameter template details.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplates(
            self,
            request: models.DescribeParamTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplatesResponse:
        """
        This API is used to query the parameter template list.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        This API (DescribeProjectSecurityGroups) is used to query the security group details of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyCustomConf(
            self,
            request: models.DescribeProxyCustomConfRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyCustomConfResponse:
        """
        This API is used to query the proxy configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyCustomConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyCustomConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySupportParam(
            self,
            request: models.DescribeProxySupportParamRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySupportParamResponse:
        """
        This API is used to query instance support proxy version and parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySupportParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySupportParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRemoteBackupConfig(
            self,
            request: models.DescribeRemoteBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeRemoteBackupConfigResponse:
        """
        This API is used to query the configuration information of a remote TencentDB instance backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRemoteBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRemoteBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoGroups(
            self,
            request: models.DescribeRoGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRoGroupsResponse:
        """
        This API is used to query all RO groups of a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoMinScale(
            self,
            request: models.DescribeRoMinScaleRequest,
            opts: Dict = None,
    ) -> models.DescribeRoMinScaleResponse:
        """
        This API is used to query the minimum specification of a read-only instance that can be purchased or upgraded to.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoMinScale"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoMinScaleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackRangeTime(
            self,
            request: models.DescribeRollbackRangeTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackRangeTimeResponse:
        """
        This API (DescribeRollbackRangeTime) is used to query the time range available for instance rollback.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackRangeTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackRangeTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTaskDetail(
            self,
            request: models.DescribeRollbackTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTaskDetailResponse:
        """
        This API is used to query the rollback task detail of a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSLStatus(
            self,
            request: models.DescribeSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSSLStatusResponse:
        """
        This API is used to query SSL activation status. If SSL has been enabled, it will synchronously return the certificate download URL.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogData(
            self,
            request: models.DescribeSlowLogDataRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogDataResponse:
        """
        This API is used to search for instance slow logs under usage conditions. Only allow viewing slow logs within one month.
        During use, pay attention: a single slow log may be too large, causing the entire http request return content to be too large, furthermore leading to API timeout. Once timed out, narrow down the Limit parameter value when querying, thereby reducing the size and enabling the API to return content promptly.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        This API is used to obtain the slow query log of a cloud database instance.
        Description: If the data volume is too large in a single query, it may lead to response timeout. We recommend shortening the query time range per request, such as one hour, to avoid timeout.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedPrivileges(
            self,
            request: models.DescribeSupportedPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedPrivilegesResponse:
        """
        This API (DescribeSupportedPrivileges) is used to query the information of TencentDB account permissions, including global permissions, database permissions, table permissions, and column permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableColumns(
            self,
            request: models.DescribeTableColumnsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableColumnsResponse:
        """
        This API is used to query table column information of a designated database in a cloud database instance. It only supports primary instance and disaster recovery instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableColumns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableColumnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        This API is used to query the information of database tables in a TencentDB instance. It only supports source or disaster recovery instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagsOfInstanceIds(
            self,
            request: models.DescribeTagsOfInstanceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsOfInstanceIdsResponse:
        """
        This API is used to access tag information of the instance for cloud databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagsOfInstanceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsOfInstanceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        This API (DescribeTasks) is used to query the list of tasks for a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeWindow(
            self,
            request: models.DescribeTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeWindowResponse:
        """
        This API (DescribeTimeWindow) is used to query the maintenance time window of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadedFiles(
            self,
            request: models.DescribeUploadedFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadedFilesResponse:
        """
        This API is used to query the list of SQL files imported by users. The common request parameter `Region` must be `ap-shanghai`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadedFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadedFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API (DisassociateSecurityGroups) is used to unbind security groups from instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        This API is used to isolate a cloud database instance. After an instance is isolated, you cannot access the database via IP and port. The isolated instance can be started in the recycle bin. If the instance is isolated due to arrears, please recharge as soon as possible.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        This API (ModifyAccountDescription) is used to modify the remarks of a TencentDB instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountMaxUserConnections(
            self,
            request: models.ModifyAccountMaxUserConnectionsRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountMaxUserConnectionsResponse:
        """
        This API is used to modify the maximum number of available connections for a cloud database account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountMaxUserConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountMaxUserConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPassword(
            self,
            request: models.ModifyAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPasswordResponse:
        """
        This API (ModifyAccountPassword) is used to modify the password of a TencentDB instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        This API is used to modify the permissions of a TencentDB instance account.

        Note that when modifying account permissions, you need to pass in the full permission information of the account. You can [query the account permission information
        ](https://intl.cloud.tencent.com/document/api/236/17500?from_cn_redirect=1) first before modifying permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditConfig(
            self,
            request: models.ModifyAuditConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditConfigResponse:
        """
        This API is used to modify the service configurations for a TencentDB audit policy, including the audit log retention period.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditRuleTemplates(
            self,
            request: models.ModifyAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditRuleTemplatesResponse:
        """
        This API is used to modify audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        This API is used to modify the service configurations for a TencentDB instance, including the audit log retention period and the audit rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        This API is used to modify the auto-renewal flag of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupConfig(
            self,
            request: models.ModifyBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupConfigResponse:
        """
        This API is used to modify database backup configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        This API is used to modify the restrictions of downloading backups in a region. You can specify which types of networks (private, or both private and public), VPCs, and IPs to download backups.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupEncryptionStatus(
            self,
            request: models.ModifyBackupEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupEncryptionStatusResponse:
        """
        This API is used to set the encryption status of an instance backup.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyAddressDesc(
            self,
            request: models.ModifyCdbProxyAddressDescRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyAddressDescResponse:
        """
        This API is used to modify the proxy address description.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyAddressDesc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyAddressDescResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyAddressVipAndVPort(
            self,
            request: models.ModifyCdbProxyAddressVipAndVPortRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyAddressVipAndVPortResponse:
        """
        This API is used to modify the database proxy address VPC information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyAddressVipAndVPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyAddressVipAndVPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdbProxyParam(
            self,
            request: models.ModifyCdbProxyParamRequest,
            opts: Dict = None,
    ) -> models.ModifyCdbProxyParamResponse:
        """
        This API is used to configure database proxy parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdbProxyParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdbProxyParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceLogToCLS(
            self,
            request: models.ModifyDBInstanceLogToCLSRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceLogToCLSResponse:
        """
        This API is used to enable or disable the feature of sending CDB slow and error logs to CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceLogToCLS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceLogToCLSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceModes(
            self,
            request: models.ModifyDBInstanceModesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceModesResponse:
        """
        This API is used to change the mode of a cloud database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceModes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceModesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        This API (ModifyDBInstanceName) is used to rename a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceProject(
            self,
            request: models.ModifyDBInstanceProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceProjectResponse:
        """
        This API (ModifyDBInstanceProject) is used to modify the project to which a TencentDB instance belongs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API (ModifyDBInstanceSecurityGroups) is used to modify the security groups bound to a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceVipVport(
            self,
            request: models.ModifyDBInstanceVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceVipVportResponse:
        """
        This API is used to modify the IP and port number of a cloud database instance. It can also perform basic network to VPC network and subnet change under VPC network.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParam(
            self,
            request: models.ModifyInstanceParamRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamResponse:
        """
        This API (ModifyInstanceParam) is used to modify instance parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePasswordComplexity(
            self,
            request: models.ModifyInstancePasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePasswordComplexityResponse:
        """
        This API is used to modify the password complexity of a cloud database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceTag(
            self,
            request: models.ModifyInstanceTagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceTagResponse:
        """
        This API (ModifyInstanceTag) is used to add, modify, or delete an instance tag.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLocalBinlogConfig(
            self,
            request: models.ModifyLocalBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLocalBinlogConfigResponse:
        """
        This API is used to modify the local binlog retention policy of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLocalBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLocalBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNameOrDescByDpId(
            self,
            request: models.ModifyNameOrDescByDpIdRequest,
            opts: Dict = None,
    ) -> models.ModifyNameOrDescByDpIdResponse:
        """
        This API is used to modify the name or description of a placement group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNameOrDescByDpId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNameOrDescByDpIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        This API is used to modify parameter templates.
        Description: The parameter template is a common component, effective across all regions once configured. For api calls, Guangzhou or Singapore is available to configure region.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectMode(
            self,
            request: models.ModifyProtectModeRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectModeResponse:
        """
        This API is used to modify the sync method of an instance.
        Description: This API can be called only by an exclusive cluster. This API is about to go offline.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRemoteBackupConfig(
            self,
            request: models.ModifyRemoteBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyRemoteBackupConfigResponse:
        """
        This API is used to modify the configuration information of a remote TencentDB instance backup.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRemoteBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRemoteBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoGroupInfo(
            self,
            request: models.ModifyRoGroupInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyRoGroupInfoResponse:
        """
        This API is used to update the information of a TencentDB RO group, such as configuring a read-only instance removal policy in case of excessive delay, setting read weights of read-only instances, and setting the replication delay.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoGroupVipVport(
            self,
            request: models.ModifyRoGroupVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyRoGroupVipVportResponse:
        """
        This API is used to modify the vip and vport of a Ro group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoGroupVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoGroupVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTimeWindow(
            self,
            request: models.ModifyTimeWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyTimeWindowResponse:
        """
        This API (ModifyTimeWindow) is used to update the maintenance time window of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTimeWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTimeWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedInstances(
            self,
            request: models.OfflineIsolatedInstancesRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedInstancesResponse:
        """
        This api is used to deactivate cloud database instances in quarantined state now. The instance Status for row operations must be quarantined state, such as instances with Status value 5 queried through the query instance list api.

        This API is used to perform asynchronous operation, and delays may occur when reclaiming partial resources. You can query by using the query instance list API (https://www.tencentcloud.com/document/api/236/15872?from_cn_redirect=1) with specified instance InstanceId and status Status as [5,6,7]. Among them, 5 represents isolated, 6 represents offline, and 7 represents Offline. If the return instance is empty, all instance resources have been released.

        Note that after the instance goes offline, relevant resources and data cannot be recovered. Proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        This API is used to activate audit service for CDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBInstanceEncryption(
            self,
            request: models.OpenDBInstanceEncryptionRequest,
            opts: Dict = None,
    ) -> models.OpenDBInstanceEncryptionResponse:
        """
        This API is used to enable data storage encryption for instance and support users to specify custom keys.

        Note that before enabling data storage encryption for instance, perform the following operations:

        1. Perform instance initialization (https://www.tencentcloud.com/document/api/236/15873?from_cn_redirect=1).

        2. Enable the KMS service (https://console.cloud.tencent.com/kms2).

        3. Grant the cloud database (MySQL) permission to access the KMS key (https://console.cloud.tencent.com/cam/role). The role name is MySQL_QCSRole and the preset policy name is QcloudAccessForMySQLRole.
        4. Closing is not allowed after encryption being enabled.

        This API may take up to 10s, and the client may timeout. If the API call returns InternalError, please call [DescribeDBInstanceInfo](https://www.tencentcloud.com/document/product/236/44160?from_cn_redirect=1) to confirm whether backend encryption is successfully enabled. After calling, if the parameter Encryption is YES, it means activation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBInstanceEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBInstanceEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBInstanceGTID(
            self,
            request: models.OpenDBInstanceGTIDRequest,
            opts: Dict = None,
    ) -> models.OpenDBInstanceGTIDResponse:
        """
        This API (OpenDBInstanceGTID) is used to enable GTID for a TencentDB instance. Only instances on or above version 5.6 are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBInstanceGTID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBInstanceGTIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSSL(
            self,
            request: models.OpenSSLRequest,
            opts: Dict = None,
    ) -> models.OpenSSLResponse:
        """
        This API is used to enable SSL connectivity function.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWanService(
            self,
            request: models.OpenWanServiceRequest,
            opts: Dict = None,
    ) -> models.OpenWanServiceResponse:
        """
        This API (OpenWanService) is used to enable public network access for an instance.

        Note that before enabling public network access, you need to first [initialize the instance](https://intl.cloud.tencent.com/document/api/236/15873?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWanService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWanServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIsolatedDBInstances(
            self,
            request: models.ReleaseIsolatedDBInstancesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIsolatedDBInstancesResponse:
        """
        This API is used to restore isolated cloud database instances. It is only used for de-isolating pay-as-you-go instances. For monthly subscription instances, please use RenewDBInstance.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIsolatedDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIsolatedDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReloadBalanceProxyNode(
            self,
            request: models.ReloadBalanceProxyNodeRequest,
            opts: Dict = None,
    ) -> models.ReloadBalanceProxyNodeResponse:
        """
        This API is used to rebalance the load on database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "ReloadBalanceProxyNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReloadBalanceProxyNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBInstance(
            self,
            request: models.RenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstanceResponse:
        """
        This API is used to renew cloud database instances. It supports yearly/monthly subscription instances. Pay-as-you-go instances can be renewed as yearly/monthly subscription instances through this API.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        Manually refresh rotation passwords
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRootAccount(
            self,
            request: models.ResetRootAccountRequest,
            opts: Dict = None,
    ) -> models.ResetRootAccountResponse:
        """
        This API is used to reset the root account and initialize the account permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRootAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRootAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstances(
            self,
            request: models.RestartDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstancesResponse:
        """
        This API is used to restart cloud database instances.

        Note:
        This API supports performing a restart operation on primary instances, read-only instances, and disaster recovery instances.
        2. The instance status must be normal and no other async tasks are in progress.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBatchRollback(
            self,
            request: models.StartBatchRollbackRequest,
            opts: Dict = None,
    ) -> models.StartBatchRollbackResponse:
        """
        This API (StartBatchRollback) is used to roll back the tables of a TencentDB instance in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "StartBatchRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBatchRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCpuExpand(
            self,
            request: models.StartCpuExpandRequest,
            opts: Dict = None,
    ) -> models.StartCpuExpandResponse:
        """
        This API is used to enable CPU Elastic Scaling, including one-time manual scale-out and automatic elastic scaling.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCpuExpand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCpuExpandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartReplication(
            self,
            request: models.StartReplicationRequest,
            opts: Dict = None,
    ) -> models.StartReplicationResponse:
        """
        This API is used to enable RO replication and sync data from the primary instance.
        """
        
        kwargs = {}
        kwargs["action"] = "StartReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCpuExpand(
            self,
            request: models.StopCpuExpandRequest,
            opts: Dict = None,
    ) -> models.StopCpuExpandResponse:
        """
        This API is used to disable elastic CPU expansion.
        """
        
        kwargs = {}
        kwargs["action"] = "StopCpuExpand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCpuExpandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopDBImportJob(
            self,
            request: models.StopDBImportJobRequest,
            opts: Dict = None,
    ) -> models.StopDBImportJobResponse:
        """
        This API is used to terminate a data import task.
        Description: Only incomplete import jobs support termination, and the executed SQL part is retained after termination.
        """
        
        kwargs = {}
        kwargs["action"] = "StopDBImportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopDBImportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopReplication(
            self,
            request: models.StopReplicationRequest,
            opts: Dict = None,
    ) -> models.StopReplicationResponse:
        """
        This API is used to stop RO replication and interrupt data sync from the primary instance.
        """
        
        kwargs = {}
        kwargs["action"] = "StopReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRollback(
            self,
            request: models.StopRollbackRequest,
            opts: Dict = None,
    ) -> models.StopRollbackResponse:
        """
        This api is used to revoke an ongoing rollback task of an instance. The api response returns an Asynchronous Task ID. The revocation result can be queried through [DescribeAsyncRequestInfo](https://www.tencentcloud.com/document/api/236/20410?from_cn_redirect=1) for task execution.
        """
        
        kwargs = {}
        kwargs["action"] = "StopRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitInstanceUpgradeCheckJob(
            self,
            request: models.SubmitInstanceUpgradeCheckJobRequest,
            opts: Dict = None,
    ) -> models.SubmitInstanceUpgradeCheckJobResponse:
        """
        This API is used to submit an instance version upgrade validation task.
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitInstanceUpgradeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitInstanceUpgradeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchCDBProxy(
            self,
            request: models.SwitchCDBProxyRequest,
            opts: Dict = None,
    ) -> models.SwitchCDBProxyResponse:
        """
        This API is used to manually initiate an immediate switch after database proxy configuration modification or edition upgrade.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchCDBProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchCDBProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstanceMasterSlave(
            self,
            request: models.SwitchDBInstanceMasterSlaveRequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstanceMasterSlaveResponse:
        """
        This API is used for source-to-replica switch.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDBInstanceMasterSlave"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDBInstanceMasterSlaveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDrInstanceToMaster(
            self,
            request: models.SwitchDrInstanceToMasterRequest,
            opts: Dict = None,
    ) -> models.SwitchDrInstanceToMasterResponse:
        """
        This API is used to switch a cloud database disaster recovery instance to primary instance. Note that the request must be sent to the region where the disaster recovery instance is located.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDrInstanceToMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDrInstanceToMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchForUpgrade(
            self,
            request: models.SwitchForUpgradeRequest,
            opts: Dict = None,
    ) -> models.SwitchForUpgradeResponse:
        """
        This API (SwitchForUpgrade) is used to switch to a new instance. You can initiate this process when the primary instance being upgraded is pending switch.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchForUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchForUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeCDBProxyVersion(
            self,
            request: models.UpgradeCDBProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeCDBProxyVersionResponse:
        """
        This API is used to upgrade the database proxy version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeCDBProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeCDBProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        This API is used to upgrade or downgrade the configuration of a cloud database instance. Supported instance types include primary instance, disaster recovery instance and read-only instance. If you need to migrate business, fill in the instance specification (CPU, memory), otherwise the system will use the minimum allowed specification by default.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceEngineVersion(
            self,
            request: models.UpgradeDBInstanceEngineVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceEngineVersionResponse:
        """
        This API is used to upgrade the version of a cloud database instance. Supported instance types include primary instance, disaster recovery instance, and read-only instance. Before upgrade, submit an upgrade check task via SubmitInstanceUpgradeCheckJob (https://www.tencentcloud.com/document/product/236/110468?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceEngineVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceEngineVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)