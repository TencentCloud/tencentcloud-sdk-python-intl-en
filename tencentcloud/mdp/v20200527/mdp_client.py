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
            headers = request.headers
            body = self.call("BindNewLVBDomainWithChannel", params, headers=headers)
            response = json.loads(body)
            model = models.BindNewLVBDomainWithChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageChannel(self, request):
        """This API is used to create a StreamPackage channel.

        :param request: Request instance for CreateStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageChannelEndpoint(self, request):
        """This API is used to create an endpoint on a StreamPackage channel.

        :param request: Request instance for CreateStreamPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageChannelEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageChannelEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageChannelEndpoints(self, request):
        """This API is used to delete endpoints from a StreamPackage channel in batches.

        :param request: Request instance for DeleteStreamPackageChannelEndpoints.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelEndpointsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageChannelEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageChannelEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageChannels(self, request):
        """This API is used to delete StreamPackage channels in batches.

        :param request: Request instance for DeleteStreamPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageChannel(self, request):
        """This API is used to query the information of a StreamPackage channel.

        :param request: Request instance for DescribeStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageChannels(self, request):
        """This API is used to query the information of multiple StreamPackage channels.

        :param request: Request instance for DescribeStreamPackageChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageChannel(self, request):
        """This API is used to modify a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageChannel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageChannelEndpoint(self, request):
        """This API is used to modify an endpoint of a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannelEndpoint.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelEndpointRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageChannelEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageChannelEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageChannelInputAuthInfo(self, request):
        """This API is used to modify the input authentication information of a StreamPackage channel.

        :param request: Request instance for ModifyStreamPackageChannelInputAuthInfo.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelInputAuthInfoRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageChannelInputAuthInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageChannelInputAuthInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageChannelInputAuthInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindCdnDomainWithChannel(self, request):
        """This API is used to unbind a CDN playback domain name from a channel.

        :param request: Request instance for UnbindCdnDomainWithChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.UnbindCdnDomainWithChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.UnbindCdnDomainWithChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindCdnDomainWithChannel", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindCdnDomainWithChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))