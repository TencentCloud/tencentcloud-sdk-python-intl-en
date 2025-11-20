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
from tencentcloud.domain.v20180808 import models
from typing import Dict


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.intl.tencentcloudapi.com'
    _service = 'domain'

    async def BatchModifyIntlDomainDNS(
            self,
            request: models.BatchModifyIntlDomainDNSRequest,
            opts: Dict = None,
    ) -> models.BatchModifyIntlDomainDNSResponse:
        """
        This API is used to bulk modify DNS servers for domains.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyIntlDomainDNS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyIntlDomainDNSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyIntlDomainInfo(
            self,
            request: models.BatchModifyIntlDomainInfoRequest,
            opts: Dict = None,
    ) -> models.BatchModifyIntlDomainInfoResponse:
        """
        This API is used to bulk modify registrant information.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyIntlDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyIntlDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIntlDomainNew(
            self,
            request: models.CheckIntlDomainNewRequest,
            opts: Dict = None,
    ) -> models.CheckIntlDomainNewResponse:
        """
        This API is used to check whether a domain is available for registration.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIntlDomainNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIntlDomainNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntlDomainBatch(
            self,
            request: models.CreateIntlDomainBatchRequest,
            opts: Dict = None,
    ) -> models.CreateIntlDomainBatchResponse:
        """
        This API is used to bulk register domains.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntlDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntlDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntlPhoneEmail(
            self,
            request: models.CreateIntlPhoneEmailRequest,
            opts: Dict = None,
    ) -> models.CreateIntlPhoneEmailResponse:
        """
        This API is used to verify a mobile number or an email address via a verification code.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntlPhoneEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntlPhoneEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntlTemplate(
            self,
            request: models.CreateIntlTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateIntlTemplateResponse:
        """
        This API is used to add a registrant profile.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntlPhoneEmail(
            self,
            request: models.DeleteIntlPhoneEmailRequest,
            opts: Dict = None,
    ) -> models.DeleteIntlPhoneEmailResponse:
        """
        This API is used to delete a mobile number or an email address.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntlPhoneEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntlPhoneEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntlTemplate(
            self,
            request: models.DeleteIntlTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteIntlTemplateResponse:
        """
        This API is used to delete a registrant profile.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlBatchDetailStatus(
            self,
            request: models.DescribeIntlBatchDetailStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlBatchDetailStatusResponse:
        """
        This API is used to query the status of a bulk task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlBatchDetailStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlBatchDetailStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlBatchOperationLogs(
            self,
            request: models.DescribeIntlBatchOperationLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlBatchOperationLogsResponse:
        """
        This API is used to query the logs of bulk domain purchase.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlBatchOperationLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlBatchOperationLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlDomain(
            self,
            request: models.DescribeIntlDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlDomainResponse:
        """
        This API is used to query domain information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlDomainBatchDetails(
            self,
            request: models.DescribeIntlDomainBatchDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlDomainBatchDetailsResponse:
        """
        This API is used to get the log details of bulk domain purchase.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlDomainBatchDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlDomainBatchDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlDomainList(
            self,
            request: models.DescribeIntlDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlDomainListResponse:
        """
        This API is used to query the "My domains" list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlDomainPriceNewList(
            self,
            request: models.DescribeIntlDomainPriceNewListRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlDomainPriceNewListResponse:
        """
        This API is used to get the price list by domain suffix.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlDomainPriceNewList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlDomainPriceNewListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlPhoneEmailList(
            self,
            request: models.DescribeIntlPhoneEmailListRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlPhoneEmailListResponse:
        """
        This API is used to get the list of verified mobile numbers and email addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlPhoneEmailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlPhoneEmailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlTemplate(
            self,
            request: models.DescribeIntlTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlTemplateResponse:
        """
        This API is used to get the details of a registrant profile.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntlTemplateList(
            self,
            request: models.DescribeIntlTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeIntlTemplateListResponse:
        """
        This API is used to get the list of registrant profiles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntlTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntlTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwnerIntlBatch(
            self,
            request: models.ModifyOwnerIntlBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyOwnerIntlBatchResponse:
        """
        This API is used to bulk transfer domains to another account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwnerIntlBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwnerIntlBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewIntlDomainBatch(
            self,
            request: models.RenewIntlDomainBatchRequest,
            opts: Dict = None,
    ) -> models.RenewIntlDomainBatchResponse:
        """
        This API is used to bulk renew domains.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewIntlDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewIntlDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendIntlPhoneEmailCode(
            self,
            request: models.SendIntlPhoneEmailCodeRequest,
            opts: Dict = None,
    ) -> models.SendIntlPhoneEmailCodeResponse:
        """
        This API is used to send a verification code to a mobile number or an email address.
        """
        
        kwargs = {}
        kwargs["action"] = "SendIntlPhoneEmailCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendIntlPhoneEmailCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetIntlDomainAutoRenew(
            self,
            request: models.SetIntlDomainAutoRenewRequest,
            opts: Dict = None,
    ) -> models.SetIntlDomainAutoRenewResponse:
        """
        This API is used to set auto-renewal.
        """
        
        kwargs = {}
        kwargs["action"] = "SetIntlDomainAutoRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetIntlDomainAutoRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferInIntlDomainBatch(
            self,
            request: models.TransferInIntlDomainBatchRequest,
            opts: Dict = None,
    ) -> models.TransferInIntlDomainBatchResponse:
        """
        This API is used to bulk transfer domains in.
        """
        
        kwargs = {}
        kwargs["action"] = "TransferInIntlDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferInIntlDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferProhibitionIntlBatch(
            self,
            request: models.TransferProhibitionIntlBatchRequest,
            opts: Dict = None,
    ) -> models.TransferProhibitionIntlBatchResponse:
        """
        This API is used to bulk set transfer prohibition for domains.
        """
        
        kwargs = {}
        kwargs["action"] = "TransferProhibitionIntlBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferProhibitionIntlBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProhibitionIntlBatch(
            self,
            request: models.UpdateProhibitionIntlBatchRequest,
            opts: Dict = None,
    ) -> models.UpdateProhibitionIntlBatchResponse:
        """
        This API is used to bulk set update prohibition for domains.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProhibitionIntlBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProhibitionIntlBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)