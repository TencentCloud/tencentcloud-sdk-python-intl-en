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
from tencentcloud.monitor.v20180724 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'


    def BindingPolicyObject(self, request):
        """This API is used to bind an alarm policy to a specific object.

        :param request: Request instance for BindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindingPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindingPolicyObjectResponse()
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


    def CreateAlarmNotice(self, request):
        """This API is used to create a notification template.

        :param request: Request instance for CreateAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAlarmNotice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAlarmNoticeResponse()
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


    def CreateAlarmPolicy(self, request):
        """This API is used to create an alarm policy.

        :param request: Request instance for CreateAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAlarmPolicyResponse()
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


    def CreatePolicyGroup(self, request):
        """This API is used to add a policy group.

        :param request: Request instance for CreatePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyGroupResponse()
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


    def DeleteAlarmNotices(self, request):
        """This API is used to delete alarm notification templates.

        :param request: Request instance for DeleteAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlarmNotices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAlarmNoticesResponse()
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


    def DeleteAlarmPolicy(self, request):
        """This API is used to delete an alarm policy.

        :param request: Request instance for DeleteAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAlarmPolicyResponse()
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


    def DeletePolicyGroup(self, request):
        """This API is used to delete an alarm policy group.

        :param request: Request instance for DeletePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyGroupResponse()
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


    def DescribeAccidentEventList(self, request):
        """This API is used to get the platform event list.

        :param request: Request instance for DescribeAccidentEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccidentEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccidentEventListResponse()
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


    def DescribeAlarmEvents(self, request):
        """This API is used to query the list of alarm events.

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmEventsResponse()
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


    def DescribeAlarmHistories(self, request):
        """This API is used to query the alarm records.

        :param request: Request instance for DescribeAlarmHistories.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmHistories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmHistoriesResponse()
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


    def DescribeAlarmMetrics(self, request):
        """This API is used to query the list of alarm metrics.

        :param request: Request instance for DescribeAlarmMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmMetrics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmMetricsResponse()
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


    def DescribeAlarmNotice(self, request):
        """This API is used to query the details of a single notification template.

        :param request: Request instance for DescribeAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmNotice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticeResponse()
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


    def DescribeAlarmNoticeCallbacks(self, request):
        """This API is used to get all the callback URLs of an alarm notification template.

        :param request: Request instance for DescribeAlarmNoticeCallbacks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmNoticeCallbacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticeCallbacksResponse()
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


    def DescribeAlarmNotices(self, request):
        """This API is used to query the list of notification templates.

        :param request: Request instance for DescribeAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmNotices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticesResponse()
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


    def DescribeAlarmPolicies(self, request):
        """This API is used to query the list of alarm policies.

        :param request: Request instance for DescribeAlarmPolicies.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmPoliciesResponse()
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


    def DescribeAlarmPolicy(self, request):
        """This API is used to get the details of a single alarm policy.

        :param request: Request instance for DescribeAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmPolicyResponse()
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


    def DescribeAllNamespaces(self, request):
        """This API is used to query all namespaces.

        :param request: Request instance for DescribeAllNamespaces.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllNamespacesResponse()
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


    def DescribeBaseMetrics(self, request):
        """This API is used to get the attributes of basic metrics.

        :param request: Request instance for DescribeBaseMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaseMetrics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaseMetricsResponse()
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


    def DescribeBasicAlarmList(self, request):
        """This API is used to get the basic alarm list.

        :param request: Request instance for DescribeBasicAlarmList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicAlarmList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicAlarmListResponse()
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


    def DescribeBindingPolicyObjectList(self, request):
        """This API is used to get the bound object list.

        :param request: Request instance for DescribeBindingPolicyObjectList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBindingPolicyObjectList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindingPolicyObjectListResponse()
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


    def DescribeMonitorTypes(self, request):
        """This API is used to list all the monitor types supported by CM.

        :param request: Request instance for DescribeMonitorTypes.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMonitorTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMonitorTypesResponse()
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


    def DescribePolicyConditionList(self, request):
        """This API is used to get basic alarm policy conditions.

        :param request: Request instance for DescribePolicyConditionList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyConditionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyConditionListResponse()
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


    def DescribePolicyGroupInfo(self, request):
        """This API is used to get details of a basic policy group.

        :param request: Request instance for DescribePolicyGroupInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupInfoResponse()
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


    def DescribePolicyGroupList(self, request):
        """This API is used to get the list of basic policy alarm groups.

        :param request: Request instance for DescribePolicyGroupList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupListResponse()
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


    def DescribeProductEventList(self, request):
        """This API is used to get the list of product events by page.

        :param request: Request instance for DescribeProductEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductEventListResponse()
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


    def DescribeStatisticData(self, request):
        """This API is used to query monitoring data by dimension conditions.

        :param request: Request instance for DescribeStatisticData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStatisticData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStatisticDataResponse()
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


    def GetMonitorData(self, request):
        """This API is used to get the monitoring data of a Tencent Cloud service by passing in its namespace, object dimension description, and monitoring metrics.
        API call rate limit: 20 calls/second (1,200 calls/minute). A single request can obtain the data of up to 10 instances and up to 1,440 data points.
        This API may fail due to the rate limit if you need to call a lot of metrics and objects. We recommended that you spread the call requests over time.

        :param request: Request instance for GetMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetMonitorData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetMonitorDataResponse()
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


    def ModifyAlarmNotice(self, request):
        """This API is used to edit an alarm notification template.

        :param request: Request instance for ModifyAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmNotice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmNoticeResponse()
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


    def ModifyAlarmPolicyCondition(self, request):
        """This API is used to modify the trigger condition of an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyCondition.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmPolicyCondition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyConditionResponse()
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


    def ModifyAlarmPolicyInfo(self, request):
        """This API is used to edit the basic information of a v2.0 alarm policy, including policy name and remarks.

        :param request: Request instance for ModifyAlarmPolicyInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmPolicyInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyInfoResponse()
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


    def ModifyAlarmPolicyNotice(self, request):
        """This API is used to modify the alarm notification template bound to an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmPolicyNotice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyNoticeResponse()
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


    def ModifyAlarmPolicyStatus(self, request):
        """This API is used to enable/disable an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmPolicyStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyStatusResponse()
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


    def ModifyAlarmPolicyTasks(self, request):
        """This API is used to modify the task triggered by an alarm policy. The `TriggerTasks` field contains the list of triggered tasks. If an empty array is passed in for `TriggerTasks`, it indicates to unbind all the triggered tasks from this policy.

        :param request: Request instance for ModifyAlarmPolicyTasks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmPolicyTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyTasksResponse()
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


    def ModifyAlarmReceivers(self, request):
        """This API is used to modify alarm recipients.

        :param request: Request instance for ModifyAlarmReceivers.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmReceiversResponse()
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


    def ModifyPolicyGroup(self, request):
        """This API is used to update policy group.

        :param request: Request instance for ModifyPolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPolicyGroupResponse()
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


    def PutMonitorData(self, request):
        """The default API request rate limit is 50 requests/sec.
        The default upper limit on metrics of a single tenant is 100.
        A maximum of 30 metric/value pairs can be reported at a time. When an error is returned for a request, no metrics/values in the request will be saved.

        The reporting timestamp is the timestamp when you want to save the data. We recommend that you construct a timestamp at integer minutes.
        The time range of a timestamp is from 300 seconds before the current time to the current time.
        The data of the same IP metric/value pair must be reported by minute in chronological order.

        :param request: Request instance for PutMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutMonitorData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutMonitorDataResponse()
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


    def SendCustomAlarmMsg(self, request):
        """This API is used to send a custom alarm notification.

        :param request: Request instance for SendCustomAlarmMsg.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendCustomAlarmMsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendCustomAlarmMsgResponse()
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


    def SetDefaultAlarmPolicy(self, request):
        """This API is used to set an alarm policy as the default policy in the current policy type under the current project.
        Alarm policies in the same type under the project will be set as non-default.

        :param request: Request instance for SetDefaultAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetDefaultAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDefaultAlarmPolicyResponse()
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


    def UnBindingAllPolicyObject(self, request):
        """This API is used to delete all bound objects.

        :param request: Request instance for UnBindingAllPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindingAllPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingAllPolicyObjectResponse()
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


    def UnBindingPolicyObject(self, request):
        """This API is used to delete an object that is bound to a policy.

        :param request: Request instance for UnBindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindingPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingPolicyObjectResponse()
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