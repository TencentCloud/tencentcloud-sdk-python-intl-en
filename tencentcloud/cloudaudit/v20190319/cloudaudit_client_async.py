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
from tencentcloud.cloudaudit.v20190319 import models
from typing import Dict


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.intl.tencentcloudapi.com'
    _service = 'cloudaudit'

    async def CreateAudit(
            self,
            request: models.CreateAuditRequest,
            opts: Dict = None,
    ) -> models.CreateAuditResponse:
        """
        Parameter requirements:
        1. If the value of `IsCreateNewBucket` exists, `cosRegion` and `osBucketName` are required.
        2. If the value of `IsEnableCmqNotify` is 1, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` are required.
        3. If the value of `IsEnableCmqNotify` is 0, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` cannot be passed in.
        4. If the value of `IsEnableKmsEncry` is 1, `KmsRegion` and `KeyId` are required.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditTrack(
            self,
            request: models.CreateAuditTrackRequest,
            opts: Dict = None,
    ) -> models.CreateAuditTrackResponse:
        """
        This API is used to create a tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAudit(
            self,
            request: models.DeleteAuditRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditResponse:
        """
        This API is used to delete a tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditTrack(
            self,
            request: models.DeleteAuditTrackRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditTrackResponse:
        """
        This API is used to delete a CloudAudit tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAudit(
            self,
            request: models.DescribeAuditRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditResponse:
        """
        This API is used to query the details of a tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditTrack(
            self,
            request: models.DescribeAuditTrackRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditTrackResponse:
        """
        This API is used to query the CloudAudit tracking set details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditTracks(
            self,
            request: models.DescribeAuditTracksRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditTracksResponse:
        """
        This API is used to query the CloudAudit tracking set list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditTracks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditTracksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvents(
            self,
            request: models.DescribeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsResponse:
        """
        This API is used to query CloudAudit logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttributeKey(
            self,
            request: models.GetAttributeKeyRequest,
            opts: Dict = None,
    ) -> models.GetAttributeKeyResponse:
        """
        This API is used to query the valid values of `AttributeKey`.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttributeKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttributeKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquireAuditCredit(
            self,
            request: models.InquireAuditCreditRequest,
            opts: Dict = None,
    ) -> models.InquireAuditCreditResponse:
        """
        This API is used to query the number of tracking sets that can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "InquireAuditCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquireAuditCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAudits(
            self,
            request: models.ListAuditsRequest,
            opts: Dict = None,
    ) -> models.ListAuditsResponse:
        """
        This API is used to query the summary of tracking sets.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAudits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuditsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCmqEnableRegion(
            self,
            request: models.ListCmqEnableRegionRequest,
            opts: Dict = None,
    ) -> models.ListCmqEnableRegionResponse:
        """
        This API is used to query CloudAudit-enabled CMQ AZs.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCmqEnableRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCmqEnableRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCosEnableRegion(
            self,
            request: models.ListCosEnableRegionRequest,
            opts: Dict = None,
    ) -> models.ListCosEnableRegionResponse:
        """
        This API is used to query CloudAudit-enabled COS AZs.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCosEnableRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCosEnableRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LookUpEvents(
            self,
            request: models.LookUpEventsRequest,
            opts: Dict = None,
    ) -> models.LookUpEventsResponse:
        """
        This API is used to search for operation logs to help query relevant operation information.
        """
        
        kwargs = {}
        kwargs["action"] = "LookUpEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LookUpEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditTrack(
            self,
            request: models.ModifyAuditTrackRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditTrackResponse:
        """
        This API is used to modify a CloudAudit tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLogging(
            self,
            request: models.StartLoggingRequest,
            opts: Dict = None,
    ) -> models.StartLoggingResponse:
        """
        This API is used to enable a tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "StartLogging"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLoggingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLogging(
            self,
            request: models.StopLoggingRequest,
            opts: Dict = None,
    ) -> models.StopLoggingResponse:
        """
        This API is used to disable a tracking set.
        """
        
        kwargs = {}
        kwargs["action"] = "StopLogging"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLoggingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAudit(
            self,
            request: models.UpdateAuditRequest,
            opts: Dict = None,
    ) -> models.UpdateAuditResponse:
        """
        Parameter requirements:
        1. If the value of `IsCreateNewBucket` exists, `cosRegion` and `osBucketName` are required.
        2. If the value of `IsEnableCmqNotify` is 1, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` are required.
        3. If the value of `IsEnableCmqNotify` is 0, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` cannot be passed in.
        4. If the value of `IsEnableKmsEncry` is 1, `KmsRegion` and `KeyId` are required.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)