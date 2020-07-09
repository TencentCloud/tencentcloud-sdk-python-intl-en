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
from tencentcloud.mdp.v20200527 import models


class MdpClient(AbstractClient):
    _apiVersion = '2020-05-27'
    _endpoint = 'mdp.tencentcloudapi.com'


    def CreateMediaPackageChannel(self, request):
        """This API is used to create a media package channel.

        :param request: Request instance for CreateMediaPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateMediaPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateMediaPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaPackageChannelResponse()
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


    def CreateMediaPackageChannelEndpoint(self, request):
        """This API is used to create an endpoint of a media package channel.

        :param request: Request instance for CreateMediaPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateMediaPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateMediaPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaPackageChannelEndpoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaPackageChannelEndpointResponse()
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


    def DeleteMediaPackageChannelEndpoints(self, request):
        """This API is used to delete endpoints from a media package channel in batches.

        :param request: Request instance for DeleteMediaPackageChannelEndpoints.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteMediaPackageChannelEndpointsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteMediaPackageChannelEndpointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaPackageChannelEndpoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaPackageChannelEndpointsResponse()
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


    def DeleteMediaPackageChannels(self, request):
        """This API is used to delete media package channels in batches.

        :param request: Request instance for DeleteMediaPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteMediaPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteMediaPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaPackageChannels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaPackageChannelsResponse()
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


    def DescribeMediaPackageChannel(self, request):
        """This API is used to query the information of a media package channel.

        :param request: Request instance for DescribeMediaPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeMediaPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeMediaPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaPackageChannelResponse()
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


    def DescribeMediaPackageChannels(self, request):
        """This API is used to query the information list of media package channels.

        :param request: Request instance for DescribeMediaPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeMediaPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeMediaPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaPackageChannels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaPackageChannelsResponse()
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


    def ModifyMediaPackageChannel(self, request):
        """This API is used to modify the information of a media package channel.

        :param request: Request instance for ModifyMediaPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaPackageChannelResponse()
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


    def ModifyMediaPackageChannelEndpoint(self, request):
        """This API is used to modify an endpoint of a media package channel.

        :param request: Request instance for ModifyMediaPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaPackageChannelEndpoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaPackageChannelEndpointResponse()
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


    def ModifyMediaPackageChannelInputAuthInfo(self, request):
        """This API is used to modify the input authentication information of a media package channel.

        :param request: Request instance for ModifyMediaPackageChannelInputAuthInfo.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelInputAuthInfoRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyMediaPackageChannelInputAuthInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaPackageChannelInputAuthInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaPackageChannelInputAuthInfoResponse()
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