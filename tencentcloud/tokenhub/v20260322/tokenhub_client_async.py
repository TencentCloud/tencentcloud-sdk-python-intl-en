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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tokenhub.v20260322 import models
from typing import Dict


class TokenhubClient(AbstractClient):
    _apiVersion = '2026-03-22'
    _endpoint = 'tokenhub.intl.tencentcloudapi.com'
    _service = 'tokenhub'

    async def CreateApiKey(
            self,
            request: models.CreateApiKeyRequest,
            opts: Dict = None,
    ) -> models.CreateApiKeyResponse:
        """
        Create an API key.

        Create a new API key. Upon successful creation, return the API Key ID. Specify the platform kind, binding method, and initial state.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlossary(
            self,
            request: models.CreateGlossaryRequest,
            opts: Dict = None,
    ) -> models.CreateGlossaryResponse:
        """
        Create a Termbase.

        Create a new Termbase in this application for custom definition source to target language terminology mapping. Return the Termbase ID upon success, which can be used to carry out other management operations on terminology entries.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlossary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlossaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlossaryEntries(
            self,
            request: models.CreateGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateGlossaryEntriesResponse:
        """
        Create terminology entries in batches.

        Create terminology entries in batches under the designated Termbase. You can create up to 100 entries at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTokenPlanApiKeys(
            self,
            request: models.CreateTokenPlanApiKeysRequest,
            opts: Dict = None,
    ) -> models.CreateTokenPlanApiKeysResponse:
        """
        Batch create TokenPlan API Keys.

        Import a name prefix and quantity to automatically generate names in the `{Api Key Name}-{serial number}` format (for example, aaa-1, aaa-2). Duplicate names are allowed. Partial success is supported for up to 100 entries.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTokenPlanApiKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenPlanApiKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTokenPlanTeamOrderAndBuy(
            self,
            request: models.CreateTokenPlanTeamOrderAndBuyRequest,
            opts: Dict = None,
    ) -> models.CreateTokenPlanTeamOrderAndBuyResponse:
        """
        Purchase a package (This API is also used to reactivate and renew expired packages. The teamId of the expired package is required. After the renewal is successful, the total cycle count of the package will include historical cycles. The actual effective cycle of the package is determined by the effective time and expiration time.)

        Initiate an order for a TokenPlan package and complete payment. Return the order ID and associated sub-orders and resource information upon success.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTokenPlanTeamOrderAndBuy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenPlanTeamOrderAndBuyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiKey(
            self,
            request: models.DeleteApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteApiKeyResponse:
        """
        This API is used to delete specified api keys and clean up associated model binding relationships.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlossary(
            self,
            request: models.DeleteGlossaryRequest,
            opts: Dict = None,
    ) -> models.DeleteGlossaryResponse:
        """
        Delete a termbase.

        This API is used to delete specified Termbase and ALL terminology entries under it. The deletion is idempotent and returns a successful result for non-existing Termbase. After calling the API, if the corresponding Termbase cannot be found via DescribeGlossaries, it indicates successful deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlossary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlossaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlossaryEntries(
            self,
            request: models.DeleteGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteGlossaryEntriesResponse:
        """
        Delete terminology entries in batches.

        Delete terminology entries in batches under the specified Termbase. You can delete up to 200 entries at a time. If the Termbase is nonexistent or NOT_IN this application, it returns a ResourceNotFound error.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTokenPlanApiKey(
            self,
            request: models.DeleteTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteTokenPlanApiKeyResponse:
        """
        Delete the Token Plan API key.

        Simultaneously delete the limit center sub-limit package and notify the Notification Gateway to purge cache.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKey(
            self,
            request: models.DescribeApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyResponse:
        """
        This API is used to query API Key details based on API Key ID or key value, and return the plaintext key. At least one of ApiKeyId and ApiKey must be input, with priority given to ApiKeyId.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKeyList(
            self,
            request: models.DescribeApiKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyListResponse:
        """
        Query API key list.

        Query the API key list of the current user with key values in masking display. Support pagination, filtering, and sorting.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlossaries(
            self,
            request: models.DescribeGlossariesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlossariesResponse:
        """
        Query the terminology repository list.

        Query the Termbase list under this application. Support paginate, filter, and sort.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlossaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlossariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlossaryEntries(
            self,
            request: models.DescribeGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlossaryEntriesResponse:
        """
        Query the terminology entry list.

        Query specified entries in a Termbase. Support pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlan(
            self,
            request: models.DescribeTokenPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanResponse:
        """
        Query the TokenPlan package details.

        Return the package basic info and the remaining quota of the package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKey(
            self,
            request: models.DescribeTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyResponse:
        """
        Query TokenPlan APIKey details.

        Return the complete APIKey information (including the plaintext key) and the remaining quota of the sub-quota package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeyList(
            self,
            request: models.DescribeTokenPlanApiKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyListResponse:
        """
        Query the list of Token Plan API keys.

        Returns the API key list under a specified package. Keys are masked. Root accounts can view all keys, while sub-accounts can only view keys created by themselves.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeySecret(
            self,
            request: models.DescribeTokenPlanApiKeySecretRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeySecretResponse:
        """
        Query the TokenPlan APIKey (plaintext).

        Return the plaintext key value of the designated APIKey. Keep it safe.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeyUsageDetail(
            self,
            request: models.DescribeTokenPlanApiKeyUsageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyUsageDetailResponse:
        """
        Query the Token Plan APIKey call detail.

        This API is used to query call details under a package from CLS log service, filter by team_id, and support cursor-based pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeyUsageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyUsageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanList(
            self,
            request: models.DescribeTokenPlanListRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanListResponse:
        """
        Query the list of Token Plan package options.

        Supports pagination, filtering, and sorting. Root accounts can view all packages, while sub-accounts can only view packages created by themselves. Returned results include the main limit package details associated with each package in the limit center.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageRankList(
            self,
            request: models.DescribeUsageRankListRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageRankListResponse:
        """
        Query the usage ranking list.

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
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageRankList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageRankListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiKeyInfo(
            self,
            request: models.ModifyApiKeyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyApiKeyInfoResponse:
        """
        Refresh API key information.

        This API is used to update the remark information, IP allowlist and Token quota of an API key (recommended to use QuotaDesired parameter for quota modification). Passing no optional parameters means no modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiKeyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiKeyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiKeyStatus(
            self,
            request: models.ModifyApiKeyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApiKeyStatusResponse:
        """
        This API is used to enable or disable the status of an api key.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiKeyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiKeyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlossaryEntries(
            self,
            request: models.ModifyGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyGlossaryEntriesResponse:
        """
        Batch modify terminology entries.

        This API is used to batch modify terminology entries in a designated Termbase. You can modify up to 200 entries at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTokenPlanApiKey(
            self,
            request: models.ModifyTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyTokenPlanApiKeyResponse:
        """
        Modify the Token Plan APIKey configuration (field that the gateway focuses on).

        After modification, automatically notify the gateway to update the cache and sync the limit center.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTokenPlanApiKeySecret(
            self,
            request: models.ModifyTokenPlanApiKeySecretRequest,
            opts: Dict = None,
    ) -> models.ModifyTokenPlanApiKeySecretResponse:
        """
        Reset the TokenPlan API Key.

        Regenerate the key value. The key version increments and the old key expires immediately. The API Key ID remains unchanged. After resetting, the new key can be queried through DescribeTokenPlanApiKeySecret.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTokenPlanApiKeySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTokenPlanApiKeySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewTokenPlanTeamOrder(
            self,
            request: models.RenewTokenPlanTeamOrderRequest,
            opts: Dict = None,
    ) -> models.RenewTokenPlanTeamOrderResponse:
        """
        Renew a package.

        Initiate a renewal order for an existing Token Plan package and complete payment. Return the order ID and associated sub-orders and resource information upon success.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewTokenPlanTeamOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewTokenPlanTeamOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeTokenPlanTeamOrder(
            self,
            request: models.UpgradeTokenPlanTeamOrderRequest,
            opts: Dict = None,
    ) -> models.UpgradeTokenPlanTeamOrderResponse:
        """
        Upgrade the package.

        Initiate an upgrade order for an existing Token Plan package and complete payment to expand point or token limits. Return the order ID and associated sub-orders and resource information upon success. The new limit must be greater than the current limit.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeTokenPlanTeamOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeTokenPlanTeamOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)