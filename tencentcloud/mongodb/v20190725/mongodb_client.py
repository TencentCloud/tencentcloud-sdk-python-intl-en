# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
    _endpoint = 'mongodb.tencentcloudapi.com'
    _service = 'mongodb'


    def AssignProject(self, request):
        """This API is used to specify the project to which a TencentDB instance belongs.

        :param request: Request instance for AssignProject.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBackupDBInstance(self, request):
        """This API is used to create instance backups.

        :param request: Request instance for CreateBackupDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackupDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBInstance(self, request):
        """This API is used to create a monthly subscription TencentDB for MongoDB instance. The purchasable specifications supported by this API can be obtained through the `DescribeSpecInfo` API.

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBInstanceHour(self, request):
        """This API is used to create a pay-as-you-go TencentDB for MongoDB instance.

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceHourResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAsyncRequestInfo(self, request):
        """This API is used to query async task status.

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsyncRequestInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAsyncRequestInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupAccess(self, request):
        """This API is used to get the permission to download a backup file. The specific backup file information can be obtained through the DescribeDBBackups API.

        :param request: Request instance for DescribeBackupAccess.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupAccessRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupAccessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClientConnections(self, request):
        """This API is used to query the client connection information of an instance, including the IP and number of connections. Currently, only instances of MongoDB 3.2 are supported.

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientConnectionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBBackups(self, request):
        """This API is used to query the list of instance backups. Currently, only backups in the last 7 days can be queried.

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBBackupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstanceDeal(self, request):
        """This API is used to get details of purchase, renewal, and specification adjustment orders of a MongoDB instance.

        :param request: Request instance for DescribeDBInstanceDeal.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceDeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceDealResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstances(self, request):
        """This API is used to query the list of TencentDB instances (which can be primary, disaster recovery, or read-only instances). It supports filtering instances by project ID, instance ID, and instance status.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSlowLogPatterns(self, request):
        """This API is used to get the slow log statistics of a database instance.

        :param request: Request instance for DescribeSlowLogPatterns.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogPatterns", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogPatternsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSlowLogs(self, request):
        """This API is used to get the slow log information of a TencentDB instance. Only slow logs for the last 7 days can be queried.

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpecInfo(self, request):
        """This API is used to query the purchasable instance specifications.

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSpecInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpecInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FlushInstanceRouterConfig(self, request):
        """This API is used to run the `FlushRouterConfig` command on all mongos instances.

        :param request: Request instance for FlushInstanceRouterConfig.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FlushInstanceRouterConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlushInstanceRouterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquirePriceCreateDBInstances(self, request):
        """This API is used to query price of instance creation. The `region` parameter must be passed in this API, otherwise verification will fail. This API allows queries only for purchasable instance specifications.

        :param request: Request instance for InquirePriceCreateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceCreateDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquirePriceModifyDBInstanceSpec(self, request):
        """This API is used to query price of instance specification adjustment.

        :param request: Request instance for InquirePriceModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceModifyDBInstanceSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceModifyDBInstanceSpecResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquirePriceRenewDBInstances(self, request):
        """This API is used to query the renewal price of a monthly subscription instance.

        :param request: Request instance for InquirePriceRenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceRenewDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceRenewDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateDBInstance(self, request):
        """This API is used to isolate a pay-as-you-go TencentDB for MongoDB instance. An isolated instance is retained in the recycle bin and data can no longer be written to it. After it is isolated for a certain period of time, it will be completely deleted. For the retention period in the recycle bin, please see the terms of service for pay-as-you-go billing. Isolated pay-as-you-go instances cannot be recovered, so please proceed with caution.

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSpec(self, request):
        """This API is used to adjust the specification configuration of a TencentDB for MongoDB. The purchasable specifications supported by the API can be obtained through the DescribeSpecInfo API.

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSpecResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OfflineIsolatedDBInstance(self, request):
        """This API is used to deactivate isolated TencentDB instances immediately. The instances must be in isolated status.

        :param request: Request instance for OfflineIsolatedDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OfflineIsolatedDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineIsolatedDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenameInstance(self, request):
        """This API is used to rename a TencentDB instance.

        :param request: Request instance for RenameInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenameInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenameInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewDBInstances(self, request):
        """This API is used to renew a monthly subscription TencentDB instance. Only monthly subscription instances are supported, while pay-as-you-go instances do not need to be renewed.

        :param request: Request instance for RenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetDBInstancePassword(self, request):
        """This API is used to modify instance password.

        :param request: Request instance for ResetDBInstancePassword.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDBInstancePassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDBInstancePasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)