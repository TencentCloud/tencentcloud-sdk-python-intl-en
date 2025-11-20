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

    async def ApplyCardVerification(
            self,
            request: models.ApplyCardVerificationRequest,
            opts: Dict = None,
    ) -> models.ApplyCardVerificationResponse:
        """
        The types of national cards supported by the API and whether instructions on the back of the card are required are as follows:
        <table> <thead> <tr> <td>Nationality</td> <td style="width:200px">CardType</td> <td style="width:200px">Back side required</td> </tr> </thead> <tbody> <tr> <td>Indonesia</td> <td>ID card</td> <td>No</td> </tr> <tr> <td>Indonesia</td> <td>Driving License</td> <td>No</td> </tr> <tr> <td>Hongkong</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Thailand</td> <td>ID card</td> <td>No</td> </tr> <tr> <td>Thailand</td> <td>Driving License</td> <td>Yes</td> </tr> <tr> <td>Malaysia</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Malaysia</td> <td>Driving License</td> <td>Yes</td> </tr> <tr> <td>Singapore</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Singapore</td> <td>Driving License</td> <td>Yes</td> </tr> <tr> <td>Philippine</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Philippine</td> <td>Driving License</td> <td>No</td> </tr> <tr> <td>Japan</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Japan</td> <td>Driving License</td> <td>No</td> </tr> <tr> <td>Taiwan</td> <td>ID Card</td> <td>Yes</td> </tr>  <tr> <td>Bangladesh</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Nigeria</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Nigeria</td> <td>Driving License</td> <td>Yes</td> </tr> <tr> <td>Pakistan</td> <td>ID card</td> <td>Yes</td> </tr> <tr> <td>Pakistan</td> <td>Driving License</td> <td>Yes</td> </tr> </tbody> </table>
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def ApplyWebVerificationToken(
            self,
            request: models.ApplyWebVerificationTokenRequest,
            opts: Dict = None,
    ) -> models.ApplyWebVerificationTokenResponse:
        """
        This API is used to apply for a token before calling the web-based verification service each time. This token is required for initiating the verification process and getting the result after the verification is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyWebVerificationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyWebVerificationTokenResponse
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
        
    async def GetCardVerificationResult(
            self,
            request: models.GetCardVerificationResultRequest,
            opts: Dict = None,
    ) -> models.GetCardVerificationResultResponse:
        """
        The interface supports obtaining the certificate authentication result based on the token.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCardVerificationResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCardVerificationResultResponse
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
        
    async def GetWebVerificationResult(
            self,
            request: models.GetWebVerificationResultRequest,
            opts: Dict = None,
    ) -> models.GetWebVerificationResultResponse:
        """
        This API is used to get the verification result with the corresponding token (BizToken) after the web-based verification is completed. The BizToken is valid for three days (3*24*3,600s) after issuance and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWebVerificationResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWebVerificationResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWebVerificationResultIntl(
            self,
            request: models.GetWebVerificationResultIntlRequest,
            opts: Dict = None,
    ) -> models.GetWebVerificationResultIntlResponse:
        """
        This API is used to get the verification result with the corresponding BizToken after the web-based verification is completed. The token is valid for three days (259,200s) after issuance and can be called multiple times.
        """
        
        kwargs = {}
        kwargs["action"] = "GetWebVerificationResultIntl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWebVerificationResultIntlResponse
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