# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.tts.v20190823 import models


class TtsClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tts.tencentcloudapi.com'
    _service = 'tts'


    def TextToVoice(self, request):
        """This API is used to convert any text to speech, allowing your devices and applications to talk to users.
        ​Tencent Cloud Text To Speech (TTS) can synthesize speech from text in real time for many use cases, such as audiobook and news apps, voice reminders on smart devices, quick synthesis of a celebrity's voice based on existing programs or certain voice records available on the Internet, and personalized vehicle navigation systems.
        It is free for use in beta.
        It supports SSML. For syntax details, see [SSML](https://intl.cloud.tencent.com/document/product/1073/49575?from_cn_redirect=1).

        :param request: Request instance for TextToVoice.
        :type request: :class:`tencentcloud.tts.v20190823.models.TextToVoiceRequest`
        :rtype: :class:`tencentcloud.tts.v20190823.models.TextToVoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToVoice", params, headers=headers)
            response = json.loads(body)
            model = models.TextToVoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)