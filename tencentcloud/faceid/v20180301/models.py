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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Address(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Country: Nationality.
        :type Country: str
        :param _PostalCode: Post code.
        :type PostalCode: str
        :param _Subdivision: Subregion.
        :type Subdivision: str
        :param _City: City.
        :type City: str
        :param _FormattedAddress: Complete address.
        :type FormattedAddress: str
        :param _LineOne: The first line of address.
        :type LineOne: str
        :param _LineTwo: The second line of address.
        :type LineTwo: str
        :param _LineThree: The third line of address.
        :type LineThree: str
        :param _LineFour: The fourth line of address.
        :type LineFour: str
        :param _LineFive: The fifth line of address.
        :type LineFive: str
        """
        self._Country = None
        self._PostalCode = None
        self._Subdivision = None
        self._City = None
        self._FormattedAddress = None
        self._LineOne = None
        self._LineTwo = None
        self._LineThree = None
        self._LineFour = None
        self._LineFive = None

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def Subdivision(self):
        return self._Subdivision

    @Subdivision.setter
    def Subdivision(self, Subdivision):
        self._Subdivision = Subdivision

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress

    @property
    def LineOne(self):
        return self._LineOne

    @LineOne.setter
    def LineOne(self, LineOne):
        self._LineOne = LineOne

    @property
    def LineTwo(self):
        return self._LineTwo

    @LineTwo.setter
    def LineTwo(self, LineTwo):
        self._LineTwo = LineTwo

    @property
    def LineThree(self):
        return self._LineThree

    @LineThree.setter
    def LineThree(self, LineThree):
        self._LineThree = LineThree

    @property
    def LineFour(self):
        return self._LineFour

    @LineFour.setter
    def LineFour(self, LineFour):
        self._LineFour = LineFour

    @property
    def LineFive(self):
        return self._LineFive

    @LineFive.setter
    def LineFive(self, LineFive):
        self._LineFive = LineFive


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._PostalCode = params.get("PostalCode")
        self._Subdivision = params.get("Subdivision")
        self._City = params.get("City")
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
        


class ApplySdkVerificationTokenRequest(AbstractModel):
    """ApplySdkVerificationToken request structure.

    """

    def __init__(self):
        r"""
        :param _CheckMode: The verification mode. Valid values:
1: OCR + liveness detection + face comparison
2: Liveness detection + face comparison
3: Liveness detection
Default value: 1
        :type CheckMode: int
        :param _SecurityLevel: The security level of the verification. Valid values:
1: Video-based liveness detection
2: Motion-based liveness detection
3: Reflection-based liveness detection
4: Motion- and reflection-based liveness detection
Default value: 4
        :type SecurityLevel: int
        :param _IdCardType: The identity document type. Valid values: 
1. `HK` (default): Identity card of Hong Kong (China)
2. `ML`: Malaysian identity card
3. `IndonesiaIDCard`: Indonesian identity card
4. `PhilippinesVoteID`: Philippine voters ID card
5. `PhilippinesDrivingLicense`: Philippine driver's license
6. `PhilippinesTinID`: Philippine TIN ID card
7. `PhilippinesSSSID`: Philippine SSS ID card
8. `PhilippinesUMID`: Philippine UMID card
9. `MLIDPassport`: Passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions
10..MacaoIDCard: Macao ID Card
11.ThailandIDCard: Thailand ID Card
12.MainlandIDCard: Mainland ID Card
        :type IdCardType: str
        :param _CompareImage: The Base64-encoded value of the photo to compare, which is required only when `CheckMode` is set to `2`.
        :type CompareImage: str
        :param _NeedVerifyIdCard: Whether ID card authentication is required. If not, only document OCR will be performed. Currently, authentication is available only when the value of `IdCardType` is `HK`.
        :type NeedVerifyIdCard: bool
        :param _DisableChangeOcrResult: Whether to forbid the modification of the OCR result by users. Default value: `false` (modification allowed). (Currently, this parameter is not applied.)
        :type DisableChangeOcrResult: bool
        :param _DisableCheckOcrWarnings: Whether to disable the OCR warnings. Default value: `false` (not disable), where OCR warnings are enabled and the OCR result will not be returned if there is a warning.
This feature applies only to Hong Kong (China) identity cards, Malaysian identity cards, and passports.
        :type DisableCheckOcrWarnings: bool
        :param _Extra: A passthrough field, which is returned together with the verification result and can contain up to 1,024 bits.
        :type Extra: str
        """
        self._CheckMode = None
        self._SecurityLevel = None
        self._IdCardType = None
        self._CompareImage = None
        self._NeedVerifyIdCard = None
        self._DisableChangeOcrResult = None
        self._DisableCheckOcrWarnings = None
        self._Extra = None

    @property
    def CheckMode(self):
        return self._CheckMode

    @CheckMode.setter
    def CheckMode(self, CheckMode):
        self._CheckMode = CheckMode

    @property
    def SecurityLevel(self):
        return self._SecurityLevel

    @SecurityLevel.setter
    def SecurityLevel(self, SecurityLevel):
        self._SecurityLevel = SecurityLevel

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def CompareImage(self):
        return self._CompareImage

    @CompareImage.setter
    def CompareImage(self, CompareImage):
        self._CompareImage = CompareImage

    @property
    def NeedVerifyIdCard(self):
        warnings.warn("parameter `NeedVerifyIdCard` is deprecated", DeprecationWarning) 

        return self._NeedVerifyIdCard

    @NeedVerifyIdCard.setter
    def NeedVerifyIdCard(self, NeedVerifyIdCard):
        warnings.warn("parameter `NeedVerifyIdCard` is deprecated", DeprecationWarning) 

        self._NeedVerifyIdCard = NeedVerifyIdCard

    @property
    def DisableChangeOcrResult(self):
        return self._DisableChangeOcrResult

    @DisableChangeOcrResult.setter
    def DisableChangeOcrResult(self, DisableChangeOcrResult):
        self._DisableChangeOcrResult = DisableChangeOcrResult

    @property
    def DisableCheckOcrWarnings(self):
        return self._DisableCheckOcrWarnings

    @DisableCheckOcrWarnings.setter
    def DisableCheckOcrWarnings(self, DisableCheckOcrWarnings):
        self._DisableCheckOcrWarnings = DisableCheckOcrWarnings

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._CheckMode = params.get("CheckMode")
        self._SecurityLevel = params.get("SecurityLevel")
        self._IdCardType = params.get("IdCardType")
        self._CompareImage = params.get("CompareImage")
        self._NeedVerifyIdCard = params.get("NeedVerifyIdCard")
        self._DisableChangeOcrResult = params.get("DisableChangeOcrResult")
        self._DisableCheckOcrWarnings = params.get("DisableCheckOcrWarnings")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySdkVerificationTokenResponse(AbstractModel):
    """ApplySdkVerificationToken response structure.

    """

    def __init__(self):
        r"""
        :param _SdkToken: The token used to identify an SDK-based verification process. It is valid for 7,200s and can be used to get the verification result after the process is completed.
        :type SdkToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SdkToken = None
        self._RequestId = None

    @property
    def SdkToken(self):
        return self._SdkToken

    @SdkToken.setter
    def SdkToken(self, SdkToken):
        self._SdkToken = SdkToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkToken = params.get("SdkToken")
        self._RequestId = params.get("RequestId")


class CardInfo(AbstractModel):
    """License OCR result

    """

    def __init__(self):
        r"""
        :param _HKIDCard: Hong Kong ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type HKIDCard: :class:`tencentcloud.faceid.v20180301.models.HKIDCard`
        :param _MLIDCard: Malaysia ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type MLIDCard: :class:`tencentcloud.faceid.v20180301.models.MLIDCard`
        :param _PhilippinesVoteID: Philippines VoteID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesVoteID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesVoteID`
        :param _IndonesiaIDCard: Indonesia ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndonesiaIDCard: :class:`tencentcloud.faceid.v20180301.models.IndonesiaIDCard`
        :param _PhilippinesDrivingLicense: Philippines Driving License
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesDrivingLicense: :class:`tencentcloud.faceid.v20180301.models.PhilippinesDrivingLicense`
        :param _PhilippinesTinID: Philippines TinID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesTinID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesTinID`
        :param _PhilippinesSSSID: Philippines SSSID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesSSSID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesSSSID`
        :param _PhilippinesUMID: Philippines UMID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesUMID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesUMID`
        :param _InternationalIDPassport: ID Cards of Hong Kong, Macao and Taiwan (China), and International Passport
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternationalIDPassport: :class:`tencentcloud.faceid.v20180301.models.InternationalIDPassport`
        :param _GeneralCard: General license information
Note: This field may return null, indicating that no valid values can be obtained.
        :type GeneralCard: :class:`tencentcloud.faceid.v20180301.models.GeneralCard`
        :param _IndonesiaDrivingLicense: Indonesia Driving License
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndonesiaDrivingLicense: :class:`tencentcloud.faceid.v20180301.models.IndonesiaDrivingLicense`
        :param _ThailandIDCard: Thailand ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThailandIDCard: :class:`tencentcloud.faceid.v20180301.models.ThailandIDCard`
        :param _SingaporeIDCard: Singapore ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type SingaporeIDCard: :class:`tencentcloud.faceid.v20180301.models.SingaporeIDCard`
        :param _MacaoIDCard: Macao ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type MacaoIDCard: :class:`tencentcloud.faceid.v20180301.models.MacaoIDCard`
        """
        self._HKIDCard = None
        self._MLIDCard = None
        self._PhilippinesVoteID = None
        self._IndonesiaIDCard = None
        self._PhilippinesDrivingLicense = None
        self._PhilippinesTinID = None
        self._PhilippinesSSSID = None
        self._PhilippinesUMID = None
        self._InternationalIDPassport = None
        self._GeneralCard = None
        self._IndonesiaDrivingLicense = None
        self._ThailandIDCard = None
        self._SingaporeIDCard = None
        self._MacaoIDCard = None

    @property
    def HKIDCard(self):
        return self._HKIDCard

    @HKIDCard.setter
    def HKIDCard(self, HKIDCard):
        self._HKIDCard = HKIDCard

    @property
    def MLIDCard(self):
        return self._MLIDCard

    @MLIDCard.setter
    def MLIDCard(self, MLIDCard):
        self._MLIDCard = MLIDCard

    @property
    def PhilippinesVoteID(self):
        return self._PhilippinesVoteID

    @PhilippinesVoteID.setter
    def PhilippinesVoteID(self, PhilippinesVoteID):
        self._PhilippinesVoteID = PhilippinesVoteID

    @property
    def IndonesiaIDCard(self):
        return self._IndonesiaIDCard

    @IndonesiaIDCard.setter
    def IndonesiaIDCard(self, IndonesiaIDCard):
        self._IndonesiaIDCard = IndonesiaIDCard

    @property
    def PhilippinesDrivingLicense(self):
        return self._PhilippinesDrivingLicense

    @PhilippinesDrivingLicense.setter
    def PhilippinesDrivingLicense(self, PhilippinesDrivingLicense):
        self._PhilippinesDrivingLicense = PhilippinesDrivingLicense

    @property
    def PhilippinesTinID(self):
        return self._PhilippinesTinID

    @PhilippinesTinID.setter
    def PhilippinesTinID(self, PhilippinesTinID):
        self._PhilippinesTinID = PhilippinesTinID

    @property
    def PhilippinesSSSID(self):
        return self._PhilippinesSSSID

    @PhilippinesSSSID.setter
    def PhilippinesSSSID(self, PhilippinesSSSID):
        self._PhilippinesSSSID = PhilippinesSSSID

    @property
    def PhilippinesUMID(self):
        return self._PhilippinesUMID

    @PhilippinesUMID.setter
    def PhilippinesUMID(self, PhilippinesUMID):
        self._PhilippinesUMID = PhilippinesUMID

    @property
    def InternationalIDPassport(self):
        return self._InternationalIDPassport

    @InternationalIDPassport.setter
    def InternationalIDPassport(self, InternationalIDPassport):
        self._InternationalIDPassport = InternationalIDPassport

    @property
    def GeneralCard(self):
        return self._GeneralCard

    @GeneralCard.setter
    def GeneralCard(self, GeneralCard):
        self._GeneralCard = GeneralCard

    @property
    def IndonesiaDrivingLicense(self):
        return self._IndonesiaDrivingLicense

    @IndonesiaDrivingLicense.setter
    def IndonesiaDrivingLicense(self, IndonesiaDrivingLicense):
        self._IndonesiaDrivingLicense = IndonesiaDrivingLicense

    @property
    def ThailandIDCard(self):
        return self._ThailandIDCard

    @ThailandIDCard.setter
    def ThailandIDCard(self, ThailandIDCard):
        self._ThailandIDCard = ThailandIDCard

    @property
    def SingaporeIDCard(self):
        return self._SingaporeIDCard

    @SingaporeIDCard.setter
    def SingaporeIDCard(self, SingaporeIDCard):
        self._SingaporeIDCard = SingaporeIDCard

    @property
    def MacaoIDCard(self):
        return self._MacaoIDCard

    @MacaoIDCard.setter
    def MacaoIDCard(self, MacaoIDCard):
        self._MacaoIDCard = MacaoIDCard


    def _deserialize(self, params):
        if params.get("HKIDCard") is not None:
            self._HKIDCard = HKIDCard()
            self._HKIDCard._deserialize(params.get("HKIDCard"))
        if params.get("MLIDCard") is not None:
            self._MLIDCard = MLIDCard()
            self._MLIDCard._deserialize(params.get("MLIDCard"))
        if params.get("PhilippinesVoteID") is not None:
            self._PhilippinesVoteID = PhilippinesVoteID()
            self._PhilippinesVoteID._deserialize(params.get("PhilippinesVoteID"))
        if params.get("IndonesiaIDCard") is not None:
            self._IndonesiaIDCard = IndonesiaIDCard()
            self._IndonesiaIDCard._deserialize(params.get("IndonesiaIDCard"))
        if params.get("PhilippinesDrivingLicense") is not None:
            self._PhilippinesDrivingLicense = PhilippinesDrivingLicense()
            self._PhilippinesDrivingLicense._deserialize(params.get("PhilippinesDrivingLicense"))
        if params.get("PhilippinesTinID") is not None:
            self._PhilippinesTinID = PhilippinesTinID()
            self._PhilippinesTinID._deserialize(params.get("PhilippinesTinID"))
        if params.get("PhilippinesSSSID") is not None:
            self._PhilippinesSSSID = PhilippinesSSSID()
            self._PhilippinesSSSID._deserialize(params.get("PhilippinesSSSID"))
        if params.get("PhilippinesUMID") is not None:
            self._PhilippinesUMID = PhilippinesUMID()
            self._PhilippinesUMID._deserialize(params.get("PhilippinesUMID"))
        if params.get("InternationalIDPassport") is not None:
            self._InternationalIDPassport = InternationalIDPassport()
            self._InternationalIDPassport._deserialize(params.get("InternationalIDPassport"))
        if params.get("GeneralCard") is not None:
            self._GeneralCard = GeneralCard()
            self._GeneralCard._deserialize(params.get("GeneralCard"))
        if params.get("IndonesiaDrivingLicense") is not None:
            self._IndonesiaDrivingLicense = IndonesiaDrivingLicense()
            self._IndonesiaDrivingLicense._deserialize(params.get("IndonesiaDrivingLicense"))
        if params.get("ThailandIDCard") is not None:
            self._ThailandIDCard = ThailandIDCard()
            self._ThailandIDCard._deserialize(params.get("ThailandIDCard"))
        if params.get("SingaporeIDCard") is not None:
            self._SingaporeIDCard = SingaporeIDCard()
            self._SingaporeIDCard._deserialize(params.get("SingaporeIDCard"))
        if params.get("MacaoIDCard") is not None:
            self._MacaoIDCard = MacaoIDCard()
            self._MacaoIDCard._deserialize(params.get("MacaoIDCard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CardVerifyResult(AbstractModel):
    """The OCR result of a user's identity document during the eKYC verification process.

    """

    def __init__(self):
        r"""
        :param _IsPass: Whether the authentication or OCR process is successful.
        :type IsPass: bool
        :param _IsEdit: Whether the user modified the card recognition result
        :type IsEdit: bool
        :param _CardVideo: The download URL of the video used for identity document verification, which is valid for 10 minutes. This parameter is returned only if video-based identity document verification is enabled.
Note: This field may return null, indicating that no valid value can be obtained.
        :type CardVideo: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _CardImage: The download URL of the identity document image, which is valid for 10 minutes.
Note: This field may return null, indicating that no valid value can be obtained.
        :type CardImage: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _CardInfoOcrJson: The OCR result (in JSON) of the identity document image. If verification or OCR fails, this parameter is left empty. The URL is valid for 10 minutes.
(1) Hong Kong (China) identity card
When the value of `IdCardType` is `HK`:
- CnName (string): Name in Chinese.
- EnName (string): Name in English.
- TelexCode (string): The code corresponding to the name in Chinese.
- Sex (string): Gender. Valid values: `M` (male) and `F` (female).
- Birthday (string): Date of birth.
- Permanent (int): Whether it is a permanent residence identity card. Valid values: `0` (non-permanent), `1` (permanent), and `-1` (unknown).
- IdNum (string): Identity card number.
- Symbol (string): The ID symbol below the date of birth, such as "***AZ".
- FirstIssueDate (string): Month and year of first registration.
- CurrentIssueDate (string): The date of latest issuance.

(2) Malaysian identity card
When the value of `IdCardType` is `ML`:
- Sex (string): Gender. Valid values: `LELAKI` (male) and `PEREMPUAN` (female).
- Birthday (string): Date of birth.
- ID (string): Identity card number.
- Name (string): Name.
- Address (string): Address.
- Type (string): Identity document type.

(3) Philippine identity document
When the value of `IdCardType` is `PhilippinesVoteID`:
- Birthday (string): Date of birth.
- Address (string): Address.
- LastName (string): Last name.
- FirstName (string): First name.
- VIN (string): Voter's identification number (VIN).
- CivilStatus (string): Civil status.
- Citizenship (string): Citizenship.
- PrecinctNo (string): Precinct.

When the value of `IdCardType` is `PhilippinesDrivingLicense`:
- Sex (string): Gender.
- Birthday (string): Date of birth.
- Name (string): Name.
- Address (string): Address.
- LastName (string): Last name.
- FirstName (string): First name.
- MiddleName (string): Middle name.
- Nationality (string): Nationality.
- LicenseNo (string): License number.
- ExpiresDate (string): Expiration date.
- AgencyCode (string): Agency code.

When the value of `IdCardType` is `PhilippinesTinID`:
- LicenseNumber (string): Tax identification number (TIN).
- FullName (string): Full name.
- Address (string): Address.
- Birthday (string): Date of birth.
- IssueDate (string): Issue date.

When the value of `IdCardType` is `PhilippinesSSSID`:
- LicenseNumber (string): Common reference number (CRN).
- FullName (string): Full name.
- Birthday (string): Date of birth.

When the value of `IdCardType` is `PhilippinesUMID`:
- Surname (string): Surname.
- MiddleName (string):Middle name.
- GivenName (string): Given name.
- Sex (string): Gender.
- Birthday (string): Date of birth.
- Address (string): Address.
- CRN (string): Common reference number (CRN).

(4) Indonesian identity card
When the value of `IdCardType` is `IndonesiaIDCard`:
- NIK (string): Single Identity Number.
- Nama (string): Full name.
- TempatTglLahir (string): Place and date of birth.
- JenisKelamin (string): Gender.
- GolDarah (string): Blood type.
- Alamat (string): Address.
- RTRW (string): Street.
- KelDesa (string): Village.
- Kecamatan (string): Region.
- Agama (string): Religion.
- StatusPerkawinan (string): Marital status.
- Perkerjaan (string): Occupation.
- KewargaNegaraan (string): Nationality.
- BerlakuHingga (string): Expiry date.
- IssuedDate (string): Issue date.

(5) A passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions
When the value of `IdCardType` is `MLIDPassport`:
- FullName (string): Full name.
- Surname (string): Surname.
- GivenName (string): Given name.
- Birthday (string): Date of birth.
- Sex (string): Gender. Valid values: `F` (female) and `M` (male).
- DateOfExpiration (string): Expiration date.
- IssuingCountry (string): Issuing country.
- NationalityCode (string): Country/region code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardInfoOcrJson: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _RequestId: The request ID of a single process.
        :type RequestId: str
        :param _CardInfo: The recognition results of ID card
        :type CardInfo: :class:`tencentcloud.faceid.v20180301.models.CardInfo`
        :param _NormalCardInfo: License OCR result
        :type NormalCardInfo: :class:`tencentcloud.faceid.v20180301.models.NormalCardInfo`
        :param _WarnCardInfos: Card warning information
-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        """
        self._IsPass = None
        self._IsEdit = None
        self._CardVideo = None
        self._CardImage = None
        self._CardInfoOcrJson = None
        self._RequestId = None
        self._CardInfo = None
        self._NormalCardInfo = None
        self._WarnCardInfos = None

    @property
    def IsPass(self):
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

    @property
    def IsEdit(self):
        return self._IsEdit

    @IsEdit.setter
    def IsEdit(self, IsEdit):
        self._IsEdit = IsEdit

    @property
    def CardVideo(self):
        return self._CardVideo

    @CardVideo.setter
    def CardVideo(self, CardVideo):
        self._CardVideo = CardVideo

    @property
    def CardImage(self):
        return self._CardImage

    @CardImage.setter
    def CardImage(self, CardImage):
        self._CardImage = CardImage

    @property
    def CardInfoOcrJson(self):
        return self._CardInfoOcrJson

    @CardInfoOcrJson.setter
    def CardInfoOcrJson(self, CardInfoOcrJson):
        self._CardInfoOcrJson = CardInfoOcrJson

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def CardInfo(self):
        warnings.warn("parameter `CardInfo` is deprecated", DeprecationWarning) 

        return self._CardInfo

    @CardInfo.setter
    def CardInfo(self, CardInfo):
        warnings.warn("parameter `CardInfo` is deprecated", DeprecationWarning) 

        self._CardInfo = CardInfo

    @property
    def NormalCardInfo(self):
        return self._NormalCardInfo

    @NormalCardInfo.setter
    def NormalCardInfo(self, NormalCardInfo):
        self._NormalCardInfo = NormalCardInfo

    @property
    def WarnCardInfos(self):
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos


    def _deserialize(self, params):
        self._IsPass = params.get("IsPass")
        self._IsEdit = params.get("IsEdit")
        if params.get("CardVideo") is not None:
            self._CardVideo = FileInfo()
            self._CardVideo._deserialize(params.get("CardVideo"))
        if params.get("CardImage") is not None:
            self._CardImage = FileInfo()
            self._CardImage._deserialize(params.get("CardImage"))
        if params.get("CardInfoOcrJson") is not None:
            self._CardInfoOcrJson = FileInfo()
            self._CardInfoOcrJson._deserialize(params.get("CardInfoOcrJson"))
        self._RequestId = params.get("RequestId")
        if params.get("CardInfo") is not None:
            self._CardInfo = CardInfo()
            self._CardInfo._deserialize(params.get("CardInfo"))
        if params.get("NormalCardInfo") is not None:
            self._NormalCardInfo = NormalCardInfo()
            self._NormalCardInfo._deserialize(params.get("NormalCardInfo"))
        self._WarnCardInfos = params.get("WarnCardInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareResult(AbstractModel):
    """The description of a single comparison result.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: The final verification result code.
0: Success.
1001: Failed to call the liveness detection engine.
1004: Face detection failed.
2004: The uploaded face image is too large or too small.
2012: The face is not fully exposed.
2013: No face is detected.
2014: The resolution of the uploaded image is too low . Please upload a new one.
2015: Face comparison failed.
2016: The similarity did not reach the passing standard.
        :type ErrorCode: str
        :param _ErrorMsg: The description of the final verification result.
        :type ErrorMsg: str
        :param _LiveData: The liveness algorithm package generated during this SDK-based liveness detection.
        :type LiveData: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _LiveVideo: The download URL of the video used for verification, which is valid for 10 minutes.
        :type LiveVideo: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _LiveErrorCode: The liveness detection result code.
0: Success.
1001: Failed to call the liveness detection engine.
1004: Face detection failed.
        :type LiveErrorCode: str
        :param _LiveErrorMsg: The description of the liveness detection result.
        :type LiveErrorMsg: str
        :param _BestFrame: The download URL of the face screenshot during verification, which is valid for 10 minutes.
Note: This field may return null, indicating that no valid value can be obtained.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _ProfileImage: The download URL of the profile photo screenshot from the identity document, which is valid for 10 minutes.
        :type ProfileImage: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _CompareErrorCode: The face comparison result code.
0: Success.
2004: The uploaded face image is too large or too small.
2012: The face is not fully exposed.
2013: No face is detected.
2014: The resolution of the uploaded image is too low . Please upload a new one.
2015: Face comparison failed.
2016: The similarity did not reach the passing standard.
Note: This field may return null, indicating that no valid value can be obtained.
        :type CompareErrorCode: str
        :param _CompareErrorMsg: The description of the face comparison result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorMsg: str
        :param _Sim: The similarity score of face comparison.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sim: float
        :param _IsNeedCharge: This parameter is disused.
        :type IsNeedCharge: bool
        :param _CardInfoInputJson: The identity document photo info edited by the user. Currently, this parameter is not applied.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardInfoInputJson: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _RequestId: The request ID of this verification process.
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._LiveData = None
        self._LiveVideo = None
        self._LiveErrorCode = None
        self._LiveErrorMsg = None
        self._BestFrame = None
        self._ProfileImage = None
        self._CompareErrorCode = None
        self._CompareErrorMsg = None
        self._Sim = None
        self._IsNeedCharge = None
        self._CardInfoInputJson = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def LiveData(self):
        return self._LiveData

    @LiveData.setter
    def LiveData(self, LiveData):
        self._LiveData = LiveData

    @property
    def LiveVideo(self):
        return self._LiveVideo

    @LiveVideo.setter
    def LiveVideo(self, LiveVideo):
        self._LiveVideo = LiveVideo

    @property
    def LiveErrorCode(self):
        return self._LiveErrorCode

    @LiveErrorCode.setter
    def LiveErrorCode(self, LiveErrorCode):
        self._LiveErrorCode = LiveErrorCode

    @property
    def LiveErrorMsg(self):
        return self._LiveErrorMsg

    @LiveErrorMsg.setter
    def LiveErrorMsg(self, LiveErrorMsg):
        self._LiveErrorMsg = LiveErrorMsg

    @property
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def ProfileImage(self):
        return self._ProfileImage

    @ProfileImage.setter
    def ProfileImage(self, ProfileImage):
        self._ProfileImage = ProfileImage

    @property
    def CompareErrorCode(self):
        return self._CompareErrorCode

    @CompareErrorCode.setter
    def CompareErrorCode(self, CompareErrorCode):
        self._CompareErrorCode = CompareErrorCode

    @property
    def CompareErrorMsg(self):
        return self._CompareErrorMsg

    @CompareErrorMsg.setter
    def CompareErrorMsg(self, CompareErrorMsg):
        self._CompareErrorMsg = CompareErrorMsg

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def IsNeedCharge(self):
        return self._IsNeedCharge

    @IsNeedCharge.setter
    def IsNeedCharge(self, IsNeedCharge):
        self._IsNeedCharge = IsNeedCharge

    @property
    def CardInfoInputJson(self):
        return self._CardInfoInputJson

    @CardInfoInputJson.setter
    def CardInfoInputJson(self, CardInfoInputJson):
        self._CardInfoInputJson = CardInfoInputJson

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("LiveData") is not None:
            self._LiveData = FileInfo()
            self._LiveData._deserialize(params.get("LiveData"))
        if params.get("LiveVideo") is not None:
            self._LiveVideo = FileInfo()
            self._LiveVideo._deserialize(params.get("LiveVideo"))
        self._LiveErrorCode = params.get("LiveErrorCode")
        self._LiveErrorMsg = params.get("LiveErrorMsg")
        if params.get("BestFrame") is not None:
            self._BestFrame = FileInfo()
            self._BestFrame._deserialize(params.get("BestFrame"))
        if params.get("ProfileImage") is not None:
            self._ProfileImage = FileInfo()
            self._ProfileImage._deserialize(params.get("ProfileImage"))
        self._CompareErrorCode = params.get("CompareErrorCode")
        self._CompareErrorMsg = params.get("CompareErrorMsg")
        self._Sim = params.get("Sim")
        self._IsNeedCharge = params.get("IsNeedCharge")
        if params.get("CardInfoInputJson") is not None:
            self._CardInfoInputJson = FileInfo()
            self._CardInfoInputJson._deserialize(params.get("CardInfoInputJson"))
        self._RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """The description of a file, including a download URL and the MD5 checksum and size of the file.

    """

    def __init__(self):
        r"""
        :param _Url: The URL for downloading the file
        :type Url: str
        :param _MD5: The 32-bit MD5 checksum of the file
        :type MD5: str
        :param _Size: The file size
        :type Size: int
        """
        self._Url = None
        self._MD5 = None
        self._Size = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def MD5(self):
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._MD5 = params.get("MD5")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralCard(AbstractModel):
    """General liscense information.

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _PersonalNumber: Personal number, which is returned when it is a passport
Note: This field may return null, indicating that no valid values can be obtained.
        :type PersonalNumber: str
        :param _PassportCodeFirst: The first line of passport machine reading code
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeFirst: str
        :param _PassportCodeSecond: The first line of passport machine reading code
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeSecond: str
        :param _ExpirationDate: Date of expiry in the format of YYYY-MM-DD
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _DueDate: Valid date in the format of YYYY-MM-DD
Note: This field may return null, indicating that no valid values can be obtained.
        :type DueDate: str
        :param _IssuedDate: Date of issue in the format of YYYY-MM-DD
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _IssuedAuthority: Issuing authority
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedAuthority: str
        :param _IssuedCountry: Issuing country, which is returned following the ISO 3166 country coding specification
Note: This field may return null, indicating that no valid values can be obtained.
Example: MYS
        :type IssuedCountry: str
        :param _FullName: Full Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _Sex: Gender on the license
- M: male
- F: female
- X: other gender
Note: This field may return null, indicating that no valid values can be obtained.
Example: M
        :type Sex: str
        :param _Age: Age. 0 indicates that no valid information is obtained.
Example: 0
        :type Age: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _BirthPlace: Birth place
Note: This field may return null, indicating that no valid values can be obtained.
        :type BirthPlace: str
        :param _Nationality: Nationality, which is returned following the ISO 3166 country coding specification
Note: This field may return null, indicating that no valid values can be obtained.
Example: IND
        :type Nationality: str
        :param _RegistrationNumber: Registration number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistrationNumber: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: :class:`tencentcloud.faceid.v20180301.models.Address`
        """
        self._LicenseNumber = None
        self._PersonalNumber = None
        self._PassportCodeFirst = None
        self._PassportCodeSecond = None
        self._ExpirationDate = None
        self._DueDate = None
        self._IssuedDate = None
        self._IssuedAuthority = None
        self._IssuedCountry = None
        self._FullName = None
        self._FirstName = None
        self._LastName = None
        self._Sex = None
        self._Age = None
        self._Birthday = None
        self._BirthPlace = None
        self._Nationality = None
        self._RegistrationNumber = None
        self._Address = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def PersonalNumber(self):
        return self._PersonalNumber

    @PersonalNumber.setter
    def PersonalNumber(self, PersonalNumber):
        self._PersonalNumber = PersonalNumber

    @property
    def PassportCodeFirst(self):
        return self._PassportCodeFirst

    @PassportCodeFirst.setter
    def PassportCodeFirst(self, PassportCodeFirst):
        self._PassportCodeFirst = PassportCodeFirst

    @property
    def PassportCodeSecond(self):
        return self._PassportCodeSecond

    @PassportCodeSecond.setter
    def PassportCodeSecond(self, PassportCodeSecond):
        self._PassportCodeSecond = PassportCodeSecond

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def DueDate(self):
        return self._DueDate

    @DueDate.setter
    def DueDate(self, DueDate):
        self._DueDate = DueDate

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def IssuedAuthority(self):
        return self._IssuedAuthority

    @IssuedAuthority.setter
    def IssuedAuthority(self, IssuedAuthority):
        self._IssuedAuthority = IssuedAuthority

    @property
    def IssuedCountry(self):
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._PersonalNumber = params.get("PersonalNumber")
        self._PassportCodeFirst = params.get("PassportCodeFirst")
        self._PassportCodeSecond = params.get("PassportCodeSecond")
        self._ExpirationDate = params.get("ExpirationDate")
        self._DueDate = params.get("DueDate")
        self._IssuedDate = params.get("IssuedDate")
        self._IssuedAuthority = params.get("IssuedAuthority")
        self._IssuedCountry = params.get("IssuedCountry")
        self._FullName = params.get("FullName")
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Sex = params.get("Sex")
        self._Age = params.get("Age")
        self._Birthday = params.get("Birthday")
        self._BirthPlace = params.get("BirthPlace")
        self._Nationality = params.get("Nationality")
        self._RegistrationNumber = params.get("RegistrationNumber")
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSdkVerificationResultRequest(AbstractModel):
    """GetSdkVerificationResult request structure.

    """

    def __init__(self):
        r"""
        :param _SdkToken: The token used to identify an SDK-based verification process.
        :type SdkToken: str
        """
        self._SdkToken = None

    @property
    def SdkToken(self):
        return self._SdkToken

    @SdkToken.setter
    def SdkToken(self, SdkToken):
        self._SdkToken = SdkToken


    def _deserialize(self, params):
        self._SdkToken = params.get("SdkToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSdkVerificationResultResponse(AbstractModel):
    """GetSdkVerificationResult response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The result code of the verification result.
        :type Result: str
        :param _Description: The verification result description.
        :type Description: str
        :param _ChargeCount: The charge count.
        :type ChargeCount: int
        :param _CardVerifyResults: The results of multiple OCR processes (in order). The result of the final process is used as the valid result.
        :type CardVerifyResults: list of CardVerifyResult
        :param _CompareResults: The results of multiple liveness detection processes (in order). The result of the final process is used as the valid result.
        :type CompareResults: list of CompareResult
        :param _Extra: Data passed through in the process of getting the token.
        :type Extra: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._ChargeCount = None
        self._CardVerifyResults = None
        self._CompareResults = None
        self._Extra = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChargeCount(self):
        return self._ChargeCount

    @ChargeCount.setter
    def ChargeCount(self, ChargeCount):
        self._ChargeCount = ChargeCount

    @property
    def CardVerifyResults(self):
        return self._CardVerifyResults

    @CardVerifyResults.setter
    def CardVerifyResults(self, CardVerifyResults):
        self._CardVerifyResults = CardVerifyResults

    @property
    def CompareResults(self):
        return self._CompareResults

    @CompareResults.setter
    def CompareResults(self, CompareResults):
        self._CompareResults = CompareResults

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._ChargeCount = params.get("ChargeCount")
        if params.get("CardVerifyResults") is not None:
            self._CardVerifyResults = []
            for item in params.get("CardVerifyResults"):
                obj = CardVerifyResult()
                obj._deserialize(item)
                self._CardVerifyResults.append(obj)
        if params.get("CompareResults") is not None:
            self._CompareResults = []
            for item in params.get("CompareResults"):
                obj = CompareResult()
                obj._deserialize(item)
                self._CompareResults.append(obj)
        self._Extra = params.get("Extra")
        self._RequestId = params.get("RequestId")


class HKIDCard(AbstractModel):
    """Hong Kong ID card.

    """

    def __init__(self):
        r"""
        :param _CnName: 
        :type CnName: str
        :param _EnName: English name
Note: This field may return null, indicating that no valid values can be obtained.
Example: SAN, Nan
        :type EnName: str
        :param _TelexCode: Telex code correspondint to the Chinese name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TelexCode: str
        :param _Sex: Gender: "Male-M" or "Female-F"
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
Example: 01-01-2001
        :type Birthday: str
        :param _Permanent: Permanent resident ID card: 0-non-permanent; 1-permanent; -1-unknown
Note: This field may return null, indicating that no valid values can be obtained.
        :type Permanent: str
        :param _IdNum: ID card number
Note: This field may return null, indicating that no valid values can be obtained.
Example: C000000(E)
        :type IdNum: str
        :param _Symbol: Lisence symbol, which is the symbol below Birthday. Example: "***AZ"
Note: This field may return null, indicating that no valid values can be obtained.
        :type Symbol: str
        :param _FirstIssueDate: The first date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstIssueDate: str
        :param _CurrentIssueDate: The current date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentIssueDate: str
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

    @property
    def CnName(self):
        return self._CnName

    @CnName.setter
    def CnName(self, CnName):
        self._CnName = CnName

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def TelexCode(self):
        return self._TelexCode

    @TelexCode.setter
    def TelexCode(self, TelexCode):
        self._TelexCode = TelexCode

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Permanent(self):
        return self._Permanent

    @Permanent.setter
    def Permanent(self, Permanent):
        self._Permanent = Permanent

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Symbol(self):
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def FirstIssueDate(self):
        return self._FirstIssueDate

    @FirstIssueDate.setter
    def FirstIssueDate(self, FirstIssueDate):
        self._FirstIssueDate = FirstIssueDate

    @property
    def CurrentIssueDate(self):
        return self._CurrentIssueDate

    @CurrentIssueDate.setter
    def CurrentIssueDate(self, CurrentIssueDate):
        self._CurrentIssueDate = CurrentIssueDate


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndonesiaDrivingLicense(AbstractModel):
    """Indonesia driving license.

    """

    def __init__(self):
        r"""
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _ExpirationDate: Expiration date
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _IssuedDate: Date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _IssuedCountry: Issuing country
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountry: str
        """
        self._LastName = None
        self._FirstName = None
        self._LicenseNumber = None
        self._Birthday = None
        self._Address = None
        self._ExpirationDate = None
        self._IssuedDate = None
        self._IssuedCountry = None

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def IssuedCountry(self):
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry


    def _deserialize(self, params):
        self._LastName = params.get("LastName")
        self._FirstName = params.get("FirstName")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Birthday = params.get("Birthday")
        self._Address = params.get("Address")
        self._ExpirationDate = params.get("ExpirationDate")
        self._IssuedDate = params.get("IssuedDate")
        self._IssuedCountry = params.get("IssuedCountry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndonesiaIDCard(AbstractModel):
    """Indonesia ID card.

    """

    def __init__(self):
        r"""
        :param _NIK: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type NIK: str
        :param _Nama: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nama: str
        :param _TempatTglLahir: Birth place/Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type TempatTglLahir: str
        :param _JenisKelamin: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type JenisKelamin: str
        :param _GolDarah: Blood type
Note: This field may return null, indicating that no valid values can be obtained.
        :type GolDarah: str
        :param _Alamat: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alamat: str
        :param _RTRW: Street
Note: This field may return null, indicating that no valid values can be obtained.
        :type RTRW: str
        :param _KelDesa: Village
Note: This field may return null, indicating that no valid values can be obtained.
        :type KelDesa: str
        :param _Kecamatan: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kecamatan: str
        :param _Agama: Religious beliefs
Note: This field may return null, indicating that no valid values can be obtained.
        :type Agama: str
        :param _StatusPerkawinan: Marital status
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusPerkawinan: str
        :param _Perkerjaan: Job
Note: This field may return null, indicating that no valid values can be obtained.
        :type Perkerjaan: str
        :param _KewargaNegaraan: Nationality
Note: This field may return null, indicating that no valid values can be obtained.
        :type KewargaNegaraan: str
        :param _BerlakuHingga: ID card validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :type BerlakuHingga: str
        :param _IssuedDate: Date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _Provinsi: Province
Note: This field may return null, indicating that no valid values can be obtained.
        :type Provinsi: str
        :param _Kota: City
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kota: str
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
        self._Provinsi = None
        self._Kota = None

    @property
    def NIK(self):
        return self._NIK

    @NIK.setter
    def NIK(self, NIK):
        self._NIK = NIK

    @property
    def Nama(self):
        return self._Nama

    @Nama.setter
    def Nama(self, Nama):
        self._Nama = Nama

    @property
    def TempatTglLahir(self):
        return self._TempatTglLahir

    @TempatTglLahir.setter
    def TempatTglLahir(self, TempatTglLahir):
        self._TempatTglLahir = TempatTglLahir

    @property
    def JenisKelamin(self):
        return self._JenisKelamin

    @JenisKelamin.setter
    def JenisKelamin(self, JenisKelamin):
        self._JenisKelamin = JenisKelamin

    @property
    def GolDarah(self):
        return self._GolDarah

    @GolDarah.setter
    def GolDarah(self, GolDarah):
        self._GolDarah = GolDarah

    @property
    def Alamat(self):
        return self._Alamat

    @Alamat.setter
    def Alamat(self, Alamat):
        self._Alamat = Alamat

    @property
    def RTRW(self):
        return self._RTRW

    @RTRW.setter
    def RTRW(self, RTRW):
        self._RTRW = RTRW

    @property
    def KelDesa(self):
        return self._KelDesa

    @KelDesa.setter
    def KelDesa(self, KelDesa):
        self._KelDesa = KelDesa

    @property
    def Kecamatan(self):
        return self._Kecamatan

    @Kecamatan.setter
    def Kecamatan(self, Kecamatan):
        self._Kecamatan = Kecamatan

    @property
    def Agama(self):
        return self._Agama

    @Agama.setter
    def Agama(self, Agama):
        self._Agama = Agama

    @property
    def StatusPerkawinan(self):
        return self._StatusPerkawinan

    @StatusPerkawinan.setter
    def StatusPerkawinan(self, StatusPerkawinan):
        self._StatusPerkawinan = StatusPerkawinan

    @property
    def Perkerjaan(self):
        return self._Perkerjaan

    @Perkerjaan.setter
    def Perkerjaan(self, Perkerjaan):
        self._Perkerjaan = Perkerjaan

    @property
    def KewargaNegaraan(self):
        return self._KewargaNegaraan

    @KewargaNegaraan.setter
    def KewargaNegaraan(self, KewargaNegaraan):
        self._KewargaNegaraan = KewargaNegaraan

    @property
    def BerlakuHingga(self):
        return self._BerlakuHingga

    @BerlakuHingga.setter
    def BerlakuHingga(self, BerlakuHingga):
        self._BerlakuHingga = BerlakuHingga

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def Provinsi(self):
        return self._Provinsi

    @Provinsi.setter
    def Provinsi(self, Provinsi):
        self._Provinsi = Provinsi

    @property
    def Kota(self):
        return self._Kota

    @Kota.setter
    def Kota(self, Kota):
        self._Kota = Kota


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
        self._Provinsi = params.get("Provinsi")
        self._Kota = params.get("Kota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternationalIDPassport(AbstractModel):
    """ID cards of Hong Kong, Macao and Taiwan (China), and international passport.

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: Passport ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _FullName: Full name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _Surname: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Surname: str
        :param _GivenName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type GivenName: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Sex: Gender (F-Female, M-Male)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _DateOfExpiration: Expiration date
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfExpiration: str
        :param _IssuingCountry: Issuing country
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuingCountry: str
        :param _NationalityCode: Nationality code
Note: This field may return null, indicating that no valid values can be obtained.
        :type NationalityCode: str
        :param _PassportCodeFirst: The first line at the bottom, the MRZ Code sequence
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeFirst: str
        :param _PassportCodeSecond: The second line at the bottom, the MRZ Code sequence
Note: This field may return null, indicating that no valid values can be obtained.
        :type PassportCodeSecond: str
        """
        self._LicenseNumber = None
        self._FullName = None
        self._Surname = None
        self._GivenName = None
        self._Birthday = None
        self._Sex = None
        self._DateOfExpiration = None
        self._IssuingCountry = None
        self._NationalityCode = None
        self._PassportCodeFirst = None
        self._PassportCodeSecond = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Surname(self):
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def GivenName(self):
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def DateOfExpiration(self):
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def IssuingCountry(self):
        return self._IssuingCountry

    @IssuingCountry.setter
    def IssuingCountry(self, IssuingCountry):
        self._IssuingCountry = IssuingCountry

    @property
    def NationalityCode(self):
        return self._NationalityCode

    @NationalityCode.setter
    def NationalityCode(self, NationalityCode):
        self._NationalityCode = NationalityCode

    @property
    def PassportCodeFirst(self):
        return self._PassportCodeFirst

    @PassportCodeFirst.setter
    def PassportCodeFirst(self, PassportCodeFirst):
        self._PassportCodeFirst = PassportCodeFirst

    @property
    def PassportCodeSecond(self):
        return self._PassportCodeSecond

    @PassportCodeSecond.setter
    def PassportCodeSecond(self, PassportCodeSecond):
        self._PassportCodeSecond = PassportCodeSecond


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._FullName = params.get("FullName")
        self._Surname = params.get("Surname")
        self._GivenName = params.get("GivenName")
        self._Birthday = params.get("Birthday")
        self._Sex = params.get("Sex")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._IssuingCountry = params.get("IssuingCountry")
        self._NationalityCode = params.get("NationalityCode")
        self._PassportCodeFirst = params.get("PassportCodeFirst")
        self._PassportCodeSecond = params.get("PassportCodeSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCard(AbstractModel):
    """Malaysia ID card.

    """

    def __init__(self):
        r"""
        :param _Name: Full Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ID: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Type: Lisence type
MyKad ID card
MyPR Permanent resident ID card
MyTentera Military ID card
MyKAS Temporary ID card
POLIS Police ID card
IKAD Labor ID card
MyKid Juvenile ID card
Example: MyKad
        :type Type: str
        :param _Birthday: Birthday (Currently, this filed only supports IKAD labor ID card and MyKad ID card)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        """
        self._Name = None
        self._ID = None
        self._Sex = None
        self._Address = None
        self._Type = None
        self._Birthday = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._Sex = params.get("Sex")
        self._Address = params.get("Address")
        self._Type = params.get("Type")
        self._Birthday = params.get("Birthday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MacaoIDCard(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _FirstName: 
        :type FirstName: str
        :param _LastName: 
        :type LastName: str
        :param _Birthday: 
        :type Birthday: str
        :param _ExpirationDate: 
        :type ExpirationDate: str
        :param _LicenseNumber: 
        :type LicenseNumber: str
        :param _Sex: 
        :type Sex: str
        :param _Age: 
        :type Age: str
        :param _IssuedCountry: 
        :type IssuedCountry: str
        :param _Field1: 
        :type Field1: str
        :param _Field2: 
        :type Field2: str
        """
        self._FirstName = None
        self._LastName = None
        self._Birthday = None
        self._ExpirationDate = None
        self._LicenseNumber = None
        self._Sex = None
        self._Age = None
        self._IssuedCountry = None
        self._Field1 = None
        self._Field2 = None

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def IssuedCountry(self):
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry

    @property
    def Field1(self):
        return self._Field1

    @Field1.setter
    def Field1(self, Field1):
        self._Field1 = Field1

    @property
    def Field2(self):
        return self._Field2

    @Field2.setter
    def Field2(self, Field2):
        self._Field2 = Field2


    def _deserialize(self, params):
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Birthday = params.get("Birthday")
        self._ExpirationDate = params.get("ExpirationDate")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Sex = params.get("Sex")
        self._Age = params.get("Age")
        self._IssuedCountry = params.get("IssuedCountry")
        self._Field1 = params.get("Field1")
        self._Field2 = params.get("Field2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalCardInfo(AbstractModel):
    """License OCR result

    """

    def __init__(self):
        r"""
        :param _HKIDCard: Hong Kong ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type HKIDCard: :class:`tencentcloud.faceid.v20180301.models.NormalHKIDCard`
        :param _MLIDCard: Malaysia ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type MLIDCard: :class:`tencentcloud.faceid.v20180301.models.NormalMLIDCard`
        :param _PhilippinesVoteID: Philippines VoteID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesVoteID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesVoteID`
        :param _IndonesiaIDCard: Indonesia ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndonesiaIDCard: :class:`tencentcloud.faceid.v20180301.models.NormalIndonesiaIDCard`
        :param _PhilippinesDrivingLicense: Philippines Driving License
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesDrivingLicense: :class:`tencentcloud.faceid.v20180301.models.PhilippinesDrivingLicense`
        :param _PhilippinesTinID: Philippines TinID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesTinID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesTinID`
        :param _PhilippinesSSSID: Philippines SSSID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesSSSID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesSSSID`
        :param _PhilippinesUMID: Philippines UMID
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhilippinesUMID: :class:`tencentcloud.faceid.v20180301.models.PhilippinesUMID`
        :param _InternationalIDPassport: ID Cards of Hong Kong, Macao and Taiwan (China), and International Passport
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternationalIDPassport: :class:`tencentcloud.faceid.v20180301.models.InternationalIDPassport`
        :param _GeneralCard: General license information
Note: This field may return null, indicating that no valid values can be obtained.
        :type GeneralCard: :class:`tencentcloud.faceid.v20180301.models.GeneralCard`
        :param _IndonesiaDrivingLicense: Indonesia Driving License
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndonesiaDrivingLicense: :class:`tencentcloud.faceid.v20180301.models.IndonesiaDrivingLicense`
        :param _ThailandIDCard: Thailand ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThailandIDCard: :class:`tencentcloud.faceid.v20180301.models.NormalThailandIDCard`
        :param _SingaporeIDCard: Singapore ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type SingaporeIDCard: :class:`tencentcloud.faceid.v20180301.models.SingaporeIDCard`
        :param _MacaoIDCard: Macao ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type MacaoIDCard: :class:`tencentcloud.faceid.v20180301.models.MacaoIDCard`
        """
        self._HKIDCard = None
        self._MLIDCard = None
        self._PhilippinesVoteID = None
        self._IndonesiaIDCard = None
        self._PhilippinesDrivingLicense = None
        self._PhilippinesTinID = None
        self._PhilippinesSSSID = None
        self._PhilippinesUMID = None
        self._InternationalIDPassport = None
        self._GeneralCard = None
        self._IndonesiaDrivingLicense = None
        self._ThailandIDCard = None
        self._SingaporeIDCard = None
        self._MacaoIDCard = None

    @property
    def HKIDCard(self):
        return self._HKIDCard

    @HKIDCard.setter
    def HKIDCard(self, HKIDCard):
        self._HKIDCard = HKIDCard

    @property
    def MLIDCard(self):
        return self._MLIDCard

    @MLIDCard.setter
    def MLIDCard(self, MLIDCard):
        self._MLIDCard = MLIDCard

    @property
    def PhilippinesVoteID(self):
        return self._PhilippinesVoteID

    @PhilippinesVoteID.setter
    def PhilippinesVoteID(self, PhilippinesVoteID):
        self._PhilippinesVoteID = PhilippinesVoteID

    @property
    def IndonesiaIDCard(self):
        return self._IndonesiaIDCard

    @IndonesiaIDCard.setter
    def IndonesiaIDCard(self, IndonesiaIDCard):
        self._IndonesiaIDCard = IndonesiaIDCard

    @property
    def PhilippinesDrivingLicense(self):
        return self._PhilippinesDrivingLicense

    @PhilippinesDrivingLicense.setter
    def PhilippinesDrivingLicense(self, PhilippinesDrivingLicense):
        self._PhilippinesDrivingLicense = PhilippinesDrivingLicense

    @property
    def PhilippinesTinID(self):
        return self._PhilippinesTinID

    @PhilippinesTinID.setter
    def PhilippinesTinID(self, PhilippinesTinID):
        self._PhilippinesTinID = PhilippinesTinID

    @property
    def PhilippinesSSSID(self):
        return self._PhilippinesSSSID

    @PhilippinesSSSID.setter
    def PhilippinesSSSID(self, PhilippinesSSSID):
        self._PhilippinesSSSID = PhilippinesSSSID

    @property
    def PhilippinesUMID(self):
        return self._PhilippinesUMID

    @PhilippinesUMID.setter
    def PhilippinesUMID(self, PhilippinesUMID):
        self._PhilippinesUMID = PhilippinesUMID

    @property
    def InternationalIDPassport(self):
        return self._InternationalIDPassport

    @InternationalIDPassport.setter
    def InternationalIDPassport(self, InternationalIDPassport):
        self._InternationalIDPassport = InternationalIDPassport

    @property
    def GeneralCard(self):
        return self._GeneralCard

    @GeneralCard.setter
    def GeneralCard(self, GeneralCard):
        self._GeneralCard = GeneralCard

    @property
    def IndonesiaDrivingLicense(self):
        return self._IndonesiaDrivingLicense

    @IndonesiaDrivingLicense.setter
    def IndonesiaDrivingLicense(self, IndonesiaDrivingLicense):
        self._IndonesiaDrivingLicense = IndonesiaDrivingLicense

    @property
    def ThailandIDCard(self):
        return self._ThailandIDCard

    @ThailandIDCard.setter
    def ThailandIDCard(self, ThailandIDCard):
        self._ThailandIDCard = ThailandIDCard

    @property
    def SingaporeIDCard(self):
        return self._SingaporeIDCard

    @SingaporeIDCard.setter
    def SingaporeIDCard(self, SingaporeIDCard):
        self._SingaporeIDCard = SingaporeIDCard

    @property
    def MacaoIDCard(self):
        return self._MacaoIDCard

    @MacaoIDCard.setter
    def MacaoIDCard(self, MacaoIDCard):
        self._MacaoIDCard = MacaoIDCard


    def _deserialize(self, params):
        if params.get("HKIDCard") is not None:
            self._HKIDCard = NormalHKIDCard()
            self._HKIDCard._deserialize(params.get("HKIDCard"))
        if params.get("MLIDCard") is not None:
            self._MLIDCard = NormalMLIDCard()
            self._MLIDCard._deserialize(params.get("MLIDCard"))
        if params.get("PhilippinesVoteID") is not None:
            self._PhilippinesVoteID = PhilippinesVoteID()
            self._PhilippinesVoteID._deserialize(params.get("PhilippinesVoteID"))
        if params.get("IndonesiaIDCard") is not None:
            self._IndonesiaIDCard = NormalIndonesiaIDCard()
            self._IndonesiaIDCard._deserialize(params.get("IndonesiaIDCard"))
        if params.get("PhilippinesDrivingLicense") is not None:
            self._PhilippinesDrivingLicense = PhilippinesDrivingLicense()
            self._PhilippinesDrivingLicense._deserialize(params.get("PhilippinesDrivingLicense"))
        if params.get("PhilippinesTinID") is not None:
            self._PhilippinesTinID = PhilippinesTinID()
            self._PhilippinesTinID._deserialize(params.get("PhilippinesTinID"))
        if params.get("PhilippinesSSSID") is not None:
            self._PhilippinesSSSID = PhilippinesSSSID()
            self._PhilippinesSSSID._deserialize(params.get("PhilippinesSSSID"))
        if params.get("PhilippinesUMID") is not None:
            self._PhilippinesUMID = PhilippinesUMID()
            self._PhilippinesUMID._deserialize(params.get("PhilippinesUMID"))
        if params.get("InternationalIDPassport") is not None:
            self._InternationalIDPassport = InternationalIDPassport()
            self._InternationalIDPassport._deserialize(params.get("InternationalIDPassport"))
        if params.get("GeneralCard") is not None:
            self._GeneralCard = GeneralCard()
            self._GeneralCard._deserialize(params.get("GeneralCard"))
        if params.get("IndonesiaDrivingLicense") is not None:
            self._IndonesiaDrivingLicense = IndonesiaDrivingLicense()
            self._IndonesiaDrivingLicense._deserialize(params.get("IndonesiaDrivingLicense"))
        if params.get("ThailandIDCard") is not None:
            self._ThailandIDCard = NormalThailandIDCard()
            self._ThailandIDCard._deserialize(params.get("ThailandIDCard"))
        if params.get("SingaporeIDCard") is not None:
            self._SingaporeIDCard = SingaporeIDCard()
            self._SingaporeIDCard._deserialize(params.get("SingaporeIDCard"))
        if params.get("MacaoIDCard") is not None:
            self._MacaoIDCard = MacaoIDCard()
            self._MacaoIDCard._deserialize(params.get("MacaoIDCard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalHKIDCard(AbstractModel):
    """Hong Kong ID card.

    """

    def __init__(self):
        r"""
        :param _ChineseName: Chinese name
Note: This field may return null, indicating that no valid values can be obtained.

        :type ChineseName: str
        :param _FullName: English name
Note: This field may return null, indicating that no valid values can be obtained.
Example: SAN, Nan
        :type FullName: str
        :param _RegistrationNumber: Telex code correspondint to the Chinese name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistrationNumber: str
        :param _Sex: Gender: "Male-M" or "Female-F"
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
Example: 01-01-2001
        :type Birthday: str
        :param _Permanent: Permanent resident ID card: 0-non-permanent; 1-permanent; -1-unknown
Note: This field may return null, indicating that no valid values can be obtained.
        :type Permanent: str
        :param _LicenseNumber: ID card number
Note: This field may return null, indicating that no valid values can be obtained.
Example: C000000(E)
        :type LicenseNumber: str
        :param _Symbol: Lisence symbol, which is the symbol below Birthday. Example: "***AZ"
Note: This field may return null, indicating that no valid values can be obtained.
        :type Symbol: str
        :param _IssuedDate: The first date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _CurrentIssueDate: The current date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentIssueDate: str
        """
        self._ChineseName = None
        self._FullName = None
        self._RegistrationNumber = None
        self._Sex = None
        self._Birthday = None
        self._Permanent = None
        self._LicenseNumber = None
        self._Symbol = None
        self._IssuedDate = None
        self._CurrentIssueDate = None

    @property
    def ChineseName(self):
        return self._ChineseName

    @ChineseName.setter
    def ChineseName(self, ChineseName):
        self._ChineseName = ChineseName

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Permanent(self):
        return self._Permanent

    @Permanent.setter
    def Permanent(self, Permanent):
        self._Permanent = Permanent

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def Symbol(self):
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def CurrentIssueDate(self):
        return self._CurrentIssueDate

    @CurrentIssueDate.setter
    def CurrentIssueDate(self, CurrentIssueDate):
        self._CurrentIssueDate = CurrentIssueDate


    def _deserialize(self, params):
        self._ChineseName = params.get("ChineseName")
        self._FullName = params.get("FullName")
        self._RegistrationNumber = params.get("RegistrationNumber")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._Permanent = params.get("Permanent")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Symbol = params.get("Symbol")
        self._IssuedDate = params.get("IssuedDate")
        self._CurrentIssueDate = params.get("CurrentIssueDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalIndonesiaIDCard(AbstractModel):
    """Indonesia ID card.

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _FullName: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _Birthday: Birth place/Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _BloodType: Blood type
Note: This field may return null, indicating that no valid values can be obtained.
        :type BloodType: str
        :param _FormattedAddress: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        :param _Street: Street
Note: This field may return null, indicating that no valid values can be obtained.
        :type Street: str
        :param _Village: Village
Note: This field may return null, indicating that no valid values can be obtained.
        :type Village: str
        :param _Area: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param _Religion: Religious beliefs
Note: This field may return null, indicating that no valid values can be obtained.
        :type Religion: str
        :param _MaritalStatus: Marital status
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaritalStatus: str
        :param _Occupation: Job
Note: This field may return null, indicating that no valid values can be obtained.
        :type Occupation: str
        :param _Nationality: Nationality
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _DueDate: ID card validity period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DueDate: str
        :param _IssuedDate: Date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _Province: Province
Note: This field may return null, indicating that no valid values can be obtained.
        :type Province: str
        :param _City: City
Note: This field may return null, indicating that no valid values can be obtained.
        :type City: str
        """
        self._LicenseNumber = None
        self._FullName = None
        self._Birthday = None
        self._Sex = None
        self._BloodType = None
        self._FormattedAddress = None
        self._Street = None
        self._Village = None
        self._Area = None
        self._Religion = None
        self._MaritalStatus = None
        self._Occupation = None
        self._Nationality = None
        self._DueDate = None
        self._IssuedDate = None
        self._Province = None
        self._City = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def BloodType(self):
        return self._BloodType

    @BloodType.setter
    def BloodType(self, BloodType):
        self._BloodType = BloodType

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress

    @property
    def Street(self):
        return self._Street

    @Street.setter
    def Street(self, Street):
        self._Street = Street

    @property
    def Village(self):
        return self._Village

    @Village.setter
    def Village(self, Village):
        self._Village = Village

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Religion(self):
        return self._Religion

    @Religion.setter
    def Religion(self, Religion):
        self._Religion = Religion

    @property
    def MaritalStatus(self):
        return self._MaritalStatus

    @MaritalStatus.setter
    def MaritalStatus(self, MaritalStatus):
        self._MaritalStatus = MaritalStatus

    @property
    def Occupation(self):
        return self._Occupation

    @Occupation.setter
    def Occupation(self, Occupation):
        self._Occupation = Occupation

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def DueDate(self):
        return self._DueDate

    @DueDate.setter
    def DueDate(self, DueDate):
        self._DueDate = DueDate

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._FullName = params.get("FullName")
        self._Birthday = params.get("Birthday")
        self._Sex = params.get("Sex")
        self._BloodType = params.get("BloodType")
        self._FormattedAddress = params.get("FormattedAddress")
        self._Street = params.get("Street")
        self._Village = params.get("Village")
        self._Area = params.get("Area")
        self._Religion = params.get("Religion")
        self._MaritalStatus = params.get("MaritalStatus")
        self._Occupation = params.get("Occupation")
        self._Nationality = params.get("Nationality")
        self._DueDate = params.get("DueDate")
        self._IssuedDate = params.get("IssuedDate")
        self._Province = params.get("Province")
        self._City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalMLIDCard(AbstractModel):
    """Malaysia ID card.

    """

    def __init__(self):
        r"""
        :param _FullName: Full Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _FormattedAddress: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        :param _Type: Lisence type
MyKad ID card
MyPR Permanent resident ID card
MyTentera Military ID card
MyKAS Temporary ID card
POLIS Police ID card
IKAD Labor ID card
MyKid Juvenile ID card
Example: MyKad
        :type Type: str
        :param _Birthday: Birthday (Currently, this filed only supports IKAD labor ID card and MyKad ID card)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        """
        self._FullName = None
        self._LicenseNumber = None
        self._Sex = None
        self._FormattedAddress = None
        self._Type = None
        self._Birthday = None

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Sex = params.get("Sex")
        self._FormattedAddress = params.get("FormattedAddress")
        self._Type = params.get("Type")
        self._Birthday = params.get("Birthday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalThailandIDCard(AbstractModel):
    """Thailand ID Card

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: LicenseNumber
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _FullName: Thailand name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _FormattedAddress: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        :param _ExpirationDate: Expiration date
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _IssuedDate: Issued date
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedDate: str
        :param _RegistrationNumber: Registration number 
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistrationNumber: str
        :param _Religion: Religion
Note: This field may return null, indicating that no valid values can be obtained.
        :type Religion: str
        :param _ThaiBirthday: Birthday in Thai
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThaiBirthday: str
        :param _ThaiExpirationDate: Expiration date in Thai
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThaiExpirationDate: str
        :param _ThaiIssueDate: Issued date in Thai
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThaiIssueDate: str
        """
        self._LicenseNumber = None
        self._FullName = None
        self._LastName = None
        self._FirstName = None
        self._Birthday = None
        self._FormattedAddress = None
        self._ExpirationDate = None
        self._IssuedDate = None
        self._RegistrationNumber = None
        self._Religion = None
        self._ThaiBirthday = None
        self._ThaiExpirationDate = None
        self._ThaiIssueDate = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber

    @property
    def Religion(self):
        return self._Religion

    @Religion.setter
    def Religion(self, Religion):
        self._Religion = Religion

    @property
    def ThaiBirthday(self):
        return self._ThaiBirthday

    @ThaiBirthday.setter
    def ThaiBirthday(self, ThaiBirthday):
        self._ThaiBirthday = ThaiBirthday

    @property
    def ThaiExpirationDate(self):
        return self._ThaiExpirationDate

    @ThaiExpirationDate.setter
    def ThaiExpirationDate(self, ThaiExpirationDate):
        self._ThaiExpirationDate = ThaiExpirationDate

    @property
    def ThaiIssueDate(self):
        return self._ThaiIssueDate

    @ThaiIssueDate.setter
    def ThaiIssueDate(self, ThaiIssueDate):
        self._ThaiIssueDate = ThaiIssueDate


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._FullName = params.get("FullName")
        self._LastName = params.get("LastName")
        self._FirstName = params.get("FirstName")
        self._Birthday = params.get("Birthday")
        self._FormattedAddress = params.get("FormattedAddress")
        self._ExpirationDate = params.get("ExpirationDate")
        self._IssuedDate = params.get("IssuedDate")
        self._RegistrationNumber = params.get("RegistrationNumber")
        self._Religion = params.get("Religion")
        self._ThaiBirthday = params.get("ThaiBirthday")
        self._ThaiExpirationDate = params.get("ThaiExpirationDate")
        self._ThaiIssueDate = params.get("ThaiIssueDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhilippinesDrivingLicense(AbstractModel):
    """Philippines driving license

    """

    def __init__(self):
        r"""
        :param _Name: Full Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _LastName: Last name

Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _MiddleName: Middle name
Note: This field may return null, indicating that no valid values can be obtained.
        :type MiddleName: str
        :param _Nationality: Nationality
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _LicenseNo: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNo: str
        :param _ExpiresDate: Date of expiry
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiresDate: str
        :param _AgencyCode: Agency code
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgencyCode: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        """
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

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def MiddleName(self):
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LicenseNo(self):
        return self._LicenseNo

    @LicenseNo.setter
    def LicenseNo(self, LicenseNo):
        self._LicenseNo = LicenseNo

    @property
    def ExpiresDate(self):
        return self._ExpiresDate

    @ExpiresDate.setter
    def ExpiresDate(self, ExpiresDate):
        self._ExpiresDate = ExpiresDate

    @property
    def AgencyCode(self):
        return self._AgencyCode

    @AgencyCode.setter
    def AgencyCode(self, AgencyCode):
        self._AgencyCode = AgencyCode

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._LastName = params.get("LastName")
        self._FirstName = params.get("FirstName")
        self._MiddleName = params.get("MiddleName")
        self._Nationality = params.get("Nationality")
        self._Sex = params.get("Sex")
        self._Address = params.get("Address")
        self._LicenseNo = params.get("LicenseNo")
        self._ExpiresDate = params.get("ExpiresDate")
        self._AgencyCode = params.get("AgencyCode")
        self._Birthday = params.get("Birthday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhilippinesSSSID(AbstractModel):
    """Philippines SSSID Card

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _FullName: Full name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        """
        self._LicenseNumber = None
        self._FullName = None
        self._Birthday = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._FullName = params.get("FullName")
        self._Birthday = params.get("Birthday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhilippinesTinID(AbstractModel):
    """Philippines TinID Card

    """

    def __init__(self):
        r"""
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _FullName: Full name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _IssueDate: Date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssueDate: str
        """
        self._LicenseNumber = None
        self._FullName = None
        self._Address = None
        self._Birthday = None
        self._IssueDate = None

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate


    def _deserialize(self, params):
        self._LicenseNumber = params.get("LicenseNumber")
        self._FullName = params.get("FullName")
        self._Address = params.get("Address")
        self._Birthday = params.get("Birthday")
        self._IssueDate = params.get("IssueDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhilippinesUMID(AbstractModel):
    """Philippines UMID Card

    """

    def __init__(self):
        r"""
        :param _Surname: Surname
Note: This field may return null, indicating that no valid values can be obtained.
        :type Surname: str
        :param _MiddleName: Middle Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type MiddleName: str
        :param _GivenName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type GivenName: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _CRN: CRN code
Note: This field may return null, indicating that no valid values can be obtained.
        :type CRN: str
        """
        self._Surname = None
        self._MiddleName = None
        self._GivenName = None
        self._Sex = None
        self._Birthday = None
        self._Address = None
        self._CRN = None

    @property
    def Surname(self):
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def MiddleName(self):
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def GivenName(self):
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def CRN(self):
        return self._CRN

    @CRN.setter
    def CRN(self, CRN):
        self._CRN = CRN


    def _deserialize(self, params):
        self._Surname = params.get("Surname")
        self._MiddleName = params.get("MiddleName")
        self._GivenName = params.get("GivenName")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._Address = params.get("Address")
        self._CRN = params.get("CRN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhilippinesVoteID(AbstractModel):
    """Philippines VoteID Card

    """

    def __init__(self):
        r"""
        :param _VIN: VIN of Philippines VoteID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VIN: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _CivilStatus: Civil status
Note: This field may return null, indicating that no valid values can be obtained.
        :type CivilStatus: str
        :param _Citizenship: Nationality
Note: This field may return null, indicating that no valid values can be obtained.
        :type Citizenship: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _PrecinctNo: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrecinctNo: str
        """
        self._VIN = None
        self._FirstName = None
        self._LastName = None
        self._Birthday = None
        self._CivilStatus = None
        self._Citizenship = None
        self._Address = None
        self._PrecinctNo = None

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def CivilStatus(self):
        return self._CivilStatus

    @CivilStatus.setter
    def CivilStatus(self, CivilStatus):
        self._CivilStatus = CivilStatus

    @property
    def Citizenship(self):
        return self._Citizenship

    @Citizenship.setter
    def Citizenship(self, Citizenship):
        self._Citizenship = Citizenship

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def PrecinctNo(self):
        return self._PrecinctNo

    @PrecinctNo.setter
    def PrecinctNo(self, PrecinctNo):
        self._PrecinctNo = PrecinctNo


    def _deserialize(self, params):
        self._VIN = params.get("VIN")
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Birthday = params.get("Birthday")
        self._CivilStatus = params.get("CivilStatus")
        self._Citizenship = params.get("Citizenship")
        self._Address = params.get("Address")
        self._PrecinctNo = params.get("PrecinctNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingaporeIDCard(AbstractModel):
    """Singapore ID Card

    """

    def __init__(self):
        r"""
        :param _ChName: Chinese name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChName: str
        :param _EnName: English name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnName: str
        :param _ID: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _CountryOfBirth: Country of birth
Note: This field may return null, indicating that no valid values can be obtained.
        :type CountryOfBirth: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Address: Address (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Race: Nationality (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Race: str
        :param _NRICCode:  NRIC number (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type NRICCode: str
        :param _PostCode: Post number (on the front)
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostCode: str
        :param _DateOfExpiration: Date of expiry (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfExpiration: str
        :param _DateOfIssue: Date of issue (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfIssue: str
        """
        self._ChName = None
        self._EnName = None
        self._ID = None
        self._Sex = None
        self._CountryOfBirth = None
        self._Birthday = None
        self._Address = None
        self._Race = None
        self._NRICCode = None
        self._PostCode = None
        self._DateOfExpiration = None
        self._DateOfIssue = None

    @property
    def ChName(self):
        return self._ChName

    @ChName.setter
    def ChName(self, ChName):
        self._ChName = ChName

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def CountryOfBirth(self):
        return self._CountryOfBirth

    @CountryOfBirth.setter
    def CountryOfBirth(self, CountryOfBirth):
        self._CountryOfBirth = CountryOfBirth

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Race(self):
        return self._Race

    @Race.setter
    def Race(self, Race):
        self._Race = Race

    @property
    def NRICCode(self):
        return self._NRICCode

    @NRICCode.setter
    def NRICCode(self, NRICCode):
        self._NRICCode = NRICCode

    @property
    def PostCode(self):
        return self._PostCode

    @PostCode.setter
    def PostCode(self, PostCode):
        self._PostCode = PostCode

    @property
    def DateOfExpiration(self):
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def DateOfIssue(self):
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue


    def _deserialize(self, params):
        self._ChName = params.get("ChName")
        self._EnName = params.get("EnName")
        self._ID = params.get("ID")
        self._Sex = params.get("Sex")
        self._CountryOfBirth = params.get("CountryOfBirth")
        self._Birthday = params.get("Birthday")
        self._Address = params.get("Address")
        self._Race = params.get("Race")
        self._NRICCode = params.get("NRICCode")
        self._PostCode = params.get("PostCode")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._DateOfIssue = params.get("DateOfIssue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThailandIDCard(AbstractModel):
    """Thailand ID Card

    """

    def __init__(self):
        r"""
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _DateOfBirth: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfBirth: str
        :param _DateOfExpiry: Date of expiry
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfExpiry: str
        :param _DateOfIssue: Date of issue
Note: This field may return null, indicating that no valid values can be obtained.
        :type DateOfIssue: str
        :param _IssuedCountry: Issuing country
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountry: str
        """
        self._LastName = None
        self._FirstName = None
        self._LicenseNumber = None
        self._DateOfBirth = None
        self._DateOfExpiry = None
        self._DateOfIssue = None
        self._IssuedCountry = None

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def DateOfExpiry(self):
        return self._DateOfExpiry

    @DateOfExpiry.setter
    def DateOfExpiry(self, DateOfExpiry):
        self._DateOfExpiry = DateOfExpiry

    @property
    def DateOfIssue(self):
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue

    @property
    def IssuedCountry(self):
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry


    def _deserialize(self, params):
        self._LastName = params.get("LastName")
        self._FirstName = params.get("FirstName")
        self._LicenseNumber = params.get("LicenseNumber")
        self._DateOfBirth = params.get("DateOfBirth")
        self._DateOfExpiry = params.get("DateOfExpiry")
        self._DateOfIssue = params.get("DateOfIssue")
        self._IssuedCountry = params.get("IssuedCountry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        