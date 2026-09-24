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
from tencentcloud.faceid.v20180301 import models
from typing import Dict


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.intl.tencentcloudapi.com'
    _service = 'faceid'

    async def ApplyLivenessToken(
            self,
            request: models.ApplyLivenessTokenRequest,
            opts: Dict = None,
    ) -> models.ApplyLivenessTokenResponse:
        """
        This API is used to apply for a token before calling the liveness detection service each time. This token is required for initiating the verification process and getting the result after the verification is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyLivenessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyLivenessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplySdkVerificationToken(
            self,
            request: models.ApplySdkVerificationTokenRequest,
            opts: Dict = None,
    ) -> models.ApplySdkVerificationTokenResponse:
        """
        This API is used to apply for a token before calling the eKYC SDK service each time. This token is required for initiating the verification process and getting the result after the verification is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplySdkVerificationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplySdkVerificationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyWebVerificationBizTokenIntl(
            self,
            request: models.ApplyWebVerificationBizTokenIntlRequest,
            opts: Dict = None,
    ) -> models.ApplyWebVerificationBizTokenIntlResponse:
        """
        This API is used to obtain a BizToken before each call to the Web verification service. Save the BizToken to initiate the verification process and retrieve the result upon completion. The BizToken is valid for 10 minutes.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyWebVerificationBizTokenIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyWebVerificationBizTokenIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCard2EVerification(
            self,
            request: models.BankCard2EVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCard2EVerificationResponse:
        """
        This API is used to validate the authenticity and consistency of the name and bank card number.
        """
        
        kwargs = {}
        kwargs["action"] = "BankCard2EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCard2EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCard4EVerification(
            self,
            request: models.BankCard4EVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCard4EVerificationResponse:
        """
        This API is used to verify the authenticity and consistency of the bank card number, name, ID number, and mobile number for account opening.
        """
        
        kwargs = {}
        kwargs["action"] = "BankCard4EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCard4EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCardVerification(
            self,
            request: models.BankCardVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCardVerificationResponse:
        """
        This API is used to verify the authenticity and consistency of the bank card number, name, and ID number of information.
        """
        
        kwargs = {}
        kwargs["action"] = "BankCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCardInformation(
            self,
            request: models.CheckBankCardInformationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCardInformationResponse:
        """
        Bank card basic information query
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCardInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCardInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIdCardInformation(
            self,
            request: models.CheckIdCardInformationRequest,
            opts: Dict = None,
    ) -> models.CheckIdCardInformationResponse:
        """
        This API is used to import the ID card portrait side photo, recognize the information on the ID card photo, and compare the name, identity card number, and ID card portrait photo with the ID photo in the authoritative database to verify if they belong to the same person, thereby verifying the authenticity of the identity card information.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIdCardInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIdCardInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIdNameDate(
            self,
            request: models.CheckIdNameDateRequest,
            opts: Dict = None,
    ) -> models.CheckIdNameDateResponse:
        """
        This API is used to validate the authenticity and consistency of the name, identity card number, and valid period.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIdNameDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIdNameDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareFaceLiveness(
            self,
            request: models.CompareFaceLivenessRequest,
            opts: Dict = None,
    ) -> models.CompareFaceLivenessResponse:
        """
        This interface supports judgment of real person and photo comparison to verify the user's identity online. By passing the video and photo into the interface, it will first judge whether the person in the video is real. If yes, it judges whether the person in the video is the same one as the uploaded photo and returns authentication result.
        """
        
        kwargs = {}
        kwargs["action"] = "CompareFaceLiveness"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareFaceLivenessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEKYCWebhook(
            self,
            request: models.CreateEKYCWebhookRequest,
            opts: Dict = None,
    ) -> models.CreateEKYCWebhookResponse:
        """
        This API is used to create an EKYC Webhook configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEKYCWebhook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEKYCWebhookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUploadUrl(
            self,
            request: models.CreateUploadUrlRequest,
            opts: Dict = None,
    ) -> models.CreateUploadUrlResponse:
        """
        This API is used to generate a temporary `UploadUrl` for uploading resource files (with the `HTTP PUT` method). After resource upload, `ResourceUrl` will be passed to the `TargetAction` API to complete the resource passing (specific fields vary by case).
        The data will be stored in a COS bucket in the region specified by the parameter `Region` for two hours.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUploadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUploadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEKYCWebhook(
            self,
            request: models.DeleteEKYCWebhookRequest,
            opts: Dict = None,
    ) -> models.DeleteEKYCWebhookResponse:
        """
        This API deletes the Webhook configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEKYCWebhook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEKYCWebhookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectAIFakeFaces(
            self,
            request: models.DetectAIFakeFacesRequest,
            opts: Dict = None,
    ) -> models.DetectAIFakeFacesResponse:
        """
        Based on the multimodal AI large model algorithm, it provides anti-attack detection capabilities for facial images and videos. It can effectively identify highly simulated AIGC face-changing, high-definition remakes, batch black market attacks, watermarks and other attack traces, and enhance the anti-counterfeiting security capabilities of images and videos.
        """
        
        kwargs = {}
        kwargs["action"] = "DetectAIFakeFaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectAIFakeFacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectReflectLivenessAndCompare(
            self,
            request: models.DetectReflectLivenessAndCompareRequest,
            opts: Dict = None,
    ) -> models.DetectReflectLivenessAndCompareResponse:
        """
        This API is used to detect liveness with the package generated by the liveness comparison (reflection-based) SDK, and to compare the person detected with that in the image passed in.
        The image and the data generated with the SDK must be stored in COS, and the region of the COS bucket must be same as that of requests made with this API. We recommend that you pass resources with upload link APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DetectReflectLivenessAndCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectReflectLivenessAndCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateReflectSequence(
            self,
            request: models.GenerateReflectSequenceRequest,
            opts: Dict = None,
    ) -> models.GenerateReflectSequenceResponse:
        """
        This API is used to generate an appropriate light sequence based on the information collected by the liveness comparison (reflection-based) SDK and pass the light sequence into the SDK to start the eKYC process.
        The data generated with the SDK must be stored in COS, and the region of the COS bucket must be same as that of requests made with this API. We recommend that you pass resources with upload link APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateReflectSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateReflectSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAMLScreeningResult(
            self,
            request: models.GetAMLScreeningResultRequest,
            opts: Dict = None,
    ) -> models.GetAMLScreeningResultResponse:
        """
        Status change of continuous name list screening
        """
        
        kwargs = {}
        kwargs["action"] = "GetAMLScreeningResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAMLScreeningResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceIdResultIntl(
            self,
            request: models.GetFaceIdResultIntlRequest,
            opts: Dict = None,
    ) -> models.GetFaceIdResultIntlResponse:
        """
        This API is used to get the verification result with the corresponding SDK token after the identity verification process is completed. The SDK token is valid for 72 hours (72*3600s) after generation and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceIdResultIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceIdResultIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceIdTokenIntl(
            self,
            request: models.GetFaceIdTokenIntlRequest,
            opts: Dict = None,
    ) -> models.GetFaceIdTokenIntlResponse:
        """
        This API is used to apply for an SDK token before calling the selfie verification SDK each time. The SDK token is used throughout the eKYC process and to get the verification result after the verification is completed. A token is valid for one eKYC process only.
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceIdTokenIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceIdTokenIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLivenessResult(
            self,
            request: models.GetLivenessResultRequest,
            opts: Dict = None,
    ) -> models.GetLivenessResultResponse:
        """
        This API is used to get the verification result with the corresponding token (SdkToken) after the liveness detection is completed. The token is valid for two hours after issuance and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetLivenessResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLivenessResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetNFCResult(
            self,
            request: models.GetNFCResultRequest,
            opts: Dict = None,
    ) -> models.GetNFCResultResponse:
        """
        This API verifies NFC data. Pass in the NFCToken returned by the SDK, along with the document fields and portrait photo to be verified.The service automatically compares the information to verify with the decrypted document NFC data and outputs the verification result. The NFCToken generated by the SDK is valid for 10 minutes. The service is billed per query.
        The service currently supports NFC recognition and verification of the following fields and portrait photos on Chinese mainland second-generation resident identity cards, exit-entry permits for traveling to and from Hong Kong and Macao, and international passports with an NFC chip:

        -Chinese mainland second-generation resident identity card: identity card number, name, sex, ethnicity, date of birth, address, issuing authority, validity start time, validity end time, portrait photo
        -Exit-Entry Permit for Traveling to and from Hong Kong and Macao: ID number, name, sex, English name, issuing place, issuing authority, validity end time, date of birth, portrait photo, machine-readable code
        -International passports with an NFC chip: passport number, name, nationality, sex, country or region code, validity start time, validity end time, date of birth, birth place, issuing place, issuing authority, portrait photo, machine-readable code
        """
        
        kwargs = {}
        kwargs["action"] = "GetNFCResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetNFCResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetNFCToken(
            self,
            request: models.GetNFCTokenRequest,
            opts: Dict = None,
    ) -> models.GetNFCTokenResponse:
        """
        NFC verification service: obtain Token information (valid for 10 minutes) for the NFC identify request. This API supports NFC recognition and verification of the following documents:

        -Chinese mainland second-generation resident identity card
        -Exit-Entry Permit for Traveling to and from Hong Kong and Macao
        -International passports with an NFC chip
        """
        
        kwargs = {}
        kwargs["action"] = "GetNFCToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetNFCTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSdkVerificationResult(
            self,
            request: models.GetSdkVerificationResultRequest,
            opts: Dict = None,
    ) -> models.GetSdkVerificationResultResponse:
        """
        This API is used to get the verification result with the corresponding token after the SDK-based verification is completed. The token is valid for three days after issuance and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSdkVerificationResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSdkVerificationResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWebVerificationResultIntl(
            self,
            request: models.GetWebVerificationResultIntlRequest,
            opts: Dict = None,
    ) -> models.GetWebVerificationResultIntlResponse:
        """
        After completing the Web verification process, call this API with the verification token (BizToken) to query the verification result info. The BizToken is valid within three days (259,200 seconds) after application and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWebVerificationResultIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWebVerificationResultIntlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdCardOCRVerification(
            self,
            request: models.IdCardOCRVerificationRequest,
            opts: Dict = None,
    ) -> models.IdCardOCRVerificationResponse:
        """
        This API is used to validate the authenticity and consistency of the name and identity card number. You can provide the required verification information by manually inputting the name and identity card number or importing the ID card portrait side image.
        """
        
        kwargs = {}
        kwargs["action"] = "IdCardOCRVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdCardOCRVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdCardVerification(
            self,
            request: models.IdCardVerificationRequest,
            opts: Dict = None,
    ) -> models.IdCardVerificationResponse:
        """
        This API is used to validate the authenticity and consistency of the name and identity card number.
        """
        
        kwargs = {}
        kwargs["action"] = "IdCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageRecognitionV2(
            self,
            request: models.ImageRecognitionV2Request,
            opts: Dict = None,
    ) -> models.ImageRecognitionV2Response:
        """
        This API is used to judge whether the image passed in and the ID photo in the authoritative database belong to the same person based on the identity information.
        """
        
        kwargs = {}
        kwargs["action"] = "ImageRecognitionV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageRecognitionV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEKYCWebhooks(
            self,
            request: models.ListEKYCWebhooksRequest,
            opts: Dict = None,
    ) -> models.ListEKYCWebhooksResponse:
        """
        This API queries the list of Webhook configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEKYCWebhooks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEKYCWebhooksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LivenessCompare(
            self,
            request: models.LivenessCompareRequest,
            opts: Dict = None,
    ) -> models.LivenessCompareResponse:
        """
        This API is used to pass in a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.
        This API on the legacy version will continue to serve existing users but will be unavailable to new users. We recommend you use `VideoLivenessCompare` for better service quality.
        """
        
        kwargs = {}
        kwargs["action"] = "LivenessCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LivenessCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MobileNetworkTimeVerification(
            self,
            request: models.MobileNetworkTimeVerificationRequest,
            opts: Dict = None,
    ) -> models.MobileNetworkTimeVerificationResponse:
        """
        This API is used to query the duration of a mobile number. Enter mobile number to query.
        """
        
        kwargs = {}
        kwargs["action"] = "MobileNetworkTimeVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MobileNetworkTimeVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MobileStatus(
            self,
            request: models.MobileStatusRequest,
            opts: Dict = None,
    ) -> models.MobileStatusResponse:
        """
        This API is used to verify phone number status. You can enter mobile number to query.
        """
        
        kwargs = {}
        kwargs["action"] = "MobileStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MobileStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PhoneVerification(
            self,
            request: models.PhoneVerificationRequest,
            opts: Dict = None,
    ) -> models.PhoneVerificationResponse:
        """
        This API is used to validate the authenticity and consistency of the mobile number, name, and identity card number. For details on supported mobile number segments, see the <a href="https://www.tencentcloud.com/document/product/1061/79689">carrier</a> document.
        """
        
        kwargs = {}
        kwargs["action"] = "PhoneVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PhoneVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunAMLNameScreening(
            self,
            request: models.RunAMLNameScreeningRequest,
            opts: Dict = None,
    ) -> models.RunAMLNameScreeningResponse:
        """
        AML list screening
        """
        
        kwargs = {}
        kwargs["action"] = "RunAMLNameScreening"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunAMLNameScreeningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAMLCustomerProfile(
            self,
            request: models.UpdateAMLCustomerProfileRequest,
            opts: Dict = None,
    ) -> models.UpdateAMLCustomerProfileResponse:
        """
        AML list screening
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAMLCustomerProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAMLCustomerProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAMLOngoingScreeningStatus(
            self,
            request: models.UpdateAMLOngoingScreeningStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAMLOngoingScreeningStatusResponse:
        """
        Continuous name list screening status change
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAMLOngoingScreeningStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAMLOngoingScreeningStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEKYCWebhook(
            self,
            request: models.UpdateEKYCWebhookRequest,
            opts: Dict = None,
    ) -> models.UpdateEKYCWebhookResponse:
        """
        This API is used to update Webhook configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEKYCWebhook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEKYCWebhookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VideoLivenessCompare(
            self,
            request: models.VideoLivenessCompareRequest,
            opts: Dict = None,
    ) -> models.VideoLivenessCompareResponse:
        """
        This API is used to pass in URLs of a video and a photo, determine whether the person in the video is real, and if yes, then determine whether the person in the video is the same as that in the photo.
        """
        
        kwargs = {}
        kwargs["action"] = "VideoLivenessCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VideoLivenessCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)