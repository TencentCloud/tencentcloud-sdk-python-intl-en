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
        


class ApplyCardVerificationRequest(AbstractModel):
    """ApplyCardVerification request structure.

    """

    def __init__(self):
        r"""
        :param _Nationality: Please select the country code of ID document.
IDN: Indonesia
HKG: Hong Kong
THA: Thailand
MYS: Malaysia
SGP: Singapore
JPN: Japan
TWN:Taiwan
AUTO: Automatic Identification
        :type Nationality: str
        :param _CardType: Please select the type of ID document. The supported options are:
ID_CARD
PASSPORT
DRIVING_LICENSE
AUTO
        :type CardType: str
        :param _ImageBase64Front: Base64 value for the front of the document. Supported image formats: PNG, JPEG. 
GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 5M after Base64 encoding.
The image download takes no more than 3 seconds. Supported image resolution: 8000*8000. One of ImageUrlFront and ImageBase64 Front of the image must be provided. If both are provided, only ImageUrlFront will be used.
        :type ImageBase64Front: str
        :param _ImageBase64Back: Base64 value of the reverse side of the document. Supported image formats: PNG, JPEG. 
GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 5M after Base64 encoding. The image download takes no more than 3 seconds. Maximum supported image resolution: 8000*8000. For some certificates, one of ImageUrlBack and ImageBase64Back must be provided. If both are provided, only ImageUrlBack will be used.
        :type ImageBase64Back: str
        :param _ImageUrlFront: The URL value on the back of the certificate. Supported image formats: PNG, JPEG. 
GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 5M after Base64 encoding. The image download takes no more than 3 seconds. Maximum supported image resolution: 8000*8000. One of ImageUrlFront and ImageBase64Front of the image must be provided. If both are provided, only ImageUrlFront will be used.
        :type ImageUrlFront: str
        :param _ImageUrlBack: The URL value on the back of the certificate. Supported image formats: PNG, JPEG. 
GIF format is not supported yet. Supported image size: The downloaded image cannot exceed 5M after Base64 encoding. The image download takes no more than 3 seconds. Maximum supported image resolution: 8000*8000. For some certificates, one of ImageUrlBack and ImageBase64Back must be provided. If both are provided, only ImageUrlBack will be used.
        :type ImageUrlBack: str
        """
        self._Nationality = None
        self._CardType = None
        self._ImageBase64Front = None
        self._ImageBase64Back = None
        self._ImageUrlFront = None
        self._ImageUrlBack = None

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def ImageBase64Front(self):
        return self._ImageBase64Front

    @ImageBase64Front.setter
    def ImageBase64Front(self, ImageBase64Front):
        self._ImageBase64Front = ImageBase64Front

    @property
    def ImageBase64Back(self):
        return self._ImageBase64Back

    @ImageBase64Back.setter
    def ImageBase64Back(self, ImageBase64Back):
        self._ImageBase64Back = ImageBase64Back

    @property
    def ImageUrlFront(self):
        return self._ImageUrlFront

    @ImageUrlFront.setter
    def ImageUrlFront(self, ImageUrlFront):
        self._ImageUrlFront = ImageUrlFront

    @property
    def ImageUrlBack(self):
        return self._ImageUrlBack

    @ImageUrlBack.setter
    def ImageUrlBack(self, ImageUrlBack):
        self._ImageUrlBack = ImageUrlBack


    def _deserialize(self, params):
        self._Nationality = params.get("Nationality")
        self._CardType = params.get("CardType")
        self._ImageBase64Front = params.get("ImageBase64Front")
        self._ImageBase64Back = params.get("ImageBase64Back")
        self._ImageUrlFront = params.get("ImageUrlFront")
        self._ImageUrlBack = params.get("ImageUrlBack")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCardVerificationResponse(AbstractModel):
    """ApplyCardVerification response structure.

    """

    def __init__(self):
        r"""
        :param _CardVerificationToken: The token used to identify an verification process. It can be used to get the verification result after the process is completed.
        :type CardVerificationToken: str
        :param _AsyncCardVerificationMaxPollingTimes: The maximum number of polls for calling the pull result interface polling.
        :type AsyncCardVerificationMaxPollingTimes: int
        :param _AsyncCardVerificationPollingWaitTime: The interval for polling when calling the pull result interface (in seconds).
        :type AsyncCardVerificationPollingWaitTime: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CardVerificationToken = None
        self._AsyncCardVerificationMaxPollingTimes = None
        self._AsyncCardVerificationPollingWaitTime = None
        self._RequestId = None

    @property
    def CardVerificationToken(self):
        return self._CardVerificationToken

    @CardVerificationToken.setter
    def CardVerificationToken(self, CardVerificationToken):
        self._CardVerificationToken = CardVerificationToken

    @property
    def AsyncCardVerificationMaxPollingTimes(self):
        return self._AsyncCardVerificationMaxPollingTimes

    @AsyncCardVerificationMaxPollingTimes.setter
    def AsyncCardVerificationMaxPollingTimes(self, AsyncCardVerificationMaxPollingTimes):
        self._AsyncCardVerificationMaxPollingTimes = AsyncCardVerificationMaxPollingTimes

    @property
    def AsyncCardVerificationPollingWaitTime(self):
        return self._AsyncCardVerificationPollingWaitTime

    @AsyncCardVerificationPollingWaitTime.setter
    def AsyncCardVerificationPollingWaitTime(self, AsyncCardVerificationPollingWaitTime):
        self._AsyncCardVerificationPollingWaitTime = AsyncCardVerificationPollingWaitTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CardVerificationToken = params.get("CardVerificationToken")
        self._AsyncCardVerificationMaxPollingTimes = params.get("AsyncCardVerificationMaxPollingTimes")
        self._AsyncCardVerificationPollingWaitTime = params.get("AsyncCardVerificationPollingWaitTime")
        self._RequestId = params.get("RequestId")


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
1. HK (default): Identity card of Hong Kong (China)
2. ML: Malaysian identity card
3. IndonesiaIDCard: Indonesian identity card
4. PhilippinesVoteID: Philippine voters ID card
5. PhilippinesDrivingLicense: Philippine driver's license
6. PhilippinesTinID: Philippine TIN ID card
7. PhilippinesSSSID: Philippine SSS ID card
8. PhilippinesUMID: Philippine UMID card
9. MLIDPassport: Passport issued in Hong Kong/Macao/Taiwan (China) or other countries/regions
10..MacaoIDCard: Macao ID Card
11.ThailandIDCard: Thailand ID Card
12.MainlandIDCard: Mainland ID Card
13.SingaporeIDCard: Singapore ID Card
14.JapanIDCard: Japan ID Card
15.MLDrivingLicense: Malaysian Driving License
16.IndonesiaDrivingLicense: Indonesia Driving License
17.ThailandDrivingLicense: Thailand Driving License
18.SingaporeDrivingLicense: Singapore Driving License
19.JapanDrivingLicense: Japan Driving License
20.TaiWanIDCard:Taiwan ID Card
21.HMTPermit: exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan
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
        :param _ActionList: This interface is used to control th action sequences.
Action types are as follows:
"blink"
"mouth"
"nod"
"shake"
You can choose 1-2 actions out of the four.
Single action example: "blink"
Multiple action example: "blink,mouth"
The default value is blink. The different action types passed in this parameter take effect only when the SecurityLevel is 2 or 4; otherwise, the interface reports an error.
        :type ActionList: str
        """
        self._CheckMode = None
        self._SecurityLevel = None
        self._IdCardType = None
        self._CompareImage = None
        self._NeedVerifyIdCard = None
        self._DisableChangeOcrResult = None
        self._DisableCheckOcrWarnings = None
        self._Extra = None
        self._ActionList = None

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

    @property
    def ActionList(self):
        return self._ActionList

    @ActionList.setter
    def ActionList(self, ActionList):
        self._ActionList = ActionList


    def _deserialize(self, params):
        self._CheckMode = params.get("CheckMode")
        self._SecurityLevel = params.get("SecurityLevel")
        self._IdCardType = params.get("IdCardType")
        self._CompareImage = params.get("CompareImage")
        self._NeedVerifyIdCard = params.get("NeedVerifyIdCard")
        self._DisableChangeOcrResult = params.get("DisableChangeOcrResult")
        self._DisableCheckOcrWarnings = params.get("DisableCheckOcrWarnings")
        self._Extra = params.get("Extra")
        self._ActionList = params.get("ActionList")
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


class ApplyWebVerificationBizTokenIntlRequest(AbstractModel):
    """ApplyWebVerificationBizTokenIntl request structure.

    """

    def __init__(self):
        r"""
        :param _RedirectURL: The web callback URL to redirect to after the verification is completed, including the protocol, hostname, and path. 
After the verification process is completed, the BizToken of this process will be spliced to the callback URL in the format of https://www.tencentcloud.com/products/faceid?token={BizToken} before redirect.
Example: https://www.tencentcloud.com/products/faceid.
        :type RedirectURL: str
        :param _CompareImageBase64: The Base64-encoded string (max 8 MB in size) of the photo to be compared.The Data URI scheme header needs to be removed from the encoded string
Example: xhBQAAACBjSFJNAAB6****AAAASUVORK5CYII=
        :type CompareImageBase64: str
        :param _Extra: The passthrough parameter of the business, max 1,000 characters, which will be returned in GetWebVerificationResultIntl.
        :type Extra: str
        :param _Config: The parameter control the page configuration.
Example: {"AutoSkip": true,"CheckMode": 1,"IdCardType": "HKIDCard"}
        :type Config: :class:`tencentcloud.faceid.v20180301.models.WebVerificationConfigIntl`
        """
        self._RedirectURL = None
        self._CompareImageBase64 = None
        self._Extra = None
        self._Config = None

    @property
    def RedirectURL(self):
        return self._RedirectURL

    @RedirectURL.setter
    def RedirectURL(self, RedirectURL):
        self._RedirectURL = RedirectURL

    @property
    def CompareImageBase64(self):
        return self._CompareImageBase64

    @CompareImageBase64.setter
    def CompareImageBase64(self, CompareImageBase64):
        self._CompareImageBase64 = CompareImageBase64

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
        self._RedirectURL = params.get("RedirectURL")
        self._CompareImageBase64 = params.get("CompareImageBase64")
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
Example: https://intl.faceid.qq.com/reflect/?token=81EEF678-28EE-4759-A82E-6CBBBE6BC442
        :type VerificationUrl: str
        :param _BizToken: The token for the web-based verification, which is generated using the ApplyWebVerificationBizTokenIntl API.
Example: 81EEF678-28EE-4759-A82E-6CBBBE6BC442
        :type BizToken: str
        :param _VerificationURL: The verification URL to be opened with a browser to start the verification process.
Example: https://intl.faceid.qq.com/reflect/?token=81EEF678-28EE-4759-A82E-6CBBBE6BC442
        :type VerificationURL: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class AttackRiskDetail(AbstractModel):
    """Suspected attack detail

    """

    def __init__(self):
        r"""
        :param _Type: Suspected attack trace types
SuspectedSpoofingAttack: Suspected spoofing attack
 SuspectedSynthesisImage: Suspected synthesis image SuspectedSynthesisVideo: Suspected synthesis video SuspectedeAnomalyAttack: Suspected anomaly attack SuspectedAdversarialAttack: Suspected adversarial attack SuspectedBlackIndustry: Suspected batch generation attack
SuspectedWatermark: Suspected watermark
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _TaiWanIDCard: TaiWan ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaiWanIDCard: :class:`tencentcloud.faceid.v20180301.models.TaiWanIDCard`
        :param _JapanIDCard: Japan ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type JapanIDCard: :class:`tencentcloud.faceid.v20180301.models.JapanIDCard`
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
        self._TaiWanIDCard = None
        self._JapanIDCard = None

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

    @property
    def TaiWanIDCard(self):
        return self._TaiWanIDCard

    @TaiWanIDCard.setter
    def TaiWanIDCard(self, TaiWanIDCard):
        self._TaiWanIDCard = TaiWanIDCard

    @property
    def JapanIDCard(self):
        return self._JapanIDCard

    @JapanIDCard.setter
    def JapanIDCard(self, JapanIDCard):
        self._JapanIDCard = JapanIDCard


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
        if params.get("TaiWanIDCard") is not None:
            self._TaiWanIDCard = TaiWanIDCard()
            self._TaiWanIDCard._deserialize(params.get("TaiWanIDCard"))
        if params.get("JapanIDCard") is not None:
            self._JapanIDCard = JapanIDCard()
            self._JapanIDCard._deserialize(params.get("JapanIDCard"))
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
        :param _EditDetails: Details of the OCR modifications for this EKYC card, when the user manually modifies the card recognition results (IsEdit=true), EditDetails will return the modified fields. When IsEdit=false, EditDetails is empty.
        :type EditDetails: list of EditDetail
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
        self._EditDetails = None

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

    @property
    def EditDetails(self):
        return self._EditDetails

    @EditDetails.setter
    def EditDetails(self, EditDetails):
        self._EditDetails = EditDetails


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
        if params.get("EditDetails") is not None:
            self._EditDetails = []
            for item in params.get("EditDetails"):
                obj = EditDetail()
                obj._deserialize(item)
                self._EditDetails.append(obj)
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
        :param _VideoBase64: Base64 value of videos used for face comparison. 
The size of videos data encoded by Base64 shall not exceed 8M, only mp4,avi,flv are supported. 
Please use standard Base64 encoding (use = for padding). Refer to RFC4648 for encoding specifications. 
Example values: "/9j/4AAQSk... (total length:61944)KiiK//2Q=="
        :type VideoBase64: str
        :param _LivenessType: The liveness detection type. Valid values: `LIP`, `ACTION`, and `SILENT`.
`LIP`: Numeric mode; `ACTION`: Motion mode; `SILENT`: silent mode. Select one of them.
Example value: "SILENT"
        :type LivenessType: str
        :param _ValidateData: When the "LivenessType" parameter is "ACTION", it must be specified.
It is used to control the action sequence. Action types: 
1 (open mouth)
2 (blink)
3 (nod)
4 (shake head). 
Select one or two from the four actions.
Example of passing single action parameter: "1".
Example of passing multiple action parameters: "4,2".
When the "LivenessType" parameter value is "SILENT", it shall be unspecified.
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
        :param _Sim: This value is valid when the "Result" parameter is "Success" or "FailedOperation.CompareLowSimilarity." 
This value indicates the similarity of face comparison. Value range: [0.00, 100.00]. The false pass rate for threshold 70 is 1 in 1,000, and the false pass rate for threshold 80 is 1 in 10,000. 
Example value: 80.00
        :type Sim: float
        :param _BestFrameBase64: The optimal screenshot of the video after verification is the value encoded by BASE64, jpg format. 
Note: This field may return "null", indicating that no valid value can be obtained. 
Example values: "/9j/4AAQSk... (total length:142036)s97n//2Q=="
        :type BestFrameBase64: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DetectAIFakeFacesRequest(AbstractModel):
    """DetectAIFakeFaces request structure.

    """

    def __init__(self):
        r"""
        :param _FaceInput: Enter the image or video with a face to be detected, in base64 encoding. Base64 value of the image: The overall image resolution is recommended to be 480x640, and the face size is 100X100 or larger; The image data size after Base64 encoding does not exceed 3M, and only supports jpg and png formats. Please use standard Base64 encoding (use = for padding). Refer to RFC4648 for encoding specifications. Base64 value of the video: The size after Base64 encoding does not exceed 8M, and supports mp4, avi, and flv formats. Please use standard Base64 encoding (use = for padding). Refer to RFC4648 for encoding specifications. The maximum supported video length is 20s, and the recommended length is 2 to 5s. The recommended video resolution is 480x640, and the frame rate is between 25fps and 30fps.
        :type FaceInput: str
        :param _FaceInputType: The type of input is 1- The input type is a picture 2- The input type is a video Others - Return error code InvalidParameter
        :type FaceInputType: int
        :param _Encryption: Whether the request information needs to be fully encrypted; Supported encryption algorithms: AES-256-CBC, SM4-GCM; Users with encryption requirements can use this parameter, for details, please click the link on the left.
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _EncryptedBody: Encrypted ciphertext; The data format before encryption is as follows:{"FaceInput":"AAAAA","FaceInputType":1}
        :type EncryptedBody: str
        """
        self._FaceInput = None
        self._FaceInputType = None
        self._Encryption = None
        self._EncryptedBody = None

    @property
    def FaceInput(self):
        return self._FaceInput

    @FaceInput.setter
    def FaceInput(self, FaceInput):
        self._FaceInput = FaceInput

    @property
    def FaceInputType(self):
        return self._FaceInputType

    @FaceInputType.setter
    def FaceInputType(self, FaceInputType):
        self._FaceInputType = FaceInputType

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def EncryptedBody(self):
        return self._EncryptedBody

    @EncryptedBody.setter
    def EncryptedBody(self, EncryptedBody):
        self._EncryptedBody = EncryptedBody


    def _deserialize(self, params):
        self._FaceInput = params.get("FaceInput")
        self._FaceInputType = params.get("FaceInputType")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        self._EncryptedBody = params.get("EncryptedBody")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectAIFakeFacesResponse(AbstractModel):
    """DetectAIFakeFaces response structure.

    """

    def __init__(self):
        r"""
        :param _AttackRiskLevel: Whether the detected image is an attack: Low: No attack risk Mid: Moderately suspected attack High: Highly suspected attack
        :type AttackRiskLevel: str
        :param _AttackRiskDetailList: A list of suspected attack traces detected. Note: When no attack traces are detected, an empty array is returned. This parameter is only used as a reference for result judgment. In actual applications, it is still recommended to use the result of AttackRiskLevel.
        :type AttackRiskDetailList: list of AttackRiskDetail
        :param _ExtraInfo: Additional Information
        :type ExtraInfo: :class:`tencentcloud.faceid.v20180301.models.ExtraInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttackRiskLevel = None
        self._AttackRiskDetailList = None
        self._ExtraInfo = None
        self._RequestId = None

    @property
    def AttackRiskLevel(self):
        return self._AttackRiskLevel

    @AttackRiskLevel.setter
    def AttackRiskLevel(self, AttackRiskLevel):
        self._AttackRiskLevel = AttackRiskLevel

    @property
    def AttackRiskDetailList(self):
        return self._AttackRiskDetailList

    @AttackRiskDetailList.setter
    def AttackRiskDetailList(self, AttackRiskDetailList):
        self._AttackRiskDetailList = AttackRiskDetailList

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AttackRiskLevel = params.get("AttackRiskLevel")
        if params.get("AttackRiskDetailList") is not None:
            self._AttackRiskDetailList = []
            for item in params.get("AttackRiskDetailList"):
                obj = AttackRiskDetail()
                obj._deserialize(item)
                self._AttackRiskDetailList.append(obj)
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class EditDetail(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _FieldName: Modified Field Name
        :type FieldName: str
        :param _OriginalFieldValue: Value of the field before modification, the original OCR result
        :type OriginalFieldValue: str
        :param _RevisedFieldValue: Value of the field after modification,the user's manually entered result
        :type RevisedFieldValue: str
        """
        self._FieldName = None
        self._OriginalFieldValue = None
        self._RevisedFieldValue = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def OriginalFieldValue(self):
        return self._OriginalFieldValue

    @OriginalFieldValue.setter
    def OriginalFieldValue(self, OriginalFieldValue):
        self._OriginalFieldValue = OriginalFieldValue

    @property
    def RevisedFieldValue(self):
        return self._RevisedFieldValue

    @RevisedFieldValue.setter
    def RevisedFieldValue(self, RevisedFieldValue):
        self._RevisedFieldValue = RevisedFieldValue


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._OriginalFieldValue = params.get("OriginalFieldValue")
        self._RevisedFieldValue = params.get("RevisedFieldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Encryption(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _EncryptList: 
        :type EncryptList: list of str
        :param _CiphertextBlob: 
        :type CiphertextBlob: str
        :param _Iv: 
        :type Iv: str
        :param _Algorithm: 
        :type Algorithm: str
        :param _TagList: 
        :type TagList: list of str
        """
        self._EncryptList = None
        self._CiphertextBlob = None
        self._Iv = None
        self._Algorithm = None
        self._TagList = None

    @property
    def EncryptList(self):
        return self._EncryptList

    @EncryptList.setter
    def EncryptList(self, EncryptList):
        self._EncryptList = EncryptList

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def Iv(self):
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._EncryptList = params.get("EncryptList")
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._Iv = params.get("Iv")
        self._Algorithm = params.get("Algorithm")
        self._TagList = params.get("TagList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _RetrievalLivenessExtraInfo: 
        :type RetrievalLivenessExtraInfo: list of RetrievalLivenessExtraInfo
        """
        self._RetrievalLivenessExtraInfo = None

    @property
    def RetrievalLivenessExtraInfo(self):
        return self._RetrievalLivenessExtraInfo

    @RetrievalLivenessExtraInfo.setter
    def RetrievalLivenessExtraInfo(self, RetrievalLivenessExtraInfo):
        self._RetrievalLivenessExtraInfo = RetrievalLivenessExtraInfo


    def _deserialize(self, params):
        if params.get("RetrievalLivenessExtraInfo") is not None:
            self._RetrievalLivenessExtraInfo = []
            for item in params.get("RetrievalLivenessExtraInfo"):
                obj = RetrievalLivenessExtraInfo()
                obj._deserialize(item)
                self._RetrievalLivenessExtraInfo.append(obj)
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class GetCardVerificationResultRequest(AbstractModel):
    """GetCardVerificationResult request structure.

    """

    def __init__(self):
        r"""
        :param _CardVerificationToken: The token used to identify an verification process. It can be used to get the verification result after the process is completed.
        :type CardVerificationToken: str
        """
        self._CardVerificationToken = None

    @property
    def CardVerificationToken(self):
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
        


class GetCardVerificationResultResponse(AbstractModel):
    """GetCardVerificationResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Pass status. When Warning and Rejected are returned, please check the specific reasons in the WarnInfo structure return. Example values are as follows:
PASSED
WARNING
REJECTED
PROCESSING
        :type Status: str
        :param _WarnInfo: Warning information returned by document verification.
        :type WarnInfo: list of str
        :param _Nationality: Nationality code. Complies with standard ISO 3166-1 alpha-3. 

Example value: IDN
        :type Nationality: str
        :param _CardType: Card Type. The supported options are:
ID_CARD
PASSPORT
DRIVING_LICENSE
AUTO

Example value: ID_CARD
        :type CardType: str
        :param _CardSubType: Subtype of the ID document.

        :type CardSubType: str
        :param _CardInfo: Recognition results of the ID document.
        :type CardInfo: :class:`tencentcloud.faceid.v20180301.models.CardInfo`
        :param _IDVerificationToken: The token used to identify an verification process. It can be used to get the verification result after the process is completed.
        :type IDVerificationToken: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._WarnInfo = None
        self._Nationality = None
        self._CardType = None
        self._CardSubType = None
        self._CardInfo = None
        self._IDVerificationToken = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WarnInfo(self):
        return self._WarnInfo

    @WarnInfo.setter
    def WarnInfo(self, WarnInfo):
        self._WarnInfo = WarnInfo

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def CardSubType(self):
        return self._CardSubType

    @CardSubType.setter
    def CardSubType(self, CardSubType):
        self._CardSubType = CardSubType

    @property
    def CardInfo(self):
        return self._CardInfo

    @CardInfo.setter
    def CardInfo(self, CardInfo):
        self._CardInfo = CardInfo

    @property
    def IDVerificationToken(self):
        return self._IDVerificationToken

    @IDVerificationToken.setter
    def IDVerificationToken(self, IDVerificationToken):
        self._IDVerificationToken = IDVerificationToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._WarnInfo = params.get("WarnInfo")
        self._Nationality = params.get("Nationality")
        self._CardType = params.get("CardType")
        self._CardSubType = params.get("CardSubType")
        if params.get("CardInfo") is not None:
            self._CardInfo = CardInfo()
            self._CardInfo._deserialize(params.get("CardInfo"))
        self._IDVerificationToken = params.get("IDVerificationToken")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :param _ActionList: This interface is used to control th action sequences.
Action types are as follows:
"blink"
"mouth"
"nod"
"shake"
You can choose 1-2 actions out of the four.
Single action example: "blink"
Multiple action example: "blink,mouth"
The default value is blink. The different action types passed in this parameter take effect only when the SecurityLevel is 2 or 4; otherwise, the interface reports an error.
        :type ActionList: str
        """
        self._CheckMode = None
        self._SecureLevel = None
        self._Image = None
        self._Extra = None
        self._ActionList = None

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

    @property
    def ActionList(self):
        return self._ActionList

    @ActionList.setter
    def ActionList(self, ActionList):
        self._ActionList = ActionList


    def _deserialize(self, params):
        self._CheckMode = params.get("CheckMode")
        self._SecureLevel = params.get("SecureLevel")
        self._Image = params.get("Image")
        self._Extra = params.get("Extra")
        self._ActionList = params.get("ActionList")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param _ErrorMsg: The description of the final verification result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _VerificationDetailList: The detailed verification result list of this process. Retries are allowed, so a verification process may have several entries of results.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VerificationDetailList: list of VerificationDetail
        :param _VideoBase64: The Base64-encoded string of the video collected from the video stream. Retries are allowed, and this field returns only the data collected in the last verification. If no video is collected, null is returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoBase64: str
        :param _BestFrameBase64: The Base64-encoded string of the best face screenshot collected from the video stream. Retries are allowed, and this field returns only the data collected in the last verification. If no best face screenshot is collected, null is returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BestFrameBase64: str
        :param _OCRResult: Card recognize result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OCRResult: list of OCRResult
        :param _Extra: The passthrough parameter of the business, max 1,000 characters, which will be returned in GetWebVerificationResultIntl.
        :type Extra: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._VerificationDetailList = None
        self._VideoBase64 = None
        self._BestFrameBase64 = None
        self._OCRResult = None
        self._Extra = None
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
    def OCRResult(self):
        return self._OCRResult

    @OCRResult.setter
    def OCRResult(self, OCRResult):
        self._OCRResult = OCRResult

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
        if params.get("OCRResult") is not None:
            self._OCRResult = []
            for item in params.get("OCRResult"):
                obj = OCRResult()
                obj._deserialize(item)
                self._OCRResult.append(obj)
        self._Extra = params.get("Extra")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        


class HMTPermit(AbstractModel):
    """Exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _EnglishName: English name
        :type EnglishName: str
        :param _Number: License number
        :type Number: str
        :param _Sex: Gender
        :type Sex: str
        :param _ValidDate: Valid date
        :type ValidDate: str
        :param _IssueAuthority: Issued authority
        :type IssueAuthority: str
        :param _IssueAddress: Issued address
        :type IssueAddress: str
        :param _Birthday: Birthday
        :type Birthday: str
        """
        self._Name = None
        self._EnglishName = None
        self._Number = None
        self._Sex = None
        self._ValidDate = None
        self._IssueAuthority = None
        self._IssueAddress = None
        self._Birthday = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def IssueAuthority(self):
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def IssueAddress(self):
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        self._Number = params.get("Number")
        self._Sex = params.get("Sex")
        self._ValidDate = params.get("ValidDate")
        self._IssueAuthority = params.get("IssueAuthority")
        self._IssueAddress = params.get("IssueAddress")
        self._Birthday = params.get("Birthday")
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
        


class JapanIDCard(AbstractModel):
    """Japan ID card.

    """

    def __init__(self):
        r"""
        :param _FullName: Full name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Age: Age
Note: This field may return null, indicating that no valid values can be obtained.
        :type Age: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _ExpirationDate: Expire date
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _FormattedAddress: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        """
        self._FullName = None
        self._LicenseNumber = None
        self._Age = None
        self._Birthday = None
        self._ExpirationDate = None
        self._FormattedAddress = None

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
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Age = params.get("Age")
        self._Birthday = params.get("Birthday")
        self._ExpirationDate = params.get("ExpirationDate")
        self._FormattedAddress = params.get("FormattedAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    """Macao ID Card

    """

    def __init__(self):
        r"""
        :param _FirstName: First name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstName: str
        :param _LastName: Last name
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastName: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _ExpirationDate: Expiration date
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpirationDate: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Sex: Sex
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Age: Age
Note: This field may return null, indicating that no valid values can be obtained.
        :type Age: str
        :param _IssuedCountry: Issued country
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountry: str
        :param _Field1: MRZ1 on card
Note: This field may return null, indicating that no valid values can be obtained. 
        :type Field1: str
        :param _Field2: MRZ2 on card
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class MainlandIDCard(AbstractModel):
    """Mainland ID Card OCR

    """

    def __init__(self):
        r"""
        :param _FullName: Chinese name
Note: This field may return null, indicating that no valid values can be obtained.

        :type FullName: str
        :param _Sex: Sex
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _Nation: Nation
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nation: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Address: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.

        :type LicenseNumber: str
        :param _FormattedAddress: Address
Note: This field may return null, indicating that no valid values can be obtained.
        :type FormattedAddress: str
        """
        self._FullName = None
        self._Sex = None
        self._Nation = None
        self._Birthday = None
        self._Address = None
        self._LicenseNumber = None
        self._FormattedAddress = None

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Address(self):
        warnings.warn("parameter `Address` is deprecated", DeprecationWarning) 

        return self._Address

    @Address.setter
    def Address(self, Address):
        warnings.warn("parameter `Address` is deprecated", DeprecationWarning) 

        self._Address = Address

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FormattedAddress(self):
        return self._FormattedAddress

    @FormattedAddress.setter
    def FormattedAddress(self, FormattedAddress):
        self._FormattedAddress = FormattedAddress


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._Sex = params.get("Sex")
        self._Nation = params.get("Nation")
        self._Birthday = params.get("Birthday")
        self._Address = params.get("Address")
        self._LicenseNumber = params.get("LicenseNumber")
        self._FormattedAddress = params.get("FormattedAddress")
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
        :param _MainlandIDCard: Mainland ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type MainlandIDCard: :class:`tencentcloud.faceid.v20180301.models.MainlandIDCard`
        :param _JapanIDCard: Japan ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type JapanIDCard: :class:`tencentcloud.faceid.v20180301.models.JapanIDCard`
        :param _TaiWanIDCard: Taiwan ID Card
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaiWanIDCard: :class:`tencentcloud.faceid.v20180301.models.TaiWanIDCard`
        :param _HMTPermitCard: exit/entry permit (card) for traveling to and from Hong Kong, Macao, or Taiwan.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HMTPermitCard: :class:`tencentcloud.faceid.v20180301.models.HMTPermit`
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
        self._MainlandIDCard = None
        self._JapanIDCard = None
        self._TaiWanIDCard = None
        self._HMTPermitCard = None

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

    @property
    def MainlandIDCard(self):
        return self._MainlandIDCard

    @MainlandIDCard.setter
    def MainlandIDCard(self, MainlandIDCard):
        self._MainlandIDCard = MainlandIDCard

    @property
    def JapanIDCard(self):
        return self._JapanIDCard

    @JapanIDCard.setter
    def JapanIDCard(self, JapanIDCard):
        self._JapanIDCard = JapanIDCard

    @property
    def TaiWanIDCard(self):
        return self._TaiWanIDCard

    @TaiWanIDCard.setter
    def TaiWanIDCard(self, TaiWanIDCard):
        self._TaiWanIDCard = TaiWanIDCard

    @property
    def HMTPermitCard(self):
        return self._HMTPermitCard

    @HMTPermitCard.setter
    def HMTPermitCard(self, HMTPermitCard):
        self._HMTPermitCard = HMTPermitCard


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
        if params.get("MainlandIDCard") is not None:
            self._MainlandIDCard = MainlandIDCard()
            self._MainlandIDCard._deserialize(params.get("MainlandIDCard"))
        if params.get("JapanIDCard") is not None:
            self._JapanIDCard = JapanIDCard()
            self._JapanIDCard._deserialize(params.get("JapanIDCard"))
        if params.get("TaiWanIDCard") is not None:
            self._TaiWanIDCard = TaiWanIDCard()
            self._TaiWanIDCard._deserialize(params.get("TaiWanIDCard"))
        if params.get("HMTPermitCard") is not None:
            self._HMTPermitCard = HMTPermit()
            self._HMTPermitCard._deserialize(params.get("HMTPermitCard"))
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
        


class OCRResult(AbstractModel):
    """The content of a single license in the license information.

    """

    def __init__(self):
        r"""
        :param _IsPass: Is the indentity verification or OCR process passed
        :type IsPass: bool
        :param _CardImageBase64: The Base64 of ID card image
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardImageBase64: str
        :param _CardInfo: OCR result of the ID card.
        :type CardInfo: :class:`tencentcloud.faceid.v20180301.models.CardInfo`
        :param _NormalCardInfo: OCR result of the ID card.
        :type NormalCardInfo: :class:`tencentcloud.faceid.v20180301.models.NormalCardInfo`
        :param _RequestId: The request id
        :type RequestId: str
        :param _CardCutImageBase64: Base64 of cropped image of ID card
        :type CardCutImageBase64: str
        :param _CardBackCutImageBase64: Base64 of the cropped image on the reverse side of the ID card
        :type CardBackCutImageBase64: str
        :param _WarnCardInfos: Card Warning Information

-9101 Alarm for covered certificate,
-9102 Alarm for photocopied certificate,
-9103 Alarm for photographed certificate,
-9104 Alarm for PS certificate,
-9107 Alarm for reflective certificate,
-9108 Alarm for blurry image,
-9109 This capability is not enabled.
        :type WarnCardInfos: list of int
        """
        self._IsPass = None
        self._CardImageBase64 = None
        self._CardInfo = None
        self._NormalCardInfo = None
        self._RequestId = None
        self._CardCutImageBase64 = None
        self._CardBackCutImageBase64 = None
        self._WarnCardInfos = None

    @property
    def IsPass(self):
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

    @property
    def CardImageBase64(self):
        return self._CardImageBase64

    @CardImageBase64.setter
    def CardImageBase64(self, CardImageBase64):
        self._CardImageBase64 = CardImageBase64

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def CardCutImageBase64(self):
        return self._CardCutImageBase64

    @CardCutImageBase64.setter
    def CardCutImageBase64(self, CardCutImageBase64):
        self._CardCutImageBase64 = CardCutImageBase64

    @property
    def CardBackCutImageBase64(self):
        return self._CardBackCutImageBase64

    @CardBackCutImageBase64.setter
    def CardBackCutImageBase64(self, CardBackCutImageBase64):
        self._CardBackCutImageBase64 = CardBackCutImageBase64

    @property
    def WarnCardInfos(self):
        return self._WarnCardInfos

    @WarnCardInfos.setter
    def WarnCardInfos(self, WarnCardInfos):
        self._WarnCardInfos = WarnCardInfos


    def _deserialize(self, params):
        self._IsPass = params.get("IsPass")
        self._CardImageBase64 = params.get("CardImageBase64")
        if params.get("CardInfo") is not None:
            self._CardInfo = CardInfo()
            self._CardInfo._deserialize(params.get("CardInfo"))
        if params.get("NormalCardInfo") is not None:
            self._NormalCardInfo = NormalCardInfo()
            self._NormalCardInfo._deserialize(params.get("NormalCardInfo"))
        self._RequestId = params.get("RequestId")
        self._CardCutImageBase64 = params.get("CardCutImageBase64")
        self._CardBackCutImageBase64 = params.get("CardBackCutImageBase64")
        self._WarnCardInfos = params.get("WarnCardInfos")
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
        


class RetrievalLivenessExtraInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _HitGroup: 
        :type HitGroup: str
        :param _SimilarityScore: 
        :type SimilarityScore: float
        :param _HitTemplate: 
        :type HitTemplate: str
        """
        self._HitGroup = None
        self._SimilarityScore = None
        self._HitTemplate = None

    @property
    def HitGroup(self):
        return self._HitGroup

    @HitGroup.setter
    def HitGroup(self, HitGroup):
        self._HitGroup = HitGroup

    @property
    def SimilarityScore(self):
        return self._SimilarityScore

    @SimilarityScore.setter
    def SimilarityScore(self, SimilarityScore):
        self._SimilarityScore = SimilarityScore

    @property
    def HitTemplate(self):
        return self._HitTemplate

    @HitTemplate.setter
    def HitTemplate(self, HitTemplate):
        self._HitTemplate = HitTemplate


    def _deserialize(self, params):
        self._HitGroup = params.get("HitGroup")
        self._SimilarityScore = params.get("SimilarityScore")
        self._HitTemplate = params.get("HitTemplate")
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
        :param _ChineseName: Chinese name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChineseName: str
        :param _EnName: English name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnName: str
        :param _FullName: English name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _ID: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _CountryOfBirth: Country of birth
Note: This field may return null, indicating that no valid values can be obtained.
        :type CountryOfBirth: str
        :param _Nationality: Nationality
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nationality: str
        :param _Birthday: Birthday
Note: This field may return null, indicating that no valid values can be obtained.
        :type Birthday: str
        :param _Address: Address (on the back)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Race: Race (on the back)
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
        self._ChineseName = None
        self._EnName = None
        self._FullName = None
        self._ID = None
        self._LicenseNumber = None
        self._Sex = None
        self._CountryOfBirth = None
        self._Nationality = None
        self._Birthday = None
        self._Address = None
        self._Race = None
        self._NRICCode = None
        self._PostCode = None
        self._DateOfExpiration = None
        self._DateOfIssue = None

    @property
    def ChName(self):
        warnings.warn("parameter `ChName` is deprecated", DeprecationWarning) 

        return self._ChName

    @ChName.setter
    def ChName(self, ChName):
        warnings.warn("parameter `ChName` is deprecated", DeprecationWarning) 

        self._ChName = ChName

    @property
    def ChineseName(self):
        return self._ChineseName

    @ChineseName.setter
    def ChineseName(self, ChineseName):
        self._ChineseName = ChineseName

    @property
    def EnName(self):
        warnings.warn("parameter `EnName` is deprecated", DeprecationWarning) 

        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        warnings.warn("parameter `EnName` is deprecated", DeprecationWarning) 

        self._EnName = EnName

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def ID(self):
        warnings.warn("parameter `ID` is deprecated", DeprecationWarning) 

        return self._ID

    @ID.setter
    def ID(self, ID):
        warnings.warn("parameter `ID` is deprecated", DeprecationWarning) 

        self._ID = ID

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
    def CountryOfBirth(self):
        warnings.warn("parameter `CountryOfBirth` is deprecated", DeprecationWarning) 

        return self._CountryOfBirth

    @CountryOfBirth.setter
    def CountryOfBirth(self, CountryOfBirth):
        warnings.warn("parameter `CountryOfBirth` is deprecated", DeprecationWarning) 

        self._CountryOfBirth = CountryOfBirth

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

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
        self._ChineseName = params.get("ChineseName")
        self._EnName = params.get("EnName")
        self._FullName = params.get("FullName")
        self._ID = params.get("ID")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Sex = params.get("Sex")
        self._CountryOfBirth = params.get("CountryOfBirth")
        self._Nationality = params.get("Nationality")
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
        


class TaiWanIDCard(AbstractModel):
    """Taiwan ID card.

    """

    def __init__(self):
        r"""
        :param _FullName: Full name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullName: str
        :param _LicenseNumber: License number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseNumber: str
        :param _Sex: Gender
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sex: str
        :param _IssuedCountry: Issued country
Note: This field may return null, indicating that no valid values can be obtained.
        :type IssuedCountry: str
        :param _RegistrationNumber: Registration number
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistrationNumber: str
        """
        self._FullName = None
        self._LicenseNumber = None
        self._Sex = None
        self._IssuedCountry = None
        self._RegistrationNumber = None

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
    def IssuedCountry(self):
        return self._IssuedCountry

    @IssuedCountry.setter
    def IssuedCountry(self, IssuedCountry):
        self._IssuedCountry = IssuedCountry

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Sex = params.get("Sex")
        self._IssuedCountry = params.get("IssuedCountry")
        self._RegistrationNumber = params.get("RegistrationNumber")
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
        


class VerificationDetail(AbstractModel):
    """The details of the verification process.

    """

    def __init__(self):
        r"""
        :param _ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param _ErrorMsg: The description of the final verification result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _LivenessErrorCode: The result of this liveness detection process. `0` indicates success.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorCode: int
        :param _LivenessErrorMsg: The result description of this liveness detection process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorMsg: str
        :param _CompareErrorCode: The result of this comparison process. `0` indicates that the person in the best face screenshot collected from the video stream is the same as that in the uploaded image for comparison.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorCode: int
        :param _CompareErrorMsg: The result description of this comparison process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorMsg: str
        :param _ReqTimestamp: The timestamp (ms) of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReqTimestamp: int
        :param _Similarity: The similarity of the best face screenshot collected from the video stream and the uploaded image for comparison in this verification process. Value range: [0.00, 100.00]. By default, the person in the screenshot is determined to be the same person in the image if the similarity is greater than or equal to 70.
Note: This field may return null, indicating that no valid values can be obtained.
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        :param _AutoSkipStartPage: When starting verification, whether to skip the starting verification page. If true, enter the verification process directly. The default is false. This configuration will not take effect if the downgrade policy is triggered.
        :type AutoSkipStartPage: bool
        :param _AutoSkip: When the verification passed, whether to skip the result page and automatically jump to RedirectURL. The default value is false.
Example value: false
        :type AutoSkip: bool
        :param _CheckMode: Detection mode, parameter values are as follows:
1: OCR+living detection & face comparison;
2: Living detection & face comparison;
3: Living detection;
The default value is 2.
Example value: 3
        :type CheckMode: int
        :param _IDCardType: The type of lisence used for verification. The following types are supported.
1.HKIDCard: Hong Kong (China) ID card
2.MLIDCard: Malaysia ID card
3.IndonesiaIDCard: Indonesia ID card
4.PhilippinesVoteID: Philippines VoteID card
5.PhilippinesDrivingLicense: Philippines driving license
6.PhilippinesTinID: Philippines TinID card
7.PhilippinesSSSID: Philippines SSSID card
8.PhilippinesUMID: Philippines UMID card
9.InternationalIDPassport: ID cards of Hong Kong, Macao and Taiwan (China), and international passport.
10.IndonesiaDrivingLicense:Indonesia driving license
11.ThailandIDCard: Thailand ID card
12.ThailandDrivingLicense: Thailand driving license
13.MLDrivingLicense: Malaysia driving license
14.SingaporeIDCard: Singapore ID card
15.SingaporeDrivingLicense: Singapore driving license
16.JapanIDCard: Japan ID card
17.JapanDrivingLicense: Japan driving license
18.PhilippinesIDCard: Philippines ID card
19.MainlandIDCard: Mainland ID card
20.MacaoIDCard: Macao ID card
Example: HKIDCard
        :type IDCardType: str
        :param _DisableCheckOcrWarnings: Whether to turn off document alarms, the default is false (the alarm detection function is turned on). When enabled, the identity authentication process will be intercepted based on the alarm status of the certificate. If you need to use the document authentication function, please contact us.
        :type DisableCheckOcrWarnings: bool
        :param _SecurityLevel: Liveness security level: 1:Silent mode;2:Action mode;3:Lighting mode;4:Action+Lighting mode;5:Action+Lighting(High security) mode; default value is 3
        :type SecurityLevel: int
        :param _SkipPrivacyPolicy: Whether to skip the agreement page, the default is false. When SkipPrivacyPolicy is false, the agreement page will be displayed and the privacy agreement needs to be checked; when SkipPrivacyPolicy is true, the agreement page will be skipped and the liveness process will be entered directly without checking the privacy agreement page.
        :type SkipPrivacyPolicy: bool
        :param _IdCardCutReturn: The default value is false. If it is false, the original ID image will be displayed. If it is true, the cut ID image will be displayed.
        :type IdCardCutReturn: bool
        :param _ThemeColor: Front-end theme color, in the format of RGB hexadecimal color code. The default value is "#2d72+1". If the format is incorrect, the default value color will be used.
        :type ThemeColor: str
        :param _Language: International language, the default value is en (English). Currently supported: th: Thai; en: English; zh-cn: Simplified Chinese; zh-tc: Tradionnal Chinese; id: Bahasa Indonesia.
        :type Language: str
        :param _AutoDowngrade: Automatic downgrade mode, with the following parameter values: 1: Downgrade to silent live mode; 2: Disable downgrade mode. The default value is 1.
        :type AutoDowngrade: int
        :param _ActionList: This interface is used to control th action sequences.
Action types are as follows:
"blink"
"mouth"
"nod"
"shake"
You can choose 1-2 actions out of the four.
Single action example: "blink"
Multiple action example: "blink,mouth"
The default value is blink. The different action types passed in this parameter take effect only when the SecurityLevel is 2, 4, or 5; otherwise, the interface reports an error.
        :type ActionList: str
        """
        self._AutoSkipStartPage = None
        self._AutoSkip = None
        self._CheckMode = None
        self._IDCardType = None
        self._DisableCheckOcrWarnings = None
        self._SecurityLevel = None
        self._SkipPrivacyPolicy = None
        self._IdCardCutReturn = None
        self._ThemeColor = None
        self._Language = None
        self._AutoDowngrade = None
        self._ActionList = None

    @property
    def AutoSkipStartPage(self):
        return self._AutoSkipStartPage

    @AutoSkipStartPage.setter
    def AutoSkipStartPage(self, AutoSkipStartPage):
        self._AutoSkipStartPage = AutoSkipStartPage

    @property
    def AutoSkip(self):
        return self._AutoSkip

    @AutoSkip.setter
    def AutoSkip(self, AutoSkip):
        self._AutoSkip = AutoSkip

    @property
    def CheckMode(self):
        return self._CheckMode

    @CheckMode.setter
    def CheckMode(self, CheckMode):
        self._CheckMode = CheckMode

    @property
    def IDCardType(self):
        return self._IDCardType

    @IDCardType.setter
    def IDCardType(self, IDCardType):
        self._IDCardType = IDCardType

    @property
    def DisableCheckOcrWarnings(self):
        return self._DisableCheckOcrWarnings

    @DisableCheckOcrWarnings.setter
    def DisableCheckOcrWarnings(self, DisableCheckOcrWarnings):
        self._DisableCheckOcrWarnings = DisableCheckOcrWarnings

    @property
    def SecurityLevel(self):
        return self._SecurityLevel

    @SecurityLevel.setter
    def SecurityLevel(self, SecurityLevel):
        self._SecurityLevel = SecurityLevel

    @property
    def SkipPrivacyPolicy(self):
        return self._SkipPrivacyPolicy

    @SkipPrivacyPolicy.setter
    def SkipPrivacyPolicy(self, SkipPrivacyPolicy):
        self._SkipPrivacyPolicy = SkipPrivacyPolicy

    @property
    def IdCardCutReturn(self):
        return self._IdCardCutReturn

    @IdCardCutReturn.setter
    def IdCardCutReturn(self, IdCardCutReturn):
        self._IdCardCutReturn = IdCardCutReturn

    @property
    def ThemeColor(self):
        return self._ThemeColor

    @ThemeColor.setter
    def ThemeColor(self, ThemeColor):
        self._ThemeColor = ThemeColor

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AutoDowngrade(self):
        return self._AutoDowngrade

    @AutoDowngrade.setter
    def AutoDowngrade(self, AutoDowngrade):
        self._AutoDowngrade = AutoDowngrade

    @property
    def ActionList(self):
        return self._ActionList

    @ActionList.setter
    def ActionList(self, ActionList):
        self._ActionList = ActionList


    def _deserialize(self, params):
        self._AutoSkipStartPage = params.get("AutoSkipStartPage")
        self._AutoSkip = params.get("AutoSkip")
        self._CheckMode = params.get("CheckMode")
        self._IDCardType = params.get("IDCardType")
        self._DisableCheckOcrWarnings = params.get("DisableCheckOcrWarnings")
        self._SecurityLevel = params.get("SecurityLevel")
        self._SkipPrivacyPolicy = params.get("SkipPrivacyPolicy")
        self._IdCardCutReturn = params.get("IdCardCutReturn")
        self._ThemeColor = params.get("ThemeColor")
        self._Language = params.get("Language")
        self._AutoDowngrade = params.get("AutoDowngrade")
        self._ActionList = params.get("ActionList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        