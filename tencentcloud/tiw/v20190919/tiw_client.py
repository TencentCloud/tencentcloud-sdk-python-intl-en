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
from tencentcloud.tiw.v20190919 import models


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'
    _service = 'tiw'


    def CreateTranscode(self, request):
        """This API is used to create a document transcoding task.

        :param request: Request instance for CreateTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecord(self, request):
        """This API is used to query the status and result of a real-time recording task.

        :param request: Request instance for DescribeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecordCallback(self, request):
        """This API is used to query the real-time recording callback address.

        :param request: Request instance for DescribeOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscode(self, request):
        """This API is used to query the progress and result of a document transcoding task.

        :param request: Request instance for DescribeTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscodeCallback(self, request):
        """This API is used to query the document transcoding callback address.

        :param request: Request instance for DescribeTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseOnlineRecord(self, request):
        """This API is used to pause real-time recording.

        :param request: Request instance for PauseOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeOnlineRecord(self, request):
        """This API is used to resume real-time recording.

        :param request: Request instance for ResumeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOnlineRecordCallback(self, request):
        """This API is used to set the real-time recording callback address. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40258?from_cn_redirect=1).

        :param request: Request instance for SetOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOnlineRecordCallbackKey(self, request):
        """This API is used to set the callback authentication key for real-time recording. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetOnlineRecordCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTranscodeCallback(self, request):
        """This API is used to set the callback address for document transcoding. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40260?from_cn_redirect=1).

        :param request: Request instance for SetTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTranscodeCallbackKey(self, request):
        """This API is used to set the callback authentication key for document transcoding. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetTranscodeCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartOnlineRecord(self, request):
        """This API is used to start a real-time recording task.

        :param request: Request instance for StartOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopOnlineRecord(self, request):
        """This API is used to stop real-time recording.

        :param request: Request instance for StopOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)