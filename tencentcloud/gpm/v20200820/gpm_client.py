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
from tencentcloud.gpm.v20200820 import models


class GpmClient(AbstractClient):
    _apiVersion = '2020-08-20'
    _endpoint = 'gpm.tencentcloudapi.com'
    _service = 'gpm'


    def CancelMatching(self, request):
        """This API is used to cancel matching.

        :param request: Request instance for CancelMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelMatching", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelMatchingResponse()
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


    def DescribeMatchingProgress(self, request):
        """This API is used to query the matching progress.

        :param request: Request instance for DescribeMatchingProgress.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMatchingProgress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMatchingProgressResponse()
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


    def DescribeToken(self, request):
        """This API is used to query the token of a Matchcode, which is used for verified the pushed message.

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTokenResponse()
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


    def ModifyToken(self, request):
        """This API is used to modify the token of a Matchcode.

        :param request: Request instance for ModifyToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTokenResponse()
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


    def StartMatching(self, request):
        """This API is used to pass in one player or multiple players to initiate match. Players within the same request will be assigned to the same game session.

        :param request: Request instance for StartMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.StartMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.StartMatchingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMatching", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMatchingResponse()
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