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