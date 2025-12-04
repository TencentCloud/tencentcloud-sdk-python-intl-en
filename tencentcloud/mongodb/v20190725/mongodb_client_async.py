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
from tencentcloud.mongodb.v20190725 import models
from typing import Dict


class MongodbClient(AbstractClient):
    _apiVersion = '2019-07-25'
    _endpoint = 'mongodb.intl.tencentcloudapi.com'
    _service = 'mongodb'

    async def AssignProject(
            self,
            request: models.AssignProjectRequest,
            opts: Dict = None,
    ) -> models.AssignProjectResponse:
        """
        This API is used to specify the project of a TencentDB for MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AssignProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccountUser(
            self,
            request: models.CreateAccountUserRequest,
            opts: Dict = None,
    ) -> models.CreateAccountUserResponse:
        """
        This API is used to customize an account to access the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccountUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupDBInstance(
            self,
            request: models.CreateBackupDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateBackupDBInstanceResponse:
        """
        This API is used to back up an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupDownloadTask(
            self,
            request: models.CreateBackupDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateBackupDownloadTaskResponse:
        """
        This API is used to create a backup download task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        This API is used to create a yearly/monthly subscription TencentDB for MongoDB instance. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/35767?from_cn_redirect=1) API can be called to query and obtain the supported sales specifications.
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
        This API is used to create a pay-as-you-go TencentDB for MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogDownloadTask(
            self,
            request: models.CreateLogDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLogDownloadTaskResponse:
        """
        This API is used to create a log download task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccountUser(
            self,
            request: models.DeleteAccountUserRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountUserResponse:
        """
        This API is used to delete a custom account of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccountUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogDownloadTask(
            self,
            request: models.DeleteLogDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteLogDownloadTaskResponse:
        """
        This API is used to delete a log download task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        This API is used to query the asynchronous task status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadTask(
            self,
            request: models.DescribeBackupDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadTaskResponse:
        """
        This API is used to query information about the backup download task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupRules(
            self,
            request: models.DescribeBackupRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupRulesResponse:
        """
        This API is used to obtain the automatic backup configuration information of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientConnections(
            self,
            request: models.DescribeClientConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClientConnectionsResponse:
        """
        This API is used to query the client connection information on an instance, including the IP address for connection and the number of connections.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentOp(
            self,
            request: models.DescribeCurrentOpRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentOpResponse:
        """
        This API is used to query the operation currently being performed on a TencentDB for MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentOp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentOpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBBackups(
            self,
            request: models.DescribeDBBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBBackupsResponse:
        """
        This API is used to query the list of instance backups. Currently, only backups created in the last seven days can be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceDeal(
            self,
            request: models.DescribeDBInstanceDealRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDealResponse:
        """
        This API is used to get order details of purchase, renewal, and specification adjustment of a MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceNamespace(
            self,
            request: models.DescribeDBInstanceNamespaceRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceNamespaceResponse:
        """
        This API is used to query the table information on a database.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceNodeProperty(
            self,
            request: models.DescribeDBInstanceNodePropertyRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceNodePropertyResponse:
        """
        This API is used to query node attributes, such as the AZ, node name, address, role, status, delay between primary and secondary nodes, priority, voting right, and tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceNodeProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceNodePropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        This API is used to query the list of TencentDB for MongoDB instances. It supports filtering primary instances, disaster recovery instances, and read-only instances by project ID, instance ID, instance status, and other conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetailedSlowLogs(
            self,
            request: models.DescribeDetailedSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDetailedSlowLogsResponse:
        """
        This API is used to query slow log details of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetailedSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetailedSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        This API is used to query the list of parameters that can be modified for the current instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSSL(
            self,
            request: models.DescribeInstanceSSLRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSSLResponse:
        """
        This API is used to view the enabling status of Secure Sockets Layer (SSL) for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogDownloadTasks(
            self,
            request: models.DescribeLogDownloadTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeLogDownloadTasksResponse:
        """
        This API is used to query a log download task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogDownloadTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogDownloadTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMongodbLogs(
            self,
            request: models.DescribeMongodbLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeMongodbLogsResponse:
        """
        This API is used to query running logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMongodbLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMongodbLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroup(
            self,
            request: models.DescribeSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupResponse:
        """
        This API is used to query security groups bound to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogPatterns(
            self,
            request: models.DescribeSlowLogPatternsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogPatternsResponse:
        """
        This API is used to get the slow log statistics of a database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogPatterns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogPatternsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        This API is used to get the slow log information of a TencentDB instance. Only slow logs for the last 7 days can be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecInfo(
            self,
            request: models.DescribeSpecInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecInfoResponse:
        """
        This API is used to query the sales specification of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTransparentDataEncryption(
            self,
            request: models.EnableTransparentDataEncryptionRequest,
            opts: Dict = None,
    ) -> models.EnableTransparentDataEncryptionResponse:
        """
        This API is used to enable the transparent data encryption (TDE) capability for TencentDB for MongoDB.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTransparentDataEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTransparentDataEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FlushInstanceRouterConfig(
            self,
            request: models.FlushInstanceRouterConfigRequest,
            opts: Dict = None,
    ) -> models.FlushInstanceRouterConfigResponse:
        """
        This API is used to run the `FlushRouterConfig` command on all mongos instances.
        """
        
        kwargs = {}
        kwargs["action"] = "FlushInstanceRouterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlushInstanceRouterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateDBInstances(
            self,
            request: models.InquirePriceCreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateDBInstancesResponse:
        """
        This API is used to query price of instance creation. The `region` parameter must be passed in this API, otherwise verification will fail. This API allows queries only for purchasable instance specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyDBInstanceSpec(
            self,
            request: models.InquirePriceModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyDBInstanceSpecResponse:
        """
        This API is used to query the price of instance specification adjustment.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewDBInstances(
            self,
            request: models.InquirePriceRenewDBInstancesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewDBInstancesResponse:
        """
        This API is used to query the renewal price of a monthly subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstanceEnableSSL(
            self,
            request: models.InstanceEnableSSLRequest,
            opts: Dict = None,
    ) -> models.InstanceEnableSSLResponse:
        """
        This API is used to set the SSL status for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InstanceEnableSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstanceEnableSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        This API is used to isolate a pay-as-you-go TencentDB for MongoDB instance. After isolation, the instance is retained in the recycle bin, and data cannot be written into it. After a certain period of isolation, the instance is deleted permanently. For the retention time in the recycle bin, see the pay-as-you-go service terms. The deleted pay-as-you-go instance cannot be recovered. Proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillOps(
            self,
            request: models.KillOpsRequest,
            opts: Dict = None,
    ) -> models.KillOpsResponse:
        """
        This API is used to terminate a specific operation performed on a TencentDB for MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "KillOps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillOpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceNetworkAddress(
            self,
            request: models.ModifyDBInstanceNetworkAddressRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceNetworkAddressResponse:
        """
        This API is used to modify the network information on a TencentDB for MongoDB instance. It supports switching from a basic network to a VPC network or from one VPC network to another VPC network.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceNetworkAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceNetworkAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroup(
            self,
            request: models.ModifyDBInstanceSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupResponse:
        """
        This API is used to modify security groups bound to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSpec(
            self,
            request: models.ModifyDBInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSpecResponse:
        """
        This API is used to adjust the TencentDB for MongoDB instance configuration. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to query and obtain the supported sales specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParams(
            self,
            request: models.ModifyInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamsResponse:
        """
        This API is used to modify the parameter configuration of a TencentDB for MongoDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedDBInstance(
            self,
            request: models.OfflineIsolatedDBInstanceRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedDBInstanceResponse:
        """
        This API is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status.
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenameInstance(
            self,
            request: models.RenameInstanceRequest,
            opts: Dict = None,
    ) -> models.RenameInstanceResponse:
        """
        This API is used to rename a TencentDB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RenameInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenameInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBInstances(
            self,
            request: models.RenewDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewDBInstancesResponse:
        """
        This API is used to renew a monthly subscription TencentDB instance. Only monthly subscription instances are supported, while pay-as-you-go instances do not need to be renewed.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDBInstancePassword(
            self,
            request: models.ResetDBInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDBInstancePasswordResponse:
        """
        This API is used to reset the instance access password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDBInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDBInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAccountUserPrivilege(
            self,
            request: models.SetAccountUserPrivilegeRequest,
            opts: Dict = None,
    ) -> models.SetAccountUserPrivilegeResponse:
        """
        This API is used to set the account permissions of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SetAccountUserPrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAccountUserPrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDBInstanceDeletionProtection(
            self,
            request: models.SetDBInstanceDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.SetDBInstanceDeletionProtectionResponse:
        """
        This API is used to set instance termination protection.
        """
        
        kwargs = {}
        kwargs["action"] = "SetDBInstanceDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDBInstanceDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetInstanceMaintenance(
            self,
            request: models.SetInstanceMaintenanceRequest,
            opts: Dict = None,
    ) -> models.SetInstanceMaintenanceResponse:
        """
        This API is used to set the instance maintenance window.
        """
        
        kwargs = {}
        kwargs["action"] = "SetInstanceMaintenance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetInstanceMaintenanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDBInstances(
            self,
            request: models.TerminateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateDBInstancesResponse:
        """
        This API is used to terminate monthly subscription billing instances.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceKernelVersion(
            self,
            request: models.UpgradeDBInstanceKernelVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceKernelVersionResponse:
        """
        This API is used to upgrade the kernel version of the database instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceKernelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceKernelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDbInstanceVersion(
            self,
            request: models.UpgradeDbInstanceVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeDbInstanceVersionResponse:
        """
        This API is used to upgrade the database kernel across versions. Currently, it is only supported to upgrade from version 3.6 to 4.0, 4.0 to 4.2, 4.2 to 4.4, and 4.4 to 5.0.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDbInstanceVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDbInstanceVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)