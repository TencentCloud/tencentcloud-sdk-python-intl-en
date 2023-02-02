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
from tencentcloud.tem.v20210701 import models


class TemClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def CreateApplication(self, request):
        """This API is used to create an application.

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplicationAutoscaler(self, request):
        """This API is used to create a scaling rule.

        :param request: Request instance for CreateApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationAutoscalerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplicationService(self, request):
        """This API is used to create an access policy.

        :param request: Request instance for CreateApplicationService.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateApplicationServiceRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateApplicationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateConfigData(self, request):
        """This API is used to create a configuration.

        :param request: Request instance for CreateConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigData", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCosToken(self, request):
        """This API is used to generate a COS temporary key.

        :param request: Request instance for CreateCosToken.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateCosTokenRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateCosTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateEnvironment(self, request):
        """This API is used to create an environment.

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLogConfig(self, request):
        """This API is used to create a log collecting configuration.

        :param request: Request instance for CreateLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateResource(self, request):
        """This API is used to bind a cloud resource.

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplication(self, request):
        """This API is used to delete an application.
          - Stop running the current application
          - Delete resources related to the application
          - Delete the application

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplicationAutoscaler(self, request):
        """This API is used to delete a scaling rule.

        :param request: Request instance for DeleteApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationAutoscalerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplicationService(self, request):
        """This API is used to delete an access policy.

        :param request: Request instance for DeleteApplicationService.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationServiceRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIngress(self, request):
        """This API is used to delete an ingress rule.

        :param request: Request instance for DeleteIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIngress", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIngressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployApplication(self, request):
        """This API is used to deploy an application.

        :param request: Request instance for DeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeployApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeployApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationAutoscalerList(self, request):
        """This API is used to query the scaling rules of an application.

        :param request: Request instance for DescribeApplicationAutoscalerList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationAutoscalerListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationAutoscalerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationAutoscalerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationAutoscalerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationInfo(self, request):
        """This API is used to check the basic information of an application.

        :param request: Request instance for DescribeApplicationInfo.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationPods(self, request):
        """This API is used to get the list of application pods.

        :param request: Request instance for DescribeApplicationPods.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationPodsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationPods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationServiceList(self, request):
        """This API is used to query the list of access policies.

        :param request: Request instance for DescribeApplicationServiceList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationServiceListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplications(self, request):
        """This API is to query the list of running applications.

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationsStatus(self, request):
        """This API is used to query the status of all applications in an envrionment.

        :param request: Request instance for DescribeApplicationsStatus.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsStatusRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigData(self, request):
        """This API is used to query details of a configuration.

        :param request: Request instance for DescribeConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigDataList(self, request):
        """This API is used to query the list of configurations.

        :param request: Request instance for DescribeConfigDataList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigDataList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigDataListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironment(self, request):
        """This API is used to obtain the basic information of an environment.

        :param request: Request instance for DescribeEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironmentStatus(self, request):
        """This API is used to obtain the environment status.

        :param request: Request instance for DescribeEnvironmentStatus.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentStatusRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironments(self, request):
        """This API is used to obtain the list of environments.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIngress(self, request):
        """This API is used to query an ingress rule.

        :param request: Request instance for DescribeIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIngress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIngressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIngresses(self, request):
        """This API is used to query the list of ingress rules.

        :param request: Request instance for DescribeIngresses.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeIngressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIngresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIngressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogConfig(self, request):
        """This API is used to query details of a log collecting configuration.

        :param request: Request instance for DescribeLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePagedLogConfigList(self, request):
        """This API is used to querying the list of log collecting configurations.

        :param request: Request instance for DescribePagedLogConfigList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribePagedLogConfigListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribePagedLogConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePagedLogConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePagedLogConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRelatedIngresses(self, request):
        """This API is used to query the list of ingress rules associated with the application.

        :param request: Request instance for DescribeRelatedIngresses.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeRelatedIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeRelatedIngressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedIngresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelatedIngressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyConfigData(self, request):
        """This API is used to terminate a configuration.

        :param request: Request instance for DestroyConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyConfigData", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyConfigDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyEnvironment(self, request):
        """This API is used to terminate an environment.

        :param request: Request instance for DestroyEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyLogConfig(self, request):
        """This API is used to terminate a log collecting configuration.

        :param request: Request instance for DestroyLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableApplicationAutoscaler(self, request):
        """This API is used to disable a scaling rule.

        :param request: Request instance for DisableApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.DisableApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DisableApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            model = models.DisableApplicationAutoscalerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableApplicationAutoscaler(self, request):
        """This API is used to enable a scaling rule.

        :param request: Request instance for EnableApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.EnableApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.EnableApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            model = models.EnableApplicationAutoscalerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateApplicationPackageDownloadUrl(self, request):
        """This API is used to generate the pre-signed download URL for the specified application package.

        :param request: Request instance for GenerateApplicationPackageDownloadUrl.
        :type request: :class:`tencentcloud.tem.v20210701.models.GenerateApplicationPackageDownloadUrlRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.GenerateApplicationPackageDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateApplicationPackageDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateApplicationPackageDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationAutoscaler(self, request):
        """This API is used to modify a scaling rule.

        :param request: Request instance for ModifyApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationAutoscalerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationInfo(self, request):
        """This API is used to modify the basic information of an application.

        :param request: Request instance for ModifyApplicationInfo.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationService(self, request):
        """This API is used to modify an access policy.

        :param request: Request instance for ModifyApplicationService.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationServiceRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyConfigData(self, request):
        """This API is used to modify a configuration.

        :param request: Request instance for ModifyConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigData", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEnvironment(self, request):
        """This API is used to edit an environment.

        :param request: Request instance for ModifyEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIngress(self, request):
        """This API is used to create or update an ingress rule.

        :param request: Request instance for ModifyIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIngress", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIngressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLogConfig(self, request):
        """This API is used to modify a log collecting configuration.

        :param request: Request instance for ModifyLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartApplication(self, request):
        """This API is used to restart an application.

        :param request: Request instance for RestartApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.RestartApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RestartApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartApplication", params, headers=headers)
            response = json.loads(body)
            model = models.RestartApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartApplicationPod(self, request):
        """This API is used to restart an application pod.

        :param request: Request instance for RestartApplicationPod.
        :type request: :class:`tencentcloud.tem.v20210701.models.RestartApplicationPodRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RestartApplicationPodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartApplicationPod", params, headers=headers)
            response = json.loads(body)
            model = models.RestartApplicationPodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RollingUpdateApplicationByVersion(self, request):
        """This API is used to configure the rolling update policy for an application.

        :param request: Request instance for RollingUpdateApplicationByVersion.
        :type request: :class:`tencentcloud.tem.v20210701.models.RollingUpdateApplicationByVersionRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RollingUpdateApplicationByVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollingUpdateApplicationByVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollingUpdateApplicationByVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopApplication(self, request):
        """This API is used to stop an application.

        :param request: Request instance for StopApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.StopApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.StopApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopApplication", params, headers=headers)
            response = json.loads(body)
            model = models.StopApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)