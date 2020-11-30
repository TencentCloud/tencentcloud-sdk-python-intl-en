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
from tencentcloud.mdl.v20200326 import models


class MdlClient(AbstractClient):
    _apiVersion = '2020-03-26'
    _endpoint = 'mdl.tencentcloudapi.com'
    _service = 'mdl'


    def CreateMediaLiveChannel(self, request):
        """This API is used to create a media channel.

        :param request: Request instance for CreateMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaLiveChannelResponse()
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


    def CreateMediaLiveInput(self, request):
        """This API is used to create a media input.

        :param request: Request instance for CreateMediaLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveInputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaLiveInput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaLiveInputResponse()
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


    def CreateMediaLiveInputSecurityGroup(self, request):
        """This API is used to create an input security group. Up to 5 ones can be created.

        :param request: Request instance for CreateMediaLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateMediaLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaLiveInputSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaLiveInputSecurityGroupResponse()
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


    def DeleteMediaLiveChannel(self, request):
        """This API is used to delete a MediaLive channel.

        :param request: Request instance for DeleteMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaLiveChannelResponse()
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


    def DeleteMediaLiveInput(self, request):
        """This API is used to delete a media input.

        :param request: Request instance for DeleteMediaLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveInputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaLiveInput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaLiveInputResponse()
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


    def DeleteMediaLiveInputSecurityGroup(self, request):
        """This API is used to delete an input security group.

        :param request: Request instance for DeleteMediaLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteMediaLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaLiveInputSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaLiveInputSecurityGroupResponse()
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


    def DescribeMediaLiveChannel(self, request):
        """This API is used to query the information of a MediaLive channel.

        :param request: Request instance for DescribeMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelResponse()
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


    def DescribeMediaLiveChannelAlerts(self, request):
        """This API is used to query the channel alarm information.

        :param request: Request instance for DescribeMediaLiveChannelAlerts.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelAlertsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelAlertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannelAlerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelAlertsResponse()
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


    def DescribeMediaLiveChannelInputStatistics(self, request):
        """This API is used to query the input statistics.

        :param request: Request instance for DescribeMediaLiveChannelInputStatistics.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelInputStatisticsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelInputStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannelInputStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelInputStatisticsResponse()
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


    def DescribeMediaLiveChannelLogs(self, request):
        """This API is used to query MediaLive channel logs, such as push event logs.

        :param request: Request instance for DescribeMediaLiveChannelLogs.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelLogsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannelLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelLogsResponse()
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


    def DescribeMediaLiveChannelOutputStatistics(self, request):
        """This API is used to query the output statistics of a channel.

        :param request: Request instance for DescribeMediaLiveChannelOutputStatistics.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelOutputStatisticsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelOutputStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannelOutputStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelOutputStatisticsResponse()
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


    def DescribeMediaLiveChannels(self, request):
        """This API is used to query the information of MediaLive channels in batches.

        :param request: Request instance for DescribeMediaLiveChannels.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveChannelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveChannels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveChannelsResponse()
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


    def DescribeMediaLiveInput(self, request):
        """This API is used to query a media input.

        :param request: Request instance for DescribeMediaLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveInput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveInputResponse()
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


    def DescribeMediaLiveInputSecurityGroup(self, request):
        """This API is used to query an input security group.

        :param request: Request instance for DescribeMediaLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveInputSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveInputSecurityGroupResponse()
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


    def DescribeMediaLiveInputSecurityGroups(self, request):
        """This API is used to query the information of input security groups in batches.

        :param request: Request instance for DescribeMediaLiveInputSecurityGroups.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveInputSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveInputSecurityGroupsResponse()
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


    def DescribeMediaLiveInputs(self, request):
        """This API is used to query the information of media inputs in batches.

        :param request: Request instance for DescribeMediaLiveInputs.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeMediaLiveInputsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaLiveInputs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaLiveInputsResponse()
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


    def ModifyMediaLiveChannel(self, request):
        """This API is used to modify the information of a MediaLive channel.

        :param request: Request instance for ModifyMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaLiveChannelResponse()
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


    def ModifyMediaLiveInput(self, request):
        """This API is used to update a media input.

        :param request: Request instance for ModifyMediaLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveInputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaLiveInput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaLiveInputResponse()
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


    def ModifyMediaLiveInputSecurityGroup(self, request):
        """This API is used to update an input security group.

        :param request: Request instance for ModifyMediaLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyMediaLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaLiveInputSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaLiveInputSecurityGroupResponse()
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


    def StartMediaLiveChannel(self, request):
        """This API is used to start a MediaLive channel.

        :param request: Request instance for StartMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.StartMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.StartMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMediaLiveChannelResponse()
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


    def StopMediaLiveChannel(self, request):
        """This API is used to stop a MediaLive channel.

        :param request: Request instance for StopMediaLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.StopMediaLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.StopMediaLiveChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMediaLiveChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMediaLiveChannelResponse()
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