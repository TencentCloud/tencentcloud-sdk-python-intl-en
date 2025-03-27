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
from tencentcloud.facefusion.v20220927 import models


class FacefusionClient(AbstractClient):
    _apiVersion = '2022-09-27'
    _endpoint = 'facefusion.intl.tencentcloudapi.com'
    _service = 'facefusion'


    def FuseFace(self, request):
        """This API is used to perform the fusion of a single face, multiple faces, and specified faces with the material template by uploading face images. Users can add logos to generated images. See <a href="https://intl.cloud.tencent.com/document/product/670/38247?from_cn_redirect=1" target="_blank">Fusion Access Guide</a>.



        - The signature method in the public parameters must be specified as the V3 version. In other words, set the SignatureMethod parameter to TC3-HMAC-SHA256.

        :param request: Request instance for FuseFace.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FuseFace", params, headers=headers)
            response = json.loads(body)
            model = models.FuseFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryVideoFaceFusionJob(self, request):
        """This API is used to query the progress and status of video face fusion tasks by Job ID.

        :param request: Request instance for QueryVideoFaceFusionJob.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.QueryVideoFaceFusionJobRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.QueryVideoFaceFusionJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVideoFaceFusionJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVideoFaceFusionJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoFaceFusionJob(self, request):
        """This API is used to submit asynchronous processing tasks of video face fusion. After a task is submitted, the Job ID, estimated completion time, and current queue length will be returned.

        :param request: Request instance for SubmitVideoFaceFusionJob.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.SubmitVideoFaceFusionJobRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.SubmitVideoFaceFusionJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoFaceFusionJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoFaceFusionJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))