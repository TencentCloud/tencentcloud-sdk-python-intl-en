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
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'
    _service = 'faceid'


    def ApplyLivenessToken(self, request):
        """This API is used to apply for a token before calling the liveness detection service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplyLivenessToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplyLivenessTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplyLivenessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyLivenessToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyLivenessTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplySdkVerificationToken(self, request):
        """This API is used to apply for a token before calling the SDK-based verification service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplySdkVerificationToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplySdkVerificationToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplySdkVerificationTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyWebVerificationToken(self, request):
        """This API is used to apply for a token before calling the web-based verification service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplyWebVerificationToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplyWebVerificationTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplyWebVerificationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyWebVerificationToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyWebVerificationTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUploadUrl(self, request):
        """This API is used to generate a temporary `UploadUrl` for uploading resource files (with the `HTTP PUT` method). After resource upload, `ResourceUrl` will be passed to the `TargetAction` API to complete the resource passing (specific fields vary by case).
        The data will be stored in a COS bucket in the region specified by the parameter `Region` for two hours.

        :param request: Request instance for CreateUploadUrl.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CreateUploadUrlRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CreateUploadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUploadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUploadUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetectReflectLivenessAndCompare(self, request):
        """This API is used to detect liveness with the package generated by the liveness comparison (reflection-based) SDK, and to compare the person detected with that in the image passed in.
        The image and the data generated with the SDK must be stored in COS, and the region of the COS bucket must be same as that of requests made with this API. We recommend that you pass resources with upload link APIs.

        :param request: Request instance for DetectReflectLivenessAndCompare.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectReflectLivenessAndCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectReflectLivenessAndCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectReflectLivenessAndCompare", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectReflectLivenessAndCompareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateReflectSequence(self, request):
        """This API is used to generate an appropriate light sequence based on the information collected by the liveness comparison (reflection-based) SDK and pass the light sequence into the SDK to start the identity verification process.
        The data generated with the SDK must be stored in COS, and the region of the COS bucket must be same as that of requests made with this API. We recommend that you pass resources with upload link APIs.

        :param request: Request instance for GenerateReflectSequence.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GenerateReflectSequenceRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GenerateReflectSequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateReflectSequence", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateReflectSequenceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetLivenessResult(self, request):
        """This API is used to get the verification result with the corresponding token (SdkToken) after the liveness detection is completed. The token is valid for two hours after issuance and can be called multiple times.

        :param request: Request instance for GetLivenessResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetLivenessResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetLivenessResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLivenessResult", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLivenessResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSdkVerificationResult(self, request):
        """This API is used to get the verification result with the corresponding token after the SDK-based verification is completed. The token is valid for three days after issuance and can be called multiple times.

        :param request: Request instance for GetSdkVerificationResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetSdkVerificationResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetSdkVerificationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSdkVerificationResult", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSdkVerificationResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetWebVerificationResult(self, request):
        """This API is used to get the verification result with the corresponding token (BizToken) after the web-based verification is completed. The BizToken is valid for three days (3*24*3,600s) after issuance and can be called multiple times.

        :param request: Request instance for GetWebVerificationResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetWebVerificationResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetWebVerificationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWebVerificationResult", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetWebVerificationResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LivenessCompare(self, request):
        """This API is used to pass in a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.
        This API on the legacy version will continue to serve existing users but will be unavailable to new users. We recommend you use `VideoLivenessCompare` for better service quality.

        :param request: Request instance for LivenessCompare.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LivenessCompare", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessCompareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VideoLivenessCompare(self, request):
        """This API is used to pass in URLs of a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.

        :param request: Request instance for VideoLivenessCompare.
        :type request: :class:`tencentcloud.faceid.v20180301.models.VideoLivenessCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.VideoLivenessCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VideoLivenessCompare", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VideoLivenessCompareResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)