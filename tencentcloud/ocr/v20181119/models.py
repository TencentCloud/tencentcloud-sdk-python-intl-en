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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddressInfo(AbstractModel):
    r"""Overseas document recognition address information.

    """

    def __init__(self):
        r"""
        :param _Country: Country.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Country: str
        :param _PostalCode: Postal code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostalCode: str
        :param _Subdivision: Sub-region or state/province.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Subdivision: str
        :param _District: District or county.
Note: This field may return null, indicating that no valid values can be obtained.
        :type District: str
        :param _City: City name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type City: str
        :param _Subdistrict: Subdistrict or township.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Subdistrict: str
        :param _FormattedAddress: Formatted complete address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        :param _LineOne: First line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LineOne: str
        :param _LineTwo: Second line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LineTwo: str
        :param _LineThree: Specifies the third line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LineThree: str
        :param _LineFour: Specifies the fourth line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LineFour: str
        :param _LineFive: Specifies the fifth line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LineFive: str
        """
        self._Country = None
        self._PostalCode = None
        self._Subdivision = None
        self._District = None
        self._City = None
        self._Subdistrict = None
        self._FormattedAddress = None
        self._LineOne = None
        self._LineTwo = None
        self._LineThree = None
        self._LineFour = None
        self._LineFive = None

    @property
    def Country(self):
        r"""Country.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def PostalCode(self):
        r"""Postal code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def Subdivision(self):
        r"""Sub-region or state/province.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Subdivision

    @Subdivision.setter
    def Subdivision(self, Subdivision):
        self._Subdivision = Subdivision

    @property
    def District(self):
        r"""District or county.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def City(self):
        r"""City name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Subdistrict(self):
        r"""Subdistrict or township.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Subdistrict

    @Subdistrict.setter
    def Subdistrict(self, Subdistrict):
        self._Subdistrict = Subdistrict

    @property
    def FormattedAddress(self):
        r"""Formatted complete address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress

    @property
    def LineOne(self):
        r"""First line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LineOne

    @LineOne.setter
    def LineOne(self, LineOne):
        self._LineOne = LineOne

    @property
    def LineTwo(self):
        r"""Second line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LineTwo

    @LineTwo.setter
    def LineTwo(self, LineTwo):
        self._LineTwo = LineTwo

    @property
    def LineThree(self):
        r"""Specifies the third line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LineThree

    @LineThree.setter
    def LineThree(self, LineThree):
        self._LineThree = LineThree

    @property
    def LineFour(self):
        r"""Specifies the fourth line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LineFour

    @LineFour.setter
    def LineFour(self, LineFour):
        self._LineFour = LineFour

    @property
    def LineFive(self):
        r"""Specifies the fifth line of the address bar.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LineFive

    @LineFive.setter
    def LineFive(self, LineFive):
        self._LineFive = LineFive


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._PostalCode = params.get("PostalCode")
        self._Subdivision = params.get("Subdivision")
        self._District = params.get("District")
        self._City = params.get("City")
        self._Subdistrict = params.get("Subdistrict")
        self._FormattedAddress = params.get("FormattedAddress")
        self._LineOne = params.get("LineOne")
        self._LineTwo = params.get("LineTwo")
        self._LineThree = params.get("LineThree")
        self._LineFour = params.get("LineFour")
        self._LineFive = params.get("LineFive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzedLog(AbstractModel):
    r"""Intelligent review log

    """

    def __init__(self):
        r"""
        :param _StepKey: <p>Indexes of the procedure.</p><p>Enumeration value:</p><ul><li>L1_IMAGE_QUALITY: Image quality detection</li><li>L2_RULE_ENGINE: Rule verification</li><li>L3_LLM_JUDGE: Large model judgment</li></ul>
        :type StepKey: str
        :param _Decision: <p>Compliant and non-compliant are final states; to be determined is an intermediate state. Judgment status of each layer: Compliant Non-Compliant Pending.</p>
        :type Decision: str
        :param _DecisionMessage: <p>Reason for the current layer judgment</p>
        :type DecisionMessage: str
        :param _CostTime: <p>Time taken by the current layer</p><p>Unit: ms</p>
        :type CostTime: int
        """
        self._StepKey = None
        self._Decision = None
        self._DecisionMessage = None
        self._CostTime = None

    @property
    def StepKey(self):
        r"""<p>Indexes of the procedure.</p><p>Enumeration value:</p><ul><li>L1_IMAGE_QUALITY: Image quality detection</li><li>L2_RULE_ENGINE: Rule verification</li><li>L3_LLM_JUDGE: Large model judgment</li></ul>
        :rtype: str
        """
        return self._StepKey

    @StepKey.setter
    def StepKey(self, StepKey):
        self._StepKey = StepKey

    @property
    def Decision(self):
        r"""<p>Compliant and non-compliant are final states; to be determined is an intermediate state. Judgment status of each layer: Compliant Non-Compliant Pending.</p>
        :rtype: str
        """
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision

    @property
    def DecisionMessage(self):
        r"""<p>Reason for the current layer judgment</p>
        :rtype: str
        """
        return self._DecisionMessage

    @DecisionMessage.setter
    def DecisionMessage(self, DecisionMessage):
        self._DecisionMessage = DecisionMessage

    @property
    def CostTime(self):
        r"""<p>Time taken by the current layer</p><p>Unit: ms</p>
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime


    def _deserialize(self, params):
        self._StepKey = params.get("StepKey")
        self._Decision = params.get("Decision")
        self._DecisionMessage = params.get("DecisionMessage")
        self._CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCardVerificationExternalRequest(AbstractModel):
    r"""ApplyCardVerificationExternal request structure.

    """

    def __init__(self):
        r"""
        :param _Nationality: Country/Region of the document. For the full list of supported countries/regions, refer to the API description.
        :type Nationality: str
        :param _CardType: Document type. Supported values: ID_CARD, PASSPORT, DRIVING_LICENSE, RESIDENCE_PERMIT (only supported in certain countries/regions, including Australia, Canada, Germany, New Zealand, Nigeria, Singapore).
        :type CardType: str
        :param _ImageBase64Front: Base64-encoded image of the document front.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: You must provide either ImageUrlFront or ImageBase64Front. If both are provided, only ImageUrlFront is used.
        :type ImageBase64Front: str
        :param _ImageBase64Back: The Base64 value of the reverse side of the document. Supported image formats: PNG, JPG/JPEG. 
Supported image size: the downloaded image after Base64 encoding must be no more than 2M. Image download time must be no more than 5 seconds. 
Supported image resolution: between 256 \* 256 and 4096 \* 4096. For some documents, either ImageUrlBack or ImageBase64Back must be provided. If both are provided, only ImageUrlBack is used.
        :type ImageBase64Back: str
        :param _ImageUrlFront: URL of the document front image.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: You must provide either ImageUrlFront or ImageBase64Front. If both are provided, only ImageUrlFront is used.
        :type ImageUrlFront: str
        :param _ImageUrlBack: URL of the document back image.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: For some documents, you must provide either ImageUrlBack or ImageBase64Back. If both are provided, only ImageUrlBack is used.
        :type ImageUrlBack: str
        :param _ReturnHeadImage: Whether to crop and return the face image from the document. Default: false.
If set to true, the image constraints are:
- Size after Base64 encoding must not exceed 5 MB.
- Maximum pixel width/height: 4000 for JPG, 2000 for other formats.
- Minimum pixel width/height: 64.
- Supported formats: PNG, JPG, JPEG, BMP (GIF not supported).
        :type ReturnHeadImage: bool
        """
        self._Nationality = None
        self._CardType = None
        self._ImageBase64Front = None
        self._ImageBase64Back = None
        self._ImageUrlFront = None
        self._ImageUrlBack = None
        self._ReturnHeadImage = None

    @property
    def Nationality(self):
        r"""Country/Region of the document. For the full list of supported countries/regions, refer to the API description.
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def CardType(self):
        r"""Document type. Supported values: ID_CARD, PASSPORT, DRIVING_LICENSE, RESIDENCE_PERMIT (only supported in certain countries/regions, including Australia, Canada, Germany, New Zealand, Nigeria, Singapore).
        :rtype: str
        """
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def ImageBase64Front(self):
        r"""Base64-encoded image of the document front.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: You must provide either ImageUrlFront or ImageBase64Front. If both are provided, only ImageUrlFront is used.
        :rtype: str
        """
        return self._ImageBase64Front

    @ImageBase64Front.setter
    def ImageBase64Front(self, ImageBase64Front):
        self._ImageBase64Front = ImageBase64Front

    @property
    def ImageBase64Back(self):
        r"""The Base64 value of the reverse side of the document. Supported image formats: PNG, JPG/JPEG. 
Supported image size: the downloaded image after Base64 encoding must be no more than 2M. Image download time must be no more than 5 seconds. 
Supported image resolution: between 256 \* 256 and 4096 \* 4096. For some documents, either ImageUrlBack or ImageBase64Back must be provided. If both are provided, only ImageUrlBack is used.
        :rtype: str
        """
        return self._ImageBase64Back

    @ImageBase64Back.setter
    def ImageBase64Back(self, ImageBase64Back):
        self._ImageBase64Back = ImageBase64Back

    @property
    def ImageUrlFront(self):
        r"""URL of the document front image.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: You must provide either ImageUrlFront or ImageBase64Front. If both are provided, only ImageUrlFront is used.
        :rtype: str
        """
        return self._ImageUrlFront

    @ImageUrlFront.setter
    def ImageUrlFront(self, ImageUrlFront):
        self._ImageUrlFront = ImageUrlFront

    @property
    def ImageUrlBack(self):
        r"""URL of the document back image.
Supported image formats: PNG, JPG/JPEG (GIF not supported).
Supported image size: The downloaded image after Base64 encoding must not exceed 2 MB. Image download time must not exceed 5 seconds.
Supported image resolution: Between 256*256 and 4096*4096 pixels.
Note: For some documents, you must provide either ImageUrlBack or ImageBase64Back. If both are provided, only ImageUrlBack is used.
        :rtype: str
        """
        return self._ImageUrlBack

    @ImageUrlBack.setter
    def ImageUrlBack(self, ImageUrlBack):
        self._ImageUrlBack = ImageUrlBack

    @property
    def ReturnHeadImage(self):
        r"""Whether to crop and return the face image from the document. Default: false.
If set to true, the image constraints are:
- Size after Base64 encoding must not exceed 5 MB.
- Maximum pixel width/height: 4000 for JPG, 2000 for other formats.
- Minimum pixel width/height: 64.
- Supported formats: PNG, JPG, JPEG, BMP (GIF not supported).
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._Nationality = params.get("Nationality")
        self._CardType = params.get("CardType")
        self._ImageBase64Front = params.get("ImageBase64Front")
        self._ImageBase64Back = params.get("ImageBase64Back")
        self._ImageUrlFront = params.get("ImageUrlFront")
        self._ImageUrlBack = params.get("ImageUrlBack")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCardVerificationExternalResponse(AbstractModel):
    r"""ApplyCardVerificationExternal response structure.

    """

    def __init__(self):
        r"""
        :param _CardVerificationToken: Unique token for the verification process, used to retrieve the result.
        :type CardVerificationToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CardVerificationToken = None
        self._RequestId = None

    @property
    def CardVerificationToken(self):
        r"""Unique token for the verification process, used to retrieve the result.
        :rtype: str
        """
        return self._CardVerificationToken

    @CardVerificationToken.setter
    def CardVerificationToken(self, CardVerificationToken):
        self._CardVerificationToken = CardVerificationToken

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CardVerificationToken = params.get("CardVerificationToken")
        self._RequestId = params.get("RequestId")


class BrazilCardInfo(AbstractModel):
    r"""Type of document in brazil.

    """

    def __init__(self):
        r"""
        :param _RNE: RNE document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RNE: :class:`tencentcloud.ocr.v20181119.models.BrazilRNEInfo`
        :param _RNM: Specifies the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RNM: :class:`tencentcloud.ocr.v20181119.models.BrazilRNMInfo`
        :param _DriverLicense: Driver license document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DriverLicense: :class:`tencentcloud.ocr.v20181119.models.BrazilDriverLicenseInfo`
        :param _IDCard: ID card document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IDCard: :class:`tencentcloud.ocr.v20181119.models.BrazilIDCardInfo`
        """
        self._RNE = None
        self._RNM = None
        self._DriverLicense = None
        self._IDCard = None

    @property
    def RNE(self):
        r"""RNE document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BrazilRNEInfo`
        """
        return self._RNE

    @RNE.setter
    def RNE(self, RNE):
        self._RNE = RNE

    @property
    def RNM(self):
        r"""Specifies the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BrazilRNMInfo`
        """
        return self._RNM

    @RNM.setter
    def RNM(self, RNM):
        self._RNM = RNM

    @property
    def DriverLicense(self):
        r"""Driver license document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BrazilDriverLicenseInfo`
        """
        return self._DriverLicense

    @DriverLicense.setter
    def DriverLicense(self, DriverLicense):
        self._DriverLicense = DriverLicense

    @property
    def IDCard(self):
        r"""ID card document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BrazilIDCardInfo`
        """
        return self._IDCard

    @IDCard.setter
    def IDCard(self, IDCard):
        self._IDCard = IDCard


    def _deserialize(self, params):
        if params.get("RNE") is not None:
            self._RNE = BrazilRNEInfo()
            self._RNE._deserialize(params.get("RNE"))
        if params.get("RNM") is not None:
            self._RNM = BrazilRNMInfo()
            self._RNM._deserialize(params.get("RNM"))
        if params.get("DriverLicense") is not None:
            self._DriverLicense = BrazilDriverLicenseInfo()
            self._DriverLicense._deserialize(params.get("DriverLicense"))
        if params.get("IDCard") is not None:
            self._IDCard = BrazilIDCardInfo()
            self._IDCard._deserialize(params.get("IDCard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrazilDriverLicenseInfo(AbstractModel):
    r"""Driver'S license type in brazil.

    """

    def __init__(self):
        r"""
        :param _NOME: Name.
        :type NOME: str
        :param _CatHab: Specifies the driver's license type.
        :type CatHab: str
        :param _CNHNumber: Driver’s license id.
        :type CNHNumber: str
        :param _VALIDADE: Expiration date.
        :type VALIDADE: str
        :param _QUALIFICATION: Indicates the qualification.
        :type QUALIFICATION: str
        :param _IDENTIDADE: Identity card number.
        :type IDENTIDADE: str
        :param _CPF: Tax number of the person.
        :type CPF: str
        :param _NASCIMENTO: Date of birth.
        :type NASCIMENTO: str
        :param _MEMBERSHIP: Membership status.
        :type MEMBERSHIP: str
        :param _REGISTRO: Registration number.
        :type REGISTRO: str
        :param _OBSERVATIONS: Remarks.
        :type OBSERVATIONS: str
        :param _IssueDate: Issue date.
        :type IssueDate: str
        :param _LOCAL: Issuing location.
        :type LOCAL: str
        :param _BackNumber: Record number.
        :type BackNumber: str
        :param _PortraitImage: Specifies the avatar in base64 format.
        :type PortraitImage: str
        """
        self._NOME = None
        self._CatHab = None
        self._CNHNumber = None
        self._VALIDADE = None
        self._QUALIFICATION = None
        self._IDENTIDADE = None
        self._CPF = None
        self._NASCIMENTO = None
        self._MEMBERSHIP = None
        self._REGISTRO = None
        self._OBSERVATIONS = None
        self._IssueDate = None
        self._LOCAL = None
        self._BackNumber = None
        self._PortraitImage = None

    @property
    def NOME(self):
        r"""Name.
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def CatHab(self):
        r"""Specifies the driver's license type.
        :rtype: str
        """
        return self._CatHab

    @CatHab.setter
    def CatHab(self, CatHab):
        self._CatHab = CatHab

    @property
    def CNHNumber(self):
        r"""Driver’s license id.
        :rtype: str
        """
        return self._CNHNumber

    @CNHNumber.setter
    def CNHNumber(self, CNHNumber):
        self._CNHNumber = CNHNumber

    @property
    def VALIDADE(self):
        r"""Expiration date.
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def QUALIFICATION(self):
        r"""Indicates the qualification.
        :rtype: str
        """
        return self._QUALIFICATION

    @QUALIFICATION.setter
    def QUALIFICATION(self, QUALIFICATION):
        self._QUALIFICATION = QUALIFICATION

    @property
    def IDENTIDADE(self):
        r"""Identity card number.
        :rtype: str
        """
        return self._IDENTIDADE

    @IDENTIDADE.setter
    def IDENTIDADE(self, IDENTIDADE):
        self._IDENTIDADE = IDENTIDADE

    @property
    def CPF(self):
        r"""Tax number of the person.
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def NASCIMENTO(self):
        r"""Date of birth.
        :rtype: str
        """
        return self._NASCIMENTO

    @NASCIMENTO.setter
    def NASCIMENTO(self, NASCIMENTO):
        self._NASCIMENTO = NASCIMENTO

    @property
    def MEMBERSHIP(self):
        r"""Membership status.
        :rtype: str
        """
        return self._MEMBERSHIP

    @MEMBERSHIP.setter
    def MEMBERSHIP(self, MEMBERSHIP):
        self._MEMBERSHIP = MEMBERSHIP

    @property
    def REGISTRO(self):
        r"""Registration number.
        :rtype: str
        """
        return self._REGISTRO

    @REGISTRO.setter
    def REGISTRO(self, REGISTRO):
        self._REGISTRO = REGISTRO

    @property
    def OBSERVATIONS(self):
        r"""Remarks.
        :rtype: str
        """
        return self._OBSERVATIONS

    @OBSERVATIONS.setter
    def OBSERVATIONS(self, OBSERVATIONS):
        self._OBSERVATIONS = OBSERVATIONS

    @property
    def IssueDate(self):
        r"""Issue date.
        :rtype: str
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def LOCAL(self):
        r"""Issuing location.
        :rtype: str
        """
        return self._LOCAL

    @LOCAL.setter
    def LOCAL(self, LOCAL):
        self._LOCAL = LOCAL

    @property
    def BackNumber(self):
        r"""Record number.
        :rtype: str
        """
        return self._BackNumber

    @BackNumber.setter
    def BackNumber(self, BackNumber):
        self._BackNumber = BackNumber

    @property
    def PortraitImage(self):
        r"""Specifies the avatar in base64 format.
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage


    def _deserialize(self, params):
        self._NOME = params.get("NOME")
        self._CatHab = params.get("CatHab")
        self._CNHNumber = params.get("CNHNumber")
        self._VALIDADE = params.get("VALIDADE")
        self._QUALIFICATION = params.get("QUALIFICATION")
        self._IDENTIDADE = params.get("IDENTIDADE")
        self._CPF = params.get("CPF")
        self._NASCIMENTO = params.get("NASCIMENTO")
        self._MEMBERSHIP = params.get("MEMBERSHIP")
        self._REGISTRO = params.get("REGISTRO")
        self._OBSERVATIONS = params.get("OBSERVATIONS")
        self._IssueDate = params.get("IssueDate")
        self._LOCAL = params.get("LOCAL")
        self._BackNumber = params.get("BackNumber")
        self._PortraitImage = params.get("PortraitImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrazilIDCardInfo(AbstractModel):
    r"""Specifies the identity card type in brazil.

    """

    def __init__(self):
        r"""
        :param _Nome: Name.
        :type Nome: str
        :param _MemberShip: Parent information.
        :type MemberShip: str
        :param _DataNascimento: Date of birth.
        :type DataNascimento: str
        :param _IssuingAgency: Issuing organization.
        :type IssuingAgency: str
        :param _Fatorrh: Specifies the blood type.
        :type Fatorrh: str
        :param _NaturalIDade: Birthplace.
        :type NaturalIDade: str
        :param _Observations: Remarks.
        :type Observations: str
        :param _CPF: CPF Type
        :type CPF: str
        :param _DNI: DNI Type
        :type DNI: str
        :param _RegistroGeral: Common registration.
        :type RegistroGeral: str
        :param _DispatchDate: Issue date. valid values: dd/mm/yyyy.
        :type DispatchDate: str
        :param _Registro: Address.
        :type Registro: str
        :param _PortraitImage: Specifies the avatar in Base64 format of the id card.
        :type PortraitImage: str
        :param _DocOrigem: Original identity information.
        :type DocOrigem: str
        """
        self._Nome = None
        self._MemberShip = None
        self._DataNascimento = None
        self._IssuingAgency = None
        self._Fatorrh = None
        self._NaturalIDade = None
        self._Observations = None
        self._CPF = None
        self._DNI = None
        self._RegistroGeral = None
        self._DispatchDate = None
        self._Registro = None
        self._PortraitImage = None
        self._DocOrigem = None

    @property
    def Nome(self):
        r"""Name.
        :rtype: str
        """
        return self._Nome

    @Nome.setter
    def Nome(self, Nome):
        self._Nome = Nome

    @property
    def MemberShip(self):
        r"""Parent information.
        :rtype: str
        """
        return self._MemberShip

    @MemberShip.setter
    def MemberShip(self, MemberShip):
        self._MemberShip = MemberShip

    @property
    def DataNascimento(self):
        r"""Date of birth.
        :rtype: str
        """
        return self._DataNascimento

    @DataNascimento.setter
    def DataNascimento(self, DataNascimento):
        self._DataNascimento = DataNascimento

    @property
    def IssuingAgency(self):
        r"""Issuing organization.
        :rtype: str
        """
        return self._IssuingAgency

    @IssuingAgency.setter
    def IssuingAgency(self, IssuingAgency):
        self._IssuingAgency = IssuingAgency

    @property
    def Fatorrh(self):
        r"""Specifies the blood type.
        :rtype: str
        """
        return self._Fatorrh

    @Fatorrh.setter
    def Fatorrh(self, Fatorrh):
        self._Fatorrh = Fatorrh

    @property
    def NaturalIDade(self):
        r"""Birthplace.
        :rtype: str
        """
        return self._NaturalIDade

    @NaturalIDade.setter
    def NaturalIDade(self, NaturalIDade):
        self._NaturalIDade = NaturalIDade

    @property
    def Observations(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Observations

    @Observations.setter
    def Observations(self, Observations):
        self._Observations = Observations

    @property
    def CPF(self):
        r"""CPF Type
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def DNI(self):
        r"""DNI Type
        :rtype: str
        """
        return self._DNI

    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI

    @property
    def RegistroGeral(self):
        r"""Common registration.
        :rtype: str
        """
        return self._RegistroGeral

    @RegistroGeral.setter
    def RegistroGeral(self, RegistroGeral):
        self._RegistroGeral = RegistroGeral

    @property
    def DispatchDate(self):
        r"""Issue date. valid values: dd/mm/yyyy.
        :rtype: str
        """
        return self._DispatchDate

    @DispatchDate.setter
    def DispatchDate(self, DispatchDate):
        self._DispatchDate = DispatchDate

    @property
    def Registro(self):
        r"""Address.
        :rtype: str
        """
        return self._Registro

    @Registro.setter
    def Registro(self, Registro):
        self._Registro = Registro

    @property
    def PortraitImage(self):
        r"""Specifies the avatar in Base64 format of the id card.
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def DocOrigem(self):
        r"""Original identity information.
        :rtype: str
        """
        return self._DocOrigem

    @DocOrigem.setter
    def DocOrigem(self, DocOrigem):
        self._DocOrigem = DocOrigem


    def _deserialize(self, params):
        self._Nome = params.get("Nome")
        self._MemberShip = params.get("MemberShip")
        self._DataNascimento = params.get("DataNascimento")
        self._IssuingAgency = params.get("IssuingAgency")
        self._Fatorrh = params.get("Fatorrh")
        self._NaturalIDade = params.get("NaturalIDade")
        self._Observations = params.get("Observations")
        self._CPF = params.get("CPF")
        self._DNI = params.get("DNI")
        self._RegistroGeral = params.get("RegistroGeral")
        self._DispatchDate = params.get("DispatchDate")
        self._Registro = params.get("Registro")
        self._PortraitImage = params.get("PortraitImage")
        self._DocOrigem = params.get("DocOrigem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrazilRNEInfo(AbstractModel):
    r"""BrazilRNEInfo

    """

    def __init__(self):
        r"""
        :param _RNE: RNE
        :type RNE: str
        :param _CLASSIFICATION: CLASSIFICAÇÃO(CLASSIFICATION)
        :type CLASSIFICATION: str
        :param _VALIDADE: VALIDADE
        :type VALIDADE: str
        :param _NOME: NOME
        :type NOME: str
        :param _Membership: FILIAÇÃO(MEMBERSHIP)
        :type Membership: str
        :param _NACIONALIDADE: NACIONALIDADE
        :type NACIONALIDADE: str
        :param _NATURALIDADE: NATURALIDADE(PAÍS)
        :type NATURALIDADE: str
        :param _IssuingAgency: ORGÃO EXPEDIDOR(IssuingAgency)
        :type IssuingAgency: str
        :param _DateOfBirth: DATA DE NASCIMENTO(DateOfBirth)
        :type DateOfBirth: str
        :param _Sex: SEXO
        :type Sex: str
        :param _EntryDate: DATA DE ENTRADA(EntryDate)
        :type EntryDate: str
        :param _VIA: VIA
        :type VIA: str
        :param _DispatchDate: DATA DE EXPEDIÇÃO(DispatchDate)
        :type DispatchDate: str
        :param _MRZ: MRZ
        :type MRZ: str
        :param _PortraitImage: PortraitImage
        :type PortraitImage: str
        """
        self._RNE = None
        self._CLASSIFICATION = None
        self._VALIDADE = None
        self._NOME = None
        self._Membership = None
        self._NACIONALIDADE = None
        self._NATURALIDADE = None
        self._IssuingAgency = None
        self._DateOfBirth = None
        self._Sex = None
        self._EntryDate = None
        self._VIA = None
        self._DispatchDate = None
        self._MRZ = None
        self._PortraitImage = None

    @property
    def RNE(self):
        r"""RNE
        :rtype: str
        """
        return self._RNE

    @RNE.setter
    def RNE(self, RNE):
        self._RNE = RNE

    @property
    def CLASSIFICATION(self):
        r"""CLASSIFICAÇÃO(CLASSIFICATION)
        :rtype: str
        """
        return self._CLASSIFICATION

    @CLASSIFICATION.setter
    def CLASSIFICATION(self, CLASSIFICATION):
        self._CLASSIFICATION = CLASSIFICATION

    @property
    def VALIDADE(self):
        r"""VALIDADE
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def NOME(self):
        r"""NOME
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def Membership(self):
        r"""FILIAÇÃO(MEMBERSHIP)
        :rtype: str
        """
        return self._Membership

    @Membership.setter
    def Membership(self, Membership):
        self._Membership = Membership

    @property
    def NACIONALIDADE(self):
        r"""NACIONALIDADE
        :rtype: str
        """
        return self._NACIONALIDADE

    @NACIONALIDADE.setter
    def NACIONALIDADE(self, NACIONALIDADE):
        self._NACIONALIDADE = NACIONALIDADE

    @property
    def NATURALIDADE(self):
        r"""NATURALIDADE(PAÍS)
        :rtype: str
        """
        return self._NATURALIDADE

    @NATURALIDADE.setter
    def NATURALIDADE(self, NATURALIDADE):
        self._NATURALIDADE = NATURALIDADE

    @property
    def IssuingAgency(self):
        r"""ORGÃO EXPEDIDOR(IssuingAgency)
        :rtype: str
        """
        return self._IssuingAgency

    @IssuingAgency.setter
    def IssuingAgency(self, IssuingAgency):
        self._IssuingAgency = IssuingAgency

    @property
    def DateOfBirth(self):
        r"""DATA DE NASCIMENTO(DateOfBirth)
        :rtype: str
        """
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def Sex(self):
        r"""SEXO
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def EntryDate(self):
        r"""DATA DE ENTRADA(EntryDate)
        :rtype: str
        """
        return self._EntryDate

    @EntryDate.setter
    def EntryDate(self, EntryDate):
        self._EntryDate = EntryDate

    @property
    def VIA(self):
        r"""VIA
        :rtype: str
        """
        return self._VIA

    @VIA.setter
    def VIA(self, VIA):
        self._VIA = VIA

    @property
    def DispatchDate(self):
        r"""DATA DE EXPEDIÇÃO(DispatchDate)
        :rtype: str
        """
        return self._DispatchDate

    @DispatchDate.setter
    def DispatchDate(self, DispatchDate):
        self._DispatchDate = DispatchDate

    @property
    def MRZ(self):
        r"""MRZ
        :rtype: str
        """
        return self._MRZ

    @MRZ.setter
    def MRZ(self, MRZ):
        self._MRZ = MRZ

    @property
    def PortraitImage(self):
        r"""PortraitImage
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage


    def _deserialize(self, params):
        self._RNE = params.get("RNE")
        self._CLASSIFICATION = params.get("CLASSIFICATION")
        self._VALIDADE = params.get("VALIDADE")
        self._NOME = params.get("NOME")
        self._Membership = params.get("Membership")
        self._NACIONALIDADE = params.get("NACIONALIDADE")
        self._NATURALIDADE = params.get("NATURALIDADE")
        self._IssuingAgency = params.get("IssuingAgency")
        self._DateOfBirth = params.get("DateOfBirth")
        self._Sex = params.get("Sex")
        self._EntryDate = params.get("EntryDate")
        self._VIA = params.get("VIA")
        self._DispatchDate = params.get("DispatchDate")
        self._MRZ = params.get("MRZ")
        self._PortraitImage = params.get("PortraitImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrazilRNMInfo(AbstractModel):
    r"""Document type for brazil RNM.

    """

    def __init__(self):
        r"""
        :param _SOBRENOME: SOBRENOME Type
        :type SOBRENOME: str
        :param _NOME: NOME Type
        :type NOME: str
        :param _DATADENASCIMENTO: DATA DE NASCIMENTO
        :type DATADENASCIMENTO: str
        :param _SEXO: SEXO F
        :type SEXO: str
        :param _MEMBERSHIP: FILIAÇÃO(MEMBERSHIP)
        :type MEMBERSHIP: str
        :param _NACIONALIDADE: NACIONALIDADE Type
        :type NACIONALIDADE: str
        :param _VALIDADE: VALIDADE Type
        :type VALIDADE: str
        :param _RNM: RNM Type
        :type RNM: str
        :param _CPF: CPF Type
        :type CPF: str
        :param _CLASSIFICATION: CLASSIFICAÇÃO(CLASSIFICATION)
        :type CLASSIFICATION: str
        :param _PRAZODERESIDENCIA: PRAZO DE RESIDENCIA
        :type PRAZODERESIDENCIA: str
        :param _ISSUANCE: EMISSÃO(ISSUANCE)
        :type ISSUANCE: str
        :param _AMPAROLEGAL: AMPARO LEGAL(LegalHelp)
        :type AMPAROLEGAL: str
        :param _MRZ: MRZCode
        :type MRZ: str
        :param _PortraitImage: Portrait Image
        :type PortraitImage: str
        :param _PortraitImageBack: PortraitImage(Back)
        :type PortraitImageBack: str
        """
        self._SOBRENOME = None
        self._NOME = None
        self._DATADENASCIMENTO = None
        self._SEXO = None
        self._MEMBERSHIP = None
        self._NACIONALIDADE = None
        self._VALIDADE = None
        self._RNM = None
        self._CPF = None
        self._CLASSIFICATION = None
        self._PRAZODERESIDENCIA = None
        self._ISSUANCE = None
        self._AMPAROLEGAL = None
        self._MRZ = None
        self._PortraitImage = None
        self._PortraitImageBack = None

    @property
    def SOBRENOME(self):
        r"""SOBRENOME Type
        :rtype: str
        """
        return self._SOBRENOME

    @SOBRENOME.setter
    def SOBRENOME(self, SOBRENOME):
        self._SOBRENOME = SOBRENOME

    @property
    def NOME(self):
        r"""NOME Type
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def DATADENASCIMENTO(self):
        r"""DATA DE NASCIMENTO
        :rtype: str
        """
        return self._DATADENASCIMENTO

    @DATADENASCIMENTO.setter
    def DATADENASCIMENTO(self, DATADENASCIMENTO):
        self._DATADENASCIMENTO = DATADENASCIMENTO

    @property
    def SEXO(self):
        r"""SEXO F
        :rtype: str
        """
        return self._SEXO

    @SEXO.setter
    def SEXO(self, SEXO):
        self._SEXO = SEXO

    @property
    def MEMBERSHIP(self):
        r"""FILIAÇÃO(MEMBERSHIP)
        :rtype: str
        """
        return self._MEMBERSHIP

    @MEMBERSHIP.setter
    def MEMBERSHIP(self, MEMBERSHIP):
        self._MEMBERSHIP = MEMBERSHIP

    @property
    def NACIONALIDADE(self):
        r"""NACIONALIDADE Type
        :rtype: str
        """
        return self._NACIONALIDADE

    @NACIONALIDADE.setter
    def NACIONALIDADE(self, NACIONALIDADE):
        self._NACIONALIDADE = NACIONALIDADE

    @property
    def VALIDADE(self):
        r"""VALIDADE Type
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def RNM(self):
        r"""RNM Type
        :rtype: str
        """
        return self._RNM

    @RNM.setter
    def RNM(self, RNM):
        self._RNM = RNM

    @property
    def CPF(self):
        r"""CPF Type
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def CLASSIFICATION(self):
        r"""CLASSIFICAÇÃO(CLASSIFICATION)
        :rtype: str
        """
        return self._CLASSIFICATION

    @CLASSIFICATION.setter
    def CLASSIFICATION(self, CLASSIFICATION):
        self._CLASSIFICATION = CLASSIFICATION

    @property
    def PRAZODERESIDENCIA(self):
        r"""PRAZO DE RESIDENCIA
        :rtype: str
        """
        return self._PRAZODERESIDENCIA

    @PRAZODERESIDENCIA.setter
    def PRAZODERESIDENCIA(self, PRAZODERESIDENCIA):
        self._PRAZODERESIDENCIA = PRAZODERESIDENCIA

    @property
    def ISSUANCE(self):
        r"""EMISSÃO(ISSUANCE)
        :rtype: str
        """
        return self._ISSUANCE

    @ISSUANCE.setter
    def ISSUANCE(self, ISSUANCE):
        self._ISSUANCE = ISSUANCE

    @property
    def AMPAROLEGAL(self):
        r"""AMPARO LEGAL(LegalHelp)
        :rtype: str
        """
        return self._AMPAROLEGAL

    @AMPAROLEGAL.setter
    def AMPAROLEGAL(self, AMPAROLEGAL):
        self._AMPAROLEGAL = AMPAROLEGAL

    @property
    def MRZ(self):
        r"""MRZCode
        :rtype: str
        """
        return self._MRZ

    @MRZ.setter
    def MRZ(self, MRZ):
        self._MRZ = MRZ

    @property
    def PortraitImage(self):
        r"""Portrait Image
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def PortraitImageBack(self):
        r"""PortraitImage(Back)
        :rtype: str
        """
        return self._PortraitImageBack

    @PortraitImageBack.setter
    def PortraitImageBack(self, PortraitImageBack):
        self._PortraitImageBack = PortraitImageBack


    def _deserialize(self, params):
        self._SOBRENOME = params.get("SOBRENOME")
        self._NOME = params.get("NOME")
        self._DATADENASCIMENTO = params.get("DATADENASCIMENTO")
        self._SEXO = params.get("SEXO")
        self._MEMBERSHIP = params.get("MEMBERSHIP")
        self._NACIONALIDADE = params.get("NACIONALIDADE")
        self._VALIDADE = params.get("VALIDADE")
        self._RNM = params.get("RNM")
        self._CPF = params.get("CPF")
        self._CLASSIFICATION = params.get("CLASSIFICATION")
        self._PRAZODERESIDENCIA = params.get("PRAZODERESIDENCIA")
        self._ISSUANCE = params.get("ISSUANCE")
        self._AMPAROLEGAL = params.get("AMPAROLEGAL")
        self._MRZ = params.get("MRZ")
        self._PortraitImage = params.get("PortraitImage")
        self._PortraitImageBack = params.get("PortraitImageBack")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigAdvanced(AbstractModel):
    r"""Supports single attribute configuration for templates.

    """

    def __init__(self):
        r"""
        :param _Scene: Single attribute configuration of a template.
        :type Scene: str
        """
        self._Scene = None

    @property
    def Scene(self):
        r"""Single attribute configuration of a template.
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    r"""Coordinates

    """

    def __init__(self):
        r"""
        :param _X: Horizontal coordinate
        :type X: int
        :param _Y: Vertical coordinate
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""Horizontal coordinate
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Vertical coordinate
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoordsItem(AbstractModel):
    r"""Detected coordinate recognition information.

    """

    def __init__(self):
        r"""
        :param _Polygon: Coordinates of four points in the image.
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _Coords: Coordinates of two points in the image.
        :type Coords: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self._Polygon = None
        self._Coords = None

    @property
    def Polygon(self):
        r"""Coordinates of four points in the image.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def Coords(self):
        r"""Coordinates of two points in the image.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        if params.get("Coords") is not None:
            self._Coords = ItemCoord()
            self._Coords._deserialize(params.get("Coords"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWordCoordPoint(AbstractModel):
    r"""Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner

    """

    def __init__(self):
        r"""
        :param _WordCoordinate: Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner
        :type WordCoordinate: list of Coord
        """
        self._WordCoordinate = None

    @property
    def WordCoordinate(self):
        r"""Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner
        :rtype: list of Coord
        """
        return self._WordCoordinate

    @WordCoordinate.setter
    def WordCoordinate(self, WordCoordinate):
        self._WordCoordinate = WordCoordinate


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self._WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self._WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWords(AbstractModel):
    r"""Information about a character detected, including the character itself and its confidence

    """

    def __init__(self):
        r"""
        :param _Confidence: Confidence. Value range: 0–100
        :type Confidence: int
        :param _Character: A possible character
        :type Character: str
        """
        self._Confidence = None
        self._Character = None

    @property
    def Confidence(self):
        r"""Confidence. Value range: 0–100
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Character(self):
        r"""A possible character
        :rtype: str
        """
        return self._Character

    @Character.setter
    def Character(self, Character):
        self._Character = Character


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractDocMultiRequest(AbstractModel):
    r"""ExtractDocMulti request structure.

    """

    def __init__(self):
        r"""
        :param _ImageUrl: The Url address of the image. supported image formats: PNG, JPG, JPEG, WORD, EXCEL. GIF format is not currently supported. supported image size: no more than 10M after Base64 encoding. image download time should not exceed 3 seconds. supported image pixels: between 20-10000px. images stored in tencent cloud's Url ensure higher download speed and stability. it is recommended to store images in tencent cloud. the speed and stability of non-tencent cloud storage urls may be impacted.
        :type ImageUrl: str
        :param _ImageBase64: The Base64 value of the image. supported image formats: PNG, JPG, JPEG, WORD, EXCEL. GIF format is not currently supported. supported image size: no more than 10M after encoding the downloaded image with Base64. image download time: no more than 3 seconds. supported image pixels: between 20-10000px. either ImageUrl or ImageBase64 must be provided. if both are provided, only use ImageUrl.
        :type ImageBase64: str
        :param _PdfPageNumber: Specifies the page number of the PDF to be recognized. only single page recognition is supported. valid when uploading a PDF file with the IsPdf parameter set to true. default value is the first 3 pages.
        :type PdfPageNumber: int
        :param _ItemNames: Specifies the field names to be returned by the customized structuring feature. for example, if the customer wants to add the recognition result of two fields, name and gender, manually input ItemNames=["name","gender"].
        :type ItemNames: list of str
        :param _ItemNamesShowMode: true: only custom field.
False: default value field + custom field.
Default true.
        :type ItemNamesShowMode: bool
        :param _ReturnFullText: Whether the full-text field recognition is enabled.
        :type ReturnFullText: bool
        :param _ConfigId: Configuration ID support: 
-- General
-- InvoiceEng
-- WayBillEng
-- CustomsDeclaration
-- WeightNote
-- MedicalMeter
-- BillOfLading
-- EntrustmentBook
-- Statement
-- BookingConfirmation
-- AirWayBill
-- Table
-- SteelLabel
-- CarInsurance
-- MultiRealEstateCertificate
-- MultiRealEstateMaterial
-- HongKongUtilityBill
-- OverseasCheques
-- RegistrationCertificate
-- GridPhoto
-- SignaturePage
        :type ConfigId: str
        :param _EnableCoord: Whether the full-text field coordinate value recognition is enabled.
        :type EnableCoord: bool
        :param _OutputParentKey: Whether parent-child key recognition is enabled. the option is selected by default.
        :type OutputParentKey: bool
        :param _ConfigAdvanced: Single attribute configuration of a template.
        :type ConfigAdvanced: :class:`tencentcloud.ocr.v20181119.models.ConfigAdvanced`
        :param _OutputLanguage: When cn, the added key is chinese.  
When set to en, the added key is english.
        :type OutputLanguage: str
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._PdfPageNumber = None
        self._ItemNames = None
        self._ItemNamesShowMode = None
        self._ReturnFullText = None
        self._ConfigId = None
        self._EnableCoord = None
        self._OutputParentKey = None
        self._ConfigAdvanced = None
        self._OutputLanguage = None

    @property
    def ImageUrl(self):
        r"""The Url address of the image. supported image formats: PNG, JPG, JPEG, WORD, EXCEL. GIF format is not currently supported. supported image size: no more than 10M after Base64 encoding. image download time should not exceed 3 seconds. supported image pixels: between 20-10000px. images stored in tencent cloud's Url ensure higher download speed and stability. it is recommended to store images in tencent cloud. the speed and stability of non-tencent cloud storage urls may be impacted.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. supported image formats: PNG, JPG, JPEG, WORD, EXCEL. GIF format is not currently supported. supported image size: no more than 10M after encoding the downloaded image with Base64. image download time: no more than 3 seconds. supported image pixels: between 20-10000px. either ImageUrl or ImageBase64 must be provided. if both are provided, only use ImageUrl.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def PdfPageNumber(self):
        r"""Specifies the page number of the PDF to be recognized. only single page recognition is supported. valid when uploading a PDF file with the IsPdf parameter set to true. default value is the first 3 pages.
        :rtype: int
        """
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ItemNames(self):
        r"""Specifies the field names to be returned by the customized structuring feature. for example, if the customer wants to add the recognition result of two fields, name and gender, manually input ItemNames=["name","gender"].
        :rtype: list of str
        """
        return self._ItemNames

    @ItemNames.setter
    def ItemNames(self, ItemNames):
        self._ItemNames = ItemNames

    @property
    def ItemNamesShowMode(self):
        r"""true: only custom field.
False: default value field + custom field.
Default true.
        :rtype: bool
        """
        return self._ItemNamesShowMode

    @ItemNamesShowMode.setter
    def ItemNamesShowMode(self, ItemNamesShowMode):
        self._ItemNamesShowMode = ItemNamesShowMode

    @property
    def ReturnFullText(self):
        r"""Whether the full-text field recognition is enabled.
        :rtype: bool
        """
        return self._ReturnFullText

    @ReturnFullText.setter
    def ReturnFullText(self, ReturnFullText):
        self._ReturnFullText = ReturnFullText

    @property
    def ConfigId(self):
        r"""Configuration ID support: 
-- General
-- InvoiceEng
-- WayBillEng
-- CustomsDeclaration
-- WeightNote
-- MedicalMeter
-- BillOfLading
-- EntrustmentBook
-- Statement
-- BookingConfirmation
-- AirWayBill
-- Table
-- SteelLabel
-- CarInsurance
-- MultiRealEstateCertificate
-- MultiRealEstateMaterial
-- HongKongUtilityBill
-- OverseasCheques
-- RegistrationCertificate
-- GridPhoto
-- SignaturePage
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def EnableCoord(self):
        r"""Whether the full-text field coordinate value recognition is enabled.
        :rtype: bool
        """
        return self._EnableCoord

    @EnableCoord.setter
    def EnableCoord(self, EnableCoord):
        self._EnableCoord = EnableCoord

    @property
    def OutputParentKey(self):
        r"""Whether parent-child key recognition is enabled. the option is selected by default.
        :rtype: bool
        """
        return self._OutputParentKey

    @OutputParentKey.setter
    def OutputParentKey(self, OutputParentKey):
        self._OutputParentKey = OutputParentKey

    @property
    def ConfigAdvanced(self):
        r"""Single attribute configuration of a template.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ConfigAdvanced`
        """
        return self._ConfigAdvanced

    @ConfigAdvanced.setter
    def ConfigAdvanced(self, ConfigAdvanced):
        self._ConfigAdvanced = ConfigAdvanced

    @property
    def OutputLanguage(self):
        r"""When cn, the added key is chinese.  
When set to en, the added key is english.
        :rtype: str
        """
        return self._OutputLanguage

    @OutputLanguage.setter
    def OutputLanguage(self, OutputLanguage):
        self._OutputLanguage = OutputLanguage


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._ItemNames = params.get("ItemNames")
        self._ItemNamesShowMode = params.get("ItemNamesShowMode")
        self._ReturnFullText = params.get("ReturnFullText")
        self._ConfigId = params.get("ConfigId")
        self._EnableCoord = params.get("EnableCoord")
        self._OutputParentKey = params.get("OutputParentKey")
        if params.get("ConfigAdvanced") is not None:
            self._ConfigAdvanced = ConfigAdvanced()
            self._ConfigAdvanced._deserialize(params.get("ConfigAdvanced"))
        self._OutputLanguage = params.get("OutputLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractDocMultiResponse(AbstractModel):
    r"""ExtractDocMulti response structure.

    """

    def __init__(self):
        r"""
        :param _Angle: Image rotation angle (angle system). the text's horizontal direction is 0. clockwise is positive; counterclockwise is negative.
        :type Angle: float
        :param _StructuralList: Configures the structured text info.
        :type StructuralList: list of GroupInfo
        :param _WordList: Restore text information.
        :type WordList: list of WordItem
        :param _TokenNum: Number of sample identification fields.
        :type TokenNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Angle = None
        self._StructuralList = None
        self._WordList = None
        self._TokenNum = None
        self._RequestId = None

    @property
    def Angle(self):
        r"""Image rotation angle (angle system). the text's horizontal direction is 0. clockwise is positive; counterclockwise is negative.
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def StructuralList(self):
        r"""Configures the structured text info.
        :rtype: list of GroupInfo
        """
        return self._StructuralList

    @StructuralList.setter
    def StructuralList(self, StructuralList):
        self._StructuralList = StructuralList

    @property
    def WordList(self):
        r"""Restore text information.
        :rtype: list of WordItem
        """
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def TokenNum(self):
        r"""Number of sample identification fields.
        :rtype: int
        """
        return self._TokenNum

    @TokenNum.setter
    def TokenNum(self, TokenNum):
        self._TokenNum = TokenNum

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        if params.get("StructuralList") is not None:
            self._StructuralList = []
            for item in params.get("StructuralList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._StructuralList.append(obj)
        if params.get("WordList") is not None:
            self._WordList = []
            for item in params.get("WordList"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordList.append(obj)
        self._TokenNum = params.get("TokenNum")
        self._RequestId = params.get("RequestId")


class GeneralAccurateOCRRequest(AbstractModel):
    r"""GeneralAccurateOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: <p>The Base64 value of the image/PDF. The image size after Base64 encoding must be no more than 10M, with a resolution of 600*800 or higher recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.</p>
        :type ImageBase64: str
        :param _ImageUrl: URL address of image. 
The image cannot exceed 10 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _EnableDetectSplit: <p>Whether to enable original image slicing detection. Once enabled, it improves recognition accuracy in scenarios where "the overall image area is large but the single character occupies a small proportion" (for example: exam paper). Default: disabled. Note: Only supported when ConfigID is configured as OCR.</p>
        :type EnableDetectSplit: bool
        :param _IsPdf: <p>Whether PDF recognition is enabled. The default value is false. Once enabled, it can simultaneously support image and PDF recognition.</p>
        :type IsPdf: bool
        :param _PdfPageNumber: <p>The corresponding page number of the PDF page to be recognized. Only single page recognition is supported. Valid at that time when the upload file is a PDF and the IsPdf parameter value is true. The default value is 1.</p>
        :type PdfPageNumber: int
        :param _EnableDetectText: <p>Text Detection Switch, true by default. Set to false to directly perform single-line recognition, suitable for image scenarios containing only forward single-line text.</p>
        :type EnableDetectText: bool
        :param _ConfigID: <p>Configuration ID support: OCR -- common scenarios MulOCR -- multilingual scenario. Default value: OCR.</p>
        :type ConfigID: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._EnableDetectSplit = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._EnableDetectText = None
        self._ConfigID = None

    @property
    def ImageBase64(self):
        r"""<p>The Base64 value of the image/PDF. The image size after Base64 encoding must be no more than 10M, with a resolution of 600*800 or higher recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.</p>
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of image. 
The image cannot exceed 10 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def EnableDetectSplit(self):
        r"""<p>Whether to enable original image slicing detection. Once enabled, it improves recognition accuracy in scenarios where "the overall image area is large but the single character occupies a small proportion" (for example: exam paper). Default: disabled. Note: Only supported when ConfigID is configured as OCR.</p>
        :rtype: bool
        """
        return self._EnableDetectSplit

    @EnableDetectSplit.setter
    def EnableDetectSplit(self, EnableDetectSplit):
        self._EnableDetectSplit = EnableDetectSplit

    @property
    def IsPdf(self):
        r"""<p>Whether PDF recognition is enabled. The default value is false. Once enabled, it can simultaneously support image and PDF recognition.</p>
        :rtype: bool
        """
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        r"""<p>The corresponding page number of the PDF page to be recognized. Only single page recognition is supported. Valid at that time when the upload file is a PDF and the IsPdf parameter value is true. The default value is 1.</p>
        :rtype: int
        """
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def EnableDetectText(self):
        r"""<p>Text Detection Switch, true by default. Set to false to directly perform single-line recognition, suitable for image scenarios containing only forward single-line text.</p>
        :rtype: bool
        """
        return self._EnableDetectText

    @EnableDetectText.setter
    def EnableDetectText(self, EnableDetectText):
        self._EnableDetectText = EnableDetectText

    @property
    def ConfigID(self):
        r"""<p>Configuration ID support: OCR -- common scenarios MulOCR -- multilingual scenario. Default value: OCR.</p>
        :rtype: str
        """
        return self._ConfigID

    @ConfigID.setter
    def ConfigID(self, ConfigID):
        self._ConfigID = ConfigID


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._EnableDetectSplit = params.get("EnableDetectSplit")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._EnableDetectText = params.get("EnableDetectText")
        self._ConfigID = params.get("ConfigID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRResponse(AbstractModel):
    r"""GeneralAccurateOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TextDetections: <p>Detected text information, including row content, confidence degree, text line coordinate, and rotation corrected coordinate. For specific content, please click the left-side link.</p>
        :type TextDetections: list of TextDetection
        :param _Angel: Image rotation angle in degrees. Zero degrees: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :type Angel: float
        :param _Angle: <p>Image rotation angle (angle system), the text's horizontal direction is Zero degrees; clockwise is positive, counterclockwise is negative. Click to view <a href="https://www.tencentcloud.com/document/product/866/45139?from_cn_redirect=1">How to correct tilt text</a></p>
        :type Angle: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._Angle = None
        self._RequestId = None

    @property
    def TextDetections(self):
        r"""<p>Detected text information, including row content, confidence degree, text line coordinate, and rotation corrected coordinate. For specific content, please click the left-side link.</p>
        :rtype: list of TextDetection
        """
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        r"""Image rotation angle in degrees. Zero degrees: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :rtype: float
        """
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        self._Angel = Angel

    @property
    def Angle(self):
        r"""<p>Image rotation angle (angle system), the text's horizontal direction is Zero degrees; clockwise is positive, counterclockwise is negative. Click to view <a href="https://www.tencentcloud.com/document/product/866/45139?from_cn_redirect=1">How to correct tilt text</a></p>
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angel = params.get("Angel")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    r"""GeneralBasicOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded value of image/PDF.
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
        :type ImageBase64: str
        :param _ImageUrl: URL address of image/PDF. (This field is not supported outside Chinese mainland)
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _Scene: Reserved field.
        :type Scene: str
        :param _LanguageType: Language to recognize
The language can be automatically recognized or manually specified. Chinese-English mix (`zh`) is selected by default. Mixed characters in English and each supported language can be recognized together.
Valid values:
`zh`: Chinese-English mix
`zh_rare`: supports letters, digits, rare Chinese characters, Traditional Chinese characters, special characters, etc.
`auto`
`mix`: language mix
`jap`: Japanese
`kor`: Korean
`spa`: Spanish
`fre`: French
`ger`: German
`por`: Portuguese
`vie`: Vietnamese
`may`: Malay
`rus`: Russian
`ita`: Italian
`hol`: Dutch
`swe`: Swedish
`fin`: Finnish
`dan`: Danish
`nor`: Norwegian
`hun`: Hungarian
`tha`: Thai
`hi`: Hindi
`ara`: Arabic
        :type LanguageType: str
        :param _IsPdf: Whether to enable PDF recognition. Default value: false. After this feature is enabled, both images and PDF files can be recognized at the same time.
        :type IsPdf: bool
        :param _PdfPageNumber: Page number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of the `IsPdf` parameter is `true`. Default value: 1.
        :type PdfPageNumber: int
        :param _IsWords: Whether to return the character information. Default value: `false`
        :type IsWords: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Scene = None
        self._LanguageType = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._IsWords = None

    @property
    def ImageBase64(self):
        r"""Base64-encoded value of image/PDF.
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of image/PDF. (This field is not supported outside Chinese mainland)
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Scene(self):
        r"""Reserved field.
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LanguageType(self):
        r"""Language to recognize
The language can be automatically recognized or manually specified. Chinese-English mix (`zh`) is selected by default. Mixed characters in English and each supported language can be recognized together.
Valid values:
`zh`: Chinese-English mix
`zh_rare`: supports letters, digits, rare Chinese characters, Traditional Chinese characters, special characters, etc.
`auto`
`mix`: language mix
`jap`: Japanese
`kor`: Korean
`spa`: Spanish
`fre`: French
`ger`: German
`por`: Portuguese
`vie`: Vietnamese
`may`: Malay
`rus`: Russian
`ita`: Italian
`hol`: Dutch
`swe`: Swedish
`fin`: Finnish
`dan`: Danish
`nor`: Norwegian
`hun`: Hungarian
`tha`: Thai
`hi`: Hindi
`ara`: Arabic
        :rtype: str
        """
        return self._LanguageType

    @LanguageType.setter
    def LanguageType(self, LanguageType):
        self._LanguageType = LanguageType

    @property
    def IsPdf(self):
        r"""Whether to enable PDF recognition. Default value: false. After this feature is enabled, both images and PDF files can be recognized at the same time.
        :rtype: bool
        """
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        r"""Page number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of the `IsPdf` parameter is `true`. Default value: 1.
        :rtype: int
        """
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def IsWords(self):
        r"""Whether to return the character information. Default value: `false`
        :rtype: bool
        """
        return self._IsWords

    @IsWords.setter
    def IsWords(self, IsWords):
        self._IsWords = IsWords


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Scene = params.get("Scene")
        self._LanguageType = params.get("LanguageType")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._IsWords = params.get("IsWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralBasicOCRResponse(AbstractModel):
    r"""GeneralBasicOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TextDetections: Information of recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :type TextDetections: list of TextDetection
        :param _Language: Detected language. For more information on the supported languages, please see the description of the `LanguageType` input parameter.
        :type Language: str
        :param _Angel: Image rotation angle in degrees. 0: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :type Angel: float
        :param _PdfPageSize: Total number of PDF pages to be returned if the image is a PDF. Default value: 0.
        :type PdfPageSize: int
        :param _Angle: 
        :type Angle: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TextDetections = None
        self._Language = None
        self._Angel = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def TextDetections(self):
        r"""Information of recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :rtype: list of TextDetection
        """
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Language(self):
        r"""Detected language. For more information on the supported languages, please see the description of the `LanguageType` input parameter.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Angel(self):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        r"""Image rotation angle in degrees. 0: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :rtype: float
        """
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        self._Angel = Angel

    @property
    def PdfPageSize(self):
        r"""Total number of PDF pages to be returned if the image is a PDF. Default value: 0.
        :rtype: int
        """
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        r"""
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Language = params.get("Language")
        self._Angel = params.get("Angel")
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class GeneralCard(AbstractModel):
    r"""General card certificate information.

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: ID number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _PersonalNumber: Personal number. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type PersonalNumber: str
        :param _FullName: Full name on the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _FullNameLocal: Full name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullNameLocal: str
        :param _FirstName: First name or given name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _FirstNameLocal: First name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstNameLocal: str
        :param _MiddleName: Middle name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MiddleName: str
        :param _MiddleNameLocal: Middle name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MiddleNameLocal: str
        :param _LastName: Last name or surname.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _LastNameLocal: Last name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastNameLocal: str
        :param _Sex: Gender on the document.
- M: man.
- F: woman.
- X: other gender identity.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Birthday: Date of birth.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _BirthPlace: Birth place.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BirthPlace: str
        :param _IssuedDate: Issue date.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _IssuedAuthority: Issuing authority.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedAuthority: str
        :param _IssuedPlace: Place of issue.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedPlace: str
        :param _IssuedCountry: Issuing country.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountry: str
        :param _IssuedCountryCode: Country code of issue, ISO Alpha-3 format.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountryCode: str
        :param _ExpirationDate: Expiry date.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _MRZLine1: First line of the Machine Readable Zone (MRZ).
Note: This field may return null, indicating that no valid values can be obtained.
        :type MRZLine1: str
        :param _MRZLine2: Second line of the Machine Readable Zone (MRZ).
Note: This field may return null, indicating that no valid values can be obtained.
        :type MRZLine2: str
        :param _Nationality: Document nationality, following ISO 3166 country coding specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _Address: Address information on the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.AddressInfo`
        :param _Religion: Religion (if displayed on the document).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Religion: str
        :param _Type: Type of document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _BloodType: Blood type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BloodType: str
        :param _Height: Height.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Height: str
        :param _Weight: Weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: str
        :param _VehicleClass: Vehicle class authorized on the driver license (e.g., A, B, C).
Note: This field may return null, indicating that no valid values can be obtained.
        :type VehicleClass: str
        :param _Restrictions: Restrictions on the driver license.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Restrictions: str
        :param _Endorsement: Endorsements or additional records on the driver license.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Endorsement: str
        :param _Others: Supplementary fields (varies by document type).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Others: str
        :param _PassportCodeFirst: First line of the passport MRZ (Machine Readable Zone).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeFirst: str
        :param _PassportCodeSecond: Second line of the passport MRZ (Machine Readable Zone).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeSecond: str
        :param _DueDate: Expiry date.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DueDate: str
        :param _Age: Age. 0 means no valid info.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Age: str
        :param _RegistrationNumber: Registration number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistrationNumber: str
        """
        self._LicenseNumber = None
        self._PersonalNumber = None
        self._FullName = None
        self._FullNameLocal = None
        self._FirstName = None
        self._FirstNameLocal = None
        self._MiddleName = None
        self._MiddleNameLocal = None
        self._LastName = None
        self._LastNameLocal = None
        self._Sex = None
        self._Birthday = None
        self._BirthPlace = None
        self._IssuedDate = None
        self._IssuedAuthority = None
        self._IssuedPlace = None
        self._IssuedCountry = None
        self._IssuedCountryCode = None
        self._ExpirationDate = None
        self._MRZLine1 = None
        self._MRZLine2 = None
        self._Nationality = None
        self._Address = None
        self._Religion = None
        self._Type = None
        self._BloodType = None
        self._Height = None
        self._Weight = None
        self._VehicleClass = None
        self._Restrictions = None
        self._Endorsement = None
        self._Others = None
        self._PassportCodeFirst = None
        self._PassportCodeSecond = None
        self._DueDate = None
        self._Age = None
        self._RegistrationNumber = None

    @property
    def LicenseNumber(self):
        r"""ID number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def PersonalNumber(self):
        r"""Personal number. 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PersonalNumber

    @PersonalNumber.setter
    def PersonalNumber(self, PersonalNumber):
        self._PersonalNumber = PersonalNumber

    @property
    def FullName(self):
        r"""Full name on the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def FullNameLocal(self):
        r"""Full name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FullNameLocal

    @FullNameLocal.setter
    def FullNameLocal(self, FullNameLocal):
        self._FullNameLocal = FullNameLocal

    @property
    def FirstName(self):
        r"""First name or given name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def FirstNameLocal(self):
        r"""First name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FirstNameLocal

    @FirstNameLocal.setter
    def FirstNameLocal(self, FirstNameLocal):
        self._FirstNameLocal = FirstNameLocal

    @property
    def MiddleName(self):
        r"""Middle name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def MiddleNameLocal(self):
        r"""Middle name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MiddleNameLocal

    @MiddleNameLocal.setter
    def MiddleNameLocal(self, MiddleNameLocal):
        self._MiddleNameLocal = MiddleNameLocal

    @property
    def LastName(self):
        r"""Last name or surname.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def LastNameLocal(self):
        r"""Last name in local language.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastNameLocal

    @LastNameLocal.setter
    def LastNameLocal(self, LastNameLocal):
        self._LastNameLocal = LastNameLocal

    @property
    def Sex(self):
        r"""Gender on the document.
- M: man.
- F: woman.
- X: other gender identity.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        r"""Date of birth.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def BirthPlace(self):
        r"""Birth place.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def IssuedDate(self):
        r"""Issue date.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def IssuedAuthority(self):
        r"""Issuing authority.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IssuedAuthority

    @IssuedAuthority.setter
    def IssuedAuthority(self, IssuedAuthority):
        self._IssuedAuthority = IssuedAuthority

    @property
    def IssuedPlace(self):
        r"""Place of issue.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IssuedPlace

    @IssuedPlace.setter
    def IssuedPlace(self, IssuedPlace):
        self._IssuedPlace = IssuedPlace

    @property
    def IssuedCountry(self):
        r"""Issuing country.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry

    @property
    def IssuedCountryCode(self):
        r"""Country code of issue, ISO Alpha-3 format.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IssuedCountryCode

    @IssuedCountryCode.setter
    def IssuedCountryCode(self, IssuedCountryCode):
        self._IssuedCountryCode = IssuedCountryCode

    @property
    def ExpirationDate(self):
        r"""Expiry date.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def MRZLine1(self):
        r"""First line of the Machine Readable Zone (MRZ).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MRZLine1

    @MRZLine1.setter
    def MRZLine1(self, MRZLine1):
        self._MRZLine1 = MRZLine1

    @property
    def MRZLine2(self):
        r"""Second line of the Machine Readable Zone (MRZ).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MRZLine2

    @MRZLine2.setter
    def MRZLine2(self, MRZLine2):
        self._MRZLine2 = MRZLine2

    @property
    def Nationality(self):
        r"""Document nationality, following ISO 3166 country coding specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Address(self):
        r"""Address information on the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.AddressInfo`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Religion(self):
        r"""Religion (if displayed on the document).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Religion

    @Religion.setter
    def Religion(self, Religion):
        self._Religion = Religion

    @property
    def Type(self):
        r"""Type of document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BloodType(self):
        r"""Blood type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BloodType

    @BloodType.setter
    def BloodType(self, BloodType):
        self._BloodType = BloodType

    @property
    def Height(self):
        r"""Height.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Weight(self):
        r"""Weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def VehicleClass(self):
        r"""Vehicle class authorized on the driver license (e.g., A, B, C).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VehicleClass

    @VehicleClass.setter
    def VehicleClass(self, VehicleClass):
        self._VehicleClass = VehicleClass

    @property
    def Restrictions(self):
        r"""Restrictions on the driver license.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Restrictions

    @Restrictions.setter
    def Restrictions(self, Restrictions):
        self._Restrictions = Restrictions

    @property
    def Endorsement(self):
        r"""Endorsements or additional records on the driver license.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Endorsement

    @Endorsement.setter
    def Endorsement(self, Endorsement):
        self._Endorsement = Endorsement

    @property
    def Others(self):
        r"""Supplementary fields (varies by document type).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Others

    @Others.setter
    def Others(self, Others):
        self._Others = Others

    @property
    def PassportCodeFirst(self):
        warnings.warn("parameter `PassportCodeFirst` is deprecated", DeprecationWarning) 

        r"""First line of the passport MRZ (Machine Readable Zone).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PassportCodeFirst

    @PassportCodeFirst.setter
    def PassportCodeFirst(self, PassportCodeFirst):
        warnings.warn("parameter `PassportCodeFirst` is deprecated", DeprecationWarning) 

        self._PassportCodeFirst = PassportCodeFirst

    @property
    def PassportCodeSecond(self):
        warnings.warn("parameter `PassportCodeSecond` is deprecated", DeprecationWarning) 

        r"""Second line of the passport MRZ (Machine Readable Zone).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PassportCodeSecond

    @PassportCodeSecond.setter
    def PassportCodeSecond(self, PassportCodeSecond):
        warnings.warn("parameter `PassportCodeSecond` is deprecated", DeprecationWarning) 

        self._PassportCodeSecond = PassportCodeSecond

    @property
    def DueDate(self):
        warnings.warn("parameter `DueDate` is deprecated", DeprecationWarning) 

        r"""Expiry date.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DueDate

    @DueDate.setter
    def DueDate(self, DueDate):
        warnings.warn("parameter `DueDate` is deprecated", DeprecationWarning) 

        self._DueDate = DueDate

    @property
    def Age(self):
        warnings.warn("parameter `Age` is deprecated", DeprecationWarning) 

        r"""Age. 0 means no valid info.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        warnings.warn("parameter `Age` is deprecated", DeprecationWarning) 

        self._Age = Age

    @property
    def RegistrationNumber(self):
        warnings.warn("parameter `RegistrationNumber` is deprecated", DeprecationWarning) 

        r"""Registration number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        warnings.warn("parameter `RegistrationNumber` is deprecated", DeprecationWarning) 

        self._RegistrationNumber = RegistrationNumber


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._PersonalNumber = params.get("PersonalNumber")
        self._FullName = params.get("FullName")
        self._FullNameLocal = params.get("FullNameLocal")
        self._FirstName = params.get("FirstName")
        self._FirstNameLocal = params.get("FirstNameLocal")
        self._MiddleName = params.get("MiddleName")
        self._MiddleNameLocal = params.get("MiddleNameLocal")
        self._LastName = params.get("LastName")
        self._LastNameLocal = params.get("LastNameLocal")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._BirthPlace = params.get("BirthPlace")
        self._IssuedDate = params.get("IssuedDate")
        self._IssuedAuthority = params.get("IssuedAuthority")
        self._IssuedPlace = params.get("IssuedPlace")
        self._IssuedCountry = params.get("IssuedCountry")
        self._IssuedCountryCode = params.get("IssuedCountryCode")
        self._ExpirationDate = params.get("ExpirationDate")
        self._MRZLine1 = params.get("MRZLine1")
        self._MRZLine2 = params.get("MRZLine2")
        self._Nationality = params.get("Nationality")
        if params.get("Address") is not None:
            self._Address = AddressInfo()
            self._Address._deserialize(params.get("Address"))
        self._Religion = params.get("Religion")
        self._Type = params.get("Type")
        self._BloodType = params.get("BloodType")
        self._Height = params.get("Height")
        self._Weight = params.get("Weight")
        self._VehicleClass = params.get("VehicleClass")
        self._Restrictions = params.get("Restrictions")
        self._Endorsement = params.get("Endorsement")
        self._Others = params.get("Others")
        self._PassportCodeFirst = params.get("PassportCodeFirst")
        self._PassportCodeSecond = params.get("PassportCodeSecond")
        self._DueDate = params.get("DueDate")
        self._Age = params.get("Age")
        self._RegistrationNumber = params.get("RegistrationNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCardVerificationExternalResultRequest(AbstractModel):
    r"""GetCardVerificationExternalResult request structure.

    """

    def __init__(self):
        r"""
        :param _CardVerificationToken: Initiates the recognition interface and returns a unique token.
        :type CardVerificationToken: str
        """
        self._CardVerificationToken = None

    @property
    def CardVerificationToken(self):
        r"""Initiates the recognition interface and returns a unique token.
        :rtype: str
        """
        return self._CardVerificationToken

    @CardVerificationToken.setter
    def CardVerificationToken(self, CardVerificationToken):
        self._CardVerificationToken = CardVerificationToken


    def _deserialize(self, params):
        self._CardVerificationToken = params.get("CardVerificationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCardVerificationExternalResultResponse(AbstractModel):
    r"""GetCardVerificationExternalResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Verification status. Valid values: 
PROCESSING
ABNORMAL
COMPLETED
        :type Status: str
        :param _WarnInfo: Anti-counterfeiting information. 
- ScreenshotSuspected: The image is a screenshot.
- RetakeSuspected: The image is taken from another screen.
- PaperCopy: The image is a black and white, or color photocopy.
- FakeSuspected: The image of the card, or the information on the card has been edited or altered.
- PoorImageQuality: The image is bad quality.
- InformationVerificationFailed: Information verification failed based on OCR recognition results
- TooManyCards: Multiple cards present in the frame.
- IncompleteCard: Captured document is incomplete.
- OtherWarning: Document's authenticity is not verified for various reasons.

Note: This field may return null, indicating that no valid values can be obtained.
        :type WarnInfo: list of str
        :param _Nationality: Country or region of the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _CardInfo: Front-side document recognition results. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardInfo: :class:`tencentcloud.ocr.v20181119.models.GeneralCard`
        :param _BackCardInfo: Back-side document recognition results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackCardInfo: :class:`tencentcloud.ocr.v20181119.models.GeneralCard`
        :param _CardVerificationToken: The token passed in the input parameters.
        :type CardVerificationToken: str
        :param _HeadImageBase64: Base64-encoded head image from the document. If ReturnHeadImage was set to false or not provided in the request, this field returns an empty string. If ReturnHeadImage was set to true and this field returns an empty string, indicating a failure to extract the head image extraction failed. Please check the input document photo.
        :type HeadImageBase64: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._WarnInfo = None
        self._Nationality = None
        self._CardInfo = None
        self._BackCardInfo = None
        self._CardVerificationToken = None
        self._HeadImageBase64 = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Verification status. Valid values: 
PROCESSING
ABNORMAL
COMPLETED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WarnInfo(self):
        r"""Anti-counterfeiting information. 
- ScreenshotSuspected: The image is a screenshot.
- RetakeSuspected: The image is taken from another screen.
- PaperCopy: The image is a black and white, or color photocopy.
- FakeSuspected: The image of the card, or the information on the card has been edited or altered.
- PoorImageQuality: The image is bad quality.
- InformationVerificationFailed: Information verification failed based on OCR recognition results
- TooManyCards: Multiple cards present in the frame.
- IncompleteCard: Captured document is incomplete.
- OtherWarning: Document's authenticity is not verified for various reasons.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._WarnInfo

    @WarnInfo.setter
    def WarnInfo(self, WarnInfo):
        self._WarnInfo = WarnInfo

    @property
    def Nationality(self):
        warnings.warn("parameter `Nationality` is deprecated", DeprecationWarning) 

        r"""Country or region of the document.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        warnings.warn("parameter `Nationality` is deprecated", DeprecationWarning) 

        self._Nationality = Nationality

    @property
    def CardInfo(self):
        r"""Front-side document recognition results. 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralCard`
        """
        return self._CardInfo

    @CardInfo.setter
    def CardInfo(self, CardInfo):
        self._CardInfo = CardInfo

    @property
    def BackCardInfo(self):
        r"""Back-side document recognition results.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralCard`
        """
        return self._BackCardInfo

    @BackCardInfo.setter
    def BackCardInfo(self, BackCardInfo):
        self._BackCardInfo = BackCardInfo

    @property
    def CardVerificationToken(self):
        r"""The token passed in the input parameters.
        :rtype: str
        """
        return self._CardVerificationToken

    @CardVerificationToken.setter
    def CardVerificationToken(self, CardVerificationToken):
        self._CardVerificationToken = CardVerificationToken

    @property
    def HeadImageBase64(self):
        r"""Base64-encoded head image from the document. If ReturnHeadImage was set to false or not provided in the request, this field returns an empty string. If ReturnHeadImage was set to true and this field returns an empty string, indicating a failure to extract the head image extraction failed. Please check the input document photo.
        :rtype: str
        """
        return self._HeadImageBase64

    @HeadImageBase64.setter
    def HeadImageBase64(self, HeadImageBase64):
        self._HeadImageBase64 = HeadImageBase64

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._WarnInfo = params.get("WarnInfo")
        self._Nationality = params.get("Nationality")
        if params.get("CardInfo") is not None:
            self._CardInfo = GeneralCard()
            self._CardInfo._deserialize(params.get("CardInfo"))
        if params.get("BackCardInfo") is not None:
            self._BackCardInfo = GeneralCard()
            self._BackCardInfo._deserialize(params.get("BackCardInfo"))
        self._CardVerificationToken = params.get("CardVerificationToken")
        self._HeadImageBase64 = params.get("HeadImageBase64")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    r"""The sequence number of an element group in the image

    """

    def __init__(self):
        r"""
        :param _Groups: The elements in each line.
        :type Groups: list of LineInfo
        """
        self._Groups = None

    @property
    def Groups(self):
        r"""The elements in each line.
        :rtype: list of LineInfo
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = LineInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRRequest(AbstractModel):
    r"""HKIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: Whether to return identity photo.
        :type ReturnHeadImage: bool
        :param _DetectFake: Whether to check for authenticity.
        :type DetectFake: bool
        :param _ImageBase64: Base64 string of the image
Supported image formats: PNG, JPG, JPEG. GIF is not supported yet.
Supported image size: The downloaded image cannot exceed 7 MB after being Base64-encoded, and it cannot take longer than 3 seconds to download the image.
        :type ImageBase64: str
        :param _ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 3 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._DetectFake = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        r"""Whether to return identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def DetectFake(self):
        warnings.warn("parameter `DetectFake` is deprecated", DeprecationWarning) 

        r"""Whether to check for authenticity.
        :rtype: bool
        """
        return self._DetectFake

    @DetectFake.setter
    def DetectFake(self, DetectFake):
        warnings.warn("parameter `DetectFake` is deprecated", DeprecationWarning) 

        self._DetectFake = DetectFake

    @property
    def ImageBase64(self):
        r"""Base64 string of the image
Supported image formats: PNG, JPG, JPEG. GIF is not supported yet.
Supported image size: The downloaded image cannot exceed 7 MB after being Base64-encoded, and it cannot take longer than 3 seconds to download the image.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 3 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._DetectFake = params.get("DetectFake")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRResponse(AbstractModel):
    r"""HKIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _CnName: Name in Chinese
        :type CnName: str
        :param _EnName: Name in English
        :type EnName: str
        :param _TelexCode: Telecode of the name in Chinese
        :type TelexCode: str
        :param _Sex: Gender. Valid values: Male, Female
        :type Sex: str
        :param _Birthday: Date of birth
        :type Birthday: str
        :param _Permanent: Permanent identity card.
0: non-permanent;
1: permanent;
-1: unknown.
        :type Permanent: int
        :param _IdNum: Identity card number
        :type IdNum: str
        :param _Symbol: Document symbol, i.e., the symbol under the date of birth, such as "***AZ"
        :type Symbol: str
        :param _FirstIssueDate: Date of first issue
        :type FirstIssueDate: str
        :param _CurrentIssueDate: Date of last receipt
        :type CurrentIssueDate: str
        :param _FakeDetectResult: Authenticity check.
0: unable to judge (because the image is blurred, incomplete, reflective, too dark, etc.);
1: forged;
2: authentic.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FakeDetectResult: int
        :param _HeadImage: Base64-encoded large primary portrait photo from the left side of the new-generation Hong Kong Identity Card.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeadImage: str
        :param _SmallHeadImage: Base64-encoded small secondary portrait photo from the right side of the new-generation Hong Kong Identity Card.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SmallHeadImage: str
        :param _WarningCode: This field is deprecated and will always return an empty array. Usage is not recommended.
        :type WarningCode: list of int
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _WindowEmbeddedText: Text information incorporated within the laser-perforated see-through window on the new-generation Hong Kong Identity Card.
        :type WindowEmbeddedText: str
        :param _HKIDVersion: Versions of the Hong Kong Identity Card: HKID-2018, HKID-2003.
        :type HKIDVersion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CnName = None
        self._EnName = None
        self._TelexCode = None
        self._Sex = None
        self._Birthday = None
        self._Permanent = None
        self._IdNum = None
        self._Symbol = None
        self._FirstIssueDate = None
        self._CurrentIssueDate = None
        self._FakeDetectResult = None
        self._HeadImage = None
        self._SmallHeadImage = None
        self._WarningCode = None
        self._WarnCardInfos = None
        self._WindowEmbeddedText = None
        self._HKIDVersion = None
        self._RequestId = None

    @property
    def CnName(self):
        r"""Name in Chinese
        :rtype: str
        """
        return self._CnName

    @CnName.setter
    def CnName(self, CnName):
        self._CnName = CnName

    @property
    def EnName(self):
        r"""Name in English
        :rtype: str
        """
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def TelexCode(self):
        r"""Telecode of the name in Chinese
        :rtype: str
        """
        return self._TelexCode

    @TelexCode.setter
    def TelexCode(self, TelexCode):
        self._TelexCode = TelexCode

    @property
    def Sex(self):
        r"""Gender. Valid values: Male, Female
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        r"""Date of birth
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Permanent(self):
        r"""Permanent identity card.
0: non-permanent;
1: permanent;
-1: unknown.
        :rtype: int
        """
        return self._Permanent

    @Permanent.setter
    def Permanent(self, Permanent):
        self._Permanent = Permanent

    @property
    def IdNum(self):
        r"""Identity card number
        :rtype: str
        """
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Symbol(self):
        r"""Document symbol, i.e., the symbol under the date of birth, such as "***AZ"
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def FirstIssueDate(self):
        r"""Date of first issue
        :rtype: str
        """
        return self._FirstIssueDate

    @FirstIssueDate.setter
    def FirstIssueDate(self, FirstIssueDate):
        self._FirstIssueDate = FirstIssueDate

    @property
    def CurrentIssueDate(self):
        r"""Date of last receipt
        :rtype: str
        """
        return self._CurrentIssueDate

    @CurrentIssueDate.setter
    def CurrentIssueDate(self, CurrentIssueDate):
        self._CurrentIssueDate = CurrentIssueDate

    @property
    def FakeDetectResult(self):
        warnings.warn("parameter `FakeDetectResult` is deprecated", DeprecationWarning) 

        r"""Authenticity check.
0: unable to judge (because the image is blurred, incomplete, reflective, too dark, etc.);
1: forged;
2: authentic.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FakeDetectResult

    @FakeDetectResult.setter
    def FakeDetectResult(self, FakeDetectResult):
        warnings.warn("parameter `FakeDetectResult` is deprecated", DeprecationWarning) 

        self._FakeDetectResult = FakeDetectResult

    @property
    def HeadImage(self):
        r"""Base64-encoded large primary portrait photo from the left side of the new-generation Hong Kong Identity Card.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HeadImage

    @HeadImage.setter
    def HeadImage(self, HeadImage):
        self._HeadImage = HeadImage

    @property
    def SmallHeadImage(self):
        r"""Base64-encoded small secondary portrait photo from the right side of the new-generation Hong Kong Identity Card.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SmallHeadImage

    @SmallHeadImage.setter
    def SmallHeadImage(self, SmallHeadImage):
        self._SmallHeadImage = SmallHeadImage

    @property
    def WarningCode(self):
        warnings.warn("parameter `WarningCode` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return an empty array. Usage is not recommended.
        :rtype: list of int
        """
        return self._WarningCode

    @WarningCode.setter
    def WarningCode(self, WarningCode):
        warnings.warn("parameter `WarningCode` is deprecated", DeprecationWarning) 

        self._WarningCode = WarningCode

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def WindowEmbeddedText(self):
        r"""Text information incorporated within the laser-perforated see-through window on the new-generation Hong Kong Identity Card.
        :rtype: str
        """
        return self._WindowEmbeddedText

    @WindowEmbeddedText.setter
    def WindowEmbeddedText(self, WindowEmbeddedText):
        self._WindowEmbeddedText = WindowEmbeddedText

    @property
    def HKIDVersion(self):
        r"""Versions of the Hong Kong Identity Card: HKID-2018, HKID-2003.
        :rtype: str
        """
        return self._HKIDVersion

    @HKIDVersion.setter
    def HKIDVersion(self, HKIDVersion):
        self._HKIDVersion = HKIDVersion

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CnName = params.get("CnName")
        self._EnName = params.get("EnName")
        self._TelexCode = params.get("TelexCode")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._Permanent = params.get("Permanent")
        self._IdNum = params.get("IdNum")
        self._Symbol = params.get("Symbol")
        self._FirstIssueDate = params.get("FirstIssueDate")
        self._CurrentIssueDate = params.get("CurrentIssueDate")
        self._FakeDetectResult = params.get("FakeDetectResult")
        self._HeadImage = params.get("HeadImage")
        self._SmallHeadImage = params.get("SmallHeadImage")
        self._WarningCode = params.get("WarningCode")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._WindowEmbeddedText = params.get("WindowEmbeddedText")
        self._HKIDVersion = params.get("HKIDVersion")
        self._RequestId = params.get("RequestId")


class ItemCoord(AbstractModel):
    r"""Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.

    """

    def __init__(self):
        r"""
        :param _X: X-coordinate of top-left point.
        :type X: int
        :param _Y: Y-coordinate of top-left point.
        :type Y: int
        :param _Width: Width
        :type Width: int
        :param _Height: Height
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""X-coordinate of top-left point.
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y-coordinate of top-left point.
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""Width
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""Height
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemInfo(AbstractModel):
    r"""Structured element group

    """

    def __init__(self):
        r"""
        :param _Key: The key information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: :class:`tencentcloud.ocr.v20181119.models.Key`
        :param _Value: The value information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: :class:`tencentcloud.ocr.v20181119.models.Value`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""The key information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Key`
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""The value information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Value`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        if params.get("Key") is not None:
            self._Key = Key()
            self._Key._deserialize(params.get("Key"))
        if params.get("Value") is not None:
            self._Value = Value()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Key(AbstractModel):
    r"""Key information

    """

    def __init__(self):
        r"""
        :param _AutoName: The name of the recognized field.
        :type AutoName: str
        :param _ConfigName: The name of a defined field (the key passed in).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigName: str
        """
        self._AutoName = None
        self._ConfigName = None

    @property
    def AutoName(self):
        r"""The name of the recognized field.
        :rtype: str
        """
        return self._AutoName

    @AutoName.setter
    def AutoName(self, AutoName):
        self._AutoName = AutoName

    @property
    def ConfigName(self):
        r"""The name of a defined field (the key passed in).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName


    def _deserialize(self, params):
        self._AutoName = params.get("AutoName")
        self._ConfigName = params.get("ConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineInfo(AbstractModel):
    r"""Line number

    """

    def __init__(self):
        r"""
        :param _Lines: The elements in a line
        :type Lines: list of ItemInfo
        """
        self._Lines = None

    @property
    def Lines(self):
        r"""The elements in a line
        :rtype: list of ItemInfo
        """
        return self._Lines

    @Lines.setter
    def Lines(self, Lines):
        self._Lines = Lines


    def _deserialize(self, params):
        if params.get("Lines") is not None:
            self._Lines = []
            for item in params.get("Lines"):
                obj = ItemInfo()
                obj._deserialize(item)
                self._Lines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRRequest(AbstractModel):
    r"""MLIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
        :type ImageBase64: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _ImageUrl: The URL of an image. (This field is not available outside the Chinese mainland.)
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be low.
        :type ImageUrl: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :type BackImageUrl: str
        :param _RetImage: Whether to return an image. Default value: `false`.
        :type RetImage: bool
        """
        self._ImageBase64 = None
        self._BackImageBase64 = None
        self._ImageUrl = None
        self._BackImageUrl = None
        self._RetImage = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of an image. (This field is not available outside the Chinese mainland.)
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def RetImage(self):
        r"""Whether to return an image. Default value: `false`.
        :rtype: bool
        """
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageUrl = params.get("BackImageUrl")
        self._RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRResponse(AbstractModel):
    r"""MLIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: ID number
        :type ID: str
        :param _Name: Full name
        :type Name: str
        :param _Address: Address
        :type Address: str
        :param _Sex: Gender
        :type Sex: str
        :param _Warn: This field is deprecated and will always return an empty array. Usage is not recommended.
        :type Warn: list of int
        :param _Image: Identity photo
        :type Image: str
        :param _AdvancedInfo: This field is deprecated and will always return "1". Usage is not recommended.
        :type AdvancedInfo: str
        :param _Type: Certificate type: 
- MyKad: ID card 
- MyPR: Permanent resident card 
- MyTentera: Military identity card 
- MyKAS: Temporary ID card 
- POLIS: Police card 
- IKAD: Work permit 
- MyKid: Child ID card
        :type Type: str
        :param _Birthday: Date of birth. This field is available only for work permits (i-Kad) and ID cards (MyKad).
        :type Birthday: str
        :param _MyKadNumber: Number on the back of the Malaysian ID card
        :type MyKadNumber: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._Name = None
        self._Address = None
        self._Sex = None
        self._Warn = None
        self._Image = None
        self._AdvancedInfo = None
        self._Type = None
        self._Birthday = None
        self._MyKadNumber = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def ID(self):
        r"""ID number
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Full name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Address(self):
        r"""Address
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Warn(self):
        warnings.warn("parameter `Warn` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return an empty array. Usage is not recommended.
        :rtype: list of int
        """
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        warnings.warn("parameter `Warn` is deprecated", DeprecationWarning) 

        self._Warn = Warn

    @property
    def Image(self):
        r"""Identity photo
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return "1". Usage is not recommended.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        self._AdvancedInfo = AdvancedInfo

    @property
    def Type(self):
        r"""Certificate type: 
- MyKad: ID card 
- MyPR: Permanent resident card 
- MyTentera: Military identity card 
- MyKAS: Temporary ID card 
- POLIS: Police card 
- IKAD: Work permit 
- MyKid: Child ID card
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Birthday(self):
        r"""Date of birth. This field is available only for work permits (i-Kad) and ID cards (MyKad).
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def MyKadNumber(self):
        r"""Number on the back of the Malaysian ID card
        :rtype: str
        """
        return self._MyKadNumber

    @MyKadNumber.setter
    def MyKadNumber(self, MyKadNumber):
        self._MyKadNumber = MyKadNumber

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Address = params.get("Address")
        self._Sex = params.get("Sex")
        self._Warn = params.get("Warn")
        self._Image = params.get("Image")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._Type = params.get("Type")
        self._Birthday = params.get("Birthday")
        self._MyKadNumber = params.get("MyKadNumber")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    r"""MLIDPassportOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded image data. The image must be no larger than 7 MB after Base64 encoding. A resolution of at least 500x800 is recommended. Supported image formats: PNG, JPG, JPEG, BMP, and PDF. The document should occupy more than 2/3 of the image area.
        :type ImageBase64: str
        :param _RetImage: Whether to return an image. 
Default value: false.
        :type RetImage: bool
        :param _ImageUrl: URL of the image. The downloaded image must be no larger than 7 MB after Base64 encoding. A resolution of at least 500x800 is recommended. Supported image formats: PNG, JPG, JPEG, BMP, and PDF. The document should occupy more than 2/3 of the image area. Image download must complete within 3 seconds. We recommend storing images in Tencent Cloud for higher download speed and stability. The speed and stability of URLs from non-Tencent Cloud storage may be affected. Note: This field is not supported outside the Chinese mainland region.
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._RetImage = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        r"""Base64-encoded image data. The image must be no larger than 7 MB after Base64 encoding. A resolution of at least 500x800 is recommended. Supported image formats: PNG, JPG, JPEG, BMP, and PDF. The document should occupy more than 2/3 of the image area.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def RetImage(self):
        r"""Whether to return an image. 
Default value: false.
        :rtype: bool
        """
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage

    @property
    def ImageUrl(self):
        r"""URL of the image. The downloaded image must be no larger than 7 MB after Base64 encoding. A resolution of at least 500x800 is recommended. Supported image formats: PNG, JPG, JPEG, BMP, and PDF. The document should occupy more than 2/3 of the image area. Image download must complete within 3 seconds. We recommend storing images in Tencent Cloud for higher download speed and stability. The speed and stability of URLs from non-Tencent Cloud storage may be affected. Note: This field is not supported outside the Chinese mainland region.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._RetImage = params.get("RetImage")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDPassportOCRResponse(AbstractModel):
    r"""MLIDPassportOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: Passport ID
        :type ID: str
        :param _Name: Name
        :type Name: str
        :param _DateOfBirth: Date of birth
        :type DateOfBirth: str
        :param _Sex: Gender (F: female, M: male)
        :type Sex: str
        :param _DateOfExpiration: Expiration date
        :type DateOfExpiration: str
        :param _IssuingCountry: Issuing country
        :type IssuingCountry: str
        :param _Nationality: Nationality code (MRZ field)
        :type Nationality: str
        :param _Warn: This field is deprecated and will always return an empty array. Usage is not recommended.
        :type Warn: list of int
        :param _Image: Base64-encoded identity photo
        :type Image: str
        :param _AdvancedInfo: This field is deprecated and will always return "1". Usage is not recommended.
        :type AdvancedInfo: str
        :param _CodeSet: The first row of the machine-readable zone (MRZ) at the bottom
        :type CodeSet: str
        :param _CodeCrc: The second row of the MRZ at the bottom
        :type CodeCrc: str
        :param _Surname: The surname.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Surname: str
        :param _GivenName: The given name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GivenName: str
        :param _Type: Type (in Machine Readable Zone)
        :type Type: str
        :param _PassportRecognizeInfos: Document content in the visual zone
        :type PassportRecognizeInfos: :class:`tencentcloud.ocr.v20181119.models.PassportRecognizeInfos`
        :param _WarnCardInfos: Warning information for the document. This field applies only to international site requests and will return an empty array for domestic site requests. Valid warning codes: 
-9101 (incomplete card border), 
-9102 (photocopied document), 
-9103 (re-photographed document), -9104 (PS-altered document), 
-9107 (reflective document), 
-9108 (blurry image), 
-9109 (warning capability not enabled).
        :type WarnCardInfos: list of int
        :param _CardCount: The number of cards detected in the input image.(Currently supported only in ap-bangkok region)
        :type CardCount: int
        :param _IsComplete: Whether the passport information is complete.
        :type IsComplete: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._Name = None
        self._DateOfBirth = None
        self._Sex = None
        self._DateOfExpiration = None
        self._IssuingCountry = None
        self._Nationality = None
        self._Warn = None
        self._Image = None
        self._AdvancedInfo = None
        self._CodeSet = None
        self._CodeCrc = None
        self._Surname = None
        self._GivenName = None
        self._Type = None
        self._PassportRecognizeInfos = None
        self._WarnCardInfos = None
        self._CardCount = None
        self._IsComplete = None
        self._RequestId = None

    @property
    def ID(self):
        r"""Passport ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DateOfBirth(self):
        r"""Date of birth
        :rtype: str
        """
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def Sex(self):
        r"""Gender (F: female, M: male)
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def DateOfExpiration(self):
        r"""Expiration date
        :rtype: str
        """
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def IssuingCountry(self):
        r"""Issuing country
        :rtype: str
        """
        return self._IssuingCountry

    @IssuingCountry.setter
    def IssuingCountry(self, IssuingCountry):
        self._IssuingCountry = IssuingCountry

    @property
    def Nationality(self):
        r"""Nationality code (MRZ field)
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Warn(self):
        warnings.warn("parameter `Warn` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return an empty array. Usage is not recommended.
        :rtype: list of int
        """
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        warnings.warn("parameter `Warn` is deprecated", DeprecationWarning) 

        self._Warn = Warn

    @property
    def Image(self):
        r"""Base64-encoded identity photo
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return "1". Usage is not recommended.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        self._AdvancedInfo = AdvancedInfo

    @property
    def CodeSet(self):
        r"""The first row of the machine-readable zone (MRZ) at the bottom
        :rtype: str
        """
        return self._CodeSet

    @CodeSet.setter
    def CodeSet(self, CodeSet):
        self._CodeSet = CodeSet

    @property
    def CodeCrc(self):
        r"""The second row of the MRZ at the bottom
        :rtype: str
        """
        return self._CodeCrc

    @CodeCrc.setter
    def CodeCrc(self, CodeCrc):
        self._CodeCrc = CodeCrc

    @property
    def Surname(self):
        r"""The surname.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def GivenName(self):
        r"""The given name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Type(self):
        r"""Type (in Machine Readable Zone)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PassportRecognizeInfos(self):
        r"""Document content in the visual zone
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PassportRecognizeInfos`
        """
        return self._PassportRecognizeInfos

    @PassportRecognizeInfos.setter
    def PassportRecognizeInfos(self, PassportRecognizeInfos):
        self._PassportRecognizeInfos = PassportRecognizeInfos

    @property
    def WarnCardInfos(self):
        r"""Warning information for the document. This field applies only to international site requests and will return an empty array for domestic site requests. Valid warning codes: 
-9101 (incomplete card border), 
-9102 (photocopied document), 
-9103 (re-photographed document), -9104 (PS-altered document), 
-9107 (reflective document), 
-9108 (blurry image), 
-9109 (warning capability not enabled).
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def CardCount(self):
        r"""The number of cards detected in the input image.(Currently supported only in ap-bangkok region)
        :rtype: int
        """
        return self._CardCount

    @CardCount.setter
    def CardCount(self, CardCount):
        self._CardCount = CardCount

    @property
    def IsComplete(self):
        r"""Whether the passport information is complete.
        :rtype: bool
        """
        return self._IsComplete

    @IsComplete.setter
    def IsComplete(self, IsComplete):
        self._IsComplete = IsComplete

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._DateOfBirth = params.get("DateOfBirth")
        self._Sex = params.get("Sex")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._IssuingCountry = params.get("IssuingCountry")
        self._Nationality = params.get("Nationality")
        self._Warn = params.get("Warn")
        self._Image = params.get("Image")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._CodeSet = params.get("CodeSet")
        self._CodeCrc = params.get("CodeCrc")
        self._Surname = params.get("Surname")
        self._GivenName = params.get("GivenName")
        self._Type = params.get("Type")
        if params.get("PassportRecognizeInfos") is not None:
            self._PassportRecognizeInfos = PassportRecognizeInfos()
            self._PassportRecognizeInfos._deserialize(params.get("PassportRecognizeInfos"))
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._CardCount = params.get("CardCount")
        self._IsComplete = params.get("IsComplete")
        self._RequestId = params.get("RequestId")


class MainlandPermitOCRRequest(AbstractModel):
    r"""MainlandPermitOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _RetProfile: Whether to return the ID photo. By default, the ID photo is not returned.
        :type RetProfile: bool
        :param _CardSide: The side of the document. Valid values: FRONT (front side, default),
BACK (back side, only supported for Mainland Travel Permit for inbound visits). 
Note: Back side recognition is only supported for the "Mainland Travel Permit for Hong Kong and Macao Residents" , and is not supported for Hong Kong, Macao, or Taiwan passes.
        :type CardSide: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetProfile = None
        self._CardSide = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RetProfile(self):
        r"""Whether to return the ID photo. By default, the ID photo is not returned.
        :rtype: bool
        """
        return self._RetProfile

    @RetProfile.setter
    def RetProfile(self, RetProfile):
        self._RetProfile = RetProfile

    @property
    def CardSide(self):
        r"""The side of the document. Valid values: FRONT (front side, default),
BACK (back side, only supported for Mainland Travel Permit for inbound visits). 
Note: Back side recognition is only supported for the "Mainland Travel Permit for Hong Kong and Macao Residents" , and is not supported for Hong Kong, Macao, or Taiwan passes.
        :rtype: str
        """
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetProfile = params.get("RetProfile")
        self._CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRResponse(AbstractModel):
    r"""MainlandPermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name in Chinese
        :type Name: str
        :param _EnglishName: Name in English
        :type EnglishName: str
        :param _Sex: Gender
        :type Sex: str
        :param _Birthday: Date of birth
        :type Birthday: str
        :param _IssueAuthority: Issuing authority
        :type IssueAuthority: str
        :param _ValidDate: Validity period
        :type ValidDate: str
        :param _Number: ID number
        :type Number: str
        :param _IssueAddress: Place of issue
        :type IssueAddress: str
        :param _IssueNumber: Number of issues
        :type IssueNumber: str
        :param _Type: Document type, such as: Mainland Travel Permit for Taiwan Residents, Mainland Travel Permit for Hong Kong and Macao Residents, or Exit-Entry Permit for Travelling to and from Hong Kong and Macao.
        :type Type: str
        :param _Profile: Base64-encoded profile photo, which is returned only when `RetProfile` is set to `True`
        :type Profile: str
        :param _Nationality: Nationality of the document holder.
        :type Nationality: str
        :param _MainlandTravelPermitBackInfos: Information on the back of the document. 
Note: Only supported for the back side of the Mainland Travel Permit for Hong Kong and Macao Residents.
        :type MainlandTravelPermitBackInfos: :class:`tencentcloud.ocr.v20181119.models.MainlandTravelPermitBackInfos`
        :param _WarnCardInfos: Warning information for the document. This field is only valid for international site requests. 
Warning codes: 
-9102: photocopy warning; 
-9103: recapture warning; 
-9104: Photoshopped document warning; 
-9109: warning capability not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._EnglishName = None
        self._Sex = None
        self._Birthday = None
        self._IssueAuthority = None
        self._ValidDate = None
        self._Number = None
        self._IssueAddress = None
        self._IssueNumber = None
        self._Type = None
        self._Profile = None
        self._Nationality = None
        self._MainlandTravelPermitBackInfos = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def Name(self):
        r"""Name in Chinese
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        r"""Name in English
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        r"""Date of birth
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueAuthority(self):
        r"""Issuing authority
        :rtype: str
        """
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def ValidDate(self):
        r"""Validity period
        :rtype: str
        """
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Number(self):
        r"""ID number
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def IssueAddress(self):
        r"""Place of issue
        :rtype: str
        """
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def IssueNumber(self):
        r"""Number of issues
        :rtype: str
        """
        return self._IssueNumber

    @IssueNumber.setter
    def IssueNumber(self, IssueNumber):
        self._IssueNumber = IssueNumber

    @property
    def Type(self):
        r"""Document type, such as: Mainland Travel Permit for Taiwan Residents, Mainland Travel Permit for Hong Kong and Macao Residents, or Exit-Entry Permit for Travelling to and from Hong Kong and Macao.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Profile(self):
        r"""Base64-encoded profile photo, which is returned only when `RetProfile` is set to `True`
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Nationality(self):
        r"""Nationality of the document holder.
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def MainlandTravelPermitBackInfos(self):
        r"""Information on the back of the document. 
Note: Only supported for the back side of the Mainland Travel Permit for Hong Kong and Macao Residents.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MainlandTravelPermitBackInfos`
        """
        return self._MainlandTravelPermitBackInfos

    @MainlandTravelPermitBackInfos.setter
    def MainlandTravelPermitBackInfos(self, MainlandTravelPermitBackInfos):
        self._MainlandTravelPermitBackInfos = MainlandTravelPermitBackInfos

    @property
    def WarnCardInfos(self):
        r"""Warning information for the document. This field is only valid for international site requests. 
Warning codes: 
-9102: photocopy warning; 
-9103: recapture warning; 
-9104: Photoshopped document warning; 
-9109: warning capability not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._IssueAuthority = params.get("IssueAuthority")
        self._ValidDate = params.get("ValidDate")
        self._Number = params.get("Number")
        self._IssueAddress = params.get("IssueAddress")
        self._IssueNumber = params.get("IssueNumber")
        self._Type = params.get("Type")
        self._Profile = params.get("Profile")
        self._Nationality = params.get("Nationality")
        if params.get("MainlandTravelPermitBackInfos") is not None:
            self._MainlandTravelPermitBackInfos = MainlandTravelPermitBackInfos()
            self._MainlandTravelPermitBackInfos._deserialize(params.get("MainlandTravelPermitBackInfos"))
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class MainlandTravelPermitBackInfos(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Type: 
        :type Type: str
        :param _Name: 
        :type Name: str
        :param _IDNumber: 
        :type IDNumber: str
        :param _HistoryNumber: 
        :type HistoryNumber: str
        """
        self._Type = None
        self._Name = None
        self._IDNumber = None
        self._HistoryNumber = None

    @property
    def Type(self):
        r"""
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IDNumber(self):
        r"""
        :rtype: str
        """
        return self._IDNumber

    @IDNumber.setter
    def IDNumber(self, IDNumber):
        self._IDNumber = IDNumber

    @property
    def HistoryNumber(self):
        r"""
        :rtype: str
        """
        return self._HistoryNumber

    @HistoryNumber.setter
    def HistoryNumber(self, HistoryNumber):
        self._HistoryNumber = HistoryNumber


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._IDNumber = params.get("IDNumber")
        self._HistoryNumber = params.get("HistoryNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PODAuditAIRequest(AbstractModel):
    r"""PODAuditAI request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64List: <p>The Base64 value of the image/PDF. The Base64 must be no more than 10M, resolution is recommended to be 600*800 or higher, and supports PNG, JPG, JPEG, BMP, PDF formats. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only use ImageUrl. Example value: /9j/4AAQSkZJRg.....s97n//2Q==</p>
        :type ImageBase64List: list of str
        :param _ImageUrlList: <p>The Url address of the image/PDF. The image after Base64 encoding should be no more than 10M, with a resolution of 600*800 or higher, and supports PNG, JPG, JPEG, BMP, and PDF formats. The image download time should not exceed 3 seconds. Images stored in Tencent Cloud's Url can guarantee higher download speed and stability. It is recommended to store images in Tencent Cloud. The speed and stability of non-Tencent Cloud storage URLs may be impacted to a certain extent. Example value: https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.JPG</p>
        :type ImageUrlList: list of str
        :param _WaybillNumber: <p>Waybill number is used for pod rule review assistance</p>
        :type WaybillNumber: str
        :param _SignType: <p>No      The acknowledge type, 0 is selected by default</p><p>Enumeration value:</p><ul><li>0: Doorstep/yard</li><li>1: Parcel reception room</li><li>2: Myself/others acknowledge</li><li>3: Front desk/reception</li><li>4: Express delivery collection point</li><li>5: Express cabinet</li></ul>
        :type SignType: int
        """
        self._ImageBase64List = None
        self._ImageUrlList = None
        self._WaybillNumber = None
        self._SignType = None

    @property
    def ImageBase64List(self):
        r"""<p>The Base64 value of the image/PDF. The Base64 must be no more than 10M, resolution is recommended to be 600*800 or higher, and supports PNG, JPG, JPEG, BMP, PDF formats. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only use ImageUrl. Example value: /9j/4AAQSkZJRg.....s97n//2Q==</p>
        :rtype: list of str
        """
        return self._ImageBase64List

    @ImageBase64List.setter
    def ImageBase64List(self, ImageBase64List):
        self._ImageBase64List = ImageBase64List

    @property
    def ImageUrlList(self):
        r"""<p>The Url address of the image/PDF. The image after Base64 encoding should be no more than 10M, with a resolution of 600*800 or higher, and supports PNG, JPG, JPEG, BMP, and PDF formats. The image download time should not exceed 3 seconds. Images stored in Tencent Cloud's Url can guarantee higher download speed and stability. It is recommended to store images in Tencent Cloud. The speed and stability of non-Tencent Cloud storage URLs may be impacted to a certain extent. Example value: https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.JPG</p>
        :rtype: list of str
        """
        return self._ImageUrlList

    @ImageUrlList.setter
    def ImageUrlList(self, ImageUrlList):
        self._ImageUrlList = ImageUrlList

    @property
    def WaybillNumber(self):
        r"""<p>Waybill number is used for pod rule review assistance</p>
        :rtype: str
        """
        return self._WaybillNumber

    @WaybillNumber.setter
    def WaybillNumber(self, WaybillNumber):
        self._WaybillNumber = WaybillNumber

    @property
    def SignType(self):
        r"""<p>No      The acknowledge type, 0 is selected by default</p><p>Enumeration value:</p><ul><li>0: Doorstep/yard</li><li>1: Parcel reception room</li><li>2: Myself/others acknowledge</li><li>3: Front desk/reception</li><li>4: Express delivery collection point</li><li>5: Express cabinet</li></ul>
        :rtype: int
        """
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType


    def _deserialize(self, params):
        self._ImageBase64List = params.get("ImageBase64List")
        self._ImageUrlList = params.get("ImageUrlList")
        self._WaybillNumber = params.get("WaybillNumber")
        self._SignType = params.get("SignType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PODAuditAIResponse(AbstractModel):
    r"""PODAuditAI response structure.

    """

    def __init__(self):
        r"""
        :param _AuditorDecision: <p>0 means non-compliance 1 means compliance</p>
        :type AuditorDecision: int
        :param _FailCode: <p>Reason code for non-compliance. If there are multiple, return a list of multiple codes.</p><p>Enumeration value:</p><ul><li>100: Wrong delivery address</li><li>101: No house number</li><li>104: Single question</li><li>200: No package</li><li>202: Privacy leakage</li></ul>
        :type FailCode: list of str
        :param _ResultAnalysis: <p>Entire approval result analysis content</p>
        :type ResultAnalysis: str
        :param _AnalyzedLogs: <p>Analysis result logs of each layer, including time taken, judgment reason, and judgment conclusion</p>
        :type AnalyzedLogs: list of AnalyzedLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuditorDecision = None
        self._FailCode = None
        self._ResultAnalysis = None
        self._AnalyzedLogs = None
        self._RequestId = None

    @property
    def AuditorDecision(self):
        r"""<p>0 means non-compliance 1 means compliance</p>
        :rtype: int
        """
        return self._AuditorDecision

    @AuditorDecision.setter
    def AuditorDecision(self, AuditorDecision):
        self._AuditorDecision = AuditorDecision

    @property
    def FailCode(self):
        r"""<p>Reason code for non-compliance. If there are multiple, return a list of multiple codes.</p><p>Enumeration value:</p><ul><li>100: Wrong delivery address</li><li>101: No house number</li><li>104: Single question</li><li>200: No package</li><li>202: Privacy leakage</li></ul>
        :rtype: list of str
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def ResultAnalysis(self):
        r"""<p>Entire approval result analysis content</p>
        :rtype: str
        """
        return self._ResultAnalysis

    @ResultAnalysis.setter
    def ResultAnalysis(self, ResultAnalysis):
        self._ResultAnalysis = ResultAnalysis

    @property
    def AnalyzedLogs(self):
        r"""<p>Analysis result logs of each layer, including time taken, judgment reason, and judgment conclusion</p>
        :rtype: list of AnalyzedLog
        """
        return self._AnalyzedLogs

    @AnalyzedLogs.setter
    def AnalyzedLogs(self, AnalyzedLogs):
        self._AnalyzedLogs = AnalyzedLogs

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuditorDecision = params.get("AuditorDecision")
        self._FailCode = params.get("FailCode")
        self._ResultAnalysis = params.get("ResultAnalysis")
        if params.get("AnalyzedLogs") is not None:
            self._AnalyzedLogs = []
            for item in params.get("AnalyzedLogs"):
                obj = AnalyzedLog()
                obj._deserialize(item)
                self._AnalyzedLogs.append(obj)
        self._RequestId = params.get("RequestId")


class PassportRecognizeInfos(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Type: 
        :type Type: str
        :param _IssuingCountry: 
        :type IssuingCountry: str
        :param _PassportID: 
        :type PassportID: str
        :param _Surname: 
        :type Surname: str
        :param _GivenName: 
        :type GivenName: str
        :param _Name: 
        :type Name: str
        :param _Nationality: 
        :type Nationality: str
        :param _DateOfBirth: 
        :type DateOfBirth: str
        :param _Sex: 
        :type Sex: str
        :param _DateOfIssuance: 
        :type DateOfIssuance: str
        :param _DateOfExpiration: 
        :type DateOfExpiration: str
        :param _Signature: 
        :type Signature: str
        :param _IssuePlace: 
        :type IssuePlace: str
        :param _IssuingAuthority: 
        :type IssuingAuthority: str
        :param _BirthPlace: 
        :type BirthPlace: str
        """
        self._Type = None
        self._IssuingCountry = None
        self._PassportID = None
        self._Surname = None
        self._GivenName = None
        self._Name = None
        self._Nationality = None
        self._DateOfBirth = None
        self._Sex = None
        self._DateOfIssuance = None
        self._DateOfExpiration = None
        self._Signature = None
        self._IssuePlace = None
        self._IssuingAuthority = None
        self._BirthPlace = None

    @property
    def Type(self):
        r"""
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IssuingCountry(self):
        r"""
        :rtype: str
        """
        return self._IssuingCountry

    @IssuingCountry.setter
    def IssuingCountry(self, IssuingCountry):
        self._IssuingCountry = IssuingCountry

    @property
    def PassportID(self):
        r"""
        :rtype: str
        """
        return self._PassportID

    @PassportID.setter
    def PassportID(self, PassportID):
        self._PassportID = PassportID

    @property
    def Surname(self):
        r"""
        :rtype: str
        """
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def GivenName(self):
        r"""
        :rtype: str
        """
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Nationality(self):
        r"""
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def DateOfBirth(self):
        r"""
        :rtype: str
        """
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def Sex(self):
        r"""
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def DateOfIssuance(self):
        r"""
        :rtype: str
        """
        return self._DateOfIssuance

    @DateOfIssuance.setter
    def DateOfIssuance(self, DateOfIssuance):
        self._DateOfIssuance = DateOfIssuance

    @property
    def DateOfExpiration(self):
        r"""
        :rtype: str
        """
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def Signature(self):
        r"""
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def IssuePlace(self):
        r"""
        :rtype: str
        """
        return self._IssuePlace

    @IssuePlace.setter
    def IssuePlace(self, IssuePlace):
        self._IssuePlace = IssuePlace

    @property
    def IssuingAuthority(self):
        r"""
        :rtype: str
        """
        return self._IssuingAuthority

    @IssuingAuthority.setter
    def IssuingAuthority(self, IssuingAuthority):
        self._IssuingAuthority = IssuingAuthority

    @property
    def BirthPlace(self):
        r"""
        :rtype: str
        """
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._IssuingCountry = params.get("IssuingCountry")
        self._PassportID = params.get("PassportID")
        self._Surname = params.get("Surname")
        self._GivenName = params.get("GivenName")
        self._Name = params.get("Name")
        self._Nationality = params.get("Nationality")
        self._DateOfBirth = params.get("DateOfBirth")
        self._Sex = params.get("Sex")
        self._DateOfIssuance = params.get("DateOfIssuance")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._Signature = params.get("Signature")
        self._IssuePlace = params.get("IssuePlace")
        self._IssuingAuthority = params.get("IssuingAuthority")
        self._BirthPlace = params.get("BirthPlace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRRequest(AbstractModel):
    r"""PermitOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of the image. Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported. Supported image size: The downloaded image after Base64 encoding cannot exceed 7 MB. The download time of the image cannot exceed 3 seconds. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only ImageUrl is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image. Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported. Supported image size: The downloaded image after Base64 encoding cannot exceed 7 MB. The download time of the image cannot exceed 3 seconds. We recommend that you store the image in Tencent Cloud for higher download speed and stability. The download speed and stability of images stored outside Tencent Cloud may be compromised.
        :type ImageUrl: str
        :param _CropPortrait: Whether to return the ID photo. The default value is false.
        :type CropPortrait: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CropPortrait = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of the image. Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported. Supported image size: The downloaded image after Base64 encoding cannot exceed 7 MB. The download time of the image cannot exceed 3 seconds. Either ImageUrl or ImageBase64 of the image must be provided. If both are provided, only ImageUrl is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image. Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported. Supported image size: The downloaded image after Base64 encoding cannot exceed 7 MB. The download time of the image cannot exceed 3 seconds. We recommend that you store the image in Tencent Cloud for higher download speed and stability. The download speed and stability of images stored outside Tencent Cloud may be compromised.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CropPortrait(self):
        r"""Whether to return the ID photo. The default value is false.
        :rtype: bool
        """
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CropPortrait = params.get("CropPortrait")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRResponse(AbstractModel):
    r"""PermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name in Chinese
        :type Name: str
        :param _EnglishName: English name
        :type EnglishName: str
        :param _Number: ID number
        :type Number: str
        :param _Sex: Gender
        :type Sex: str
        :param _ValidDate: Validity period
        :type ValidDate: str
        :param _IssueAuthority: Issuing authority
        :type IssueAuthority: str
        :param _IssueAddress: Place of issue
        :type IssueAddress: str
        :param _Birthday: Date of birth
        :type Birthday: str
        :param _PortraitImage: Base64-encoded profile photo of the document holder.
        :type PortraitImage: str
        :param _Type: Document type, such as: Exit-Entry Permit for Travelling to and from Hong Kong and Macao, or Exit-Entry Permit for Travelling to and from Taiwan.
        :type Type: str
        :param _WarnCardInfos: Warning information for the document. This field is only valid for international site requests. Warning codes:
-9101: Incomplete card border warning
-9102: Photocopied card warning
-9103: Recaptured card warning
-9104: Photoshopped card warning
-9107: Reflective card warning
-9108: Blurry image warning
-9109: Warning capability not enabled
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._EnglishName = None
        self._Number = None
        self._Sex = None
        self._ValidDate = None
        self._IssueAuthority = None
        self._IssueAddress = None
        self._Birthday = None
        self._PortraitImage = None
        self._Type = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def Name(self):
        r"""Name in Chinese
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        r"""English name
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Number(self):
        r"""ID number
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def ValidDate(self):
        r"""Validity period
        :rtype: str
        """
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def IssueAuthority(self):
        r"""Issuing authority
        :rtype: str
        """
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def IssueAddress(self):
        r"""Place of issue
        :rtype: str
        """
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def Birthday(self):
        r"""Date of birth
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def PortraitImage(self):
        r"""Base64-encoded profile photo of the document holder.
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def Type(self):
        r"""Document type, such as: Exit-Entry Permit for Travelling to and from Hong Kong and Macao, or Exit-Entry Permit for Travelling to and from Taiwan.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WarnCardInfos(self):
        r"""Warning information for the document. This field is only valid for international site requests. Warning codes:
-9101: Incomplete card border warning
-9102: Photocopied card warning
-9103: Recaptured card warning
-9104: Photoshopped card warning
-9107: Reflective card warning
-9108: Blurry image warning
-9109: Warning capability not enabled
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        self._Number = params.get("Number")
        self._Sex = params.get("Sex")
        self._ValidDate = params.get("ValidDate")
        self._IssueAuthority = params.get("IssueAuthority")
        self._IssueAddress = params.get("IssueAddress")
        self._Birthday = params.get("Birthday")
        self._PortraitImage = params.get("PortraitImage")
        self._Type = params.get("Type")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    r"""The coordinates of the four vertices of the text
    Note: This field may return null, indicating that no valid values can be obtained.

    """

    def __init__(self):
        r"""
        :param _LeftTop: The coordinates of the upper-left vertex.
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightTop: The coordinates of the upper-right vertex.
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightBottom: The coordinates of the lower-left vertex.
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _LeftBottom: The coordinates of the lower-right vertex.
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self._LeftTop = None
        self._RightTop = None
        self._RightBottom = None
        self._LeftBottom = None

    @property
    def LeftTop(self):
        r"""The coordinates of the upper-left vertex.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        return self._LeftTop

    @LeftTop.setter
    def LeftTop(self, LeftTop):
        self._LeftTop = LeftTop

    @property
    def RightTop(self):
        r"""The coordinates of the upper-right vertex.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        return self._RightTop

    @RightTop.setter
    def RightTop(self, RightTop):
        self._RightTop = RightTop

    @property
    def RightBottom(self):
        r"""The coordinates of the lower-left vertex.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        return self._RightBottom

    @RightBottom.setter
    def RightBottom(self, RightBottom):
        self._RightBottom = RightBottom

    @property
    def LeftBottom(self):
        r"""The coordinates of the lower-right vertex.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        return self._LeftBottom

    @LeftBottom.setter
    def LeftBottom(self, LeftBottom):
        self._LeftBottom = LeftBottom


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self._LeftTop = Coord()
            self._LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self._RightTop = Coord()
            self._RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self._RightBottom = Coord()
            self._RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self._LeftBottom = Coord()
            self._LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilCommonOCRRequest(AbstractModel):
    r"""RecognizeBrazilCommonOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64 value of the image. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after encoding. image download time: no more than 3 seconds.
        :type ImageBase64: str
        :param _ImageUrl: The Url of the image. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after Base64 encoding. image download time is no more than 3 seconds. urls stored in tencent cloud guarantee higher download speed and stability. it is advisable to store images in tencent cloud. urls not stored in tencent cloud may possibly be impacted in speed and stability.
        :type ImageUrl: str
        :param _BackImageBase64: The Base64 value of the back side of the card. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after encoding. image download time: not more than 3 seconds. either ImageUrl or ImageBase64 must be provided. if both are provided, only use ImageUrl.
        :type BackImageBase64: str
        :param _BackImageUrl: The Url address of the back side of the card. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after Base64 encoding. image download time is no more than 3 seconds. urls stored in tencent cloud guarantee higher download speed and stability. it is recommended to store images in tencent cloud. speed and stability of non-tencent cloud storage urls may be impacted.
        :type BackImageUrl: str
        :param _ReturnHeadImage: Specifies whether to return the portrait photo.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._BackImageBase64 = None
        self._BackImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after encoding. image download time: no more than 3 seconds.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The Url of the image. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after Base64 encoding. image download time is no more than 3 seconds. urls stored in tencent cloud guarantee higher download speed and stability. it is advisable to store images in tencent cloud. urls not stored in tencent cloud may possibly be impacted in speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageBase64(self):
        r"""The Base64 value of the back side of the card. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after encoding. image download time: not more than 3 seconds. either ImageUrl or ImageBase64 must be provided. if both are provided, only use ImageUrl.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def BackImageUrl(self):
        r"""The Url address of the back side of the card. supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. supported image size: no more than 7M after Base64 encoding. image download time is no more than 3 seconds. urls stored in tencent cloud guarantee higher download speed and stability. it is recommended to store images in tencent cloud. speed and stability of non-tencent cloud storage urls may be impacted.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Specifies whether to return the portrait photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._BackImageUrl = params.get("BackImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilCommonOCRResponse(AbstractModel):
    r"""RecognizeBrazilCommonOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Type: Specifies the type of document in brazil. valid values: 
1. RNE 
2. RNM 
3. IDCard 
4. DrivingLicense.
        :type Type: int
        :param _Result: The recognized content of the Brazilian document.
        :type Result: :class:`tencentcloud.ocr.v20181119.models.BrazilCardInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Type = None
        self._Result = None
        self._RequestId = None

    @property
    def Type(self):
        r"""Specifies the type of document in brazil. valid values: 
1. RNE 
2. RNM 
3. IDCard 
4. DrivingLicense.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Result(self):
        r"""The recognized content of the Brazilian document.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BrazilCardInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Result") is not None:
            self._Result = BrazilCardInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class RecognizeBrazilDriverLicenseOCRRequest(AbstractModel):
    r"""RecognizeBrazilDriverLicenseOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64 value of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type ImageBase64: str
        :param _BackImageBase64: The Base64 value of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _ImageUrl: The URL address of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :type ImageUrl: str
        :param _BackImageUrl: The URL address of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :type BackImageUrl: str
        :param _CropPortrait: Picture switch. The default is false, and the base64 encoding of the avatar photo is not returned. When set to true, the base64 encoding of the portrait photo is returned.
        :type CropPortrait: bool
        :param _LicenceVersion: Version of the driver's license image. 
Valid values: 
OLD (old version), 
NEW (new version). 
The default value is OLD.
        :type LicenceVersion: str
        """
        self._ImageBase64 = None
        self._BackImageBase64 = None
        self._ImageUrl = None
        self._BackImageUrl = None
        self._CropPortrait = None
        self._LicenceVersion = None

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def BackImageBase64(self):
        r"""The Base64 value of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def ImageUrl(self):
        r"""The URL address of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageUrl(self):
        r"""The URL address of the image. It is required that the image after Base64 encoding should not exceed 7M, the resolution is recommended to be 500*800 or above, and PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def CropPortrait(self):
        r"""Picture switch. The default is false, and the base64 encoding of the avatar photo is not returned. When set to true, the base64 encoding of the portrait photo is returned.
        :rtype: bool
        """
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait

    @property
    def LicenceVersion(self):
        r"""Version of the driver's license image. 
Valid values: 
OLD (old version), 
NEW (new version). 
The default value is OLD.
        :rtype: str
        """
        return self._LicenceVersion

    @LicenceVersion.setter
    def LicenceVersion(self, LicenceVersion):
        self._LicenceVersion = LicenceVersion


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageUrl = params.get("BackImageUrl")
        self._CropPortrait = params.get("CropPortrait")
        self._LicenceVersion = params.get("LicenceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilDriverLicenseOCRResponse(AbstractModel):
    r"""RecognizeBrazilDriverLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param _NOME: Name of the license holder.
        :type NOME: str
        :param _CatHab: Driver's license category.
        :type CatHab: str
        :param _CNHNumber: Driver's license number (CNH).
        :type CNHNumber: str
        :param _VALIDADE: Validity date (valid until).
        :type VALIDADE: str
        :param _QUALIFICATION: Qualification information.
        :type QUALIFICATION: str
        :param _IDENTIDADE: ID number (Identity document number).
        :type IDENTIDADE: str
        :param _CPF: CPF
        :type CPF: str
        :param _NASCIMENTO: Date of birth.
        :type NASCIMENTO: str
        :param _MEMBERSHIP: Membership
        :type MEMBERSHIP: str
        :param _REGISTRO: Registration number
        :type REGISTRO: str
        :param _OBSERVATIONS: Remarks
        :type OBSERVATIONS: str
        :param _IssueDate: Date of issue.
        :type IssueDate: str
        :param _LOCAL: Place of issue.
        :type LOCAL: str
        :param _BackNumber: Registration number on the back of the card.
        :type BackNumber: str
        :param _AdvancedInfo: This field is deprecated and will always return "1". Usage is not recommended.
        :type AdvancedInfo: str
        :param _PortraitImage: PortraitImage base64
        :type PortraitImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NOME = None
        self._CatHab = None
        self._CNHNumber = None
        self._VALIDADE = None
        self._QUALIFICATION = None
        self._IDENTIDADE = None
        self._CPF = None
        self._NASCIMENTO = None
        self._MEMBERSHIP = None
        self._REGISTRO = None
        self._OBSERVATIONS = None
        self._IssueDate = None
        self._LOCAL = None
        self._BackNumber = None
        self._AdvancedInfo = None
        self._PortraitImage = None
        self._RequestId = None

    @property
    def NOME(self):
        r"""Name of the license holder.
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def CatHab(self):
        r"""Driver's license category.
        :rtype: str
        """
        return self._CatHab

    @CatHab.setter
    def CatHab(self, CatHab):
        self._CatHab = CatHab

    @property
    def CNHNumber(self):
        r"""Driver's license number (CNH).
        :rtype: str
        """
        return self._CNHNumber

    @CNHNumber.setter
    def CNHNumber(self, CNHNumber):
        self._CNHNumber = CNHNumber

    @property
    def VALIDADE(self):
        r"""Validity date (valid until).
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def QUALIFICATION(self):
        r"""Qualification information.
        :rtype: str
        """
        return self._QUALIFICATION

    @QUALIFICATION.setter
    def QUALIFICATION(self, QUALIFICATION):
        self._QUALIFICATION = QUALIFICATION

    @property
    def IDENTIDADE(self):
        r"""ID number (Identity document number).
        :rtype: str
        """
        return self._IDENTIDADE

    @IDENTIDADE.setter
    def IDENTIDADE(self, IDENTIDADE):
        self._IDENTIDADE = IDENTIDADE

    @property
    def CPF(self):
        r"""CPF
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def NASCIMENTO(self):
        r"""Date of birth.
        :rtype: str
        """
        return self._NASCIMENTO

    @NASCIMENTO.setter
    def NASCIMENTO(self, NASCIMENTO):
        self._NASCIMENTO = NASCIMENTO

    @property
    def MEMBERSHIP(self):
        r"""Membership
        :rtype: str
        """
        return self._MEMBERSHIP

    @MEMBERSHIP.setter
    def MEMBERSHIP(self, MEMBERSHIP):
        self._MEMBERSHIP = MEMBERSHIP

    @property
    def REGISTRO(self):
        r"""Registration number
        :rtype: str
        """
        return self._REGISTRO

    @REGISTRO.setter
    def REGISTRO(self, REGISTRO):
        self._REGISTRO = REGISTRO

    @property
    def OBSERVATIONS(self):
        r"""Remarks
        :rtype: str
        """
        return self._OBSERVATIONS

    @OBSERVATIONS.setter
    def OBSERVATIONS(self, OBSERVATIONS):
        self._OBSERVATIONS = OBSERVATIONS

    @property
    def IssueDate(self):
        r"""Date of issue.
        :rtype: str
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def LOCAL(self):
        r"""Place of issue.
        :rtype: str
        """
        return self._LOCAL

    @LOCAL.setter
    def LOCAL(self, LOCAL):
        self._LOCAL = LOCAL

    @property
    def BackNumber(self):
        r"""Registration number on the back of the card.
        :rtype: str
        """
        return self._BackNumber

    @BackNumber.setter
    def BackNumber(self, BackNumber):
        self._BackNumber = BackNumber

    @property
    def AdvancedInfo(self):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return "1". Usage is not recommended.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        self._AdvancedInfo = AdvancedInfo

    @property
    def PortraitImage(self):
        r"""PortraitImage base64
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NOME = params.get("NOME")
        self._CatHab = params.get("CatHab")
        self._CNHNumber = params.get("CNHNumber")
        self._VALIDADE = params.get("VALIDADE")
        self._QUALIFICATION = params.get("QUALIFICATION")
        self._IDENTIDADE = params.get("IDENTIDADE")
        self._CPF = params.get("CPF")
        self._NASCIMENTO = params.get("NASCIMENTO")
        self._MEMBERSHIP = params.get("MEMBERSHIP")
        self._REGISTRO = params.get("REGISTRO")
        self._OBSERVATIONS = params.get("OBSERVATIONS")
        self._IssueDate = params.get("IssueDate")
        self._LOCAL = params.get("LOCAL")
        self._BackNumber = params.get("BackNumber")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._PortraitImage = params.get("PortraitImage")
        self._RequestId = params.get("RequestId")


class RecognizeBrazilIDCardOCRRequest(AbstractModel):
    r"""RecognizeBrazilIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. Image download time does not exceed 3 seconds.
        :type ImageBase64: str
        :param _ImageUrl: URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :type ImageUrl: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :type BackImageUrl: str
        :param _ReturnHeadImage: Whether to return portrait photos.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._BackImageBase64 = None
        self._BackImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. Image download time does not exceed 3 seconds.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return portrait photos.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._BackImageUrl = params.get("BackImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilIDCardOCRResponse(AbstractModel):
    r"""RecognizeBrazilIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Nome: Name
        :type Nome: str
        :param _MemberShip: Family information
        :type MemberShip: str
        :param _DataNascimento: Date of birth
        :type DataNascimento: str
        :param _IssuingAgency: Issuing agency
        :type IssuingAgency: str
        :param _Fatorrh: Blood type
        :type Fatorrh: str
        :param _NaturalIDade: Birth place
        :type NaturalIDade: str
        :param _Observations: Additional information 
        :type Observations: str
        :param _CPF: CPF
        :type CPF: str
        :param _DNI: DNI
        :type DNI: str
        :param _RegistroGeral: General registry (Registro Geral)
        :type RegistroGeral: str
        :param _DispatchDate: Issue date
        :type DispatchDate: str
        :param _Registro: address
        :type Registro: str
        :param _PortraitImage: Portrait image
        :type PortraitImage: str
        :param _DocOrigem: Original identity information
        :type DocOrigem: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Nome = None
        self._MemberShip = None
        self._DataNascimento = None
        self._IssuingAgency = None
        self._Fatorrh = None
        self._NaturalIDade = None
        self._Observations = None
        self._CPF = None
        self._DNI = None
        self._RegistroGeral = None
        self._DispatchDate = None
        self._Registro = None
        self._PortraitImage = None
        self._DocOrigem = None
        self._RequestId = None

    @property
    def Nome(self):
        r"""Name
        :rtype: str
        """
        return self._Nome

    @Nome.setter
    def Nome(self, Nome):
        self._Nome = Nome

    @property
    def MemberShip(self):
        r"""Family information
        :rtype: str
        """
        return self._MemberShip

    @MemberShip.setter
    def MemberShip(self, MemberShip):
        self._MemberShip = MemberShip

    @property
    def DataNascimento(self):
        r"""Date of birth
        :rtype: str
        """
        return self._DataNascimento

    @DataNascimento.setter
    def DataNascimento(self, DataNascimento):
        self._DataNascimento = DataNascimento

    @property
    def IssuingAgency(self):
        r"""Issuing agency
        :rtype: str
        """
        return self._IssuingAgency

    @IssuingAgency.setter
    def IssuingAgency(self, IssuingAgency):
        self._IssuingAgency = IssuingAgency

    @property
    def Fatorrh(self):
        r"""Blood type
        :rtype: str
        """
        return self._Fatorrh

    @Fatorrh.setter
    def Fatorrh(self, Fatorrh):
        self._Fatorrh = Fatorrh

    @property
    def NaturalIDade(self):
        r"""Birth place
        :rtype: str
        """
        return self._NaturalIDade

    @NaturalIDade.setter
    def NaturalIDade(self, NaturalIDade):
        self._NaturalIDade = NaturalIDade

    @property
    def Observations(self):
        r"""Additional information 
        :rtype: str
        """
        return self._Observations

    @Observations.setter
    def Observations(self, Observations):
        self._Observations = Observations

    @property
    def CPF(self):
        r"""CPF
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def DNI(self):
        r"""DNI
        :rtype: str
        """
        return self._DNI

    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI

    @property
    def RegistroGeral(self):
        r"""General registry (Registro Geral)
        :rtype: str
        """
        return self._RegistroGeral

    @RegistroGeral.setter
    def RegistroGeral(self, RegistroGeral):
        self._RegistroGeral = RegistroGeral

    @property
    def DispatchDate(self):
        r"""Issue date
        :rtype: str
        """
        return self._DispatchDate

    @DispatchDate.setter
    def DispatchDate(self, DispatchDate):
        self._DispatchDate = DispatchDate

    @property
    def Registro(self):
        r"""address
        :rtype: str
        """
        return self._Registro

    @Registro.setter
    def Registro(self, Registro):
        self._Registro = Registro

    @property
    def PortraitImage(self):
        r"""Portrait image
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def DocOrigem(self):
        r"""Original identity information
        :rtype: str
        """
        return self._DocOrigem

    @DocOrigem.setter
    def DocOrigem(self, DocOrigem):
        self._DocOrigem = DocOrigem

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Nome = params.get("Nome")
        self._MemberShip = params.get("MemberShip")
        self._DataNascimento = params.get("DataNascimento")
        self._IssuingAgency = params.get("IssuingAgency")
        self._Fatorrh = params.get("Fatorrh")
        self._NaturalIDade = params.get("NaturalIDade")
        self._Observations = params.get("Observations")
        self._CPF = params.get("CPF")
        self._DNI = params.get("DNI")
        self._RegistroGeral = params.get("RegistroGeral")
        self._DispatchDate = params.get("DispatchDate")
        self._Registro = params.get("Registro")
        self._PortraitImage = params.get("PortraitImage")
        self._DocOrigem = params.get("DocOrigem")
        self._RequestId = params.get("RequestId")


class RecognizeBrazilRNEOCRRequest(AbstractModel):
    r"""RecognizeBrazilRNEOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :type ImageBase64: str
        :param _ImageUrl: URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :type ImageUrl: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :type BackImageUrl: str
        :param _ReturnHeadImage: Whether to return portrait photos.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._BackImageBase64 = None
        self._BackImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return portrait photos.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._BackImageUrl = params.get("BackImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilRNEOCRResponse(AbstractModel):
    r"""RecognizeBrazilRNEOCR response structure.

    """

    def __init__(self):
        r"""
        :param _RNE: The RNE (Registro Nacional de Estrangeiros) number.
        :type RNE: str
        :param _CLASSIFICATION: The classification of the RNE document.
        :type CLASSIFICATION: str
        :param _VALIDADE: The validity period (expiry date) of the RNE document.
        :type VALIDADE: str
        :param _NOME: The full name.
        :type NOME: str
        :param _Membership: Family information (parents' names).
        :type Membership: str
        :param _NACIONALIDADE: Nationality
        :type NACIONALIDADE: str
        :param _NATURALIDADE: Place of Birth
        :type NATURALIDADE: str
        :param _IssuingAgency: The issuing agency.
        :type IssuingAgency: str
        :param _DateOfBirth: Date of birth.
        :type DateOfBirth: str
        :param _Sex: Gender
        :type Sex: str
        :param _EntryDate: The date of entry into Brazil.
        :type EntryDate: str
        :param _VIA: The VIA (document version/sequence number).
        :type VIA: str
        :param _DispatchDate: The issue date.
        :type DispatchDate: str
        :param _MRZ: The machine readable zone (MRZ) code.
        :type MRZ: str
        :param _PortraitImage: PortraitImage base64
        :type PortraitImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RNE = None
        self._CLASSIFICATION = None
        self._VALIDADE = None
        self._NOME = None
        self._Membership = None
        self._NACIONALIDADE = None
        self._NATURALIDADE = None
        self._IssuingAgency = None
        self._DateOfBirth = None
        self._Sex = None
        self._EntryDate = None
        self._VIA = None
        self._DispatchDate = None
        self._MRZ = None
        self._PortraitImage = None
        self._RequestId = None

    @property
    def RNE(self):
        r"""The RNE (Registro Nacional de Estrangeiros) number.
        :rtype: str
        """
        return self._RNE

    @RNE.setter
    def RNE(self, RNE):
        self._RNE = RNE

    @property
    def CLASSIFICATION(self):
        r"""The classification of the RNE document.
        :rtype: str
        """
        return self._CLASSIFICATION

    @CLASSIFICATION.setter
    def CLASSIFICATION(self, CLASSIFICATION):
        self._CLASSIFICATION = CLASSIFICATION

    @property
    def VALIDADE(self):
        r"""The validity period (expiry date) of the RNE document.
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def NOME(self):
        r"""The full name.
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def Membership(self):
        r"""Family information (parents' names).
        :rtype: str
        """
        return self._Membership

    @Membership.setter
    def Membership(self, Membership):
        self._Membership = Membership

    @property
    def NACIONALIDADE(self):
        r"""Nationality
        :rtype: str
        """
        return self._NACIONALIDADE

    @NACIONALIDADE.setter
    def NACIONALIDADE(self, NACIONALIDADE):
        self._NACIONALIDADE = NACIONALIDADE

    @property
    def NATURALIDADE(self):
        r"""Place of Birth
        :rtype: str
        """
        return self._NATURALIDADE

    @NATURALIDADE.setter
    def NATURALIDADE(self, NATURALIDADE):
        self._NATURALIDADE = NATURALIDADE

    @property
    def IssuingAgency(self):
        r"""The issuing agency.
        :rtype: str
        """
        return self._IssuingAgency

    @IssuingAgency.setter
    def IssuingAgency(self, IssuingAgency):
        self._IssuingAgency = IssuingAgency

    @property
    def DateOfBirth(self):
        r"""Date of birth.
        :rtype: str
        """
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def EntryDate(self):
        r"""The date of entry into Brazil.
        :rtype: str
        """
        return self._EntryDate

    @EntryDate.setter
    def EntryDate(self, EntryDate):
        self._EntryDate = EntryDate

    @property
    def VIA(self):
        r"""The VIA (document version/sequence number).
        :rtype: str
        """
        return self._VIA

    @VIA.setter
    def VIA(self, VIA):
        self._VIA = VIA

    @property
    def DispatchDate(self):
        r"""The issue date.
        :rtype: str
        """
        return self._DispatchDate

    @DispatchDate.setter
    def DispatchDate(self, DispatchDate):
        self._DispatchDate = DispatchDate

    @property
    def MRZ(self):
        r"""The machine readable zone (MRZ) code.
        :rtype: str
        """
        return self._MRZ

    @MRZ.setter
    def MRZ(self, MRZ):
        self._MRZ = MRZ

    @property
    def PortraitImage(self):
        r"""PortraitImage base64
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RNE = params.get("RNE")
        self._CLASSIFICATION = params.get("CLASSIFICATION")
        self._VALIDADE = params.get("VALIDADE")
        self._NOME = params.get("NOME")
        self._Membership = params.get("Membership")
        self._NACIONALIDADE = params.get("NACIONALIDADE")
        self._NATURALIDADE = params.get("NATURALIDADE")
        self._IssuingAgency = params.get("IssuingAgency")
        self._DateOfBirth = params.get("DateOfBirth")
        self._Sex = params.get("Sex")
        self._EntryDate = params.get("EntryDate")
        self._VIA = params.get("VIA")
        self._DispatchDate = params.get("DispatchDate")
        self._MRZ = params.get("MRZ")
        self._PortraitImage = params.get("PortraitImage")
        self._RequestId = params.get("RequestId")


class RecognizeBrazilRNMOCRRequest(AbstractModel):
    r"""RecognizeBrazilRNMOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :type ImageBase64: str
        :param _ImageUrl: URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :type ImageUrl: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :type BackImageUrl: str
        :param _ReturnHeadImage: Whether to return portrait photos.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._BackImageBase64 = None
        self._BackImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. An ImageUrl and ImageBase64 must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download time does not exceed 3 seconds. The URL of the image stored in Tencent Cloud can ensure higher download speed and stability. It is recommended to store the image in Tencent Cloud. The speed and stability of the URL stored outside Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return portrait photos.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._BackImageUrl = params.get("BackImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeBrazilRNMOCRResponse(AbstractModel):
    r"""RecognizeBrazilRNMOCR response structure.

    """

    def __init__(self):
        r"""
        :param _SOBRENOME: Last name
        :type SOBRENOME: str
        :param _NOME: First name
        :type NOME: str
        :param _DATADENASCIMENTO: Date of Birth
        :type DATADENASCIMENTO: str
        :param _SEXO: Gender
        :type SEXO: str
        :param _MEMBERSHIP: Parents name
        :type MEMBERSHIP: str
        :param _NACIONALIDADE: Nationality
        :type NACIONALIDADE: str
        :param _VALIDADE: Expiry Date
        :type VALIDADE: str
        :param _RNM: RNM
        :type RNM: str
        :param _CPF: CPF
        :type CPF: str
        :param _CLASSIFICATION: Residence category
        :type CLASSIFICATION: str
        :param _PRAZODERESIDENCIA: Residence validity term
        :type PRAZODERESIDENCIA: str
        :param _ISSUANCE: Issue Date
        :type ISSUANCE: str
        :param _AMPAROLEGAL: Legal basis
        :type AMPAROLEGAL: str
        :param _MRZ: Machine readable zone code
        :type MRZ: str
        :param _PortraitImage: PortraitImage
        :type PortraitImage: str
        :param _PortraitImageBack: PortraitImage(Back)
        :type PortraitImageBack: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SOBRENOME = None
        self._NOME = None
        self._DATADENASCIMENTO = None
        self._SEXO = None
        self._MEMBERSHIP = None
        self._NACIONALIDADE = None
        self._VALIDADE = None
        self._RNM = None
        self._CPF = None
        self._CLASSIFICATION = None
        self._PRAZODERESIDENCIA = None
        self._ISSUANCE = None
        self._AMPAROLEGAL = None
        self._MRZ = None
        self._PortraitImage = None
        self._PortraitImageBack = None
        self._RequestId = None

    @property
    def SOBRENOME(self):
        r"""Last name
        :rtype: str
        """
        return self._SOBRENOME

    @SOBRENOME.setter
    def SOBRENOME(self, SOBRENOME):
        self._SOBRENOME = SOBRENOME

    @property
    def NOME(self):
        r"""First name
        :rtype: str
        """
        return self._NOME

    @NOME.setter
    def NOME(self, NOME):
        self._NOME = NOME

    @property
    def DATADENASCIMENTO(self):
        r"""Date of Birth
        :rtype: str
        """
        return self._DATADENASCIMENTO

    @DATADENASCIMENTO.setter
    def DATADENASCIMENTO(self, DATADENASCIMENTO):
        self._DATADENASCIMENTO = DATADENASCIMENTO

    @property
    def SEXO(self):
        r"""Gender
        :rtype: str
        """
        return self._SEXO

    @SEXO.setter
    def SEXO(self, SEXO):
        self._SEXO = SEXO

    @property
    def MEMBERSHIP(self):
        r"""Parents name
        :rtype: str
        """
        return self._MEMBERSHIP

    @MEMBERSHIP.setter
    def MEMBERSHIP(self, MEMBERSHIP):
        self._MEMBERSHIP = MEMBERSHIP

    @property
    def NACIONALIDADE(self):
        r"""Nationality
        :rtype: str
        """
        return self._NACIONALIDADE

    @NACIONALIDADE.setter
    def NACIONALIDADE(self, NACIONALIDADE):
        self._NACIONALIDADE = NACIONALIDADE

    @property
    def VALIDADE(self):
        r"""Expiry Date
        :rtype: str
        """
        return self._VALIDADE

    @VALIDADE.setter
    def VALIDADE(self, VALIDADE):
        self._VALIDADE = VALIDADE

    @property
    def RNM(self):
        r"""RNM
        :rtype: str
        """
        return self._RNM

    @RNM.setter
    def RNM(self, RNM):
        self._RNM = RNM

    @property
    def CPF(self):
        r"""CPF
        :rtype: str
        """
        return self._CPF

    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF

    @property
    def CLASSIFICATION(self):
        r"""Residence category
        :rtype: str
        """
        return self._CLASSIFICATION

    @CLASSIFICATION.setter
    def CLASSIFICATION(self, CLASSIFICATION):
        self._CLASSIFICATION = CLASSIFICATION

    @property
    def PRAZODERESIDENCIA(self):
        r"""Residence validity term
        :rtype: str
        """
        return self._PRAZODERESIDENCIA

    @PRAZODERESIDENCIA.setter
    def PRAZODERESIDENCIA(self, PRAZODERESIDENCIA):
        self._PRAZODERESIDENCIA = PRAZODERESIDENCIA

    @property
    def ISSUANCE(self):
        r"""Issue Date
        :rtype: str
        """
        return self._ISSUANCE

    @ISSUANCE.setter
    def ISSUANCE(self, ISSUANCE):
        self._ISSUANCE = ISSUANCE

    @property
    def AMPAROLEGAL(self):
        r"""Legal basis
        :rtype: str
        """
        return self._AMPAROLEGAL

    @AMPAROLEGAL.setter
    def AMPAROLEGAL(self, AMPAROLEGAL):
        self._AMPAROLEGAL = AMPAROLEGAL

    @property
    def MRZ(self):
        r"""Machine readable zone code
        :rtype: str
        """
        return self._MRZ

    @MRZ.setter
    def MRZ(self, MRZ):
        self._MRZ = MRZ

    @property
    def PortraitImage(self):
        r"""PortraitImage
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def PortraitImageBack(self):
        r"""PortraitImage(Back)
        :rtype: str
        """
        return self._PortraitImageBack

    @PortraitImageBack.setter
    def PortraitImageBack(self, PortraitImageBack):
        self._PortraitImageBack = PortraitImageBack

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SOBRENOME = params.get("SOBRENOME")
        self._NOME = params.get("NOME")
        self._DATADENASCIMENTO = params.get("DATADENASCIMENTO")
        self._SEXO = params.get("SEXO")
        self._MEMBERSHIP = params.get("MEMBERSHIP")
        self._NACIONALIDADE = params.get("NACIONALIDADE")
        self._VALIDADE = params.get("VALIDADE")
        self._RNM = params.get("RNM")
        self._CPF = params.get("CPF")
        self._CLASSIFICATION = params.get("CLASSIFICATION")
        self._PRAZODERESIDENCIA = params.get("PRAZODERESIDENCIA")
        self._ISSUANCE = params.get("ISSUANCE")
        self._AMPAROLEGAL = params.get("AMPAROLEGAL")
        self._MRZ = params.get("MRZ")
        self._PortraitImage = params.get("PortraitImage")
        self._PortraitImageBack = params.get("PortraitImageBack")
        self._RequestId = params.get("RequestId")


class RecognizeDetectCardCoordsRequest(AbstractModel):
    r"""RecognizeDetectCardCoords request structure.

    """

    def __init__(self):
        r"""
        :param _ImageUrl: URL of the image. Supported image formats: PNG, JPG, JPEG. GIF is not supported. The downloaded image must be no larger than 7 MB after Base64 encoding. Image download must complete within 3 seconds. Images stored in Tencent Cloud offer higher download speed and stability. We recommend storing images in Tencent Cloud. The speed and stability of URLs from non-Tencent Cloud storage may be affected.
        :type ImageUrl: str
        :param _ImageBase64: Base64-encoded image data. Supported image formats: PNG, JPG, JPEG. GIF is not supported. The image must be no larger than 7 MB after Base64 encoding. Image download must complete within 3 seconds. You must provide either ImageUrl or ImageBase64. If both are provided, ImageUrl will be used.
        :type ImageBase64: str
        """
        self._ImageUrl = None
        self._ImageBase64 = None

    @property
    def ImageUrl(self):
        r"""URL of the image. Supported image formats: PNG, JPG, JPEG. GIF is not supported. The downloaded image must be no larger than 7 MB after Base64 encoding. Image download must complete within 3 seconds. Images stored in Tencent Cloud offer higher download speed and stability. We recommend storing images in Tencent Cloud. The speed and stability of URLs from non-Tencent Cloud storage may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""Base64-encoded image data. Supported image formats: PNG, JPG, JPEG. GIF is not supported. The image must be no larger than 7 MB after Base64 encoding. Image download must complete within 3 seconds. You must provide either ImageUrl or ImageBase64. If both are provided, ImageUrl will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeDetectCardCoordsResponse(AbstractModel):
    r"""RecognizeDetectCardCoords response structure.

    """

    def __init__(self):
        r"""
        :param _ItemList: Coordinate information of the detected four corners of the card.
        :type ItemList: list of CoordsItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ItemList = None
        self._RequestId = None

    @property
    def ItemList(self):
        r"""Coordinate information of the detected four corners of the card.
        :rtype: list of CoordsItem
        """
        return self._ItemList

    @ItemList.setter
    def ItemList(self, ItemList):
        self._ItemList = ItemList

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ItemList") is not None:
            self._ItemList = []
            for item in params.get("ItemList"):
                obj = CoordsItem()
                obj._deserialize(item)
                self._ItemList.append(obj)
        self._RequestId = params.get("RequestId")


class RecognizeIndonesiaIDCardOCRRequest(AbstractModel):
    r"""RecognizeIndonesiaIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64 value of the image. Supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. Supported image size: the downloaded image after Base64 encoding is no more than 7M. Image download time is not more than 3 seconds. Either ImageUrl or ImageBase64 must be provided. If both are provided, only use ImageUrl.
        :type ImageBase64: str
        :param _ImageUrl: The Url address of the image. 
Supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. 
Supported image size: the downloaded image after Base64 encoding is no more than 7M. Image download time is no more than 3 seconds. 
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        :param _ReturnHeadImage: Whether to return the portrait photo.
If selected true, image restrictions are: Image size after encoding must not exceed 5M, jpg format long side pixel cannot exceed 4000, other formats image long edge pixel maximum of 2000. Short side pixel of all format images not less than 64.
Support PNG, jpg, JPEG, BMP, no support for GIF images.
If portrait matting fails, return an empty string.
        :type ReturnHeadImage: bool
        :param _Scene: Scene parameter, default value is V1
Available values:
V1
V2
        :type Scene: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None
        self._Scene = None

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. Supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. Supported image size: the downloaded image after Base64 encoding is no more than 7M. Image download time is not more than 3 seconds. Either ImageUrl or ImageBase64 must be provided. If both are provided, only use ImageUrl.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The Url address of the image. 
Supported image formats: PNG, JPG, JPEG. GIF format is not currently supported. 
Supported image size: the downloaded image after Base64 encoding is no more than 7M. Image download time is no more than 3 seconds. 
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the portrait photo.
If selected true, image restrictions are: Image size after encoding must not exceed 5M, jpg format long side pixel cannot exceed 4000, other formats image long edge pixel maximum of 2000. Short side pixel of all format images not less than 64.
Support PNG, jpg, JPEG, BMP, no support for GIF images.
If portrait matting fails, return an empty string.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def Scene(self):
        warnings.warn("parameter `Scene` is deprecated", DeprecationWarning) 

        r"""Scene parameter, default value is V1
Available values:
V1
V2
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        warnings.warn("parameter `Scene` is deprecated", DeprecationWarning) 

        self._Scene = Scene


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeIndonesiaIDCardOCRResponse(AbstractModel):
    r"""RecognizeIndonesiaIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _NIK: The Single Identity Number.
        :type NIK: str
        :param _Nama: The full name.
        :type Nama: str
        :param _TempatTglLahir: The place and date of birth.
        :type TempatTglLahir: str
        :param _JenisKelamin: The gender.
        :type JenisKelamin: str
        :param _GolDarah: The blood type.
        :type GolDarah: str
        :param _Alamat: The address.
        :type Alamat: str
        :param _RTRW: The neighborhood/community unit (RT/RW).
        :type RTRW: str
        :param _KelDesa: The village.
        :type KelDesa: str
        :param _Kecamatan: The region.
        :type Kecamatan: str
        :param _Agama: The religion.
        :type Agama: str
        :param _StatusPerkawinan: The marital status.
        :type StatusPerkawinan: str
        :param _Perkerjaan: The occupation.
        :type Perkerjaan: str
        :param _KewargaNegaraan: The nationality.
        :type KewargaNegaraan: str
        :param _BerlakuHingga: The expiry date.
        :type BerlakuHingga: str
        :param _IssuedDate: The issue date.
        :type IssuedDate: str
        :param _Photo: The portraitImage.
        :type Photo: str
        :param _Provinsi: The province.
        :type Provinsi: str
        :param _Kota: The city.
        :type Kota: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-8101 Alarm for document information format verification,
-8102 Alarm for document information consistency verification,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NIK = None
        self._Nama = None
        self._TempatTglLahir = None
        self._JenisKelamin = None
        self._GolDarah = None
        self._Alamat = None
        self._RTRW = None
        self._KelDesa = None
        self._Kecamatan = None
        self._Agama = None
        self._StatusPerkawinan = None
        self._Perkerjaan = None
        self._KewargaNegaraan = None
        self._BerlakuHingga = None
        self._IssuedDate = None
        self._Photo = None
        self._Provinsi = None
        self._Kota = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def NIK(self):
        r"""The Single Identity Number.
        :rtype: str
        """
        return self._NIK

    @NIK.setter
    def NIK(self, NIK):
        self._NIK = NIK

    @property
    def Nama(self):
        r"""The full name.
        :rtype: str
        """
        return self._Nama

    @Nama.setter
    def Nama(self, Nama):
        self._Nama = Nama

    @property
    def TempatTglLahir(self):
        r"""The place and date of birth.
        :rtype: str
        """
        return self._TempatTglLahir

    @TempatTglLahir.setter
    def TempatTglLahir(self, TempatTglLahir):
        self._TempatTglLahir = TempatTglLahir

    @property
    def JenisKelamin(self):
        r"""The gender.
        :rtype: str
        """
        return self._JenisKelamin

    @JenisKelamin.setter
    def JenisKelamin(self, JenisKelamin):
        self._JenisKelamin = JenisKelamin

    @property
    def GolDarah(self):
        r"""The blood type.
        :rtype: str
        """
        return self._GolDarah

    @GolDarah.setter
    def GolDarah(self, GolDarah):
        self._GolDarah = GolDarah

    @property
    def Alamat(self):
        r"""The address.
        :rtype: str
        """
        return self._Alamat

    @Alamat.setter
    def Alamat(self, Alamat):
        self._Alamat = Alamat

    @property
    def RTRW(self):
        r"""The neighborhood/community unit (RT/RW).
        :rtype: str
        """
        return self._RTRW

    @RTRW.setter
    def RTRW(self, RTRW):
        self._RTRW = RTRW

    @property
    def KelDesa(self):
        r"""The village.
        :rtype: str
        """
        return self._KelDesa

    @KelDesa.setter
    def KelDesa(self, KelDesa):
        self._KelDesa = KelDesa

    @property
    def Kecamatan(self):
        r"""The region.
        :rtype: str
        """
        return self._Kecamatan

    @Kecamatan.setter
    def Kecamatan(self, Kecamatan):
        self._Kecamatan = Kecamatan

    @property
    def Agama(self):
        r"""The religion.
        :rtype: str
        """
        return self._Agama

    @Agama.setter
    def Agama(self, Agama):
        self._Agama = Agama

    @property
    def StatusPerkawinan(self):
        r"""The marital status.
        :rtype: str
        """
        return self._StatusPerkawinan

    @StatusPerkawinan.setter
    def StatusPerkawinan(self, StatusPerkawinan):
        self._StatusPerkawinan = StatusPerkawinan

    @property
    def Perkerjaan(self):
        r"""The occupation.
        :rtype: str
        """
        return self._Perkerjaan

    @Perkerjaan.setter
    def Perkerjaan(self, Perkerjaan):
        self._Perkerjaan = Perkerjaan

    @property
    def KewargaNegaraan(self):
        r"""The nationality.
        :rtype: str
        """
        return self._KewargaNegaraan

    @KewargaNegaraan.setter
    def KewargaNegaraan(self, KewargaNegaraan):
        self._KewargaNegaraan = KewargaNegaraan

    @property
    def BerlakuHingga(self):
        r"""The expiry date.
        :rtype: str
        """
        return self._BerlakuHingga

    @BerlakuHingga.setter
    def BerlakuHingga(self, BerlakuHingga):
        self._BerlakuHingga = BerlakuHingga

    @property
    def IssuedDate(self):
        r"""The issue date.
        :rtype: str
        """
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def Photo(self):
        r"""The portraitImage.
        :rtype: str
        """
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

    @property
    def Provinsi(self):
        r"""The province.
        :rtype: str
        """
        return self._Provinsi

    @Provinsi.setter
    def Provinsi(self, Provinsi):
        self._Provinsi = Provinsi

    @property
    def Kota(self):
        r"""The city.
        :rtype: str
        """
        return self._Kota

    @Kota.setter
    def Kota(self, Kota):
        self._Kota = Kota

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-8101 Alarm for document information format verification,
-8102 Alarm for document information consistency verification,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NIK = params.get("NIK")
        self._Nama = params.get("Nama")
        self._TempatTglLahir = params.get("TempatTglLahir")
        self._JenisKelamin = params.get("JenisKelamin")
        self._GolDarah = params.get("GolDarah")
        self._Alamat = params.get("Alamat")
        self._RTRW = params.get("RTRW")
        self._KelDesa = params.get("KelDesa")
        self._Kecamatan = params.get("Kecamatan")
        self._Agama = params.get("Agama")
        self._StatusPerkawinan = params.get("StatusPerkawinan")
        self._Perkerjaan = params.get("Perkerjaan")
        self._KewargaNegaraan = params.get("KewargaNegaraan")
        self._BerlakuHingga = params.get("BerlakuHingga")
        self._IssuedDate = params.get("IssuedDate")
        self._Photo = params.get("Photo")
        self._Provinsi = params.get("Provinsi")
        self._Kota = params.get("Kota")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class RecognizeMacaoIDCardOCRRequest(AbstractModel):
    r"""RecognizeMacaoIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageUrl: The URL address of the image. 
Supported image formats: PNG, JPG, JPEG. Not support GIF yet.
Supported image size: The downloaded image should not exceed 7M. The image download takes no more than 3 seconds.Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :type ImageUrl: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. The GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :type BackImageUrl: str
        :param _ImageBase64: Base64 value of the image.Supported image formats: PNG, JPG, JPEG. Not support GIF yet.
Supported image size: The downloaded image should not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds.
One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type ImageBase64: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. The GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _Config: The following optional fields are of string type and are empty by default: 
RetImage: whether to return the processed image (base64 encrypted string); the value and meaning of RetImage are as follows: 1.portrait Return portrait image data 2."" Do not return image data SDK setting method reference: Config = Json.stringify({"RetImage":"portrait"}) API 3.0 Explorer setting method reference: Config = {"RetImage":"portrait" }
        :type Config: str
        """
        self._ImageUrl = None
        self._BackImageUrl = None
        self._ImageBase64 = None
        self._BackImageBase64 = None
        self._Config = None

    @property
    def ImageUrl(self):
        r"""The URL address of the image. 
Supported image formats: PNG, JPG, JPEG. Not support GIF yet.
Supported image size: The downloaded image should not exceed 7M. The image download takes no more than 3 seconds.Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. The GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def ImageBase64(self):
        r"""Base64 value of the image.Supported image formats: PNG, JPG, JPEG. Not support GIF yet.
Supported image size: The downloaded image should not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds.
One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. The GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def Config(self):
        r"""The following optional fields are of string type and are empty by default: 
RetImage: whether to return the processed image (base64 encrypted string); the value and meaning of RetImage are as follows: 1.portrait Return portrait image data 2."" Do not return image data SDK setting method reference: Config = Json.stringify({"RetImage":"portrait"}) API 3.0 Explorer setting method reference: Config = {"RetImage":"portrait" }
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageUrl = params.get("BackImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMacaoIDCardOCRResponse(AbstractModel):
    r"""RecognizeMacaoIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _CnLastName: Last name in Chinese
        :type CnLastName: str
        :param _EnLastName: Last name in English
        :type EnLastName: str
        :param _LastNameCode: Telecode of the last name in Chinese
        :type LastNameCode: str
        :param _CnFirstName: First name in Chinese
        :type CnFirstName: str
        :param _EnFirstName: First name in English
        :type EnFirstName: str
        :param _FirstNameCode: Telecode of the first name in Chinese
        :type FirstNameCode: str
        :param _ID: Identity card number
        :type ID: str
        :param _Birthday: Date of birth (DD-MM-YYYY)
        :type Birthday: str
        :param _Sex: Gender
        :type Sex: str
        :param _FirstIssueDate: Date of first issue (DD-MM-YYYY)
        :type FirstIssueDate: str
        :param _CurrentIssueDate: Date of issue (DD-MM-YYYY)
        :type CurrentIssueDate: str
        :param _ValidityPeriod: Validity period (DD-MM-YYYY)
        :type ValidityPeriod: str
        :param _Symbol: Document symbol
        :type Symbol: str
        :param _Height: Height (unit: meters)
        :type Height: str
        :param _RetImage: Processed image (Base64)
        :type RetImage: str
        :param _Angle: This field is deprecated and will always return null. Usage is not recommended.
        :type Angle: str
        :param _ResidentType: Resident type. 
Valid values: Permanent Resident Identity Card, Non-permanent Resident Identity Card.
        :type ResidentType: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CnLastName = None
        self._EnLastName = None
        self._LastNameCode = None
        self._CnFirstName = None
        self._EnFirstName = None
        self._FirstNameCode = None
        self._ID = None
        self._Birthday = None
        self._Sex = None
        self._FirstIssueDate = None
        self._CurrentIssueDate = None
        self._ValidityPeriod = None
        self._Symbol = None
        self._Height = None
        self._RetImage = None
        self._Angle = None
        self._ResidentType = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def CnLastName(self):
        r"""Last name in Chinese
        :rtype: str
        """
        return self._CnLastName

    @CnLastName.setter
    def CnLastName(self, CnLastName):
        self._CnLastName = CnLastName

    @property
    def EnLastName(self):
        r"""Last name in English
        :rtype: str
        """
        return self._EnLastName

    @EnLastName.setter
    def EnLastName(self, EnLastName):
        self._EnLastName = EnLastName

    @property
    def LastNameCode(self):
        r"""Telecode of the last name in Chinese
        :rtype: str
        """
        return self._LastNameCode

    @LastNameCode.setter
    def LastNameCode(self, LastNameCode):
        self._LastNameCode = LastNameCode

    @property
    def CnFirstName(self):
        r"""First name in Chinese
        :rtype: str
        """
        return self._CnFirstName

    @CnFirstName.setter
    def CnFirstName(self, CnFirstName):
        self._CnFirstName = CnFirstName

    @property
    def EnFirstName(self):
        r"""First name in English
        :rtype: str
        """
        return self._EnFirstName

    @EnFirstName.setter
    def EnFirstName(self, EnFirstName):
        self._EnFirstName = EnFirstName

    @property
    def FirstNameCode(self):
        r"""Telecode of the first name in Chinese
        :rtype: str
        """
        return self._FirstNameCode

    @FirstNameCode.setter
    def FirstNameCode(self, FirstNameCode):
        self._FirstNameCode = FirstNameCode

    @property
    def ID(self):
        r"""Identity card number
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Birthday(self):
        r"""Date of birth (DD-MM-YYYY)
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def FirstIssueDate(self):
        r"""Date of first issue (DD-MM-YYYY)
        :rtype: str
        """
        return self._FirstIssueDate

    @FirstIssueDate.setter
    def FirstIssueDate(self, FirstIssueDate):
        self._FirstIssueDate = FirstIssueDate

    @property
    def CurrentIssueDate(self):
        r"""Date of issue (DD-MM-YYYY)
        :rtype: str
        """
        return self._CurrentIssueDate

    @CurrentIssueDate.setter
    def CurrentIssueDate(self, CurrentIssueDate):
        self._CurrentIssueDate = CurrentIssueDate

    @property
    def ValidityPeriod(self):
        r"""Validity period (DD-MM-YYYY)
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def Symbol(self):
        r"""Document symbol
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def Height(self):
        r"""Height (unit: meters)
        :rtype: str
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def RetImage(self):
        r"""Processed image (Base64)
        :rtype: str
        """
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage

    @property
    def Angle(self):
        warnings.warn("parameter `Angle` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return null. Usage is not recommended.
        :rtype: str
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        warnings.warn("parameter `Angle` is deprecated", DeprecationWarning) 

        self._Angle = Angle

    @property
    def ResidentType(self):
        r"""Resident type. 
Valid values: Permanent Resident Identity Card, Non-permanent Resident Identity Card.
        :rtype: str
        """
        return self._ResidentType

    @ResidentType.setter
    def ResidentType(self, ResidentType):
        self._ResidentType = ResidentType

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CnLastName = params.get("CnLastName")
        self._EnLastName = params.get("EnLastName")
        self._LastNameCode = params.get("LastNameCode")
        self._CnFirstName = params.get("CnFirstName")
        self._EnFirstName = params.get("EnFirstName")
        self._FirstNameCode = params.get("FirstNameCode")
        self._ID = params.get("ID")
        self._Birthday = params.get("Birthday")
        self._Sex = params.get("Sex")
        self._FirstIssueDate = params.get("FirstIssueDate")
        self._CurrentIssueDate = params.get("CurrentIssueDate")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._Symbol = params.get("Symbol")
        self._Height = params.get("Height")
        self._RetImage = params.get("RetImage")
        self._Angle = params.get("Angle")
        self._ResidentType = params.get("ResidentType")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class RecognizeMainlandIDCardOCRRequest(AbstractModel):
    r"""RecognizeMainlandIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64 value of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL address of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :type ImageUrl: str
        :param _CardSide: FRONT: The side of the ID card with the photo (portrait side), BACK: The side of the ID card with the national emblem (national emblem side). If this parameter is not filled in, the front and back of the ID card will be automatically determined for you.
        :type CardSide: str
        :param _CropPortrait: Whether to return the ID card portrait, the default is false
        :type CropPortrait: bool
        :param _CropIdCard: Whether to enable ID card photo cropping (removing excess edges outside the ID, automatically correcting the shooting angle), the default value is false
        :type CropIdCard: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None
        self._CropPortrait = None
        self._CropIdCard = None

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL address of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CardSide(self):
        r"""FRONT: The side of the ID card with the photo (portrait side), BACK: The side of the ID card with the national emblem (national emblem side). If this parameter is not filled in, the front and back of the ID card will be automatically determined for you.
        :rtype: str
        """
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide

    @property
    def CropPortrait(self):
        r"""Whether to return the ID card portrait, the default is false
        :rtype: bool
        """
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait

    @property
    def CropIdCard(self):
        r"""Whether to enable ID card photo cropping (removing excess edges outside the ID, automatically correcting the shooting angle), the default value is false
        :rtype: bool
        """
        return self._CropIdCard

    @CropIdCard.setter
    def CropIdCard(self, CropIdCard):
        self._CropIdCard = CropIdCard


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        self._CropPortrait = params.get("CropPortrait")
        self._CropIdCard = params.get("CropIdCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMainlandIDCardOCRResponse(AbstractModel):
    r"""RecognizeMainlandIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name((portrait side))
        :type Name: str
        :param _Sex: Gender (portrait side)
        :type Sex: str
        :param _Nation: Ethnicity (portrait side)
        :type Nation: str
        :param _Birth: Date of birth (portrait side)
        :type Birth: str
        :param _Address: Address(portrait side)
        :type Address: str
        :param _IdNum: ID number (portrait side)
        :type IdNum: str
        :param _Authority: Issuing authority (national emblem side)
        :type Authority: str
        :param _ValidDate: Validity period (national emblem side)
        :type ValidDate: str
        :param _WarnCardInfos: Warning information for the ID card. Valid warning codes: 
-9101 (incomplete card border), 
-9102 (photocopied document), 
-9103 (re-photographed document), 
-9104 (PS-altered document), 
-9107 (reflective document), 
-9108 (blurry image), 
-9109 (warning capability not enabled).
        :type WarnCardInfos: list of int
        :param _PortraitImage: Portrait image base64
        :type PortraitImage: str
        :param _IdCardImage: ID card photo cropping results base64
        :type IdCardImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Nation = None
        self._Birth = None
        self._Address = None
        self._IdNum = None
        self._Authority = None
        self._ValidDate = None
        self._WarnCardInfos = None
        self._PortraitImage = None
        self._IdCardImage = None
        self._RequestId = None

    @property
    def Name(self):
        r"""Name((portrait side))
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        r"""Gender (portrait side)
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nation(self):
        r"""Ethnicity (portrait side)
        :rtype: str
        """
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Birth(self):
        r"""Date of birth (portrait side)
        :rtype: str
        """
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        r"""Address(portrait side)
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdNum(self):
        r"""ID number (portrait side)
        :rtype: str
        """
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Authority(self):
        r"""Issuing authority (national emblem side)
        :rtype: str
        """
        return self._Authority

    @Authority.setter
    def Authority(self, Authority):
        self._Authority = Authority

    @property
    def ValidDate(self):
        r"""Validity period (national emblem side)
        :rtype: str
        """
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def WarnCardInfos(self):
        r"""Warning information for the ID card. Valid warning codes: 
-9101 (incomplete card border), 
-9102 (photocopied document), 
-9103 (re-photographed document), 
-9104 (PS-altered document), 
-9107 (reflective document), 
-9108 (blurry image), 
-9109 (warning capability not enabled).
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def PortraitImage(self):
        r"""Portrait image base64
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def IdCardImage(self):
        r"""ID card photo cropping results base64
        :rtype: str
        """
        return self._IdCardImage

    @IdCardImage.setter
    def IdCardImage(self, IdCardImage):
        self._IdCardImage = IdCardImage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Nation = params.get("Nation")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._IdNum = params.get("IdNum")
        self._Authority = params.get("Authority")
        self._ValidDate = params.get("ValidDate")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._PortraitImage = params.get("PortraitImage")
        self._IdCardImage = params.get("IdCardImage")
        self._RequestId = params.get("RequestId")


class RecognizeMexicoVTIDRequest(AbstractModel):
    r"""RecognizeMexicoVTID request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :type ImageBase64: str
        :param _ImageUrl: URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :type ImageUrl: str
        :param _ReturnHeadImage: Whether to return portrait photos.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""Base64 value of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image downloading time should not exceed 3 seconds.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""URL address of the image. Supported image formats: PNG, JPG, JPEG, GIF format is not supported yet. Supported image size: The downloaded image should not exceed 7M after Base64 encoding. Image download time should not exceed 3 seconds. URLs of images stored in Tencent Cloud can guarantee higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The speed and stability of URLs not stored in Tencent Cloud may be affected to a certain extent.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return portrait photos.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMexicoVTIDResponse(AbstractModel):
    r"""RecognizeMexicoVTID response structure.

    """

    def __init__(self):
        r"""
        :param _Name: The full name.
        :type Name: str
        :param _Sex: Gender.
        :type Sex: str
        :param _Address: Address
        :type Address: str
        :param _VotePIN: Vote PIN Code
        :type VotePIN: str
        :param _CURP: Unique Population Registry Code
        :type CURP: str
        :param _Birth: Date of birth.
        :type Birth: str
        :param _SECCION: Section Number
        :type SECCION: str
        :param _IssueDate: IssueDate
        :type IssueDate: str
        :param _ValidDate: The validity period (expiration date).
        :type ValidDate: str
        :param _State: State
        :type State: str
        :param _City: City
        :type City: str
        :param _Locality: Locality
        :type Locality: str
        :param _EMISION: Edition
        :type EMISION: str
        :param _PortraitImage: Portrait image base64
        :type PortraitImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Address = None
        self._VotePIN = None
        self._CURP = None
        self._Birth = None
        self._SECCION = None
        self._IssueDate = None
        self._ValidDate = None
        self._State = None
        self._City = None
        self._Locality = None
        self._EMISION = None
        self._PortraitImage = None
        self._RequestId = None

    @property
    def Name(self):
        r"""The full name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        r"""Gender.
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Address(self):
        r"""Address
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def VotePIN(self):
        r"""Vote PIN Code
        :rtype: str
        """
        return self._VotePIN

    @VotePIN.setter
    def VotePIN(self, VotePIN):
        self._VotePIN = VotePIN

    @property
    def CURP(self):
        r"""Unique Population Registry Code
        :rtype: str
        """
        return self._CURP

    @CURP.setter
    def CURP(self, CURP):
        self._CURP = CURP

    @property
    def Birth(self):
        r"""Date of birth.
        :rtype: str
        """
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def SECCION(self):
        r"""Section Number
        :rtype: str
        """
        return self._SECCION

    @SECCION.setter
    def SECCION(self, SECCION):
        self._SECCION = SECCION

    @property
    def IssueDate(self):
        r"""IssueDate
        :rtype: str
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def ValidDate(self):
        r"""The validity period (expiration date).
        :rtype: str
        """
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def State(self):
        r"""State
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def City(self):
        r"""City
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Locality(self):
        r"""Locality
        :rtype: str
        """
        return self._Locality

    @Locality.setter
    def Locality(self, Locality):
        self._Locality = Locality

    @property
    def EMISION(self):
        r"""Edition
        :rtype: str
        """
        return self._EMISION

    @EMISION.setter
    def EMISION(self, EMISION):
        self._EMISION = EMISION

    @property
    def PortraitImage(self):
        r"""Portrait image base64
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Address = params.get("Address")
        self._VotePIN = params.get("VotePIN")
        self._CURP = params.get("CURP")
        self._Birth = params.get("Birth")
        self._SECCION = params.get("SECCION")
        self._IssueDate = params.get("IssueDate")
        self._ValidDate = params.get("ValidDate")
        self._State = params.get("State")
        self._City = params.get("City")
        self._Locality = params.get("Locality")
        self._EMISION = params.get("EMISION")
        self._PortraitImage = params.get("PortraitImage")
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesDrivingLicenseOCRRequest(AbstractModel):
    r"""RecognizePhilippinesDrivingLicenseOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        :param _ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesDrivingLicenseOCRResponse(AbstractModel):
    r"""RecognizePhilippinesDrivingLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Name: Full name of the license holder.
        :type Name: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: Last name / surname of the license holder.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: First name of the license holder.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: Middle name of the license holder.
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Nationality: Nationality of the license holder.
        :type Nationality: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Sex: Gender
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: Address of the license holder.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNo: Driver's license number.
        :type LicenseNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _ExpiresDate: Expiration date of the driver's license.
        :type ExpiresDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _AgencyCode: Code of the issuing agency.
        :type AgencyCode: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: Date of birth of the license holder.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._Name = None
        self._LastName = None
        self._FirstName = None
        self._MiddleName = None
        self._Nationality = None
        self._Sex = None
        self._Address = None
        self._LicenseNo = None
        self._ExpiresDate = None
        self._AgencyCode = None
        self._Birthday = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        r"""The Base64-encoded identity photo.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def Name(self):
        r"""Full name of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LastName(self):
        r"""Last name / surname of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        r"""First name of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def MiddleName(self):
        r"""Middle name of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def Nationality(self):
        r"""Nationality of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Sex(self):
        r"""Gender
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Address(self):
        r"""Address of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LicenseNo(self):
        r"""Driver's license number.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._LicenseNo

    @LicenseNo.setter
    def LicenseNo(self, LicenseNo):
        self._LicenseNo = LicenseNo

    @property
    def ExpiresDate(self):
        r"""Expiration date of the driver's license.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._ExpiresDate

    @ExpiresDate.setter
    def ExpiresDate(self, ExpiresDate):
        self._ExpiresDate = ExpiresDate

    @property
    def AgencyCode(self):
        r"""Code of the issuing agency.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._AgencyCode

    @AgencyCode.setter
    def AgencyCode(self, AgencyCode):
        self._AgencyCode = AgencyCode

    @property
    def Birthday(self):
        r"""Date of birth of the license holder.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("Name") is not None:
            self._Name = TextDetectionResult()
            self._Name._deserialize(params.get("Name"))
        if params.get("LastName") is not None:
            self._LastName = TextDetectionResult()
            self._LastName._deserialize(params.get("LastName"))
        if params.get("FirstName") is not None:
            self._FirstName = TextDetectionResult()
            self._FirstName._deserialize(params.get("FirstName"))
        if params.get("MiddleName") is not None:
            self._MiddleName = TextDetectionResult()
            self._MiddleName._deserialize(params.get("MiddleName"))
        if params.get("Nationality") is not None:
            self._Nationality = TextDetectionResult()
            self._Nationality._deserialize(params.get("Nationality"))
        if params.get("Sex") is not None:
            self._Sex = TextDetectionResult()
            self._Sex._deserialize(params.get("Sex"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("LicenseNo") is not None:
            self._LicenseNo = TextDetectionResult()
            self._LicenseNo._deserialize(params.get("LicenseNo"))
        if params.get("ExpiresDate") is not None:
            self._ExpiresDate = TextDetectionResult()
            self._ExpiresDate._deserialize(params.get("ExpiresDate"))
        if params.get("AgencyCode") is not None:
            self._AgencyCode = TextDetectionResult()
            self._AgencyCode._deserialize(params.get("AgencyCode"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesSssIDOCRRequest(AbstractModel):
    r"""RecognizePhilippinesSssIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesSssIDOCRResponse(AbstractModel):
    r"""RecognizePhilippinesSssIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: The license number (SSSID number).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: The full name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._LicenseNumber = None
        self._FullName = None
        self._Birthday = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        r"""The Base64-encoded identity photo.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def LicenseNumber(self):
        r"""The license number (SSSID number).
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        r"""The full name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Birthday(self):
        r"""The date of birth.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self._LicenseNumber = TextDetectionResult()
            self._LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self._FullName = TextDetectionResult()
            self._FullName._deserialize(params.get("FullName"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesTinIDOCRRequest(AbstractModel):
    r"""RecognizePhilippinesTinIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesTinIDOCRResponse(AbstractModel):
    r"""RecognizePhilippinesTinIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: The tax identification number (TIN).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: The full name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The birth date.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _IssueDate: The issue date.
        :type IssueDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._LicenseNumber = None
        self._FullName = None
        self._Address = None
        self._Birthday = None
        self._IssueDate = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        r"""The Base64-encoded identity photo.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def LicenseNumber(self):
        r"""The tax identification number (TIN).
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        r"""The full name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Address(self):
        r"""The address.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        r"""The birth date.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueDate(self):
        r"""The issue date.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self._LicenseNumber = TextDetectionResult()
            self._LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self._FullName = TextDetectionResult()
            self._FullName._deserialize(params.get("FullName"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("IssueDate") is not None:
            self._IssueDate = TextDetectionResult()
            self._IssueDate._deserialize(params.get("IssueDate"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesUMIDOCRRequest(AbstractModel):
    r"""RecognizePhilippinesUMIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesUMIDOCRResponse(AbstractModel):
    r"""RecognizePhilippinesUMIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Surname: The surname.
        :type Surname: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: The middle name.
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _GivenName: The given name.
        :type GivenName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _CRN: The common reference number (CRN).
        :type CRN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Sex: The gender.
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Surname = None
        self._MiddleName = None
        self._GivenName = None
        self._Address = None
        self._Birthday = None
        self._CRN = None
        self._Sex = None
        self._HeadPortrait = None
        self._RequestId = None

    @property
    def Surname(self):
        r"""The surname.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def MiddleName(self):
        r"""The middle name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def GivenName(self):
        r"""The given name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Address(self):
        r"""The address.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        r"""The date of birth.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def CRN(self):
        r"""The common reference number (CRN).
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._CRN

    @CRN.setter
    def CRN(self, CRN):
        self._CRN = CRN

    @property
    def Sex(self):
        r"""The gender.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def HeadPortrait(self):
        r"""The Base64-encoded identity photo.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Surname") is not None:
            self._Surname = TextDetectionResult()
            self._Surname._deserialize(params.get("Surname"))
        if params.get("MiddleName") is not None:
            self._MiddleName = TextDetectionResult()
            self._MiddleName._deserialize(params.get("MiddleName"))
        if params.get("GivenName") is not None:
            self._GivenName = TextDetectionResult()
            self._GivenName._deserialize(params.get("GivenName"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("CRN") is not None:
            self._CRN = TextDetectionResult()
            self._CRN._deserialize(params.get("CRN"))
        if params.get("Sex") is not None:
            self._Sex = TextDetectionResult()
            self._Sex._deserialize(params.get("Sex"))
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesVoteIDOCRRequest(AbstractModel):
    r"""RecognizePhilippinesVoteIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        r"""Whether to return the identity photo.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesVoteIDOCRResponse(AbstractModel):
    r"""RecognizePhilippinesVoteIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _VIN: The voter's identification number (VIN).
        :type VIN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: The last name.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: The first name.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: 
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _CivilStatus: The civil status.
        :type CivilStatus: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Citizenship: The citizenship.
        :type Citizenship: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _PrecinctNo: The precinct.
        :type PrecinctNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._VIN = None
        self._LastName = None
        self._FirstName = None
        self._MiddleName = None
        self._Birthday = None
        self._CivilStatus = None
        self._Citizenship = None
        self._Address = None
        self._PrecinctNo = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        r"""The Base64-encoded identity photo.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def VIN(self):
        r"""The voter's identification number (VIN).
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def LastName(self):
        r"""The last name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        r"""The first name.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def MiddleName(self):
        r"""
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def Birthday(self):
        r"""The date of birth.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def CivilStatus(self):
        r"""The civil status.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._CivilStatus

    @CivilStatus.setter
    def CivilStatus(self, CivilStatus):
        self._CivilStatus = CivilStatus

    @property
    def Citizenship(self):
        r"""The citizenship.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Citizenship

    @Citizenship.setter
    def Citizenship(self, Citizenship):
        self._Citizenship = Citizenship

    @property
    def Address(self):
        r"""The address.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def PrecinctNo(self):
        r"""The precinct.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        """
        return self._PrecinctNo

    @PrecinctNo.setter
    def PrecinctNo(self, PrecinctNo):
        self._PrecinctNo = PrecinctNo

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("VIN") is not None:
            self._VIN = TextDetectionResult()
            self._VIN._deserialize(params.get("VIN"))
        if params.get("LastName") is not None:
            self._LastName = TextDetectionResult()
            self._LastName._deserialize(params.get("LastName"))
        if params.get("FirstName") is not None:
            self._FirstName = TextDetectionResult()
            self._FirstName._deserialize(params.get("FirstName"))
        if params.get("MiddleName") is not None:
            self._MiddleName = TextDetectionResult()
            self._MiddleName._deserialize(params.get("MiddleName"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("CivilStatus") is not None:
            self._CivilStatus = TextDetectionResult()
            self._CivilStatus._deserialize(params.get("CivilStatus"))
        if params.get("Citizenship") is not None:
            self._Citizenship = TextDetectionResult()
            self._Citizenship._deserialize(params.get("Citizenship"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("PrecinctNo") is not None:
            self._PrecinctNo = TextDetectionResult()
            self._PrecinctNo._deserialize(params.get("PrecinctNo"))
        self._RequestId = params.get("RequestId")


class RecognizeSingaporeIDCardOCRRequest(AbstractModel):
    r"""RecognizeSingaporeIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64 value of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type ImageBase64: str
        :param _ImageUrl: The URL address of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :type ImageUrl: str
        :param _ReturnHeadImage: Whether to return portrait photos.
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        r"""The Base64 value of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL address of the image. The image is required to be no larger than 7M after Base64 encoding, and the resolution is recommended to be 500*800 or above. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies at least 2/3 of the picture. It is recommended that images be stored in Tencent Cloud to ensure higher download speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        r"""Whether to return portrait photos.
        :rtype: bool
        """
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeSingaporeIDCardOCRResponse(AbstractModel):
    r"""RecognizeSingaporeIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ChName: Chinese name
        :type ChName: str
        :param _EnName: English name
        :type EnName: str
        :param _Sex: Gender
        :type Sex: str
        :param _CountryOfBirth: Country of birth
        :type CountryOfBirth: str
        :param _Birthday: Date of birth
        :type Birthday: str
        :param _Address: Address (back side)
        :type Address: str
        :param _ID: ID number
        :type ID: str
        :param _Race: Nationality(back side)
        :type Race: str
        :param _NRICCode: NRIC code(back side)
        :type NRICCode: str
        :param _PostCode: Postal code (back side)
        :type PostCode: str
        :param _DateOfExpiration: Date of Expiration(back side)
        :type DateOfExpiration: str
        :param _DateOfIssue: Date of issue(back side)
        :type DateOfIssue: str
        :param _Photo: Head image 
        :type Photo: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ChName = None
        self._EnName = None
        self._Sex = None
        self._CountryOfBirth = None
        self._Birthday = None
        self._Address = None
        self._ID = None
        self._Race = None
        self._NRICCode = None
        self._PostCode = None
        self._DateOfExpiration = None
        self._DateOfIssue = None
        self._Photo = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def ChName(self):
        r"""Chinese name
        :rtype: str
        """
        return self._ChName

    @ChName.setter
    def ChName(self, ChName):
        self._ChName = ChName

    @property
    def EnName(self):
        r"""English name
        :rtype: str
        """
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def Sex(self):
        r"""Gender
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def CountryOfBirth(self):
        r"""Country of birth
        :rtype: str
        """
        return self._CountryOfBirth

    @CountryOfBirth.setter
    def CountryOfBirth(self, CountryOfBirth):
        self._CountryOfBirth = CountryOfBirth

    @property
    def Birthday(self):
        r"""Date of birth
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Address(self):
        r"""Address (back side)
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ID(self):
        r"""ID number
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Race(self):
        r"""Nationality(back side)
        :rtype: str
        """
        return self._Race

    @Race.setter
    def Race(self, Race):
        self._Race = Race

    @property
    def NRICCode(self):
        r"""NRIC code(back side)
        :rtype: str
        """
        return self._NRICCode

    @NRICCode.setter
    def NRICCode(self, NRICCode):
        self._NRICCode = NRICCode

    @property
    def PostCode(self):
        r"""Postal code (back side)
        :rtype: str
        """
        return self._PostCode

    @PostCode.setter
    def PostCode(self, PostCode):
        self._PostCode = PostCode

    @property
    def DateOfExpiration(self):
        r"""Date of Expiration(back side)
        :rtype: str
        """
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def DateOfIssue(self):
        r"""Date of issue(back side)
        :rtype: str
        """
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue

    @property
    def Photo(self):
        r"""Head image 
        :rtype: str
        """
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ChName = params.get("ChName")
        self._EnName = params.get("EnName")
        self._Sex = params.get("Sex")
        self._CountryOfBirth = params.get("CountryOfBirth")
        self._Birthday = params.get("Birthday")
        self._Address = params.get("Address")
        self._ID = params.get("ID")
        self._Race = params.get("Race")
        self._NRICCode = params.get("NRICCode")
        self._PostCode = params.get("PostCode")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._DateOfIssue = params.get("DateOfIssue")
        self._Photo = params.get("Photo")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class RecognizeThaiIDCardOCRRequest(AbstractModel):
    r"""RecognizeThaiIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param _BackImageBase64: Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :type BackImageBase64: str
        :param _ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        :param _BackImageUrl: The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :type BackImageUrl: str
        :param _CropPortrait: Whether to crop the profile photo. The default value is `false`, meaning not to return the Base64-encoded value of the profile photo on the Thai identity card.
When this parameter is set to `true`, the Base64-encoded value of the profile photo on the Thai identity card after rotation correction is returned.
        :type CropPortrait: bool
        """
        self._ImageBase64 = None
        self._BackImageBase64 = None
        self._ImageUrl = None
        self._BackImageUrl = None
        self._CropPortrait = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def BackImageBase64(self):
        r"""Base64 value of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. One of ImageUrl and ImageBase64 of the image must be provided. If both are provided, only ImageUrl will be used.
        :rtype: str
        """
        return self._BackImageBase64

    @BackImageBase64.setter
    def BackImageBase64(self, BackImageBase64):
        self._BackImageBase64 = BackImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def BackImageUrl(self):
        r"""The URL address of the image on the back of the card. Supported image formats: PNG, JPG, JPEG. GIF format is not supported yet. Supported image size: The downloaded image does not exceed 7M after Base64 encoding. The image download takes no more than 3 seconds. Storing images in Tencent Cloud URLs can ensure higher download speed and stability. It is recommended that images be stored in Tencent Cloud. The URL speed and stability of non-Tencent cloud storage may be affected to a certain extent.
        :rtype: str
        """
        return self._BackImageUrl

    @BackImageUrl.setter
    def BackImageUrl(self, BackImageUrl):
        self._BackImageUrl = BackImageUrl

    @property
    def CropPortrait(self):
        r"""Whether to crop the profile photo. The default value is `false`, meaning not to return the Base64-encoded value of the profile photo on the Thai identity card.
When this parameter is set to `true`, the Base64-encoded value of the profile photo on the Thai identity card after rotation correction is returned.
        :rtype: bool
        """
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._BackImageBase64 = params.get("BackImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._BackImageUrl = params.get("BackImageUrl")
        self._CropPortrait = params.get("CropPortrait")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeThaiIDCardOCRResponse(AbstractModel):
    r"""RecognizeThaiIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: ID card number
        :type ID: str
        :param _ThaiName: Name in Thai
        :type ThaiName: str
        :param _EnFirstName: First name in English
        :type EnFirstName: str
        :param _EnLastName: Last name in English
        :type EnLastName: str
        :param _IssueDate: Date of issue in Thai
        :type IssueDate: str
        :param _ExpirationDate: Expiration date in Thai
        :type ExpirationDate: str
        :param _EnIssueDate: Date of issue in English
        :type EnIssueDate: str
        :param _EnExpirationDate: Expiration date in English
        :type EnExpirationDate: str
        :param _Birthday: Date of birth in Thai
        :type Birthday: str
        :param _EnBirthday: Date of birth in English
        :type EnBirthday: str
        :param _Religion: Religion
        :type Religion: str
        :param _SerialNumber: Serial number
        :type SerialNumber: str
        :param _Address: Address
        :type Address: str
        :param _LaserID: Laser ID on the back of the card.
        :type LaserID: str
        :param _PortraitImage: Identity photo
        :type PortraitImage: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _AdvancedInfo: This field is deprecated and will always return "1". Usage is not recommended.
        :type AdvancedInfo: str
        :param _CardCount: The number of cards detected in the input image provided via ImageBase64 parameter.(Currently supported only in ap-bangkok region)
        :type CardCount: int
        :param _IsComplete: The card information field complete or not
true: complete; false: incomplete
        :type IsComplete: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._ThaiName = None
        self._EnFirstName = None
        self._EnLastName = None
        self._IssueDate = None
        self._ExpirationDate = None
        self._EnIssueDate = None
        self._EnExpirationDate = None
        self._Birthday = None
        self._EnBirthday = None
        self._Religion = None
        self._SerialNumber = None
        self._Address = None
        self._LaserID = None
        self._PortraitImage = None
        self._WarnCardInfos = None
        self._AdvancedInfo = None
        self._CardCount = None
        self._IsComplete = None
        self._RequestId = None

    @property
    def ID(self):
        r"""ID card number
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ThaiName(self):
        r"""Name in Thai
        :rtype: str
        """
        return self._ThaiName

    @ThaiName.setter
    def ThaiName(self, ThaiName):
        self._ThaiName = ThaiName

    @property
    def EnFirstName(self):
        r"""First name in English
        :rtype: str
        """
        return self._EnFirstName

    @EnFirstName.setter
    def EnFirstName(self, EnFirstName):
        self._EnFirstName = EnFirstName

    @property
    def EnLastName(self):
        r"""Last name in English
        :rtype: str
        """
        return self._EnLastName

    @EnLastName.setter
    def EnLastName(self, EnLastName):
        self._EnLastName = EnLastName

    @property
    def IssueDate(self):
        r"""Date of issue in Thai
        :rtype: str
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def ExpirationDate(self):
        r"""Expiration date in Thai
        :rtype: str
        """
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def EnIssueDate(self):
        r"""Date of issue in English
        :rtype: str
        """
        return self._EnIssueDate

    @EnIssueDate.setter
    def EnIssueDate(self, EnIssueDate):
        self._EnIssueDate = EnIssueDate

    @property
    def EnExpirationDate(self):
        r"""Expiration date in English
        :rtype: str
        """
        return self._EnExpirationDate

    @EnExpirationDate.setter
    def EnExpirationDate(self, EnExpirationDate):
        self._EnExpirationDate = EnExpirationDate

    @property
    def Birthday(self):
        r"""Date of birth in Thai
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def EnBirthday(self):
        r"""Date of birth in English
        :rtype: str
        """
        return self._EnBirthday

    @EnBirthday.setter
    def EnBirthday(self, EnBirthday):
        self._EnBirthday = EnBirthday

    @property
    def Religion(self):
        r"""Religion
        :rtype: str
        """
        return self._Religion

    @Religion.setter
    def Religion(self, Religion):
        self._Religion = Religion

    @property
    def SerialNumber(self):
        r"""Serial number
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def Address(self):
        r"""Address
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LaserID(self):
        r"""Laser ID on the back of the card.
        :rtype: str
        """
        return self._LaserID

    @LaserID.setter
    def LaserID(self, LaserID):
        self._LaserID = LaserID

    @property
    def PortraitImage(self):
        r"""Identity photo
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def AdvancedInfo(self):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return "1". Usage is not recommended.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        self._AdvancedInfo = AdvancedInfo

    @property
    def CardCount(self):
        r"""The number of cards detected in the input image provided via ImageBase64 parameter.(Currently supported only in ap-bangkok region)
        :rtype: int
        """
        return self._CardCount

    @CardCount.setter
    def CardCount(self, CardCount):
        self._CardCount = CardCount

    @property
    def IsComplete(self):
        r"""The card information field complete or not
true: complete; false: incomplete
        :rtype: bool
        """
        return self._IsComplete

    @IsComplete.setter
    def IsComplete(self, IsComplete):
        self._IsComplete = IsComplete

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ThaiName = params.get("ThaiName")
        self._EnFirstName = params.get("EnFirstName")
        self._EnLastName = params.get("EnLastName")
        self._IssueDate = params.get("IssueDate")
        self._ExpirationDate = params.get("ExpirationDate")
        self._EnIssueDate = params.get("EnIssueDate")
        self._EnExpirationDate = params.get("EnExpirationDate")
        self._Birthday = params.get("Birthday")
        self._EnBirthday = params.get("EnBirthday")
        self._Religion = params.get("Religion")
        self._SerialNumber = params.get("SerialNumber")
        self._Address = params.get("Address")
        self._LaserID = params.get("LaserID")
        self._PortraitImage = params.get("PortraitImage")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._CardCount = params.get("CardCount")
        self._IsComplete = params.get("IsComplete")
        self._RequestId = params.get("RequestId")


class RecognizeThaiPinkCardRequest(AbstractModel):
    r"""RecognizeThaiPinkCard request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        :param _CropPortrait: Whether to crop the profile photo. The default value is `false`, meaning not to return the Base64-encoded value of the profile photo on the Thai identity card.
When this parameter is set to `true`, the Base64-encoded value of the profile photo on the Thai identity card after rotation correction is returned.
        :type CropPortrait: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CropPortrait = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CropPortrait(self):
        r"""Whether to crop the profile photo. The default value is `false`, meaning not to return the Base64-encoded value of the profile photo on the Thai identity card.
When this parameter is set to `true`, the Base64-encoded value of the profile photo on the Thai identity card after rotation correction is returned.
        :rtype: bool
        """
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CropPortrait = params.get("CropPortrait")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeThaiPinkCardResponse(AbstractModel):
    r"""RecognizeThaiPinkCard response structure.

    """

    def __init__(self):
        r"""
        :param _Country: Country
        :type Country: str
        :param _IDNumber: ID number
        :type IDNumber: str
        :param _ThaiName: Name in Thai
        :type ThaiName: str
        :param _EnName: Name in English
        :type EnName: str
        :param _ThaiSurName: Surname in Thai
        :type ThaiSurName: str
        :param _ThaiDOB: Date of birth in Thai
        :type ThaiDOB: str
        :param _EnDOB: Date of birth in English
        :type EnDOB: str
        :param _PhotoNumber: Photo number
        :type PhotoNumber: str
        :param _ThaiAddress: Address in Thai
        :type ThaiAddress: str
        :param _ThaiDateOfIssue: Date of issue in Thai
        :type ThaiDateOfIssue: str
        :param _DateOfIssue: Date of issue in English
        :type DateOfIssue: str
        :param _ThaiDateOfExpiry: Expiration date in Thai
        :type ThaiDateOfExpiry: str
        :param _DateOfExpiry: Expiration date in English
        :type DateOfExpiry: str
        :param _IssuingAgency: Issuing agency
        :type IssuingAgency: str
        :param _RefNumber: Ref number
        :type RefNumber: str
        :param _AdvancedInfo: This field is deprecated and will always return "1". Usage is not recommended.
        :type AdvancedInfo: str
        :param _PortraitImage: Identity photo
        :type PortraitImage: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Country = None
        self._IDNumber = None
        self._ThaiName = None
        self._EnName = None
        self._ThaiSurName = None
        self._ThaiDOB = None
        self._EnDOB = None
        self._PhotoNumber = None
        self._ThaiAddress = None
        self._ThaiDateOfIssue = None
        self._DateOfIssue = None
        self._ThaiDateOfExpiry = None
        self._DateOfExpiry = None
        self._IssuingAgency = None
        self._RefNumber = None
        self._AdvancedInfo = None
        self._PortraitImage = None
        self._WarnCardInfos = None
        self._RequestId = None

    @property
    def Country(self):
        r"""Country
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def IDNumber(self):
        r"""ID number
        :rtype: str
        """
        return self._IDNumber

    @IDNumber.setter
    def IDNumber(self, IDNumber):
        self._IDNumber = IDNumber

    @property
    def ThaiName(self):
        r"""Name in Thai
        :rtype: str
        """
        return self._ThaiName

    @ThaiName.setter
    def ThaiName(self, ThaiName):
        self._ThaiName = ThaiName

    @property
    def EnName(self):
        r"""Name in English
        :rtype: str
        """
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def ThaiSurName(self):
        r"""Surname in Thai
        :rtype: str
        """
        return self._ThaiSurName

    @ThaiSurName.setter
    def ThaiSurName(self, ThaiSurName):
        self._ThaiSurName = ThaiSurName

    @property
    def ThaiDOB(self):
        r"""Date of birth in Thai
        :rtype: str
        """
        return self._ThaiDOB

    @ThaiDOB.setter
    def ThaiDOB(self, ThaiDOB):
        self._ThaiDOB = ThaiDOB

    @property
    def EnDOB(self):
        r"""Date of birth in English
        :rtype: str
        """
        return self._EnDOB

    @EnDOB.setter
    def EnDOB(self, EnDOB):
        self._EnDOB = EnDOB

    @property
    def PhotoNumber(self):
        r"""Photo number
        :rtype: str
        """
        return self._PhotoNumber

    @PhotoNumber.setter
    def PhotoNumber(self, PhotoNumber):
        self._PhotoNumber = PhotoNumber

    @property
    def ThaiAddress(self):
        r"""Address in Thai
        :rtype: str
        """
        return self._ThaiAddress

    @ThaiAddress.setter
    def ThaiAddress(self, ThaiAddress):
        self._ThaiAddress = ThaiAddress

    @property
    def ThaiDateOfIssue(self):
        r"""Date of issue in Thai
        :rtype: str
        """
        return self._ThaiDateOfIssue

    @ThaiDateOfIssue.setter
    def ThaiDateOfIssue(self, ThaiDateOfIssue):
        self._ThaiDateOfIssue = ThaiDateOfIssue

    @property
    def DateOfIssue(self):
        r"""Date of issue in English
        :rtype: str
        """
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue

    @property
    def ThaiDateOfExpiry(self):
        r"""Expiration date in Thai
        :rtype: str
        """
        return self._ThaiDateOfExpiry

    @ThaiDateOfExpiry.setter
    def ThaiDateOfExpiry(self, ThaiDateOfExpiry):
        self._ThaiDateOfExpiry = ThaiDateOfExpiry

    @property
    def DateOfExpiry(self):
        r"""Expiration date in English
        :rtype: str
        """
        return self._DateOfExpiry

    @DateOfExpiry.setter
    def DateOfExpiry(self, DateOfExpiry):
        self._DateOfExpiry = DateOfExpiry

    @property
    def IssuingAgency(self):
        r"""Issuing agency
        :rtype: str
        """
        return self._IssuingAgency

    @IssuingAgency.setter
    def IssuingAgency(self, IssuingAgency):
        self._IssuingAgency = IssuingAgency

    @property
    def RefNumber(self):
        r"""Ref number
        :rtype: str
        """
        return self._RefNumber

    @RefNumber.setter
    def RefNumber(self, RefNumber):
        self._RefNumber = RefNumber

    @property
    def AdvancedInfo(self):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return "1". Usage is not recommended.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        warnings.warn("parameter `AdvancedInfo` is deprecated", DeprecationWarning) 

        self._AdvancedInfo = AdvancedInfo

    @property
    def PortraitImage(self):
        r"""Identity photo
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def WarnCardInfos(self):
        r"""Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :rtype: list of int
        """
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._IDNumber = params.get("IDNumber")
        self._ThaiName = params.get("ThaiName")
        self._EnName = params.get("EnName")
        self._ThaiSurName = params.get("ThaiSurName")
        self._ThaiDOB = params.get("ThaiDOB")
        self._EnDOB = params.get("EnDOB")
        self._PhotoNumber = params.get("PhotoNumber")
        self._ThaiAddress = params.get("ThaiAddress")
        self._ThaiDateOfIssue = params.get("ThaiDateOfIssue")
        self._DateOfIssue = params.get("DateOfIssue")
        self._ThaiDateOfExpiry = params.get("ThaiDateOfExpiry")
        self._DateOfExpiry = params.get("DateOfExpiry")
        self._IssuingAgency = params.get("IssuingAgency")
        self._RefNumber = params.get("RefNumber")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._PortraitImage = params.get("PortraitImage")
        self._WarnCardInfos = params.get("WarnCardInfos")
        self._RequestId = params.get("RequestId")


class SmartStructuralOCRV2Request(AbstractModel):
    r"""SmartStructuralOCRV2 request structure.

    """

    def __init__(self):
        r"""
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _IsPdf: Whether to enable PDF recognition. Default value: `false`. If you enable this feature, both images and PDF files can be recognized.
        :type IsPdf: bool
        :param _PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `IsPdf` is `true`. Default value: `1`.
        :type PdfPageNumber: int
        :param _ItemNames: The names of the fields you want to return for the structured information recognition.
For example, if you want to return only the recognition result of the "Name" and "Gender" fields, set this parameter as follows:
ItemNames=["Name","Gender"]
        :type ItemNames: list of str
        :param _ReturnFullText: Whether to enable recognition of all fields.
        :type ReturnFullText: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._ItemNames = None
        self._ReturnFullText = None

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def IsPdf(self):
        r"""Whether to enable PDF recognition. Default value: `false`. If you enable this feature, both images and PDF files can be recognized.
        :rtype: bool
        """
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        r"""The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `IsPdf` is `true`. Default value: `1`.
        :rtype: int
        """
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ItemNames(self):
        r"""The names of the fields you want to return for the structured information recognition.
For example, if you want to return only the recognition result of the "Name" and "Gender" fields, set this parameter as follows:
ItemNames=["Name","Gender"]
        :rtype: list of str
        """
        return self._ItemNames

    @ItemNames.setter
    def ItemNames(self, ItemNames):
        self._ItemNames = ItemNames

    @property
    def ReturnFullText(self):
        r"""Whether to enable recognition of all fields.
        :rtype: bool
        """
        return self._ReturnFullText

    @ReturnFullText.setter
    def ReturnFullText(self, ReturnFullText):
        self._ReturnFullText = ReturnFullText


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._ItemNames = params.get("ItemNames")
        self._ReturnFullText = params.get("ReturnFullText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRV2Response(AbstractModel):
    r"""SmartStructuralOCRV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Angle: The rotation angle (degrees) of the text on the image. 0: The text is horizontal. Positive value: The text is rotated clockwise. Negative value: The text is rotated counterclockwise.
        :type Angle: float
        :param _StructuralList: The structural information (key-value).
        :type StructuralList: list of GroupInfo
        :param _WordList: The recognized text information.
        :type WordList: list of WordItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Angle = None
        self._StructuralList = None
        self._WordList = None
        self._RequestId = None

    @property
    def Angle(self):
        r"""The rotation angle (degrees) of the text on the image. 0: The text is horizontal. Positive value: The text is rotated clockwise. Negative value: The text is rotated counterclockwise.
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def StructuralList(self):
        r"""The structural information (key-value).
        :rtype: list of GroupInfo
        """
        return self._StructuralList

    @StructuralList.setter
    def StructuralList(self, StructuralList):
        self._StructuralList = StructuralList

    @property
    def WordList(self):
        r"""The recognized text information.
        :rtype: list of WordItem
        """
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        if params.get("StructuralList") is not None:
            self._StructuralList = []
            for item in params.get("StructuralList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._StructuralList.append(obj)
        if params.get("WordList") is not None:
            self._WordList = []
            for item in params.get("WordList"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordList.append(obj)
        self._RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    r"""OCR result.

    """

    def __init__(self):
        r"""
        :param _DetectedText: Recognized text line content.
        :type DetectedText: str
        :param _Confidence: Confidence. Value range: 0–100.
        :type Confidence: int
        :param _Polygon: Text line coordinates, which are represented as 4 vertex coordinates.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Polygon: list of Coord
        :param _AdvancedInfo: Extended field.
The paragraph information `Parag` returned by the `GeneralBasicOcr` API contains `ParagNo`.
        :type AdvancedInfo: str
        :param _ItemPolygon: Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.
        :type ItemPolygon: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param _Words: Information about a character, including the character itself and its confidence. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :type Words: list of DetectedWords
        :param _WordCoordPoint: Coordinates of a word’s four corners on the input image. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :type WordCoordPoint: list of DetectedWordCoordPoint
        """
        self._DetectedText = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._ItemPolygon = None
        self._Words = None
        self._WordCoordPoint = None

    @property
    def DetectedText(self):
        r"""Recognized text line content.
        :rtype: str
        """
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        r"""Confidence. Value range: 0–100.
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        r"""Text line coordinates, which are represented as 4 vertex coordinates.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Coord
        """
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        r"""Extended field.
The paragraph information `Parag` returned by the `GeneralBasicOcr` API contains `ParagNo`.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def ItemPolygon(self):
        r"""Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        return self._ItemPolygon

    @ItemPolygon.setter
    def ItemPolygon(self, ItemPolygon):
        self._ItemPolygon = ItemPolygon

    @property
    def Words(self):
        r"""Information about a character, including the character itself and its confidence. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :rtype: list of DetectedWords
        """
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def WordCoordPoint(self):
        r"""Coordinates of a word’s four corners on the input image. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :rtype: list of DetectedWordCoordPoint
        """
        return self._WordCoordPoint

    @WordCoordPoint.setter
    def WordCoordPoint(self, WordCoordPoint):
        self._WordCoordPoint = WordCoordPoint


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemPolygon") is not None:
            self._ItemPolygon = ItemCoord()
            self._ItemPolygon._deserialize(params.get("ItemPolygon"))
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = DetectedWords()
                obj._deserialize(item)
                self._Words.append(obj)
        if params.get("WordCoordPoint") is not None:
            self._WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = DetectedWordCoordPoint()
                obj._deserialize(item)
                self._WordCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectionResult(AbstractModel):
    r"""Recognition result

    """

    def __init__(self):
        r"""
        :param _Value: The recognized text line content.
        :type Value: str
        :param _Polygon: This field is deprecated and will always return an empty array. Usage is not recommended.
        :type Polygon: list of Coord
        """
        self._Value = None
        self._Polygon = None

    @property
    def Value(self):
        r"""The recognized text line content.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Polygon(self):
        warnings.warn("parameter `Polygon` is deprecated", DeprecationWarning) 

        r"""This field is deprecated and will always return an empty array. Usage is not recommended.
        :rtype: list of Coord
        """
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        warnings.warn("parameter `Polygon` is deprecated", DeprecationWarning) 

        self._Polygon = Polygon


    def _deserialize(self, params):
        self._Value = params.get("Value")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    r"""Value information

    """

    def __init__(self):
        r"""
        :param _AutoContent: The value of the recognized field.
        :type AutoContent: str
        :param _Coord: The coordinates of the four vertices.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._AutoContent = None
        self._Coord = None

    @property
    def AutoContent(self):
        r"""The value of the recognized field.
        :rtype: str
        """
        return self._AutoContent

    @AutoContent.setter
    def AutoContent(self, AutoContent):
        self._AutoContent = AutoContent

    @property
    def Coord(self):
        r"""The coordinates of the four vertices.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord


    def _deserialize(self, params):
        self._AutoContent = params.get("AutoContent")
        if params.get("Coord") is not None:
            self._Coord = Polygon()
            self._Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRRequest(AbstractModel):
    r"""VinOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        r"""The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRResponse(AbstractModel):
    r"""VinOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Vin: The detected VIN.
        :type Vin: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Vin = None
        self._RequestId = None

    @property
    def Vin(self):
        r"""The detected VIN.
        :rtype: str
        """
        return self._Vin

    @Vin.setter
    def Vin(self, Vin):
        self._Vin = Vin

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vin = params.get("Vin")
        self._RequestId = params.get("RequestId")


class WordItem(AbstractModel):
    r"""The recognized text information.

    """

    def __init__(self):
        r"""
        :param _DetectedText: The text content.
        :type DetectedText: str
        :param _Coord: The coordinates of the four vertices.
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _AdvancedInfo: Description.
        :type AdvancedInfo: str
        :param _WordCoord: Specifies the four-point coordinate of the word.
        :type WordCoord: list of WordPolygon
        """
        self._DetectedText = None
        self._Coord = None
        self._AdvancedInfo = None
        self._WordCoord = None

    @property
    def DetectedText(self):
        r"""The text content.
        :rtype: str
        """
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Coord(self):
        r"""The coordinates of the four vertices.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord

    @property
    def AdvancedInfo(self):
        r"""Description.
        :rtype: str
        """
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def WordCoord(self):
        r"""Specifies the four-point coordinate of the word.
        :rtype: list of WordPolygon
        """
        return self._WordCoord

    @WordCoord.setter
    def WordCoord(self, WordCoord):
        self._WordCoord = WordCoord


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        if params.get("Coord") is not None:
            self._Coord = Polygon()
            self._Coord._deserialize(params.get("Coord"))
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("WordCoord") is not None:
            self._WordCoord = []
            for item in params.get("WordCoord"):
                obj = WordPolygon()
                obj._deserialize(item)
                self._WordCoord.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordPolygon(AbstractModel):
    r"""Word coordinates info.

    """

    def __init__(self):
        r"""
        :param _DetectedText: The text content.
        :type DetectedText: str
        :param _Coord: The coordinates of the four vertices.
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._DetectedText = None
        self._Coord = None

    @property
    def DetectedText(self):
        r"""The text content.
        :rtype: str
        """
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Coord(self):
        r"""The coordinates of the four vertices.
        :rtype: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        if params.get("Coord") is not None:
            self._Coord = Polygon()
            self._Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        