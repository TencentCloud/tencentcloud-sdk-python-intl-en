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
from tencentcloud.mdp.v20200527 import models


class MdpClient(AbstractClient):
    _apiVersion = '2020-05-27'
    _endpoint = 'mdp.tencentcloudapi.com'
    _service = 'mdp'


    def BindNewLVBDomainWithChannel(self, request):
        """This API is used to bind an LVB domain name to a channel.

        :param request: Request instance for BindNewLVBDomainWithChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.BindNewLVBDomainWithChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.BindNewLVBDomainWithChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindNewLVBDomainWithChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindNewLVBDomainWithChannelResponse()
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


    def CreateStreamPackageChannel(self, request):
        """This API is used to create a StreamPackage channel.

        :param request: Request instance for CreateStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStreamPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStreamPackageChannelResponse()
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


    def CreateStreamPackageChannelEndpoint(self, request):
        """This API is used to create an endpoint on a StreamPackage channel.

        :param request: Request instance for CreateStreamPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStreamPackageChannelEndpoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStreamPackageChannelEndpointResponse()
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


    def DeleteStreamPackageChannelEndpoints(self, request):
        """This API is used to delete endpoints from a StreamPackage channel in batches.

        :param request: Request instance for DeleteStreamPackageChannelEndpoints.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelEndpointsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelEndpointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStreamPackageChannelEndpoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStreamPackageChannelEndpointsResponse()
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


    def DeleteStreamPackageChannels(self, request):
        """This API is used to delete StreamPackage channels in batches.

        :param request: Request instance for DeleteStreamPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStreamPackageChannels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStreamPackageChannelsResponse()
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


    def DescribeStreamPackageChannel(self, request):
        """This API is used to query the information of a StreamPackage channel.

        :param request: Request instance for DescribeStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamPackageChannelResponse()
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


    def DescribeStreamPackageChannels(self, request):
        """This API is used to query the information of multiple StreamPackage channels.

        :param request: Request instance for DescribeStreamPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamPackageChannels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamPackageChannelsResponse()
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


    def ModifyStreamPackageChannel(self, request):
        """This API is used to modify a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStreamPackageChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStreamPackageChannelResponse()
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


    def ModifyStreamPackageChannelEndpoint(self, request):
        """This API is used to modify an endpoint of a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStreamPackageChannelEndpoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStreamPackageChannelEndpointResponse()
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


    def ModifyStreamPackageChannelInputAuthInfo(self, request):
        """This API is used to modify the input authentication information of a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannelInputAuthInfo.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelInputAuthInfoRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelInputAuthInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStreamPackageChannelInputAuthInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStreamPackageChannelInputAuthInfoResponse()
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