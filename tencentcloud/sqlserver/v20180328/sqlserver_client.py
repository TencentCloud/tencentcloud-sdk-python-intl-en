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
from tencentcloud.sqlserver.v20180328 import models


class SqlserverClient(AbstractClient):
    _apiVersion = '2018-03-28'
    _endpoint = 'sqlserver.intl.tencentcloudapi.com'
    _service = 'sqlserver'


    def AssociateSecurityGroups(self, request):
        """This API is used to bind security groups to instances in batches.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.AssociateSecurityGroupsResponse`

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


    def BalanceReadOnlyGroup(self, request):
        """This API is used to balance the routing weight of each read-only instance according to the predefined weights. The DescribeReadOnlyGroupAutoWeight API is used to query the predefined weights.

        :param request: Request instance for BalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.BalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.BalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BalanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BalanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneDB(self, request):
        """This API is used to clone and rename databases of an instance. The clones are still in the instance from which they are cloned.

        :param request: Request instance for CloneDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneDB", params, headers=headers)
            response = json.loads(body)
            model = models.CloneDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseInterCommunication(self, request):
        """This API is used to disable instance interconnection.

        :param request: Request instance for CloseInterCommunication.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CloseInterCommunicationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CloseInterCommunicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseInterCommunication", params, headers=headers)
            response = json.loads(body)
            model = models.CloseInterCommunicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteExpansion(self, request):
        """This API is used to complete the instance upgrade and switch immediately without waiting for the maintenance window when the instance status is "upgrade pending switch" after scale-out is initiated. This API needs to be called during off-peak hours of the instance. Some databases cannot be accessed before the switch is completed.

        :param request: Request instance for CompleteExpansion.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteExpansion", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteExpansionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteMigration(self, request):
        """This API is used to complete a migration task.

        :param request: Request instance for CompleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """This API is used to create an instance account.

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountResponse`

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


    def CreateBackup(self, request):
        """This API is used to create a backup.

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupResponse`

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


    def CreateBackupMigration(self, request):
        """This API is used to create a backup import task.

        :param request: Request instance for CreateBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBasicDBInstances(self, request):
        """This API is used to create basic edition instances (cloud disk).

        :param request: Request instance for CreateBasicDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBasicDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBasicDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBusinessDBInstances(self, request):
        """This API is used to create business intelligence service instances (cloud disk).

        :param request: Request instance for CreateBusinessDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBusinessDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBusinessDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBusinessIntelligenceFile(self, request):
        """This API is used to add a business intelligence service file.

        :param request: Request instance for CreateBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudDBInstances(self, request):
        """This API is used to create high-availability instances (cloud disk).

        :param request: Request instance for CreateCloudDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudReadOnlyDBInstances(self, request):
        """This API is used to create read-only instances (cloud disk).

        :param request: Request instance for CreateCloudReadOnlyDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudReadOnlyDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudReadOnlyDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudReadOnlyDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudReadOnlyDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDB(self, request):
        """This API is used to create a database.

        :param request: Request instance for CreateDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDB", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstances(self, request):
        """This API is used to create high-availability instances (local disk).

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIncrementalMigration(self, request):
        """This API is used to create an incremental backup import task.

        :param request: Request instance for CreateIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigration(self, request):
        """This API is used to create a migration task.

        :param request: Request instance for CreateMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublishSubscribe(self, request):
        """This API is used to create a publish/subscribe relationship between two databases. A subscriber cannot act as a publisher, and a publisher can have multiple subscriber instances.

        :param request: Request instance for CreatePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyDBInstances(self, request):
        """This API is used to create read-only instances (local disk).

        :param request: Request instance for CreateReadOnlyDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CutXEvents(self, request):
        """This API is used to manually cut block logs and deadlock logs.

        :param request: Request instance for CutXEvents.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CutXEventsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CutXEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CutXEvents", params, headers=headers)
            response = json.loads(body)
            model = models.CutXEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """This API is used to delete an instance account.

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountResponse`

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


    def DeleteBackupMigration(self, request):
        """This API is used to delete a backup import task.

        :param request: Request instance for DeleteBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBusinessIntelligenceFile(self, request):
        """This API is used to delete a business intelligence service file.

        :param request: Request instance for DeleteBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDB(self, request):
        """This API is used to drop a database.

        :param request: Request instance for DeleteDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDB", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBInstance(self, request):
        """This API is used to release SQL server instances (eliminated immediately) in the recycle bin. The released instances will be physically terminated after being retained for a period of time. Their publish-subscribe relationships will be automatically disassociated, and their RO replicas will be automatically released.

        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIncrementalMigration(self, request):
        """This API is used to delete an incremental backup import task.

        :param request: Request instance for DeleteIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMigration(self, request):
        """This API is used to delete a migration task.

        :param request: Request instance for DeleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePublishSubscribe(self, request):
        """This API is used to delete the publish/subscribe relationship between two databases.

        :param request: Request instance for DeletePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivilegeByDB(self, request):
        """This API is used to query information on the account and permissions associated with the database.

        :param request: Request instance for DescribeAccountPrivilegeByDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountPrivilegeByDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountPrivilegeByDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivilegeByDB", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegeByDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """This API is used to pull the list of instance accounts.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsResponse`

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


    def DescribeBackupByFlowId(self, request):
        """This API is used to query the created backup details through the backup creation process ID. The process ID can be obtained through the CreateBackup API.

        :param request: Request instance for DescribeBackupByFlowId.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupByFlowId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupByFlowIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupCommand(self, request):
        """This API is used to query the commands of creating backups canonically.

        :param request: Request instance for DescribeBackupCommand.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupCommandRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupFiles(self, request):
        """This API is used to query the details of an unarchived backup.

        :param request: Request instance for DescribeBackupFiles.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupFilesResponse`

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


    def DescribeBackupMigration(self, request):
        """This API is used to create an incremental backup import task.

        :param request: Request instance for DescribeBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupMonitor(self, request):
        """This API is used to query backup space usage details.

        :param request: Request instance for DescribeBackupMonitor.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMonitorRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupStatistical(self, request):
        """This API is used to query the real-time statistics list of backups.

        :param request: Request instance for DescribeBackupStatistical.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupStatisticalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupStatisticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupStatistical", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupStatisticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummary(self, request):
        """This API is used to query the backup overview information of databases.

        :param request: Request instance for DescribeBackupSummary.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupSummaryRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupUploadSize(self, request):
        """This API is used to query the size of uploaded backup files. It is valid if the backup file type is `COS_UPLOAD` (the file is stored in COS).

        :param request: Request instance for DescribeBackupUploadSize.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupUploadSizeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupUploadSizeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupUploadSize", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupUploadSizeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackups(self, request):
        """This API is used to query the list of backups.

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsResponse`

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


    def DescribeBusinessIntelligenceFile(self, request):
        """This API is used to query the files required by business intelligence service.

        :param request: Request instance for DescribeBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCollationTimeZone(self, request):
        """This API is used to query the character set and time zone supported by the instance.

        :param request: Request instance for DescribeCollationTimeZone.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCollationTimeZoneRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCollationTimeZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCollationTimeZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCollationTimeZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBackupStatistical(self, request):
        """This API is used to query the real-time statistics list of cross-region backups.

        :param request: Request instance for DescribeCrossBackupStatistical.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossBackupStatisticalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossBackupStatisticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBackupStatistical", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBackupStatisticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossRegionZone(self, request):
        """This API is used to query the disaster recovery region and AZ of the secondary node based on the primary instance.

        :param request: Request instance for DescribeCrossRegionZone.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossRegionZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossRegionZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossRegions(self, request):
        """This API is used to query the target region for cross-region backups.

        :param request: Request instance for DescribeCrossRegions.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCharsets(self, request):
        """This API is used to query the database character sets supported by an instance.

        :param request: Request instance for DescribeDBCharsets.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBCharsetsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBCharsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCharsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCharsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceInter(self, request):
        """This API is used to query the information of the interconnected instances.

        :param request: Request instance for DescribeDBInstanceInter.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstanceInterRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstanceInterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceInter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceInterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """This API is used to query the list of instances.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesResponse`

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


    def DescribeDBInstancesAttribute(self, request):
        """This API is used to query the attributes of an instance.

        :param request: Request instance for DescribeDBInstancesAttribute.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBPrivilegeByAccount(self, request):
        """This API is used to query information on the databases and permissions associated with the account.

        :param request: Request instance for DescribeDBPrivilegeByAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBPrivilegeByAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBPrivilegeByAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBPrivilegeByAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBPrivilegeByAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBRestoreTime(self, request):
        """This API is used to query databases that can be rolled back.

        :param request: Request instance for DescribeDBRestoreTime.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBRestoreTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBRestoreTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBRestoreTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBRestoreTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group details of instances.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeDBs(self, request):
        """This API is used to query the list of databases

        :param request: Request instance for DescribeDBs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBsNormal(self, request):
        """This API is used to query database configurations. It does not return information of the accounts that have permissions to operate the database.

        :param request: Request instance for DescribeDBsNormal.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsNormalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsNormalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBsNormal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBsNormalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseNames(self, request):
        """This API is used to query the database name associated with the account.

        :param request: Request instance for DescribeDatabaseNames.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabaseNamesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabaseNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseNames", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseNamesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """This API is used to query the database list.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesResponse`

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


    def DescribeDatabasesNormal(self, request):
        """This API is used to query database configuration information. This API does not contain accounts associated with databases.

        :param request: Request instance for DescribeDatabasesNormal.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesNormalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesNormalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabasesNormal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesNormalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowStatus(self, request):
        """This API is used to query flow status.

        :param request: Request instance for DescribeFlowStatus.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHASwitchLog(self, request):
        """This API is used to perform the manual primary-secondary switch.

        :param request: Request instance for DescribeHASwitchLog.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeHASwitchLogRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeHASwitchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHASwitchLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHASwitchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementalMigration(self, request):
        """This API is used to query an incremental backup import task.

        :param request: Request instance for DescribeIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceByOrders(self, request):
        """This API is used to query the instance ID by the order number.

        :param request: Request instance for DescribeInstanceByOrders.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceByOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceByOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceByOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceByOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        """This API is used to query the parameter modification records of an instance.

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamRecordsResponse`

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
        """This API is used to query the parameter list of an instance.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamsResponse`

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


    def DescribeInstanceTasks(self, request):
        """This API is used to query the list of asynchronous tasks related to an instance.

        :param request: Request instance for DescribeInstanceTasks.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTasksRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTradeParameter(self, request):
        """This API is used to query the instance billing parameters.

        :param request: Request instance for DescribeInstanceTradeParameter.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTradeParameterRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTradeParameterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTradeParameter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTradeParameterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaintenanceSpan(self, request):
        """This API is used to query the maintenance time window of an instance based on its instance ID.

        :param request: Request instance for DescribeMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintenanceSpan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintenanceSpanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDatabases(self, request):
        """This API is used to query the list of databases to be migrated.

        :param request: Request instance for DescribeMigrationDatabases.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDetail(self, request):
        """This API is used to query migration task details.

        :param request: Request instance for DescribeMigrationDetail.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrations(self, request):
        """This API is used to query the list of eligible migration tasks based on the entered criteria.

        :param request: Request instance for DescribeMigrations.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """This API is used to query order information.

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersResponse`

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


    def DescribeProductConfig(self, request):
        """This API is used to query purchasable specification configuration.

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query security group details of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribePublishSubscribe(self, request):
        """This API is used to query the publish/subscribe relationship list.

        :param request: Request instance for DescribePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupAutoWeight(self, request):
        """This API is used to query the automatic weight assignment result of the read-only group. The BalanceReadOnlyGroup API is used to perform routing weight assignment according to the automatic weight assignment result.

        :param request: Request instance for DescribeReadOnlyGroupAutoWeight.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupAutoWeightRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupAutoWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupAutoWeight", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupAutoWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupByReadOnlyInstance(self, request):
        """This API is used to query the read-only group where the read-only instance is located by its ID.

        :param request: Request instance for DescribeReadOnlyGroupByReadOnlyInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupByReadOnlyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupByReadOnlyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupDetails(self, request):
        """This API is used to query read-only group details.

        :param request: Request instance for DescribeReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupList(self, request):
        """This API is used to query the read-only group list.

        :param request: Request instance for DescribeReadOnlyGroupList.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to query purchasable regions.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegularBackupPlan(self, request):
        """This API is used to query the scheduled backup retention plans of instances.

        :param request: Request instance for DescribeRegularBackupPlan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegularBackupPlanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegularBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegularBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegularBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTask(self, request):
        """This API is used to query the list of rollback tasks.

        :param request: Request instance for DescribeRestoreTask.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTaskRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTimeRange(self, request):
        """This API is used to query the time range available for rollback by time point.

        :param request: Request instance for DescribeRestoreTimeRange.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTimeRangeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTimeRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTimeRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTime(self, request):
        """This API is used to query the time range available for instance rollback.

        :param request: Request instance for DescribeRollbackTime.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowlogs(self, request):
        """This API is used to get file information of slow query logs.

        :param request: Request instance for DescribeSlowlogs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecSellStatus(self, request):
        """This API is used to query the status information on specifications, including the sales status and reference price. (The actual price is subject to the result returned by price querying APIs.)

        :param request: Request instance for DescribeSpecSellStatus.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSpecSellStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSpecSellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecSellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecSellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpgradeInstanceCheck(self, request):
        """This API is used to pre-check the impact of the instance configuration adjustment before the adjustment.

        :param request: Request instance for DescribeUpgradeInstanceCheck.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUpgradeInstanceCheckRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUpgradeInstanceCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpgradeInstanceCheck", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpgradeInstanceCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadBackupInfo(self, request):
        """This API is used to query a backup upload permission.

        :param request: Request instance for DescribeUploadBackupInfo.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadBackupInfoRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadBackupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadBackupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadBackupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeXEvents(self, request):
        """This API is used to query the list of extended events.

        :param request: Request instance for DescribeXEvents.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeXEventsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeXEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeXEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeXEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query currently purchasable AZs.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API is used to unbind security groups from instances in batches.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsResponse`

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


    def InquiryPriceCreateDBInstances(self, request):
        """This API is used to query the price of requested instances.

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpgradeDBInstance(self, request):
        """This API is used to query the upgrade prices of a monthly subscribed instance.
        .

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpgradeDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpgradeDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivilege(self, request):
        """This API is used to modify instance account permissions.

        :param request: Request instance for ModifyAccountPrivilege.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountRemark(self, request):
        """This API is used to modify account remarks.

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupMigration(self, request):
        """This API is used to modify a backup import task.

        :param request: Request instance for ModifyBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupName(self, request):
        """This API is used to modify the name of a backup task.

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupStrategy(self, request):
        """This API is used to modify the backup policy.

        :param request: Request instance for ModifyBackupStrategy.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloseWanIp(self, request):
        """This API is used to disable the public network for the instance.

        :param request: Request instance for ModifyCloseWanIp.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCloseWanIpRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCloseWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloseWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloseWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCrossBackupStrategy(self, request):
        """This API is used to enable or disable cross-region backup policies.

        :param request: Request instance for ModifyCrossBackupStrategy.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCrossBackupStrategyRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCrossBackupStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCrossBackupStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCrossBackupStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBEncryptAttributes(self, request):
        """This API is used to enable or disable TDE of a database.

        :param request: Request instance for ModifyDBEncryptAttributes.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBEncryptAttributesResponse`

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
        """This API is used to rename an instance.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceNetwork(self, request):
        """This API is used to switch a running instance from a VPC to another.

        :param request: Request instance for ModifyDBInstanceNetwork.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceNote(self, request):
        """This API is used to modify the instance remarks.

        :param request: Request instance for ModifyDBInstanceNote.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNoteRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNoteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNote", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNoteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceProject(self, request):
        """This API is used to modify the project to which a database instance belongs.

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectResponse`

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


    def ModifyDBInstanceSSL(self, request):
        """This API is used to enable/disable/update SSL encryption.

        :param request: Request instance for ModifyDBInstanceSSL.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSSLRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSSL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify security groups bound to an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBName(self, request):
        """This API is used to rename a database.

        :param request: Request instance for ModifyDBName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBRemark(self, request):
        """This API is used to modify database remarks.

        :param request: Request instance for ModifyDBRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDReadable(self, request):
        """This API is used to enable or disable the read-only feature of the replica server.

        :param request: Request instance for ModifyDReadable.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDReadableRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDReadableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDReadable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDReadableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseCDC(self, request):
        """This API is used to enable or disable the change data capture (CDC) feature.

        :param request: Request instance for ModifyDatabaseCDC.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCDCRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCDCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseCDC", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseCDCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseCT(self, request):
        """This API is used to enable or disable the change tracking (CT) feature.

        :param request: Request instance for ModifyDatabaseCT.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCTRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCTResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseCT", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseCTResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseMdf(self, request):
        """This API is used to shrink database MDF files.

        :param request: Request instance for ModifyDatabaseMdf.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseMdfRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseMdfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseMdf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseMdfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabasePrivilege(self, request):
        """This API is used to modify instance database permissions.

        :param request: Request instance for ModifyDatabasePrivilege.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabasePrivilegeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabasePrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabasePrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabasePrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseShrinkMDF(self, request):
        """This API is used to shrink the database mdf (Shrink mdf).

        :param request: Request instance for ModifyDatabaseShrinkMDF.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseShrinkMDFRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseShrinkMDFResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseShrinkMDF", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseShrinkMDFResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIncrementalMigration(self, request):
        """This API is used to modify an incremental backup import task.

        :param request: Request instance for ModifyIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceEncryptAttributes(self, request):
        """This API is used to enable TDE of an instance.

        :param request: Request instance for ModifyInstanceEncryptAttributes.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """This API is used to modify instance parameters.
        <b>Note</b>: if <b>the instance needs to be restarted</b> for the modified parameter to take effect, <b>it will be restarted</b> immediately or during the maintenance time according to the `WaitSwitch` parameter.
        Before you modify a parameter, you can use the `DescribeInstanceParams` API to query whether the instance needs to be restarted.

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceParamResponse`

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


    def ModifyMaintenanceSpan(self, request):
        """This API is used to modify the maintenance window of the instance.

        :param request: Request instance for ModifyMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintenanceSpan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintenanceSpanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigration(self, request):
        """This API is used to modify an existing migration task.

        :param request: Request instance for ModifyMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOpenWanIp(self, request):
        """This API is used to enable the public network for the instance.

        :param request: Request instance for ModifyOpenWanIp.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyOpenWanIpRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyOpenWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOpenWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOpenWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublishSubscribe(self, request):
        """This API is used to modify the publish/subscribe relationship of the instance.

        :param request: Request instance for ModifyPublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublishSubscribeName(self, request):
        """This API is used to modify the publish/subscribe names.

        :param request: Request instance for ModifyPublishSubscribeName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublishSubscribeName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublishSubscribeNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReadOnlyGroupDetails(self, request):
        """This API is used to modify read-only group details.

        :param request: Request instance for ModifyReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReadOnlyGroupDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReadOnlyGroupDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenInterCommunication(self, request):
        """This API is used to enable instance interconnection, which can interconnect business intelligence services.

        :param request: Request instance for OpenInterCommunication.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.OpenInterCommunicationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.OpenInterCommunicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenInterCommunication", params, headers=headers)
            response = json.loads(body)
            model = models.OpenInterCommunicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecycleDBInstance(self, request):
        """This API is used to return a deactivated SQL Server instance.

        :param request: Request instance for RecycleDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecycleDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RecycleDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecycleReadOnlyGroup(self, request):
        """This API is used to reclaim resources of read-only groups immediately. The resources, such as VIP, occupied by the read-only group will be released immediately and cannot be recovered.

        :param request: Request instance for RecycleReadOnlyGroup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecycleReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RecycleReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveBackups(self, request):
        """This API is used to delete backup files created by users manually. The backup policy to be deleted can be instance backup or multi-database backup.

        :param request: Request instance for RemoveBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveBackups", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewPostpaidDBInstance(self, request):
        """This API is used to recover the pay-as-you-go instance that is manually isolated through the API TerminateDBInstance from the recycle bin.

        :param request: Request instance for RenewPostpaidDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewPostpaidDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewPostpaidDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """This API is used to reset the account password of an instance.

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordResponse`

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


    def RestartDBInstance(self, request):
        """This API is used to restart a database instance.

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreInstance(self, request):
        """This API is used to roll back the database by backup set.

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackInstance(self, request):
        """This API is used to roll back the instance by time point.

        :param request: Request instance for RollbackInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunMigration(self, request):
        """This API is used to start running a migration task.

        :param request: Request instance for RunMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunMigration", params, headers=headers)
            response = json.loads(body)
            model = models.RunMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBackupMigration(self, request):
        """This API is used to start a backup import task.

        :param request: Request instance for StartBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.StartBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartIncrementalMigration(self, request):
        """This API is used to start an incremental backup import task.

        :param request: Request instance for StartIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.StartIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstanceXEvent(self, request):
        """This API is used to start and stop an extended event.

        :param request: Request instance for StartInstanceXEvent.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartInstanceXEventRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartInstanceXEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstanceXEvent", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstanceXEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchCloudInstanceHA(self, request):
        """This API is used to manually switch between primary and secondary.

        :param request: Request instance for SwitchCloudInstanceHA.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.SwitchCloudInstanceHARequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SwitchCloudInstanceHAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchCloudInstanceHA", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchCloudInstanceHAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDBInstance(self, request):
        """This API is used to isolate an instance to move it into a recycle bin.

        :param request: Request instance for TerminateDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """This API is used to upgrade an instance.

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceResponse`

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