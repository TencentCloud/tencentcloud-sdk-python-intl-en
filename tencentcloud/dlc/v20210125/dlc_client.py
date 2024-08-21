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
from tencentcloud.dlc.v20210125 import models


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'


    def AddUsersToWorkGroup(self, request):
        """This API is used to add users to working groups.

        :param request: Request instance for AddUsersToWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersToWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersToWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AlterDMSDatabase(self, request):
        """This API is used to update databases in the DMS metadata module.

        :param request: Request instance for AlterDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AlterDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AlterDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AlterDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.AlterDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachUserPolicy(self, request):
        """This API is used to bind the authentication policy to the user.

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachUserPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachUserPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachWorkGroupPolicy(self, request):
        """This API is used to bind an authentication policy to a working group.

        :param request: Request instance for AttachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachWorkGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachWorkGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindWorkGroupsToUser(self, request):
        """This API is used to bind working groups to users.

        :param request: Request instance for BindWorkGroupsToUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindWorkGroupsToUser", params, headers=headers)
            response = json.loads(body)
            model = models.BindWorkGroupsToUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelSparkSessionBatchSQL(self, request):
        """This API is used to cancel a Spark SQL batch task.

        :param request: Request instance for CancelSparkSessionBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelSparkSessionBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelSparkSessionBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelSparkSessionBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.CancelSparkSessionBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelTask(self, request):
        """This API is used to cancel a task.

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineConfigPairsValidity(self, request):
        """This API is used to check the validity of the engine's user-defined parameters.

        :param request: Request instance for CheckDataEngineConfigPairsValidity.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineConfigPairsValidityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineConfigPairsValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineConfigPairsValidity", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineConfigPairsValidityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineImageCanBeRollback(self, request):
        """This API is used to check whether the cluster can be rolled back.

        :param request: Request instance for CheckDataEngineImageCanBeRollback.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeRollbackRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineImageCanBeRollback", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineImageCanBeRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineImageCanBeUpgrade(self, request):
        """This API is used to check whether the cluster image can be upgraded.

        :param request: Request instance for CheckDataEngineImageCanBeUpgrade.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeUpgradeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeUpgradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineImageCanBeUpgrade", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineImageCanBeUpgradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckGrantedPermission(self, request):
        """This API is used to check the permission status.

        :param request: Request instance for CheckGrantedPermission.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckGrantedPermissionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckGrantedPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckGrantedPermission", params, headers=headers)
            response = json.loads(body)
            model = models.CheckGrantedPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyDLCTable(self, request):
        """This API is used to copy a table.

        :param request: Request instance for CopyDLCTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CopyDLCTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CopyDLCTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyDLCTable", params, headers=headers)
            response = json.loads(body)
            model = models.CopyDLCTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCHDFSBindingProduct(self, request):
        """This API is used to create metadata acceleration buckets and the binding relationship between products.

        :param request: Request instance for CreateCHDFSBindingProduct.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateCHDFSBindingProductRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateCHDFSBindingProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCHDFSBindingProduct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCHDFSBindingProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDLCTable(self, request):
        """This API is used to create a table.

        :param request: Request instance for CreateDLCTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDLCTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDLCTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDLCTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDLCTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDMSDatabase(self, request):
        """This API is used to create databases in the DMS metadata module.

        :param request: Request instance for CreateDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataEngine(self, request):
        """This API is used to create a data engine.

        :param request: Request instance for CreateDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInternalTable(self, request):
        """This API is used to create a managed internal table. It has been disused.

        :param request: Request instance for CreateInternalTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateInternalTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateInternalTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInternalTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInternalTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResultDownload(self, request):
        """This API is used to create a query result download task.

        :param request: Request instance for CreateResultDownload.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateResultDownloadRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateResultDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResultDownload", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResultDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSparkApp(self, request):
        """This API is used to create a Spark job.

        :param request: Request instance for CreateSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSparkAppTask(self, request):
        """This API is used to start a Spark job.

        :param request: Request instance for CreateSparkAppTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkAppTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkAppTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSparkSessionBatchSQL(self, request):
        """This API is used to submit a Spark SQL batch task to the job engine.

        :param request: Request instance for CreateSparkSessionBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSessionBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSessionBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkSessionBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkSessionBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStoreLocation(self, request):
        """This API is used to add or overwrite the storage location of results.

        :param request: Request instance for CreateStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        """This API is used to create and execute a SQL task. (`CreateTasks` is recommended.)

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTasks(self, request):
        """This API is used to create and execute SQL tasks in batches.

        :param request: Request instance for CreateTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """This API is used to create users.

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkGroup(self, request):
        """This API is used to create working groups.

        :param request: Request instance for CreateWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCHDFSBindingProduct(self, request):
        """This API is used to delete the binding relationship between metadata acceleration buckets and products.

        :param request: Request instance for DeleteCHDFSBindingProduct.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteCHDFSBindingProductRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteCHDFSBindingProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCHDFSBindingProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCHDFSBindingProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataEngine(self, request):
        """This API is used to delete the data engine.

        :param request: Request instance for DeleteDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSparkApp(self, request):
        """This API is used to delete a Spark job.

        :param request: Request instance for DeleteSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteThirdPartyAccessUser(self, request):
        """This API is used to remove visits through the third-party platform.

        :param request: Request instance for DeleteThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """This API is used to delete users.

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsersFromWorkGroup(self, request):
        """This API is used to delete users from working groups.

        :param request: Request instance for DeleteUsersFromWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsersFromWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersFromWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkGroup(self, request):
        """This API is used to delete working groups.

        :param request: Request instance for DeleteWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdvancedStoreLocation(self, request):
        """This API is used to query the advanced settings of the SQL query interface.

        :param request: Request instance for DescribeAdvancedStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeAdvancedStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeAdvancedStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdvancedStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdvancedStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLCCatalogAccess(self, request):
        """This API is used to query the DLC Catalog authorization list.

        :param request: Request instance for DescribeDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLCTable(self, request):
        """This API is used to obtain the table.

        :param request: Request instance for DescribeDLCTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLCTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLCTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLCTableList(self, request):
        """This API is used to obtain the list of tables.

        :param request: Request instance for DescribeDLCTableList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCTableListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLCTableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLCTableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDMSDatabase(self, request):
        """This API is used to obtain databases in the DMS metadata module.

        :param request: Request instance for DescribeDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDMSDatabaseList(self, request):
        """This API is used to obtain the list of databases.

        :param request: Request instance for DescribeDMSDatabaseList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngine(self, request):
        """This API is used to obtain detailed data engine information based on names.

        :param request: Request instance for DescribeDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngineImageVersions(self, request):
        """This API is used to obtain the major version image list of exclusive clusters.

        :param request: Request instance for DescribeDataEngineImageVersions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineImageVersionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineImageVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngineImageVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineImageVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEnginePythonSparkImages(self, request):
        """This API is used to obtain the PYSPARK image list.

        :param request: Request instance for DescribeDataEnginePythonSparkImages.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginePythonSparkImagesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginePythonSparkImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEnginePythonSparkImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEnginePythonSparkImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEnginesScaleDetail(self, request):
        """This API is used to query engine specification details.

        :param request: Request instance for DescribeDataEnginesScaleDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesScaleDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesScaleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEnginesScaleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEnginesScaleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEngineUsageInfo(self, request):
        """This API is used to query the resource usage of a data engine based on its ID.

        :param request: Request instance for DescribeEngineUsageInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineUsageInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEngineUsageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEngineUsageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForbiddenTablePro(self, request):
        """This API is used to get the list of disabled table attributes (new).

        :param request: Request instance for DescribeForbiddenTablePro.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeForbiddenTableProRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeForbiddenTableProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForbiddenTablePro", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForbiddenTableProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJob(self, request):
        """This API is used to obtain the job information.

        :param request: Request instance for DescribeJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobs(self, request):
        """This API is used to obtain the list of job information.

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLakeFsDirSummary(self, request):
        """This API is used to query the summary of a specified directory in a managed storage.

        :param request: Request instance for DescribeLakeFsDirSummary.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsDirSummaryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsDirSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLakeFsDirSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLakeFsDirSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLakeFsInfo(self, request):
        """This API is used to query managed storage information.

        :param request: Request instance for DescribeLakeFsInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLakeFsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLakeFsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOtherCHDFSBindingList(self, request):
        """This API is used to query the list of metadata acceleration buckets bound to other products.

        :param request: Request instance for DescribeOtherCHDFSBindingList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeOtherCHDFSBindingListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeOtherCHDFSBindingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOtherCHDFSBindingList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOtherCHDFSBindingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuery(self, request):
        """This API is used to obtain the query results.

        :param request: Request instance for DescribeQuery.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeQueryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResultDownload(self, request):
        """This API is used to get a query result download task.

        :param request: Request instance for DescribeResultDownload.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeResultDownloadRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeResultDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResultDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResultDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkAppJob(self, request):
        """u200cThis API is used to query the information of a Spark job.

        :param request: Request instance for DescribeSparkAppJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkAppJobs(self, request):
        """This API is used to query the list of Spark jobs.

        :param request: Request instance for DescribeSparkAppJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkAppTasks(self, request):
        """This API is used to query the list of running task instances of a Spark job.

        :param request: Request instance for DescribeSparkAppTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkSessionBatchSqlLog(self, request):
        """This API is used to query Spark SQL batch task logs.

        :param request: Request instance for DescribeSparkSessionBatchSqlLog.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSqlLogRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSqlLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkSessionBatchSqlLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkSessionBatchSqlLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStoreLocation(self, request):
        """This API is used to query the storage location of calculation results.

        :param request: Request instance for DescribeStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubUserAccessPolicy(self, request):
        """This API is used to query the sub-user's visiting policy for users accessing through the third-party platform.

        :param request: Request instance for DescribeSubUserAccessPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSubUserAccessPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSubUserAccessPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubUserAccessPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubUserAccessPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablesName(self, request):
        """This API is used to query the data table name list.

        :param request: Request instance for DescribeTablesName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablesName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResult(self, request):
        """This API is used to query the result of a task.

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatistics(self, request):
        """This API is used to describe the information on task statistics.

        :param request: Request instance for DescribeTaskStatistics.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskStatisticsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """This API is used to query the list of tasks.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeThirdPartyAccessUser(self, request):
        """This API is used to query the information of users visiting through the third-party platform.

        :param request: Request instance for DescribeThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpdatableDataEngines(self, request):
        """This API is used to query the list of engines that are able to upgrade their configuration.

        :param request: Request instance for DescribeUpdatableDataEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUpdatableDataEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUpdatableDataEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpdatableDataEngines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpdatableDataEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDataEngineConfig(self, request):
        """This API is used to query user-defined engine parameters.

        :param request: Request instance for DescribeUserDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInfo(self, request):
        """This API is used to get detailed user information.

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoles(self, request):
        """This API is used to enumerate user roles.

        :param request: Request instance for DescribeUserRoles.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRolesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserType(self, request):
        """This API is used to get the types of users.

        :param request: Request instance for DescribeUserType.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserTypeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsers(self, request):
        """This API is used to obtain the user list.

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkGroupInfo(self, request):
        """This API is used to get detailed information about working groups.

        :param request: Request instance for DescribeWorkGroupInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkGroups(self, request):
        """This API is used to get a list of working groups.

        :param request: Request instance for DescribeWorkGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachUserPolicy(self, request):
        """This API is used to unbind the authentication policy from the user.

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachUserPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DetachUserPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachWorkGroupPolicy(self, request):
        """This API is used to unbind the authentication policy from the working group.

        :param request: Request instance for DetachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachWorkGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DetachWorkGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropDLCTable(self, request):
        """This API is used to delete the table.

        :param request: Request instance for DropDLCTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDLCTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDLCTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDLCTable", params, headers=headers)
            response = json.loads(body)
            model = models.DropDLCTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropDMSDatabase(self, request):
        """This API is used to delete databases in the DMS metadata module.

        :param request: Request instance for DropDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DropDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropDMSTable(self, request):
        """This API is used to delete tables in the DMS metadata module.

        :param request: Request instance for DropDMSTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDMSTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDMSTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDMSTable", params, headers=headers)
            response = json.loads(body)
            model = models.DropDMSTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateCreateMangedTableSql(self, request):
        """This API is used to generate SQL statements for creating a managed table.

        :param request: Request instance for GenerateCreateMangedTableSql.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GenerateCreateMangedTableSqlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GenerateCreateMangedTableSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateCreateMangedTableSql", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateCreateMangedTableSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOptimizerPolicy(self, request):
        """GetOptimizerPolicy

        :param request: Request instance for GetOptimizerPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetOptimizerPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetOptimizerPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOptimizerPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.GetOptimizerPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantDLCCatalogAccess(self, request):
        """This API is used to grant permissions for visiting DLC Catalog.

        :param request: Request instance for GrantDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GrantDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GrantDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.GrantDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAdvancedStoreLocation(self, request):
        """This API is used to modify the advanced settings of the SQL query interface.

        :param request: Request instance for ModifyAdvancedStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyAdvancedStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyAdvancedStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAdvancedStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAdvancedStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataEngineDescription(self, request):
        """This API is used to modify the engine's description.

        :param request: Request instance for ModifyDataEngineDescription.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyDataEngineDescriptionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyDataEngineDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataEngineDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataEngineDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernEventRule(self, request):
        """This API is used to change data governance event thresholds.

        :param request: Request instance for ModifyGovernEventRule.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyGovernEventRuleRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyGovernEventRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernEventRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernEventRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySparkApp(self, request):
        """This API is used to update a Spark job.

        :param request: Request instance for ModifySparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySparkAppBatch(self, request):
        """This API is used to modify Spark job parameters in batches.

        :param request: Request instance for ModifySparkAppBatch.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppBatchRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkAppBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySparkAppBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        """This API is used to modify user information.

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserType(self, request):
        """This API is used to modify the types of users. Only users who are also administrators can call this API to conduct the operation.

        :param request: Request instance for ModifyUserType.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyUserTypeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyUserTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkGroup(self, request):
        """This API is used to modify working group information.

        :param request: Request instance for ModifyWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryResult(self, request):
        """This API is used to query the result of obtaining tasks.

        :param request: Request instance for QueryResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryResult", params, headers=headers)
            response = json.loads(body)
            model = models.QueryResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryTaskCostDetail(self, request):
        """This API is used to query task consumption details.

        :param request: Request instance for QueryTaskCostDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryTaskCostDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryTaskCostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTaskCostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTaskCostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterThirdPartyAccessUser(self, request):
        """This API is used to enable visits to the third-party platform.

        :param request: Request instance for RegisterThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RegisterThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RegisterThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDataEngine(self, request):
        """This API is used to renew the data engine.

        :param request: Request instance for RenewDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RenewDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RenewDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDataEngine(self, request):
        """This API is used to restart engines.

        :param request: Request instance for RestartDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RestartDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RestartDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeDLCCatalogAccess(self, request):
        """This API is used to revoke permissions for visiting DLC Catalog.

        :param request: Request instance for RevokeDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RevokeDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RevokeDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackDataEngineImage(self, request):
        """This API is used to roll back the versions of the engine image.

        :param request: Request instance for RollbackDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RollbackDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RollbackDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SuspendResumeDataEngine(self, request):
        """This API is used to suspend or start a data engine.

        :param request: Request instance for SuspendResumeDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SuspendResumeDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SuspendResumeDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendResumeDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendResumeDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDataEngine(self, request):
        """This API is used to switch between the primary and standby clusters.

        :param request: Request instance for SwitchDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDataEngineImage(self, request):
        """This API is used to switch the versions of the engine image.

        :param request: Request instance for SwitchDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindWorkGroupsFromUser(self, request):
        """This API is used to unbind a user group from a user.

        :param request: Request instance for UnbindWorkGroupsFromUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindWorkGroupsFromUser", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindWorkGroupsFromUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataEngine(self, request):
        """This API is used to upgrade data engine configuration.

        :param request: Request instance for UpdateDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataEngineConfig(self, request):
        """This API is used to trigger the modification of the engine configuration by the user through a certain operation.

        :param request: Request instance for UpdateDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRowFilter(self, request):
        """This API is used to update row filters. Please note that it updates filters only but not catalogs, databases, or tables.

        :param request: Request instance for UpdateRowFilter.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateRowFilterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateRowFilterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRowFilter", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRowFilterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserDataEngineConfig(self, request):
        """This API is used to modify the custom configuration of the user's engine.

        :param request: Request instance for UpdateUserDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateUserDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateUserDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDataEngineImage(self, request):
        """This API is used to upgrade the engine image.

        :param request: Request instance for UpgradeDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpgradeDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpgradeDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))