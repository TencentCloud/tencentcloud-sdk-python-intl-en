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
from tencentcloud.ocr.v20181119 import models


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.tencentcloudapi.com'
    _service = 'ocr'


    def BankCardOCR(self, request):
        """This API is used to detect and recognize key fields such as the card number, bank information, and expiration date on mainstream bank cards in Mainland China.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for BankCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.BankCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GeneralAccurateOCR(self, request):
        """This API is used to detect and recognize characters in an image. It can recognize Chinese, English, Chinese-English, digits, and special symbols and return the text box positions and characters.

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
        """This API is used to detect and recognize characters in an image in the following 20 languages: Chinese, English, Japanese, Korean, Spanish, French, German, Portuguese, Vietnamese, Malay, Russian, Italian, Dutch, Swedish, Finnish, Danish, Norwegian, Hungarian, Thai, and Arabic. Mixed characters in English and each supported language can be recognized together.

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


    def HKIDCardOCR(self, request):
        """This API is used to recognize key fields on the photo side of a Hong Kong (China) identity card, including name in Chinese, name in English, telecode for name, date of birth, gender, document symbol, date of the first issue, date of the last receipt, identity card number, and permanent residency attribute.

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


    def HmtResidentPermitOCR(self, request):
        """This API is used to recognize key fields on the front and back sides of a residence permit for Hong Kong, Macao, or Taiwan residents, including name, gender, date of birth, address, ID number, issuing authority, validity period, number of issues, and permit number. It can be used for residence permit OCR in scenarios such as bank account opening and user registration.

        A maximum of 20 requests can be initiated per second for this API.

        :param request: Request instance for HmtResidentPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HmtResidentPermitOCR", params, headers=headers)
            response = json.loads(body)
            model = models.HmtResidentPermitOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IDCardOCR(self, request):
        """This API is used to recognize all fields on the front and back sides of a second-generation resident identity card for the Chinese mainland: name, gender, ethnicity, date of birth, domicile, identification number, issuing authority, and validity period, with a recognition accuracy of over 99%.

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

        :param request: Request instance for IDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.IDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LicensePlateOCR(self, request):
        """This API is used to recognize a license plate attached to a motor vehicle in the Chinese mainland and return the regional code, license plate number, and license plate color.

        A maximum of 10 requests can be initiated per second for this API.

        :param request: Request instance for LicensePlateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LicensePlateOCR", params, headers=headers)
            response = json.loads(body)
            model = models.LicensePlateOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MLIDCardOCR(self, request):
        """This API is used to recognize a Malaysian identity card, including identity card number, name, gender, and address. It is also used to crop identity photos and give alarms for photographed or photocopied certificates.

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
        """This API is used to recognize a passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions. Recognizable fields include passport ID, name, date of birth, gender, expiration date, issuing country/region, and nationality. It has the features of cropping identity photos and alarming for photographed or photocopied documents.

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
        """This API is used to recognize all fields on the front of a mainland travel permit for Hong Kong, Macao, or Taiwan residents: name in Chinese, name in English, gender, date of birth, issuing authority, validity period, document number, place of issuance, number of issues, and document type.

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


    def PermitOCR(self, request):
        """This API is used to recognize the fields on an exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan, including place of issuance, issuing authority, validity period, gender, date of birth, name in English, name in Chinese, and document number.

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


    def RecognizeGeneralInvoice(self, request):
        """This API is used to recognize various types of invoices or tickets in an image or PDF file. You can also specify a type. 14 types of standard expense reimbursement invoices are supported, including value-added tax (VAT) invoice (special, general, roll, blockchain, and toll), fully digitalized electronic invoice (special and general), non-tax revenue invoice (general receipt and general payment voucher), quota invoice, general machine-printed invoice, car sales invoice (motor vehicle sales invoice and used car invoice), train ticket, taxi receipt, itinerary/receipt of e-ticket for air transportation, bus ticket, ship ticket, toll receipt, and medical invoice (inpatient and outpatient). This API can also be used for intelligent recognition of other types of invoices. To try now, click [here](https://intl.cloud.tencent.com/product/ocr?from_cn_redirect=1).

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

        :param request: Request instance for RecognizeGeneralInvoice.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeGeneralInvoiceRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeGeneralInvoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeGeneralInvoice", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeGeneralInvoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeIndonesiaIDCardOCR(self, request):
        """This API is used to recognize an Indonesian identity card.

        The API request rate is limited to 20 requests/sec by default.

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


    def RecognizeKoreanDrivingLicenseOCR(self, request):
        """This API is used to recognize a South Korean driver's license.

        :param request: Request instance for RecognizeKoreanDrivingLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeKoreanDrivingLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeKoreanDrivingLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeKoreanDrivingLicenseOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeKoreanDrivingLicenseOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeKoreanIDCardOCR(self, request):
        """This API is used to recognize a South Korean ID card.

        :param request: Request instance for RecognizeKoreanIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeKoreanIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeKoreanIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeKoreanIDCardOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeKoreanIDCardOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeMainlandIDCardOCR(self, request):
        """This interface supports the identification of all fields on the front and back of the second-generation ID card for mainland Chinese residents.Including name, gender, ethnicity, date of birth, address, citizen ID number, issuing authority, and validity period, the identification accuracy reaches more than 99%.In addition, this interface also supports a variety of value-added capabilities to meet the needs of different scenarios. Such as the cropping function of ID card photos and portrait photos, and also has 5 alarm functions.
        As shown in the table below. <table style="width:650px"> <thead> <tr> <th width="150">Value-added ability</th> <th width="500">Ability items</th> </tr> </thead> <tbody> <tr> <td rowspan="9">Alarm function</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>ID card copy warning</td> </tr> <tr> <td>Alarm for occlusion in the ID card frame</td> </tr> <tr> <td>ID card reflective warning</td> </tr> <tr> <td>Blurry picture warning</td> </tr> </tbody> </table> Default interface request frequency limit: 20 times/second

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


    def RecognizePhilippinesDrivingLicenseOCR(self, request):
        """This API is used to recognize a Philippine driver's license.

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
        """This API is used to recognize a Philippine SSSID/UMID card.

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
        """This API is used to recognize a Philippine TIN ID card.

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
        """This API is used to recognize a Philippine Unified Multi-Purpose ID (UMID) card.

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
        """This API is used to recognize a Philippine voters ID card. It can recognize fields such as first name, family name, date of birth, civil status, citizenship, address, precinct, and voter's identification number (VIN).

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


    def RecognizeTableAccurateOCR(self, request):
        """This API is used to recognize regular tables, borderless tables, or multi-tables in images or PDF files containing Chinese and English texts. It returns the text content of each cell, supports recognition of rotated table images, and can save the recognition results into an Excel document. It delivers higher recognition accuracy than that of table OCR v2 and applies to more scenarios. The recognition accuracy in difficult table scenarios, such as irregular tables and nested tables (borderless tables contained in bordered tables), is better than that of table OCR v2. To try it, click [here](https://intl.cloud.tencent.com/product/smart?from_cn_redirect=1-ocr).

        A maximum of 2 requests can be initiated per second for this API.

        :param request: Request instance for RecognizeTableAccurateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.RecognizeTableAccurateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.RecognizeTableAccurateOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeTableAccurateOCR", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeTableAccurateOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeThaiIDCardOCR(self, request):
        """This API is used to recognize the fields on a Thai identity card, including name in Thai, name in English, address, date of birth, identification number, date of issue, and date of expiry.
        Currently, this API is not generally available. For more information, please [contact your sales rep](https://intl.cloud.tencent.com/about/connect?from_cn_redirect=1).

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


    def SealOCR(self, request):
        """This API is used to recognize various types of seals, including invoice seals and finance seals. It is suitable for scenarios such as official document and invoice/ticket OCR.

        A maximum of 5 requests can be initiated per second for this API.

        :param request: Request instance for SealOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.SealOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.SealOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SealOCR", params, headers=headers)
            response = json.loads(body)
            model = models.SealOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SmartStructuralOCRV2(self, request):
        """This API is used to recognize fields from cards, documents, bills, forms, contracts, and other structured information. It is flexible and efficient to use, without any configuration required. This API is suitable for recognizing structured information.

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


    def TableOCR(self, request):
        """This API is used to detect and recognize Chinese and English forms in images. It can return the text content of each cell and save the recognition result as Excel.

        This API is not fully available for the time being. For more information, please contact your [Tencent Cloud sales rep](https://intl.cloud.tencent.com/contact-sales).

        :param request: Request instance for TableOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TableOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TableOCRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TableOCR", params, headers=headers)
            response = json.loads(body)
            model = models.TableOCRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VinOCR(self, request):
        """This API is used to recognize the vehicle identification number (VIN) in an image.

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