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
from tencentcloud.bi.v20220105 import models


class BiClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'bi.intl.tencentcloudapi.com'
    _service = 'bi'


    def ApplyEmbedInterval(self, request):
        """This API is used to extend the available time of a token with strong authentication.

        :param request: Request instance for ApplyEmbedInterval.
        :type request: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyEmbedInterval", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyEmbedIntervalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatasource(self, request):
        """This API is used to create a data source.

        :param request: Request instance for CreateDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatasourceCloud(self, request):
        """This API is used to create a cloud database.

        :param request: Request instance for CreateDatasourceCloud.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceCloudRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasourceCloud", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmbedToken(self, request):
        """This API is used to create an embedded report with strong authentication.

        :param request: Request instance for CreateEmbedToken.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateEmbedTokenRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateEmbedTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmbedToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmbedTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """This API is used to create a project.

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserRole(self, request):
        """This API is used to create a user role.

        :param request: Request instance for CreateUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserRoleProject(self, request):
        """This API is used to create a user role in the project.

        :param request: Request instance for CreateUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDatasource(self, request):
        """This API is used to delete a data source.

        :param request: Request instance for DeleteDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        """This API is used to delete a project.

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserRole(self, request):
        """This API is used to remove a user role, which will result in user deletion.

        :param request: Request instance for DeleteUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserRoleProject(self, request):
        """This API is used to delete a user role in the project.

        :param request: Request instance for DeleteUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasourceList(self, request):
        """This API is used to query a data source list.

        :param request: Request instance for DescribeDatasourceList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeDatasourceListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeDatasourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePageWidgetList(self, request):
        """This API is used to query component information on the page.

        :param request: Request instance for DescribePageWidgetList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribePageWidgetListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribePageWidgetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePageWidgetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePageWidgetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectInfo(self, request):
        """This API is used to obtain project details.

        :param request: Request instance for DescribeProjectInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeProjectInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeProjectInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectList(self, request):
        """This API is used to obtain project information.

        :param request: Request instance for DescribeProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserProjectList(self, request):
        """This API is used to obtain the user interface in the project.

        :param request: Request instance for DescribeUserProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoleList(self, request):
        """This API is used to obtain the user role list.

        :param request: Request instance for DescribeUserRoleList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoleProjectList(self, request):
        """This API is used to obtain the user role list in the project.

        :param request: Request instance for DescribeUserRoleProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoleProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRoleProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportScreenPage(self, request):
        """This API is used to export a screenshot.

        :param request: Request instance for ExportScreenPage.
        :type request: :class:`tencentcloud.bi.v20220105.models.ExportScreenPageRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ExportScreenPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportScreenPage", params, headers=headers)
            response = json.loads(body)
            model = models.ExportScreenPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatasource(self, request):
        """This API is used to update a data source.

        :param request: Request instance for ModifyDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatasourceCloud(self, request):
        """This API is used to update a cloud database.

        :param request: Request instance for ModifyDatasourceCloud.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceCloudRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatasourceCloud", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatasourceCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        """This API is used to modify project information.

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserRole(self, request):
        """This API is used to modify user role info.

        :param request: Request instance for ModifyUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserRoleProject(self, request):
        """This API is used to modify the user role info in the project.

        :param request: Request instance for ModifyUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))