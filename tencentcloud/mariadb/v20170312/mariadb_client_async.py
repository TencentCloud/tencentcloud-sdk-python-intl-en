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
from tencentcloud.mariadb.v20170312 import models
from typing import Dict


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.intl.tencentcloudapi.com'
    _service = 'mariadb'

    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API is used to associate security groups with Tencent Cloud resources in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDcnJob(
            self,
            request: models.CancelDcnJobRequest,
            opts: Dict = None,
    ) -> models.CancelDcnJobResponse:
        """
        This API is used to cancel DCN synchronization.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDcnJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDcnJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneAccount(
            self,
            request: models.CloneAccountRequest,
            opts: Dict = None,
    ) -> models.CloneAccountResponse:
        """
        This API is used to clone an instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseDBExtranetAccess(
            self,
            request: models.CloseDBExtranetAccessRequest,
            opts: Dict = None,
    ) -> models.CloseDBExtranetAccessResponse:
        """
        This API is used to disable public network access for a TencentDB instance, which will make the public IP address inaccessible. The `DescribeDCDBInstances` API will not return the public domain name and port information of the corresponding instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseDBExtranetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseDBExtranetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyAccountPrivileges(
            self,
            request: models.CopyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.CopyAccountPrivilegesResponse:
        """
        This API is used to copy the permissions of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts. Permissions can only be copied between accounts with the same `Readonly` attribute.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccount(
            self,
            request: models.CreateAccountRequest,
            opts: Dict = None,
    ) -> models.CreateAccountResponse:
        """
        This API is used to create a TencentDB account. Multiple accounts can be created for one instance. Accounts with the same username but different hosts are different accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        This API is used to create a monthly subscribed TencentDB for MariaDB instance by passing in information such as instance specifications, database version number, validity period, and quantity.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHourDBInstance(
            self,
            request: models.CreateHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateHourDBInstanceResponse:
        """
        This API is used to create a pay-as-you-go TencentDB for MariaDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHourDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        This API is used to delete a TencentDB account, which is uniquely identified by username and host.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        This API is used to query the permissions of a TencentDB account.
        Note: Accounts with the same username but different hosts are different accounts.
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
        This API is used to query the list of accounts of a specified TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupFiles(
            self,
            request: models.DescribeBackupFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupFilesResponse:
        """
        This API is used to query the list of backup files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBEncryptAttributes(
            self,
            request: models.DescribeDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBEncryptAttributesResponse:
        """
        This API is used to query the encryption status of the instance data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceDetail(
            self,
            request: models.DescribeDBInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDetailResponse:
        """
        This API is used to query the details of a specified instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query the TencentDB instance list. It supports filtering instances by project ID, instance ID, private address, and instance name.
        If no filter is specified, 20 instances will be returned by default. Up to 100 instances can be returned for a single request.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBLogFiles(
            self,
            request: models.DescribeDBLogFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBLogFilesResponse:
        """
        This API is used to get the list of various logs of a database, including cold backups, binlogs, errlogs, and slowlogs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBLogFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBLogFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParameters(
            self,
            request: models.DescribeDBParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParametersResponse:
        """
        This API is used to get the current parameter settings of a database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API is used to query the security group details of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSlowLogs(
            self,
            request: models.DescribeDBSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSlowLogsResponse:
        """
        This API is used to query the list of slow query logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBTmpInstances(
            self,
            request: models.DescribeDBTmpInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBTmpInstancesResponse:
        """
        This API is used to obtain a temp rollback instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBTmpInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBTmpInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseObjects(
            self,
            request: models.DescribeDatabaseObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseObjectsResponse:
        """
        This API is used to query the list of database objects in a TencentDB instance, including tables, stored procedures, views, and functions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseTable(
            self,
            request: models.DescribeDatabaseTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseTableResponse:
        """
        This API is used to query the table information of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        This API is used to query the database list of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDcnDetail(
            self,
            request: models.DescribeDcnDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDcnDetailResponse:
        """
        This API is used to query the disaster recovery details of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDcnDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDcnDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileDownloadUrl(
            self,
            request: models.DescribeFileDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeFileDownloadUrlResponse:
        """
        This API is used to get the download URL of a specific backup or log file of a database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodeInfo(
            self,
            request: models.DescribeInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodeInfoResponse:
        """
        This API is used to query the information of primary and replica nodes of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogFileRetentionPeriod(
            self,
            request: models.DescribeLogFileRetentionPeriodRequest,
            opts: Dict = None,
    ) -> models.DescribeLogFileRetentionPeriodResponse:
        """
        This API is used to view the backup log retention days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogFileRetentionPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogFileRetentionPeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        This API is used to query TencentDB order information. You can pass in an order ID to query the TencentDB instance associated with the order and the corresponding task process ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrice(
            self,
            request: models.DescribePriceRequest,
            opts: Dict = None,
    ) -> models.DescribePriceResponse:
        """
        This API is used to query the instance price before you purchase it.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        This API is used to query the security group details of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBInstance(
            self,
            request: models.DestroyDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyDBInstanceResponse:
        """
        This API is used to terminate an isolated monthly subscribed instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyHourDBInstance(
            self,
            request: models.DestroyHourDBInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyHourDBInstanceResponse:
        """
        This API is used to terminate a pay-as-you-go TencentDB for MariaDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyHourDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyHourDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API is used to unassociate security groups from instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantAccountPrivileges(
            self,
            request: models.GrantAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.GrantAccountPrivilegesResponse:
        """
        This API is used to grant permissions to a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "GrantAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        This API is used to isolate a monthly subscribed TencentDB for MariaDB instance, which will no longer be accessible via IP and port.  The isolated instance can be started up in the recycle bin.  If it is isolated due to overdue payments, top up your account as soon as possible.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDedicatedDBInstance(
            self,
            request: models.IsolateDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDedicatedDBInstanceResponse:
        """
        This API is used to isolate a dedicated TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillSession(
            self,
            request: models.KillSessionRequest,
            opts: Dict = None,
    ) -> models.KillSessionResponse:
        """
        This API is used to kill the specified session.
        """
        
        kwargs = {}
        kwargs["action"] = "KillSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        This API is used to modify the remarks of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        This API is used to modify the permissions of a TencentDB instance account. \n\n**Note**\n-Only the SELECT permission (that is, set the permission parameter to `["SELECT"]`) of the system database `mysql` can be granted.An error will be reported if read-write permissions are granted to a read-only account. If the parameter is not passed in, no change will be made to the granted table permissions. To clear the granted view permissions, set `Privileges` to an empty array.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBEncryptAttributes(
            self,
            request: models.ModifyDBEncryptAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDBEncryptAttributesResponse:
        """
        This API is used to modify the instance data encryption.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBEncryptAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBEncryptAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstancesProject(
            self,
            request: models.ModifyDBInstancesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstancesProjectResponse:
        """
        This API is used to modify the project to which TencentDB instances belong.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstancesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstancesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        This API is used to modify database parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSyncMode(
            self,
            request: models.ModifyDBSyncModeRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSyncModeResponse:
        """
        This API is used to modify the sync mode of a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSyncMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSyncModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceNetwork(
            self,
            request: models.ModifyInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNetworkResponse:
        """
        This API is used to modify instance network.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceVip(
            self,
            request: models.ModifyInstanceVipRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceVipResponse:
        """
        This API is used to modify instance VIP.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceVport(
            self,
            request: models.ModifyInstanceVportRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceVportResponse:
        """
        This API is used to modify instance Vport.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncTaskAttribute(
            self,
            request: models.ModifySyncTaskAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySyncTaskAttributeResponse:
        """
        This API is used to modify sync task attributes (currently, only the task name can be modified).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncTaskAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncTaskAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        This API is used to reset the password of a TencentDB account.
        Note: accounts with the same username but different hosts are different accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDedicatedDBInstance(
            self,
            request: models.TerminateDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateDedicatedDBInstanceResponse:
        """
        This API is used to terminate the isolated dedicated TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDedicatedDBInstance(
            self,
            request: models.UpgradeDedicatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDedicatedDBInstanceResponse:
        """
        This API is used to expand the dedicated TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDedicatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDedicatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)