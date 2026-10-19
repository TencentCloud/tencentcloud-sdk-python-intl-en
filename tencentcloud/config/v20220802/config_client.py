# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
from tencentcloud.config.v20220802 import models


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.intl.tencentcloudapi.com'
    _service = 'config'


    def AddAggregateCompliancePack(self, request):
        r"""This API is used to create compliance packages for account groups.

        :param request: Request instance for AddAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.AddAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.AddAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAggregateConfigRule(self, request):
        r"""This API is used to create rules for account groups.

        :param request: Request instance for AddAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.AddAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAlarmPolicy(self, request):
        r"""This API is used to add alarm monitoring rules.

        :param request: Request instance for AddAlarmPolicy.
        :type request: :class:`tencentcloud.config.v20220802.models.AddAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AddAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCompliancePack(self, request):
        r"""This API is used to create a compliance package.

        :param request: Request instance for AddCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.AddCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.AddCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddConfigRule(self, request):
        r"""This API is used to create rules.

        :param request: Request instance for AddConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.AddConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAggregateConfigRule(self, request):
        r"""This API is used to close rules for account groups.

        :param request: Request instance for CloseAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseConfigRecorder(self, request):
        r"""This API is used to manage resource monitoring - disabling monitoring.

        :param request: Request instance for CloseConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.CloseConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseConfigRule(self, request):
        r"""Close rules

        :param request: Request instance for CloseConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.CloseConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAggregator(self, request):
        r"""This API is used to create account groups.

        :param request: Request instance for CreateAggregator.
        :type request: :class:`tencentcloud.config.v20220802.models.CreateAggregatorRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CreateAggregatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAggregator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAggregatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRemediation(self, request):
        r"""This API is used to add rule remediation settings.

        :param request: Request instance for CreateRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.CreateRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CreateRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAggregateCompliancePack(self, request):
        r"""This API is used to delete compliance packages for account groups.

        :param request: Request instance for DeleteAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAggregateConfigRule(self, request):
        r"""This API is used to delete rules for account groups.

        :param request: Request instance for DeleteAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAggregators(self, request):
        r"""This API is used to delete account groups.

        :param request: Request instance for DeleteAggregators.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAggregatorsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAggregatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAggregators", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAggregatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarmPolicy(self, request):
        r"""Deletes alarm rules

        :param request: Request instance for DeleteAlarmPolicy.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompliancePack(self, request):
        r"""This API is used to delete compliance packages.

        :param request: Request instance for DeleteCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigRule(self, request):
        r"""Delete a rule

        :param request: Request instance for DeleteConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRemediations(self, request):
        r"""This API is used to delete rule remediation settings.

        :param request: Request instance for DeleteRemediations.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteRemediationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteRemediationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRemediations", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRemediationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateCompliancePack(self, request):
        r"""This API is used to query compliance package details for account groups.

        :param request: Request instance for DescribeAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateConfigDeliver(self, request):
        r"""This API is used to query delivery setting details for account groups.

        :param request: Request instance for DescribeAggregateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateConfigRule(self, request):
        r"""This API is used to query rule details for account groups.

        :param request: Request instance for DescribeAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateDiscoveredResource(self, request):
        r"""This API is used to query resource details for account groups.

        :param request: Request instance for DescribeAggregateDiscoveredResource.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateDiscoveredResourceRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateDiscoveredResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateDiscoveredResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateDiscoveredResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregator(self, request):
        r"""This example shows you how to query account group details.

        :param request: Request instance for DescribeAggregator.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregatorRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregator", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompliancePack(self, request):
        r"""This API is used to query compliance package details.

        :param request: Request instance for DescribeCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigDeliver(self, request):
        r"""This API is used to query delivery setting details.

        :param request: Request instance for DescribeConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigRecorder(self, request):
        r"""This API is used to query monitoring details.

        :param request: Request instance for DescribeConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigRule(self, request):
        r"""This example shows you how to query rule details.

        :param request: Request instance for DescribeConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiscoveredResource(self, request):
        r"""Resource details.

        :param request: Request instance for DescribeDiscoveredResource.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeDiscoveredResourceRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeDiscoveredResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiscoveredResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiscoveredResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemCompliancePack(self, request):
        r"""This API is used to query the system compliance package details.

        :param request: Request instance for DescribeSystemCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeSystemCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeSystemCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemRule(self, request):
        r"""This API is used to preset rule details.

        :param request: Request instance for DescribeSystemRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeSystemRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeSystemRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachAggregateConfigRuleToCompliancePack(self, request):
        r"""This API is used to remove rules from compliance packages for account groups.

        :param request: Request instance for DetachAggregateConfigRuleToCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DetachAggregateConfigRuleToCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DetachAggregateConfigRuleToCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachAggregateConfigRuleToCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DetachAggregateConfigRuleToCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachConfigRuleToCompliancePack(self, request):
        r"""This API is used to remove rules for a compliance package.

        :param request: Request instance for DetachConfigRuleToCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DetachConfigRuleToCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DetachConfigRuleToCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachConfigRuleToCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DetachConfigRuleToCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateCompliancePacks(self, request):
        r"""This API is used to query the list of compliance packages for account groups.

        :param request: Request instance for ListAggregateCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateConfigRuleEvaluationResults(self, request):
        r"""This API is used to query evaluation results from the rule dimension for account groups (the list of evaluation results for resources under a specific rule).

        :param request: Request instance for ListAggregateConfigRuleEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRuleEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRuleEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateConfigRuleResourceEvaluationResults(self, request):
        r"""This API is used to list resource evaluation results of compliance rules in account groups.

        :param request: Request instance for ListAggregateConfigRuleResourceEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleResourceEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleResourceEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRuleResourceEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRuleResourceEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateConfigRules(self, request):
        r"""This API is used to query the list of rules for account groups.

        :param request: Request instance for ListAggregateConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateDiscoveredResources(self, request):
        r"""This API is used to query the list of resources for account groups.

        :param request: Request instance for ListAggregateDiscoveredResources.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateDiscoveredResourcesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateDiscoveredResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateDiscoveredResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateDiscoveredResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregators(self, request):
        r"""Account group list.

        :param request: Request instance for ListAggregators.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregatorsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregators", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAlarmPolicy(self, request):
        r"""Alarm rule list

        :param request: Request instance for ListAlarmPolicy.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ListAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCompliancePacks(self, request):
        r"""This API is used to query the list of compliance packages.

        :param request: Request instance for ListCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRuleEvaluationResults(self, request):
        r"""This API is used to obtain evaluation results from the rule dimension (the list of evaluation results for resources under a specific rule).

        :param request: Request instance for ListConfigRuleEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRuleEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRuleEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRuleEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRuleEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRuleResourceEvaluationResults(self, request):
        r"""This API is used to query the list of resource evaluation results under configuration rules.

        :param request: Request instance for ListConfigRuleResourceEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRuleResourceEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRuleResourceEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRuleResourceEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRuleResourceEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRules(self, request):
        r"""This example shows you how to query the rule list.

        :param request: Request instance for ListConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDiscoveredResources(self, request):
        r"""Obtaining the Resource List

        :param request: Request instance for ListDiscoveredResources.
        :type request: :class:`tencentcloud.config.v20220802.models.ListDiscoveredResourcesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListDiscoveredResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDiscoveredResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListDiscoveredResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRemediationExecutions(self, request):
        r"""Correction records.

        :param request: Request instance for ListRemediationExecutions.
        :type request: :class:`tencentcloud.config.v20220802.models.ListRemediationExecutionsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListRemediationExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRemediationExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListRemediationExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRemediations(self, request):
        r"""This API is used to list remediation settings.

        :param request: Request instance for ListRemediations.
        :type request: :class:`tencentcloud.config.v20220802.models.ListRemediationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListRemediationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRemediations", params, headers=headers)
            response = json.loads(body)
            model = models.ListRemediationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceTypes(self, request):
        r"""This API is used to query the resource type list.

        :param request: Request instance for ListResourceTypes.
        :type request: :class:`tencentcloud.config.v20220802.models.ListResourceTypesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListResourceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSystemCompliancePacks(self, request):
        r"""This API is used to query the list of system compliance packages.

        :param request: Request instance for ListSystemCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListSystemCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListSystemCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSystemCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSystemCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSystemRules(self, request):
        r"""This API is used to query the preset rule list.

        :param request: Request instance for ListSystemRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListSystemRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListSystemRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSystemRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListSystemRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAggregateConfigRule(self, request):
        r"""This API is used to enable a rule for an account group.

        :param request: Request instance for OpenAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenConfigRecorder(self, request):
        r"""This API is used to manage resource monitoring - enabling monitoring.

        :param request: Request instance for OpenConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.OpenConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenConfigRule(self, request):
        r"""Enable rules

        :param request: Request instance for OpenConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.OpenConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutEvaluations(self, request):
        r"""Reporting Evaluation Results Under Custom Rules

        :param request: Request instance for PutEvaluations.
        :type request: :class:`tencentcloud.config.v20220802.models.PutEvaluationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.PutEvaluationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutEvaluations", params, headers=headers)
            response = json.loads(body)
            model = models.PutEvaluationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAggregateConfigRuleEvaluation(self, request):
        r"""This API is used to trigger evaluation for account groups.

        :param request: Request instance for StartAggregateConfigRuleEvaluation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartAggregateConfigRuleEvaluationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartAggregateConfigRuleEvaluationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAggregateConfigRuleEvaluation", params, headers=headers)
            response = json.loads(body)
            model = models.StartAggregateConfigRuleEvaluationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartConfigRuleEvaluation(self, request):
        r"""This API is used to trigger evaluations.

        :param request: Request instance for StartConfigRuleEvaluation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartConfigRuleEvaluationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartConfigRuleEvaluationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartConfigRuleEvaluation", params, headers=headers)
            response = json.loads(body)
            model = models.StartConfigRuleEvaluationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRemediation(self, request):
        r"""This API is used to manually execute rule repairs.

        :param request: Request instance for StartRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.StartRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateCompliancePack(self, request):
        r"""This API is used to edit conformance packages for account groups.

        :param request: Request instance for UpdateAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateCompliancePackStatus(self, request):
        r"""This API is used to enable or disable compliance packages for account groups.

        :param request: Request instance for UpdateAggregateCompliancePackStatus.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackStatusRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateCompliancePackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateCompliancePackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateConfigDeliver(self, request):
        r"""This API is used to edit delivery settings for account groups.

        :param request: Request instance for UpdateAggregateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateConfigRule(self, request):
        r"""This API is used to edit rules for account groups.

        :param request: Request instance for UpdateAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregator(self, request):
        r"""Edit an account group.

        :param request: Request instance for UpdateAggregator.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregatorRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregator", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlarmPolicy(self, request):
        r"""Updating an Alarm Rule

        :param request: Request instance for UpdateAlarmPolicy.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCompliancePack(self, request):
        r"""This API is used to edit a conformance pack.

        :param request: Request instance for UpdateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCompliancePackStatus(self, request):
        r"""This API is used to enable or disable compliance packages.

        :param request: Request instance for UpdateCompliancePackStatus.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackStatusRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCompliancePackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCompliancePackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigDeliver(self, request):
        r"""This API is used to edit shipping settings.

        :param request: Request instance for UpdateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigRecorder(self, request):
        r"""Edit the monitoring scope.

        :param request: Request instance for UpdateConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigRule(self, request):
        r"""This API is used to edit a rule.

        :param request: Request instance for UpdateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRemediation(self, request):
        r"""This API is used to add alarm monitoring rules.

        :param request: Request instance for UpdateRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))