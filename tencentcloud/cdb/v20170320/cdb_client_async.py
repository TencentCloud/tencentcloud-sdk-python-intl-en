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
        This API (AddTimeWindow) is used to add a maintenance time window for a TencentDB instance, so as to specify when the instance can automatically perform access switch operations.
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
        This API is used to adjust the configuration of database proxy.
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
        This API is used to adjust the database proxy address.
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
        This API is used to aggregate the audit logs filtered by different conditions and aggregate the statistics of the specified data rows.
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
        
    async def CloseCDBProxy(
            self,
            request: models.CloseCDBProxyRequest,
            opts: Dict = None,
    ) -> models.CloseCDBProxyResponse:
        """
        This API is used to disable database proxy.
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
        This API is used to disable the database proxy address.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCdbProxyAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCdbProxyAddressResponse
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
        This API is used to create a TencentDB account. The account name, host address, and password are required. Account remarks and maximum connections can also be configured.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountsResponse
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
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        This API (CreateBackup) is used to create a TencentDB instance backup.
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
        This API is used create a database proxy for a source instance.
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
        This API is used to create a database proxy address.
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
        This API is used to create a clone of a specific instance, and roll back the clone by using a physical backup file of the instance or roll back the clone to a point in time.
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
        This API (CreateDBImportJob) is used to create a data import task for a TencentDB instance.

        Note that the files for a data import task must be uploaded to Tencent Cloud in advance. You need to do so in the console.
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
        This API is used to create a monthly subscribed TencentDB instance (which can be a source, disaster recovery, or read-only instance) by passing in information such as instance specifications, MySQL version number, purchased duration, and quantity.

        This is an asynchronous API. You can also use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance details. If the output parameter `Status` is `1` and the output parameter `TaskStatus` is `0`, the instance has been successfully delivered.

        1. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the purchasable instance specifications, and then use the [DescribeDBPrice](https://intl.cloud.tencent.com/document/api/236/18566?from_cn_redirect=1) API to query the prices of the purchasable instances.
        2. You can create up to 100 instances at a time, with an instance validity period of up to 36 months.
        3. MySQL v5.5, v5.6, v5.7, and v8.0 are supported.
        4. Source instances, read-only instances, and disaster recovery instances can be created.
        5. If `Port`, `ParamList`, or `Password` is specified in the input parameters, the instance (excluding basic instances) will be initialized.
        6. If `Port`, `ParamTemplateId`, or `AlarmPolicyList` is specified in the input parameters, you need to update your SDK to the latest version.
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
        This API is used to create a pay-as-you-go TencentDB instance (which can be a source, disaster recovery, or read-only instance) by passing in information such as instance specifications, MySQL version number, and quantity.

        This is an async API. You can also use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance details. If the `Status` value of an instance is `1` and `TaskStatus` is `0`, the instance has been successfully delivered.

        1. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the purchasable instance specifications, and then use the [DescribeDBPrice](https://intl.cloud.tencent.com/document/api/236/18566?from_cn_redirect=1) API to query the prices of the purchasable instances.
        2. You can create up to 100 instances at a time, with an instance validity period of up to 36 months.
        3. MySQL 5.5, 5.6, 5.7, and 8.0 are supported.
        4. Source instances, disaster recovery instances, and read-only instances can be created.
        5. If `Port`, `ParamList`, or `Password` is specified in the input parameters, the instance will be initialized.
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
        This API is used to create a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.
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
        
    async def DeleteAccounts(
            self,
            request: models.DeleteAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountsResponse:
        """
        This API (DeleteAccounts) is used to delete TencentDB accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackup(
            self,
            request: models.DeleteBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupResponse:
        """
        This API is used to delete a database backup. It can only delete manually initiated backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        This API is used to delete a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTimeWindow(
            self,
            request: models.DeleteTimeWindowRequest,
            opts: Dict = None,
    ) -> models.DeleteTimeWindowResponse:
        """
        This API (DeleteTimeWindow) is used to delete a maintenance time window for a TencentDB instance. After it is deleted, the default maintenance time window will be 03:00-04:00, i.e., switch to a new instance will be performed during 03:00-04:00 by default.
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
        This API (DescribeAccountPrivileges) is used to query the information of TencentDB account permissions.
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
        This API is used to query information of all TencentDB accounts.
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
        
    async def DescribeAuditLogs(
            self,
            request: models.DescribeAuditLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogsResponse:
        """
        This API is used to query a database audit log.
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
        This API is used to query the audit policies of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRules(
            self,
            request: models.DescribeAuditRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRulesResponse:
        """
        This API is used to query the audit rules in the current region.
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
        This API (DescribeBackupConfig) is used to query the configuration information of a TencentDB instance backup.
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
        This API is used to query the statistics of backups. It will return the capacity used by backups at the instance level and the number and used capacity of data backups and log backups of each instance (all capacity values are in bytes).
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
        
    async def DescribeCdbProxyInfo(
            self,
            request: models.DescribeCdbProxyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCdbProxyInfoResponse:
        """
        This API is used to query the details of a database proxy.
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
        This API is used to query the clone task list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCpuExpandStrategy(
            self,
            request: models.DescribeCpuExpandStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeCpuExpandStrategyResponse:
        """
        This API is used to query the elastic expansion policy of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCpuExpandStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCpuExpandStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBFeatures(
            self,
            request: models.DescribeDBFeaturesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBFeaturesResponse:
        """
        This API is used to query database version attributes, including supported features such as database encryption and audit.
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
        This API (DescribeDBInstanceConfig) is used to query the configuration information of a TencentDB instance, such as its synchronization mode and deployment mode.
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
        This API is used to query the basic information of an instance (instance ID, instance name, and whether encryption is enabled).
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
        The API DescribeDBInstanceLogToCLS is used to query the configurations of sending slow and error logs of an instance (InstanceId) filtered by AppId and Region to Cloud Log Service (CLS).
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
        This API (DescribeDBInstanceRebootTime) is used to query the estimated time needed for a TencentDB instance to restart.
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
        This API is used to return the availability zone (AZ) status during purchase, which does not change along with the proactive HA switch. If you want to know the AZ status in real time, query through the [DescribeDBInstanceConfig](https://www.tencentcloud.comom/document/product/236/17491?from_cn_redirect=1) API.
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
        This API is used to query the purchase or renewal price of a pay-as-you-go or monthly subscribed TencentDB instance by passing in information such as instance type, purchase duration, number of instances to purchase, memory size, disk size, and AZ. For the price of instance renewal, you can pass in instance name to query.

        Note: To query prices in a specific region, you need to use the access point of the region. For more information on access points, see <a href="https://www.tencentcloud.com/document/product/236/15832">Service Address</a>. For example, to query prices in Guangzhou, send a request to: cdb.ap-guangzhou.tencentcloudapi.com. Likewise, to query prices in Shanghai, send a request to: cdb.ap-shanghai.tencentcloudapi.com.
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
        This API is used to query parameter template details. The common request parameter `Region` can only be set to `ap-guangzhou`.
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
        This API is used to query the parameter template list. The common request parameter `Region` can only be set to `ap-guangzhou`.
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
        This API is used to query the supported proxy versions and parameters for an instance.
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
        This API is used to query the information of all RO groups of a TencentDB instance.
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
        This API is used to query the details of a TencentDB instance rollback task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogData(
            self,
            request: models.DescribeSlowLogDataRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogDataResponse:
        """
        This API is used to query the slow logs of an instance over the past month by search criteria.
        Note: the HTTP response packet will be very large if it contain a single large slow log, which causes the API call to time out. If this happens, we recommend you lower the value of the input parameter `Limit` to reduce the packet size so that the API can respond timely.
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
        The API DescribeSlowLogs is used to obtain slow query logs of a cloud database (CDB) instance. Note: If the size of logs to be queried is too large, the operation may time out. It is recommended that you select a shorter time range, such as one hour.
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
        This API (DescribeTagsOfInstanceIds) is used to query the tag information of a TencentDB instance.
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
        This API is used to isolate a TencentDB instance, which will no longer be accessible via IP and port. The isolated instance can be started up in the recycle bin. If it is isolated due to arrears, please top up your account as soon as possible.
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
        This API is used to modify the maximum connections of one or more TencentDB instance accounts.
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
        This API (ModifyBackupConfig) is used to modify the database backup configuration.
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
        This API is used to modify the description of a proxy address.
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
        This API is used to modify the VPC of the database proxy address.
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
        This API is used to configure the database proxy parameters.
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
        This API is used to modify the IP and port number of a TencentDB instance, switch from classic network to VPC, or change VPC subnets.
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
        This API is used to modify the password complexity of a TencentDB instance.
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
        This API is used to modify the retention policy of local binlog of an instance.
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
        This API is used to modify a parameter template. The common request parameter `Region` can only be set to `ap-guangzhou`.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
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
        This API (OfflineIsolatedInstances) is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status, i.e., their `Status` value is 5 in the return of the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1).

        This is an asynchronous API. There may be a delay in repossessing some resources. You can query the details by using the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) and specifying the InstanceId and the `Status` value as [5, 6, 7]. If the returned instance is empty, then all its resources have been released.

        Note that once an instance is deactivated, its resources and data will not be recoverable. Please do so with caution.
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
        This API is used to enable the audit service.
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
        This API is used to enable the encryption feature for instance data storage, and custom keys are supported.

        Note: Before enabling data storage encryption for an instance, you need to perform the following operations:

        1. [Initialize an instance](https://intl.cloud.tencent.com/document/api/236/15873?from_cn_redirect=1).

        2. Enable [KMS service](https://console.cloud.tencent.com/kms2)

        3. [Grant permission to access KMS](https://console.cloud.tencent.com/cam/role) for TencentDB for MySQL. The role name is `MySQL_QCSRole`, and the preset policy name is `QcloudAccessForMySQLRole`.

        This API calling may take up to 10 seconds, causing the client to time out. If it returns `InternalError`, call `DescribeDBInstanceInfo` to confirm whether the backend encryption is enabled successfully.
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
        This API is used to deisolate an isolated TencentDB instance.
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
        This API is used to renew a monthly subscribed TencentDB instance, and a pay-as-you-go instance can be renewed as a monthly subscribed one by this API.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstanceResponse
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
        This API (RestartDBInstances) is used to restart TencentDB instances.

        Note:
        1. This API only supports restarting primary instances.
        2. The instance status must be normal, and no other async tasks are in progress.
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
        u200cThis API is used to enable elastic CPU expansion manually or automatically.
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
        This API is used to start the data replication from the source instance to the read-only instance.
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
        This API (StopDBImportJob) is used to stop a data import task.
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
        This API is used to stop the data replication from the source instance to the read-only instance.
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
        This API is used to cancel a rollback task in progress, and returns an async task ID. You can use the `DescribeAsyncRequestInfo` API to query the result of cancellation.
        """
        
        kwargs = {}
        kwargs["action"] = "StopRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchCDBProxy(
            self,
            request: models.SwitchCDBProxyRequest,
            opts: Dict = None,
    ) -> models.SwitchCDBProxyResponse:
        """
        This API is used to switch database proxy after the proxy configuration is modified or the proxy version is upgraded.
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
        This API is used to promote a disaster recovery instance to source instance. The request parameter `Region` must be the region of the disaster recovery instance.
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
        This API is used to upgrade the version of database proxy.
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
        This API is used to upgrade or downgrade a TencentDB instance, which can be a primary instance, disaster recovery instance, or read-only instance.
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
        This API (UpgradeDBInstanceEngineVersion) is used to upgrade the version of a TencentDB instance, which can be a primary instance, disaster recovery instance, or read-only instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceEngineVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceEngineVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)