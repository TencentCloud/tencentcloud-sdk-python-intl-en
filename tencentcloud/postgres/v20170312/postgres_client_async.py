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
from tencentcloud.postgres.v20170312 import models
from typing import Dict


class PostgresClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'postgres.intl.tencentcloudapi.com'
    _service = 'postgres'

    async def AddDBInstanceToReadOnlyGroup(
            self,
            request: models.AddDBInstanceToReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.AddDBInstanceToReadOnlyGroupResponse:
        """
        This API is used to add a read-only replica to an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddDBInstanceToReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDBInstanceToReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneDBInstance(
            self,
            request: models.CloneDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CloneDBInstanceResponse:
        """
        This API is used to clone an instance by specifying a backup set or a point in time.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseDBExtranetAccess(
            self,
            request: models.CloseDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.CloseDBExtranetAccessResponse:
        """
        This API is used to disable the public network address of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseServerlessDBExtranetAccess(
            self,
            request: models.CloseServerlessDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.CloseServerlessDBExtranetAccessResponse:
        """
        This API is used to disable the public network address of a PostgreSQL for Serverless instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseServerlessDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseServerlessDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaseBackup(
            self,
            request: models.CreateBaseBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBaseBackupResponse:
        """
        This API is used to create a data backup of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaseBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaseBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceNetworkAccess(
            self,
            request: models.CreateDBInstanceNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceNetworkAccessResponse:
        """
        This API is used to create a network for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstances(
            self,
            request: models.CreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstancesResponse:
        """
        This API is used to create (but not initialize) one or more TencentDB for PostgreSQL instances. This API is disused and replaced by the [CreateInstances](https://intl.cloud.tencent.com/document/api/409/56107?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        This API is used to create one or more PostgreSQL instances. Instances created through this interface do not need to be initialized and can be used directly.
        <li>After an instance is successfully created, it will automatically start up, and its status changes to "Running".</li>
        <li>For prepaid instances, the required amount for the instance purchase will be deducted in advance. For post-paid hourly instances, the amount required for the purchase within the first hour will be temporarily frozen. Please ensure that your account balance is sufficient before calling this interface.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParameterTemplate(
            self,
            request: models.CreateParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParameterTemplateResponse:
        """
        This API is used to create a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyDBInstance(
            self,
            request: models.CreateReadOnlyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyDBInstanceResponse:
        """
        This API is used to create read-only replicas.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyGroup(
            self,
            request: models.CreateReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyGroupResponse:
        """
        This API is used to create an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyGroupNetworkAccess(
            self,
            request: models.CreateReadOnlyGroupNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyGroupNetworkAccessResponse:
        """
        This API is used to create a network for an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyGroupNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyGroupNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServerlessDBInstance(
            self,
            request: models.CreateServerlessDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateServerlessDBInstanceResponse:
        """
        This API is used to create a PostgreSQL for Serverless instance. If the creation succeeds, the instance ID will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServerlessDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServerlessDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaseBackup(
            self,
            request: models.DeleteBaseBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBaseBackupResponse:
        """
        This API is used to delete a specified data backup for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaseBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaseBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBInstanceNetworkAccess(
            self,
            request: models.DeleteDBInstanceNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteDBInstanceNetworkAccessResponse:
        """
        This API is used to delete a network of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBInstanceNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBInstanceNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogBackup(
            self,
            request: models.DeleteLogBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteLogBackupResponse:
        """
        This API is used to delete the specified log backup of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParameterTemplate(
            self,
            request: models.DeleteParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParameterTemplateResponse:
        """
        This API is used to delete a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReadOnlyGroup(
            self,
            request: models.DeleteReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteReadOnlyGroupResponse:
        """
        This API is used to delete an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReadOnlyGroupNetworkAccess(
            self,
            request: models.DeleteReadOnlyGroupNetworkAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteReadOnlyGroupNetworkAccessResponse:
        """
        This API is used to delete a network of an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReadOnlyGroupNetworkAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReadOnlyGroupNetworkAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServerlessDBInstance(
            self,
            request: models.DeleteServerlessDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteServerlessDBInstanceResponse:
        """
        This API is used to delete a PostgreSQL for Serverless instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServerlessDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServerlessDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to query the list of the database accounts for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableRecoveryTime(
            self,
            request: models.DescribeAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableRecoveryTimeResponse:
        """
        This API is used to query the available restoration time of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        This API is used to query the backup download restrictions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadURL(
            self,
            request: models.DescribeBackupDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadURLResponse:
        """
        u200cThis API is used to query the download address of a specified backup set, including full backup sets and incremental log backup sets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupOverview(
            self,
            request: models.DescribeBackupOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupOverviewResponse:
        """
        This API is used to query the backup overview. It will return the current number and size of backups, free backup space size, and paid backup space size (all size values are in bytes).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupPlans(
            self,
            request: models.DescribeBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupPlansResponse:
        """
        This API is used to query all backup plans of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummaries(
            self,
            request: models.DescribeBackupSummariesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummariesResponse:
        """
        This API is used to query the backup statistics of an instance. It will return the number and size (bytes) of backups of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseBackups(
            self,
            request: models.DescribeBaseBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseBackupsResponse:
        """
        This API is used to query the list of data backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClasses(
            self,
            request: models.DescribeClassesRequest,
            opts: Dict = None,
    ) -> models.DescribeClassesResponse:
        """
        This API is used to query purchasable instance specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClasses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloneDBInstanceSpec(
            self,
            request: models.DescribeCloneDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeCloneDBInstanceSpecResponse:
        """
        This API is used to query the minimum specification required by a cloned instance, including `SpecCode` and disk specification.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloneDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloneDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBBackups(
            self,
            request: models.DescribeDBBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBBackupsResponse:
        """
        This API is used to query the backup list of an instance. This API is disused and replaced by the [DescribeBaseBackups](https://intl.cloud.tencent.com/document/api/409/89022?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBErrlogs(
            self,
            request: models.DescribeDBErrlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBErrlogsResponse:
        """
        This API is used to query an error log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBErrlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBErrlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceAttribute(
            self,
            request: models.DescribeDBInstanceAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceAttributeResponse:
        """
        This API is used to query the details of one instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceHAConfig(
            self,
            request: models.DescribeDBInstanceHAConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceHAConfigResponse:
        """
        This API is used to query the HA configuration of an instance, which includes:
        <li>Allow a standby node to promote to a primary node.
        <li>Allow a semi-sync instance to adopt sync or async replication.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceHAConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceHAConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceParameters(
            self,
            request: models.DescribeDBInstanceParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceParametersResponse:
        """
        This API is used to query the parameters of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceSecurityGroups(
            self,
            request: models.DescribeDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceSecurityGroupsResponse:
        """
        This API is used to query the security group of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query the details of one or more instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSlowlogs(
            self,
            request: models.DescribeDBSlowlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSlowlogsResponse:
        """
        This API is used to get a slow query log. Since it was deprecated on September 1, 2021, it has no longer returned data. You need to use the [DescribeSlowQueryList](https://intl.cloud.tencent.com/document/product/409/60540?from_cn_redirect=1) API instead to get slow query logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSlowlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSlowlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBVersions(
            self,
            request: models.DescribeDBVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBVersionsResponse:
        """
        This API is used to query the list of supported database versions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBXlogs(
            self,
            request: models.DescribeDBXlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBXlogsResponse:
        """
        This API is used to get the instance Xlog list. This API is disused and replaced by the [DescribeBaseBackups](https://www.tencentcloud.com/zh/document/product/409/54343) API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBXlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBXlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        This API is used to query the database list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultParameters(
            self,
            request: models.DescribeDefaultParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultParametersResponse:
        """
        This API is used to query all parameters supported by a database version and engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptionKeys(
            self,
            request: models.DescribeEncryptionKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptionKeysResponse:
        """
        This API is used to query the instance key list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptionKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptionKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogBackups(
            self,
            request: models.DescribeLogBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogBackupsResponse:
        """
        This API is used to query the list of log backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        This API is used to query the order information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParameterTemplateAttributes(
            self,
            request: models.DescribeParameterTemplateAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeParameterTemplateAttributesResponse:
        """
        This API is used to query the details of a parameter template, including basic information and parameter information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParameterTemplateAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParameterTemplateAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParameterTemplates(
            self,
            request: models.DescribeParameterTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParameterTemplatesResponse:
        """
        This API is used to query the list of parameter templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParameterTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParameterTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamsEvent(
            self,
            request: models.DescribeParamsEventRequest,
            opts: Dict = None,
    ) -> models.DescribeParamsEventResponse:
        """
        This API is used to query the parameter modification event.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductConfig(
            self,
            request: models.DescribeProductConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeProductConfigResponse:
        """
        This API is used to query the purchasable specification configuration. u200cThis API is disused and replaced by the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroups(
            self,
            request: models.DescribeReadOnlyGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupsResponse:
        """
        This API is used to query the list of RO groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query the purchasable regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessDBInstances(
            self,
            request: models.DescribeServerlessDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessDBInstancesResponse:
        """
        This API is used to query the details of one or more PostgreSQL for Serverless instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryAnalysis(
            self,
            request: models.DescribeSlowQueryAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryAnalysisResponse:
        """
        This API is used to count and analyze slow query statements during the specified period of time and return aggregated statistical analysis results which are classified by statement with abstract parameter values.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryList(
            self,
            request: models.DescribeSlowQueryListRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryListResponse:
        """
        This API is used to get the slow queries during the specified period of time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query the supported AZs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBInstance(
            self,
            request: models.DestroyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyDBInstanceResponse:
        """
        This API is used to terminate an isolated instance by specifying the `DBInstanceId` parameter. The data of a terminated instance will be deleted and cannot be recovered. Be cautious with this API calling. Only the instance in isolation can be terminated.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisIsolateDBInstances(
            self,
            request: models.DisIsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DisIsolateDBInstancesResponse:
        """
        This API is used to remove one or more instances from isolation.
        """
        
        kwargs = {}
        kwargs["action"] = "DisIsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisIsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitDBInstances(
            self,
            request: models.InitDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InitDBInstancesResponse:
        """
        This API is used to initialize a TencentDB for PostgreSQL instance. This API is disused and replaced by the [CreateInstances](https://intl.cloud.tencent.com/document/api/409/56107?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "InitDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDBInstances(
            self,
            request: models.InquiryPriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDBInstancesResponse:
        """
        This API is used to query the purchase price of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewDBInstance(
            self,
            request: models.InquiryPriceRenewDBInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewDBInstanceResponse:
        """
        This API is used to query the renewal price of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpgradeDBInstance(
            self,
            request: models.InquiryPriceUpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeDBInstanceResponse:
        """
        This API is used to query the fees of upgrading a specified database instance. Only pay-as-you-go instance is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstances(
            self,
            request: models.IsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstancesResponse:
        """
        This API is used to isolate an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountRemark(
            self,
            request: models.ModifyAccountRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountRemarkResponse:
        """
        This API is used to modify account remarks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        This API is used to modify the backup download restrictions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupPlan(
            self,
            request: models.ModifyBackupPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupPlanResponse:
        """
        This API is used to modify the backup plan of an instance, such as modifying the backup start time. By default, a full backup starts at midnight every day and the generated backup files will be retained for seven days.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaseBackupExpireTime(
            self,
            request: models.ModifyBaseBackupExpireTimeRequest,
            opts: Dict = None,
    ) -> models.ModifyBaseBackupExpireTimeResponse:
        """
        This API is used to modify the expiration time of a specified data backup for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaseBackupExpireTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaseBackupExpireTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceChargeType(
            self,
            request: models.ModifyDBInstanceChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceChargeTypeResponse:
        """
        This API is used to switch the instance billing mode from pay-as-you-go to monthly subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceDeployment(
            self,
            request: models.ModifyDBInstanceDeploymentRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceDeploymentResponse:
        """
        This API is used to modify the AZs where the nodes of a source instance reside.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceHAConfig(
            self,
            request: models.ModifyDBInstanceHAConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceHAConfigResponse:
        """
        This API is used to modify the HA configuration of an instance. which includes:
        <li>Allow the standby node to promote to the primary node.
        <li>Allow a semi-sync instance to adopt sync or async replication.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceHAConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceHAConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        This API is used to rename a TencentDB for PostgreSQL instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceParameters(
            self,
            request: models.ModifyDBInstanceParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceParametersResponse:
        """
        This API is used to modify instance parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceReadOnlyGroup(
            self,
            request: models.ModifyDBInstanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceReadOnlyGroupResponse:
        """
        This API is used to modify the RO group of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API is used to modify the security group of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSpec(
            self,
            request: models.ModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSpecResponse:
        """
        This API is used to modify instance specifications, including memory and disk size.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstancesProject(
            self,
            request: models.ModifyDBInstancesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstancesProjectResponse:
        """
        This API is used to modify the project of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstancesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstancesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParameterTemplate(
            self,
            request: models.ModifyParameterTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParameterTemplateResponse:
        """
        This API is used to modify the configurations, such as parameter template name and description. It can also be used to manage the parameter list in the parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParameterTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParameterTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReadOnlyGroupConfig(
            self,
            request: models.ModifyReadOnlyGroupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyReadOnlyGroupConfigResponse:
        """
        This API is used to modify RO group configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReadOnlyGroupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReadOnlyGroupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySwitchTimePeriod(
            self,
            request: models.ModifySwitchTimePeriodRequest,
            opts: Dict = None,
    ) -> models.ModifySwitchTimePeriodResponse:
        """
        This API is used to perform a primary-standby switch for an instance waiting for the switch after it is upgraded.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySwitchTimePeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySwitchTimePeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenDBExtranetAccess(
            self,
            request: models.OpenDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.OpenDBExtranetAccessResponse:
        """
        This API is used to enable the public network access of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenServerlessDBExtranetAccess(
            self,
            request: models.OpenServerlessDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.OpenServerlessDBExtranetAccessResponse:
        """
        This API is used to enable the public network address of a PostgreSQL for Serverless instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenServerlessDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenServerlessDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebalanceReadOnlyGroup(
            self,
            request: models.RebalanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RebalanceReadOnlyGroupResponse:
        """
        This API is used to rebalance the loads of read-only replicas in an RO group. Please note that connections to those read-only replicas will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "RebalanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebalanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveDBInstanceFromReadOnlyGroup(
            self,
            request: models.RemoveDBInstanceFromReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveDBInstanceFromReadOnlyGroupResponse:
        """
        This API is used to remove a read-only replica from an RO group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveDBInstanceFromReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveDBInstanceFromReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        This API is used to renew an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        This API is used to reset the account password of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstance(
            self,
            request: models.RestartDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstanceResponse:
        """
        This API is used to restart an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreDBInstanceObjects(
            self,
            request: models.RestoreDBInstanceObjectsRequest,
            opts: Dict = None,
    ) -> models.RestoreDBInstanceObjectsResponse:
        """
        This API is used to recover database-related objects such as databases and tables on the original instance based on the backup set or recovery target time.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreDBInstanceObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreDBInstanceObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAutoRenewFlag(
            self,
            request: models.SetAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetAutoRenewFlagResponse:
        """
        This API is used to set auto-renewal.
        """
        
        kwargs = {}
        kwargs["action"] = "SetAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDBInstancePrimary(
            self,
            request: models.SwitchDBInstancePrimaryRequest,
            opts: Dict = None,
    ) -> models.SwitchDBInstancePrimaryResponse:
        """
        This API is used to enable the primary-standby switch of an instance.
        <li>By initiating a switch, you can verify whether the primary-standby switch is performed correctly.
        <li>By using forced switch, you can forcibly initiate the primary-standby switch when the delay of replica node failed to meet the switch requirement.
        <li>This operation can only be performed for the primary instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDBInstancePrimary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDBInstancePrimaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        This API is used to upgrade instance configurations. u200cThis API is disused and replaced by the [ModifyDBInstanceSpec](https://intl.cloud.tencent.com/document/api/409/63689?from_cn_redirect=1) API.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceKernelVersion(
            self,
            request: models.UpgradeDBInstanceKernelVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceKernelVersionResponse:
        """
        This API is used to upgrade the kernel version of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceKernelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceKernelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceMajorVersion(
            self,
            request: models.UpgradeDBInstanceMajorVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceMajorVersionResponse:
        """
        This API is used to upgrade the major kernel version of an instance, for example, from PostgreSQL 12 to PostgreSQL 15.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceMajorVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceMajorVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)