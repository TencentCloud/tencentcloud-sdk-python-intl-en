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
from tencentcloud.yunjing.v20180228 import models


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.tencentcloudapi.com'
    _service = 'yunjing'


    def AddLoginWhiteList(self, request):
        """This API is used to add a allowlist rule.

        :param request: Request instance for AddLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.AddLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddMachineTag(self, request):
        """This API is used to add a tag to a server.

        :param request: Request instance for AddMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.AddMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseProVersion(self, request):
        """This API is used to deactivate CWP Pro.

        :param request: Request instance for CloseProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenPortTask(self, request):
        """This API is used to create a real-time port acquisition task.

        :param request: Request instance for CreateOpenPortTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenPortTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenPortTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProcessTask(self, request):
        """This API is used to create a real-time process pulling task.

        :param request: Request instance for CreateProcessTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcessTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcessTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUsualLoginPlaces(self, request):
        """This API is used to add one or more usual login locations.

        :param request: Request instance for CreateUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBruteAttacks(self, request):
        """This API is used to delete brute force attack records.

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoginWhiteList(self, request):
        """This API is used to delete a allowlist rule.

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMachine(self, request):
        """This API is used to uninstall the CWP agent.

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMachineTag(self, request):
        """This API is used to remove a tag from a server.

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMaliciousRequests(self, request):
        """This API is used to delete malicious request records.

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMalwares(self, request):
        """This API is used to delete trojan records.

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNonlocalLoginPlaces(self, request):
        """This API is used to delete unusual login location records.

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUsualLoginPlaces(self, request):
        """This API is used to delete one or more usual login locations.

        :param request: Request instance for DeleteUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountStatistics(self, request):
        """This API is used to get the account statistics list.

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """This API is used to get the account list.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentVuls(self, request):
        """This API is used to get the list of vulnerabilities on a single server.

        :param request: Request instance for DescribeAgentVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmAttribute(self, request):
        """This API is used to get the alarm settings.

        :param request: Request instance for DescribeAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBruteAttacks(self, request):
        """This API is used to get the brute force attack event list.

        :param request: Request instance for DescribeBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComponentInfo(self, request):
        """This API is used to get the component information.

        :param request: Request instance for DescribeComponentInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComponentStatistics(self, request):
        """This API is used to get the component statistics list.

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComponents(self, request):
        """This API is used to get the component list.

        :param request: Request instance for DescribeComponents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHistoryAccounts(self, request):
        """This API is used to get the account change history list.

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImpactedHosts(self, request):
        """This API is used to get the list of servers affected by a vulnerability.

        :param request: Request instance for DescribeImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoginWhiteList(self, request):
        """This API is used to get the list of login allowlist entries.

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachineInfo(self, request):
        """This API is used to get server details.

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachines(self, request):
        """This API is used to get the list of servers in a specified region.

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMaliciousRequests(self, request):
        """This API is used to get malicious request data.

        :param request: Request instance for DescribeMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMalwares(self, request):
        """This API is used to get the list of trojan events.

        :param request: Request instance for DescribeMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNonlocalLoginPlaces(self, request):
        """This API is used to get unusual login events.

        :param request: Request instance for DescribeNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOpenPortStatistics(self, request):
        """This API is used to get the statistics on port usage

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOpenPortTaskStatus(self, request):
        """This API is used to get the status of a real-time port pulling task.

        :param request: Request instance for DescribeOpenPortTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOpenPorts(self, request):
        """This API is used to get the port list.

        :param request: Request instance for DescribeOpenPorts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOverviewStatistics(self, request):
        """This API is used to get the overview statistics of CWP under the current account.

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProVersionInfo(self, request):
        """This API is used to get the CWP Pro information.

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProcessStatistics(self, request):
        """This API is used to get the process statistics list.

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProcessTaskStatus(self, request):
        """This API is used to get the status of a real-time process pulling task.

        :param request: Request instance for DescribeProcessTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProcesses(self, request):
        """This API is used to get the process list.

        :param request: Request instance for DescribeProcesses.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcesses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityDynamics(self, request):
        """This API is used to get the security event message data.

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityDynamics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityDynamicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityTrends(self, request):
        """This API is used to get the security event statistics.

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagMachines(self, request):
        """This API is used to get the information of servers associated with a specified tag.

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTags(self, request):
        """This API is used to get all server tags.

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsualLoginPlaces(self, request):
        """This API is used to query usual login locations.

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulInfo(self, request):
        """This API is used to get vulnerability details.

        :param request: Request instance for DescribeVulInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulScanResult(self, request):
        """This API is used to get the vulnerability detection result.

        :param request: Request instance for DescribeVulScanResult.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVuls(self, request):
        """This API is used to get the vulnerability list.

        :param request: Request instance for DescribeVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReportBruteAttacks(self, request):
        """This API is used to get the brute force attack data in the weekly CWP Pro report.

        :param request: Request instance for DescribeWeeklyReportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReportInfo(self, request):
        """This API is used to get the details in the weekly CWP Pro report.

        :param request: Request instance for DescribeWeeklyReportInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReportMalwares(self, request):
        """This API is used to get the trojan data in the weekly CWP Pro report.

        :param request: Request instance for DescribeWeeklyReportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReportNonlocalLoginPlaces(self, request):
        """This API is used to get the unusual login location data in the weekly CWP Pro report.

        :param request: Request instance for DescribeWeeklyReportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReportVuls(self, request):
        """This API is used to get the vulnerability data in the weekly CWP Pro report.

        :param request: Request instance for DescribeWeeklyReportVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWeeklyReports(self, request):
        """This API is used to get the weekly report list.

        :param request: Request instance for DescribeWeeklyReports.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EditTags(self, request):
        """This API is used to add or edit tags.

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditTags", params, headers=headers)
            response = json.loads(body)
            model = models.EditTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportBruteAttacks(self, request):
        """This API is used to export brute force attack records into a CSV file.

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportMaliciousRequests(self, request):
        """This API is used to export the malicious request file into a CSV file for download.

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportMalwares(self, request):
        """This API is used to export trojan records into a CSV file.

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportNonlocalLoginPlaces(self, request):
        """This API is used to export unusual login location events into a CSV file.

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.ExportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IgnoreImpactedHosts(self, request):
        """This API is used to ignore one or more vulnerabilities.

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MisAlarmNonlocalLoginPlaces(self, request):
        """This API is used to set the current location as the usual login location.

        :param request: Request instance for MisAlarmNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MisAlarmNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.MisAlarmNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmAttribute(self, request):
        """This API is used to modify alarm settings.

        :param request: Request instance for ModifyAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAutoOpenProVersionConfig(self, request):
        """This API is used to set whether to automatically activate CWP Pro for newly added servers.

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoOpenProVersionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoOpenProVersionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLoginWhiteList(self, request):
        """This API is used to edit a allowlist rule.

        :param request: Request instance for ModifyLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProVersionRenewFlag(self, request):
        """This API is used to modify the renewal flag of CWP Pro.

        :param request: Request instance for ModifyProVersionRenewFlag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProVersionRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProVersionRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenProVersion(self, request):
        """This API is used to activate CWP Pro.

        :param request: Request instance for OpenProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenProVersion", params, headers=headers)
            response = json.loads(body)
            model = models.OpenProVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverMalwares(self, request):
        """This API is used to recover isolated trojan files in a batch.

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RescanImpactedHost(self, request):
        """This API is used to re-scan for vulnerabilities.

        :param request: Request instance for RescanImpactedHost.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RescanImpactedHost", params, headers=headers)
            response = json.loads(body)
            model = models.RescanImpactedHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SeparateMalwares(self, request):
        """This API is used to isolate trojans.

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SeparateMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.SeparateMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TrustMaliciousRequest(self, request):
        """This API is used to trust a malicious request.

        :param request: Request instance for TrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMaliciousRequest", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMaliciousRequestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TrustMalwares(self, request):
        """This API is used to trust an identified trojan file.

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UntrustMaliciousRequest(self, request):
        """This API is used to untrust a malicious request.

        :param request: Request instance for UntrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMaliciousRequest", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMaliciousRequestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UntrustMalwares(self, request):
        """This API is used to untrust a trojan file.

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)