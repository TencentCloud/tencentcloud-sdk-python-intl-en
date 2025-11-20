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
from tencentcloud.dms.v20200819 import models
from typing import Dict


class DmsClient(AbstractClient):
    _apiVersion = '2020-08-19'
    _endpoint = 'dms.intl.tencentcloudapi.com'
    _service = 'dms'

    async def SendEmail(
            self,
            request: models.SendEmailRequest,
            opts: Dict = None,
    ) -> models.SendEmailResponse:
        """
        This API is used to send regular emails.
        """
        
        kwargs = {}
        kwargs["action"] = "SendEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendTemplatedEmail(
            self,
            request: models.SendTemplatedEmailRequest,
            opts: Dict = None,
    ) -> models.SendTemplatedEmailResponse:
        """
        This API is used to send template emails.
        """
        
        kwargs = {}
        kwargs["action"] = "SendTemplatedEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendTemplatedEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)