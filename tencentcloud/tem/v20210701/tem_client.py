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
            if "Error" not in response["Response"]:
                model = models.CreateApplicationResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateEnvironmentResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateResourceResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteIngressResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeployApplicationResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationPodsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationsStatusResponse()
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


    def DescribeEnvironments(self, request):
        """This API is used to get the list of tenant environments.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeIngressResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeIngressesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeRelatedIngressesResponse()
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


    def DestroyEnvironment(self, request):
        """This API is used to terminate a namespace.

        :param request: Request instance for DestroyEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyEnvironmentResponse()
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
            if "Error" not in response["Response"]:
                model = models.GenerateApplicationPackageDownloadUrlResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyEnvironmentResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyIngressResponse()
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
            if "Error" not in response["Response"]:
                model = models.RestartApplicationResponse()
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
            if "Error" not in response["Response"]:
                model = models.RestartApplicationPodResponse()
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
            if "Error" not in response["Response"]:
                model = models.RollingUpdateApplicationByVersionResponse()
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
            if "Error" not in response["Response"]:
                model = models.StopApplicationResponse()
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