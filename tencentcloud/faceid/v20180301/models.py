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
        :param SecureLevel: Enumerated value. Valid values: `1`, `2`, `3`, and `4`.
Their meanings are as follows:
1 - silent
2 - blinking
3 - light
4 - blinking + light (default)
        :type SecureLevel: str
        """
        self.SecureLevel = None


    def _deserialize(self, params):
        self.SecureLevel = params.get("SecureLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyLivenessTokenResponse(AbstractModel):
    """ApplyLivenessToken response structure.

    """

    def __init__(self):
        r"""
        :param SdkToken: The token used to identify an SDK-based verification process. It is valid for 10 minutes and can be used to get the verification result after the process is completed.
        :type SdkToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SdkToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkToken = params.get("SdkToken")
        self.RequestId = params.get("RequestId")


class ApplySdkVerificationTokenRequest(AbstractModel):
    """ApplySdkVerificationToken request structure.

    """

    def __init__(self):
        r"""
        :param NeedVerifyIdCard: Whether ID card authentication is required. If not, only document OCR will be performed. Currently, authentication is available only when the value of `IdCardType` is `HK`.
        :type NeedVerifyIdCard: bool
        :param IdCardType: Card type. Valid values: `HK` (Hong Kong ID cards) (default), `ML` (Malaysian ID cards), `PhilippinesVoteID` (Philippine voters ID cards), and `PhilippinesDrivingLicense` (Philippine driving licenses).
        :type IdCardType: str
        :param DisableChangeOcrResult: Disable the modification of the OCR result by the user. Default value: `false` (modification allowed).
        :type DisableChangeOcrResult: bool
        :param DisableCheckOcrWarnings: Disable the OCR warnings. Default value: `false` (not disable), where OCR warnings are enabled and the OCR result will not be returned based on the warnings. If the value of `NeedVerifyIdCard` is `true`, the value of this field will also be `true`.
        :type DisableCheckOcrWarnings: bool
        :param Extra: A passthrough field, which is returned together with the verification result and can contain up to 1,024 bits.
        :type Extra: str
        """
        self.NeedVerifyIdCard = None
        self.IdCardType = None
        self.DisableChangeOcrResult = None
        self.DisableCheckOcrWarnings = None
        self.Extra = None


    def _deserialize(self, params):
        self.NeedVerifyIdCard = params.get("NeedVerifyIdCard")
        self.IdCardType = params.get("IdCardType")
        self.DisableChangeOcrResult = params.get("DisableChangeOcrResult")
        self.DisableCheckOcrWarnings = params.get("DisableCheckOcrWarnings")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplySdkVerificationTokenResponse(AbstractModel):
    """ApplySdkVerificationToken response structure.

    """

    def __init__(self):
        r"""
        :param SdkToken: The token used to identify an SDK-based verification process. It is valid for 7,200s and can be used to get the verification result after the process is completed.
        :type SdkToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SdkToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkToken = params.get("SdkToken")
        self.RequestId = params.get("RequestId")


class ApplyWebVerificationTokenRequest(AbstractModel):
    """ApplyWebVerificationToken request structure.

    """

    def __init__(self):
        r"""
        :param RedirectUrl: The web redirect URL after the verification is completed.
        :type RedirectUrl: str
        :param CompareImageUrl: The COS URL of the image for face comparison, which can be obtained with one of the following methods:
1. Call the `CreateUploadUrl` API to generate a URL and call it again after the image is successfully uploaded.
2. Use an existing COS URL. For a private bucket, grant the download permission with a pre-signed URL. The corresponding COS bucket must be in the same region as the input parameter `Region`.
        :type CompareImageUrl: str
        :param CompareImageMd5: The MD5 hash values of the image for face comparison (CompareImageUrl).
        :type CompareImageMd5: str
        """
        self.RedirectUrl = None
        self.CompareImageUrl = None
        self.CompareImageMd5 = None


    def _deserialize(self, params):
        self.RedirectUrl = params.get("RedirectUrl")
        self.CompareImageUrl = params.get("CompareImageUrl")
        self.CompareImageMd5 = params.get("CompareImageMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWebVerificationTokenResponse(AbstractModel):
    """ApplyWebVerificationToken response structure.

    """

    def __init__(self):
        r"""
        :param VerificationUrl: The verification URL to be opened with a browser to start the verification process.
        :type VerificationUrl: str
        :param BizToken: The token used to identify a web-based verification process. It is valid for 7,200s and can be used to get the verification result after the process is completed.
        :type BizToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VerificationUrl = None
        self.BizToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VerificationUrl = params.get("VerificationUrl")
        self.BizToken = params.get("BizToken")
        self.RequestId = params.get("RequestId")


class CardVerifyResult(AbstractModel):
    """The result of a single authentication or OCR process during the identity verification.

    """

    def __init__(self):
        r"""
        :param IsPass: Whether the authentication or OCR process is successful.
        :type IsPass: bool
        :param CardVideo: The video for ID card authentication. This field is returned only if the video-based ID card authentication is enabled. The URL is valid for 10 minutes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardVideo: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param CardImage: The identity document image. The URL is valid for 10 minutes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardImage: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param CardInfoOcrJson: The OCR result (in JSON) of the identity document image. If authentication or OCR fails, this parameter is left empty. The URL is valid for 10 minutes.
When the value of `IdCardType` is `HK`:
- CnName string: Chinese name
- EnName string: English name
- TelexCode string: The code corresponding to the Chinese name
- Sex string: Gender. Valid values: `M` (male) and `F` (female).
- Birthday string: Date of birth.
- Permanent int: Whether it is a permanent residence identity card. Valid values: `0` (non-permanent), `1` (permanent), and `-1` (unknown).
- IdNum string: ID number.
- Symbol string: The ID symbol below the date of birth, such as "***AZ".
- FirstIssueDate string: The date of first issuance.
- CurrentIssueDate string: The date of latest issuance.

When the value of `IdCardType` is `ML`:
- Sex string: `LELAKI` (male) and `PEREMPUAN` (female).
- Birthday string: Date of birth.
- ID string: ID number.
- Name string: Name.
- Address string: Address.
- Type string: Identity document type.

When the value of `IdCardType` is `PhilippinesVoteID`:
- Birthday string: Date of birth.
- Address string: Address.
- LastName string: Family name.
- FirstName string: First name.
- VIN string: VIN number.
- CivilStatus string: Marital status.
- Citizenship string: Citizenship.
- PrecinctNo string: Region.

When the value of `IdCardType` is `PhilippinesDrivingLicense`:
- Sex string: Gender.
- Birthday string: Date of birth.
- Name string: Name.
- Address string: Address.
- LastName string: Family name.
- FirstName string: First name.
- MiddleName string: Middle name.
- Nationality string: Nationality.
- LicenseNo string: License number.
- ExpiresDate string: Validity period.
- AgencyCode string: Agency code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardInfoOcrJson: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param RequestId: The request ID of a single process.
        :type RequestId: str
        """
        self.IsPass = None
        self.CardVideo = None
        self.CardImage = None
        self.CardInfoOcrJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsPass = params.get("IsPass")
        if params.get("CardVideo") is not None:
            self.CardVideo = FileInfo()
            self.CardVideo._deserialize(params.get("CardVideo"))
        if params.get("CardImage") is not None:
            self.CardImage = FileInfo()
            self.CardImage._deserialize(params.get("CardImage"))
        if params.get("CardInfoOcrJson") is not None:
            self.CardInfoOcrJson = FileInfo()
            self.CardInfoOcrJson._deserialize(params.get("CardInfoOcrJson"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareResult(AbstractModel):
    """The description of a single comparison result.

    """

    def __init__(self):
        r"""
        :param ErrorCode: The final comparison result.
        :type ErrorCode: str
        :param ErrorMsg: The description of the final comparison result.
        :type ErrorMsg: str
        :param LiveData: 
        :type LiveData: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param LiveVideo: The video for this liveness detection process. The URL is valid for 10 minutes.
        :type LiveVideo: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param LiveErrorCode: The code of the liveness detection result.
        :type LiveErrorCode: str
        :param LiveErrorMsg: The description of the liveness detection result.
        :type LiveErrorMsg: str
        :param BestFrame: The best face screenshot in this liveness detection. The URL is valid for 10 minutes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param ProfileImage: The profile photo screenshot from the identity document. The URL is valid for 10 minutes.
        :type ProfileImage: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param CompareErrorCode: The code of the face comparison result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorCode: str
        :param CompareErrorMsg: The description of the face comparison result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorMsg: str
        :param Sim: Similarity
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sim: float
        :param IsNeedCharge: This field is disused.
        :type IsNeedCharge: bool
        :param CardInfoInputJson: The identity document photo info edited by the user in JSON. If the value of `DisableChangeOcrResult` is `true`, the editing feature is disabled and this field does not exist. The URL is valid for 10 minutes.
When the value of `IdCardType` is `HK`:
- CnName string: Chinese name
- EnName string: English name
- TelexCode string: The code corresponding to the Chinese name
- Sex string: Gender. Valid values: `M` (male) and `F` (female).
- Birthday string: Date of birth.
- Permanent int: Whether it is a permanent residence identity card. Valid values: `0` (non-permanent), `1` (permanent), and `-1` (unknown).
- IdNum string: ID number.
- Symbol string: The ID symbol below the date of birth, such as "***AZ".
- FirstIssueDate string: The date of first issuance.
- CurrentIssueDate string: The date of latest issuance.

When the value of `IdCardType` is `ML`:
- Sex string: `LELAKI` (male) and `PEREMPUAN` (female).
- Birthday string
- ID string
- Name string
- Address string
- Type string: Identity document type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CardInfoInputJson: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param RequestId: The request ID of this verification process.
        :type RequestId: str
        """
        self.ErrorCode = None
        self.ErrorMsg = None
        self.LiveData = None
        self.LiveVideo = None
        self.LiveErrorCode = None
        self.LiveErrorMsg = None
        self.BestFrame = None
        self.ProfileImage = None
        self.CompareErrorCode = None
        self.CompareErrorMsg = None
        self.Sim = None
        self.IsNeedCharge = None
        self.CardInfoInputJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        if params.get("LiveData") is not None:
            self.LiveData = FileInfo()
            self.LiveData._deserialize(params.get("LiveData"))
        if params.get("LiveVideo") is not None:
            self.LiveVideo = FileInfo()
            self.LiveVideo._deserialize(params.get("LiveVideo"))
        self.LiveErrorCode = params.get("LiveErrorCode")
        self.LiveErrorMsg = params.get("LiveErrorMsg")
        if params.get("BestFrame") is not None:
            self.BestFrame = FileInfo()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("ProfileImage") is not None:
            self.ProfileImage = FileInfo()
            self.ProfileImage._deserialize(params.get("ProfileImage"))
        self.CompareErrorCode = params.get("CompareErrorCode")
        self.CompareErrorMsg = params.get("CompareErrorMsg")
        self.Sim = params.get("Sim")
        self.IsNeedCharge = params.get("IsNeedCharge")
        if params.get("CardInfoInputJson") is not None:
            self.CardInfoInputJson = FileInfo()
            self.CardInfoInputJson._deserialize(params.get("CardInfoInputJson"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUploadUrlRequest(AbstractModel):
    """CreateUploadUrl request structure.

    """

    def __init__(self):
        r"""
        :param TargetAction: Target API
        :type TargetAction: str
        """
        self.TargetAction = None


    def _deserialize(self, params):
        self.TargetAction = params.get("TargetAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUploadUrlResponse(AbstractModel):
    """CreateUploadUrl response structure.

    """

    def __init__(self):
        r"""
        :param UploadUrl: The URL for uploading contents with the `HTTP PUT` method.
        :type UploadUrl: str
        :param ResourceUrl: The resource URL obtained after this upload is completed and to be passed in where it is required later.
        :type ResourceUrl: str
        :param ExpiredTimestamp: The point in time when the upload/download link expires, which is a 10-bit Unix timestamp.
        :type ExpiredTimestamp: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UploadUrl = None
        self.ResourceUrl = None
        self.ExpiredTimestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UploadUrl = params.get("UploadUrl")
        self.ResourceUrl = params.get("ResourceUrl")
        self.ExpiredTimestamp = params.get("ExpiredTimestamp")
        self.RequestId = params.get("RequestId")


class DetectReflectLivenessAndCompareRequest(AbstractModel):
    """DetectReflectLivenessAndCompare request structure.

    """

    def __init__(self):
        r"""
        :param LiveDataUrl: URL of the liveness detection data package generated by the SDK
        :type LiveDataUrl: str
        :param LiveDataMd5: MD5 hash value (32-bit) of the liveness detection data package generated by the SDK, which is used to verify the LiveData consistency.
        :type LiveDataMd5: str
        :param ImageUrl: URL of the target image for comparison
        :type ImageUrl: str
        :param ImageMd5: MD5 hash value (32-bit) of the target image for comparison, which is used to verify the `Image` consistency.
        :type ImageMd5: str
        """
        self.LiveDataUrl = None
        self.LiveDataMd5 = None
        self.ImageUrl = None
        self.ImageMd5 = None


    def _deserialize(self, params):
        self.LiveDataUrl = params.get("LiveDataUrl")
        self.LiveDataMd5 = params.get("LiveDataMd5")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageMd5 = params.get("ImageMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectReflectLivenessAndCompareResponse(AbstractModel):
    """DetectReflectLivenessAndCompare response structure.

    """

    def __init__(self):
        r"""
        :param BestFrameUrl: Temporary URL of the best screenshot (.jpg) of the video after successful verification. Both the screenshot and the URL are valid for two hours only, so you need to download the screenshot within this period.
        :type BestFrameUrl: str
        :param BestFrameMd5: MD5 hash value (32-bit) of the best screenshot of the video after successful verification, which is used to verify the `BestFrame` consistency.
        :type BestFrameMd5: str
        :param Result: Service error code. `Success` will be returned for success. For error information, see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param Description: Service result description
        :type Description: str
        :param Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BestFrameUrl = None
        self.BestFrameMd5 = None
        self.Result = None
        self.Description = None
        self.Sim = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameUrl = params.get("BestFrameUrl")
        self.BestFrameMd5 = params.get("BestFrameMd5")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Sim = params.get("Sim")
        self.RequestId = params.get("RequestId")


class FileInfo(AbstractModel):
    """The description of a file, including a download URL and the MD5 checksum and size of the file.

    """

    def __init__(self):
        r"""
        :param Url: The URL for downloading the file
        :type Url: str
        :param MD5: The 32-bit MD5 checksum of the file
        :type MD5: str
        :param Size: The file size
        :type Size: int
        """
        self.Url = None
        self.MD5 = None
        self.Size = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.MD5 = params.get("MD5")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateReflectSequenceRequest(AbstractModel):
    """GenerateReflectSequence request structure.

    """

    def __init__(self):
        r"""
        :param DeviceDataUrl: The resource URL of the data package generated by the SDK.
        :type DeviceDataUrl: str
        :param DeviceDataMd5: The MD5 hash value of the data package generated by the SDK.
        :type DeviceDataMd5: str
        :param SecurityLevel: 1 - silent
2 - blinking
3 - light
4 - blinking + light (default)
        :type SecurityLevel: str
        """
        self.DeviceDataUrl = None
        self.DeviceDataMd5 = None
        self.SecurityLevel = None


    def _deserialize(self, params):
        self.DeviceDataUrl = params.get("DeviceDataUrl")
        self.DeviceDataMd5 = params.get("DeviceDataMd5")
        self.SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateReflectSequenceResponse(AbstractModel):
    """GenerateReflectSequence response structure.

    """

    def __init__(self):
        r"""
        :param ReflectSequenceUrl: The resource URL of the light sequence, which needs to be downloaded and passed through to the SDK to start the identity verification process.
        :type ReflectSequenceUrl: str
        :param ReflectSequenceMd5: The MD5 hash value of the light sequence, which is used to check whether the light sequence is altered.
        :type ReflectSequenceMd5: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReflectSequenceUrl = None
        self.ReflectSequenceMd5 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReflectSequenceUrl = params.get("ReflectSequenceUrl")
        self.ReflectSequenceMd5 = params.get("ReflectSequenceMd5")
        self.RequestId = params.get("RequestId")


class GetLivenessResultRequest(AbstractModel):
    """GetLivenessResult request structure.

    """

    def __init__(self):
        r"""
        :param SdkToken: The token used to identify an SDK-based verification process.
        :type SdkToken: str
        """
        self.SdkToken = None


    def _deserialize(self, params):
        self.SdkToken = params.get("SdkToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLivenessResultResponse(AbstractModel):
    """GetLivenessResult response structure.

    """

    def __init__(self):
        r"""
        :param Result: The final verification result.
        :type Result: str
        :param Description: The description of the final verification result.
        :type Description: str
        :param BestFrame: The face screenshot.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param Video: The video for the detection.
        :type Video: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.BestFrame = None
        self.Video = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        if params.get("BestFrame") is not None:
            self.BestFrame = FileInfo()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("Video") is not None:
            self.Video = FileInfo()
            self.Video._deserialize(params.get("Video"))
        self.RequestId = params.get("RequestId")


class GetSdkVerificationResultRequest(AbstractModel):
    """GetSdkVerificationResult request structure.

    """

    def __init__(self):
        r"""
        :param SdkToken: The token used to identify an SDK-based verification process.
        :type SdkToken: str
        """
        self.SdkToken = None


    def _deserialize(self, params):
        self.SdkToken = params.get("SdkToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSdkVerificationResultResponse(AbstractModel):
    """GetSdkVerificationResult response structure.

    """

    def __init__(self):
        r"""
        :param Result: The result of the entire verification process.
        :type Result: str
        :param Description: The result description.
        :type Description: str
        :param ChargeCount: The charge count.
        :type ChargeCount: int
        :param CardVerifyResults: The results of multiple OCR processes (in order). The result of the final process is taken as the valid result.
        :type CardVerifyResults: list of CardVerifyResult
        :param CompareResults: The results of multiple liveness detection processes (in order). The result of the final process is taken as the valid result.
        :type CompareResults: list of CompareResult
        :param Extra: Info passed in the process of getting the token.
        :type Extra: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.ChargeCount = None
        self.CardVerifyResults = None
        self.CompareResults = None
        self.Extra = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.ChargeCount = params.get("ChargeCount")
        if params.get("CardVerifyResults") is not None:
            self.CardVerifyResults = []
            for item in params.get("CardVerifyResults"):
                obj = CardVerifyResult()
                obj._deserialize(item)
                self.CardVerifyResults.append(obj)
        if params.get("CompareResults") is not None:
            self.CompareResults = []
            for item in params.get("CompareResults"):
                obj = CompareResult()
                obj._deserialize(item)
                self.CompareResults.append(obj)
        self.Extra = params.get("Extra")
        self.RequestId = params.get("RequestId")


class GetWebVerificationResultRequest(AbstractModel):
    """GetWebVerificationResult request structure.

    """

    def __init__(self):
        r"""
        :param BizToken: The token for the web-based verification, which is generated with the `ApplyWebVerificationToken` API.
        :type BizToken: str
        """
        self.BizToken = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWebVerificationResultResponse(AbstractModel):
    """GetWebVerificationResult response structure.

    """

    def __init__(self):
        r"""
        :param ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param ErrorMsg: The description of the final verification result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param VideoBestFrameUrl: The temporary URL of the best face screenshot collected from the video stream. It is valid for 10 minutes. Download the image if needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoBestFrameUrl: str
        :param VideoBestFrameMd5: The MD5 hash value of the best face screenshot collected from the video stream. It can be used to check whether the image content is consistent with the file content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoBestFrameMd5: str
        :param VerificationDetailList: The details list of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VerificationDetailList: list of VerificationDetail
        :param VideoUrl: The temporary URL of the video collected from the video stream. It is valid for 10 minutes. Download the video if needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoUrl: str
        :param VideoMd5: The MD5 hash value of the video collected from the video stream. It can be used to check whether the video content is consistent with the file content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoMd5: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ErrorCode = None
        self.ErrorMsg = None
        self.VideoBestFrameUrl = None
        self.VideoBestFrameMd5 = None
        self.VerificationDetailList = None
        self.VideoUrl = None
        self.VideoMd5 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.VideoBestFrameUrl = params.get("VideoBestFrameUrl")
        self.VideoBestFrameMd5 = params.get("VideoBestFrameMd5")
        if params.get("VerificationDetailList") is not None:
            self.VerificationDetailList = []
            for item in params.get("VerificationDetailList"):
                obj = VerificationDetail()
                obj._deserialize(item)
                self.VerificationDetailList.append(obj)
        self.VideoUrl = params.get("VideoUrl")
        self.VideoMd5 = params.get("VideoMd5")
        self.RequestId = params.get("RequestId")


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare request structure.

    """

    def __init__(self):
        r"""
        :param LivenessType: Liveness detection type. Valid values: LIP/ACTION/SILENT.
LIP: numeric mode; ACTION: motion mode; SILENT: silent mode. You need to select a mode to input.
        :type LivenessType: str
        :param ImageBase64: Base64 string of the image for face comparison.
The size of the Base64-encoded image data can be up to 3 MB. JPG and PNG formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL of the image for face comparison. The size of the downloaded image after Base64 encoding can be up to 3 MB. JPG and PNG formats are supported.

Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageBase64` will be used.

We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ValidateData: Lip mode: set this parameter to a custom 4-digit verification code.
Action mode: set this parameter to a custom action sequence (e.g., `2,1` or `1,2`).
Silent mode: do not pass in this parameter.
        :type ValidateData: str
        :param Optional: Optional configuration (a JSON string)
{
"BestFrameNum": 2  // Return multiple best screenshots. Value range: 2−10
}
        :type Optional: str
        :param VideoBase64: Base64 string of the video for liveness detection.
The size of the Base64-encoded video data can be up to 8 MB. MP4, AVI, and FLV formats are supported.
Please use the standard Base64 encoding scheme (with the "=" padding). For the encoding conventions, please see RFC 4648.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.
        :type VideoBase64: str
        :param VideoUrl: URL of the video for liveness detection. The size of the downloaded video after Base64 encoding can be up to 8 MB. It takes no more than 4 seconds to download. MP4, AVI, and FLV formats are supported.

Either the `VideoUrl` or `VideoBase64` of the video must be provided. If both are provided, only `VideoBase64` will be used.

We recommend you store the video in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type VideoUrl: str
        """
        self.LivenessType = None
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ValidateData = None
        self.Optional = None
        self.VideoBase64 = None
        self.VideoUrl = None


    def _deserialize(self, params):
        self.LivenessType = params.get("LivenessType")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")
        self.VideoBase64 = params.get("VideoBase64")
        self.VideoUrl = params.get("VideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare response structure.

    """

    def __init__(self):
        r"""
        :param BestFrameBase64: The best screenshot of the video after successful verification. The photo is Base64-encoded and in JPG format.
        :type BestFrameBase64: str
        :param Sim: Similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two faces are of the same person. You can adjust the threshold according to your specific scenario (the FAR at the threshold of 70 is 0.1%, and FAR at the threshold of 80 is 0.01%).
        :type Sim: float
        :param Result: Service error code. `Success` will be returned for success. For error information, please see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param Description: Service result description.
        :type Description: str
        :param BestFrameList: 
        :type BestFrameList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class VerificationDetail(AbstractModel):
    """The details of the verification process.

    """

    def __init__(self):
        r"""
        :param ErrorCode: The final result of this verification. `0` indicates that the person is the same as that in the photo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorCode: int
        :param ErrorMsg: The description of the final verification result.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param LivenessErrorCode: The result of this liveness detection process. `0` indicates success.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorCode: int
        :param LivenessErrorMsg: The result description of this liveness detection process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LivenessErrorMsg: str
        :param CompareErrorCode: The result of this comparison process. `0` indicates that the person in the best face screenshot collected from the video stream is the same as that in the uploaded image for comparison.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorCode: int
        :param CompareErrorMsg: The result description of this comparison process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareErrorMsg: str
        :param ReqTimestamp: The timestamp (ms) of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReqTimestamp: int
        :param Similarity: The similarity of the best face screenshot collected from the video stream and the uploaded image for comparison in this verification process. Valid range: [0.00, 100.00]. By default, the person in the screenshot is judged as the same person in the image if the similarity is greater than or equal to 70.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Similarity: float
        :param Seq: Unique ID of this verification process.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Seq: str
        """
        self.ErrorCode = None
        self.ErrorMsg = None
        self.LivenessErrorCode = None
        self.LivenessErrorMsg = None
        self.CompareErrorCode = None
        self.CompareErrorMsg = None
        self.ReqTimestamp = None
        self.Similarity = None
        self.Seq = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.LivenessErrorCode = params.get("LivenessErrorCode")
        self.LivenessErrorMsg = params.get("LivenessErrorMsg")
        self.CompareErrorCode = params.get("CompareErrorCode")
        self.CompareErrorMsg = params.get("CompareErrorMsg")
        self.ReqTimestamp = params.get("ReqTimestamp")
        self.Similarity = params.get("Similarity")
        self.Seq = params.get("Seq")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoLivenessCompareRequest(AbstractModel):
    """VideoLivenessCompare request structure.

    """

    def __init__(self):
        r"""
        :param ImageUrl: The URL of the photo for face comparison. The downloaded image after Base64 encoding can be up to 3 MB and must be in JPG or PNG.

The image must be stored in a COS bucket in the region where the FaceID service resides to ensure a higher download speed and better stability. You can generate an image URL by using `CreateUploadUrl` or purchase the COS service.
        :type ImageUrl: str
        :param ImageMd5: The 32-bit MD5 checksum of the image for comparison
        :type ImageMd5: str
        :param VideoUrl: The URL of the video for liveness detection. The downloaded video after Base64 encoding can be up to 8 MB and must be in MP4, AVI, or FLV. It takes no more than 4s to download the video.

The video must be stored in a COS bucket in the region where the FaceID service resides to ensure a higher download speed and better stability. You can generate a video URL by using `CreateUploadUrl` or purchase the COS service.
        :type VideoUrl: str
        :param VideoMd5: The 32-bit MD5 checksum of the video
        :type VideoMd5: str
        :param LivenessType: The liveness detection type. Valid values: `LIP`, `ACTION`, and `SILENT`.
`LIP`: Numeric mode; `ACTION`: Motion mode; `SILENT`: silent mode. Select one of them.
        :type LivenessType: str
        :param ValidateData: LIP parameter: Pass in a custom 4-digit verification code.
ACTION parameter: Pass in a custom action sequence (`2,1` or `1,2`).
SILENT parameter: Null.
        :type ValidateData: str
        """
        self.ImageUrl = None
        self.ImageMd5 = None
        self.VideoUrl = None
        self.VideoMd5 = None
        self.LivenessType = None
        self.ValidateData = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageMd5 = params.get("ImageMd5")
        self.VideoUrl = params.get("VideoUrl")
        self.VideoMd5 = params.get("VideoMd5")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoLivenessCompareResponse(AbstractModel):
    """VideoLivenessCompare response structure.

    """

    def __init__(self):
        r"""
        :param Sim: The similarity. Value range: [0.00, 100.00]. As a recommendation, when the similarity is greater than or equal to 70, it can be determined that the two persons are of the same person. You can adjust the threshold according to your specific scenario (the FARs at the thresholds of 70 and 80 are 0.1% and 0.01%, respectively).
        :type Sim: float
        :param Result: The service error code. `Success` will be returned for success. For error information, see the `FailedOperation` section in the error code list below.
        :type Result: str
        :param Description: The service result description
        :type Description: str
        :param BestFrame: The best video screenshot after successful verification
Note: This field may return null, indicating that no valid values can be obtained.
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.FileInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrame = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        if params.get("BestFrame") is not None:
            self.BestFrame = FileInfo()
            self.BestFrame._deserialize(params.get("BestFrame"))
        self.RequestId = params.get("RequestId")