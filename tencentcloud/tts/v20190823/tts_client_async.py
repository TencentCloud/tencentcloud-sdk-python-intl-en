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
from tencentcloud.tts.v20190823 import models
from typing import Dict


class TtsClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tts.intl.tencentcloudapi.com'
    _service = 'tts'

    async def TextToVoice(
            self,
            request: models.TextToVoiceRequest,
            opts: Dict = None,
    ) -> models.TextToVoiceResponse:
        """
        This API is used to convert any text to speech, allowing your devices and applications to talk to users.
        u200bTencent Cloud Text To Speech (TTS) can synthesize speech from text in real time for many use cases, such as audiobook and news apps, voice reminders on smart devices, quick synthesis of a celebrity's voice based on existing programs or certain voice records available on the internet, and personalized vehicle navigation systems.
        It is free for use in beta.
        It supports SSML. For syntax details, see [SSML](https://intl.cloud.tencent.com/document/product/1073/49575?from_cn_redirect=1).
        Default API request rate limit: 20 requests/sec.
        """
        
        kwargs = {}
        kwargs["action"] = "TextToVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)