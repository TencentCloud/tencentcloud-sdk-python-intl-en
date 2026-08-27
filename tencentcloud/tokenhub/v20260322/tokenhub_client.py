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
from tencentcloud.tokenhub.v20260322 import models


class TokenhubClient(AbstractClient):
    _apiVersion = '2026-03-22'
    _endpoint = 'tokenhub.intl.tencentcloudapi.com'
    _service = 'tokenhub'


    def CreateApiKey(self, request):
        r"""Create an API key.

        Create a new API key. Upon successful creation, return the API Key ID. Specify the platform kind, binding method, and initial state.

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlossary(self, request):
        r"""Create a Termbase.

        Create a new Termbase in this application for custom definition source to target language terminology mapping. Return the Termbase ID upon success, which can be used to carry out other management operations on terminology entries.

        :param request: Request instance for CreateGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlossaryEntries(self, request):
        r"""Create terminology entries in batches.

        Create terminology entries in batches under the designated Termbase. You can create up to 100 entries at a time.

        :param request: Request instance for CreateGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTokenPlanApiKeys(self, request):
        r"""Batch create TokenPlan API Keys.

        Import a name prefix and quantity to automatically generate names in the `{Api Key Name}-{serial number}` format (for example, aaa-1, aaa-2). Duplicate names are allowed. Partial success is supported for up to 100 entries.

        :param request: Request instance for CreateTokenPlanApiKeys.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanApiKeysRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanApiKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTokenPlanApiKeys", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTokenPlanApiKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTokenPlanTeamOrderAndBuy(self, request):
        r"""Purchase a package (This API is also used to reactivate and renew expired packages. The teamId of the expired package is required. After the renewal is successful, the total cycle count of the package will include historical cycles. The actual effective cycle of the package is determined by the effective time and expiration time.)

        Initiate an order for a TokenPlan package and complete payment. Return the order ID and associated sub-orders and resource information upon success.

        :param request: Request instance for CreateTokenPlanTeamOrderAndBuy.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanTeamOrderAndBuyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanTeamOrderAndBuyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTokenPlanTeamOrderAndBuy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTokenPlanTeamOrderAndBuyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiKey(self, request):
        r"""This API is used to delete specified api keys and clean up associated model binding relationships.

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossary(self, request):
        r"""Delete a termbase.

        This API is used to delete specified Termbase and ALL terminology entries under it. The deletion is idempotent and returns a successful result for non-existing Termbase. After calling the API, if the corresponding Termbase cannot be found via DescribeGlossaries, it indicates successful deletion.

        :param request: Request instance for DeleteGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossaryEntries(self, request):
        r"""Delete terminology entries in batches.

        Delete terminology entries in batches under the specified Termbase. You can delete up to 200 entries at a time. If the Termbase is nonexistent or NOT_IN this application, it returns a ResourceNotFound error.

        :param request: Request instance for DeleteGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTokenPlanApiKey(self, request):
        r"""Delete the Token Plan API key.

        Simultaneously delete the limit center sub-limit package and notify the Notification Gateway to purge cache.

        :param request: Request instance for DeleteTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKey(self, request):
        r"""This API is used to query API Key details based on API Key ID or key value, and return the plaintext key. At least one of ApiKeyId and ApiKey must be input, with priority given to ApiKeyId.

        :param request: Request instance for DescribeApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKeyList(self, request):
        r"""Query API key list.

        Query the API key list of the current user with key values in masking display. Support pagination, filtering, and sorting.

        :param request: Request instance for DescribeApiKeyList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaries(self, request):
        r"""Query the terminology repository list.

        Query the Termbase list under this application. Support paginate, filter, and sort.

        :param request: Request instance for DescribeGlossaries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaryEntries(self, request):
        r"""Query the terminology entry list.

        Query specified entries in a Termbase. Support pagination.

        :param request: Request instance for DescribeGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlan(self, request):
        r"""Query the TokenPlan package details.

        Return the package basic info and the remaining quota of the package.

        :param request: Request instance for DescribeTokenPlan.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKey(self, request):
        r"""Query TokenPlan APIKey details.

        Return the complete APIKey information (including the plaintext key) and the remaining quota of the sub-quota package.

        :param request: Request instance for DescribeTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeyList(self, request):
        r"""Query the list of Token Plan API keys.

        Returns the API key list under a specified package. Keys are masked. Root accounts can view all keys, while sub-accounts can only view keys created by themselves.

        :param request: Request instance for DescribeTokenPlanApiKeyList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeySecret(self, request):
        r"""Query the TokenPlan APIKey (plaintext).

        Return the plaintext key value of the designated APIKey. Keep it safe.

        :param request: Request instance for DescribeTokenPlanApiKeySecret.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeySecretRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeySecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeyUsageDetail(self, request):
        r"""Query the Token Plan APIKey call detail.

        This API is used to query call details under a package from CLS log service, filter by team_id, and support cursor-based pagination.

        :param request: Request instance for DescribeTokenPlanApiKeyUsageDetail.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyUsageDetailRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeyUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyUsageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanList(self, request):
        r"""Query the list of Token Plan package options.

        Supports pagination, filtering, and sorting. Root accounts can view all packages, while sub-accounts can only view packages created by themselves. Returned results include the main limit package details associated with each package in the limit center.

        :param request: Request instance for DescribeTokenPlanList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsageRankList(self, request):
        r"""Query the usage ranking list.

        Metric family (MetricType)
        - `tokens` (default): Token usage statistics. Supports Dimension = apikey / endpoint / model.
        Metrics returned: TotalToken (total) / InputTotalToken (input) / OutputTotalToken (output) / CacheTotalToken (read cache).
        - `search`: [To be launched] Online search usage statistics. Supports Dimension = apikey / endpoint / model.
        Returns metrics: SearchRequestCount (search request count)/SearchCount (search engine call count).

        content
        -The MetricType field is used to switch metric families. The response echoes back MetricType and MetricKeys.
        -TotalStats: The aggregated value of all objects over the entire time window.
        -PageStats: The aggregated value of objects on the current page.
        - TopList: A list of objects sorted by MetricKeys[0] in descending order, including the aggregated value over the entire period and point-in-time curves.

        :param request: Request instance for DescribeUsageRankList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeUsageRankListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeUsageRankListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageRankList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageRankListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiKeyInfo(self, request):
        r"""Refresh API key information.

        This API is used to update the remark information, IP allowlist and Token quota of an API key (recommended to use QuotaDesired parameter for quota modification). Passing no optional parameters means no modification.

        :param request: Request instance for ModifyApiKeyInfo.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyApiKeyInfoRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyApiKeyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiKeyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiKeyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiKeyStatus(self, request):
        r"""This API is used to enable or disable the status of an api key.

        :param request: Request instance for ModifyApiKeyStatus.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyApiKeyStatusRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyApiKeyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiKeyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiKeyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlossaryEntries(self, request):
        r"""Batch modify terminology entries.

        This API is used to batch modify terminology entries in a designated Termbase. You can modify up to 200 entries at a time.

        :param request: Request instance for ModifyGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTokenPlanApiKey(self, request):
        r"""Modify the Token Plan APIKey configuration (field that the gateway focuses on).

        After modification, automatically notify the gateway to update the cache and sync the limit center.

        :param request: Request instance for ModifyTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTokenPlanApiKeySecret(self, request):
        r"""Reset the TokenPlan API Key.

        Regenerate the key value. The key version increments and the old key expires immediately. The API Key ID remains unchanged. After resetting, the new key can be queried through DescribeTokenPlanApiKeySecret.

        :param request: Request instance for ModifyTokenPlanApiKeySecret.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeySecretRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTokenPlanApiKeySecret", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTokenPlanApiKeySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewTokenPlanTeamOrder(self, request):
        r"""Renew a package.

        Initiate a renewal order for an existing Token Plan package and complete payment. Return the order ID and associated sub-orders and resource information upon success.

        :param request: Request instance for RenewTokenPlanTeamOrder.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.RenewTokenPlanTeamOrderRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.RenewTokenPlanTeamOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewTokenPlanTeamOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RenewTokenPlanTeamOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeTokenPlanTeamOrder(self, request):
        r"""Upgrade the package.

        Initiate an upgrade order for an existing Token Plan package and complete payment to expand point or token limits. Return the order ID and associated sub-orders and resource information upon success. The new limit must be greater than the current limit.

        :param request: Request instance for UpgradeTokenPlanTeamOrder.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.UpgradeTokenPlanTeamOrderRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UpgradeTokenPlanTeamOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeTokenPlanTeamOrder", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeTokenPlanTeamOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))