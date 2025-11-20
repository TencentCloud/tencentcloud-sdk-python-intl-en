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
from tencentcloud.quota.v20241204 import models
from typing import Dict


class QuotaClient(AbstractClient):
    _apiVersion = '2024-12-04'
    _endpoint = 'quota.intl.tencentcloudapi.com'
    _service = 'quota'

    async def CreateAlarm(
            self,
            request: models.CreateAlarmRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmResponse:
        """
        Add alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarm(
            self,
            request: models.DeleteAlarmRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmResponse:
        """
        Deletes alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarms(
            self,
            request: models.DescribeAlarmsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmsResponse:
        """
        This API is used to query the alarm rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAlarm(
            self,
            request: models.EnableAlarmRequest,
            opts: Dict = None,
    ) -> models.EnableAlarmResponse:
        """
        This API is used to enable alarm rules.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlarm(
            self,
            request: models.UpdateAlarmRequest,
            opts: Dict = None,
    ) -> models.UpdateAlarmResponse:
        """
        Modifies alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)