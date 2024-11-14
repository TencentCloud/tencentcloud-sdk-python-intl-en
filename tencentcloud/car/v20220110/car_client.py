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
from tencentcloud.car.v20220110 import models


class CarClient(AbstractClient):
    _apiVersion = '2022-01-10'
    _endpoint = 'car.tencentcloudapi.com'
    _service = 'car'


    def ApplyConcurrent(self, request):
        """This API is used to request concurrency quota. The timeout period of the API is 20 seconds.

        :param request: Request instance for ApplyConcurrent.
        :type request: :class:`tencentcloud.car.v20220110.models.ApplyConcurrentRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ApplyConcurrentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyConcurrent", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyConcurrentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindConcurrentPackagesToProject(self, request):
        """This API is used to bind a concurrency pack to a project.

        :param request: Request instance for BindConcurrentPackagesToProject.
        :type request: :class:`tencentcloud.car.v20220110.models.BindConcurrentPackagesToProjectRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.BindConcurrentPackagesToProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindConcurrentPackagesToProject", params, headers=headers)
            response = json.loads(body)
            model = models.BindConcurrentPackagesToProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplication(self, request):
        """This API is used to create an application.

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateApplicationResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProject(self, request):
        """This API is used to create a cloud application project.

        :param request: Request instance for CreateApplicationProject.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateApplicationProjectRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateApplicationProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationSnapshot(self, request):
        """This API is used to create a cloud application version snapshot.

        :param request: Request instance for CreateApplicationSnapshot.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateApplicationSnapshotRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateApplicationSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationVersion(self, request):
        """This API is used to create a cloud application version.

        :param request: Request instance for CreateApplicationVersion.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateApplicationVersionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateApplicationVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSession(self, request):
        """This API is used to create a session. The timeout period of the API is 5 seconds.

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplication(self, request):
        """This API is used to delete a cloud application.

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.car.v20220110.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DeleteApplicationResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProjects(self, request):
        """This API is used to delete cloud application projects in batches.

        :param request: Request instance for DeleteApplicationProjects.
        :type request: :class:`tencentcloud.car.v20220110.models.DeleteApplicationProjectsRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DeleteApplicationProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationVersion(self, request):
        """This API is used to delete a cloud application version.

        :param request: Request instance for DeleteApplicationVersion.
        :type request: :class:`tencentcloud.car.v20220110.models.DeleteApplicationVersionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DeleteApplicationVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationFileInfo(self, request):
        """This API is used to query application file information.

        :param request: Request instance for DescribeApplicationFileInfo.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationFileInfoRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationFileInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationFileInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationFileInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationList(self, request):
        """This API is used to query the cloud application list.

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationPathList(self, request):
        """This API is used to query the cloud application startup path list.

        :param request: Request instance for DescribeApplicationPathList.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationPathListRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationPathListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationPathList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationPathListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProjectAdvancedConfig(self, request):
        """This API is used to obtain the advanced configuration information of a cloud application project.

        :param request: Request instance for DescribeApplicationProjectAdvancedConfig.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationProjectAdvancedConfigRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationProjectAdvancedConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProjectAdvancedConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProjectAdvancedConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProjects(self, request):
        """This API is used to obtain the cloud application project list.

        :param request: Request instance for DescribeApplicationProjects.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationProjectsRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationStatus(self, request):
        """This API is used to query the running status of a cloud application and update status information.

        :param request: Request instance for DescribeApplicationStatus.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationStatusRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationVersion(self, request):
        """This API is used to query the version information of a cloud application.

        :param request: Request instance for DescribeApplicationVersion.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeApplicationVersionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeApplicationVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrentCount(self, request):
        """This API is used to obtain the concurrency count.

        :param request: Request instance for DescribeConcurrentCount.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentCountRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrentCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrentCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrentPackages(self, request):
        """This API is used to obtain the cloud application concurrency pack list.

        :param request: Request instance for DescribeConcurrentPackages.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentPackagesRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrentPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrentPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrentSummary(self, request):
        """This API is used to query the concurrency overview.

        :param request: Request instance for DescribeConcurrentSummary.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentSummaryRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeConcurrentSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrentSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrentSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosCredential(self, request):
        """This API is used to query COS key information.

        :param request: Request instance for DescribeCosCredential.
        :type request: :class:`tencentcloud.car.v20220110.models.DescribeCosCredentialRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DescribeCosCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroySession(self, request):
        """This API is used to terminate a session. If cloud-based streaming has been enabled for this session, the cloud-based streaming will end upon session termination.

        :param request: Request instance for DestroySession.
        :type request: :class:`tencentcloud.car.v20220110.models.DestroySessionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DestroySessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroySession", params, headers=headers)
            response = json.loads(body)
            model = models.DestroySessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationBaseInfo(self, request):
        """This API is used to modify basic information of a cloud application.

        :param request: Request instance for ModifyApplicationBaseInfo.
        :type request: :class:`tencentcloud.car.v20220110.models.ModifyApplicationBaseInfoRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ModifyApplicationBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProject(self, request):
        """This API is used to modify a cloud application project.

        :param request: Request instance for ModifyApplicationProject.
        :type request: :class:`tencentcloud.car.v20220110.models.ModifyApplicationProjectRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ModifyApplicationProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationVersion(self, request):
        """This API is used to modify the version information of a cloud application.

        :param request: Request instance for ModifyApplicationVersion.
        :type request: :class:`tencentcloud.car.v20220110.models.ModifyApplicationVersionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ModifyApplicationVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConcurrentPackage(self, request):
        """This API is used to modify a cloud application concurrency pack.

        :param request: Request instance for ModifyConcurrentPackage.
        :type request: :class:`tencentcloud.car.v20220110.models.ModifyConcurrentPackageRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ModifyConcurrentPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConcurrentPackage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConcurrentPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMobileApplicationInfo(self, request):
        """This API is used to modify the mobile application data.

        :param request: Request instance for ModifyMobileApplicationInfo.
        :type request: :class:`tencentcloud.car.v20220110.models.ModifyMobileApplicationInfoRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ModifyMobileApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMobileApplicationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMobileApplicationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConcurrentPackages(self, request):
        """This API is used to reset a concurrency pack and disconnect all user connections.

        :param request: Request instance for ResetConcurrentPackages.
        :type request: :class:`tencentcloud.car.v20220110.models.ResetConcurrentPackagesRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ResetConcurrentPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConcurrentPackages", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConcurrentPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetApplicationVersionOnline(self, request):
        """This API is used to launch an application version.

        :param request: Request instance for SetApplicationVersionOnline.
        :type request: :class:`tencentcloud.car.v20220110.models.SetApplicationVersionOnlineRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.SetApplicationVersionOnlineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetApplicationVersionOnline", params, headers=headers)
            response = json.loads(body)
            model = models.SetApplicationVersionOnlineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStream(self, request):
        """This API is used to start pushing your cloud application's video streams in real time to CSS. The codec for the streaming is automatically selected based on the client's (SDK) capabilities, with a default order of H.265, H.264, VP8, and VP9.

        :param request: Request instance for StartPublishStream.
        :type request: :class:`tencentcloud.car.v20220110.models.StartPublishStreamRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StartPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStreamWithURL(self, request):
        """This API is used to start pushing your cloud application's video streams to a specified URL. The codec for the streaming is automatically selected based on the client's (SDK) capabilities, with a default order of H.265, H.264, VP8, and VP9. This streaming method will be billed separately. For details about the billing method, see [Charging for Streaming to Specified URL](https://intl.cloud.tencent.com/document/product/1547/72168?from_cn_redirect=1#98ac188a-d122-4caf-88be-05268ecefdf6).

        :param request: Request instance for StartPublishStreamWithURL.
        :type request: :class:`tencentcloud.car.v20220110.models.StartPublishStreamWithURLRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StartPublishStreamWithURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStreamWithURL", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamWithURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishStream(self, request):
        """This API is used to stop pushing streams.

        :param request: Request instance for StopPublishStream.
        :type request: :class:`tencentcloud.car.v20220110.models.StopPublishStreamRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StopPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindConcurrentPackagesFromProject(self, request):
        """This API is used to unbind a concurrency pack from a project.

        :param request: Request instance for UnbindConcurrentPackagesFromProject.
        :type request: :class:`tencentcloud.car.v20220110.models.UnbindConcurrentPackagesFromProjectRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.UnbindConcurrentPackagesFromProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindConcurrentPackagesFromProject", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindConcurrentPackagesFromProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))