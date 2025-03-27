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
    _endpoint = 'mdp.intl.tencentcloudapi.com'
    _service = 'mdp'


    def BindLinearAssemblyCDNDomainWithChannel(self, request):
        """Linear Assembly channel is bound to CDN playback domain name.

        :param request: Request instance for BindLinearAssemblyCDNDomainWithChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.BindLinearAssemblyCDNDomainWithChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.BindLinearAssemblyCDNDomainWithChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindLinearAssemblyCDNDomainWithChannel", params, headers=headers)
            response = json.loads(body)
            model = models.BindLinearAssemblyCDNDomainWithChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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


    def CreateStreamPackageHarvestJob(self, request):
        """Create HarvestJob.

        :param request: Request instance for CreateStreamPackageHarvestJob.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageHarvestJobRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageHarvestJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageHarvestJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageHarvestJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageLinearAssemblyChannel(self, request):
        """Create a linear assembly channel.

        :param request: Request instance for CreateStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageLinearAssemblyChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageLinearAssemblyProgram(self, request):
        """Create a linear assembly program.

        :param request: Request instance for CreateStreamPackageLinearAssemblyProgram.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageLinearAssemblyProgramRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageLinearAssemblyProgramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageLinearAssemblyProgram", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageLinearAssemblyProgramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageSSAIChannel(self, request):
        """CreateStreamPackageSSAIChannel

        :param request: Request instance for CreateStreamPackageSSAIChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSSAIChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSSAIChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageSSAIChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageSSAIChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageSource(self, request):
        """Create channel linear assembly Source.

        :param request: Request instance for CreateStreamPackageSource.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSourceRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamPackageSourceLocation(self, request):
        """Create Linear Assembly SourceLocation.

        :param request: Request instance for CreateStreamPackageSourceLocation.
        :type request: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSourceLocationRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CreateStreamPackageSourceLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamPackageSourceLocation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamPackageSourceLocationResponse()
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


    def DeleteStreamPackageHarvestJob(self, request):
        """Delete HarvestJob.

        :param request: Request instance for DeleteStreamPackageHarvestJob.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageHarvestJobRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageHarvestJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageHarvestJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageHarvestJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageHarvestJobs(self, request):
        """Deleting HarvestJobs in Batch.

        :param request: Request instance for DeleteStreamPackageHarvestJobs.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageHarvestJobsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageHarvestJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageHarvestJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageHarvestJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageLinearAssemblyChannel(self, request):
        """Delete channel linear assemblyChannel.

        :param request: Request instance for DeleteStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageLinearAssemblyChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageLinearAssemblyChannels(self, request):
        """Delete channels in batches and linearly assemble channels.

        :param request: Request instance for DeleteStreamPackageLinearAssemblyChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageLinearAssemblyChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageLinearAssemblyChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageLinearAssemblyProgram(self, request):
        """Delete Channel Linear Assembly Program.

        :param request: Request instance for DeleteStreamPackageLinearAssemblyProgram.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyProgramRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyProgramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageLinearAssemblyProgram", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageLinearAssemblyProgramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageLinearAssemblyPrograms(self, request):
        """Batch deletion of channels linear assembly program.

        :param request: Request instance for DeleteStreamPackageLinearAssemblyPrograms.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyProgramsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageLinearAssemblyProgramsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageLinearAssemblyPrograms", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageLinearAssemblyProgramsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageSSAIChannel(self, request):
        """DeleteStreamPackageSSAIChannel

        :param request: Request instance for DeleteStreamPackageSSAIChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSSAIChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSSAIChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageSSAIChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageSSAIChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageSource(self, request):
        """Delete channel linear assembly Source.

        :param request: Request instance for DeleteStreamPackageSource.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSourceRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamPackageSourceLocation(self, request):
        """Batch delete media packaging SourceLocation.

        :param request: Request instance for DeleteStreamPackageSourceLocation.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSourceLocationRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DeleteStreamPackageSourceLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamPackageSourceLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamPackageSourceLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLinearAssemblyCDNDomainWithChannel(self, request):
        """Query the CDN domain name associated with the LinearAssembly channel.

        :param request: Request instance for DescribeLinearAssemblyCDNDomainWithChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeLinearAssemblyCDNDomainWithChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeLinearAssemblyCDNDomainWithChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLinearAssemblyCDNDomainWithChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLinearAssemblyCDNDomainWithChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLinearAssemblyCDNDomainWithChannels(self, request):
        """Query the CDN domain names associated with all LinearAssembly channels.

        :param request: Request instance for DescribeLinearAssemblyCDNDomainWithChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeLinearAssemblyCDNDomainWithChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeLinearAssemblyCDNDomainWithChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLinearAssemblyCDNDomainWithChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLinearAssemblyCDNDomainWithChannelsResponse()
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


    def DescribeStreamPackageHarvestJob(self, request):
        """Query HarvestJob.

        :param request: Request instance for DescribeStreamPackageHarvestJob.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageHarvestJobRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageHarvestJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageHarvestJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageHarvestJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageHarvestJobs(self, request):
        """Batch query HarvestJob.

        :param request: Request instance for DescribeStreamPackageHarvestJobs.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageHarvestJobsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageHarvestJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageHarvestJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageHarvestJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyChannel(self, request):
        """Query channel linear assembly Channel information.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyChannelAlerts(self, request):
        """Query linear assembly channel alarm information.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyChannelAlerts.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelAlertsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelAlertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyChannelAlerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyChannelAlertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyChannels(self, request):
        """Query channel linear assembly Channel information list.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyProgram(self, request):
        """Query channel linear assembly program information.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyProgram.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyProgram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyProgramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyProgramSchedules(self, request):
        """Query channel linear assembly Programl assembly scheduling information list.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyProgramSchedules.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramSchedulesRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramSchedulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyProgramSchedules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyProgramSchedulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageLinearAssemblyPrograms(self, request):
        """Query channel linear assembly Programl information list.

        :param request: Request instance for DescribeStreamPackageLinearAssemblyPrograms.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageLinearAssemblyProgramsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageLinearAssemblyPrograms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageLinearAssemblyProgramsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSSAIChannel(self, request):
        """DescribeStreamPackageSSAIChannel

        :param request: Request instance for DescribeStreamPackageSSAIChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSSAIChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSSAIChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSSAIChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSSAIChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSSAIChannels(self, request):
        """DescribeStreamPackageSSAIChannels

        :param request: Request instance for DescribeStreamPackageSSAIChannels.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSSAIChannelsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSSAIChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSSAIChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSSAIChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSource(self, request):
        """Query channel linear assembly Source information.

        :param request: Request instance for DescribeStreamPackageSource.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSourceAlerts(self, request):
        """Query channel linear assembly Source alarm information.

        :param request: Request instance for DescribeStreamPackageSourceAlerts.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceAlertsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceAlertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSourceAlerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourceAlertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSourceLocation(self, request):
        """Query channel linear assembly sourceLocation information.

        :param request: Request instance for DescribeStreamPackageSourceLocation.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSourceLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourceLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSourceLocationAlerts(self, request):
        """Query channel linear assembly Location alarm information.

        :param request: Request instance for DescribeStreamPackageSourceLocationAlerts.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationAlertsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationAlertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSourceLocationAlerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourceLocationAlertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSourceLocations(self, request):
        """Query channel linear assembly SourceLocation information list.

        :param request: Request instance for DescribeStreamPackageSourceLocations.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationsRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourceLocationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSourceLocations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourceLocationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPackageSources(self, request):
        """Query channel linear assembly Source information list.

        :param request: Request instance for DescribeStreamPackageSources.
        :type request: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourcesRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DescribeStreamPackageSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPackageSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPackageSourcesResponse()
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


    def ModifyStreamPackageLinearAssemblyChannel(self, request):
        """Modify channel linear assembly Channel configuration.

        :param request: Request instance for ModifyStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageLinearAssemblyChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageLinearAssemblyProgram(self, request):
        """Modify channel linear assembly Program configuration.

        :param request: Request instance for ModifyStreamPackageLinearAssemblyProgram.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageLinearAssemblyProgramRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageLinearAssemblyProgramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageLinearAssemblyProgram", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageLinearAssemblyProgramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageSSAIChannel(self, request):
        """ModifyStreamPackageSSAIChannel

        :param request: Request instance for ModifyStreamPackageSSAIChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSSAIChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSSAIChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageSSAIChannel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageSSAIChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageSource(self, request):
        """Modify channel linear assembly Source configuration.

        :param request: Request instance for ModifyStreamPackageSource.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSourceRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamPackageSourceLocation(self, request):
        """Modify channel linear assembly SourceLocation configuration

        :param request: Request instance for ModifyStreamPackageSourceLocation.
        :type request: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSourceLocationRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ModifyStreamPackageSourceLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamPackageSourceLocation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamPackageSourceLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStreamPackageLinearAssemblyChannel(self, request):
        """Start Linear Assembly Channel.

        :param request: Request instance for StartStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.StartStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.StartStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamPackageLinearAssemblyChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopStreamPackageLinearAssemblyChannel(self, request):
        """Stop linear assembly channel.

        :param request: Request instance for StopStreamPackageLinearAssemblyChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.StopStreamPackageLinearAssemblyChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.StopStreamPackageLinearAssemblyChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamPackageLinearAssemblyChannel", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamPackageLinearAssemblyChannelResponse()
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


    def UnbindLinearAssemblyCDNDomainWithChannel(self, request):
        """Unbind LinearAssembly channel with CDN domain name.

        :param request: Request instance for UnbindLinearAssemblyCDNDomainWithChannel.
        :type request: :class:`tencentcloud.mdp.v20200527.models.UnbindLinearAssemblyCDNDomainWithChannelRequest`
        :rtype: :class:`tencentcloud.mdp.v20200527.models.UnbindLinearAssemblyCDNDomainWithChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindLinearAssemblyCDNDomainWithChannel", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindLinearAssemblyCDNDomainWithChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))