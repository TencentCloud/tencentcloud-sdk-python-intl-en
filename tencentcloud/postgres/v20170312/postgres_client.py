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
from tencentcloud.postgres.v20170312 import models


class PostgresClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'postgres.tencentcloudapi.com'
    _service = 'postgres'


    def AddDBInstanceToReadOnlyGroup(self, request):
        """This API is used to add a read-only replica to an RO group.

        :param request: Request instance for AddDBInstanceToReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.AddDBInstanceToReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.AddDBInstanceToReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDBInstanceToReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDBInstanceToReadOnlyGroupResponse()
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


    def CloseDBExtranetAccess(self, request):
        """This API is used to disable the public network link to an instance.

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
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


    def CloseServerlessDBExtranetAccess(self, request):
        """This API is used to disable public network access for a PostgreSQL for Serverless instance.

        :param request: Request instance for CloseServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseServerlessDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseServerlessDBExtranetAccessResponse()
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


    def CreateDBInstances(self, request):
        """This API is used to create (but not initialize) one or more TencentDB for PostgreSQL instances.

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstancesResponse()
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


    def CreateInstances(self, request):
        """This API is used to create and initialize one or more TencentDB for PostgreSQL instances.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstancesResponse()
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


    def CreateReadOnlyDBInstance(self, request):
        """This API is used to create read-only replicas.

        :param request: Request instance for CreateReadOnlyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReadOnlyDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReadOnlyDBInstanceResponse()
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


    def CreateReadOnlyGroup(self, request):
        """This API is used to create an RO group.

        :param request: Request instance for CreateReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReadOnlyGroupResponse()
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


    def CreateServerlessDBInstance(self, request):
        """This API is used to create a PostgreSQL for Serverless instance. If the creation succeeds, the instance ID will be returned.

        :param request: Request instance for CreateServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServerlessDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServerlessDBInstanceResponse()
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


    def DeleteReadOnlyGroup(self, request):
        """This API is used to delete an RO group.

        :param request: Request instance for DeleteReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReadOnlyGroupResponse()
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


    def DeleteServerlessDBInstance(self, request):
        """This API is used to delete a PostgreSQL for Serverless instance.

        :param request: Request instance for DeleteServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServerlessDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServerlessDBInstanceResponse()
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


    def DescribeAccounts(self, request):
        """This API is used to get the instance user list.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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
        """This API is used to query the instance backup list.

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsResponse`

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


    def DescribeDBErrlogs(self, request):
        """This API is used to get error logs.

        :param request: Request instance for DescribeDBErrlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBErrlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBErrlogsResponse()
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


    def DescribeDBInstanceAttribute(self, request):
        """This API is used to query the details of one instance.

        :param request: Request instance for DescribeDBInstanceAttribute.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceAttributeResponse()
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
        """This API is used to query the details of one or more instances.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBSlowlogs(self, request):
        """This API is used to get slow query logs.

        :param request: Request instance for DescribeDBSlowlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowlogsResponse()
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


    def DescribeDBXlogs(self, request):
        """This API is used to get the instance Xlog list.

        :param request: Request instance for DescribeDBXlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBXlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBXlogsResponse()
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


    def DescribeDatabases(self, request):
        """This API is used to pull the list of databases.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeOrders(self, request):
        """This API is used to get order information.

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
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


    def DescribeProductConfig(self, request):
        """This API is used to query the purchasable specification configuration.

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductConfigResponse()
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


    def DescribeReadOnlyGroups(self, request):
        """This API is used to query RO group information by specifying the primary instance IDs.

        :param request: Request instance for DescribeReadOnlyGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReadOnlyGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReadOnlyGroupsResponse()
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


    def DescribeRegions(self, request):
        """This API is used to query the purchasable regions.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeServerlessDBInstances(self, request):
        """This API is used to query the details of one or more PostgreSQL for Serverless instances.

        :param request: Request instance for DescribeServerlessDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessDBInstancesResponse()
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


    def DescribeZones(self, request):
        """This API is used to query the supported AZs.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def DestroyDBInstance(self, request):
        """This API is used to eliminate an isolated instance by specifying the `DBInstanceId` parameter. The data of an eliminated instance will be deleted and cannot be recovered.

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyDBInstanceResponse()
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


    def DisIsolateDBInstances(self, request):
        """This API is used to remove one or more instances from isolation.

        :param request: Request instance for DisIsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisIsolateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisIsolateDBInstancesResponse()
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


    def InitDBInstances(self, request):
        """This API is used to initialize a TencentDB for PostgreSQL instance.

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def InquiryPriceCreateDBInstances(self, request):
        """This API is used to query the purchase price of one or multiple instances.

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDBInstancesResponse()
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


    def InquiryPriceRenewDBInstance(self, request):
        """This API is used to query the renewal price of an instance.

        :param request: Request instance for InquiryPriceRenewDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewDBInstanceResponse()
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


    def InquiryPriceUpgradeDBInstance(self, request):
        """This API is used to query the upgrade price of an instance.

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeDBInstanceResponse()
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


    def IsolateDBInstances(self, request):
        """This API is used to isolate one or more instances.

        :param request: Request instance for IsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstancesResponse()
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


    def ModifyAccountRemark(self, request):
        """This API is used to modify account remarks.

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountRemarkResponse()
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


    def ModifyDBInstanceName(self, request):
        """This API is used to rename a TencentDB for PostgreSQL instance.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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


    def ModifyDBInstanceReadOnlyGroup(self, request):
        """This API is used to modify the RO group of an instance.

        :param request: Request instance for ModifyDBInstanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceReadOnlyGroupResponse()
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


    def ModifyDBInstancesProject(self, request):
        """This API is used to transfer an instance to another project.

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
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


    def ModifyReadOnlyGroupConfig(self, request):
        """This API is used to modify RO group configuration.

        :param request: Request instance for ModifyReadOnlyGroupConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyReadOnlyGroupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyReadOnlyGroupConfigResponse()
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


    def OpenDBExtranetAccess(self, request):
        """This API is used to enable public network access.

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
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


    def OpenServerlessDBExtranetAccess(self, request):
        """This API is used to enable public network access for a PostgreSQL for Serverless instance.

        :param request: Request instance for OpenServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenServerlessDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenServerlessDBExtranetAccessResponse()
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


    def RebalanceReadOnlyGroup(self, request):
        """This API is used to rebalance the loads of read-only replicas in an RO group. Please note that connections to those read-only replicas will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.

        :param request: Request instance for RebalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebalanceReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebalanceReadOnlyGroupResponse()
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


    def RemoveDBInstanceFromReadOnlyGroup(self, request):
        """This API is used to remove a read-only replica from an RO group.

        :param request: Request instance for RemoveDBInstanceFromReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveDBInstanceFromReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveDBInstanceFromReadOnlyGroupResponse()
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


    def RenewInstance(self, request):
        """This API is used to renew an instance.

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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


    def ResetAccountPassword(self, request):
        """This API is used to reset the account password of an instance.

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
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


    def RestartDBInstance(self, request):
        """This API is used to restart an instance.

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstanceResponse()
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


    def SetAutoRenewFlag(self, request):
        """This API is used to set auto-renewal.

        :param request: Request instance for SetAutoRenewFlag.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAutoRenewFlagResponse()
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


    def UpgradeDBInstance(self, request):
        """This API is used to upgrade an instance.

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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