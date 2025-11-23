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
from tencentcloud.ocr.v20181119 import models
from typing import Dict


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.intl.tencentcloudapi.com'
    _service = 'ocr'

    async def ApplyCardVerificationExternal(
            self,
            request: models.ApplyCardVerificationExternalRequest,
            opts: Dict = None,
    ) -> models.ApplyCardVerificationExternalResponse:
        """
        This API is used for general recognition of overseas cards.

        The following list details the countries or regions, document types supported by the overseas document recognition API and whether the back side of the document is required:

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
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyCardVerificationExternal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyCardVerificationExternalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCardOCR(
            self,
            request: models.BankCardOCRRequest,
            opts: Dict = None,
    ) -> models.BankCardOCRResponse:
        """
        This API is used to detect and recognize key fields such as the card number, bank information, and expiration date on mainstream bank cards in Mainland China.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "BankCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractDocMulti(
            self,
            request: models.ExtractDocMultiRequest,
            opts: Dict = None,
    ) -> models.ExtractDocMultiResponse:
        """
        This API supports identifying and extracting field information in structured scenarios such as complex scenarios and multiple formats. Key scenarios include: finance, health care, transportation, travel, insurance. Click [experience now](https://ocrdemo.cloud.tencent.com/).

        This API is used to set the alias SmartStructuralPro.

        The default API request rate limit is 5 requests per second.
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractDocMulti"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractDocMultiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralAccurateOCR(
            self,
            request: models.GeneralAccurateOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralAccurateOCRResponse:
        """
        This API is used to detect and recognize characters in an image. It can recognize Chinese, English, Chinese-English, digits, and special symbols and return the text box positions and characters.

        It is suitable for scenarios with a lot of characters in complex layouts and requiring high recognition accuracy, such as examination papers, online images, signboards, and legal documents.

        Strengths: compared with general print recognition, it provides higher-precision character recognition services. Its accuracy and recall rate are higher in difficult scenarios such as a large number of characters, long strings of digits, small characters, blurry characters, and tilted text.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralAccurateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralAccurateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralBasicOCR(
            self,
            request: models.GeneralBasicOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralBasicOCRResponse:
        """
        This API is used to detect and recognize characters in an image in the following 20 languages: Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, Thai, and Arabic. Mixed characters in English and each supported language can be recognized together.

        It can recognize printed text in paper documents, online images, ads, signboards, menus, video titles, profile photos, etc.

        Strengths: it can automatically recognize the text language, return the text box coordinate information, and automatically rotate tilted text to the upright direction.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralBasicOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralBasicOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCardVerificationExternalResult(
            self,
            request: models.GetCardVerificationExternalResultRequest,
            opts: Dict = None,
    ) -> models.GetCardVerificationExternalResultResponse:
        """
        This API is used to obtain document recognition results.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCardVerificationExternalResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCardVerificationExternalResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HKIDCardOCR(
            self,
            request: models.HKIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.HKIDCardOCRResponse:
        """
        This API is used to recognize key fields on the photo side of a Hong Kong (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "HKIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HKIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HmtResidentPermitOCR(
            self,
            request: models.HmtResidentPermitOCRRequest,
            opts: Dict = None,
    ) -> models.HmtResidentPermitOCRResponse:
        """
        This API is used to recognize key fields on the front and back sides of a residence permit for Hong Kong, Macao, or Taiwan residents, including name, gender, date of birth, address, ID number, issuing authority, validity period, number of issues, and permit number. It can be used for residence permit OCR in scenarios such as bank account opening and user registration.

        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "HmtResidentPermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HmtResidentPermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IDCardOCR(
            self,
            request: models.IDCardOCRRequest,
            opts: Dict = None,
    ) -> models.IDCardOCRResponse:
        """
        This API is used to recognize all fields on the front and back sides of a second-generation resident identity card for the Chinese mainland: name, gender, ethnicity, date of birth, domicile, identification number, issuing authority, and validity period, with a recognition accuracy of over 99%.

        In addition, this API supports multiple value-added capabilities to meet the needs of different scenarios. It can crop ID card photos and profile photos, and provide warnings for nine cases, as detailed below.

        <table style="width:650px">
              <thead>
                <tr>
               <th width="150">Capability</th>
                  <th width="500">Description</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="2">Cropping</td>
                  <td>Crops the ID card photo (by removing extra edges outside the ID card and automatically correcting the shooting angle).</td>
                </tr>
                <tr>
                  <td>Crops the profile photo (by automatically cutting out the face area in the ID card).</td>
                </tr>
                <tr>
                  <td rowspan="9">Warning</td>
                  <td>Warns about invalid ID card validity periods.</td>
                </tr>
                <tr>
                  <td>Warns about  incomplete ID card borders.</td>
                </tr>
                <tr>
                  <td>Warns about photocopied images.</td>
                </tr>
                <tr>
                  <td>Warns about spoofed images.</td>
                </tr>
                  <tr>
                  <td>Warns about border and frame occlusions.</td>
                </tr>
                 <tr>
                  <td>Warns about temporary ID cards.</td>
                </tr>
                  <tr>
                  <td>Warns about photoshopped images.</td>
                </tr>
                  <tr>
                  <td>Warns about blurry ID card images (blurriness can be determined based on the image quality score).</td>
                </tr>
              </tbody>
            </table>

        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "IDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LicensePlateOCR(
            self,
            request: models.LicensePlateOCRRequest,
            opts: Dict = None,
    ) -> models.LicensePlateOCRResponse:
        """
        This API is used to recognize a license plate attached to a motor vehicle in the Chinese mainland and return the regional code, license plate number, and license plate color.

        A maximum of 10 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "LicensePlateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LicensePlateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MLIDCardOCR(
            self,
            request: models.MLIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.MLIDCardOCRResponse:
        """
        This API is used to recognize a Malaysian identity card, including identity card number, name, gender, and address. It is also used to crop identity photos and give alarms for photographed or photocopied certificates.

        This API is not fully available for the time being. For more information, contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "MLIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MLIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MLIDPassportOCR(
            self,
            request: models.MLIDPassportOCRRequest,
            opts: Dict = None,
    ) -> models.MLIDPassportOCRResponse:
        """
        This API is used to recognize a passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country/region, and nationality. It has the features of cropping identity photos and alarming for photographed or photocopied documents.
        This interface supports regional scope: countries with machine-readable passports
        """
        
        kwargs = {}
        kwargs["action"] = "MLIDPassportOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MLIDPassportOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MainlandPermitOCR(
            self,
            request: models.MainlandPermitOCRRequest,
            opts: Dict = None,
    ) -> models.MainlandPermitOCRResponse:
        """
        This API is used to recognize all fields on the front of a mainland travel permit for Hong Kong, Macao, or Taiwan residents: name in Chinese, name in English, gender, date of birth, issuing authority, validity period, document number, place of issuance, number of issues, and document type.

        A maximum of 20 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "MainlandPermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MainlandPermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PermitOCR(
            self,
            request: models.PermitOCRRequest,
            opts: Dict = None,
    ) -> models.PermitOCRResponse:
        """
        This API is used to recognize the fields on an exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan, including place of issuance, issuing authority, validity period, gender, date of birth, name in English, name in Chinese, and document number.

        A maximum of 10 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "PermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeBrazilCommonOCR(
            self,
            request: models.RecognizeBrazilCommonOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeBrazilCommonOCRResponse:
        """
        This API is used to identify Brazil common documents.

        This API is used to set the default request rate limit to 5 requests/second.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeBrazilCommonOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeBrazilCommonOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeBrazilDriverLicenseOCR(
            self,
            request: models.RecognizeBrazilDriverLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeBrazilDriverLicenseOCRResponse:
        """
        This interface supports identification of the front and back of Brazilian driver's license. The identification fields include name, driver's license category, number, validity period, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeBrazilDriverLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeBrazilDriverLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeBrazilIDCardOCR(
            self,
            request: models.RecognizeBrazilIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeBrazilIDCardOCRResponse:
        """
        This interface supports identification of the front and back of Brazilian ID license. The identification fields include name, driver's license category, number, validity period, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeBrazilIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeBrazilIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeBrazilRNEOCR(
            self,
            request: models.RecognizeBrazilRNEOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeBrazilRNEOCRResponse:
        """
        Brazil RNE document recognition Default interface request frequency limit: 5 times/second
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeBrazilRNEOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeBrazilRNEOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeBrazilRNMOCR(
            self,
            request: models.RecognizeBrazilRNMOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeBrazilRNMOCRResponse:
        """
        This interface supports identification of the front and back of Brazilian RNM license. The default interface request frequency limit is 5 times per second.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeBrazilRNMOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeBrazilRNMOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeDetectCardCoords(
            self,
            request: models.RecognizeDetectCardCoordsRequest,
            opts: Dict = None,
    ) -> models.RecognizeDetectCardCoordsResponse:
        """
        This API is used to recognize the coordinates of four corners of cards.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeDetectCardCoords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeDetectCardCoordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeGeneralInvoice(
            self,
            request: models.RecognizeGeneralInvoiceRequest,
            opts: Dict = None,
    ) -> models.RecognizeGeneralInvoiceResponse:
        """
        This API is used to recognize various types of invoices or tickets in an image or PDF file. You can also specify a type. 14 types of standard expense reimbursement invoices are supported, including value-added tax (VAT) invoice (special, general, roll, blockchain, and toll), fully digitalized electronic invoice (special and general), non-tax revenue invoice (general receipt and general payment voucher), quota invoice, general machine-printed invoice, car sales invoice (motor vehicle sales invoice and used car invoice), train ticket, taxi receipt, itinerary/receipt of e-ticket for air transportation, bus ticket, ship ticket, toll receipt, and medical invoice (inpatient and outpatient). This API can also be used for intelligent recognition of other types of invoices. To try now, click [here](https://intl.cloud.tencent.com/product/ocr?from_cn_redirect=1).

        A maximum of 5 requests can be initiated per second for this API.


        The invoice/ticket subtype (SubType), subtype description (TypeDescription), and parent type (Type) can be returned, as described below:
        <table style="width:715px">
              <thead>
                <tr>
                  <th style="width:200px">SubType</th>
                  <th style="width:200px">TypeDescription</th>
                  <th >Type</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> VatSpecialInvoice</td>
                  <td> Special VAT invoice </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatCommonInvoice</td>
                  <td> General VAT invoice </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicCommonInvoice </td>
                  <td> Electronic general VAT invoice </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicSpecialInvoice </td>
                  <td> Electronic special VAT invoice </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceBlockchain</td>
                  <td> Blockchain electronic invoice </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceToll</td>
                  <td> Electronic general VAT invoice (toll)</td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicSpecialInvoiceFull</td>
                  <td> Electronic invoice (special)</td>
                  <td> 16 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceFull</td>
                  <td> Electronic invoice (general) </td>
                  <td> 16 </td>
                </tr>
                <tr>
                  <td> MotorVehicleSaleInvoice </td>
                  <td> Motor vehicle sales invoice </td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> UsedCarPurchaseInvoice </td>
                  <td> Used car invoice </td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> VatInvoiceRoll </td>
                  <td> General VAT invoice (roll) </td>
                  <td> 11 </td>
                </tr>
                <tr>
                  <td> TaxiTicket </td>
                  <td> Taxi receipt </td>
                  <td> 0 </td>
                </tr>
                <tr>
                  <td> QuotaInvoice </td>
                  <td> Quota invoice </td>
                  <td> 1 </td>
                </tr>
                <tr>
                  <td> TrainTicket </td>
                  <td> Train ticket </td>
                  <td> 2 </td>
                </tr>
                <tr>
                  <td> AirTransport </td>
                  <td> Itinerary/Receipt of e-ticket for air transportation </td>
                  <td> 5 </td>
                </tr>
                <tr>
                  <td> MachinePrintedInvoice </td>
                  <td> General machine-printed invoice </td>
                  <td> 8 </td>
                </tr>
                <tr>
                  <td> BusInvoice </td>
                  <td> Bus ticket </td>
                  <td> 9 </td>
                </tr>
                <tr>
                  <td> ShippingInvoice </td>
                  <td> Ship ticket </td>
                  <td> 10 </td>
                </tr>
                <tr>
                  <td> NonTaxIncomeGeneralBill </td>
                  <td> General receipt for non-tax revenue </td>
                  <td> 15 </td>
                </tr>
                <tr>
                  <td> NonTaxIncomeElectronicBill </td>
                  <td> General payment voucher for non-tax revenue (electronic) </td>
                  <td> 15 </td>
                </tr>
                <tr>
                  <td> TollInvoice </td>
                  <td> Toll receipt </td>
                  <td> 13 </td>
                </tr>
                <tr>
                  <td> OtherInvoice </td>
                  <td> Other </td>
                  <td> -1 </td>
                </tr>
              </tbody>
            </table>
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeGeneralInvoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeGeneralInvoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeIndonesiaIDCardOCR(
            self,
            request: models.RecognizeIndonesiaIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeIndonesiaIDCardOCRResponse:
        """
        This API is used to recognize an Indonesian identity card.

        The API request rate is limited to 20 requests/sec by default.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeIndonesiaIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeIndonesiaIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeKoreanDrivingLicenseOCR(
            self,
            request: models.RecognizeKoreanDrivingLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeKoreanDrivingLicenseOCRResponse:
        """
        This API is used to recognize a South Korean driver's license.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeKoreanDrivingLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeKoreanDrivingLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeKoreanIDCardOCR(
            self,
            request: models.RecognizeKoreanIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeKoreanIDCardOCRResponse:
        """
        This API is used to recognize a South Korean ID card.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeKoreanIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeKoreanIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeMacaoIDCardOCR(
            self,
            request: models.RecognizeMacaoIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeMacaoIDCardOCRResponse:
        """
        This API is used to recognize key fields on the photo side of a Macao (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeMacaoIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeMacaoIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeMainlandIDCardOCR(
            self,
            request: models.RecognizeMainlandIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeMainlandIDCardOCRResponse:
        """
        This interface supports the identification of all fields on the front and back of the second-generation ID card for mainland Chinese residents.Including name, gender, ethnicity, date of birth, address, citizen ID number, issuing authority, and validity period, the identification accuracy reaches more than 99%.In addition, this interface also supports a variety of value-added capabilities to meet the needs of different scenarios. Such as the cropping function of ID card photos and portrait photos, and also has 5 alarm functions.
        As shown in the table below. <table style="width:650px"> <thead> <tr> <th width="150">Value-added ability</th> <th width="500">Ability items</th> </tr> </thead> <tbody> <tr> <td rowspan="9">Alarm function</td> </tr> <tr> <td>ID card photocopy warning</td> </tr> <tr> <td>ID card on-screen display warning</td> </tr> <tr> <td>Alarm for occlusion in the ID card frame</td> </tr> <tr> <td>ID card reflective warning</td> </tr> <tr> <td>Blurry picture warning</td> </tr> </tbody> </table> Default interface request frequency limit: 20 times/second
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeMainlandIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeMainlandIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeMexicoVTID(
            self,
            request: models.RecognizeMexicoVTIDRequest,
            opts: Dict = None,
    ) -> models.RecognizeMexicoVTIDResponse:
        """
        This interface supports identification of the front and back of Mexican Voter ID Card. The default interface request frequency limit is 5 times per second.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeMexicoVTID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeMexicoVTIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizePhilippinesDrivingLicenseOCR(
            self,
            request: models.RecognizePhilippinesDrivingLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizePhilippinesDrivingLicenseOCRResponse:
        """
        This API is used to recognize a Philippine driver's license.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizePhilippinesDrivingLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizePhilippinesDrivingLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizePhilippinesSssIDOCR(
            self,
            request: models.RecognizePhilippinesSssIDOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizePhilippinesSssIDOCRResponse:
        """
        This API is used to recognize a Philippine SSSID/UMID card.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizePhilippinesSssIDOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizePhilippinesSssIDOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizePhilippinesTinIDOCR(
            self,
            request: models.RecognizePhilippinesTinIDOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizePhilippinesTinIDOCRResponse:
        """
        This API is used to recognize a Philippine TIN ID card.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizePhilippinesTinIDOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizePhilippinesTinIDOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizePhilippinesUMIDOCR(
            self,
            request: models.RecognizePhilippinesUMIDOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizePhilippinesUMIDOCRResponse:
        """
        This API is used to recognize a Philippine Unified Multi-Purpose ID (UMID) card.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizePhilippinesUMIDOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizePhilippinesUMIDOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizePhilippinesVoteIDOCR(
            self,
            request: models.RecognizePhilippinesVoteIDOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizePhilippinesVoteIDOCRResponse:
        """
        This API is used to recognize a Philippine voters ID card. It can recognize fields such as first name, family name, date of birth, civil status, citizenship, address, precinct, and voter's identification number (VIN).

        The API request rate is limited to 20 requests/sec by default.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizePhilippinesVoteIDOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizePhilippinesVoteIDOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeSingaporeIDCardOCR(
            self,
            request: models.RecognizeSingaporeIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeSingaporeIDCardOCRResponse:
        """
        This interface supports the identification of all fields on the front side of ID card for Singapore residents.The identification accuracy reaches more than 99%.In addition, this interface also supports a variety of value-added capabilities to meet the needs of different scenarios. Such as the cropping function of ID card photos and portrait photos, and also has 5 alarm functions.
        As shown in the table below. <table style="width:650px"> <thead> <tr> <th width="150">Value-added ability</th> <th width="500">Ability items</th> </tr> </thead> <tbody> <tr> <td rowspan="9">Alarm function</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>Alarm for occlusion in the ID card frame</td> </tr> <tr> <td>ID card reflective warning</td> </tr> <tr> <td>Blurry picture warning</td> </tr> </tbody> </table> Default interface request frequency limit: 20 times/second
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeSingaporeIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeSingaporeIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeTableAccurateOCR(
            self,
            request: models.RecognizeTableAccurateOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeTableAccurateOCRResponse:
        """
        This API is used to recognize regular tables, borderless tables, or multi-tables in images or PDF files containing Chinese and English texts. It returns the text content of each cell, supports recognition of rotated table images, and can save the recognition results into an Excel document. It delivers higher recognition accuracy than that of table OCR v2 and applies to more scenarios. The recognition accuracy in difficult table scenarios, such as irregular tables and nested tables (borderless tables contained in bordered tables), is better than that of table OCR v2. To try it, click [here](https://intl.cloud.tencent.com/product/smart?from_cn_redirect=1-ocr).

        A maximum of 2 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeTableAccurateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeTableAccurateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeThaiIDCardOCR(
            self,
            request: models.RecognizeThaiIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeThaiIDCardOCRResponse:
        """
        This API is used to recognize the fields on a Thai identity card, including name in Thai, name in English, address, date of birth, identification number, date of issue, and date of expiry.

        A maximum of 10 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeThaiIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeThaiIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeThaiPinkCard(
            self,
            request: models.RecognizeThaiPinkCardRequest,
            opts: Dict = None,
    ) -> models.RecognizeThaiPinkCardResponse:
        """
        This API is used to recognize the fields on a Thai identity card, including name in Thai, name in English, address, date of birth, identification number, date of issue, and date of expiry.
        Currently, this API is not generally available. For more information, please [contact your sales rep](https://intl.cloud.tencent.com/about/connect?from_cn_redirect=1).

        A maximum of 5 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeThaiPinkCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeThaiPinkCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SealOCR(
            self,
            request: models.SealOCRRequest,
            opts: Dict = None,
    ) -> models.SealOCRResponse:
        """
        This API is used to recognize various types of seals, including invoice seals and finance seals. It is suitable for scenarios such as official document and invoice/ticket OCR.

        A maximum of 5 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "SealOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SealOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmartStructuralOCRV2(
            self,
            request: models.SmartStructuralOCRV2Request,
            opts: Dict = None,
    ) -> models.SmartStructuralOCRV2Response:
        """
        This API is used to recognize fields from cards, documents, bills, forms, contracts, and other structured information. It is flexible and efficient to use, without any configuration required. This API is suitable for recognizing structured information.

        A maximum of 10 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "SmartStructuralOCRV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmartStructuralOCRV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmartStructuralPro(
            self,
            request: models.SmartStructuralProRequest,
            opts: Dict = None,
    ) -> models.SmartStructuralProResponse:
        """
        This API is used to recognize fields from cards, documents, bills, forms, contracts, and other structured information. It is flexible and efficient to use, without any configuration required. This API is suitable for recognizing structured information.

        A maximum of 10 requests can be initiated per second for this API.
        """
        
        kwargs = {}
        kwargs["action"] = "SmartStructuralPro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmartStructuralProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TableOCR(
            self,
            request: models.TableOCRRequest,
            opts: Dict = None,
    ) -> models.TableOCRResponse:
        """
        This API is used to detect and recognize Chinese and English forms in images. It can return the text content of each cell and save the recognition result as Excel.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).
        """
        
        kwargs = {}
        kwargs["action"] = "TableOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TableOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VinOCR(
            self,
            request: models.VinOCRRequest,
            opts: Dict = None,
    ) -> models.VinOCRResponse:
        """
        This API is used to recognize the vehicle identification number (VIN) in an image.
        """
        
        kwargs = {}
        kwargs["action"] = "VinOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VinOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)