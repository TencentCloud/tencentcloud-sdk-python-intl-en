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


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param RetBorderCutImage: Whether to return the bank card image data after preprocessing (precise cropping and alignment). Default value: `false`
        :type RetBorderCutImage: bool
        :param RetCardNoImage: Whether to return the card number image data after slicing. Default value: `false`
        :type RetCardNoImage: bool
        :param EnableCopyCheck: Whether to enable photocopy check. If the input image is a bank card photocopy, an alarm will be returned. Default value: `false`
        :type EnableCopyCheck: bool
        :param EnableReshootCheck: Whether to enable photograph check. If the input image is a bank card photograph, an alarm will be returned. Default value: `false`
        :type EnableReshootCheck: bool
        :param EnableBorderCheck: Whether to enable obscured border check. If the input image is a bank card with obscured border, an alarm will be returned. Default value: `false`
        :type EnableBorderCheck: bool
        :param EnableQualityValue: Whether to return the image quality value, which measures how clear an image is. Default value: `false`
        :type EnableQualityValue: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetBorderCutImage = None
        self.RetCardNoImage = None
        self.EnableCopyCheck = None
        self.EnableReshootCheck = None
        self.EnableBorderCheck = None
        self.EnableQualityValue = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetBorderCutImage = params.get("RetBorderCutImage")
        self.RetCardNoImage = params.get("RetCardNoImage")
        self.EnableCopyCheck = params.get("EnableCopyCheck")
        self.EnableReshootCheck = params.get("EnableReshootCheck")
        self.EnableBorderCheck = params.get("EnableBorderCheck")
        self.EnableQualityValue = params.get("EnableQualityValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param CardNo: Card number
        :type CardNo: str
        :param BankInfo: Bank information
        :type BankInfo: str
        :param ValidDate: Expiration date. Format: 07/2023
        :type ValidDate: str
        :param CardType: Card type
        :type CardType: str
        :param CardName: Card name
        :type CardName: str
        :param BorderCutImage: Sliced image data
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BorderCutImage: str
        :param CardNoImage: Card number image data
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CardNoImage: str
        :param WarningCode: Warning code:
-9110: the bank card date is invalid. 
-9111: the bank card border is incomplete. 
-9112: the bank card image is reflective.
-9113: the bank card image is a photocopy.
-9114: the bank card image is a photograph.
Multiple warning codes may be returned at a time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WarningCode: list of int
        :param QualityValue: Image quality value, which is returned when `EnableQualityValue` is set to `true`. The smaller the value, the less clear the image is. Value range: 0−100 (a threshold greater than or equal to 50 is recommended.)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QualityValue: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CardNo = None
        self.BankInfo = None
        self.ValidDate = None
        self.CardType = None
        self.CardName = None
        self.BorderCutImage = None
        self.CardNoImage = None
        self.WarningCode = None
        self.QualityValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CardNo = params.get("CardNo")
        self.BankInfo = params.get("BankInfo")
        self.ValidDate = params.get("ValidDate")
        self.CardType = params.get("CardType")
        self.CardName = params.get("CardName")
        self.BorderCutImage = params.get("BorderCutImage")
        self.CardNoImage = params.get("CardNoImage")
        self.WarningCode = params.get("WarningCode")
        self.QualityValue = params.get("QualityValue")
        self.RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """Coordinates

    """

    def __init__(self):
        r"""
        :param X: Horizontal coordinate
        :type X: int
        :param Y: Vertical coordinate
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWordCoordPoint(AbstractModel):
    """Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner

    """

    def __init__(self):
        r"""
        :param WordCoordinate: Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner
        :type WordCoordinate: list of Coord
        """
        self.WordCoordinate = None


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self.WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self.WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWords(AbstractModel):
    """Information about a character detected, including the character itself and its confidence

    """

    def __init__(self):
        r"""
        :param Confidence: Confidence. Value range: 0–100
        :type Confidence: int
        :param Character: A possible character
        :type Character: str
        """
        self.Confidence = None
        self.Character = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of image.
The image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
Either `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
The image cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param IsWords: Whether to return the character information. Default value: `false`
        :type IsWords: bool
        :param EnableDetectSplit: Whether to slice the input image to enhance the recognition effects for scenarios where the whole image is big, but the size of a single character is small (e.g., test papers). This feature is disabled by default.
        :type EnableDetectSplit: bool
        :param IsPdf: Whether to enable PDF recognition. Default value: `false`. If you enable this feature, both images and PDF files can be recognized.
        :type IsPdf: bool
        :param PdfPageNumber: Number of a PDF page that needs to be recognized. Currently, only one single page can be recognized. This parameter takes effect only if a PDF file is uploaded and `IsPdf` is set to `true`. Default value: `1`
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsWords = None
        self.EnableDetectSplit = None
        self.IsPdf = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsWords = params.get("IsWords")
        self.EnableDetectSplit = params.get("EnableDetectSplit")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR response structure.

    """

    def __init__(self):
        r"""
        :param TextDetections: Information on recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :type TextDetections: list of TextDetection
        :param Angel: Image rotation angle in degrees. 0° indicates horizontal text. A positive value indicates clockwise rotation. A negative value indicates anticlockwise rotation. For more information, please see <a href="https://intl.cloud.tencent.com/document/product/866/45139?from_cn_redirect=1">How to Correct Tilted Text</a>.
        :type Angel: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of image/PDF.
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
        :type ImageBase64: str
        :param ImageUrl: URL address of image/PDF. (This field is not supported outside Chinese mainland)
The image/PDF cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param Scene: Reserved field.
        :type Scene: str
        :param LanguageType: Language to recognize
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
        :param IsPdf: Whether to enable PDF recognition. Default value: false. After this feature is enabled, both images and PDF files can be recognized at the same time.
        :type IsPdf: bool
        :param PdfPageNumber: Page number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of the `IsPdf` parameter is `true`. Default value: 1.
        :type PdfPageNumber: int
        :param IsWords: Whether to return the character information. Default value: `false`
        :type IsWords: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.LanguageType = None
        self.IsPdf = None
        self.PdfPageNumber = None
        self.IsWords = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.LanguageType = params.get("LanguageType")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.IsWords = params.get("IsWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR response structure.

    """

    def __init__(self):
        r"""
        :param TextDetections: Information of recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :type TextDetections: list of TextDetection
        :param Language: Detected language. For more information on the supported languages, please see the description of the `LanguageType` input parameter.
        :type Language: str
        :param Angel: Image rotation angle in degrees. 0° indicates horizontal text, a positive value indicates clockwise rotation, and a negative value indicates anticlockwise rotation. For more information, please see <a href="https://intl.cloud.tencent.com/document/product/866/45139?from_cn_redirect=1">How to Correct Tilted Text</a>.
        :type Angel: float
        :param PdfPageSize: Total number of PDF pages to be returned if the image is a PDF. Default value: 0.
        :type PdfPageSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.Angel = None
        self.PdfPageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.Angel = params.get("Angel")
        self.PdfPageSize = params.get("PdfPageSize")
        self.RequestId = params.get("RequestId")


class HKIDCardOCRRequest(AbstractModel):
    """HKIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param DetectFake: Whether to check for authenticity.
        :type DetectFake: bool
        :param ReturnHeadImage: Whether to return identity photo.
        :type ReturnHeadImage: bool
        :param ImageBase64: Base64 string of the image
Supported image formats: PNG, JPG, JPEG. GIF is not supported yet.
Supported image size: The downloaded image cannot exceed 7 MB after being Base64-encoded, and it cannot take longer than 3 seconds to download the image.
        :type ImageBase64: str
        :param ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 3 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self.DetectFake = None
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.DetectFake = params.get("DetectFake")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRResponse(AbstractModel):
    """HKIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param CnName: Name in Chinese
        :type CnName: str
        :param EnName: Name in English
        :type EnName: str
        :param TelexCode: Telecode for the name in Chinese
        :type TelexCode: str
        :param Sex: Gender. Valid values: Male, Female
        :type Sex: str
        :param Birthday: Date of birth
        :type Birthday: str
        :param Permanent: Permanent identity card.
0: non-permanent;
1: permanent;
-1: unknown.
        :type Permanent: int
        :param IdNum: Identity card number
        :type IdNum: str
        :param Symbol: Document symbol, i.e., the symbol under the date of birth, such as "***AZ"
        :type Symbol: str
        :param FirstIssueDate: First issue date
        :type FirstIssueDate: str
        :param CurrentIssueDate: Last receipt date
        :type CurrentIssueDate: str
        :param FakeDetectResult: Authenticity check.
0: unable to judge (because the image is blurred, incomplete, reflective, too dark, etc.);
1: forged;
2: authentic.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FakeDetectResult: int
        :param HeadImage: Base64-encoded identity photo
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeadImage: str
        :param WarningCode: Multiple alarm codes. If the ID card is spoofed, photocopied, or doctored, the corresponding alarm code will be returned.
-9102: alarm for photocopied document
-9103: alarm for spoofed document
-9104: alarm for doctored document
-9105: alarm for forged document
        :type WarningCode: list of int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CnName = None
        self.EnName = None
        self.TelexCode = None
        self.Sex = None
        self.Birthday = None
        self.Permanent = None
        self.IdNum = None
        self.Symbol = None
        self.FirstIssueDate = None
        self.CurrentIssueDate = None
        self.FakeDetectResult = None
        self.HeadImage = None
        self.WarningCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CnName = params.get("CnName")
        self.EnName = params.get("EnName")
        self.TelexCode = params.get("TelexCode")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.Permanent = params.get("Permanent")
        self.IdNum = params.get("IdNum")
        self.Symbol = params.get("Symbol")
        self.FirstIssueDate = params.get("FirstIssueDate")
        self.CurrentIssueDate = params.get("CurrentIssueDate")
        self.FakeDetectResult = params.get("FakeDetectResult")
        self.HeadImage = params.get("HeadImage")
        self.WarningCode = params.get("WarningCode")
        self.RequestId = params.get("RequestId")


class ItemCoord(AbstractModel):
    """Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.

    """

    def __init__(self):
        r"""
        :param X: X-coordinate of top-left point.
        :type X: int
        :param Y: Y-coordinate of top-left point.
        :type Y: int
        :param Width: Width
        :type Width: int
        :param Height: Height
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of an image.
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
        :type ImageBase64: str
        :param ImageUrl: URL of an image. (This field is not supported outside the Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param RetImage: Whether to return an image
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param ID: Identity card number
        :type ID: str
        :param Name: Name
        :type Name: str
        :param Address: Address
        :type Address: str
        :param Sex: Gender
        :type Sex: str
        :param Warn: Warning code
-9103 Warning for spoofed card
-9102 Warning for photocopied card
-9106 Warning for covered card
-9107 Warning for blurry image
        :type Warn: list of int
        :param Image: Identity photo
        :type Image: str
        :param AdvancedInfo: Extended field:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param Type: Certificate type
MyKad  ID card
MyPR    Permanent resident card
MyTentera   Military identity card
MyKAS    Temporary ID card
POLIS  Police card
IKAD   Work permit
MyKid   Kid card
        :type Type: str
        :param Birthday: Date of birth (currently, this field is only supported for IKAD).
        :type Birthday: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.Address = None
        self.Sex = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.Type = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.Sex = params.get("Sex")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of image. The image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 500x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies more than 2/3 area of the image.
        :type ImageBase64: str
        :param RetImage: Whether to return an image. Default value: false.
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR response structure.

    """

    def __init__(self):
        r"""
        :param ID: Passport ID
        :type ID: str
        :param Name: Name
        :type Name: str
        :param DateOfBirth: Date of birth
        :type DateOfBirth: str
        :param Sex: Gender (F: female, M: male)
        :type Sex: str
        :param DateOfExpiration: Expiration date
        :type DateOfExpiration: str
        :param IssuingCountry: Issuing country
        :type IssuingCountry: str
        :param Nationality: Nationality
        :type Nationality: str
        :param Warn: Alarm code
-9103 Alarm for spoofed card
-9102 Alarm for photocopied card
-9106 Alarm for covered card
        :type Warn: list of int
        :param Image: Identity photo
        :type Image: str
        :param AdvancedInfo: Extended field:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param CodeSet: The first row of the machine-readable zone (MRZ) at the bottom
        :type CodeSet: str
        :param CodeCrc: The second row of the MRZ at the bottom
        :type CodeCrc: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.DateOfBirth = None
        self.Sex = None
        self.DateOfExpiration = None
        self.IssuingCountry = None
        self.Nationality = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.CodeSet = None
        self.CodeCrc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.DateOfBirth = params.get("DateOfBirth")
        self.Sex = params.get("Sex")
        self.DateOfExpiration = params.get("DateOfExpiration")
        self.IssuingCountry = params.get("IssuingCountry")
        self.Nationality = params.get("Nationality")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.CodeSet = params.get("CodeSet")
        self.CodeCrc = params.get("CodeCrc")
        self.RequestId = params.get("RequestId")


class TableOCRRequest(AbstractModel):
    """TableOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: Base64-encoded value of image.
Supported image formats: PNG, JPG, JPEG. GIF is not supported at present.
Supported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
Either `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 3 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRResponse(AbstractModel):
    """TableOCR response structure.

    """

    def __init__(self):
        r"""
        :param TextDetections: Recognized text. For more information, please click the link on the left
        :type TextDetections: list of TextTable
        :param Data: Base64-encoded Excel data.
        :type Data: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TextDetections = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextTable()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """OCR result.

    """

    def __init__(self):
        r"""
        :param DetectedText: Recognized text line content.
        :type DetectedText: str
        :param Confidence: Confidence. Value range: 0–100.
        :type Confidence: int
        :param Polygon: Text line coordinates, which are represented as 4 vertex coordinates.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Polygon: list of Coord
        :param AdvancedInfo: Extended field.
The paragraph information `Parag` returned by the `GeneralBasicOcr` API contains `ParagNo`.
        :type AdvancedInfo: str
        :param ItemPolygon: Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.
        :type ItemPolygon: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param Words: Information about a character, including the character itself and its confidence. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :type Words: list of DetectedWords
        :param WordCoordPoint: Coordinates of a word’s four corners on the input image. Supported APIs: `GeneralBasicOCR`, `GeneralAccurateOCR`
        :type WordCoordPoint: list of DetectedWordCoordPoint
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.ItemPolygon = None
        self.Words = None
        self.WordCoordPoint = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemPolygon") is not None:
            self.ItemPolygon = ItemCoord()
            self.ItemPolygon._deserialize(params.get("ItemPolygon"))
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = DetectedWords()
                obj._deserialize(item)
                self.Words.append(obj)
        if params.get("WordCoordPoint") is not None:
            self.WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = DetectedWordCoordPoint()
                obj._deserialize(item)
                self.WordCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTable(AbstractModel):
    """Form recognition result.

    """

    def __init__(self):
        r"""
        :param ColTl: Column index of the top-left corner of the cell.
        :type ColTl: int
        :param RowTl: Row index of the top-left corner of the cell.
        :type RowTl: int
        :param ColBr: Column index of the bottom-right corner of the cell.
        :type ColBr: int
        :param RowBr: Row index of the bottom-right corner of the cell.
        :type RowBr: int
        :param Text: Cell text
        :type Text: str
        :param Type: Cell type. Valid values: body, header, footer
        :type Type: str
        :param Confidence: Confidence. Value range: 0–100
        :type Confidence: int
        :param Polygon: Text line coordinates, which are represented as 4 vertex coordinates.
        :type Polygon: list of Coord
        :param AdvancedInfo: Extended field
        :type AdvancedInfo: str
        """
        self.ColTl = None
        self.RowTl = None
        self.ColBr = None
        self.RowBr = None
        self.Text = None
        self.Type = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.ColTl = params.get("ColTl")
        self.RowTl = params.get("RowTl")
        self.ColBr = params.get("ColBr")
        self.RowBr = params.get("RowBr")
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        