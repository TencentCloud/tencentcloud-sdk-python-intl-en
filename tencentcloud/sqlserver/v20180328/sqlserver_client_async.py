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
from tencentcloud.sqlserver.v20180328 import models
from typing import Dict


class SqlserverClient(AbstractClient):
    _apiVersion = '2018-03-28'
    _endpoint = 'sqlserver.intl.tencentcloudapi.com'
    _service = 'sqlserver'

    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API is used to bind security groups to instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BalanceReadOnlyGroup(
            self,
            request: models.BalanceReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.BalanceReadOnlyGroupResponse:
        """
        This API is used to balance the routing weight of each read-only instance according to the predefined weights. The DescribeReadOnlyGroupAutoWeight API is used to query the predefined weights.
        """
        
        kwargs = {}
        kwargs["action"] = "BalanceReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BalanceReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneDB(
            self,
            request: models.CloneDBRequest,
            opts: Dict = None,
    ) -> models.CloneDBResponse:
        """
        This API is used to clone and rename databases of an instance. The clones are still in the instance from which they are cloned.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseInterCommunication(
            self,
            request: models.CloseInterCommunicationRequest,
            opts: Dict = None,
    ) -> models.CloseInterCommunicationResponse:
        """
        This API is used to disable instance interconnection.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseInterCommunication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseInterCommunicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteExpansion(
            self,
            request: models.CompleteExpansionRequest,
            opts: Dict = None,
    ) -> models.CompleteExpansionResponse:
        """
        This API is used to complete the instance upgrade and switch immediately without waiting for the maintenance window when the instance status is "upgrade pending switch" after scale-out is initiated. This API needs to be called during off-peak hours of the instance. Some databases cannot be accessed before the switch is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteExpansion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteExpansionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteMigration(
            self,
            request: models.CompleteMigrationRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrationResponse:
        """
        This API is used to complete a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        This API is used to create an instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        This API is used to create a backup.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupMigration(
            self,
            request: models.CreateBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateBackupMigrationResponse:
        """
        This API is used to create a backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBasicDBInstances(
            self,
            request: models.CreateBasicDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateBasicDBInstancesResponse:
        """
        This API is used to create basic edition instances (cloud disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBasicDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBasicDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBusinessDBInstances(
            self,
            request: models.CreateBusinessDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateBusinessDBInstancesResponse:
        """
        This API is used to create business intelligence service instances (cloud disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBusinessDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBusinessDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBusinessIntelligenceFile(
            self,
            request: models.CreateBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.CreateBusinessIntelligenceFileResponse:
        """
        This API is used to add a business intelligence service file.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudDBInstances(
            self,
            request: models.CreateCloudDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateCloudDBInstancesResponse:
        """
        This API is used to create high-availability instances (cloud disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudReadOnlyDBInstances(
            self,
            request: models.CreateCloudReadOnlyDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateCloudReadOnlyDBInstancesResponse:
        """
        This API is used to create read-only instances (cloud disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudReadOnlyDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudReadOnlyDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDB(
            self,
            request: models.CreateDBRequest,
            opts: Dict = None,
    ) -> models.CreateDBResponse:
        """
        This API is used to create a database.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstances(
            self,
            request: models.CreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstancesResponse:
        """
        This API is used to create high-availability instances (local disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIncrementalMigration(
            self,
            request: models.CreateIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateIncrementalMigrationResponse:
        """
        This API is used to create an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigration(
            self,
            request: models.CreateMigrationRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationResponse:
        """
        This API is used to create a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublishSubscribe(
            self,
            request: models.CreatePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreatePublishSubscribeResponse:
        """
        This API is used to create a publish/subscribe relationship between two databases. A subscriber cannot act as a publisher, and a publisher can have multiple subscriber instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReadOnlyDBInstances(
            self,
            request: models.CreateReadOnlyDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateReadOnlyDBInstancesResponse:
        """
        This API is used to create read-only instances (local disk).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReadOnlyDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReadOnlyDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CutXEvents(
            self,
            request: models.CutXEventsRequest,
            opts: Dict = None,
    ) -> models.CutXEventsResponse:
        """
        This API is used to manually cut block logs and deadlock logs.
        """
        
        kwargs = {}
        kwargs["action"] = "CutXEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CutXEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        This API is used to delete an instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupMigration(
            self,
            request: models.DeleteBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupMigrationResponse:
        """
        This API is used to delete a backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBusinessIntelligenceFile(
            self,
            request: models.DeleteBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.DeleteBusinessIntelligenceFileResponse:
        """
        This API is used to delete a business intelligence service file.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDB(
            self,
            request: models.DeleteDBRequest,
            opts: Dict = None,
    ) -> models.DeleteDBResponse:
        """
        This API is used to drop a database.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBInstance(
            self,
            request: models.DeleteDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteDBInstanceResponse:
        """
        This API is used to release SQL server instances (eliminated immediately) in the recycle bin. The released instances will be physically terminated after being retained for a period of time. Their publish-subscribe relationships will be automatically disassociated, and their RO replicas will be automatically released.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIncrementalMigration(
            self,
            request: models.DeleteIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteIncrementalMigrationResponse:
        """
        This API is used to delete an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigration(
            self,
            request: models.DeleteMigrationRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrationResponse:
        """
        This API is used to delete a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePublishSubscribe(
            self,
            request: models.DeletePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeletePublishSubscribeResponse:
        """
        This API is used to delete the publish/subscribe relationship between two databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivilegeByDB(
            self,
            request: models.DescribeAccountPrivilegeByDBRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegeByDBResponse:
        """
        This API is used to query information on the account and permissions associated with the database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountPrivilegeByDB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountPrivilegeByDBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to pull the list of instance accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupByFlowId(
            self,
            request: models.DescribeBackupByFlowIdRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupByFlowIdResponse:
        """
        This API is used to query the created backup details through the backup creation process ID. The process ID can be obtained through the CreateBackup API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupByFlowId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupByFlowIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupCommand(
            self,
            request: models.DescribeBackupCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupCommandResponse:
        """
        This API is used to query the commands of creating backups canonically.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupFiles(
            self,
            request: models.DescribeBackupFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupFilesResponse:
        """
        This API is used to query the details of an unarchived backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupMigration(
            self,
            request: models.DescribeBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupMigrationResponse:
        """
        This API is used to create an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupMonitor(
            self,
            request: models.DescribeBackupMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupMonitorResponse:
        """
        This API is used to query backup space usage details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupStatistical(
            self,
            request: models.DescribeBackupStatisticalRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupStatisticalResponse:
        """
        This API is used to query the real-time statistics list of backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupStatistical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupStatisticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupSummary(
            self,
            request: models.DescribeBackupSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupSummaryResponse:
        """
        This API is used to query the backup overview information of databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupUploadSize(
            self,
            request: models.DescribeBackupUploadSizeRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupUploadSizeResponse:
        """
        This API is used to query the size of uploaded backup files. It is valid if the backup file type is `COS_UPLOAD` (the file is stored in COS).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupUploadSize"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupUploadSizeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackups(
            self,
            request: models.DescribeBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupsResponse:
        """
        This API is used to query the list of backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBusinessIntelligenceFile(
            self,
            request: models.DescribeBusinessIntelligenceFileRequest,
            opts: Dict = None,
    ) -> models.DescribeBusinessIntelligenceFileResponse:
        """
        This API is used to query the files required by business intelligence service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBusinessIntelligenceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBusinessIntelligenceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCollationTimeZone(
            self,
            request: models.DescribeCollationTimeZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCollationTimeZoneResponse:
        """
        This API is used to query the character set and time zone supported by the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCollationTimeZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCollationTimeZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBackupStatistical(
            self,
            request: models.DescribeCrossBackupStatisticalRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBackupStatisticalResponse:
        """
        This API is used to query the real-time statistics list of cross-region backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBackupStatistical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBackupStatisticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossRegionZone(
            self,
            request: models.DescribeCrossRegionZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossRegionZoneResponse:
        """
        This API is used to query the disaster recovery region and AZ of the secondary node based on the primary instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossRegionZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossRegionZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossRegions(
            self,
            request: models.DescribeCrossRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossRegionsResponse:
        """
        This API is used to query the target region for cross-region backups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCharsets(
            self,
            request: models.DescribeDBCharsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCharsetsResponse:
        """
        This API is used to query the database character sets supported by an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCharsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCharsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceInter(
            self,
            request: models.DescribeDBInstanceInterRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceInterResponse:
        """
        This API is used to query the information of the interconnected instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceInter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceInterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query the list of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstancesAttribute(
            self,
            request: models.DescribeDBInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesAttributeResponse:
        """
        This API is used to query the attributes of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBPrivilegeByAccount(
            self,
            request: models.DescribeDBPrivilegeByAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeDBPrivilegeByAccountResponse:
        """
        This API is used to query information on the databases and permissions associated with the account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBPrivilegeByAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBPrivilegeByAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBRestoreTime(
            self,
            request: models.DescribeDBRestoreTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBRestoreTimeResponse:
        """
        This API is used to query databases that can be rolled back.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBRestoreTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBRestoreTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API is used to query the security group details of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBs(
            self,
            request: models.DescribeDBsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBsResponse:
        """
        This API is used to query the list of databases
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBsNormal(
            self,
            request: models.DescribeDBsNormalRequest,
            opts: Dict = None,
    ) -> models.DescribeDBsNormalResponse:
        """
        This API is used to query database configurations. It does not return information of the accounts that have permissions to operate the database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBsNormal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBsNormalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseNames(
            self,
            request: models.DescribeDatabaseNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseNamesResponse:
        """
        This API is used to query the database name associated with the account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        This API is used to query the database list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabasesNormal(
            self,
            request: models.DescribeDatabasesNormalRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesNormalResponse:
        """
        This API is used to query database configuration information. This API does not contain accounts associated with databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabasesNormal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesNormalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowStatus(
            self,
            request: models.DescribeFlowStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowStatusResponse:
        """
        This API is used to query flow status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHASwitchLog(
            self,
            request: models.DescribeHASwitchLogRequest,
            opts: Dict = None,
    ) -> models.DescribeHASwitchLogResponse:
        """
        This API is used to perform the manual primary-secondary switch.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHASwitchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHASwitchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIncrementalMigration(
            self,
            request: models.DescribeIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.DescribeIncrementalMigrationResponse:
        """
        This API is used to query an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceByOrders(
            self,
            request: models.DescribeInstanceByOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceByOrdersResponse:
        """
        This API is used to query the instance ID by the order number.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceByOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceByOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        This API is used to query the parameter modification records of an instance.
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
        This API is used to query the parameter list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTasks(
            self,
            request: models.DescribeInstanceTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTasksResponse:
        """
        This API is used to query the list of asynchronous tasks related to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTradeParameter(
            self,
            request: models.DescribeInstanceTradeParameterRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTradeParameterResponse:
        """
        This API is used to query the instance billing parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTradeParameter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTradeParameterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceSpan(
            self,
            request: models.DescribeMaintenanceSpanRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceSpanResponse:
        """
        This API is used to query the maintenance time window of an instance based on its instance ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceSpan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceSpanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDatabases(
            self,
            request: models.DescribeMigrationDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDatabasesResponse:
        """
        This API is used to query the list of databases to be migrated.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDetail(
            self,
            request: models.DescribeMigrationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDetailResponse:
        """
        This API is used to query migration task details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrations(
            self,
            request: models.DescribeMigrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationsResponse:
        """
        This API is used to query the list of eligible migration tasks based on the entered criteria.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        This API is used to query order information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductConfig(
            self,
            request: models.DescribeProductConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeProductConfigResponse:
        """
        This API is used to query purchasable specification configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        This API is used to query security group details of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublishSubscribe(
            self,
            request: models.DescribePublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.DescribePublishSubscribeResponse:
        """
        This API is used to query the publish/subscribe relationship list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupAutoWeight(
            self,
            request: models.DescribeReadOnlyGroupAutoWeightRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupAutoWeightResponse:
        """
        This API is used to query the automatic weight assignment result of the read-only group. The BalanceReadOnlyGroup API is used to perform routing weight assignment according to the automatic weight assignment result.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupAutoWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupAutoWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupByReadOnlyInstance(
            self,
            request: models.DescribeReadOnlyGroupByReadOnlyInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupByReadOnlyInstanceResponse:
        """
        This API is used to query the read-only group where the read-only instance is located by its ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupByReadOnlyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupByReadOnlyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupDetails(
            self,
            request: models.DescribeReadOnlyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupDetailsResponse:
        """
        This API is used to query read-only group details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReadOnlyGroupList(
            self,
            request: models.DescribeReadOnlyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeReadOnlyGroupListResponse:
        """
        This API is used to query the read-only group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReadOnlyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReadOnlyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to query purchasable regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegularBackupPlan(
            self,
            request: models.DescribeRegularBackupPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeRegularBackupPlanResponse:
        """
        This API is used to query the scheduled backup retention plans of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegularBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegularBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTask(
            self,
            request: models.DescribeRestoreTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTaskResponse:
        """
        This API is used to query the list of rollback tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTimeRange(
            self,
            request: models.DescribeRestoreTimeRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTimeRangeResponse:
        """
        This API is used to query the time range available for rollback by time point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTimeRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTimeRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTime(
            self,
            request: models.DescribeRollbackTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTimeResponse:
        """
        This API is used to query the time range available for instance rollback.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowlogs(
            self,
            request: models.DescribeSlowlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowlogsResponse:
        """
        This API is used to get file information of slow query logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecSellStatus(
            self,
            request: models.DescribeSpecSellStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecSellStatusResponse:
        """
        This API is used to query the status information on specifications, including the sales status and reference price. (The actual price is subject to the result returned by price querying APIs.)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecSellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecSellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeInstanceCheck(
            self,
            request: models.DescribeUpgradeInstanceCheckRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeInstanceCheckResponse:
        """
        This API is used to pre-check the impact of the instance configuration adjustment before the adjustment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeInstanceCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeInstanceCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadBackupInfo(
            self,
            request: models.DescribeUploadBackupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadBackupInfoResponse:
        """
        This API is used to query a backup upload permission.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadBackupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadBackupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeXEvents(
            self,
            request: models.DescribeXEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeXEventsResponse:
        """
        This API is used to query the list of extended events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeXEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeXEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query currently purchasable AZs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API is used to unbind security groups from instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateDBInstances(
            self,
            request: models.InquiryPriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateDBInstancesResponse:
        """
        This API is used to query the price of requested instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpgradeDBInstance(
            self,
            request: models.InquiryPriceUpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeDBInstanceResponse:
        """
        This API is used to query the upgrade prices of a monthly subscribed instance.
        .
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivilege(
            self,
            request: models.ModifyAccountPrivilegeRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegeResponse:
        """
        This API is used to modify instance account permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegeResponse
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
        
    async def ModifyBackupMigration(
            self,
            request: models.ModifyBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupMigrationResponse:
        """
        This API is used to modify a backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupName(
            self,
            request: models.ModifyBackupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupNameResponse:
        """
        This API is used to modify the name of a backup task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupStrategy(
            self,
            request: models.ModifyBackupStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupStrategyResponse:
        """
        This API is used to modify the backup policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloseWanIp(
            self,
            request: models.ModifyCloseWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyCloseWanIpResponse:
        """
        This API is used to disable the public network for the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloseWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloseWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCrossBackupStrategy(
            self,
            request: models.ModifyCrossBackupStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyCrossBackupStrategyResponse:
        """
        This API is used to enable or disable cross-region backup policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCrossBackupStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCrossBackupStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBEncryptAttributes(
            self,
            request: models.ModifyDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBEncryptAttributesResponse:
        """
        This API is used to enable or disable TDE of a database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceName(
            self,
            request: models.ModifyDBInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNameResponse:
        """
        This API is used to rename an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNetwork(
            self,
            request: models.ModifyDBInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNetworkResponse:
        """
        This API is used to switch a running instance from a VPC to another.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNote(
            self,
            request: models.ModifyDBInstanceNoteRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNoteResponse:
        """
        This API is used to modify the instance remarks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNote"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNoteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceProject(
            self,
            request: models.ModifyDBInstanceProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceProjectResponse:
        """
        This API is used to modify the project to which a database instance belongs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSSL(
            self,
            request: models.ModifyDBInstanceSSLRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSSLResponse:
        """
        This API is used to enable/disable/update SSL encryption.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API is used to modify security groups bound to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBName(
            self,
            request: models.ModifyDBNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDBNameResponse:
        """
        This API is used to rename a database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBRemark(
            self,
            request: models.ModifyDBRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyDBRemarkResponse:
        """
        This API is used to modify database remarks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDReadable(
            self,
            request: models.ModifyDReadableRequest,
            opts: Dict = None,
    ) -> models.ModifyDReadableResponse:
        """
        This API is used to enable or disable the read-only feature of the replica server.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDReadable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDReadableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseCDC(
            self,
            request: models.ModifyDatabaseCDCRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseCDCResponse:
        """
        This API is used to enable or disable the change data capture (CDC) feature.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseCDC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseCDCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseCT(
            self,
            request: models.ModifyDatabaseCTRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseCTResponse:
        """
        This API is used to enable or disable the change tracking (CT) feature.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseCT"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseCTResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseMdf(
            self,
            request: models.ModifyDatabaseMdfRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseMdfResponse:
        """
        This API is used to shrink database MDF files.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseMdf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseMdfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabasePrivilege(
            self,
            request: models.ModifyDatabasePrivilegeRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabasePrivilegeResponse:
        """
        This API is used to modify instance database permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabasePrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabasePrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseShrinkMDF(
            self,
            request: models.ModifyDatabaseShrinkMDFRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseShrinkMDFResponse:
        """
        This API is used to shrink the database mdf (Shrink mdf).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseShrinkMDF"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseShrinkMDFResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIncrementalMigration(
            self,
            request: models.ModifyIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyIncrementalMigrationResponse:
        """
        This API is used to modify an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEncryptAttributes(
            self,
            request: models.ModifyInstanceEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEncryptAttributesResponse:
        """
        This API is used to enable TDE of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParam(
            self,
            request: models.ModifyInstanceParamRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamResponse:
        """
        This API is used to modify instance parameters.
        <b>Note</b>: if <b>the instance needs to be restarted</b> for the modified parameter to take effect, <b>it will be restarted</b> immediately or during the maintenance time according to the `WaitSwitch` parameter.
        Before you modify a parameter, you can use the `DescribeInstanceParams` API to query whether the instance needs to be restarted.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceSpan(
            self,
            request: models.ModifyMaintenanceSpanRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceSpanResponse:
        """
        This API is used to modify the maintenance window of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceSpan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceSpanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigration(
            self,
            request: models.ModifyMigrationRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationResponse:
        """
        This API is used to modify an existing migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOpenWanIp(
            self,
            request: models.ModifyOpenWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyOpenWanIpResponse:
        """
        This API is used to enable the public network for the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOpenWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOpenWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublishSubscribe(
            self,
            request: models.ModifyPublishSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyPublishSubscribeResponse:
        """
        This API is used to modify the publish/subscribe relationship of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublishSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublishSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublishSubscribeName(
            self,
            request: models.ModifyPublishSubscribeNameRequest,
            opts: Dict = None,
    ) -> models.ModifyPublishSubscribeNameResponse:
        """
        This API is used to modify the publish/subscribe names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublishSubscribeName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublishSubscribeNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReadOnlyGroupDetails(
            self,
            request: models.ModifyReadOnlyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.ModifyReadOnlyGroupDetailsResponse:
        """
        This API is used to modify read-only group details.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReadOnlyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReadOnlyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenInterCommunication(
            self,
            request: models.OpenInterCommunicationRequest,
            opts: Dict = None,
    ) -> models.OpenInterCommunicationResponse:
        """
        This API is used to enable instance interconnection, which can interconnect business intelligence services.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenInterCommunication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenInterCommunicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMigrationCheckProcess(
            self,
            request: models.QueryMigrationCheckProcessRequest,
            opts: Dict = None,
    ) -> models.QueryMigrationCheckProcessResponse:
        """
        This API is used to query the progress of the migration verification task, inquiry of migration check task progress, applicable to the migration method where the migration source type is TencentDB for SQL Server.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMigrationCheckProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMigrationCheckProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecycleDBInstance(
            self,
            request: models.RecycleDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RecycleDBInstanceResponse:
        """
        This API is used to return a deactivated SQL Server instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RecycleDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecycleDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecycleReadOnlyGroup(
            self,
            request: models.RecycleReadOnlyGroupRequest,
            opts: Dict = None,
    ) -> models.RecycleReadOnlyGroupResponse:
        """
        This API is used to reclaim resources of read-only groups immediately. The resources, such as VIP, occupied by the read-only group will be released immediately and cannot be recovered.
        """
        
        kwargs = {}
        kwargs["action"] = "RecycleReadOnlyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecycleReadOnlyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveBackups(
            self,
            request: models.RemoveBackupsRequest,
            opts: Dict = None,
    ) -> models.RemoveBackupsResponse:
        """
        This API is used to delete backup files created by users manually. The backup policy to be deleted can be instance backup or multi-database backup.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewPostpaidDBInstance(
            self,
            request: models.RenewPostpaidDBInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewPostpaidDBInstanceResponse:
        """
        This API is used to recover the pay-as-you-go instance that is manually isolated through the API TerminateDBInstance from the recycle bin.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewPostpaidDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewPostpaidDBInstanceResponse
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
        This API is used to restart a database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreInstance(
            self,
            request: models.RestoreInstanceRequest,
            opts: Dict = None,
    ) -> models.RestoreInstanceResponse:
        """
        This API is used to roll back the database by backup set.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackInstance(
            self,
            request: models.RollbackInstanceRequest,
            opts: Dict = None,
    ) -> models.RollbackInstanceResponse:
        """
        This API is used to roll back the instance by time point.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunMigration(
            self,
            request: models.RunMigrationRequest,
            opts: Dict = None,
    ) -> models.RunMigrationResponse:
        """
        This API is used to start running a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "RunMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBackupMigration(
            self,
            request: models.StartBackupMigrationRequest,
            opts: Dict = None,
    ) -> models.StartBackupMigrationResponse:
        """
        This API is used to start a backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartBackupMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBackupMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartIncrementalMigration(
            self,
            request: models.StartIncrementalMigrationRequest,
            opts: Dict = None,
    ) -> models.StartIncrementalMigrationResponse:
        """
        This API is used to start an incremental backup import task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartIncrementalMigration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartIncrementalMigrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstanceXEvent(
            self,
            request: models.StartInstanceXEventRequest,
            opts: Dict = None,
    ) -> models.StartInstanceXEventResponse:
        """
        This API is used to start and stop an extended event.
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstanceXEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstanceXEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchCloudInstanceHA(
            self,
            request: models.SwitchCloudInstanceHARequest,
            opts: Dict = None,
    ) -> models.SwitchCloudInstanceHAResponse:
        """
        This API is used to manually switch between primary and secondary.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchCloudInstanceHA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchCloudInstanceHAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDBInstance(
            self,
            request: models.TerminateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateDBInstanceResponse:
        """
        This API is used to isolate an instance to move it into a recycle bin.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        This API is used to upgrade an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)