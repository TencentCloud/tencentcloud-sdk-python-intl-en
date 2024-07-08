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


    def ApplyCardVerification(self, request):
        """The types of national cards supported by the API and whether instructions on the back of the card are required are as follows:
        <table> <thead> <tr> <td>Nationality</td> <td style="width:200px">CardType</td> <td style="width:200px">Back side required</td> </tr> </thead> <tbody> <tr> <td>Indonesia</td> <td>ID card</td> <td>No</td> </tr> <tr> <td>Indonesia</td> <td>Drving license</td> <td>No</td> </tr> <tr> <td>Hongkong</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Thailand</td> <td>ID card</td> <td>No</td> </tr> <tr> <td>Thailand</td> <td>Drving license</td> <td>Yes</td> </tr> <tr> <td>Malaysia</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Malaysia</td> <td>Drving license</td> <td>Yes</td> </tr> <tr> <td>Singapore</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Singapore</td> <td>Drving license</td> <td>Yes</td> </tr> <tr> <td>Philippine</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Philippine</td> <td>Drving license</td> <td>No</td> </tr> <tr> <td>Japan</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Japan</td> <td>Drving license</td> <td>No</td> </tr> </tbody> </table>

        :param request: Request instance for ApplyCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplyCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplyCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ApplyLivenessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplySdkVerificationToken(self, request):
        """This API is used to apply for a token before calling the Identity Verification SDK service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplySdkVerificationToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplySdkVerificationToken", params, headers=headers)
            response = json.loads(body)
            model = models.ApplySdkVerificationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyWebVerificationBizTokenIntl(self, request):
        """This API is used to apply for a BizToken before calling the web-based verification service each time. This token is required for initiating a verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplyWebVerificationBizTokenIntl.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplyWebVerificationBizTokenIntlRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplyWebVerificationBizTokenIntlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyWebVerificationBizTokenIntl", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyWebVerificationBizTokenIntlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ApplyWebVerificationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareFaceLiveness(self, request):
        """This interface supports judgment of real person and photo comparison to verify the user's identity online. By passing the video and photo into the interface, it will first judge whether the person in the video is real. If yes, it judges whether the person in the video is the same one as the uploaded photo and returns authentication result.

        :param request: Request instance for CompareFaceLiveness.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CompareFaceLivenessRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CompareFaceLivenessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareFaceLiveness", params, headers=headers)
            response = json.loads(body)
            model = models.CompareFaceLivenessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateUploadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DetectReflectLivenessAndCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.GenerateReflectSequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCardVerificationResult(self, request):
        """The interface supports obtaining the certificate authentication result based on the token.

        :param request: Request instance for GetCardVerificationResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetCardVerificationResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetCardVerificationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCardVerificationResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetCardVerificationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdResultIntl(self, request):
        """This API is used to get the verification result with the corresponding SDK token after the identity verification process is completed. The SDK token is valid for two hours (2*3,600s) after generation and can be called multiple times.

        :param request: Request instance for GetFaceIdResultIntl.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultIntlRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultIntlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceIdResultIntl", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceIdResultIntlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdTokenIntl(self, request):
        """This API is used to apply for an SDK token before calling the liveness detection and face comparison SDK each time. The SDK token is used throughout the identity verification process and to get the verification result after the verification is completed. A token is valid for one identity verification process only.

        :param request: Request instance for GetFaceIdTokenIntl.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenIntlRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenIntlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceIdTokenIntl", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceIdTokenIntlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.GetLivenessResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.GetSdkVerificationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.GetWebVerificationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWebVerificationResultIntl(self, request):
        """This API is used to get the verification result with the corresponding BizToken after the web-based verification is completed. The token is valid for three days (259,200s) after issuance and can be called multiple times.

        :param request: Request instance for GetWebVerificationResultIntl.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetWebVerificationResultIntlRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetWebVerificationResultIntlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWebVerificationResultIntl", params, headers=headers)
            response = json.loads(body)
            model = models.GetWebVerificationResultIntlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.LivenessCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.VideoLivenessCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))