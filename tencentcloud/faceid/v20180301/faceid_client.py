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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.intl.tencentcloudapi.com'
    _service = 'faceid'


    def ApplyLivenessToken(self, request):
        r"""This API is used to apply for a token before calling the liveness detection service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

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
        r"""This API is used to apply for a token before calling the eKYC SDK service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

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
        r"""This API is used to obtain a BizToken before each call to the Web verification service. Save the BizToken to initiate the verification process and retrieve the result upon completion. The BizToken is valid for 10 minutes.

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


    def BankCard2EVerification(self, request):
        r"""This API is used to validate the authenticity and consistency of the name and bank card number.

        :param request: Request instance for BankCard2EVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCard2EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCard2EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BankCard4EVerification(self, request):
        r"""This API is used to verify the authenticity and consistency of the bank card number, name, ID number, and mobile number for account opening.

        :param request: Request instance for BankCard4EVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCard4EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCard4EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BankCardVerification(self, request):
        r"""This API is used to verify the authenticity and consistency of the bank card number, name, and ID number of information.

        :param request: Request instance for BankCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBankCardInformation(self, request):
        r"""Bank card basic information query

        :param request: Request instance for CheckBankCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCardInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCardInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIdCardInformation(self, request):
        r"""This API is used to import the ID card portrait side photo, recognize the information on the ID card photo, and compare the name, identity card number, and ID card portrait photo with the ID photo in the authoritative database to verify if they belong to the same person, thereby verifying the authenticity of the identity card information.

        :param request: Request instance for CheckIdCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIdCardInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIdCardInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIdNameDate(self, request):
        r"""This API is used to validate the authenticity and consistency of the name, identity card number, and valid period.

        :param request: Request instance for CheckIdNameDate.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckIdNameDateRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckIdNameDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIdNameDate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIdNameDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareFaceLiveness(self, request):
        r"""This interface supports judgment of real person and photo comparison to verify the user's identity online. By passing the video and photo into the interface, it will first judge whether the person in the video is real. If yes, it judges whether the person in the video is the same one as the uploaded photo and returns authentication result.

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


    def CreateEKYCWebhook(self, request):
        r"""This API is used to create an EKYC Webhook configuration.

        :param request: Request instance for CreateEKYCWebhook.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CreateEKYCWebhookRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CreateEKYCWebhookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEKYCWebhook", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEKYCWebhookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUploadUrl(self, request):
        r"""This API is used to generate a temporary `UploadUrl` for uploading resource files (with the `HTTP PUT` method). After resource upload, `ResourceUrl` will be passed to the `TargetAction` API to complete the resource passing (specific fields vary by case).
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


    def DeleteEKYCWebhook(self, request):
        r"""This API deletes the Webhook configuration.

        :param request: Request instance for DeleteEKYCWebhook.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DeleteEKYCWebhookRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DeleteEKYCWebhookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEKYCWebhook", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEKYCWebhookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectAIFakeFaces(self, request):
        r"""Based on the multimodal AI large model algorithm, it provides anti-attack detection capabilities for facial images and videos. It can effectively identify highly simulated AIGC face-changing, high-definition remakes, batch black market attacks, watermarks and other attack traces, and enhance the anti-counterfeiting security capabilities of images and videos.

        :param request: Request instance for DetectAIFakeFaces.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAIFakeFacesRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAIFakeFacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectAIFakeFaces", params, headers=headers)
            response = json.loads(body)
            model = models.DetectAIFakeFacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectReflectLivenessAndCompare(self, request):
        r"""This API is used to detect liveness with the package generated by the liveness comparison (reflection-based) SDK, and to compare the person detected with that in the image passed in.
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
        r"""This API is used to generate an appropriate light sequence based on the information collected by the liveness comparison (reflection-based) SDK and pass the light sequence into the SDK to start the eKYC process.
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


    def GetAMLScreeningResult(self, request):
        r"""Queries the AML name list screening result.

        :param request: Request instance for GetAMLScreeningResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetAMLScreeningResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetAMLScreeningResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAMLScreeningResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetAMLScreeningResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdResultIntl(self, request):
        r"""This API is used to get the verification result with the corresponding SDK token after the identity verification process is completed. The SDK token is valid for 72 hours (72*3600s) after generation and can be called multiple times.

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
        r"""This API is used to apply for an SDK token before calling the selfie verification SDK each time. The SDK token is used throughout the eKYC process and to get the verification result after the verification is completed. A token is valid for one eKYC process only.

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
        r"""This API is used to get the verification result with the corresponding token (SdkToken) after the liveness detection is completed. The token is valid for two hours after issuance and can be called multiple times.

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


    def GetNFCResult(self, request):
        r"""This API verifies NFC data. Pass in the NFCToken returned by the SDK, along with the document fields and portrait photo to be verified.The service automatically compares the information to verify with the decrypted document NFC data and outputs the verification result. The NFCToken generated by the SDK is valid for 10 minutes. The service is billed per query.
        The service currently supports NFC recognition and verification of the following fields and portrait photos on Chinese mainland second-generation resident identity cards, exit-entry permits for traveling to and from Hong Kong and Macao, and international passports with an NFC chip:

        -Chinese mainland second-generation resident identity card: identity card number, name, sex, ethnicity, date of birth, address, issuing authority, validity start time, validity end time, portrait photo
        -Exit-Entry Permit for Traveling to and from Hong Kong and Macao: ID number, name, sex, English name, issuing place, issuing authority, validity end time, date of birth, portrait photo, machine-readable code
        -International passports with an NFC chip: passport number, name, nationality, sex, country or region code, validity start time, validity end time, date of birth, birth place, issuing place, issuing authority, portrait photo, machine-readable code

        :param request: Request instance for GetNFCResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetNFCResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetNFCResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetNFCResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetNFCResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetNFCToken(self, request):
        r"""NFC verification service: obtain Token information (valid for 10 minutes) for the NFC identify request. This API supports NFC recognition and verification of the following documents:

        -Chinese mainland second-generation resident identity card
        -Exit-Entry Permit for Traveling to and from Hong Kong and Macao
        -International passports with an NFC chip

        :param request: Request instance for GetNFCToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetNFCTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetNFCTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetNFCToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetNFCTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSdkVerificationResult(self, request):
        r"""This API is used to get the verification result with the corresponding token after the SDK-based verification is completed. The token is valid for three days after issuance and can be called multiple times.

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


    def GetWebVerificationResultIntl(self, request):
        r"""After completing the Web verification process, call this API with the verification token (BizToken) to query the verification result info. The BizToken is valid within three days (259,200 seconds) after application and can be called multiple times.

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


    def IdCardOCRVerification(self, request):
        r"""This API is used to validate the authenticity and consistency of the name and identity card number. You can provide the required verification information by manually inputting the name and identity card number or importing the ID card portrait side image.

        :param request: Request instance for IdCardOCRVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdCardOCRVerification", params, headers=headers)
            response = json.loads(body)
            model = models.IdCardOCRVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdCardVerification(self, request):
        r"""This API is used to validate the authenticity and consistency of the name and identity card number.

        :param request: Request instance for IdCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.IdCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageRecognitionV2(self, request):
        r"""This API is used to judge whether the image passed in and the ID photo in the authoritative database belong to the same person based on the identity information.

        :param request: Request instance for ImageRecognitionV2.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionV2Request`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageRecognitionV2", params, headers=headers)
            response = json.loads(body)
            model = models.ImageRecognitionV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEKYCWebhooks(self, request):
        r"""This API queries the list of Webhook configurations.

        :param request: Request instance for ListEKYCWebhooks.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ListEKYCWebhooksRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ListEKYCWebhooksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEKYCWebhooks", params, headers=headers)
            response = json.loads(body)
            model = models.ListEKYCWebhooksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LivenessCompare(self, request):
        r"""This API is used to pass in a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.
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


    def MobileNetworkTimeVerification(self, request):
        r"""This API is used to query the duration of a mobile number. Enter mobile number to query.

        :param request: Request instance for MobileNetworkTimeVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MobileNetworkTimeVerification", params, headers=headers)
            response = json.loads(body)
            model = models.MobileNetworkTimeVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MobileStatus(self, request):
        r"""This API is used to verify phone number status. You can enter mobile number to query.

        :param request: Request instance for MobileStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MobileStatus", params, headers=headers)
            response = json.loads(body)
            model = models.MobileStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PhoneVerification(self, request):
        r"""This API is used to validate the authenticity and consistency of the mobile number, name, and identity card number. For details on supported mobile number segments, see the <a href="https://www.tencentcloud.com/document/product/1061/79689">carrier</a> document.

        :param request: Request instance for PhoneVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PhoneVerification", params, headers=headers)
            response = json.loads(body)
            model = models.PhoneVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunAMLNameScreening(self, request):
        r"""AML name list screening

        :param request: Request instance for RunAMLNameScreening.
        :type request: :class:`tencentcloud.faceid.v20180301.models.RunAMLNameScreeningRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.RunAMLNameScreeningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunAMLNameScreening", params, headers=headers)
            response = json.loads(body)
            model = models.RunAMLNameScreeningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAMLCustomerProfile(self, request):
        r"""AML name list screening

        :param request: Request instance for UpdateAMLCustomerProfile.
        :type request: :class:`tencentcloud.faceid.v20180301.models.UpdateAMLCustomerProfileRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.UpdateAMLCustomerProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAMLCustomerProfile", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAMLCustomerProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAMLOngoingScreeningStatus(self, request):
        r"""Continuous name list screening status change

        :param request: Request instance for UpdateAMLOngoingScreeningStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.UpdateAMLOngoingScreeningStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.UpdateAMLOngoingScreeningStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAMLOngoingScreeningStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAMLOngoingScreeningStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEKYCWebhook(self, request):
        r"""This API is used to update Webhook configurations.

        :param request: Request instance for UpdateEKYCWebhook.
        :type request: :class:`tencentcloud.faceid.v20180301.models.UpdateEKYCWebhookRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.UpdateEKYCWebhookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEKYCWebhook", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEKYCWebhookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VideoLivenessCompare(self, request):
        r"""This API is used to pass in URLs of a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.

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