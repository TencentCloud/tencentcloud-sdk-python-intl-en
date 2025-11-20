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
from tencentcloud.tmt.v20180321 import models
from typing import Dict


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.intl.tencentcloudapi.com'
    _service = 'tmt'

    async def TextTranslate(
            self,
            request: models.TextTranslateRequest,
            opts: Dict = None,
    ) -> models.TextTranslateResponse:
        """
        This API is used to translate text in multiple language pairs, such as Chinese-English.<br />
        Note: We recommend that you simplify your development with the SDK integration mode. For how to use the SDK, see Section 5 "Developer Resources".
        """
        
        kwargs = {}
        kwargs["action"] = "TextTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)