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
from tencentcloud.tione.v20211111 import models
from typing import Dict


class TioneClient(AbstractClient):
    _apiVersion = '2021-11-11'
    _endpoint = 'tione.intl.tencentcloudapi.com'
    _service = 'tione'

    async def DescribeModelServiceGroups(
            self,
            request: models.DescribeModelServiceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeModelServiceGroupsResponse:
        """
        This API is used to list online inference service groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelServiceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelServiceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)