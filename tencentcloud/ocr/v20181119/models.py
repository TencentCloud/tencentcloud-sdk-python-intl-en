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


class AirTransport(AbstractModel):
    """Itinerary/Receipt of e-ticket for air transportation

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Number: E-ticket No.
        :type Number: str
        :param CheckCode: Check code
        :type CheckCode: str
        :param SerialNumber: Serial number
        :type SerialNumber: str
        :param Date: Date of issue
        :type Date: str
        :param AgentCode: Agent code
        :type AgentCode: str
        :param AgentCodeFirst: First line of the agent code
        :type AgentCodeFirst: str
        :param AgentCodeSecond: Second line of the agent code
        :type AgentCodeSecond: str
        :param UserName: Name
        :type UserName: str
        :param UserID: ID card number
        :type UserID: str
        :param Issuer: Issuer
        :type Issuer: str
        :param Fare: Fare
        :type Fare: str
        :param Tax: Tax
        :type Tax: str
        :param FuelSurcharge: Fuel surcharge
        :type FuelSurcharge: str
        :param AirDevelopmentFund: Aviation Development Fund
        :type AirDevelopmentFund: str
        :param Insurance: Insurance
        :type Insurance: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param Kind: Invoice type
        :type Kind: str
        :param DomesticInternationalTag: Domestic or international tag
        :type DomesticInternationalTag: str
        :param DateStart: Not-valid-before date
        :type DateStart: str
        :param DateEnd: Not-valid-after date
        :type DateEnd: str
        :param Endorsement: Endorsements/Restrictions
        :type Endorsement: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param FlightItems: Items
        :type FlightItems: list of FlightItem
        """
        self.Title = None
        self.Number = None
        self.CheckCode = None
        self.SerialNumber = None
        self.Date = None
        self.AgentCode = None
        self.AgentCodeFirst = None
        self.AgentCodeSecond = None
        self.UserName = None
        self.UserID = None
        self.Issuer = None
        self.Fare = None
        self.Tax = None
        self.FuelSurcharge = None
        self.AirDevelopmentFund = None
        self.Insurance = None
        self.Total = None
        self.Kind = None
        self.DomesticInternationalTag = None
        self.DateStart = None
        self.DateEnd = None
        self.Endorsement = None
        self.QRCodeMark = None
        self.FlightItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Number = params.get("Number")
        self.CheckCode = params.get("CheckCode")
        self.SerialNumber = params.get("SerialNumber")
        self.Date = params.get("Date")
        self.AgentCode = params.get("AgentCode")
        self.AgentCodeFirst = params.get("AgentCodeFirst")
        self.AgentCodeSecond = params.get("AgentCodeSecond")
        self.UserName = params.get("UserName")
        self.UserID = params.get("UserID")
        self.Issuer = params.get("Issuer")
        self.Fare = params.get("Fare")
        self.Tax = params.get("Tax")
        self.FuelSurcharge = params.get("FuelSurcharge")
        self.AirDevelopmentFund = params.get("AirDevelopmentFund")
        self.Insurance = params.get("Insurance")
        self.Total = params.get("Total")
        self.Kind = params.get("Kind")
        self.DomesticInternationalTag = params.get("DomesticInternationalTag")
        self.DateStart = params.get("DateStart")
        self.DateEnd = params.get("DateEnd")
        self.Endorsement = params.get("Endorsement")
        self.QRCodeMark = params.get("QRCodeMark")
        if params.get("FlightItems") is not None:
            self.FlightItems = []
            for item in params.get("FlightItems"):
                obj = FlightItem()
                obj._deserialize(item)
                self.FlightItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class BusInvoice(AbstractModel):
    """Bus ticket

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param Number: Invoice number
        :type Number: str
        :param Code: Invoice code
        :type Code: str
        :param Date: Date of issue
        :type Date: str
        :param TimeGetOn: Departure time
        :type TimeGetOn: str
        :param DateGetOn: Departure date
        :type DateGetOn: str
        :param StationGetOn: Departure station
        :type StationGetOn: str
        :param StationGetOff: Destination
        :type StationGetOff: str
        :param Total: Fare
        :type Total: str
        :param UserName: Name
        :type UserName: str
        :param Kind: Consumption type
        :type Kind: str
        :param UserID: ID card number
        :type UserID: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param PlaceGetOn: Departure place
        :type PlaceGetOn: str
        :param GateNumber: Check-in gate
        :type GateNumber: str
        :param TicketType: Fare category
        :type TicketType: str
        :param VehicleType: Vehicle type
        :type VehicleType: str
        :param SeatNumber: Seat No.
        :type SeatNumber: str
        :param TrainNumber: Fleet number
        :type TrainNumber: str
        """
        self.Title = None
        self.QRCodeMark = None
        self.Number = None
        self.Code = None
        self.Date = None
        self.TimeGetOn = None
        self.DateGetOn = None
        self.StationGetOn = None
        self.StationGetOff = None
        self.Total = None
        self.UserName = None
        self.Kind = None
        self.UserID = None
        self.Province = None
        self.City = None
        self.PlaceGetOn = None
        self.GateNumber = None
        self.TicketType = None
        self.VehicleType = None
        self.SeatNumber = None
        self.TrainNumber = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.QRCodeMark = params.get("QRCodeMark")
        self.Number = params.get("Number")
        self.Code = params.get("Code")
        self.Date = params.get("Date")
        self.TimeGetOn = params.get("TimeGetOn")
        self.DateGetOn = params.get("DateGetOn")
        self.StationGetOn = params.get("StationGetOn")
        self.StationGetOff = params.get("StationGetOff")
        self.Total = params.get("Total")
        self.UserName = params.get("UserName")
        self.Kind = params.get("Kind")
        self.UserID = params.get("UserID")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.PlaceGetOn = params.get("PlaceGetOn")
        self.GateNumber = params.get("GateNumber")
        self.TicketType = params.get("TicketType")
        self.VehicleType = params.get("VehicleType")
        self.SeatNumber = params.get("SeatNumber")
        self.TrainNumber = params.get("TrainNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class FlightItem(AbstractModel):
    """Flight items

    """

    def __init__(self):
        r"""
        :param TerminalGetOn: Departure terminal
        :type TerminalGetOn: str
        :param TerminalGetOff: Arrival terminal
        :type TerminalGetOff: str
        :param Carrier: Carrier
        :type Carrier: str
        :param FlightNumber: Flight number
        :type FlightNumber: str
        :param Seat: Class
        :type Seat: str
        :param DateGetOn: Departure date
        :type DateGetOn: str
        :param TimeGetOn: Departure time
        :type TimeGetOn: str
        :param StationGetOn: Departure city
        :type StationGetOn: str
        :param StationGetOff: Arrival city
        :type StationGetOff: str
        :param Allow: Baggage allowance
        :type Allow: str
        :param FareBasis: Fare category
        :type FareBasis: str
        """
        self.TerminalGetOn = None
        self.TerminalGetOff = None
        self.Carrier = None
        self.FlightNumber = None
        self.Seat = None
        self.DateGetOn = None
        self.TimeGetOn = None
        self.StationGetOn = None
        self.StationGetOff = None
        self.Allow = None
        self.FareBasis = None


    def _deserialize(self, params):
        self.TerminalGetOn = params.get("TerminalGetOn")
        self.TerminalGetOff = params.get("TerminalGetOff")
        self.Carrier = params.get("Carrier")
        self.FlightNumber = params.get("FlightNumber")
        self.Seat = params.get("Seat")
        self.DateGetOn = params.get("DateGetOn")
        self.TimeGetOn = params.get("TimeGetOn")
        self.StationGetOn = params.get("StationGetOn")
        self.StationGetOff = params.get("StationGetOff")
        self.Allow = params.get("Allow")
        self.FareBasis = params.get("FareBasis")
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
        :param Angel: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
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
        :param Angel: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
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


class GeneralMachineItem(AbstractModel):
    """Items of a general machine-printed invoice

    """

    def __init__(self):
        r"""
        :param Name: Item name
        :type Name: str
        :param Specification: Specification
        :type Specification: str
        :param Unit: Unit
        :type Unit: str
        :param Quantity: Quantity
        :type Quantity: str
        :param Price: Unit price
        :type Price: str
        :param Total: Amount
        :type Total: str
        :param TaxRate: Tax rate
        :type TaxRate: str
        :param Tax: Tax amount
        :type Tax: str
        """
        self.Name = None
        self.Specification = None
        self.Unit = None
        self.Quantity = None
        self.Price = None
        self.Total = None
        self.TaxRate = None
        self.Tax = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Specification = params.get("Specification")
        self.Unit = params.get("Unit")
        self.Quantity = params.get("Quantity")
        self.Price = params.get("Price")
        self.Total = params.get("Total")
        self.TaxRate = params.get("TaxRate")
        self.Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """The sequence number of an element group in the image

    """

    def __init__(self):
        r"""
        :param Groups: The elements in each line.
        :type Groups: list of LineInfo
        """
        self.Groups = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = LineInfo()
                obj._deserialize(item)
                self.Groups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param WarningCode: Multiple alarm codes. If the ID card is spoofed, photocopied, or photoshopped, the corresponding alarm code will be returned.
-9102: Alarm for photocopied document
-9103: Alarm for spoofed document
-9104: Alarm for photoshopped document
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


class HmtResidentPermitOCRRequest(AbstractModel):
    """HmtResidentPermitOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param CardSide: `FRONT`: The side with the profile photo.
`BACK`: The side with the national emblem.
If this parameter is not specified, the system will automatically determine the ID card side.
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HmtResidentPermitOCRResponse(AbstractModel):
    """HmtResidentPermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param Sex: Gender
        :type Sex: str
        :param Birth: Date of birth
        :type Birth: str
        :param Address: Address
        :type Address: str
        :param IdCardNo: ID card number
        :type IdCardNo: str
        :param CardType: 0: Front side.
1: Back side.
        :type CardType: int
        :param ValidDate: Validity period
        :type ValidDate: str
        :param Authority: Issuing authority
        :type Authority: str
        :param VisaNum: Number of issues
        :type VisaNum: str
        :param PassNo: Permit number
        :type PassNo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Birth = None
        self.Address = None
        self.IdCardNo = None
        self.CardType = None
        self.ValidDate = None
        self.Authority = None
        self.VisaNum = None
        self.PassNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdCardNo = params.get("IdCardNo")
        self.CardType = params.get("CardType")
        self.ValidDate = params.get("ValidDate")
        self.Authority = params.get("Authority")
        self.VisaNum = params.get("VisaNum")
        self.PassNo = params.get("PassNo")
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        :param CardSide: `FRONT`: The side with the profile photo.
`BACK`: The side with the national emblem.
If this parameter is not specified, the system will automatically determine the ID card side.
        :type CardSide: str
        :param Config: The following parameters are all of `bool` type and default to `false`:
`CropIdCard`: Crops the ID card photo (by removing extra edges outside the ID card and automatically correcting the shooting angle).
`CropPortrait`: Crops the profile photo (by automatically cutting out the face area in the ID card).
`CopyWarn`: Warns about photocopied images.
`BorderCheckWarn`: Warns about border and frame occlusions.
`ReshootWarn`: Warns about spoofed images.
`DetectPsWarn`: Warns about photoshopped images.
`TempIdWarn`: Warns about temporary ID cards.
`InvalidDateWarn`: Warns about invalid ID card validity periods.
`Quality`: Gets the image quality score (by evaluating the blurriness of the image).
`MultiCardDetect`: Enables multi-card detection.
`ReflectWarn`: Enables glare detection.

Parameter setting method via SDK:
Config = Json.stringify({"CropIdCard":true,"CropPortrait":true})
Parameter setting method via API 3.0 Explorer:
Config = {"CropIdCard":true,"CropPortrait":true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param Name: Name (profile photo side)
        :type Name: str
        :param Sex: Gender (profile photo side)
        :type Sex: str
        :param Nation: Ethnicity (profile photo side)
        :type Nation: str
        :param Birth: Date of birth (profile photo side)
        :type Birth: str
        :param Address: Address (profile photo side)
        :type Address: str
        :param IdNum: ID number (profile photo side)
        :type IdNum: str
        :param Authority: Issuing authority (national emblem side)
        :type Authority: str
        :param ValidDate: Validity period (national emblem side)
        :type ValidDate: str
        :param AdvancedInfo: Extended information, which will be returned only when requested. For the input parameters, please see example 3 and example 4.
`IdCard`: Base64-encoded content of the cropped ID card photo, which will be returned if `Config.CropIdCard` is set to `true`.
`Portrait`: Base64-encoded content of the ID photo on the card, which will be returned if `Config.CropPortrait` is set to `true`.

`Quality`: Image quality score, which will be returned if `Config.Quality` is set to `true`. Value range: 0–100. The lower the score, the blurrier the image. The recommended threshold is ≥ 50.
`BorderCodeValue`: Warning threshold score for incomplete ID card borders, which will be returned if `Config.BorderCheckWarn` is set to `true`. Value range: 0–100. The lower the score, the lower the probability of border occlusion. The recommended threshold value is ≤ 50.

`WarnInfos`: Warning information. Warning codes and descriptions are as follows:
-9100: The ID card validity period is invalid.
-9101: The ID card borders are incomplete.
-9102: The ID card image is photocopied.
-9103: The ID card image is spoofed. 
-9104: The ID card is a temporary one. 
-9105: The ID card frame is occluded.
-9106: The ID card image is photoshopped.
-9107: The ID card image has glares.
        :type AdvancedInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.IdNum = None
        self.Authority = None
        self.ValidDate = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdNum = params.get("IdNum")
        self.Authority = params.get("Authority")
        self.ValidDate = params.get("ValidDate")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class InvoiceItem(AbstractModel):
    """Recognition information of a single invoice/ticket among multiple types of invoices/tickets

    """

    def __init__(self):
        r"""
        :param Code: The recognition result.
`OK`: Recognition is successful.
`FailedOperation.UnsupportedInvoice`: Recognition is not supported.
`FailedOperation.UnKnowError`: Recognition failed.
For the information about other error codes, see the OCR API description for each invoice/ticket.
        :type Code: str
        :param Type: The type of invoice/ticket to which the recognized image belongs.
-1: Unknown
0: Taxi receipt
1: Quota invoice
2: Train ticket
3: VAT invoice
5: Itinerary/Receipt of e-ticket for air transportation
8: General machine-printed invoice
9: Bus ticket
10: Ship ticket
11: VAT invoice (roll)
12: Car sales invoice
13: Toll receipt
15: Non-tax revenue invoice
16: Fully digitalized electronic invoice
        :type Type: int
        :param Polygon: The coordinates of the four vertices of the rotated image.
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param Angle: The rotation angle of the recognized image in the image with multiple types of invoices/tickets.
        :type Angle: float
        :param SingleInvoiceInfos: The recognized content.
        :type SingleInvoiceInfos: :class:`tencentcloud.ocr.v20181119.models.SingleInvoiceItem`
        :param Page: The number of the page on which the recognized invoice is in the image or PDF file, starting from 1 by default.
        :type Page: int
        :param SubType: The detailed invoice type. See the description of `SubType`.
        :type SubType: str
        :param TypeDescription: The invoice description. See the description of `TypeDescription`.
        :type TypeDescription: str
        :param CutImage: The image file after cropping, encoded in Base64. This is returned if `EnableCutImage` is set to `true`.
        :type CutImage: str
        :param SubTypeDescription: The description of the detailed invoice type. See the description of `SubType`.
        :type SubTypeDescription: str
        """
        self.Code = None
        self.Type = None
        self.Polygon = None
        self.Angle = None
        self.SingleInvoiceInfos = None
        self.Page = None
        self.SubType = None
        self.TypeDescription = None
        self.CutImage = None
        self.SubTypeDescription = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        if params.get("Polygon") is not None:
            self.Polygon = Polygon()
            self.Polygon._deserialize(params.get("Polygon"))
        self.Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self.SingleInvoiceInfos = SingleInvoiceItem()
            self.SingleInvoiceInfos._deserialize(params.get("SingleInvoiceInfos"))
        self.Page = params.get("Page")
        self.SubType = params.get("SubType")
        self.TypeDescription = params.get("TypeDescription")
        self.CutImage = params.get("CutImage")
        self.SubTypeDescription = params.get("SubTypeDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ItemInfo(AbstractModel):
    """Structured element group

    """

    def __init__(self):
        r"""
        :param Key: The key information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: :class:`tencentcloud.ocr.v20181119.models.Key`
        :param Value: The value information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: :class:`tencentcloud.ocr.v20181119.models.Value`
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        if params.get("Key") is not None:
            self.Key = Key()
            self.Key._deserialize(params.get("Key"))
        if params.get("Value") is not None:
            self.Value = Value()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Key(AbstractModel):
    """Key information

    """

    def __init__(self):
        r"""
        :param AutoName: The name of the recognized field.
        :type AutoName: str
        :param ConfigName: The name of a defined field (the key passed in).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigName: str
        """
        self.AutoName = None
        self.ConfigName = None


    def _deserialize(self, params):
        self.AutoName = params.get("AutoName")
        self.ConfigName = params.get("ConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateInfo(AbstractModel):
    """Vehicle license plate information

    """

    def __init__(self):
        r"""
        :param Number: The recognized license plate number.
        :type Number: str
        :param Confidence: The confidence score (0–100).
        :type Confidence: int
        :param Rect: The bounding box coordinates of the text line in the original image.
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Color: The recognized license plate color, which currently includes "white", "black", "blue", "green", "yellow", "yellow-green", and "temporary plate".
        :type Color: str
        """
        self.Number = None
        self.Confidence = None
        self.Rect = None
        self.Color = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
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
        


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR response structure.

    """

    def __init__(self):
        r"""
        :param Number: The recognized license plate number.
        :type Number: str
        :param Confidence: The confidence score (0–100).
        :type Confidence: int
        :param Rect: The bounding box coordinates of the text line in the original image.
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Color: The recognized license plate color, which currently includes "white", "black", "blue", "green", "yellow", "yellow-green", and "temporary plate".
        :type Color: str
        :param LicensePlateInfos: The vehicle license plate information.
        :type LicensePlateInfos: list of LicensePlateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Number = None
        self.Confidence = None
        self.Rect = None
        self.Color = None
        self.LicensePlateInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Color = params.get("Color")
        if params.get("LicensePlateInfos") is not None:
            self.LicensePlateInfos = []
            for item in params.get("LicensePlateInfos"):
                obj = LicensePlateInfo()
                obj._deserialize(item)
                self.LicensePlateInfos.append(obj)
        self.RequestId = params.get("RequestId")


class LineInfo(AbstractModel):
    """Line number

    """

    def __init__(self):
        r"""
        :param Lines: The elements in a line
        :type Lines: list of ItemInfo
        """
        self.Lines = None


    def _deserialize(self, params):
        if params.get("Lines") is not None:
            self.Lines = []
            for item in params.get("Lines"):
                obj = ItemInfo()
                obj._deserialize(item)
                self.Lines.append(obj)
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
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
        :type ImageBase64: str
        :param ImageUrl: The URL of an image. (This field is not available outside the Chinese mainland.)
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be low.
        :type ImageUrl: str
        :param RetImage: Whether to return an image. Default value: `false`.
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
        :param ID: ID number
        :type ID: str
        :param Name: Full name
        :type Name: str
        :param Address: Address
        :type Address: str
        :param Sex: Gender
        :type Sex: str
        :param Warn: Alarm codes
-9103 Alarm for photographed certificate
-9102 Alarm for photocopied certificate
-9106 Alarm for covered certificate
-9107 Alarm for blurry image
        :type Warn: list of int
        :param Image: Identity photo
        :type Image: str
        :param AdvancedInfo: This is an extended field, 
with the confidence of a field recognition result returned in the following format.
{
  Field name:{
    Confidence:0.9999
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
        :param Birthday: Date of birth. This field is available only for work permits (i-Kad) and ID cards (MyKad).
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
        :param Nationality: Country/region code
        :type Nationality: str
        :param Warn: Alarm codes
-9103 Alarm for spoofed document
-9102 Alarm for photocopied document (including black & white and color ones)
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
        :param Surname: The surname.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Surname: str
        :param GivenName: The given name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GivenName: str
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
        self.Surname = None
        self.GivenName = None
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
        self.Surname = params.get("Surname")
        self.GivenName = params.get("GivenName")
        self.RequestId = params.get("RequestId")


class MachinePrintedInvoice(AbstractModel):
    """General machine-printed invoice

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Date: Date of issue
        :type Date: str
        :param Time: Time
        :type Time: str
        :param CheckCode: Check code
        :type CheckCode: str
        :param Ciphertext: Ciphertext
        :type Ciphertext: str
        :param Category: Category
        :type Category: str
        :param PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Tax: Tax
        :type Tax: str
        :param IndustryClass: Industry
        :type IndustryClass: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param SellerAddrTel: Seller's address and phone number
        :type SellerAddrTel: str
        :param SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param BuyerAddrTel: Buyer's address and phone number
        :type BuyerAddrTel: str
        :param BuyerBankAccount: Buyer's bank account number
        :type BuyerBankAccount: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param ElectronicMark: Whether it is a general machine-printed invoice issued by Zhejiang or Guangdong province (0: No, 1: Yes)
        :type ElectronicMark: int
        :param Issuer: Issuer
        :type Issuer: str
        :param Receiptor: Payee
        :type Receiptor: str
        :param Reviewer: Reviewer
        :type Reviewer: str
        :param Remark: Remarks
        :type Remark: str
        :param PaymentInfo: Operator's payment information
        :type PaymentInfo: str
        :param TicketPickupUser: Operator-assigned invoice pickup user
        :type TicketPickupUser: str
        :param MerchantNumber: Operator's merchant number
        :type MerchantNumber: str
        :param OrderNumber: Operator's order number
        :type OrderNumber: str
        :param GeneralMachineItems: Items
        :type GeneralMachineItems: list of GeneralMachineItem
        """
        self.Title = None
        self.QRCodeMark = None
        self.Code = None
        self.Number = None
        self.Date = None
        self.Time = None
        self.CheckCode = None
        self.Ciphertext = None
        self.Category = None
        self.PretaxAmount = None
        self.Total = None
        self.TotalCn = None
        self.Tax = None
        self.IndustryClass = None
        self.Seller = None
        self.SellerTaxID = None
        self.SellerAddrTel = None
        self.SellerBankAccount = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.BuyerAddrTel = None
        self.BuyerBankAccount = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.CompanySealMark = None
        self.ElectronicMark = None
        self.Issuer = None
        self.Receiptor = None
        self.Reviewer = None
        self.Remark = None
        self.PaymentInfo = None
        self.TicketPickupUser = None
        self.MerchantNumber = None
        self.OrderNumber = None
        self.GeneralMachineItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.QRCodeMark = params.get("QRCodeMark")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.Time = params.get("Time")
        self.CheckCode = params.get("CheckCode")
        self.Ciphertext = params.get("Ciphertext")
        self.Category = params.get("Category")
        self.PretaxAmount = params.get("PretaxAmount")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Tax = params.get("Tax")
        self.IndustryClass = params.get("IndustryClass")
        self.Seller = params.get("Seller")
        self.SellerTaxID = params.get("SellerTaxID")
        self.SellerAddrTel = params.get("SellerAddrTel")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.BuyerAddrTel = params.get("BuyerAddrTel")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.CompanySealMark = params.get("CompanySealMark")
        self.ElectronicMark = params.get("ElectronicMark")
        self.Issuer = params.get("Issuer")
        self.Receiptor = params.get("Receiptor")
        self.Reviewer = params.get("Reviewer")
        self.Remark = params.get("Remark")
        self.PaymentInfo = params.get("PaymentInfo")
        self.TicketPickupUser = params.get("TicketPickupUser")
        self.MerchantNumber = params.get("MerchantNumber")
        self.OrderNumber = params.get("OrderNumber")
        if params.get("GeneralMachineItems") is not None:
            self.GeneralMachineItems = []
            for item in params.get("GeneralMachineItems"):
                obj = GeneralMachineItem()
                obj._deserialize(item)
                self.GeneralMachineItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param RetProfile: Whether to return the ID photo. By default, the ID photo is not returned.
        :type RetProfile: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetProfile = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetProfile = params.get("RetProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRResponse(AbstractModel):
    """MainlandPermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param Name: Name in Chinese
        :type Name: str
        :param EnglishName: Name in English
        :type EnglishName: str
        :param Sex: Gender
        :type Sex: str
        :param Birthday: Date of birth
        :type Birthday: str
        :param IssueAuthority: Issuing authority
        :type IssueAuthority: str
        :param ValidDate: Validity period
        :type ValidDate: str
        :param Number: ID number
        :type Number: str
        :param IssueAddress: Place of issue
        :type IssueAddress: str
        :param IssueNumber: Number of issues
        :type IssueNumber: str
        :param Type: Document type
        :type Type: str
        :param Profile: Base64-encoded profile photo, which is returned only when `RetProfile` is set to `True`
        :type Profile: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Sex = None
        self.Birthday = None
        self.IssueAuthority = None
        self.ValidDate = None
        self.Number = None
        self.IssueAddress = None
        self.IssueNumber = None
        self.Type = None
        self.Profile = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.IssueAuthority = params.get("IssueAuthority")
        self.ValidDate = params.get("ValidDate")
        self.Number = params.get("Number")
        self.IssueAddress = params.get("IssueAddress")
        self.IssueNumber = params.get("IssueNumber")
        self.Type = params.get("Type")
        self.Profile = params.get("Profile")
        self.RequestId = params.get("RequestId")


class MedicalInvoice(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param Title: 
        :type Title: str
        :param Code: 
        :type Code: str
        :param Number: 
        :type Number: str
        :param Total: 
        :type Total: str
        :param TotalCn: 
        :type TotalCn: str
        :param Date: 
        :type Date: str
        :param CheckCode: 
        :type CheckCode: str
        :param Place: 
        :type Place: str
        :param Reviewer: 
        :type Reviewer: str
        """
        self.Title = None
        self.Code = None
        self.Number = None
        self.Total = None
        self.TotalCn = None
        self.Date = None
        self.CheckCode = None
        self.Place = None
        self.Reviewer = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Date = params.get("Date")
        self.CheckCode = params.get("CheckCode")
        self.Place = params.get("Place")
        self.Reviewer = params.get("Reviewer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MotorVehicleSaleInvoice(AbstractModel):
    """Motor vehicle sales invoice

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Date: Date of issue
        :type Date: str
        :param PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTaxID: Seller's company code
        :type SellerTaxID: str
        :param SellerTel: Seller's phone number
        :type SellerTel: str
        :param SellerAddress: Seller's address
        :type SellerAddress: str
        :param SellerBank: Seller's account opening bank
        :type SellerBank: str
        :param SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param BuyerID: Buyer's ID number/organization code
        :type BuyerID: str
        :param TaxAuthorities: Tax authority
        :type TaxAuthorities: str
        :param TaxAuthoritiesCode: Code of the tax authority
        :type TaxAuthoritiesCode: str
        :param VIN: VIN
        :type VIN: str
        :param VehicleModel: Vehicle model
        :type VehicleModel: str
        :param VehicleEngineCode: Engine No.
        :type VehicleEngineCode: str
        :param CertificateNumber: No. of the certificate of conformity
        :type CertificateNumber: str
        :param InspectionNumber: Inspection No.
        :type InspectionNumber: str
        :param MachineID: Machine No.
        :type MachineID: str
        :param VehicleType: Vehicle type
        :type VehicleType: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param Tax: Tax
        :type Tax: str
        :param TaxRate: Tax rate
        :type TaxRate: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param Tonnage: Tonnage
        :type Tonnage: str
        :param Remark: Remarks
        :type Remark: str
        :param FormType: Form type
        :type FormType: str
        :param FormName: Form name
        :type FormName: str
        :param Issuer: Issuer
        :type Issuer: str
        :param TaxNum: Tax payment voucher number
        :type TaxNum: str
        :param MaxPeopleNum: Passenger capacity
        :type MaxPeopleNum: str
        :param Origin: Origin
        :type Origin: str
        :param MachineCode: Machine-printed invoice code
        :type MachineCode: str
        :param MachineNumber: Machine-printed invoice number
        :type MachineNumber: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        """
        self.Title = None
        self.Code = None
        self.Number = None
        self.Date = None
        self.PretaxAmount = None
        self.Total = None
        self.TotalCn = None
        self.Seller = None
        self.SellerTaxID = None
        self.SellerTel = None
        self.SellerAddress = None
        self.SellerBank = None
        self.SellerBankAccount = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.BuyerID = None
        self.TaxAuthorities = None
        self.TaxAuthoritiesCode = None
        self.VIN = None
        self.VehicleModel = None
        self.VehicleEngineCode = None
        self.CertificateNumber = None
        self.InspectionNumber = None
        self.MachineID = None
        self.VehicleType = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.Tax = None
        self.TaxRate = None
        self.CompanySealMark = None
        self.Tonnage = None
        self.Remark = None
        self.FormType = None
        self.FormName = None
        self.Issuer = None
        self.TaxNum = None
        self.MaxPeopleNum = None
        self.Origin = None
        self.MachineCode = None
        self.MachineNumber = None
        self.QRCodeMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.PretaxAmount = params.get("PretaxAmount")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Seller = params.get("Seller")
        self.SellerTaxID = params.get("SellerTaxID")
        self.SellerTel = params.get("SellerTel")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerBank = params.get("SellerBank")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.BuyerID = params.get("BuyerID")
        self.TaxAuthorities = params.get("TaxAuthorities")
        self.TaxAuthoritiesCode = params.get("TaxAuthoritiesCode")
        self.VIN = params.get("VIN")
        self.VehicleModel = params.get("VehicleModel")
        self.VehicleEngineCode = params.get("VehicleEngineCode")
        self.CertificateNumber = params.get("CertificateNumber")
        self.InspectionNumber = params.get("InspectionNumber")
        self.MachineID = params.get("MachineID")
        self.VehicleType = params.get("VehicleType")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Tax = params.get("Tax")
        self.TaxRate = params.get("TaxRate")
        self.CompanySealMark = params.get("CompanySealMark")
        self.Tonnage = params.get("Tonnage")
        self.Remark = params.get("Remark")
        self.FormType = params.get("FormType")
        self.FormName = params.get("FormName")
        self.Issuer = params.get("Issuer")
        self.TaxNum = params.get("TaxNum")
        self.MaxPeopleNum = params.get("MaxPeopleNum")
        self.Origin = params.get("Origin")
        self.MachineCode = params.get("MachineCode")
        self.MachineNumber = params.get("MachineNumber")
        self.QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxIncomeBill(AbstractModel):
    """Non-tax revenue

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Number: Invoice number
        :type Number: str
        :param Code: Invoice code
        :type Code: str
        :param CheckCode: Check code
        :type CheckCode: str
        :param Date: Date of issue
        :type Date: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Buyer: Payer's name
        :type Buyer: str
        :param BuyerTaxID: Payer's taxpayer identification number
        :type BuyerTaxID: str
        :param Seller: Payee's name
        :type Seller: str
        :param SellerCompany: Payee's company name
        :type SellerCompany: str
        :param Remark: Remarks
        :type Remark: str
        :param CurrencyCode: Currency
        :type CurrencyCode: str
        :param Reviewer: Reviewer
        :type Reviewer: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param OtherInfo: Other information
        :type OtherInfo: str
        :param PaymentCode: Payment code
        :type PaymentCode: str
        :param ReceiveUnitCode: Collecting organization's code
        :type ReceiveUnitCode: str
        :param Receiver: Collecting organization's name
        :type Receiver: str
        :param Operator: Operator
        :type Operator: str
        :param PayerAccount: Payer's account
        :type PayerAccount: str
        :param PayerBank: Payer's account opening bank
        :type PayerBank: str
        :param ReceiverAccount: Payee's account
        :type ReceiverAccount: str
        :param ReceiverBank: Payee's account opening bank
        :type ReceiverBank: str
        :param NonTaxItems: Items
        :type NonTaxItems: list of NonTaxItem
        """
        self.Title = None
        self.Number = None
        self.Code = None
        self.CheckCode = None
        self.Date = None
        self.Total = None
        self.TotalCn = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.Seller = None
        self.SellerCompany = None
        self.Remark = None
        self.CurrencyCode = None
        self.Reviewer = None
        self.QRCodeMark = None
        self.OtherInfo = None
        self.PaymentCode = None
        self.ReceiveUnitCode = None
        self.Receiver = None
        self.Operator = None
        self.PayerAccount = None
        self.PayerBank = None
        self.ReceiverAccount = None
        self.ReceiverBank = None
        self.NonTaxItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Number = params.get("Number")
        self.Code = params.get("Code")
        self.CheckCode = params.get("CheckCode")
        self.Date = params.get("Date")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.Seller = params.get("Seller")
        self.SellerCompany = params.get("SellerCompany")
        self.Remark = params.get("Remark")
        self.CurrencyCode = params.get("CurrencyCode")
        self.Reviewer = params.get("Reviewer")
        self.QRCodeMark = params.get("QRCodeMark")
        self.OtherInfo = params.get("OtherInfo")
        self.PaymentCode = params.get("PaymentCode")
        self.ReceiveUnitCode = params.get("ReceiveUnitCode")
        self.Receiver = params.get("Receiver")
        self.Operator = params.get("Operator")
        self.PayerAccount = params.get("PayerAccount")
        self.PayerBank = params.get("PayerBank")
        self.ReceiverAccount = params.get("ReceiverAccount")
        self.ReceiverBank = params.get("ReceiverBank")
        if params.get("NonTaxItems") is not None:
            self.NonTaxItems = []
            for item in params.get("NonTaxItems"):
                obj = NonTaxItem()
                obj._deserialize(item)
                self.NonTaxItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxItem(AbstractModel):
    """Non-tax revenue items

    """

    def __init__(self):
        r"""
        :param ItemID: Item code
        :type ItemID: str
        :param Name: Item name
        :type Name: str
        :param Unit: Unit
        :type Unit: str
        :param Quantity: Quantity
        :type Quantity: str
        :param Standard: Standard
        :type Standard: str
        :param Total: Amount
        :type Total: str
        """
        self.ItemID = None
        self.Name = None
        self.Unit = None
        self.Quantity = None
        self.Standard = None
        self.Total = None


    def _deserialize(self, params):
        self.ItemID = params.get("ItemID")
        self.Name = params.get("Name")
        self.Unit = params.get("Unit")
        self.Quantity = params.get("Quantity")
        self.Standard = params.get("Standard")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoice(AbstractModel):
    """Other invoices

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Total: Amount
        :type Total: str
        :param OtherInvoiceListItems: List
        :type OtherInvoiceListItems: list of OtherInvoiceItem
        :param OtherInvoiceTableItems: Table
        :type OtherInvoiceTableItems: list of OtherInvoiceList
        """
        self.Title = None
        self.Total = None
        self.OtherInvoiceListItems = None
        self.OtherInvoiceTableItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Total = params.get("Total")
        if params.get("OtherInvoiceListItems") is not None:
            self.OtherInvoiceListItems = []
            for item in params.get("OtherInvoiceListItems"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self.OtherInvoiceListItems.append(obj)
        if params.get("OtherInvoiceTableItems") is not None:
            self.OtherInvoiceTableItems = []
            for item in params.get("OtherInvoiceTableItems"):
                obj = OtherInvoiceList()
                obj._deserialize(item)
                self.OtherInvoiceTableItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceItem(AbstractModel):
    """Items of other invoices

    """

    def __init__(self):
        r"""
        :param Name: Field name
        :type Name: str
        :param Value: Field value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceList(AbstractModel):
    """Table of other invoices

    """

    def __init__(self):
        r"""
        :param OtherInvoiceItemList: List
        :type OtherInvoiceItemList: list of OtherInvoiceItem
        """
        self.OtherInvoiceItemList = None


    def _deserialize(self, params):
        if params.get("OtherInvoiceItemList") is not None:
            self.OtherInvoiceItemList = []
            for item in params.get("OtherInvoiceItemList"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self.OtherInvoiceItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRRequest(AbstractModel):
    """PermitOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
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
        


class PermitOCRResponse(AbstractModel):
    """PermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param EnglishName: Name in English
        :type EnglishName: str
        :param Number: ID number
        :type Number: str
        :param Sex: Gender
        :type Sex: str
        :param ValidDate: Validity period
        :type ValidDate: str
        :param IssueAuthority: Issuing authority
        :type IssueAuthority: str
        :param IssueAddress: Place of issue
        :type IssueAddress: str
        :param Birthday: Date of birth
        :type Birthday: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Number = None
        self.Sex = None
        self.ValidDate = None
        self.IssueAuthority = None
        self.IssueAddress = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Number = params.get("Number")
        self.Sex = params.get("Sex")
        self.ValidDate = params.get("ValidDate")
        self.IssueAuthority = params.get("IssueAuthority")
        self.IssueAddress = params.get("IssueAddress")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    """The coordinates of the four vertices of the text
    Note: This field may return null, indicating that no valid values can be obtained.

    """

    def __init__(self):
        r"""
        :param LeftTop: The coordinates of the upper-left vertex.
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightTop: The coordinates of the upper-right vertex.
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightBottom: The coordinates of the lower-left vertex.
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param LeftBottom: The coordinates of the lower-right vertex.
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self.LeftTop = None
        self.RightTop = None
        self.RightBottom = None
        self.LeftBottom = None


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self.LeftTop = Coord()
            self.LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self.RightTop = Coord()
            self.RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self.RightBottom = Coord()
            self.RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self.LeftBottom = Coord()
            self.LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoice(AbstractModel):
    """Quota invoice

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self.Title = None
        self.Code = None
        self.Number = None
        self.Total = None
        self.TotalCn = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.QRCodeMark = None
        self.CompanySealMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.QRCodeMark = params.get("QRCodeMark")
        self.CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeGeneralInvoiceRequest(AbstractModel):
    """RecognizeGeneralInvoice request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, JPEG, and PDF. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Supported image pixels: 20 to 10,000
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, JPEG, and PDF. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Supported image pixels: 20 to 10,000
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param Types: The list of the types of invoices to be recognized. If this parameter is left empty, all types of invoices are recognized.
0: Taxi receipt
1: Quota invoice
2: Train ticket
3: VAT invoice
5: Itinerary/Receipt of e-ticket for air transport
8: General machine-printed invoice
9: Bus ticket
10: Ship ticket
11: VAT invoice (roll)
12: Car sales inovice
13: Toll receipt
15: Non-tax revenue invoice
16: Fully digitalized electronic invoice
-1: Other

By default, this parameter is left empty, which means to recognize all types of invoices.
When a single type is passed in, the image is recognized based on this type.
You can only specify a singe type or all types, but not some types.
        :type Types: list of int
        :param EnableOther: Whether to enable recognition of other invoices. If you enable this feature, other invoices can be recognized. Default value: `true`.	
        :type EnableOther: bool
        :param EnablePdf: Whether to enable PDF recognition. If you enable this feature, both images and PDF files can be recognized. Default value: `true`.
        :type EnablePdf: bool
        :param PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `EnablePdf` is `true`. Default value: 1.
        :type PdfPageNumber: int
        :param EnableMultiplePage: Whether to enable multi-page PDF recognition. If you enable this feature, multiple pages of a PDF file can be recognized, and the recognition results of a maximum of the first 30 pages can be returned. After you enable this feature, input parameters `EnablePdf` and `PdfPageNumber` are invalid. Default value: `false`.
        :type EnableMultiplePage: bool
        :param EnableCutImage: Whether to return the Base64-encoded value of the cropped image. Default value: `false`.
        :type EnableCutImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Types = None
        self.EnableOther = None
        self.EnablePdf = None
        self.PdfPageNumber = None
        self.EnableMultiplePage = None
        self.EnableCutImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Types = params.get("Types")
        self.EnableOther = params.get("EnableOther")
        self.EnablePdf = params.get("EnablePdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.EnableMultiplePage = params.get("EnableMultiplePage")
        self.EnableCutImage = params.get("EnableCutImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeGeneralInvoiceResponse(AbstractModel):
    """RecognizeGeneralInvoice response structure.

    """

    def __init__(self):
        r"""
        :param MixedInvoiceItems: Mixed invoice/ticket recognition result. Please click the link on the left for details.
        :type MixedInvoiceItems: list of InvoiceItem
        :param TotalPDFCount: Total number of pages in the PDF file.
        :type TotalPDFCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MixedInvoiceItems = None
        self.TotalPDFCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self.MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = InvoiceItem()
                obj._deserialize(item)
                self.MixedInvoiceItems.append(obj)
        self.TotalPDFCount = params.get("TotalPDFCount")
        self.RequestId = params.get("RequestId")


class RecognizeIndonesiaIDCardOCRRequest(AbstractModel):
    """RecognizeIndonesiaIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param Scene: The scene, which defaults to `V1`.
Valid values:
V1
V2
        :type Scene: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None
        self.Scene = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeIndonesiaIDCardOCRResponse(AbstractModel):
    """RecognizeIndonesiaIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param NIK: The Single Identity Number.
        :type NIK: str
        :param Nama: The full name.
        :type Nama: str
        :param TempatTglLahir: The place and date of birth.
        :type TempatTglLahir: str
        :param JenisKelamin: The gender.
        :type JenisKelamin: str
        :param GolDarah: The blood type.
        :type GolDarah: str
        :param Alamat: The address.
        :type Alamat: str
        :param RTRW: The street.
        :type RTRW: str
        :param KelDesa: The village.
        :type KelDesa: str
        :param Kecamatan: The region.
        :type Kecamatan: str
        :param Agama: The religion.
        :type Agama: str
        :param StatusPerkawinan: The marital status.
        :type StatusPerkawinan: str
        :param Perkerjaan: The occupation.
        :type Perkerjaan: str
        :param KewargaNegaraan: The nationality.
        :type KewargaNegaraan: str
        :param BerlakuHingga: The expiry date.
        :type BerlakuHingga: str
        :param IssuedDate: The issue date.
        :type IssuedDate: str
        :param Photo: The photo.
        :type Photo: str
        :param Provinsi: The province, which is supported when the value of `Scene` is `V2`.
        :type Provinsi: str
        :param Kota: The city, which is supported when the value of `Scene` is `V2`.
        :type Kota: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NIK = None
        self.Nama = None
        self.TempatTglLahir = None
        self.JenisKelamin = None
        self.GolDarah = None
        self.Alamat = None
        self.RTRW = None
        self.KelDesa = None
        self.Kecamatan = None
        self.Agama = None
        self.StatusPerkawinan = None
        self.Perkerjaan = None
        self.KewargaNegaraan = None
        self.BerlakuHingga = None
        self.IssuedDate = None
        self.Photo = None
        self.Provinsi = None
        self.Kota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NIK = params.get("NIK")
        self.Nama = params.get("Nama")
        self.TempatTglLahir = params.get("TempatTglLahir")
        self.JenisKelamin = params.get("JenisKelamin")
        self.GolDarah = params.get("GolDarah")
        self.Alamat = params.get("Alamat")
        self.RTRW = params.get("RTRW")
        self.KelDesa = params.get("KelDesa")
        self.Kecamatan = params.get("Kecamatan")
        self.Agama = params.get("Agama")
        self.StatusPerkawinan = params.get("StatusPerkawinan")
        self.Perkerjaan = params.get("Perkerjaan")
        self.KewargaNegaraan = params.get("KewargaNegaraan")
        self.BerlakuHingga = params.get("BerlakuHingga")
        self.IssuedDate = params.get("IssuedDate")
        self.Photo = params.get("Photo")
        self.Provinsi = params.get("Provinsi")
        self.Kota = params.get("Kota")
        self.RequestId = params.get("RequestId")


class RecognizeKoreanDrivingLicenseOCRRequest(AbstractModel):
    """RecognizeKoreanDrivingLicenseOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeKoreanDrivingLicenseOCRResponse(AbstractModel):
    """RecognizeKoreanDrivingLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param ID: The ID card number.
        :type ID: str
        :param LicenseNumber: The license number.
        :type LicenseNumber: str
        :param Number: The resident registration number.
        :type Number: str
        :param Type: The license class type.
        :type Type: str
        :param Address: The address.
        :type Address: str
        :param Name: The name.
        :type Name: str
        :param AptitudeTesDate: The renewal period.
        :type AptitudeTesDate: str
        :param DateOfIssue: The issue date.
        :type DateOfIssue: str
        :param Photo: The Base64-encoded identity photo.
        :type Photo: str
        :param Sex: The gender.
        :type Sex: str
        :param Birthday: The birth date in the format of dd/mm/yyyy.
        :type Birthday: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.LicenseNumber = None
        self.Number = None
        self.Type = None
        self.Address = None
        self.Name = None
        self.AptitudeTesDate = None
        self.DateOfIssue = None
        self.Photo = None
        self.Sex = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.LicenseNumber = params.get("LicenseNumber")
        self.Number = params.get("Number")
        self.Type = params.get("Type")
        self.Address = params.get("Address")
        self.Name = params.get("Name")
        self.AptitudeTesDate = params.get("AptitudeTesDate")
        self.DateOfIssue = params.get("DateOfIssue")
        self.Photo = params.get("Photo")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class RecognizeKoreanIDCardOCRRequest(AbstractModel):
    """RecognizeKoreanIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeKoreanIDCardOCRResponse(AbstractModel):
    """RecognizeKoreanIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param ID: The ID card number.
        :type ID: str
        :param Address: The address.
        :type Address: str
        :param Name: The name.
        :type Name: str
        :param DateOfIssue: The issue date.
        :type DateOfIssue: str
        :param Photo: The Base64-encoded identity photo.
        :type Photo: str
        :param Sex: The gender.
        :type Sex: str
        :param Birthday: The birth date in the format of dd/mm/yyyy.
        :type Birthday: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Address = None
        self.Name = None
        self.DateOfIssue = None
        self.Photo = None
        self.Sex = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Address = params.get("Address")
        self.Name = params.get("Name")
        self.DateOfIssue = params.get("DateOfIssue")
        self.Photo = params.get("Photo")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesDrivingLicenseOCRRequest(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesDrivingLicenseOCRResponse(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Name: The full name.
        :type Name: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LastName: The last name.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FirstName: The first name.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param MiddleName: The middle name.
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Nationality: The nationality.
        :type Nationality: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Sex: The gender.
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LicenseNo: The license No.
        :type LicenseNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param ExpiresDate: The expiration date.
        :type ExpiresDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param AgencyCode: The agency code.
        :type AgencyCode: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.Name = None
        self.LastName = None
        self.FirstName = None
        self.MiddleName = None
        self.Nationality = None
        self.Sex = None
        self.Address = None
        self.LicenseNo = None
        self.ExpiresDate = None
        self.AgencyCode = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("Name") is not None:
            self.Name = TextDetectionResult()
            self.Name._deserialize(params.get("Name"))
        if params.get("LastName") is not None:
            self.LastName = TextDetectionResult()
            self.LastName._deserialize(params.get("LastName"))
        if params.get("FirstName") is not None:
            self.FirstName = TextDetectionResult()
            self.FirstName._deserialize(params.get("FirstName"))
        if params.get("MiddleName") is not None:
            self.MiddleName = TextDetectionResult()
            self.MiddleName._deserialize(params.get("MiddleName"))
        if params.get("Nationality") is not None:
            self.Nationality = TextDetectionResult()
            self.Nationality._deserialize(params.get("Nationality"))
        if params.get("Sex") is not None:
            self.Sex = TextDetectionResult()
            self.Sex._deserialize(params.get("Sex"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("LicenseNo") is not None:
            self.LicenseNo = TextDetectionResult()
            self.LicenseNo._deserialize(params.get("LicenseNo"))
        if params.get("ExpiresDate") is not None:
            self.ExpiresDate = TextDetectionResult()
            self.ExpiresDate._deserialize(params.get("ExpiresDate"))
        if params.get("AgencyCode") is not None:
            self.AgencyCode = TextDetectionResult()
            self.AgencyCode._deserialize(params.get("AgencyCode"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesSssIDOCRRequest(AbstractModel):
    """RecognizePhilippinesSssIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesSssIDOCRResponse(AbstractModel):
    """RecognizePhilippinesSssIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LicenseNumber: The common reference number (CRN).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FullName: The full name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.LicenseNumber = None
        self.FullName = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self.LicenseNumber = TextDetectionResult()
            self.LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self.FullName = TextDetectionResult()
            self.FullName._deserialize(params.get("FullName"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesTinIDOCRRequest(AbstractModel):
    """RecognizePhilippinesTinIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesTinIDOCRResponse(AbstractModel):
    """RecognizePhilippinesTinIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LicenseNumber: The tax identification number (TIN).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FullName: The name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: The birth date.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param IssueDate: The issue date.
        :type IssueDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.LicenseNumber = None
        self.FullName = None
        self.Address = None
        self.Birthday = None
        self.IssueDate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self.LicenseNumber = TextDetectionResult()
            self.LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self.FullName = TextDetectionResult()
            self.FullName._deserialize(params.get("FullName"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        if params.get("IssueDate") is not None:
            self.IssueDate = TextDetectionResult()
            self.IssueDate._deserialize(params.get("IssueDate"))
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesUMIDOCRRequest(AbstractModel):
    """RecognizePhilippinesUMIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesUMIDOCRResponse(AbstractModel):
    """RecognizePhilippinesUMIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param Surname: The surname.
        :type Surname: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param MiddleName: The middle name.
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param GivenName: The given name.
        :type GivenName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param CRN: The common reference number (CRN).
        :type CRN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Sex: The gender.
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Surname = None
        self.MiddleName = None
        self.GivenName = None
        self.Address = None
        self.Birthday = None
        self.CRN = None
        self.Sex = None
        self.HeadPortrait = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Surname") is not None:
            self.Surname = TextDetectionResult()
            self.Surname._deserialize(params.get("Surname"))
        if params.get("MiddleName") is not None:
            self.MiddleName = TextDetectionResult()
            self.MiddleName._deserialize(params.get("MiddleName"))
        if params.get("GivenName") is not None:
            self.GivenName = TextDetectionResult()
            self.GivenName._deserialize(params.get("GivenName"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        if params.get("CRN") is not None:
            self.CRN = TextDetectionResult()
            self.CRN._deserialize(params.get("CRN"))
        if params.get("Sex") is not None:
            self.Sex = TextDetectionResult()
            self.Sex._deserialize(params.get("Sex"))
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesVoteIDOCRRequest(AbstractModel):
    """RecognizePhilippinesVoteIDOCR request structure.

    """

    def __init__(self):
        r"""
        :param ReturnHeadImage: Whether to return the identity photo.
        :type ReturnHeadImage: bool
        :param ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be affected.
        :type ImageUrl: str
        """
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesVoteIDOCRResponse(AbstractModel):
    """RecognizePhilippinesVoteIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param VIN: The voter's identification number (VIN).
        :type VIN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FirstName: The first name.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LastName: The last name.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param CivilStatus: The civil status.
        :type CivilStatus: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Citizenship: The citizenship.
        :type Citizenship: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param PrecinctNo: The precinct.
        :type PrecinctNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.VIN = None
        self.FirstName = None
        self.LastName = None
        self.Birthday = None
        self.CivilStatus = None
        self.Citizenship = None
        self.Address = None
        self.PrecinctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("VIN") is not None:
            self.VIN = TextDetectionResult()
            self.VIN._deserialize(params.get("VIN"))
        if params.get("FirstName") is not None:
            self.FirstName = TextDetectionResult()
            self.FirstName._deserialize(params.get("FirstName"))
        if params.get("LastName") is not None:
            self.LastName = TextDetectionResult()
            self.LastName._deserialize(params.get("LastName"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        if params.get("CivilStatus") is not None:
            self.CivilStatus = TextDetectionResult()
            self.CivilStatus._deserialize(params.get("CivilStatus"))
        if params.get("Citizenship") is not None:
            self.Citizenship = TextDetectionResult()
            self.Citizenship._deserialize(params.get("Citizenship"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("PrecinctNo") is not None:
            self.PrecinctNo = TextDetectionResult()
            self.PrecinctNo._deserialize(params.get("PrecinctNo"))
        self.RequestId = params.get("RequestId")


class RecognizeTableAccurateOCRRequest(AbstractModel):
    """RecognizeTableAccurateOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image.
The image cannot exceed 7 MB after being Base64-encoded. A resolution above 600 x 800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
Supported image pixels: 20 to 10,000
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image or PDF file.
The image or PDF file cannot exceed 7 MB after being Base64-encoded. A resolution above 600 x 800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
Supported image pixels: 20 to 10,000
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `IsPdf` is `true`. Default value: `1`.
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTableAccurateOCRResponse(AbstractModel):
    """RecognizeTableAccurateOCR response structure.

    """

    def __init__(self):
        r"""
        :param TableDetections: The recognized text information. Please click the link on the left for details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableDetections: list of TableInfo
        :param Data: Base64-encoded Excel data.
        :type Data: str
        :param PdfPageSize: The total number of pages in the PDF file.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PdfPageSize: int
        :param Angle: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a negative value: rotate counterclockwise. Value range: -360° to 0°.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Angle: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TableDetections = None
        self.Data = None
        self.PdfPageSize = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TableDetections") is not None:
            self.TableDetections = []
            for item in params.get("TableDetections"):
                obj = TableInfo()
                obj._deserialize(item)
                self.TableDetections.append(obj)
        self.Data = params.get("Data")
        self.PdfPageSize = params.get("PdfPageSize")
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class RecognizeThaiIDCardOCRRequest(AbstractModel):
    """RecognizeThaiIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        :param CropPortrait: Whether to crop the profile photo. The default value is `false`, meaning not to return the Base64-encoded value of the profile photo on the Thai identity card.
When this parameter is set to `true`, the Base64-encoded value of the profile photo on the Thai identity card after rotation correction is returned.
        :type CropPortrait: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CropPortrait = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CropPortrait = params.get("CropPortrait")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeThaiIDCardOCRResponse(AbstractModel):
    """RecognizeThaiIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param ID: ID card number
        :type ID: str
        :param ThaiName: Name in Thai
        :type ThaiName: str
        :param EnFirstName: Name in English
        :type EnFirstName: str
        :param Address: Address
        :type Address: str
        :param Birthday: Date of birth
        :type Birthday: str
        :param IssueDate: Date of issue
        :type IssueDate: str
        :param ExpirationDate: Expiration date
        :type ExpirationDate: str
        :param EnLastName: Name in English
        :type EnLastName: str
        :param PortraitImage: Identity photo
        :type PortraitImage: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.ThaiName = None
        self.EnFirstName = None
        self.Address = None
        self.Birthday = None
        self.IssueDate = None
        self.ExpirationDate = None
        self.EnLastName = None
        self.PortraitImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ThaiName = params.get("ThaiName")
        self.EnFirstName = params.get("EnFirstName")
        self.Address = params.get("Address")
        self.Birthday = params.get("Birthday")
        self.IssueDate = params.get("IssueDate")
        self.ExpirationDate = params.get("ExpirationDate")
        self.EnLastName = params.get("EnLastName")
        self.PortraitImage = params.get("PortraitImage")
        self.RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """Coordinates

    """

    def __init__(self):
        r"""
        :param X: X-coordinate of top-left point
        :type X: int
        :param Y: Y-coordinate of top-left point
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
        


class SealInfo(AbstractModel):
    """Seal information

    """

    def __init__(self):
        r"""
        :param SealBody: Seal body information
        :type SealBody: str
        :param Location: Seal coordinates
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param OtherTexts: Other text content
        :type OtherTexts: list of str
        :param SealShape: Seal shape. Valid values:
0: Round
1: Oval
2: Rectangle
3: Diamond
4: Triangle
        :type SealShape: str
        """
        self.SealBody = None
        self.Location = None
        self.OtherTexts = None
        self.SealShape = None


    def _deserialize(self, params):
        self.SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        self.OtherTexts = params.get("OtherTexts")
        self.SealShape = params.get("SealShape")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRRequest(AbstractModel):
    """SealOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
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
        


class SealOCRResponse(AbstractModel):
    """SealOCR response structure.

    """

    def __init__(self):
        r"""
        :param SealBody: Seal content
        :type SealBody: str
        :param Location: Seal coordinates
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param OtherTexts: Other text content
        :type OtherTexts: list of str
        :param SealInfos: All seal information
        :type SealInfos: list of SealInfo
        :param SealShape: Seal shape. Valid values:
0: Round
1: Oval
2: Rectangle
3: Diamond
4: Triangle
        :type SealShape: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SealBody = None
        self.Location = None
        self.OtherTexts = None
        self.SealInfos = None
        self.SealShape = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        self.OtherTexts = params.get("OtherTexts")
        if params.get("SealInfos") is not None:
            self.SealInfos = []
            for item in params.get("SealInfos"):
                obj = SealInfo()
                obj._deserialize(item)
                self.SealInfos.append(obj)
        self.SealShape = params.get("SealShape")
        self.RequestId = params.get("RequestId")


class ShippingInvoice(AbstractModel):
    """Ship ticket

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param UserName: Name
        :type UserName: str
        :param Date: Date
        :type Date: str
        :param Time: Time
        :type Time: str
        :param StationGetOn: Departure station
        :type StationGetOn: str
        :param StationGetOff: Destination
        :type StationGetOff: str
        :param Total: Fare
        :type Total: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param CurrencyCode: Currency
        :type CurrencyCode: str
        """
        self.Title = None
        self.QRCodeMark = None
        self.Code = None
        self.Number = None
        self.UserName = None
        self.Date = None
        self.Time = None
        self.StationGetOn = None
        self.StationGetOff = None
        self.Total = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.CurrencyCode = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.QRCodeMark = params.get("QRCodeMark")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.UserName = params.get("UserName")
        self.Date = params.get("Date")
        self.Time = params.get("Time")
        self.StationGetOn = params.get("StationGetOn")
        self.StationGetOff = params.get("StationGetOff")
        self.Total = params.get("Total")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.CurrencyCode = params.get("CurrencyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleInvoiceItem(AbstractModel):
    """Content of a single invoice/ticket among multiple types of invoices/tickets

    """

    def __init__(self):
        r"""
        :param VatSpecialInvoice: Special VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatCommonInvoice: General VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatElectronicCommonInvoice: Electronic general VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatElectronicSpecialInvoice: Electronic special VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatElectronicInvoiceBlockchain: Blockchain electronic invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceBlockchain: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatElectronicInvoiceToll: Electronic general VAT invoice (toll)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceToll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param VatElectronicSpecialInvoiceFull: Electronic invoice (special)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicSpecialInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param VatElectronicInvoiceFull: Electronic invoice (general)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param MachinePrintedInvoice: General machine-printed invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type MachinePrintedInvoice: :class:`tencentcloud.ocr.v20181119.models.MachinePrintedInvoice`
        :param BusInvoice: Bus ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusInvoice: :class:`tencentcloud.ocr.v20181119.models.BusInvoice`
        :param ShippingInvoice: Ship ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShippingInvoice: :class:`tencentcloud.ocr.v20181119.models.ShippingInvoice`
        :param TollInvoice: Toll receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type TollInvoice: :class:`tencentcloud.ocr.v20181119.models.TollInvoice`
        :param OtherInvoice: Other invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type OtherInvoice: :class:`tencentcloud.ocr.v20181119.models.OtherInvoice`
        :param MotorVehicleSaleInvoice: Motor vehicle sales invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type MotorVehicleSaleInvoice: :class:`tencentcloud.ocr.v20181119.models.MotorVehicleSaleInvoice`
        :param UsedCarPurchaseInvoice: Used car invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsedCarPurchaseInvoice: :class:`tencentcloud.ocr.v20181119.models.UsedCarPurchaseInvoice`
        :param VatInvoiceRoll: General VAT invoice (roll)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatInvoiceRoll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceRoll`
        :param TaxiTicket: Taxi receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaxiTicket: :class:`tencentcloud.ocr.v20181119.models.TaxiTicket`
        :param QuotaInvoice: Quota invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type QuotaInvoice: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoice`
        :param AirTransport: Itinerary/Receipt of e-ticket for air transportation
Note: This field may return null, indicating that no valid values can be obtained.
        :type AirTransport: :class:`tencentcloud.ocr.v20181119.models.AirTransport`
        :param NonTaxIncomeGeneralBill: Non-tax revenue general receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonTaxIncomeGeneralBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param NonTaxIncomeElectronicBill: Non-tax revenue unified payment voucher
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonTaxIncomeElectronicBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param TrainTicket: Train ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrainTicket: :class:`tencentcloud.ocr.v20181119.models.TrainTicket`
        :param MedicalOutpatientInvoice: 
        :type MedicalOutpatientInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        :param MedicalHospitalizedInvoice: 
        :type MedicalHospitalizedInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        """
        self.VatSpecialInvoice = None
        self.VatCommonInvoice = None
        self.VatElectronicCommonInvoice = None
        self.VatElectronicSpecialInvoice = None
        self.VatElectronicInvoiceBlockchain = None
        self.VatElectronicInvoiceToll = None
        self.VatElectronicSpecialInvoiceFull = None
        self.VatElectronicInvoiceFull = None
        self.MachinePrintedInvoice = None
        self.BusInvoice = None
        self.ShippingInvoice = None
        self.TollInvoice = None
        self.OtherInvoice = None
        self.MotorVehicleSaleInvoice = None
        self.UsedCarPurchaseInvoice = None
        self.VatInvoiceRoll = None
        self.TaxiTicket = None
        self.QuotaInvoice = None
        self.AirTransport = None
        self.NonTaxIncomeGeneralBill = None
        self.NonTaxIncomeElectronicBill = None
        self.TrainTicket = None
        self.MedicalOutpatientInvoice = None
        self.MedicalHospitalizedInvoice = None


    def _deserialize(self, params):
        if params.get("VatSpecialInvoice") is not None:
            self.VatSpecialInvoice = VatInvoiceInfo()
            self.VatSpecialInvoice._deserialize(params.get("VatSpecialInvoice"))
        if params.get("VatCommonInvoice") is not None:
            self.VatCommonInvoice = VatInvoiceInfo()
            self.VatCommonInvoice._deserialize(params.get("VatCommonInvoice"))
        if params.get("VatElectronicCommonInvoice") is not None:
            self.VatElectronicCommonInvoice = VatInvoiceInfo()
            self.VatElectronicCommonInvoice._deserialize(params.get("VatElectronicCommonInvoice"))
        if params.get("VatElectronicSpecialInvoice") is not None:
            self.VatElectronicSpecialInvoice = VatInvoiceInfo()
            self.VatElectronicSpecialInvoice._deserialize(params.get("VatElectronicSpecialInvoice"))
        if params.get("VatElectronicInvoiceBlockchain") is not None:
            self.VatElectronicInvoiceBlockchain = VatInvoiceInfo()
            self.VatElectronicInvoiceBlockchain._deserialize(params.get("VatElectronicInvoiceBlockchain"))
        if params.get("VatElectronicInvoiceToll") is not None:
            self.VatElectronicInvoiceToll = VatInvoiceInfo()
            self.VatElectronicInvoiceToll._deserialize(params.get("VatElectronicInvoiceToll"))
        if params.get("VatElectronicSpecialInvoiceFull") is not None:
            self.VatElectronicSpecialInvoiceFull = VatElectronicInfo()
            self.VatElectronicSpecialInvoiceFull._deserialize(params.get("VatElectronicSpecialInvoiceFull"))
        if params.get("VatElectronicInvoiceFull") is not None:
            self.VatElectronicInvoiceFull = VatElectronicInfo()
            self.VatElectronicInvoiceFull._deserialize(params.get("VatElectronicInvoiceFull"))
        if params.get("MachinePrintedInvoice") is not None:
            self.MachinePrintedInvoice = MachinePrintedInvoice()
            self.MachinePrintedInvoice._deserialize(params.get("MachinePrintedInvoice"))
        if params.get("BusInvoice") is not None:
            self.BusInvoice = BusInvoice()
            self.BusInvoice._deserialize(params.get("BusInvoice"))
        if params.get("ShippingInvoice") is not None:
            self.ShippingInvoice = ShippingInvoice()
            self.ShippingInvoice._deserialize(params.get("ShippingInvoice"))
        if params.get("TollInvoice") is not None:
            self.TollInvoice = TollInvoice()
            self.TollInvoice._deserialize(params.get("TollInvoice"))
        if params.get("OtherInvoice") is not None:
            self.OtherInvoice = OtherInvoice()
            self.OtherInvoice._deserialize(params.get("OtherInvoice"))
        if params.get("MotorVehicleSaleInvoice") is not None:
            self.MotorVehicleSaleInvoice = MotorVehicleSaleInvoice()
            self.MotorVehicleSaleInvoice._deserialize(params.get("MotorVehicleSaleInvoice"))
        if params.get("UsedCarPurchaseInvoice") is not None:
            self.UsedCarPurchaseInvoice = UsedCarPurchaseInvoice()
            self.UsedCarPurchaseInvoice._deserialize(params.get("UsedCarPurchaseInvoice"))
        if params.get("VatInvoiceRoll") is not None:
            self.VatInvoiceRoll = VatInvoiceRoll()
            self.VatInvoiceRoll._deserialize(params.get("VatInvoiceRoll"))
        if params.get("TaxiTicket") is not None:
            self.TaxiTicket = TaxiTicket()
            self.TaxiTicket._deserialize(params.get("TaxiTicket"))
        if params.get("QuotaInvoice") is not None:
            self.QuotaInvoice = QuotaInvoice()
            self.QuotaInvoice._deserialize(params.get("QuotaInvoice"))
        if params.get("AirTransport") is not None:
            self.AirTransport = AirTransport()
            self.AirTransport._deserialize(params.get("AirTransport"))
        if params.get("NonTaxIncomeGeneralBill") is not None:
            self.NonTaxIncomeGeneralBill = NonTaxIncomeBill()
            self.NonTaxIncomeGeneralBill._deserialize(params.get("NonTaxIncomeGeneralBill"))
        if params.get("NonTaxIncomeElectronicBill") is not None:
            self.NonTaxIncomeElectronicBill = NonTaxIncomeBill()
            self.NonTaxIncomeElectronicBill._deserialize(params.get("NonTaxIncomeElectronicBill"))
        if params.get("TrainTicket") is not None:
            self.TrainTicket = TrainTicket()
            self.TrainTicket._deserialize(params.get("TrainTicket"))
        if params.get("MedicalOutpatientInvoice") is not None:
            self.MedicalOutpatientInvoice = MedicalInvoice()
            self.MedicalOutpatientInvoice._deserialize(params.get("MedicalOutpatientInvoice"))
        if params.get("MedicalHospitalizedInvoice") is not None:
            self.MedicalHospitalizedInvoice = MedicalInvoice()
            self.MedicalHospitalizedInvoice._deserialize(params.get("MedicalHospitalizedInvoice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRV2Request(AbstractModel):
    """SmartStructuralOCRV2 request structure.

    """

    def __init__(self):
        r"""
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param IsPdf: Whether to enable PDF recognition. Default value: `false`. If you enable this feature, both images and PDF files can be recognized.
        :type IsPdf: bool
        :param PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `IsPdf` is `true`. Default value: `1`.
        :type PdfPageNumber: int
        :param ItemNames: The names of the fields you want to return for the structured information recognition.
For example, if you want to return only the recognition result of the "Name" and "Gender" fields, set this parameter as follows:
ItemNames=["Name","Gender"]
        :type ItemNames: list of str
        :param ReturnFullText: Whether to enable recognition of all fields.
        :type ReturnFullText: bool
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.IsPdf = None
        self.PdfPageNumber = None
        self.ItemNames = None
        self.ReturnFullText = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.ItemNames = params.get("ItemNames")
        self.ReturnFullText = params.get("ReturnFullText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRV2Response(AbstractModel):
    """SmartStructuralOCRV2 response structure.

    """

    def __init__(self):
        r"""
        :param Angle: The rotation angle (degrees) of the text on the image. 0: The text is horizontal. Positive value: The text is rotated clockwise. Negative value: The text is rotated counterclockwise.
        :type Angle: float
        :param StructuralList: The structural information (key-value).
        :type StructuralList: list of GroupInfo
        :param WordList: The recognized text information.
        :type WordList: list of WordItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Angle = None
        self.StructuralList = None
        self.WordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        if params.get("StructuralList") is not None:
            self.StructuralList = []
            for item in params.get("StructuralList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.StructuralList.append(obj)
        if params.get("WordList") is not None:
            self.WordList = []
            for item in params.get("WordList"):
                obj = WordItem()
                obj._deserialize(item)
                self.WordList.append(obj)
        self.RequestId = params.get("RequestId")


class TableCellInfo(AbstractModel):
    """Cell data

    """

    def __init__(self):
        r"""
        :param ColTl: Column index of the upper-left corner of the cell
        :type ColTl: int
        :param RowTl: Row index of the upper-left corner of the cell
        :type RowTl: int
        :param ColBr: Column index of the lower-right corner of the cell
        :type ColBr: int
        :param RowBr: Row index of the lower-right corner of the cell
        :type RowBr: int
        :param Text: Recognized string text within the cell. If there are multiple lines, they are separated by "\n".
        :type Text: str
        :param Type: Cell type
        :type Type: str
        :param Confidence: Cell confidence
        :type Confidence: float
        :param Polygon: Four-point coordinates of the cell in the image
        :type Polygon: list of Coord
        """
        self.ColTl = None
        self.RowTl = None
        self.ColBr = None
        self.RowBr = None
        self.Text = None
        self.Type = None
        self.Confidence = None
        self.Polygon = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfo(AbstractModel):
    """Recognized table information

    """

    def __init__(self):
        r"""
        :param Cells: Cell content
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Cells: list of TableCellInfo
        :param Type: Type of text in the image. Valid values:
0: Non-table text
1: Text in a bordered table
2: Text in a borderless table
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Type: int
        :param TableCoordPoint: The coordinates of the four vertices (upper-left, upper-right, lower-right, and lower-left) of the table body.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableCoordPoint: list of Coord
        """
        self.Cells = None
        self.Type = None
        self.TableCoordPoint = None


    def _deserialize(self, params):
        if params.get("Cells") is not None:
            self.Cells = []
            for item in params.get("Cells"):
                obj = TableCellInfo()
                obj._deserialize(item)
                self.Cells.append(obj)
        self.Type = params.get("Type")
        if params.get("TableCoordPoint") is not None:
            self.TableCoordPoint = []
            for item in params.get("TableCoordPoint"):
                obj = Coord()
                obj._deserialize(item)
                self.TableCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class TaxiTicket(AbstractModel):
    """Taxi receipt

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Date: Date of issue
        :type Date: str
        :param TimeGetOn: Start time
        :type TimeGetOn: str
        :param TimeGetOff: End time
        :type TimeGetOff: str
        :param Price: Unit price
        :type Price: str
        :param Mileage: Distance
        :type Mileage: str
        :param Total: Total amount
        :type Total: str
        :param Place: Invoice place
        :type Place: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param Kind: Invoice type
        :type Kind: str
        :param LicensePlate: License plate number
        :type LicensePlate: str
        :param FuelFee: Fuel surcharge
        :type FuelFee: str
        :param BookingCallFee: Booking fee
        :type BookingCallFee: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self.Title = None
        self.QRCodeMark = None
        self.Code = None
        self.Number = None
        self.Date = None
        self.TimeGetOn = None
        self.TimeGetOff = None
        self.Price = None
        self.Mileage = None
        self.Total = None
        self.Place = None
        self.Province = None
        self.City = None
        self.Kind = None
        self.LicensePlate = None
        self.FuelFee = None
        self.BookingCallFee = None
        self.CompanySealMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.QRCodeMark = params.get("QRCodeMark")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.TimeGetOn = params.get("TimeGetOn")
        self.TimeGetOff = params.get("TimeGetOff")
        self.Price = params.get("Price")
        self.Mileage = params.get("Mileage")
        self.Total = params.get("Total")
        self.Place = params.get("Place")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Kind = params.get("Kind")
        self.LicensePlate = params.get("LicensePlate")
        self.FuelFee = params.get("FuelFee")
        self.BookingCallFee = params.get("BookingCallFee")
        self.CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class TextDetectionResult(AbstractModel):
    """Recognition result

    """

    def __init__(self):
        r"""
        :param Value: The recognized text line content.
        :type Value: str
        :param Polygon: The coordinates, represented in the coordinates of the four points.
        :type Polygon: list of Coord
        """
        self.Value = None
        self.Polygon = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
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
        


class TollInvoice(AbstractModel):
    """Toll receipt

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param Kind: Invoice type
        :type Kind: str
        :param Date: Date
        :type Date: str
        :param Time: Time
        :type Time: str
        :param Entrance: Entrance
        :type Entrance: str
        :param Exit: Exit
        :type Exit: str
        :param HighwayMark: Highway mark (0: No, 1: Yes)
        :type HighwayMark: int
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        """
        self.Title = None
        self.Code = None
        self.Number = None
        self.Total = None
        self.Kind = None
        self.Date = None
        self.Time = None
        self.Entrance = None
        self.Exit = None
        self.HighwayMark = None
        self.QRCodeMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Total = params.get("Total")
        self.Kind = params.get("Kind")
        self.Date = params.get("Date")
        self.Time = params.get("Time")
        self.Entrance = params.get("Entrance")
        self.Exit = params.get("Exit")
        self.HighwayMark = params.get("HighwayMark")
        self.QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainTicket(AbstractModel):
    """Train ticket

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Number: Invoice number
        :type Number: str
        :param DateGetOn: Departure date
        :type DateGetOn: str
        :param TimeGetOn: Departure time
        :type TimeGetOn: str
        :param Name: Passenger's name
        :type Name: str
        :param StationGetOn: Departure station
        :type StationGetOn: str
        :param StationGetOff: Destination
        :type StationGetOff: str
        :param Seat: Seat class
        :type Seat: str
        :param Total: Total amount
        :type Total: str
        :param Kind: Invoice type
        :type Kind: str
        :param SerialNumber: Serial number
        :type SerialNumber: str
        :param UserID: ID card number
        :type UserID: str
        :param GateNumber: Check-in gate
        :type GateNumber: str
        :param TrainNumber: Fleet number
        :type TrainNumber: str
        :param HandlingFee: Handling fee
        :type HandlingFee: str
        :param OriginalFare: Original ticket price
        :type OriginalFare: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param SeatNumber: Seat No.
        :type SeatNumber: str
        :param PickUpAddress: Ticket pickup address
        :type PickUpAddress: str
        :param TicketChange: Ticket change information
        :type TicketChange: str
        :param AdditionalFare: Additional fare
        :type AdditionalFare: str
        :param ReceiptNumber: Receipt No.
        :type ReceiptNumber: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param ReimburseOnlyMark: Whether it is for reimbursement only (0: No, 1: Yes)
        :type ReimburseOnlyMark: int
        """
        self.Title = None
        self.Number = None
        self.DateGetOn = None
        self.TimeGetOn = None
        self.Name = None
        self.StationGetOn = None
        self.StationGetOff = None
        self.Seat = None
        self.Total = None
        self.Kind = None
        self.SerialNumber = None
        self.UserID = None
        self.GateNumber = None
        self.TrainNumber = None
        self.HandlingFee = None
        self.OriginalFare = None
        self.TotalCn = None
        self.SeatNumber = None
        self.PickUpAddress = None
        self.TicketChange = None
        self.AdditionalFare = None
        self.ReceiptNumber = None
        self.QRCodeMark = None
        self.ReimburseOnlyMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Number = params.get("Number")
        self.DateGetOn = params.get("DateGetOn")
        self.TimeGetOn = params.get("TimeGetOn")
        self.Name = params.get("Name")
        self.StationGetOn = params.get("StationGetOn")
        self.StationGetOff = params.get("StationGetOff")
        self.Seat = params.get("Seat")
        self.Total = params.get("Total")
        self.Kind = params.get("Kind")
        self.SerialNumber = params.get("SerialNumber")
        self.UserID = params.get("UserID")
        self.GateNumber = params.get("GateNumber")
        self.TrainNumber = params.get("TrainNumber")
        self.HandlingFee = params.get("HandlingFee")
        self.OriginalFare = params.get("OriginalFare")
        self.TotalCn = params.get("TotalCn")
        self.SeatNumber = params.get("SeatNumber")
        self.PickUpAddress = params.get("PickUpAddress")
        self.TicketChange = params.get("TicketChange")
        self.AdditionalFare = params.get("AdditionalFare")
        self.ReceiptNumber = params.get("ReceiptNumber")
        self.QRCodeMark = params.get("QRCodeMark")
        self.ReimburseOnlyMark = params.get("ReimburseOnlyMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsedCarPurchaseInvoice(AbstractModel):
    """Used car sales invoice

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param Date: Date of issue
        :type Date: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTel: Seller's phone number
        :type SellerTel: str
        :param SellerTaxID: Seller's company code/personal ID card number
        :type SellerTaxID: str
        :param SellerAddress: Seller's address
        :type SellerAddress: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerID: Buyer's company code/personal ID card number
        :type BuyerID: str
        :param BuyerAddress: Buyer's address
        :type BuyerAddress: str
        :param BuyerTel: Buyer's phone number
        :type BuyerTel: str
        :param CompanyName: Company (used car market) name
        :type CompanyName: str
        :param CompanyTaxID: Company's taxpayer identification number
        :type CompanyTaxID: str
        :param CompanyBankAccount: Company's account opening bank and account number
        :type CompanyBankAccount: str
        :param CompanyTel: Company's phone number
        :type CompanyTel: str
        :param CompanyAddress: Company's address
        :type CompanyAddress: str
        :param TransferAdministrationName: Name of the transfer-to department of motor vehicles
        :type TransferAdministrationName: str
        :param LicensePlate: License plate number
        :type LicensePlate: str
        :param RegistrationNumber: Registration certificate No.
        :type RegistrationNumber: str
        :param VIN: VIN
        :type VIN: str
        :param VehicleModel: Vehicle model
        :type VehicleModel: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param VehicleType: Vehicle type
        :type VehicleType: str
        :param Remark: Remarks
        :type Remark: str
        :param FormType: Form type
        :type FormType: str
        :param FormName: Form name
        :type FormName: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self.Title = None
        self.QRCodeMark = None
        self.Code = None
        self.Number = None
        self.Date = None
        self.Total = None
        self.TotalCn = None
        self.Seller = None
        self.SellerTel = None
        self.SellerTaxID = None
        self.SellerAddress = None
        self.Buyer = None
        self.BuyerID = None
        self.BuyerAddress = None
        self.BuyerTel = None
        self.CompanyName = None
        self.CompanyTaxID = None
        self.CompanyBankAccount = None
        self.CompanyTel = None
        self.CompanyAddress = None
        self.TransferAdministrationName = None
        self.LicensePlate = None
        self.RegistrationNumber = None
        self.VIN = None
        self.VehicleModel = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.VehicleType = None
        self.Remark = None
        self.FormType = None
        self.FormName = None
        self.CompanySealMark = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.QRCodeMark = params.get("QRCodeMark")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Seller = params.get("Seller")
        self.SellerTel = params.get("SellerTel")
        self.SellerTaxID = params.get("SellerTaxID")
        self.SellerAddress = params.get("SellerAddress")
        self.Buyer = params.get("Buyer")
        self.BuyerID = params.get("BuyerID")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerTel = params.get("BuyerTel")
        self.CompanyName = params.get("CompanyName")
        self.CompanyTaxID = params.get("CompanyTaxID")
        self.CompanyBankAccount = params.get("CompanyBankAccount")
        self.CompanyTel = params.get("CompanyTel")
        self.CompanyAddress = params.get("CompanyAddress")
        self.TransferAdministrationName = params.get("TransferAdministrationName")
        self.LicensePlate = params.get("LicensePlate")
        self.RegistrationNumber = params.get("RegistrationNumber")
        self.VIN = params.get("VIN")
        self.VehicleModel = params.get("VehicleModel")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.VehicleType = params.get("VehicleType")
        self.Remark = params.get("Remark")
        self.FormType = params.get("FormType")
        self.FormName = params.get("FormName")
        self.CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    """Value information

    """

    def __init__(self):
        r"""
        :param AutoContent: The value of the recognized field.
        :type AutoContent: str
        :param Coord: The coordinates of the four vertices.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self.AutoContent = None
        self.Coord = None


    def _deserialize(self, params):
        self.AutoContent = params.get("AutoContent")
        if params.get("Coord") is not None:
            self.Coord = Polygon()
            self.Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatElectronicInfo(AbstractModel):
    """Return values for an electronic invoice

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Number: Invoice number
        :type Number: str
        :param Date: Date of issue
        :type Date: str
        :param PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param Tax: Tax
        :type Tax: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param Issuer: Issuer
        :type Issuer: str
        :param Remark: Remarks
        :type Remark: str
        :param SubTotal: Subtotal amount
        :type SubTotal: str
        :param SubTax: Subtotal tax
        :type SubTax: str
        :param VatElectronicItems: Detailed items of an electronic invoice
        :type VatElectronicItems: list of VatElectronicItemInfo
        """
        self.Title = None
        self.Number = None
        self.Date = None
        self.PretaxAmount = None
        self.Tax = None
        self.Total = None
        self.TotalCn = None
        self.Seller = None
        self.SellerTaxID = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.Issuer = None
        self.Remark = None
        self.SubTotal = None
        self.SubTax = None
        self.VatElectronicItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.PretaxAmount = params.get("PretaxAmount")
        self.Tax = params.get("Tax")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Seller = params.get("Seller")
        self.SellerTaxID = params.get("SellerTaxID")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.Issuer = params.get("Issuer")
        self.Remark = params.get("Remark")
        self.SubTotal = params.get("SubTotal")
        self.SubTax = params.get("SubTax")
        if params.get("VatElectronicItems") is not None:
            self.VatElectronicItems = []
            for item in params.get("VatElectronicItems"):
                obj = VatElectronicItemInfo()
                obj._deserialize(item)
                self.VatElectronicItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatElectronicItemInfo(AbstractModel):
    """Detailed items of an electronic invoice

    """

    def __init__(self):
        r"""
        :param Name: Item name
        :type Name: str
        :param Quantity: Quantity
        :type Quantity: str
        :param Specification: Specification
        :type Specification: str
        :param Price: Unit price
        :type Price: str
        :param Total: Amount
        :type Total: str
        :param TaxRate: Tax rate
        :type TaxRate: str
        :param Tax: Tax amount
        :type Tax: str
        :param Unit: Unit
        :type Unit: str
        :param VehicleType: Vehicle type
        :type VehicleType: str
        :param VehicleBrand: Vehicle No.
        :type VehicleBrand: str
        :param DeparturePlace: Departure place
        :type DeparturePlace: str
        :param ArrivalPlace: Destination
        :type ArrivalPlace: str
        :param TransportItemsName: Name of the transported goods. It is returned only for a goods transport service invoice.
        :type TransportItemsName: str
        :param PlaceOfBuildingService: Location of the construction service. It is returned only for a construction invoice.
        :type PlaceOfBuildingService: str
        :param BuildingName: Name of the construction project. It is returned only for a construction invoice.
        :type BuildingName: str
        :param EstateNumber: Property or real estate ownership certificate No. It is returned only for a real estate operation and leasing service invoice.
        :type EstateNumber: str
        :param AreaUnit: Unit of area. It is returned only for a real estate operation and leasing service invoice.
        :type AreaUnit: str
        """
        self.Name = None
        self.Quantity = None
        self.Specification = None
        self.Price = None
        self.Total = None
        self.TaxRate = None
        self.Tax = None
        self.Unit = None
        self.VehicleType = None
        self.VehicleBrand = None
        self.DeparturePlace = None
        self.ArrivalPlace = None
        self.TransportItemsName = None
        self.PlaceOfBuildingService = None
        self.BuildingName = None
        self.EstateNumber = None
        self.AreaUnit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Quantity = params.get("Quantity")
        self.Specification = params.get("Specification")
        self.Price = params.get("Price")
        self.Total = params.get("Total")
        self.TaxRate = params.get("TaxRate")
        self.Tax = params.get("Tax")
        self.Unit = params.get("Unit")
        self.VehicleType = params.get("VehicleType")
        self.VehicleBrand = params.get("VehicleBrand")
        self.DeparturePlace = params.get("DeparturePlace")
        self.ArrivalPlace = params.get("ArrivalPlace")
        self.TransportItemsName = params.get("TransportItemsName")
        self.PlaceOfBuildingService = params.get("PlaceOfBuildingService")
        self.BuildingName = params.get("BuildingName")
        self.EstateNumber = params.get("EstateNumber")
        self.AreaUnit = params.get("AreaUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceInfo(AbstractModel):
    """Return values for a VAT invoice

    """

    def __init__(self):
        r"""
        :param CheckCode: Check code
        :type CheckCode: str
        :param FormType: Form type
        :type FormType: str
        :param TravelTax: Vehicle and vessel tax
        :type TravelTax: str
        :param BuyerAddrTel: Buyer's address and phone number
        :type BuyerAddrTel: str
        :param BuyerBankAccount: Buyer's bank account number
        :type BuyerBankAccount: str
        :param CompanySealContent: Company seal content
        :type CompanySealContent: str
        :param TaxSealContent: Tax authority seal content
        :type TaxSealContent: str
        :param ServiceName: Service type
        :type ServiceName: str
        :param City: City
        :type City: str
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param AgentMark: Whether there is an agent (0: No, 1: Yes)
        :type AgentMark: int
        :param TransitMark: Whether there is a toll (0: No, 1: Yes)
        :type TransitMark: int
        :param OilMark: Whether there is refined oil (0: No, 1: Yes)
        :type OilMark: int
        :param Title: Invoice title
        :type Title: str
        :param Kind: Invoice type
        :type Kind: str
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param NumberConfirm: Machine-printed invoice number
        :type NumberConfirm: str
        :param Date: Date of issue
        :type Date: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param Tax: Tax
        :type Tax: str
        :param MachineCode: Machine No.
        :type MachineCode: str
        :param Ciphertext: Ciphertext
        :type Ciphertext: str
        :param Remark: Remarks
        :type Remark: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param SellerAddrTel: Seller's address and phone number
        :type SellerAddrTel: str
        :param SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param Issuer: Issuer
        :type Issuer: str
        :param Reviewer: Reviewer
        :type Reviewer: str
        :param Province: Province
        :type Province: str
        :param VatInvoiceItemInfos: Information about VAT invoice items
        :type VatInvoiceItemInfos: list of VatInvoiceItemInfo
        :param CodeConfirm: Machine-printed invoice code
        :type CodeConfirm: str
        :param Receiptor: Payee
        :type Receiptor: str
        :param ElectronicFullMark: 
        :type ElectronicFullMark: int
        :param ElectronicFullNumber: 
        :type ElectronicFullNumber: str
        :param FormName: 
        :type FormName: str
        """
        self.CheckCode = None
        self.FormType = None
        self.TravelTax = None
        self.BuyerAddrTel = None
        self.BuyerBankAccount = None
        self.CompanySealContent = None
        self.TaxSealContent = None
        self.ServiceName = None
        self.City = None
        self.QRCodeMark = None
        self.AgentMark = None
        self.TransitMark = None
        self.OilMark = None
        self.Title = None
        self.Kind = None
        self.Code = None
        self.Number = None
        self.NumberConfirm = None
        self.Date = None
        self.Total = None
        self.TotalCn = None
        self.PretaxAmount = None
        self.Tax = None
        self.MachineCode = None
        self.Ciphertext = None
        self.Remark = None
        self.Seller = None
        self.SellerTaxID = None
        self.SellerAddrTel = None
        self.SellerBankAccount = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.CompanySealMark = None
        self.Issuer = None
        self.Reviewer = None
        self.Province = None
        self.VatInvoiceItemInfos = None
        self.CodeConfirm = None
        self.Receiptor = None
        self.ElectronicFullMark = None
        self.ElectronicFullNumber = None
        self.FormName = None


    def _deserialize(self, params):
        self.CheckCode = params.get("CheckCode")
        self.FormType = params.get("FormType")
        self.TravelTax = params.get("TravelTax")
        self.BuyerAddrTel = params.get("BuyerAddrTel")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.CompanySealContent = params.get("CompanySealContent")
        self.TaxSealContent = params.get("TaxSealContent")
        self.ServiceName = params.get("ServiceName")
        self.City = params.get("City")
        self.QRCodeMark = params.get("QRCodeMark")
        self.AgentMark = params.get("AgentMark")
        self.TransitMark = params.get("TransitMark")
        self.OilMark = params.get("OilMark")
        self.Title = params.get("Title")
        self.Kind = params.get("Kind")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.NumberConfirm = params.get("NumberConfirm")
        self.Date = params.get("Date")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.PretaxAmount = params.get("PretaxAmount")
        self.Tax = params.get("Tax")
        self.MachineCode = params.get("MachineCode")
        self.Ciphertext = params.get("Ciphertext")
        self.Remark = params.get("Remark")
        self.Seller = params.get("Seller")
        self.SellerTaxID = params.get("SellerTaxID")
        self.SellerAddrTel = params.get("SellerAddrTel")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.CompanySealMark = params.get("CompanySealMark")
        self.Issuer = params.get("Issuer")
        self.Reviewer = params.get("Reviewer")
        self.Province = params.get("Province")
        if params.get("VatInvoiceItemInfos") is not None:
            self.VatInvoiceItemInfos = []
            for item in params.get("VatInvoiceItemInfos"):
                obj = VatInvoiceItemInfo()
                obj._deserialize(item)
                self.VatInvoiceItemInfos.append(obj)
        self.CodeConfirm = params.get("CodeConfirm")
        self.Receiptor = params.get("Receiptor")
        self.ElectronicFullMark = params.get("ElectronicFullMark")
        self.ElectronicFullNumber = params.get("ElectronicFullNumber")
        self.FormName = params.get("FormName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceItemInfo(AbstractModel):
    """Information about VAT invoice items

    """

    def __init__(self):
        r"""
        :param Name: Item name
        :type Name: str
        :param Specification: Specification
        :type Specification: str
        :param Unit: Unit
        :type Unit: str
        :param Quantity: Quantity
        :type Quantity: str
        :param Price: Unit price
        :type Price: str
        :param Total: Amount
        :type Total: str
        :param TaxRate: Tax rate
        :type TaxRate: str
        :param Tax: Tax amount
        :type Tax: str
        :param DateStart: Start date
        :type DateStart: str
        :param DateEnd: End date
        :type DateEnd: str
        :param LicensePlate: License plate number
        :type LicensePlate: str
        :param VehicleType: Vehicle type
        :type VehicleType: str
        """
        self.Name = None
        self.Specification = None
        self.Unit = None
        self.Quantity = None
        self.Price = None
        self.Total = None
        self.TaxRate = None
        self.Tax = None
        self.DateStart = None
        self.DateEnd = None
        self.LicensePlate = None
        self.VehicleType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Specification = params.get("Specification")
        self.Unit = params.get("Unit")
        self.Quantity = params.get("Quantity")
        self.Price = params.get("Price")
        self.Total = params.get("Total")
        self.TaxRate = params.get("TaxRate")
        self.Tax = params.get("Tax")
        self.DateStart = params.get("DateStart")
        self.DateEnd = params.get("DateEnd")
        self.LicensePlate = params.get("LicensePlate")
        self.VehicleType = params.get("VehicleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceRoll(AbstractModel):
    """General VAT invoice (roll)

    """

    def __init__(self):
        r"""
        :param Title: Invoice title
        :type Title: str
        :param Code: Invoice code
        :type Code: str
        :param Number: Invoice number
        :type Number: str
        :param NumberConfirm: Machine-printed invoice number
        :type NumberConfirm: str
        :param Date: Date of issue
        :type Date: str
        :param CheckCode: Check code
        :type CheckCode: str
        :param Seller: Seller's name
        :type Seller: str
        :param SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param Buyer: Buyer's name
        :type Buyer: str
        :param BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param Category: Category
        :type Category: str
        :param Total: Total amount (in figures)
        :type Total: str
        :param TotalCn: Total amount (in words)
        :type TotalCn: str
        :param Kind: Invoice type
        :type Kind: str
        :param Province: Province
        :type Province: str
        :param City: City
        :type City: str
        :param CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param ServiceName: Service type
        :type ServiceName: str
        :param CompanySealContent: Company seal content
        :type CompanySealContent: str
        :param TaxSealContent: Tax authority seal content
        :type TaxSealContent: str
        :param VatRollItems: Items
        :type VatRollItems: list of VatRollItem
        """
        self.Title = None
        self.Code = None
        self.Number = None
        self.NumberConfirm = None
        self.Date = None
        self.CheckCode = None
        self.Seller = None
        self.SellerTaxID = None
        self.Buyer = None
        self.BuyerTaxID = None
        self.Category = None
        self.Total = None
        self.TotalCn = None
        self.Kind = None
        self.Province = None
        self.City = None
        self.CompanySealMark = None
        self.QRCodeMark = None
        self.ServiceName = None
        self.CompanySealContent = None
        self.TaxSealContent = None
        self.VatRollItems = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.NumberConfirm = params.get("NumberConfirm")
        self.Date = params.get("Date")
        self.CheckCode = params.get("CheckCode")
        self.Seller = params.get("Seller")
        self.SellerTaxID = params.get("SellerTaxID")
        self.Buyer = params.get("Buyer")
        self.BuyerTaxID = params.get("BuyerTaxID")
        self.Category = params.get("Category")
        self.Total = params.get("Total")
        self.TotalCn = params.get("TotalCn")
        self.Kind = params.get("Kind")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.CompanySealMark = params.get("CompanySealMark")
        self.QRCodeMark = params.get("QRCodeMark")
        self.ServiceName = params.get("ServiceName")
        self.CompanySealContent = params.get("CompanySealContent")
        self.TaxSealContent = params.get("TaxSealContent")
        if params.get("VatRollItems") is not None:
            self.VatRollItems = []
            for item in params.get("VatRollItems"):
                obj = VatRollItem()
                obj._deserialize(item)
                self.VatRollItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollItem(AbstractModel):
    """Items of a general VAT invoice (roll)

    """

    def __init__(self):
        r"""
        :param Name: Item name
        :type Name: str
        :param Quantity: Quantity
        :type Quantity: str
        :param Price: Unit price
        :type Price: str
        :param Total: Amount
        :type Total: str
        """
        self.Name = None
        self.Quantity = None
        self.Price = None
        self.Total = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Quantity = params.get("Quantity")
        self.Price = params.get("Price")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRRequest(AbstractModel):
    """VinOCR request structure.

    """

    def __init__(self):
        r"""
        :param ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
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
        


class VinOCRResponse(AbstractModel):
    """VinOCR response structure.

    """

    def __init__(self):
        r"""
        :param Vin: The detected VIN.
        :type Vin: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Vin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vin = params.get("Vin")
        self.RequestId = params.get("RequestId")


class WordItem(AbstractModel):
    """The recognized text information.

    """

    def __init__(self):
        r"""
        :param DetectedText: The text content.
        :type DetectedText: str
        :param Coord: The coordinates of the four vertices.
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self.DetectedText = None
        self.Coord = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        if params.get("Coord") is not None:
            self.Coord = Polygon()
            self.Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        