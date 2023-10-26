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


class ApplyLivenessTokenRequest(AbstractModel):
    """ApplyLivenessToken request structure.

    """

    def __init__(self):
        r"""
        :param _SecureLevel: Enumerated value. Valid values: `1`, `2`, `3`, and `4`.
Their meanings are as follows:
1 - silent
2 - blinking
3 - light
4 - blinking + light (default)
        :type SecureLevel: str
        """
        self._SecureLevel = None

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel


    def _deserialize(self, params):
        self._SecureLevel = params.get("SecureLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyLivenessTokenResponse(AbstractModel):
    """ApplyLivenessToken response structure.

    """

    def __init__(self):
        r"""
        :param _SdkToken: The token used to identify an SDK-based verification process. It is valid for 10 minutes and can be used to get the verification result after the process is completed.
        :type SdkToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class ApplySdkVerificationTokenRequest(AbstractModel):
    """ApplySdkVerificationToken request structure.

    """

    def __init__(self):
        r"""
        :param _NeedVerifyIdCard: Whether ID card authentication is required. If not, only document OCR will be performed. Currently, authentication is available only when the value of `IdCardType` is `HK`.
        :type NeedVerifyIdCard: bool
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
        :type IdCardType: str
        :param _CompareImage: The Base64-encoded value of the photo to compare, which is required only when `CheckMode` is set to `2`.
        :type CompareImage: str
        :param _DisableChangeOcrResult: Whether to forbid the modification of the OCR result by users. Default value: `false` (modification allowed). (Currently, this parameter is not applied.)
        :type DisableChangeOcrResult: bool
        :param _DisableCheckOcrWarnings: Whether to disable the OCR warnings. Default value: `false` (not disable), where OCR warnings are enabled and the OCR result will not be returned if there is a warning.
This feature applies only to Hong Kong (China) identity cards, Malaysian identity cards, and passports.
        :type DisableCheckOcrWarnings: bool
        :param _Extra: A passthrough field, which is returned together with the verification result and can contain up to 1,024 bits.
        :type Extra: str
        """
        self._NeedVerifyIdCard = None
        self._CheckMode = None
        self._SecurityLevel = None
        self._IdCardType = None
        self._CompareImage = None
        self._DisableChangeOcrResult = None
        self._DisableCheckOcrWarnings = None
        self._Extra = None

    @property
    def NeedVerifyIdCard(self):
        return self._NeedVerifyIdCard

    @NeedVerifyIdCard.setter
    def NeedVerifyIdCard(self, NeedVerifyIdCard):
        self._NeedVerifyIdCard = NeedVerifyIdCard

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
        self._NeedVerifyIdCard = params.get("NeedVerifyIdCard")
        self._CheckMode = params.get("CheckMode")
        self._SecurityLevel = params.get("SecurityLevel")
        self._IdCardType = params.get("IdCardType")
        self._CompareImage = params.get("CompareImage")
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class ApplyWebVerificationBizTokenIntlRequest(AbstractModel):
    """ApplyWebVerificationBizTokenIntl request structure.

    """

    def __init__(self):
        r"""
        :param _CompareImageBase64: The Base64-encoded string (max 8 MB in size) of the photo to be compared.
        :type CompareImageBase64: str
        :param _RedirectURL: The web callback URL to redirect to after the verification is completed, including the protocol, hostname, and path. 
Example: https://www.tencentcloud.com/products/faceid.
After the verification process is completed, the BizToken of this process will be spliced to the callback URL in the format of https://www.tencentcloud.com/products/faceid?token={BizToken} before redirect.
        :type RedirectURL: str
        :param _Extra: The passthrough parameter of the business, max 1,000 characters, which will be returned in GetWebVerificationResultIntl.
        :type Extra: str
        :param _Config: The parameter control the page configuration.
        :type Config: :class:`tencentcloud.faceid.v20180301.models.WebVerificationConfigIntl`
        """
        self._CompareImageBase64 = None
        self._RedirectURL = None
        self._Extra = None
        self._Config = None

    @property
    def CompareImageBase64(self):
        return self._CompareImageBase64

    @CompareImageBase64.setter
    def CompareImageBase64(self, CompareImageBase64):
        self._CompareImageBase64 = CompareImageBase64

    @property
    def RedirectURL(self):
        return self._RedirectURL

    @RedirectURL.setter
    def RedirectURL(self, RedirectURL):
        self._RedirectURL = RedirectURL

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._CompareImageBase64 = params.get("CompareImageBase64")
        self._RedirectURL = params.get("RedirectURL")
        self._Extra = params.get("Extra")
        if params.get("Config") is not None:
            self._Config = WebVerificationConfigIntl()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWebVerificationBizTokenIntlResponse(AbstractModel):
    """ApplyWebVerificationBizTokenIntl response structure.

    """

    def __init__(self):
        r"""
        :param _VerificationUrl: The token identifying this web-based verification process, valid for 7,200s after issuance. It is required for getting the result after the verification process is completed.
        :type VerificationUrl: str
        :param _BizToken: The token for the web-based verification, which is generated using the ApplyWebVerificationBizTokenIntl API.
        :type BizToken: str
        :param _VerificationURL: The verification URL to be opened with a browser to start the verification process.
        :type VerificationURL: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VerificationUrl = None
        self._BizToken = None
        self._VerificationURL = None
        self._RequestId = None

    @property
    def VerificationUrl(self):
        warnings.warn("parameter `VerificationUrl` is deprecated", DeprecationWarning) 

        return self._VerificationUrl

    @VerificationUrl.setter
    def VerificationUrl(self, VerificationUrl):
        warnings.warn("parameter `VerificationUrl` is deprecated", DeprecationWarning) 

        self._VerificationUrl = VerificationUrl

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def VerificationURL(self):
        return self._VerificationURL

    @VerificationURL.setter
    def VerificationURL(self, VerificationURL):
        self._VerificationURL = VerificationURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VerificationUrl = params.get("VerificationUrl")
        self._BizToken = params.get("BizToken")
        self._VerificationURL = params.get("VerificationURL")
        self._RequestId = params.get("RequestId")


class ApplyWebVerificationTokenRequest(AbstractModel):
    """ApplyWebVerificationToken request structure.

    """

    def __init__(self):
        r"""
        :param _RedirectUrl: The web redirect URL after the verification is completed.
        :type RedirectUrl: str
        :param _CompareImageUrl: The COS URL of the image for face comparison, which can be obtained with one of the following methods:
1. Call the `CreateUploadUrl` API to generate a URL and call it again after the image is successfully uploaded.
2. Use an existing COS URL. For a private bucket, grant the download permission with a pre-signed URL. The corresponding COS bucket must be in the same region as the input parameter `Region`.
        :type CompareImageUrl: str
        :param _CompareImageMd5: The MD5 hash values of the image for face comparison (CompareImageUrl).
        :type CompareImageMd5: str
        """
        self._RedirectUrl = None
        self._CompareImageUrl = None
        self._CompareImageMd5 = None

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def CompareImageUrl(self):
        return self._CompareImageUrl

    @CompareImageUrl.setter
    def CompareImageUrl(self, CompareImageUrl):
        self._CompareImageUrl = CompareImageUrl

    @property
    def CompareImageMd5(self):
        return self._CompareImageMd5

    @CompareImageMd5.setter
    def CompareImageMd5(self, CompareImageMd5):
        self._CompareImageMd5 = CompareImageMd5


    def _deserialize(self, params):
        self._RedirectUrl = params.get("RedirectUrl")
        self._CompareImageUrl = params.get("CompareImageUrl")
        self._CompareImageMd5 = params.get("CompareImageMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWebVerificationTokenResponse(AbstractModel):
    """ApplyWebVerificationToken response structure.

    """

    def __init__(self):
        r"""
        :param _VerificationUrl: The verification URL to be opened with a browser to start the verification process.
        :type VerificationUrl: str
        :param _BizToken: The token used to identify a web-based verification process. It is valid for 7,200s and can be used to get the verification result after the process is completed.
        :type BizToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VerificationUrl = None
        self._BizToken = None
        self._RequestId = None

    @property
    def VerificationUrl(self):
        return self._VerificationUrl

    @VerificationUrl.setter
    def VerificationUrl(self, VerificationUrl):
        self._VerificationUrl = VerificationUrl

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VerificationUrl = params.get("VerificationUrl")
        self._BizToken = params.get("BizToken")
        self._RequestId = params.get("RequestId")


class CardVerifyResult(AbstractModel):
    """The OCR result of a user's identity document during the eKYC verification process.

    """

    def __init__(self):
        r"""
        :param _IsPass: Whether the authentication or OCR process is successful.
        :type IsPass: bool
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
        """
        self._IsPass = None
        self._CardVideo = None
        self._CardImage = None
        self._CardInfoOcrJson = None
        self._RequestId = None

    @property
    def IsPass(self):
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

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


    def _deserialize(self, params):
        self._IsPass = params.get("IsPass")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceLivenessRequest(AbstractModel):
    """CompareFaceLiveness request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64 value of photos used for face comparison. 
The size of image data encoded by Base64 shall not exceed 3M, only jpg and png are supported. 
Please use standard Base64 encoding (use = for padding). Refer to RFC4648 for encoding specifications. 
Example values: "/9j/4AAQSk... (total length:61944)KiiK//2Q=="
        :type ImageBase64: str
        :param _VideoBase64: Base64 value of photos used for face comparison. 
The size of image data encoded by Base64 shall not exceed 3M, only jpg and png are supported. 
Please use standard Base64 encoding (use = for padding). Refer to RFC4648 for encoding specifications. 
Example values: "/9j/4AAQSk... (total length:61944)KiiK//2Q=="
        :type VideoBase64: str
        :param _LivenessType: The liveness detection type. Valid values: `LIP`, `ACTION`, and `SILENT`.
`LIP`: Numeric mode; `ACTION`: Motion mode; `SILENT`: silent mode. Select one of them.
Example value: "SILENT"
        :type LivenessType: str
        :param _ValidateData: When the “LivenessType” parameter is “ACTION”, it must be specified.
It is used to control the action sequence. Action types: 
1 (open mouth)
2 (blink)
3 (nod)
4 (shake head). 
Select one or two from the four actions.
Example of passing single action parameter: "1".
Example of passing multiple action parameters: "4,2".
When the “LivenessType” parameter value is “SILENT”, it shall be unspecified.
Example value: ""
        :type ValidateData: str
        """
        self._ImageBase64 = None
        self._VideoBase64 = None
        self._LivenessType = None
        self._ValidateData = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._VideoBase64 = params.get("VideoBase64")
        self._LivenessType = params.get("LivenessType")
        self._ValidateData = params.get("ValidateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceLivenessResponse(AbstractModel):
    """CompareFaceLiveness response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Service error code. When the return value is "Success", it indicates that the liveness detection and face comparison succeeded. It is determined that they are the same person. When the return value is "FailedOperation.CompareLowSimilarity", it indicates that the liveness detection succeeded, and the face comparison similarity is lower than 70 points. It is determined that they are not the same person. For other error cases, please refer to Liveness Face Comparison (Pure API) Error Code (https://www.tencentcloud.com/document/product/1061/55390). 
Example Value: "Success".
        :type Result: str
        :param _Description: Description of business results. 
Example value: "Success"
        :type Description: str
        :param _Sim: This value is valid when the “Result” parameter is "Success" or "FailedOperation.CompareLowSimilarity." 
This value indicates the similarity of face comparison. Value range: [0.00, 100.00]. The false pass rate for threshold 70 is 1 in 1,000, and the false pass rate for threshold 80 is 1 in 1,000. 
Example value: 80.00
        :type Sim: float
        :param _BestFrameBase64: The optimal screenshot of the video after verification is the value encoded by BASE64, jpg format. 
Note: This field may return “null”, indicating that no valid value can be obtained. 
Example values: "/9j/4AAQSk... (total length:142036)s97n//2Q=="
        :type BestFrameBase64: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._Sim = None
        self._BestFrameBase64 = None
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
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Sim = params.get("Sim")
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._RequestId = params.get("RequestId")


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
        


class CreateUploadUrlRequest(AbstractModel):
    """CreateUploadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _TargetAction: Target API
        :type TargetAction: str
        """
        self._TargetAction = None

    @property
    def TargetAction(self):
        return self._TargetAction

    @TargetAction.setter
    def TargetAction(self, TargetAction):
        self._TargetAction = TargetAction


    def _deserialize(self, params):
        self._TargetAction = params.get("TargetAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUploadUrlResponse(AbstractModel):
    """CreateUploadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _UploadUrl: The URL for uploading contents with the `HTTP PUT` method.
        :type UploadUrl: str
        :param _ResourceUrl: The resource URL obtained after this upload is completed and to be passed in where it is required later.
        :type ResourceUrl: str
        :param _ExpiredTimestamp: The point in time when the upload/download link expires, which is a 10-bit Unix timestamp.
        :type ExpiredTimestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UploadUrl = None
        self._ResourceUrl = None
        self._ExpiredTimestamp = None
        self._RequestId = None

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def ResourceUrl(self):
        return self._ResourceUrl

    @ResourceUrl.setter
    def ResourceUrl(self, ResourceUrl):
        self._ResourceUrl = ResourceUrl

    @property
    def ExpiredTimestamp(self):
        return self._ExpiredTimestamp

    @ExpiredTimestamp.setter
    def ExpiredTimestamp(self, ExpiredTimestamp):
        self._ExpiredTimestamp = ExpiredTimestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UploadUrl = params.get("UploadUrl")
        self._ResourceUrl = params.get("ResourceUrl")
        self._ExpiredTimestamp = params.get("ExpiredTimestamp")
        self._RequestId = params.get("RequestId")


class DetectReflectLivenessAndCompareRequest(AbstractModel):
    """DetectReflectLivenessAndCompare request structure.

    """

    def __init__(self):
        r"""
        :param _LiveDataUrl: URL of the liveness detection data package generated by the SDK
        :type LiveDataUrl: str
        :param _LiveDataMd5: MD5 hash value (32-bit) of the liveness detection data package generated by the SDK, which is used to verify the LiveData consistency.
        :type LiveDataMd5: str
        :param _ImageUrl: URL of the target image for comparison
        :type ImageUrl: str
        :param _ImageMd5: MD5 hash value (32-bit) of the target image for comparison, which is used to verify the `Image` consistency.
        :type ImageMd5: str
        """
        self._LiveDataUrl = None
        self._LiveDataMd5 = None
        self._ImageUrl = None
        self._ImageMd5 = None

    @property
    def LiveDataUrl(self):
        return self._LiveDataUrl

    @LiveDataUrl.setter
    def LiveDataUrl(self, LiveDataUrl):
        self._LiveDataUrl = LiveDataUrl

    @property
    def LiveDataMd5(self):
        return self._LiveDataMd5

    @LiveDataMd5.setter
    def LiveDataMd5(self, LiveDataMd5):
        self._LiveDataMd5 = LiveDataMd5

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageMd5(self):
        return self._ImageMd5

    @ImageMd5.setter
    def ImageMd5(self, ImageMd5):
        self._ImageMd5 = ImageMd5


    def _deserialize(self, params):
        self._LiveDataUrl = params.get("LiveDataUrl")
        self._LiveDataMd5 = params.get("LiveDataMd5")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageMd5 = params.get("ImageMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectReflectLivenessAndCompareResponse(AbstractModel):
    """DetectReflectLivenessAndCompare response structure.

    """

    def __init__(self):
        r"""
        :param _BestFrameUrl: Temporary URL of the best screenshot (.jpg) of the video after successful verification. Both the screenshot and the URL are valid for two hours only, so you need to download the screenshot within this period.
        :type BestFrameUrl: str
        :param _BestFrameMd5: MD5 hash value (32-bit) of the best screenshot of the video after successful verification, which is used to verify the `BestFrame` consistency.
        :type BestFrameMd5: str
        :param _Result: Service error code. `Success` will be returned for success. For error information, see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param _Description: Service result description
        :type Description: str
        :param _Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BestFrameUrl = None
        self._BestFrameMd5 = None
        self._Result = None
        self._Description = None
        self._Sim = None
        self._RequestId = None

    @property
    def BestFrameUrl(self):
        return self._BestFrameUrl

    @BestFrameUrl.setter
    def BestFrameUrl(self, BestFrameUrl):
        self._BestFrameUrl = BestFrameUrl

    @property
    def BestFrameMd5(self):
        return self._BestFrameMd5

    @BestFrameMd5.setter
    def BestFrameMd5(self, BestFrameMd5):
        self._BestFrameMd5 = BestFrameMd5

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
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BestFrameUrl = params.get("BestFrameUrl")
        self._BestFrameMd5 = params.get("BestFrameMd5")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Sim = params.get("Sim")
        self._RequestId = params.get("RequestId")


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
        


class GenerateReflectSequenceRequest(AbstractModel):
    """GenerateReflectSequence request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceDataUrl: The resource URL of the data package generated by the SDK.
        :type DeviceDataUrl: str
        :param _DeviceDataMd5: The MD5 hash value of the data package generated by the SDK.
        :type DeviceDataMd5: str
        :param _SecurityLevel: 1 - silent
2 - blinking
3 - light
4 - blinking + light (default)
        :type SecurityLevel: str
        """
        self._DeviceDataUrl = None
        self._DeviceDataMd5 = None
        self._SecurityLevel = None

    @property
    def DeviceDataUrl(self):
        return self._DeviceDataUrl

    @DeviceDataUrl.setter
    def DeviceDataUrl(self, DeviceDataUrl):
        self._DeviceDataUrl = DeviceDataUrl

    @property
    def DeviceDataMd5(self):
        return self._DeviceDataMd5

    @DeviceDataMd5.setter
    def DeviceDataMd5(self, DeviceDataMd5):
        self._DeviceDataMd5 = DeviceDataMd5

    @property
    def SecurityLevel(self):
        return self._SecurityLevel

    @SecurityLevel.setter
    def SecurityLevel(self, SecurityLevel):
        self._SecurityLevel = SecurityLevel


    def _deserialize(self, params):
        self._DeviceDataUrl = params.get("DeviceDataUrl")
        self._DeviceDataMd5 = params.get("DeviceDataMd5")
        self._SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateReflectSequenceResponse(AbstractModel):
    """GenerateReflectSequence response structure.

    """

    def __init__(self):
        r"""
        :param _ReflectSequenceUrl: The resource URL of the light sequence, which needs to be downloaded and passed through to the SDK to start the identity verification process.
        :type ReflectSequenceUrl: str
        :param _ReflectSequenceMd5: The MD5 hash value of the light sequence, which is used to check whether the light sequence is altered.
        :type ReflectSequenceMd5: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReflectSequenceUrl = None
        self._ReflectSequenceMd5 = None
        self._RequestId = None

    @property
    def ReflectSequenceUrl(self):
        return self._ReflectSequenceUrl

    @ReflectSequenceUrl.setter
    def ReflectSequenceUrl(self, ReflectSequenceUrl):
        self._ReflectSequenceUrl = ReflectSequenceUrl

    @property
    def ReflectSequenceMd5(self):
        return self._ReflectSequenceMd5

    @ReflectSequenceMd5.setter
    def ReflectSequenceMd5(self, ReflectSequenceMd5):
        self._ReflectSequenceMd5 = ReflectSequenceMd5

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReflectSequenceUrl = params.get("ReflectSequenceUrl")
        self._ReflectSequenceMd5 = params.get("ReflectSequenceMd5")
        self._RequestId = params.get("RequestId")


class GetFaceIdResultIntlRequest(AbstractModel):
    """GetFaceIdResultIntl request structure.

    """

    def __init__(self):
        r"""
        :param _SdkToken: The ID of the SDK-based liveness detection and face comparison process, which is generated when the `GetFaceIdTokenIntl` API is called.	
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
        


class GetFaceIdResultIntlResponse(AbstractModel):
    """GetFaceIdResultIntl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The return code of the verification result.
0: Succeeded.
1001: System error.
1004: Liveness detection and face comparison failed.
2004: The image passed in is too large or too small.
2012: Several faces were detected.
2013: No face was detected, or the face detected was incomplete.
2014: The image resolution is too low or the quality does not meet the requirements.
2015: Face comparison failed.
2016: The similarity did not reach the standard passing threshold.
-999: The verification process wasn't finished.
        :type Result: str
        :param _Description: The description of the verification result.
        :type Description: str
        :param _BestFrame: The best frame screenshot (in Base64) obtained during the verification.
        :type BestFrame: str
        :param _Video: The video file (Base64) for verification.
        :type Video: str
        :param _Similarity: The similarity, with a value range of 0-100. A greater value indicates higher similarity. This parameter is returned only in the `compare` (liveness detection and face comparison) mode.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Similarity: float
        :param _Extra: The pass-through parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._BestFrame = None
        self._Video = None
        self._Similarity = None
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
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

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
        self._BestFrame = params.get("BestFrame")
        self._Video = params.get("Video")
        self._Similarity = params.get("Similarity")
        self._Extra = params.get("Extra")
        self._RequestId = params.get("RequestId")


class GetFaceIdTokenIntlRequest(AbstractModel):
    """GetFaceIdTokenIntl request structure.

    """

    def __init__(self):
        r"""
        :param _CheckMode: The detection mode. Valid values:
`liveness`: Liveness detection only.
`compare`: Liveness detection and face comparison.
Default value: `liveness`.
        :type CheckMode: str
        :param _SecureLevel: The verification security level. Valid values:
`1`: Video-based liveness detection.
`2`: Motion-based liveness detection.
`3`: Reflection-based liveness detection.
`4`: Motion- and reflection-based liveness detection.
Default value: `4`.
        :type SecureLevel: str
        :param _Image: The photo (in Base64) to compare. This parameter is required when the value of `CheckMode` is `compare`.
        :type Image: str
        :param _Extra: The pass-through parameter, which can be omitted if there are no special requirements.
        :type Extra: str
        """
        self._CheckMode = None
        self._SecureLevel = None
        self._Image = None
        self._Extra = None

    @property
    def CheckMode(self):
        return self._CheckMode

    @CheckMode.setter
    def CheckMode(self, CheckMode):
        self._CheckMode = CheckMode

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._CheckMode = params.get("CheckMode")
        self._SecureLevel = params.get("SecureLevel")
        self._Image = params.get("Image")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdTokenIntlResponse(AbstractModel):
    """GetFaceIdTokenIntl response structure.

    """

    def __init__(self):
        r"""
        :param _SdkToken: The SDK token, which is used throughout the verification process and to get the verification result.
        :type SdkToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class GetLivenessResultRequest(AbstractModel):
    """GetLivenessResult request structure.

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
        


class GetLivenessResultResponse(AbstractModel):
    """GetLivenessResult response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The final verification result.
        :type Result: str
        :param _Description: The description of the final verification result.
        :type Description: str
        :param _BestFrame: The face screenshot.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _Video: The video for the detection.
        :type Video: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._BestFrame = None
        self._Video = None
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
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        if params.get("BestFrame") is not None:
            self._BestFrame = FileInfo()
            self._BestFrame._deserialize(params.get("BestFrame"))
        if params.get("Video") is not None:
            self._Video = FileInfo()
            self._Video._deserialize(params.get("Video"))
        self._RequestId = params.get("RequestId")


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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class GetWebVerificationResultIntlRequest(AbstractModel):
    """GetWebVerificationResultIntl request structure.

    """

    def __init__(self):
        r"""
        :param _BizToken: The token for the web-based verification, which is generated using the `ApplyWebVerificationBizTokenIntl` API.
        :type BizToken: str
        """
        self._BizToken = None

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken


    def _deserialize(self, params):
        self._BizToken = params.get("BizToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWebVerificationResultIntlResponse(AbstractModel):
    """GetWebVerificationResultIntl response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
For other error codes, see <a href="https://www.tencentcloud.com/document/product/1061/55390?lang=en&pg=#8a960e1e-39c0-42cb-b181-b3164d77f81e">Liveness Detection and Face Comparison (Mobile HTML5) Error Codes</a>
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param _ErrorMsg: The description of the final verification result.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _VerificationDetailList: The detailed verification result list of this process. Retries are allowed, so a verification process may have several entries of results.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type VerificationDetailList: list of VerificationDetail
        :param _VideoBase64: The Base64-encoded string of the video collected from the video stream. Retries are allowed, and this field returns only the data collected in the last verification. If no video is collected, null is returned.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type VideoBase64: str
        :param _BestFrameBase64: The Base64-encoded string of the best face screenshot u200dcollected from the video stream. Retries are allowed, and this field returns only the data collected in the last verification. If no best face screenshot is collected, null is returned.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type BestFrameBase64: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._VerificationDetailList = None
        self._VideoBase64 = None
        self._BestFrameBase64 = None
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
    def VerificationDetailList(self):
        return self._VerificationDetailList

    @VerificationDetailList.setter
    def VerificationDetailList(self, VerificationDetailList):
        self._VerificationDetailList = VerificationDetailList

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("VerificationDetailList") is not None:
            self._VerificationDetailList = []
            for item in params.get("VerificationDetailList"):
                obj = VerificationDetail()
                obj._deserialize(item)
                self._VerificationDetailList.append(obj)
        self._VideoBase64 = params.get("VideoBase64")
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._RequestId = params.get("RequestId")


class GetWebVerificationResultRequest(AbstractModel):
    """GetWebVerificationResult request structure.

    """

    def __init__(self):
        r"""
        :param _BizToken: The token for the web-based verification, which is generated with the `ApplyWebVerificationToken` API.
        :type BizToken: str
        """
        self._BizToken = None

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken


    def _deserialize(self, params):
        self._BizToken = params.get("BizToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWebVerificationResultResponse(AbstractModel):
    """GetWebVerificationResult response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param _ErrorMsg: The description of the final verification result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _VideoBestFrameUrl: The temporary URL of the best face screenshot collected from the video stream. It is valid for 10 minutes. Download the image if needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoBestFrameUrl: str
        :param _VideoBestFrameMd5: The MD5 hash value of the best face screenshot collected from the video stream. It can be used to check whether the image content is consistent with the file content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoBestFrameMd5: str
        :param _VerificationDetailList: The details list of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VerificationDetailList: list of VerificationDetail
        :param _VideoUrl: The temporary URL of the video collected from the video stream. It is valid for 10 minutes. Download the video if needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoUrl: str
        :param _VideoMd5: The MD5 hash value of the video collected from the video stream. It can be used to check whether the video content is consistent with the file content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoMd5: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._VideoBestFrameUrl = None
        self._VideoBestFrameMd5 = None
        self._VerificationDetailList = None
        self._VideoUrl = None
        self._VideoMd5 = None
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
    def VideoBestFrameUrl(self):
        return self._VideoBestFrameUrl

    @VideoBestFrameUrl.setter
    def VideoBestFrameUrl(self, VideoBestFrameUrl):
        self._VideoBestFrameUrl = VideoBestFrameUrl

    @property
    def VideoBestFrameMd5(self):
        return self._VideoBestFrameMd5

    @VideoBestFrameMd5.setter
    def VideoBestFrameMd5(self, VideoBestFrameMd5):
        self._VideoBestFrameMd5 = VideoBestFrameMd5

    @property
    def VerificationDetailList(self):
        return self._VerificationDetailList

    @VerificationDetailList.setter
    def VerificationDetailList(self, VerificationDetailList):
        self._VerificationDetailList = VerificationDetailList

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def VideoMd5(self):
        return self._VideoMd5

    @VideoMd5.setter
    def VideoMd5(self, VideoMd5):
        self._VideoMd5 = VideoMd5

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._VideoBestFrameUrl = params.get("VideoBestFrameUrl")
        self._VideoBestFrameMd5 = params.get("VideoBestFrameMd5")
        if params.get("VerificationDetailList") is not None:
            self._VerificationDetailList = []
            for item in params.get("VerificationDetailList"):
                obj = VerificationDetail()
                obj._deserialize(item)
                self._VerificationDetailList.append(obj)
        self._VideoUrl = params.get("VideoUrl")
        self._VideoMd5 = params.get("VideoMd5")
        self._RequestId = params.get("RequestId")


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare request structure.

    """

    def __init__(self):
        r"""
        :param _LivenessType: Liveness detection type. Valid values: LIP/ACTION/SILENT.
LIP: numeric mode; ACTION: motion mode; SILENT: silent mode. You need to select a mode to input.
        :type LivenessType: str
        :param _ImageBase64: Base64 string of the image for face comparison.
The size of the Base64-encoded image data can be up to 3 MB. JPG and PNG formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.
        :type ImageBase64: str
        :param _ImageUrl: URL of the image for face comparison. The size of the downloaded image after Base64 encoding can be up to 3 MB. JPG and PNG formats are supported.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.

We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _ValidateData: Lip mode: set this parameter to a custom 4-digit verification code.
Action mode: set this parameter to a custom action sequence (e.g., `2,1` or `1,2`).
Silent mode: do not pass in this parameter.
        :type ValidateData: str
        :param _Optional: Optional configuration (a JSON string)
{
"BestFrameNum": 2  // Return multiple best screenshots. Value range: 2−10
}
        :type Optional: str
        :param _VideoBase64: Base64 string of the video for liveness detection.
The size of the Base64-encoded video data can be up to 8 MB. MP4, AVI, and FLV formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.
        :type VideoBase64: str
        :param _VideoUrl: URL of the video for liveness detection. The size of the downloaded video after Base64 encoding can be up to 8 MB. It takes no more than 4 seconds to download. MP4, AVI, and FLV formats are supported.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.

We recommend you store the video in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type VideoUrl: str
        """
        self._LivenessType = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ValidateData = None
        self._Optional = None
        self._VideoBase64 = None
        self._VideoUrl = None

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl


    def _deserialize(self, params):
        self._LivenessType = params.get("LivenessType")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ValidateData = params.get("ValidateData")
        self._Optional = params.get("Optional")
        self._VideoBase64 = params.get("VideoBase64")
        self._VideoUrl = params.get("VideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare response structure.

    """

    def __init__(self):
        r"""
        :param _BestFrameBase64: The best screenshot of the video after successful verification. The photo is Base64-encoded and in JPG format.
        :type BestFrameBase64: str
        :param _Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param _Result: Service error code. `Success` will be returned for success. For error information, please see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param _Description: Service result description.
        :type Description: str
        :param _BestFrameList: 
        :type BestFrameList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BestFrameBase64 = None
        self._Sim = None
        self._Result = None
        self._Description = None
        self._BestFrameList = None
        self._RequestId = None

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

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
    def BestFrameList(self):
        return self._BestFrameList

    @BestFrameList.setter
    def BestFrameList(self, BestFrameList):
        self._BestFrameList = BestFrameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._BestFrameList = params.get("BestFrameList")
        self._RequestId = params.get("RequestId")


class VerificationDetail(AbstractModel):
    """The details of the verification process.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param _ErrorMsg: The description of the final verification result.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _LivenessErrorCode: The result of this liveness detection process. `0` indicates success.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorCode: int
        :param _LivenessErrorMsg: The result description of this liveness detection process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorMsg: str
        :param _CompareErrorCode: The result of this comparison process. `0` indicates that the person in the best face screenshot collected from the video stream is the same as that in the uploaded image for comparison.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type CompareErrorCode: int
        :param _CompareErrorMsg: The result description of this comparison process.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type CompareErrorMsg: str
        :param _ReqTimestamp: The timestamp (ms) of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReqTimestamp: int
        :param _Similarity: The similarity of the best face screenshot collected from the video stream and the uploaded image for comparison in this verification process. Value range: [0.00, 100.00]. By default, the person in the screenshot is determined to be the same person in the image if the similarity is greater than or equal to 70.
Note: u200dThis field may return null, indicating that no valid values can be obtained.
        :type Similarity: float
        :param _Seq: Unique ID of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Seq: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._LivenessErrorCode = None
        self._LivenessErrorMsg = None
        self._CompareErrorCode = None
        self._CompareErrorMsg = None
        self._ReqTimestamp = None
        self._Similarity = None
        self._Seq = None

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
    def LivenessErrorCode(self):
        return self._LivenessErrorCode

    @LivenessErrorCode.setter
    def LivenessErrorCode(self, LivenessErrorCode):
        self._LivenessErrorCode = LivenessErrorCode

    @property
    def LivenessErrorMsg(self):
        return self._LivenessErrorMsg

    @LivenessErrorMsg.setter
    def LivenessErrorMsg(self, LivenessErrorMsg):
        self._LivenessErrorMsg = LivenessErrorMsg

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
    def ReqTimestamp(self):
        return self._ReqTimestamp

    @ReqTimestamp.setter
    def ReqTimestamp(self, ReqTimestamp):
        self._ReqTimestamp = ReqTimestamp

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._LivenessErrorCode = params.get("LivenessErrorCode")
        self._LivenessErrorMsg = params.get("LivenessErrorMsg")
        self._CompareErrorCode = params.get("CompareErrorCode")
        self._CompareErrorMsg = params.get("CompareErrorMsg")
        self._ReqTimestamp = params.get("ReqTimestamp")
        self._Similarity = params.get("Similarity")
        self._Seq = params.get("Seq")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoLivenessCompareRequest(AbstractModel):
    """VideoLivenessCompare request structure.

    """

    def __init__(self):
        r"""
        :param _ImageUrl: The URL of the photo for face comparison. The downloaded image after Base64 encoding can be up to 3 MB and must be in JPG or PNG.

The image must be stored in a COS bucket in the region where the FaceID service resides to ensure a higher download speed and better stability. You can generate an image URL by using `CreateUploadUrl` or purchase the COS service.
        :type ImageUrl: str
        :param _ImageMd5: The 32-bit MD5 checksum of the image for comparison
        :type ImageMd5: str
        :param _VideoUrl: The URL of the video for liveness detection. The downloaded video after Base64 encoding can be up to 8 MB and must be in MP4, AVI, or FLV. It takes no more than 4s to download the video.

The video must be stored in a COS bucket in the region where the FaceID service resides to ensure a higher download speed and better stability. You can generate a video URL by using `CreateUploadUrl` or purchase the COS service.
        :type VideoUrl: str
        :param _VideoMd5: The 32-bit MD5 checksum of the video
        :type VideoMd5: str
        :param _LivenessType: The liveness detection type. Valid values: `LIP`, `ACTION`, and `SILENT`.
`LIP`: Numeric mode; `ACTION`: Motion mode; `SILENT`: silent mode. Select one of them.
        :type LivenessType: str
        :param _ValidateData: LIP parameter: Pass in a custom 4-digit verification code.
ACTION parameter: Pass in a custom action sequence (`2,1` or `1,2`).
SILENT parameter: Null.
        :type ValidateData: str
        """
        self._ImageUrl = None
        self._ImageMd5 = None
        self._VideoUrl = None
        self._VideoMd5 = None
        self._LivenessType = None
        self._ValidateData = None

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageMd5(self):
        return self._ImageMd5

    @ImageMd5.setter
    def ImageMd5(self, ImageMd5):
        self._ImageMd5 = ImageMd5

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def VideoMd5(self):
        return self._VideoMd5

    @VideoMd5.setter
    def VideoMd5(self, VideoMd5):
        self._VideoMd5 = VideoMd5

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageMd5 = params.get("ImageMd5")
        self._VideoUrl = params.get("VideoUrl")
        self._VideoMd5 = params.get("VideoMd5")
        self._LivenessType = params.get("LivenessType")
        self._ValidateData = params.get("ValidateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoLivenessCompareResponse(AbstractModel):
    """VideoLivenessCompare response structure.

    """

    def __init__(self):
        r"""
        :param _Sim: The similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two persons are of the same person. You can adjust the threshold according to your specific scenario (the FARs at the thresholds of 70 and 80 are 0.1% and 0.01%, respectively).
        :type Sim: float
        :param _Result: The service error code. `Success` will be returned for success. For error information, see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param _Description: The service result description
        :type Description: str
        :param _BestFrame: The best video screenshot after successful verification
Note: This field may return null, indicating that no valid values can be obtained.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Sim = None
        self._Result = None
        self._Description = None
        self._BestFrame = None
        self._RequestId = None

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

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
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        if params.get("BestFrame") is not None:
            self._BestFrame = FileInfo()
            self._BestFrame._deserialize(params.get("BestFrame"))
        self._RequestId = params.get("RequestId")


class WebVerificationConfigIntl(AbstractModel):
    """eKYC Web related configuration

    """

    def __init__(self):
        r"""
        :param _AutoSkip: Whether to automatically redirect to RedirectUrl after successful verification. Default value: false.
        :type AutoSkip: bool
        """
        self._AutoSkip = None

    @property
    def AutoSkip(self):
        return self._AutoSkip

    @AutoSkip.setter
    def AutoSkip(self, AutoSkip):
        self._AutoSkip = AutoSkip


    def _deserialize(self, params):
        self._AutoSkip = params.get("AutoSkip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        