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
from tencentcloud.tem.v20201221 import models


class TemClient(AbstractClient):
    _apiVersion = '2020-12-21'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def CreateCosTokenV2(self, request):
        """This API is used to generate a COS temporary key.

        :param request: Request instance for CreateCosTokenV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosTokenV2", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenV2Response()
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


    def CreateNamespace(self, request):
        """This API is used to create an environment.

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateResourceResponse`

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


    def CreateServiceV2(self, request):
        """This API is used to create a service.

        :param request: Request instance for CreateServiceV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateServiceV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateServiceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceV2", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceV2Response()
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
        :type request: :class:`tencentcloud.tem.v20201221.models.DeleteIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeleteIngressResponse`

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


    def DeployServiceV2(self, request):
        """This API is used to deploy a service.

        :param request: Request instance for DeployServiceV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.DeployServiceV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeployServiceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployServiceV2", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployServiceV2Response()
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
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeIngressResponse`

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
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeIngressesResponse`

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


    def DescribeNamespaces(self, request):
        """This API is used to get the list of tenant environments.

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaces", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNamespacesResponse()
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
        """This API is used to query the list of ingress rules associated with the service.

        :param request: Request instance for DescribeRelatedIngresses.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeRelatedIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeRelatedIngressesResponse`

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


    def DescribeServiceRunPodListV2(self, request):
        """This API is used to get the list of running pods under a service.

        :param request: Request instance for DescribeServiceRunPodListV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeServiceRunPodListV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeServiceRunPodListV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceRunPodListV2", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceRunPodListV2Response()
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


    def GenerateDownloadUrl(self, request):
        """Generate the pre-signed download URL for the specified package

        :param request: Request instance for GenerateDownloadUrl.
        :type request: :class:`tencentcloud.tem.v20201221.models.GenerateDownloadUrlRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.GenerateDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateDownloadUrlResponse()
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
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyIngressResponse`

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


    def ModifyNamespace(self, request):
        """This API is used to edit an environment.

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNamespace", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNamespaceResponse()
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


    def ModifyServiceInfo(self, request):
        """This API is used to modify a service’s basic information.

        :param request: Request instance for ModifyServiceInfo.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyServiceInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyServiceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceInfoResponse()
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


    def RestartServiceRunPod(self, request):
        """This API is used to restart an instance.

        :param request: Request instance for RestartServiceRunPod.
        :type request: :class:`tencentcloud.tem.v20201221.models.RestartServiceRunPodRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.RestartServiceRunPodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartServiceRunPod", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartServiceRunPodResponse()
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