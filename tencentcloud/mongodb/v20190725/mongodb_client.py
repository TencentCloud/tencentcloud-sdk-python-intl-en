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
from tencentcloud.mongodb.v20190725 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2019-07-25'
    _endpoint = 'mongodb.intl.tencentcloudapi.com'
    _service = 'mongodb'


    def AssignProject(self, request):
        r"""This API is used to specify the project of a TencentDB for MongoDB instance.

        :param request: Request instance for AssignProject.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignProject", params, headers=headers)
            response = json.loads(body)
            model = models.AssignProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccountUser(self, request):
        r"""This API is used to customize an account to access the instance.

        :param request: Request instance for CreateAccountUser.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateAccountUserRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateAccountUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccountUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupDBInstance(self, request):
        r"""This API is used to back up an instance.

        :param request: Request instance for CreateBackupDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupDownloadTask(self, request):
        r"""This API is used to create a backup download task.

        :param request: Request instance for CreateBackupDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstance(self, request):
        r"""This API is used to create a yearly/monthly subscription TencentDB for MongoDB instance. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/35767?from_cn_redirect=1) API can be called to query and obtain the supported sales specifications.

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceResponse`

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
        r"""This API is used to create a pay-as-you-go TencentDB for MongoDB instance.

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourResponse`

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


    def CreateLogDownloadTask(self, request):
        r"""This API is used to create a log download task.

        :param request: Request instance for CreateLogDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateLogDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateLogDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccountUser(self, request):
        r"""This API is used to delete a custom account of an instance.

        :param request: Request instance for DeleteAccountUser.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DeleteAccountUserRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DeleteAccountUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccountUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogDownloadTask(self, request):
        r"""This API is used to delete a log download task.

        :param request: Request instance for DeleteLogDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DeleteLogDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DeleteLogDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsyncRequestInfo(self, request):
        r"""This API is used to query the asynchronous task status.

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoResponse`

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


    def DescribeBackupDownloadTask(self, request):
        r"""This API is used to query information about the backup download task.

        :param request: Request instance for DescribeBackupDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupRules(self, request):
        r"""This API is used to obtain the automatic backup configuration information of an instance.

        :param request: Request instance for DescribeBackupRules.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupRulesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientConnections(self, request):
        r"""This API is used to query the client connection information on an instance, including the IP address for connection and the number of connections.

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurrentOp(self, request):
        r"""This API is used to query the operation currently being performed on a TencentDB for MongoDB instance.

        :param request: Request instance for DescribeCurrentOp.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeCurrentOpRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeCurrentOpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentOp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentOpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBBackups(self, request):
        r"""This API is used to query the list of instance backups. Currently, only backups created in the last seven days can be queried.

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceDeal(self, request):
        r"""This API is used to get order details of purchase, renewal, and specification adjustment of a MongoDB instance.

        :param request: Request instance for DescribeDBInstanceDeal.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceDeal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceDealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceNamespace(self, request):
        r"""This API is used to query the table information on a database.

        :param request: Request instance for DescribeDBInstanceNamespace.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNamespaceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceNodeProperty(self, request):
        r"""This API is used to query node attributes, such as the AZ, node name, address, role, status, delay between primary and secondary nodes, priority, voting right, and tags.

        :param request: Request instance for DescribeDBInstanceNodeProperty.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNodePropertyRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNodePropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceNodeProperty", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceNodePropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        r"""This API is used to query the list of TencentDB for MongoDB instances. It supports filtering primary instances, disaster recovery instances, and read-only instances by project ID, instance ID, instance status, and other conditions.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesResponse`

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


    def DescribeDetailedSlowLogs(self, request):
        r"""This API is used to query slow log details of the instance.

        :param request: Request instance for DescribeDetailedSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDetailedSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDetailedSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetailedSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetailedSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        r"""This API is used to query the list of parameters that can be modified for the current instance.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceParamsResponse`

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


    def DescribeInstanceSSL(self, request):
        r"""This API is used to view the enabling status of Secure Sockets Layer (SSL) for an instance.

        :param request: Request instance for DescribeInstanceSSL.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceSSLRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSSL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogDownloadTasks(self, request):
        r"""This API is used to query a log download task.

        :param request: Request instance for DescribeLogDownloadTasks.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeLogDownloadTasksRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeLogDownloadTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogDownloadTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogDownloadTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMongodbLogs(self, request):
        r"""This API is used to query running logs.

        :param request: Request instance for DescribeMongodbLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeMongodbLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeMongodbLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMongodbLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMongodbLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroup(self, request):
        r"""This API is used to query security groups bound to an instance.

        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogPatterns(self, request):
        r"""This API is used to get the slow log statistics of a database instance.

        :param request: Request instance for DescribeSlowLogPatterns.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogPatterns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogPatternsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        r"""This API is used to get the slow log information of a TencentDB instance. Only slow logs for the last 7 days can be queried.

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsResponse`

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


    def DescribeSpecInfo(self, request):
        r"""This API is used to query the sales specification of an instance.

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTransparentDataEncryption(self, request):
        r"""This API is used to enable the transparent data encryption (TDE) capability for TencentDB for MongoDB.

        :param request: Request instance for EnableTransparentDataEncryption.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.EnableTransparentDataEncryptionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.EnableTransparentDataEncryptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTransparentDataEncryption", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTransparentDataEncryptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FlushInstanceRouterConfig(self, request):
        r"""This API is used to run the `FlushRouterConfig` command on all mongos instances.

        :param request: Request instance for FlushInstanceRouterConfig.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlushInstanceRouterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.FlushInstanceRouterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDBInstances(self, request):
        r"""This API is used to query price of instance creation. The `region` parameter must be passed in this API, otherwise verification will fail. This API allows queries only for purchasable instance specifications.

        :param request: Request instance for InquirePriceCreateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceModifyDBInstanceSpec(self, request):
        r"""This API is used to query the price of instance specification adjustment.

        :param request: Request instance for InquirePriceModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceModifyDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceModifyDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewDBInstances(self, request):
        r"""This API is used to query the renewal price of a monthly subscription instance.

        :param request: Request instance for InquirePriceRenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstanceEnableSSL(self, request):
        r"""This API is used to set the SSL status for an instance.

        :param request: Request instance for InstanceEnableSSL.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InstanceEnableSSLRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InstanceEnableSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstanceEnableSSL", params, headers=headers)
            response = json.loads(body)
            model = models.InstanceEnableSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBInstance(self, request):
        r"""This API is used to isolate a pay-as-you-go TencentDB for MongoDB instance. After isolation, the instance is retained in the recycle bin, and data cannot be written into it. After a certain period of isolation, the instance is deleted permanently. For the retention time in the recycle bin, see the pay-as-you-go service terms. The deleted pay-as-you-go instance cannot be recovered. Proceed with caution.

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceResponse`

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


    def KillOps(self, request):
        r"""This API is used to terminate a specific operation performed on a TencentDB for MongoDB instance.

        :param request: Request instance for KillOps.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.KillOpsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.KillOpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillOps", params, headers=headers)
            response = json.loads(body)
            model = models.KillOpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceNetworkAddress(self, request):
        r"""This API is used to modify the network information on a TencentDB for MongoDB instance. It supports switching from a basic network to a VPC network or from one VPC network to another VPC network.

        :param request: Request instance for ModifyDBInstanceNetworkAddress.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceNetworkAddressRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceNetworkAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNetworkAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNetworkAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroup(self, request):
        r"""This API is used to modify security groups bound to an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroup.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSpec(self, request):
        r"""This API is used to adjust the TencentDB for MongoDB instance configuration. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to query and obtain the supported sales specifications.

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParams(self, request):
        r"""This API is used to modify the parameter configuration of a TencentDB for MongoDB instance.

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineIsolatedDBInstance(self, request):
        r"""This API is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status.

        :param request: Request instance for OfflineIsolatedDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineIsolatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineIsolatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameInstance(self, request):
        r"""This API is used to rename a TencentDB instance.

        :param request: Request instance for RenameInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenameInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBInstances(self, request):
        r"""This API is used to renew a monthly subscription TencentDB instance. Only monthly subscription instances are supported, while pay-as-you-go instances do not need to be renewed.

        :param request: Request instance for RenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDBInstancePassword(self, request):
        r"""This API is used to reset the instance access password.

        :param request: Request instance for ResetDBInstancePassword.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDBInstancePassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDBInstancePasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAccountUserPrivilege(self, request):
        r"""This API is used to set the account permissions of an instance.

        :param request: Request instance for SetAccountUserPrivilege.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetAccountUserPrivilegeRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetAccountUserPrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAccountUserPrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.SetAccountUserPrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetDBInstanceDeletionProtection(self, request):
        r"""This API is used to set instance termination protection.

        :param request: Request instance for SetDBInstanceDeletionProtection.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetDBInstanceDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetDBInstanceDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDBInstanceDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.SetDBInstanceDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetInstanceMaintenance(self, request):
        r"""This API is used to set the instance maintenance window.

        :param request: Request instance for SetInstanceMaintenance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetInstanceMaintenanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetInstanceMaintenanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetInstanceMaintenance", params, headers=headers)
            response = json.loads(body)
            model = models.SetInstanceMaintenanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDBInstances(self, request):
        r"""This API is used to terminate monthly subscription billing instances.

        :param request: Request instance for TerminateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.TerminateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.TerminateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstanceKernelVersion(self, request):
        r"""This API is used to upgrade the kernel version of the database instance.

        :param request: Request instance for UpgradeDBInstanceKernelVersion.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDBInstanceKernelVersionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDBInstanceKernelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceKernelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceKernelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDbInstanceVersion(self, request):
        r"""This API is used to upgrade the database kernel across versions. Currently, it is only supported to upgrade from version 3.6 to 4.0, 4.0 to 4.2, 4.2 to 4.4, and 4.4 to 5.0.

        :param request: Request instance for UpgradeDbInstanceVersion.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDbInstanceVersionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDbInstanceVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDbInstanceVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDbInstanceVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))