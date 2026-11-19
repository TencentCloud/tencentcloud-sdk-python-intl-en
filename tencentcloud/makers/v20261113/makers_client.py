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
from tencentcloud.makers.v20261113 import models


class MakersClient(AbstractClient):
    _apiVersion = '2026-11-13'
    _endpoint = 'makers.intl.tencentcloudapi.com'
    _service = 'makers'


    def CreateDeployment(self, request):
        r"""This API is used to create a deployment. When uploading an artifact, pass Upload for ViaMeta and Provider, and pass the path of the uploaded object for TempBucketPath.

        :param request: Request instance for CreateDeployment.
        :type request: :class:`tencentcloud.makers.v20261113.models.CreateDeploymentRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.CreateDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        r"""This API is used to create a project. When uploading an artifact, pass Upload for Provider and Custom for Channel.

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.makers.v20261113.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.CreateProjectResponse`

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


    def CreateZoneCustomDomain(self, request):
        r"""Bind a custom domain name to a specified environment of a project.

        :param request: Request instance for CreateZoneCustomDomain.
        :type request: :class:`tencentcloud.makers.v20261113.models.CreateZoneCustomDomainRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.CreateZoneCustomDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZoneCustomDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateZoneCustomDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""Delete a project. In-progress builds prevent deletion.

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.makers.v20261113.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DeleteProjectResponse`

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


    def DeleteProjectCustomDomains(self, request):
        r"""Unbind a custom domain name from a project by domain name.

        :param request: Request instance for DeleteProjectCustomDomains.
        :type request: :class:`tencentcloud.makers.v20261113.models.DeleteProjectCustomDomainsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DeleteProjectCustomDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectCustomDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectCustomDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectEnvs(self, request):
        r"""Delete environment variables by EnvVars. Match by Id or Key. Value is required but not used for matching. You can pass any value.

        :param request: Request instance for DeleteProjectEnvs.
        :type request: :class:`tencentcloud.makers.v20261113.models.DeleteProjectEnvsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DeleteProjectEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosTempToken(self, request):
        r"""Get the COS bucket, region, target path, and temporary key for uploading artifacts.

        :param request: Request instance for DescribeCosTempToken.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeCosTempTokenRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeCosTempTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosTempToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosTempTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeploymentLog(self, request):
        r"""Return the access address of the build log.

        :param request: Request instance for DescribeDeploymentLog.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeDeploymentLogRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeDeploymentLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeploymentLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeploymentLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployments(self, request):
        r"""Query deployment records of a project.

        :param request: Request instance for DescribeDeployments.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeDeploymentsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeDeploymentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeploymentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        r"""Query environments in a project, including built-in Production, Preview, and custom environments.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectEnvs(self, request):
        r"""Query project environment variables. If Env is not specified, return all application scopes.

        :param request: Request instance for DescribeProjectEnvs.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeProjectEnvsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeProjectEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        r"""This API is used to query projects under a site by page. Offset is the page number offset, and the backend skips Offset * Limit items.

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneCustomDomains(self, request):
        r"""Queries the custom and preset domain names of a project under a site.

        :param request: Request instance for DescribeZoneCustomDomains.
        :type request: :class:`tencentcloud.makers.v20261113.models.DescribeZoneCustomDomainsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.DescribeZoneCustomDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneCustomDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneCustomDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""Modify the project name and build configuration. Fields not passed retain their original values.

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.makers.v20261113.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.ModifyProjectResponse`

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


    def ModifyProjectEnvs(self, request):
        r"""Write environment variables based on the passed-in EnvVars.

        :param request: Request instance for ModifyProjectEnvs.
        :type request: :class:`tencentcloud.makers.v20261113.models.ModifyProjectEnvsRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.ModifyProjectEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProjectEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneCustomDomainEnv(self, request):
        r"""Switch a bound custom domain name to another environment.

        :param request: Request instance for ModifyZoneCustomDomainEnv.
        :type request: :class:`tencentcloud.makers.v20261113.models.ModifyZoneCustomDomainEnvRequest`
        :rtype: :class:`tencentcloud.makers.v20261113.models.ModifyZoneCustomDomainEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneCustomDomainEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneCustomDomainEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))