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
from tencentcloud.ocr.v20181119 import models


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.intl.tencentcloudapi.com'
    _service = 'ocr'


    def ApplyCardVerificationExternal(self, request):
        r"""This API provides general OCR recognition for overseas identity documents.

        The following table lists the supported countries or regions, document types, and whether the back side is required:

        <table>
        <thead>
        <tr>
        <td style="width:200px">Nationality</td>
        <td style="width:200px">CardType</td>
        <td style="width:200px">Whether the Back Side is Required</td>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>Argentina</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Argentina</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Argentina</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Australia</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Australia</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Australia</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Australia</td>
        <td>Residence Permit</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Bangladesh</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Bangladesh</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Bangladesh</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Cambodia</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Cambodia</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Cambodia</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Canada</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Canada</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Canada</td>
        <td>Passport</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Canada</td>
        <td>Residence Permit</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Chile</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Chile</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Chile</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Germany</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Germany</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Germany</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Germany</td>
        <td>Residence Permit</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Mexico</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Mexico</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Mexico</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Myanmar</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Myanmar</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Myanmar</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>New Zealand</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>New Zealand</td>
        <td>National ID Card</td>
        <td>No</td>
        </tr>
        <tr>
        <td>New Zealand</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>New Zealand</td>
        <td>Residence Permit</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>Residence Permit</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Pakistan</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Pakistan</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Pakistan</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Russia</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Russia</td>
        <td>National ID Card</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Russia</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>Passport</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>Residence Permit</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Indonesia</td>
        <td>National ID Card</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Indonesia</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Hong Kong, China</td>
        <td>Identity Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Thailand</td>
        <td>National ID Card</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Thailand</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Malaysia</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Malaysia</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Singapore</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Philippines</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Philippines</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Japan</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Japan</td>
        <td>Driver's License</td>
        <td>No</td>
        </tr>
        <tr>
        <td>Macau, China</td>
        <td>Identity Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Taiwan, China</td>
        <td>Identity Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Bangladesh</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Nigeria</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Pakistan</td>
        <td>National ID Card</td>
        <td>Yes</td>
        </tr>
        <tr>
        <td>Pakistan</td>
        <td>Driver's License</td>
        <td>Yes</td>
        </tr>
        </tbody>
        </table>

        :param request: Request instance for ApplyCardVerificationExternal.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ApplyCardVerificationExternalRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ApplyCardVerificationExternalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyCardVerificationExternal", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyCardVerificationExternalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExtractDocMulti(self, request):
        r"""This API supports identifying and extracting field information in structured scenarios such as complex scenarios and multiple formats. Key scenarios include: finance, health care, transportation, travel, insurance. Click [experience now](https://ocrdemo.cloud.tencent.com/).

        This API is used to set the alias SmartStructuralPro.

        The default API request rate limit is 5 requests per second.

        :param request: Request instance for ExtractDocMulti.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ExtractDocMultiRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ExtractDocMultiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractDocMulti", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractDocMultiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GeneralAccurateOCR(self, request):
        r"""This API is used to detect and recognize characters in an image. It can recognize Chinese, English, Chinese-English, digits, and special symbols and return the text box positions and characters.

        It is suitable for scenarios with a lot of characters in complex layouts and requiring high recognition accuracy, such as examination papers, online images, signboards, and legal documents.

        Strengths: compared with general print recognition, it provides higher-precision character recognition services. Its accuracy and recall rate are higher in difficult scenarios such as a large number of characters, long strings of digits, small characters, blurry characters, and tilted text.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for GeneralAccurateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GeneralAccurateOCR", params, headers=headers)
            response = json.loads(body)
            model = models.GeneralAccurateOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GeneralBasicOCR(self, request):
        r"""This API is used to detect and recognize characters in an image in the following 20 languages: Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, Thai, and Arabic. Mixed characters in English and each supported language can be recognized together.

        It can recognize printed text in paper documents, online images, ads, signboards, menus, video titles, profile photos, etc.

        Strengths: it can automatically recognize the text language, return the text box coordinate information, and automatically rotate tilted text to the upright direction.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for GeneralBasicOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GeneralBasicOCR", params, headers=headers)
            response = json.loads(body)
            model = models.GeneralBasicOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCardVerificationExternalResult(self, request):
        r"""This API is used to obtain document recognition results.

        :param request: Request instance for GetCardVerificationExternalResult.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GetCardVerificationExternalResultRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GetCardVerificationExternalResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCardVerificationExternalResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetCardVerificationExternalResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HKIDCardOCR(self, request):
        r"""This API is used to recognize key fields on the photo side of a Hong Kong (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for HKIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.HKIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.HKIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HKIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.HKIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MLIDCardOCR(self, request):
        r"""This API is used to recognize a Malaysian identity card, including identity card number, name, gender, and address. It is also used to crop identity photos and give alarms for photographed or photocopied certificates.

        This API is not fully available for the time being. For more information, contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for MLIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MLIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.MLIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MLIDPassportOCR(self, request):
        r"""This API is used to recognize a passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country/region, and nationality. It has the features of cropping identity photos and alarming for photographed or photocopied documents.
        This interface supports regional scope: countries with machine-readable passports

        :param request: Request instance for MLIDPassportOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MLIDPassportOCR", params, headers=headers)
            response = json.loads(body)
            model = models.MLIDPassportOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MainlandPermitOCR(self, request):
        r"""This API is used to recognize all fields on the front of a mainland travel permit for Hong Kong, Macao, or Taiwan residents: name in Chinese, name in English, gender, date of birth, issuing authority, validity period, document number, place of issuance, number of issues, and document type.

        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for MainlandPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MainlandPermitOCR", params, headers=headers)
            response = json.loads(body)
            model = models.MainlandPermitOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PODAuditAI(self, request):
        r"""The POD intelligent review deeply integrates multimodal large model image understanding technology, targeting the logistics last-mile delivery scenario to provide high-precision POD compliance audit service. The system auto-recognizes ticket imperfections and risks of non-compliance, helping businesses achieve standardized control in the delivery process and effectively avoid customer complaints and disputes caused by non-compliant credentials.

        :param request: Request instance for PODAuditAI.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PODAuditAIRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PODAuditAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PODAuditAI", params, headers=headers)
            response = json.loads(body)
            model = models.PODAuditAIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PermitOCR(self, request):
        r"""This API is used to recognize the fields on an exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan, including place of issuance, issuing authority, validity period, gender, date of birth, name in English, name in Chinese, and document number.

        A maximum of 10 requests can be initiated per second for this API.

        :param request: Request instance for PermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PermitOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PermitOCR", params, headers=headers)
            response = json.loads(body)
            model = models.PermitOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeBrazilCommonOCR(self, request):
        r"""This API is used to identify Brazil common documents.

        This API is used to set the default request rate limit to 5 requests/second.

        :param request: Request instance for RecognizeBrazilCommonOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilCommonOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilCommonOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeBrazilCommonOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeBrazilCommonOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeBrazilDriverLicenseOCR(self, request):
        r"""This interface supports identification of the front and back of Brazilian driver's license. The identification fields include name, driver's license category, number, validity period, etc.

        :param request: Request instance for RecognizeBrazilDriverLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilDriverLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilDriverLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeBrazilDriverLicenseOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeBrazilDriverLicenseOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeBrazilIDCardOCR(self, request):
        r"""This interface supports identification of the front and back of Brazilian ID license. The identification fields include name, driver's license category, number, validity period, etc.

        :param request: Request instance for RecognizeBrazilIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeBrazilIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeBrazilIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeBrazilRNEOCR(self, request):
        r"""Brazil RNE document recognition Default interface request frequency limit: 5 times/second

        :param request: Request instance for RecognizeBrazilRNEOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilRNEOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilRNEOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeBrazilRNEOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeBrazilRNEOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeBrazilRNMOCR(self, request):
        r"""This interface supports identification of the front and back of Brazilian RNM license. The default interface request frequency limit is 5 times per second.

        :param request: Request instance for RecognizeBrazilRNMOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilRNMOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeBrazilRNMOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeBrazilRNMOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeBrazilRNMOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeDetectCardCoords(self, request):
        r"""This API is used to recognize the coordinates of four corners of cards.

        :param request: Request instance for RecognizeDetectCardCoords.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeDetectCardCoordsRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeDetectCardCoordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeDetectCardCoords", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeDetectCardCoordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeIndonesiaIDCardOCR(self, request):
        r"""Indonesian identity card recognition

        Default API request rate limit: 5 requests/second.

        :param request: Request instance for RecognizeIndonesiaIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeIndonesiaIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeIndonesiaIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeIndonesiaIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeIndonesiaIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeMacaoIDCardOCR(self, request):
        r"""This API is used to recognize key fields on the photo side of a Macao (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for RecognizeMacaoIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeMacaoIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeMacaoIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeMacaoIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeMacaoIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeMainlandIDCardOCR(self, request):
        r"""This interface recognizes all fields on both sides of the Mainland China Resident Identity Card (second-generation), including name, gender, ethnicity, date of birth, address, ID number, issuing authority, and validity period, with an accuracy of over 99%.

        In addition, the interface provides additional features for various scenarios, such as ID card and portrait photo cropping, along with five alarm detections (see table below).<table style="width:650px"> <thead> <tr> <th width="150">Value-added ability</th> <th width="500">Ability items</th> </tr> </thead> <tbody> <tr> <td rowspan="9">Alarm function</td> </tr> <tr> <td>ID card photocopy warning</td> </tr> <tr> <td>ID card on-screen display warning</td> </tr> <tr> <td>Alarm for occlusion in the ID card frame</td> </tr> <tr> <td>ID card reflective warning</td> </tr> <tr> <td>Blurry picture warning</td> </tr> </tbody> </table> Default rate limit: 20 requests/second.

        :param request: Request instance for RecognizeMainlandIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeMainlandIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeMainlandIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeMainlandIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeMainlandIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeMexicoVTID(self, request):
        r"""This interface supports identification of the front and back of Mexican Voter ID Card. The default interface request frequency limit is 5 times per second.

        :param request: Request instance for RecognizeMexicoVTID.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeMexicoVTIDRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeMexicoVTIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeMexicoVTID", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeMexicoVTIDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizePhilippinesDrivingLicenseOCR(self, request):
        r"""This API is used to recognize a Philippine driver's license.

        :param request: Request instance for RecognizePhilippinesDrivingLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesDrivingLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesDrivingLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePhilippinesDrivingLicenseOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePhilippinesDrivingLicenseOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizePhilippinesSssIDOCR(self, request):
        r"""This API is used to recognize a Philippine SSSID/UMID card.

        :param request: Request instance for RecognizePhilippinesSssIDOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesSssIDOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesSssIDOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePhilippinesSssIDOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePhilippinesSssIDOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizePhilippinesTinIDOCR(self, request):
        r"""This API is used to recognize a Philippine TIN ID card.

        :param request: Request instance for RecognizePhilippinesTinIDOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesTinIDOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesTinIDOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePhilippinesTinIDOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePhilippinesTinIDOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizePhilippinesUMIDOCR(self, request):
        r"""This API is used to recognize a Philippine Unified Multi-Purpose ID (UMID) card.

        :param request: Request instance for RecognizePhilippinesUMIDOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesUMIDOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesUMIDOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePhilippinesUMIDOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePhilippinesUMIDOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizePhilippinesVoteIDOCR(self, request):
        r"""This API is used to recognize a Philippine voters ID card. It can recognize fields such as first name, family name, date of birth, civil status, citizenship, address, precinct, and voter's identification number (VIN).

        The API request rate is limited to 20 requests/sec by default.

        :param request: Request instance for RecognizePhilippinesVoteIDOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesVoteIDOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizePhilippinesVoteIDOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePhilippinesVoteIDOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePhilippinesVoteIDOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeSingaporeIDCardOCR(self, request):
        r"""This interface supports the identification of all fields on the front side of ID card for Singapore residents.The identification accuracy reaches more than 99%.In addition, this interface also supports a variety of value-added capabilities to meet the needs of different scenarios. Such as the cropping function of ID card photos and portrait photos, and also has 5 alarm functions.
        As shown in the table below. <table style="width:650px"> <thead> <tr> <th width="150">Value-added ability</th> <th width="500">Ability items</th> </tr> </thead> <tbody> <tr> <td rowspan="9">Alarm function</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>Alarm for occlusion in the ID card frame</td> </tr> <tr> <td>ID card reflective warning</td> </tr> <tr> <td>Blurry picture warning</td> </tr> </tbody> </table> Default interface request frequency limit: 20 times/second

        :param request: Request instance for RecognizeSingaporeIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeSingaporeIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeSingaporeIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeSingaporeIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeSingaporeIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeThaiIDCardOCR(self, request):
        r"""This API is used to recognize the fields on a Thai identity card, including name in Thai, name in English, address, date of birth, identification number, date of issue, and date of expiry.

        A maximum of 10 requests can be initiated per second for this API.

        :param request: Request instance for RecognizeThaiIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeThaiIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeThaiIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeThaiIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeThaiIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeThaiPinkCard(self, request):
        r"""This API is used to recognize the fields on a Thai identity card, including name in Thai, name in English, address, date of birth, identification number, date of issue, and date of expiry.
        Currently, this API is not generally available. For more information, please [contact your sales rep](https://intl.cloud.tencent.com/zh/contact-us).

        A maximum of 5 requests can be initiated per second for this API.

        :param request: Request instance for RecognizeThaiPinkCard.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeThaiPinkCardRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeThaiPinkCardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeThaiPinkCard", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeThaiPinkCardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SmartStructuralOCRV2(self, request):
        r"""This API is used to recognize fields from cards, documents, bills, forms, contracts, and other structured information. It is flexible and efficient to use, without any configuration required. This API is suitable for recognizing structured information.

        A maximum of 10 requests can be initiated per second for this API.

        :param request: Request instance for SmartStructuralOCRV2.
        :type request: :class:`tencentcloud.ocr.v20181119.models.SmartStructuralOCRV2Request`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.SmartStructuralOCRV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SmartStructuralOCRV2", params, headers=headers)
            response = json.loads(body)
            model = models.SmartStructuralOCRV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VinOCR(self, request):
        r"""This API is used to recognize the vehicle identification number (VIN) in an image.

        :param request: Request instance for VinOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VinOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VinOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VinOCR", params, headers=headers)
            response = json.loads(body)
            model = models.VinOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))