# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
            headers = request.headers
            body = self.call("AddDBInstanceToReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddDBInstanceToReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneDBInstance(self, request):
        """This API is used to clone an instance by specifying a backup set or a point in time.

        :param request: Request instance for CloneDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloneDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloneDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CloneDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseDBExtranetAccess(self, request):
        """This API is used to disable the public network address of an instance.

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CloseDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseServerlessDBExtranetAccess(self, request):
        """This API is used to disable the public network address of a PostgreSQL for Serverless instance.

        :param request: Request instance for CloseServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseServerlessDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CloseServerlessDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaseBackup(self, request):
        """This API is used to create a full backup of an instance.

        :param request: Request instance for CreateBaseBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateBaseBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateBaseBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaseBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaseBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstanceNetworkAccess(self, request):
        """This API is used to create a network for an instance.

        :param request: Request instance for CreateDBInstanceNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstanceNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstanceNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstances(self, request):
        """This API is used to create (but not initialize) one or more TencentDB for PostgreSQL instances. This API is disused and replaced by the [CreateInstances](https://intl.cloud.tencent.com/document/api/409/56107?from_cn_redirect=1) API.

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesResponse`

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


    def CreateInstances(self, request):
        """This API is used to create and initialize one or more TencentDB for PostgreSQL instances.
        <li>After an instance is created successfully, it will start up automatically and enter the "Running" status.
        <li>If you create a monthly subscribed instance, you will be billed for the instance before the creation; if you create a pay-as-you-go instance billed on an hourly basis, the amount equivalent to the hourly rate will be frozen before the creation. Make sure your account balance is sufficient before calling this API.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParameterTemplate(self, request):
        """This API is used to create a parameter template.

        :param request: Request instance for CreateParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyDBInstance(self, request):
        """This API is used to create read-only replicas.

        :param request: Request instance for CreateReadOnlyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyGroup(self, request):
        """This API is used to create an RO group.

        :param request: Request instance for CreateReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyGroupNetworkAccess(self, request):
        """This API is used to create a network for an RO group.

        :param request: Request instance for CreateReadOnlyGroupNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyGroupNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyGroupNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerlessDBInstance(self, request):
        """This API is used to create a PostgreSQL for Serverless instance. If the creation succeeds, the instance ID will be returned.

        :param request: Request instance for CreateServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerlessDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerlessDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaseBackup(self, request):
        """This API is used to delete the specified full backup of an instance.

        :param request: Request instance for DeleteBaseBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteBaseBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteBaseBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaseBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaseBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBInstanceNetworkAccess(self, request):
        """This API is used to delete a network of an instance.

        :param request: Request instance for DeleteDBInstanceNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteDBInstanceNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteDBInstanceNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBInstanceNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBInstanceNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogBackup(self, request):
        """This API is used to delete the specified log backup of an instance.

        :param request: Request instance for DeleteLogBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteLogBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteLogBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParameterTemplate(self, request):
        """This API is used to delete a parameter template.

        :param request: Request instance for DeleteParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReadOnlyGroup(self, request):
        """This API is used to delete an RO group.

        :param request: Request instance for DeleteReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReadOnlyGroupNetworkAccess(self, request):
        """This API is used to delete a network of an RO group.

        :param request: Request instance for DeleteReadOnlyGroupNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReadOnlyGroupNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReadOnlyGroupNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServerlessDBInstance(self, request):
        """This API is used to delete a PostgreSQL for Serverless instance.

        :param request: Request instance for DeleteServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServerlessDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServerlessDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """This API is used to query the list of the database accounts for an instance.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsResponse`

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


    def DescribeAvailableRecoveryTime(self, request):
        """This API is used to query the available restoration time of an instance.

        :param request: Request instance for DescribeAvailableRecoveryTime.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAvailableRecoveryTimeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAvailableRecoveryTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableRecoveryTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableRecoveryTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadRestriction(self, request):
        """This API is used to query the backup download restrictions.

        :param request: Request instance for DescribeBackupDownloadRestriction.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadURL(self, request):
        """u200cThis API is used to query the download address of a specified backup set, including full backup sets and incremental log backup sets.

        :param request: Request instance for DescribeBackupDownloadURL.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadURLRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupOverview(self, request):
        """This API is used to query the backup overview. It will return the current number and size of backups, free backup space size, and paid backup space size (all size values are in bytes).

        :param request: Request instance for DescribeBackupOverview.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupOverviewRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupPlans(self, request):
        """This API is used to query all backup plans of an instance.

        :param request: Request instance for DescribeBackupPlans.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupPlansRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummaries(self, request):
        """This API is used to query the backup statistics of an instance. It will return the number and size (bytes) of backups of the instance.

        :param request: Request instance for DescribeBackupSummaries.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupSummariesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupSummariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaseBackups(self, request):
        """This API is used to query the list of full backups.

        :param request: Request instance for DescribeBaseBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBaseBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBaseBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClasses(self, request):
        """This API is used to query purchasable instance specifications.

        :param request: Request instance for DescribeClasses.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeClassesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeClassesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClasses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloneDBInstanceSpec(self, request):
        """This API is used to query the minimum specification required by a cloned instance, including `SpecCode` and disk specification.

        :param request: Request instance for DescribeCloneDBInstanceSpec.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeCloneDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeCloneDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloneDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloneDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBBackups(self, request):
        """This API is used to query the backup list of an instance. This API is disused and replaced by the [DescribeBaseBackups](https://intl.cloud.tencent.com/document/api/409/89022?from_cn_redirect=1) API.

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsResponse`

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


    def DescribeDBErrlogs(self, request):
        """This API is used to query an error log.

        :param request: Request instance for DescribeDBErrlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBErrlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBErrlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceAttribute(self, request):
        """This API is used to query the details of one instance.

        :param request: Request instance for DescribeDBInstanceAttribute.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceHAConfig(self, request):
        """This API is used to query the HA configuration of an instance, u200cwhich includes:
        <li>Allow a standby node to promote to a primary node.
        <li>Allow a semi-sync instance to adopt sync or async replication.

        :param request: Request instance for DescribeDBInstanceHAConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceHAConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceHAConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceHAConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceHAConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceParameters(self, request):
        """This API is used to query the parameters of an instance.

        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceSecurityGroups(self, request):
        """This API is used to query the security group of an instance.

        :param request: Request instance for DescribeDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """This API is used to query the details of one or more instances.

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBSlowlogs(self, request):
        """This API is used to get a slow query log. Since it was deprecated on September 1, 2021, it has no longer returned data. You need to use the [DescribeSlowQueryList](https://intl.cloud.tencent.com/document/product/409/60540?from_cn_redirect=1) API instead to get slow query logs.

        :param request: Request instance for DescribeDBSlowlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSlowlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSlowlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBVersions(self, request):
        """This API is used to query the list of supported database versions.

        :param request: Request instance for DescribeDBVersions.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBVersionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBXlogs(self, request):
        """This API is used to get the instance Xlog list. This API is disused and replaced by the [DescribeBaseBackups](https://intl.cloud.tencent.com/document/api/409/89022?from_cn_redirect=1) API.

        :param request: Request instance for DescribeDBXlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBXlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBXlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """This API is used to query the database list of an instance.

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesResponse`

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


    def DescribeDefaultParameters(self, request):
        """This API is used to query all parameters supported by a database version and engine.

        :param request: Request instance for DescribeDefaultParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDefaultParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDefaultParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEncryptionKeys(self, request):
        """This API is used to query the instance key list.

        :param request: Request instance for DescribeEncryptionKeys.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeEncryptionKeysRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeEncryptionKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEncryptionKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEncryptionKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogBackups(self, request):
        """This API is used to query the list of log backups.

        :param request: Request instance for DescribeLogBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeLogBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeLogBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """This API is used to query the order information.

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersResponse`

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


    def DescribeParameterTemplateAttributes(self, request):
        """This API is used to query the details of a parameter template, including basic information and parameter information.

        :param request: Request instance for DescribeParameterTemplateAttributes.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplateAttributesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplateAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParameterTemplateAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParameterTemplateAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParameterTemplates(self, request):
        """This API is used to query the list of parameter templates.

        :param request: Request instance for DescribeParameterTemplates.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplatesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParameterTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParameterTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamsEvent(self, request):
        """This API is used to query the parameter modification event.

        :param request: Request instance for DescribeParamsEvent.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductConfig(self, request):
        """This API is used to query the purchasable specification configuration. u200cThis API is disused and replaced by the [DescribeClasses](https://intl.cloud.tencent.com/document/api/409/89019?from_cn_redirect=1) API.

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigResponse`

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


    def DescribeReadOnlyGroups(self, request):
        """This API is used to query the list of RO groups.

        :param request: Request instance for DescribeReadOnlyGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to query the purchasable regions.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsResponse`

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


    def DescribeServerlessDBInstances(self, request):
        """This API is used to query the details of one or more PostgreSQL for Serverless instances.

        :param request: Request instance for DescribeServerlessDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryAnalysis(self, request):
        """This API is used to count and analyze slow query statements during the specified period of time and return aggregated statistical analysis results which are classified by statement with abstract parameter values.

        :param request: Request instance for DescribeSlowQueryAnalysis.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryList(self, request):
        """This API is used to get the slow queries during the specified period of time.

        :param request: Request instance for DescribeSlowQueryList.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query the supported AZs.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesResponse`

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


    def DestroyDBInstance(self, request):
        """This API is used to terminate an isolated instance by specifying the `DBInstanceId` parameter. The data of a terminated instance will be deleted and cannot be recovered. Be cautious with this API calling. Only the instance in isolation can be terminated.

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisIsolateDBInstances(self, request):
        """This API is used to remove one or more instances from isolation.

        :param request: Request instance for DisIsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisIsolateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DisIsolateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitDBInstances(self, request):
        """This API is used to initialize a TencentDB for PostgreSQL instance. This API is disused and replaced by the [CreateInstances](https://intl.cloud.tencent.com/document/api/409/56107?from_cn_redirect=1) API.

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateDBInstances(self, request):
        """This API is used to query the purchase price of an instance.

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesResponse`

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


    def InquiryPriceRenewDBInstance(self, request):
        """This API is used to query the renewal price of an instance.

        :param request: Request instance for InquiryPriceRenewDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpgradeDBInstance(self, request):
        """This API is used to query the fees of upgrading a specified database instance. Only pay-as-you-go instance is supported.

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceResponse`

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


    def IsolateDBInstances(self, request):
        """This API is used to isolate an instance.

        :param request: Request instance for IsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstancesResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkResponse`

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


    def ModifyBackupDownloadRestriction(self, request):
        """This API is used to modify the backup download restrictions.

        :param request: Request instance for ModifyBackupDownloadRestriction.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupPlan(self, request):
        """This API is used to modify the backup plan of an instance, such as modifying the backup start time. By default, a full backup starts at midnight every day and the generated backup files will be retained for seven days.

        :param request: Request instance for ModifyBackupPlan.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupPlanRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaseBackupExpireTime(self, request):
        """This API is used to modify the specified expiration time of a full backup for an instance.

        :param request: Request instance for ModifyBaseBackupExpireTime.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBaseBackupExpireTimeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBaseBackupExpireTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaseBackupExpireTime", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaseBackupExpireTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceChargeType(self, request):
        """This API is used to switch the instance billing mode from pay-as-you-go to monthly subscription.

        :param request: Request instance for ModifyDBInstanceChargeType.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceChargeTypeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceChargeTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceChargeType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceChargeTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceDeployment(self, request):
        """This API is used to modify the AZs where the nodes of a source instance reside.

        :param request: Request instance for ModifyDBInstanceDeployment.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceDeploymentRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceHAConfig(self, request):
        """This API is used to modify the HA configuration of an instance. u200cwhich includes:
        <li>Allow the standby node to promote to the primary node.
        <li>Allow a semi-sync instance to adopt sync or async replication.

        :param request: Request instance for ModifyDBInstanceHAConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceHAConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceHAConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceHAConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceHAConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """This API is used to rename a TencentDB for PostgreSQL instance.

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceParameters(self, request):
        """This API is used to modify instance parameters.

        :param request: Request instance for ModifyDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceReadOnlyGroup(self, request):
        """This API is used to modify the RO group of an instance.

        :param request: Request instance for ModifyDBInstanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the security group of an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstanceSpec(self, request):
        """This API is used to modify instance specifications, including memory and disk size.

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecResponse`

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


    def ModifyDBInstancesProject(self, request):
        """This API is used to modify the project of an instance.

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstancesProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstancesProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParameterTemplate(self, request):
        """This API is used to modify the configurations, such as parameter template name and description. It can also be used to manage the parameter list in the parameter template.

        :param request: Request instance for ModifyParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReadOnlyGroupConfig(self, request):
        """This API is used to modify RO group configuration.

        :param request: Request instance for ModifyReadOnlyGroupConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReadOnlyGroupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReadOnlyGroupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySwitchTimePeriod(self, request):
        """This API is used to perform a primary-standby switch for an instance waiting for the switch after it is upgraded.

        :param request: Request instance for ModifySwitchTimePeriod.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySwitchTimePeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySwitchTimePeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBExtranetAccess(self, request):
        """This API is used to enable the public network access of an instance.

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenServerlessDBExtranetAccess(self, request):
        """This API is used to enable the public network address of a PostgreSQL for Serverless instance.

        :param request: Request instance for OpenServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenServerlessDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenServerlessDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebalanceReadOnlyGroup(self, request):
        """This API is used to rebalance the loads of read-only replicas in an RO group. Please note that connections to those read-only replicas will be interrupted transiently; therefore, you should ensure that your application can reconnect to the databases. This operation should be performed with caution.

        :param request: Request instance for RebalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebalanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RebalanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveDBInstanceFromReadOnlyGroup(self, request):
        """This API is used to remove a read-only replica from an RO group.

        :param request: Request instance for RemoveDBInstanceFromReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveDBInstanceFromReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveDBInstanceFromReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        """This API is used to renew an instance.

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordResponse`

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
        """This API is used to restart an instance.

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceResponse`

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


    def SetAutoRenewFlag(self, request):
        """This API is used to set auto-renewal.

        :param request: Request instance for SetAutoRenewFlag.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstancePrimary(self, request):
        """This API is used to enable the primary-standby switch of an instance.
        <li>By initiating a switch, you can verify whether the primary-standby switch is performed correctly.
        <li>By using forced switch, you can forcibly initiate the primary-standby switch when the delay of replica node failed to meet the switch requirement.
        <li>This operation can only be performed for the primary instance.

        :param request: Request instance for SwitchDBInstancePrimary.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SwitchDBInstancePrimaryRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SwitchDBInstancePrimaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstancePrimary", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstancePrimaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """This API is used to upgrade instance configurations. u200cThis API is disused and replaced by the [ModifyDBInstanceSpec](https://intl.cloud.tencent.com/document/api/409/63689?from_cn_redirect=1) API.

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceResponse`

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


    def UpgradeDBInstanceKernelVersion(self, request):
        """This API is used to upgrade the kernel version of an instance.

        :param request: Request instance for UpgradeDBInstanceKernelVersion.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceKernelVersionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceKernelVersionResponse`

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