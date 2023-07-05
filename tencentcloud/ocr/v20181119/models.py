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
        :param _Title: Invoice title
        :type Title: str
        :param _Number: E-ticket No.
        :type Number: str
        :param _CheckCode: Check code
        :type CheckCode: str
        :param _SerialNumber: Serial number
        :type SerialNumber: str
        :param _Date: Date of issue
        :type Date: str
        :param _AgentCode: Agent code
        :type AgentCode: str
        :param _AgentCodeFirst: First line of the agent code
        :type AgentCodeFirst: str
        :param _AgentCodeSecond: Second line of the agent code
        :type AgentCodeSecond: str
        :param _UserName: Name
        :type UserName: str
        :param _UserID: ID card number
        :type UserID: str
        :param _Issuer: Issuer
        :type Issuer: str
        :param _Fare: Fare
        :type Fare: str
        :param _Tax: Tax
        :type Tax: str
        :param _FuelSurcharge: Fuel surcharge
        :type FuelSurcharge: str
        :param _AirDevelopmentFund: Aviation Development Fund
        :type AirDevelopmentFund: str
        :param _Insurance: Insurance
        :type Insurance: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _DomesticInternationalTag: Domestic or international tag
        :type DomesticInternationalTag: str
        :param _DateStart: Not-valid-before date
        :type DateStart: str
        :param _DateEnd: Not-valid-after date
        :type DateEnd: str
        :param _Endorsement: Endorsements/Restrictions
        :type Endorsement: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _FlightItems: Items
        :type FlightItems: list of FlightItem
        """
        self._Title = None
        self._Number = None
        self._CheckCode = None
        self._SerialNumber = None
        self._Date = None
        self._AgentCode = None
        self._AgentCodeFirst = None
        self._AgentCodeSecond = None
        self._UserName = None
        self._UserID = None
        self._Issuer = None
        self._Fare = None
        self._Tax = None
        self._FuelSurcharge = None
        self._AirDevelopmentFund = None
        self._Insurance = None
        self._Total = None
        self._Kind = None
        self._DomesticInternationalTag = None
        self._DateStart = None
        self._DateEnd = None
        self._Endorsement = None
        self._QRCodeMark = None
        self._FlightItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AgentCode(self):
        return self._AgentCode

    @AgentCode.setter
    def AgentCode(self, AgentCode):
        self._AgentCode = AgentCode

    @property
    def AgentCodeFirst(self):
        return self._AgentCodeFirst

    @AgentCodeFirst.setter
    def AgentCodeFirst(self, AgentCodeFirst):
        self._AgentCodeFirst = AgentCodeFirst

    @property
    def AgentCodeSecond(self):
        return self._AgentCodeSecond

    @AgentCodeSecond.setter
    def AgentCodeSecond(self, AgentCodeSecond):
        self._AgentCodeSecond = AgentCodeSecond

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Fare(self):
        return self._Fare

    @Fare.setter
    def Fare(self, Fare):
        self._Fare = Fare

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def FuelSurcharge(self):
        return self._FuelSurcharge

    @FuelSurcharge.setter
    def FuelSurcharge(self, FuelSurcharge):
        self._FuelSurcharge = FuelSurcharge

    @property
    def AirDevelopmentFund(self):
        return self._AirDevelopmentFund

    @AirDevelopmentFund.setter
    def AirDevelopmentFund(self, AirDevelopmentFund):
        self._AirDevelopmentFund = AirDevelopmentFund

    @property
    def Insurance(self):
        return self._Insurance

    @Insurance.setter
    def Insurance(self, Insurance):
        self._Insurance = Insurance

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def DomesticInternationalTag(self):
        return self._DomesticInternationalTag

    @DomesticInternationalTag.setter
    def DomesticInternationalTag(self, DomesticInternationalTag):
        self._DomesticInternationalTag = DomesticInternationalTag

    @property
    def DateStart(self):
        return self._DateStart

    @DateStart.setter
    def DateStart(self, DateStart):
        self._DateStart = DateStart

    @property
    def DateEnd(self):
        return self._DateEnd

    @DateEnd.setter
    def DateEnd(self, DateEnd):
        self._DateEnd = DateEnd

    @property
    def Endorsement(self):
        return self._Endorsement

    @Endorsement.setter
    def Endorsement(self, Endorsement):
        self._Endorsement = Endorsement

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def FlightItems(self):
        return self._FlightItems

    @FlightItems.setter
    def FlightItems(self, FlightItems):
        self._FlightItems = FlightItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._CheckCode = params.get("CheckCode")
        self._SerialNumber = params.get("SerialNumber")
        self._Date = params.get("Date")
        self._AgentCode = params.get("AgentCode")
        self._AgentCodeFirst = params.get("AgentCodeFirst")
        self._AgentCodeSecond = params.get("AgentCodeSecond")
        self._UserName = params.get("UserName")
        self._UserID = params.get("UserID")
        self._Issuer = params.get("Issuer")
        self._Fare = params.get("Fare")
        self._Tax = params.get("Tax")
        self._FuelSurcharge = params.get("FuelSurcharge")
        self._AirDevelopmentFund = params.get("AirDevelopmentFund")
        self._Insurance = params.get("Insurance")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._DomesticInternationalTag = params.get("DomesticInternationalTag")
        self._DateStart = params.get("DateStart")
        self._DateEnd = params.get("DateEnd")
        self._Endorsement = params.get("Endorsement")
        self._QRCodeMark = params.get("QRCodeMark")
        if params.get("FlightItems") is not None:
            self._FlightItems = []
            for item in params.get("FlightItems"):
                obj = FlightItem()
                obj._deserialize(item)
                self._FlightItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded value of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either the `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _RetBorderCutImage: Whether to return the bank card image data after preprocessing (precise cropping and alignment). Default value: `false`
        :type RetBorderCutImage: bool
        :param _RetCardNoImage: Whether to return the card number image data after slicing. Default value: `false`
        :type RetCardNoImage: bool
        :param _EnableCopyCheck: Whether to enable photocopy check. If the input image is a bank card photocopy, an alarm will be returned. Default value: `false`
        :type EnableCopyCheck: bool
        :param _EnableReshootCheck: Whether to enable photograph check. If the input image is a bank card photograph, an alarm will be returned. Default value: `false`
        :type EnableReshootCheck: bool
        :param _EnableBorderCheck: Whether to enable obscured border check. If the input image is a bank card with obscured border, an alarm will be returned. Default value: `false`
        :type EnableBorderCheck: bool
        :param _EnableQualityValue: Whether to return the image quality value, which measures how clear an image is. Default value: `false`
        :type EnableQualityValue: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetBorderCutImage = None
        self._RetCardNoImage = None
        self._EnableCopyCheck = None
        self._EnableReshootCheck = None
        self._EnableBorderCheck = None
        self._EnableQualityValue = None

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
    def RetBorderCutImage(self):
        return self._RetBorderCutImage

    @RetBorderCutImage.setter
    def RetBorderCutImage(self, RetBorderCutImage):
        self._RetBorderCutImage = RetBorderCutImage

    @property
    def RetCardNoImage(self):
        return self._RetCardNoImage

    @RetCardNoImage.setter
    def RetCardNoImage(self, RetCardNoImage):
        self._RetCardNoImage = RetCardNoImage

    @property
    def EnableCopyCheck(self):
        return self._EnableCopyCheck

    @EnableCopyCheck.setter
    def EnableCopyCheck(self, EnableCopyCheck):
        self._EnableCopyCheck = EnableCopyCheck

    @property
    def EnableReshootCheck(self):
        return self._EnableReshootCheck

    @EnableReshootCheck.setter
    def EnableReshootCheck(self, EnableReshootCheck):
        self._EnableReshootCheck = EnableReshootCheck

    @property
    def EnableBorderCheck(self):
        return self._EnableBorderCheck

    @EnableBorderCheck.setter
    def EnableBorderCheck(self, EnableBorderCheck):
        self._EnableBorderCheck = EnableBorderCheck

    @property
    def EnableQualityValue(self):
        return self._EnableQualityValue

    @EnableQualityValue.setter
    def EnableQualityValue(self, EnableQualityValue):
        self._EnableQualityValue = EnableQualityValue


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetBorderCutImage = params.get("RetBorderCutImage")
        self._RetCardNoImage = params.get("RetCardNoImage")
        self._EnableCopyCheck = params.get("EnableCopyCheck")
        self._EnableReshootCheck = params.get("EnableReshootCheck")
        self._EnableBorderCheck = params.get("EnableBorderCheck")
        self._EnableQualityValue = params.get("EnableQualityValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _CardNo: Card number
        :type CardNo: str
        :param _BankInfo: Bank information
        :type BankInfo: str
        :param _ValidDate: Expiration date. Format: 07/2023
        :type ValidDate: str
        :param _CardType: Card type
        :type CardType: str
        :param _CardName: Card name
        :type CardName: str
        :param _BorderCutImage: Sliced image data
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BorderCutImage: str
        :param _CardNoImage: Card number image data
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CardNoImage: str
        :param _WarningCode: Warning code:
-9110: the bank card date is invalid. 
-9111: the bank card border is incomplete. 
-9112: the bank card image is reflective.
-9113: the bank card image is a photocopy.
-9114: the bank card image is a photograph.
Multiple warning codes may be returned at a time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WarningCode: list of int
        :param _QualityValue: Image quality value, which is returned when `EnableQualityValue` is set to `true`. The smaller the value, the less clear the image is. Value range: 0−100 (a threshold greater than or equal to 50 is recommended.)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QualityValue: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CardNo = None
        self._BankInfo = None
        self._ValidDate = None
        self._CardType = None
        self._CardName = None
        self._BorderCutImage = None
        self._CardNoImage = None
        self._WarningCode = None
        self._QualityValue = None
        self._RequestId = None

    @property
    def CardNo(self):
        return self._CardNo

    @CardNo.setter
    def CardNo(self, CardNo):
        self._CardNo = CardNo

    @property
    def BankInfo(self):
        return self._BankInfo

    @BankInfo.setter
    def BankInfo(self, BankInfo):
        self._BankInfo = BankInfo

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def CardName(self):
        return self._CardName

    @CardName.setter
    def CardName(self, CardName):
        self._CardName = CardName

    @property
    def BorderCutImage(self):
        return self._BorderCutImage

    @BorderCutImage.setter
    def BorderCutImage(self, BorderCutImage):
        self._BorderCutImage = BorderCutImage

    @property
    def CardNoImage(self):
        return self._CardNoImage

    @CardNoImage.setter
    def CardNoImage(self, CardNoImage):
        self._CardNoImage = CardNoImage

    @property
    def WarningCode(self):
        return self._WarningCode

    @WarningCode.setter
    def WarningCode(self, WarningCode):
        self._WarningCode = WarningCode

    @property
    def QualityValue(self):
        return self._QualityValue

    @QualityValue.setter
    def QualityValue(self, QualityValue):
        self._QualityValue = QualityValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CardNo = params.get("CardNo")
        self._BankInfo = params.get("BankInfo")
        self._ValidDate = params.get("ValidDate")
        self._CardType = params.get("CardType")
        self._CardName = params.get("CardName")
        self._BorderCutImage = params.get("BorderCutImage")
        self._CardNoImage = params.get("CardNoImage")
        self._WarningCode = params.get("WarningCode")
        self._QualityValue = params.get("QualityValue")
        self._RequestId = params.get("RequestId")


class BusInvoice(AbstractModel):
    """Bus ticket

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _Number: Invoice number
        :type Number: str
        :param _Code: Invoice code
        :type Code: str
        :param _Date: Date of issue
        :type Date: str
        :param _TimeGetOn: Departure time
        :type TimeGetOn: str
        :param _DateGetOn: Departure date
        :type DateGetOn: str
        :param _StationGetOn: Departure station
        :type StationGetOn: str
        :param _StationGetOff: Destination
        :type StationGetOff: str
        :param _Total: Fare
        :type Total: str
        :param _UserName: Name
        :type UserName: str
        :param _Kind: Consumption type
        :type Kind: str
        :param _UserID: ID card number
        :type UserID: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _PlaceGetOn: Departure place
        :type PlaceGetOn: str
        :param _GateNumber: Check-in gate
        :type GateNumber: str
        :param _TicketType: Fare category
        :type TicketType: str
        :param _VehicleType: Vehicle type
        :type VehicleType: str
        :param _SeatNumber: Seat No.
        :type SeatNumber: str
        :param _TrainNumber: Fleet number
        :type TrainNumber: str
        """
        self._Title = None
        self._QRCodeMark = None
        self._Number = None
        self._Code = None
        self._Date = None
        self._TimeGetOn = None
        self._DateGetOn = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Total = None
        self._UserName = None
        self._Kind = None
        self._UserID = None
        self._Province = None
        self._City = None
        self._PlaceGetOn = None
        self._GateNumber = None
        self._TicketType = None
        self._VehicleType = None
        self._SeatNumber = None
        self._TrainNumber = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

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

    @property
    def PlaceGetOn(self):
        return self._PlaceGetOn

    @PlaceGetOn.setter
    def PlaceGetOn(self, PlaceGetOn):
        self._PlaceGetOn = PlaceGetOn

    @property
    def GateNumber(self):
        return self._GateNumber

    @GateNumber.setter
    def GateNumber(self, GateNumber):
        self._GateNumber = GateNumber

    @property
    def TicketType(self):
        return self._TicketType

    @TicketType.setter
    def TicketType(self, TicketType):
        self._TicketType = TicketType

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def SeatNumber(self):
        return self._SeatNumber

    @SeatNumber.setter
    def SeatNumber(self, SeatNumber):
        self._SeatNumber = SeatNumber

    @property
    def TrainNumber(self):
        return self._TrainNumber

    @TrainNumber.setter
    def TrainNumber(self, TrainNumber):
        self._TrainNumber = TrainNumber


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Number = params.get("Number")
        self._Code = params.get("Code")
        self._Date = params.get("Date")
        self._TimeGetOn = params.get("TimeGetOn")
        self._DateGetOn = params.get("DateGetOn")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Total = params.get("Total")
        self._UserName = params.get("UserName")
        self._Kind = params.get("Kind")
        self._UserID = params.get("UserID")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PlaceGetOn = params.get("PlaceGetOn")
        self._GateNumber = params.get("GateNumber")
        self._TicketType = params.get("TicketType")
        self._VehicleType = params.get("VehicleType")
        self._SeatNumber = params.get("SeatNumber")
        self._TrainNumber = params.get("TrainNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    """Coordinates

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
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
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
        


class DetectedWordCoordPoint(AbstractModel):
    """Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner

    """

    def __init__(self):
        r"""
        :param _WordCoordinate: Coordinates of a word’s four corners in a clockwise order on the input image, starting from the upper-left corner
        :type WordCoordinate: list of Coord
        """
        self._WordCoordinate = None

    @property
    def WordCoordinate(self):
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
    """Information about a character detected, including the character itself and its confidence

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
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Character(self):
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
        


class FlightItem(AbstractModel):
    """Flight items

    """

    def __init__(self):
        r"""
        :param _TerminalGetOn: Departure terminal
        :type TerminalGetOn: str
        :param _TerminalGetOff: Arrival terminal
        :type TerminalGetOff: str
        :param _Carrier: Carrier
        :type Carrier: str
        :param _FlightNumber: Flight number
        :type FlightNumber: str
        :param _Seat: Class
        :type Seat: str
        :param _DateGetOn: Departure date
        :type DateGetOn: str
        :param _TimeGetOn: Departure time
        :type TimeGetOn: str
        :param _StationGetOn: Departure city
        :type StationGetOn: str
        :param _StationGetOff: Arrival city
        :type StationGetOff: str
        :param _Allow: Baggage allowance
        :type Allow: str
        :param _FareBasis: Fare category
        :type FareBasis: str
        """
        self._TerminalGetOn = None
        self._TerminalGetOff = None
        self._Carrier = None
        self._FlightNumber = None
        self._Seat = None
        self._DateGetOn = None
        self._TimeGetOn = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Allow = None
        self._FareBasis = None

    @property
    def TerminalGetOn(self):
        return self._TerminalGetOn

    @TerminalGetOn.setter
    def TerminalGetOn(self, TerminalGetOn):
        self._TerminalGetOn = TerminalGetOn

    @property
    def TerminalGetOff(self):
        return self._TerminalGetOff

    @TerminalGetOff.setter
    def TerminalGetOff(self, TerminalGetOff):
        self._TerminalGetOff = TerminalGetOff

    @property
    def Carrier(self):
        return self._Carrier

    @Carrier.setter
    def Carrier(self, Carrier):
        self._Carrier = Carrier

    @property
    def FlightNumber(self):
        return self._FlightNumber

    @FlightNumber.setter
    def FlightNumber(self, FlightNumber):
        self._FlightNumber = FlightNumber

    @property
    def Seat(self):
        return self._Seat

    @Seat.setter
    def Seat(self, Seat):
        self._Seat = Seat

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Allow(self):
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def FareBasis(self):
        return self._FareBasis

    @FareBasis.setter
    def FareBasis(self, FareBasis):
        self._FareBasis = FareBasis


    def _deserialize(self, params):
        self._TerminalGetOn = params.get("TerminalGetOn")
        self._TerminalGetOff = params.get("TerminalGetOff")
        self._Carrier = params.get("Carrier")
        self._FlightNumber = params.get("FlightNumber")
        self._Seat = params.get("Seat")
        self._DateGetOn = params.get("DateGetOn")
        self._TimeGetOn = params.get("TimeGetOn")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Allow = params.get("Allow")
        self._FareBasis = params.get("FareBasis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded value of image.
The image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
Either `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
The image cannot exceed 7 MB after being Base64-encoded. A resolution above 600x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _IsWords: Whether to return the character information. Default value: `false`
        :type IsWords: bool
        :param _EnableDetectSplit: Whether to slice the input image to enhance the recognition effects for scenarios where the whole image is big, but the size of a single character is small (e.g., test papers). This feature is disabled by default.
        :type EnableDetectSplit: bool
        :param _IsPdf: Whether to enable PDF recognition. Default value: `false`. If you enable this feature, both images and PDF files can be recognized.
        :type IsPdf: bool
        :param _PdfPageNumber: Number of a PDF page that needs to be recognized. Currently, only one single page can be recognized. This parameter takes effect only if a PDF file is uploaded and `IsPdf` is set to `true`. Default value: `1`
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsWords = None
        self._EnableDetectSplit = None
        self._IsPdf = None
        self._PdfPageNumber = None

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
    def IsWords(self):
        return self._IsWords

    @IsWords.setter
    def IsWords(self, IsWords):
        self._IsWords = IsWords

    @property
    def EnableDetectSplit(self):
        return self._EnableDetectSplit

    @EnableDetectSplit.setter
    def EnableDetectSplit(self, EnableDetectSplit):
        self._EnableDetectSplit = EnableDetectSplit

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsWords = params.get("IsWords")
        self._EnableDetectSplit = params.get("EnableDetectSplit")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TextDetections: Information on recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :type TextDetections: list of TextDetection
        :param _Angel: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :type Angel: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR request structure.

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
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LanguageType(self):
        return self._LanguageType

    @LanguageType.setter
    def LanguageType(self, LanguageType):
        self._LanguageType = LanguageType

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def IsWords(self):
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
    """GeneralBasicOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TextDetections: Information of recognized text, including the text line content, confidence, text line coordinates, and text line coordinates after rotation correction. For more information, please click the link on the left.
        :type TextDetections: list of TextDetection
        :param _Language: Detected language. For more information on the supported languages, please see the description of the `LanguageType` input parameter.
        :type Language: str
        :param _Angel: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a positive value: rotate clockwise; a negative value: rotate counterclockwise.
        :type Angel: float
        :param _PdfPageSize: Total number of PDF pages to be returned if the image is a PDF. Default value: 0.
        :type PdfPageSize: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TextDetections = None
        self._Language = None
        self._Angel = None
        self._PdfPageSize = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class GeneralMachineItem(AbstractModel):
    """Items of a general machine-printed invoice

    """

    def __init__(self):
        r"""
        :param _Name: Item name
        :type Name: str
        :param _Specification: Specification
        :type Specification: str
        :param _Unit: Unit
        :type Unit: str
        :param _Quantity: Quantity
        :type Quantity: str
        :param _Price: Unit price
        :type Price: str
        :param _Total: Amount
        :type Total: str
        :param _TaxRate: Tax rate
        :type TaxRate: str
        :param _Tax: Tax amount
        :type Tax: str
        """
        self._Name = None
        self._Specification = None
        self._Unit = None
        self._Quantity = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Specification = params.get("Specification")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """The sequence number of an element group in the image

    """

    def __init__(self):
        r"""
        :param _Groups: The elements in each line.
        :type Groups: list of LineInfo
        """
        self._Groups = None

    @property
    def Groups(self):
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
    """HKIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _DetectFake: Whether to check for authenticity.
        :type DetectFake: bool
        :param _ReturnHeadImage: Whether to return identity photo.
        :type ReturnHeadImage: bool
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
        self._DetectFake = None
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def DetectFake(self):
        return self._DetectFake

    @DetectFake.setter
    def DetectFake(self, DetectFake):
        self._DetectFake = DetectFake

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

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


    def _deserialize(self, params):
        self._DetectFake = params.get("DetectFake")
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
        


class HKIDCardOCRResponse(AbstractModel):
    """HKIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _CnName: Name in Chinese
        :type CnName: str
        :param _EnName: Name in English
        :type EnName: str
        :param _TelexCode: Telecode for the name in Chinese
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
        :param _FirstIssueDate: First issue date
        :type FirstIssueDate: str
        :param _CurrentIssueDate: Last receipt date
        :type CurrentIssueDate: str
        :param _FakeDetectResult: Authenticity check.
0: unable to judge (because the image is blurred, incomplete, reflective, too dark, etc.);
1: forged;
2: authentic.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FakeDetectResult: int
        :param _HeadImage: Base64-encoded identity photo
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeadImage: str
        :param _WarningCode: Multiple alarm codes. If the ID card is spoofed, photocopied, or photoshopped, the corresponding alarm code will be returned.
-9102: Alarm for photocopied document
-9103: Alarm for spoofed document
-9104: Alarm for photoshopped document
        :type WarningCode: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._WarningCode = None
        self._RequestId = None

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

    @property
    def FakeDetectResult(self):
        return self._FakeDetectResult

    @FakeDetectResult.setter
    def FakeDetectResult(self, FakeDetectResult):
        self._FakeDetectResult = FakeDetectResult

    @property
    def HeadImage(self):
        return self._HeadImage

    @HeadImage.setter
    def HeadImage(self, HeadImage):
        self._HeadImage = HeadImage

    @property
    def WarningCode(self):
        return self._WarningCode

    @WarningCode.setter
    def WarningCode(self, WarningCode):
        self._WarningCode = WarningCode

    @property
    def RequestId(self):
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
        self._WarningCode = params.get("WarningCode")
        self._RequestId = params.get("RequestId")


class HmtResidentPermitOCRRequest(AbstractModel):
    """HmtResidentPermitOCR request structure.

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
        :param _CardSide: `FRONT`: The side with the profile photo.
`BACK`: The side with the national emblem.
If this parameter is not specified, the system will automatically determine the ID card side.
        :type CardSide: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None

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
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HmtResidentPermitOCRResponse(AbstractModel):
    """HmtResidentPermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Sex: Gender
        :type Sex: str
        :param _Birth: Date of birth
        :type Birth: str
        :param _Address: Address
        :type Address: str
        :param _IdCardNo: ID card number
        :type IdCardNo: str
        :param _CardType: 0: Front side.
1: Back side.
        :type CardType: int
        :param _ValidDate: Validity period
        :type ValidDate: str
        :param _Authority: Issuing authority
        :type Authority: str
        :param _VisaNum: Number of issues
        :type VisaNum: str
        :param _PassNo: Permit number
        :type PassNo: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Birth = None
        self._Address = None
        self._IdCardNo = None
        self._CardType = None
        self._ValidDate = None
        self._Authority = None
        self._VisaNum = None
        self._PassNo = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdCardNo(self):
        return self._IdCardNo

    @IdCardNo.setter
    def IdCardNo(self, IdCardNo):
        self._IdCardNo = IdCardNo

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Authority(self):
        return self._Authority

    @Authority.setter
    def Authority(self, Authority):
        self._Authority = Authority

    @property
    def VisaNum(self):
        return self._VisaNum

    @VisaNum.setter
    def VisaNum(self, VisaNum):
        self._VisaNum = VisaNum

    @property
    def PassNo(self):
        return self._PassNo

    @PassNo.setter
    def PassNo(self, PassNo):
        self._PassNo = PassNo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._IdCardNo = params.get("IdCardNo")
        self._CardType = params.get("CardType")
        self._ValidDate = params.get("ValidDate")
        self._Authority = params.get("Authority")
        self._VisaNum = params.get("VisaNum")
        self._PassNo = params.get("PassNo")
        self._RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        :param _CardSide: `FRONT`: The side with the profile photo.
`BACK`: The side with the national emblem.
If this parameter is not specified, the system will automatically determine the ID card side.
        :type CardSide: str
        :param _Config: The following parameters are all of `bool` type and default to `false`:
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
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None
        self._Config = None

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
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name (profile photo side)
        :type Name: str
        :param _Sex: Gender (profile photo side)
        :type Sex: str
        :param _Nation: Ethnicity (profile photo side)
        :type Nation: str
        :param _Birth: Date of birth (profile photo side)
        :type Birth: str
        :param _Address: Address (profile photo side)
        :type Address: str
        :param _IdNum: ID number (profile photo side)
        :type IdNum: str
        :param _Authority: Issuing authority (national emblem side)
        :type Authority: str
        :param _ValidDate: Validity period (national emblem side)
        :type ValidDate: str
        :param _AdvancedInfo: Extended information, which will be returned only when requested. For the input parameters, please see example 3 and example 4.
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._AdvancedInfo = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Authority(self):
        return self._Authority

    @Authority.setter
    def Authority(self, Authority):
        self._Authority = Authority

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def RequestId(self):
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
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._RequestId = params.get("RequestId")


class InvoiceItem(AbstractModel):
    """Recognition information of a single invoice/ticket among multiple types of invoices/tickets

    """

    def __init__(self):
        r"""
        :param _Code: The recognition result.
`OK`: Recognition is successful.
`FailedOperation.UnsupportedInvoice`: Recognition is not supported.
`FailedOperation.UnKnowError`: Recognition failed.
For the information about other error codes, see the OCR API description for each invoice/ticket.
        :type Code: str
        :param _Type: The type of invoice/ticket to which the recognized image belongs.
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
        :param _Polygon: The coordinates of the four vertices of the rotated image.
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _Angle: The rotation angle of the recognized image in the image with multiple types of invoices/tickets.
        :type Angle: float
        :param _SingleInvoiceInfos: The recognized content.
        :type SingleInvoiceInfos: :class:`tencentcloud.ocr.v20181119.models.SingleInvoiceItem`
        :param _Page: The number of the page on which the recognized invoice is in the image or PDF file, starting from 1 by default.
        :type Page: int
        :param _SubType: The detailed invoice type. See the description of `SubType`.
        :type SubType: str
        :param _TypeDescription: The invoice description. See the description of `TypeDescription`.
        :type TypeDescription: str
        :param _CutImage: The image file after cropping, encoded in Base64. This is returned if `EnableCutImage` is set to `true`.
        :type CutImage: str
        :param _SubTypeDescription: The description of the detailed invoice type. See the description of `SubType`.
        :type SubTypeDescription: str
        """
        self._Code = None
        self._Type = None
        self._Polygon = None
        self._Angle = None
        self._SingleInvoiceInfos = None
        self._Page = None
        self._SubType = None
        self._TypeDescription = None
        self._CutImage = None
        self._SubTypeDescription = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def SingleInvoiceInfos(self):
        return self._SingleInvoiceInfos

    @SingleInvoiceInfos.setter
    def SingleInvoiceInfos(self, SingleInvoiceInfos):
        self._SingleInvoiceInfos = SingleInvoiceInfos

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TypeDescription(self):
        return self._TypeDescription

    @TypeDescription.setter
    def TypeDescription(self, TypeDescription):
        self._TypeDescription = TypeDescription

    @property
    def CutImage(self):
        return self._CutImage

    @CutImage.setter
    def CutImage(self, CutImage):
        self._CutImage = CutImage

    @property
    def SubTypeDescription(self):
        return self._SubTypeDescription

    @SubTypeDescription.setter
    def SubTypeDescription(self, SubTypeDescription):
        self._SubTypeDescription = SubTypeDescription


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        self._Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self._SingleInvoiceInfos = SingleInvoiceItem()
            self._SingleInvoiceInfos._deserialize(params.get("SingleInvoiceInfos"))
        self._Page = params.get("Page")
        self._SubType = params.get("SubType")
        self._TypeDescription = params.get("TypeDescription")
        self._CutImage = params.get("CutImage")
        self._SubTypeDescription = params.get("SubTypeDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemCoord(AbstractModel):
    """Pixel coordinates of the text line in the image after rotation correction, which is in the format of `(X-coordinate of top-left point, Y-coordinate of top-left point, width, height)`.

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
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
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
    """Structured element group

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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
    """Key information

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
        return self._AutoName

    @AutoName.setter
    def AutoName(self, AutoName):
        self._AutoName = AutoName

    @property
    def ConfigName(self):
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
        


class LicensePlateInfo(AbstractModel):
    """Vehicle license plate information

    """

    def __init__(self):
        r"""
        :param _Number: The recognized license plate number.
        :type Number: str
        :param _Confidence: The confidence score (0–100).
        :type Confidence: int
        :param _Rect: The bounding box coordinates of the text line in the original image.
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Color: The recognized license plate color, which currently includes "white", "black", "blue", "green", "yellow", "yellow-green", and "temporary plate".
        :type Color: str
        """
        self._Number = None
        self._Confidence = None
        self._Rect = None
        self._Color = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR request structure.

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
        


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Number: The recognized license plate number.
        :type Number: str
        :param _Confidence: The confidence score (0–100).
        :type Confidence: int
        :param _Rect: The bounding box coordinates of the text line in the original image.
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Color: The recognized license plate color, which currently includes "white", "black", "blue", "green", "yellow", "yellow-green", and "temporary plate".
        :type Color: str
        :param _LicensePlateInfos: The vehicle license plate information.
        :type LicensePlateInfos: list of LicensePlateInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Number = None
        self._Confidence = None
        self._Rect = None
        self._Color = None
        self._LicensePlateInfos = None
        self._RequestId = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def LicensePlateInfos(self):
        return self._LicensePlateInfos

    @LicensePlateInfos.setter
    def LicensePlateInfos(self, LicensePlateInfos):
        self._LicensePlateInfos = LicensePlateInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Color = params.get("Color")
        if params.get("LicensePlateInfos") is not None:
            self._LicensePlateInfos = []
            for item in params.get("LicensePlateInfos"):
                obj = LicensePlateInfo()
                obj._deserialize(item)
                self._LicensePlateInfos.append(obj)
        self._RequestId = params.get("RequestId")


class LineInfo(AbstractModel):
    """Line number

    """

    def __init__(self):
        r"""
        :param _Lines: The elements in a line
        :type Lines: list of ItemInfo
        """
        self._Lines = None

    @property
    def Lines(self):
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
    """MLIDCardOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image.
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
        :type ImageBase64: str
        :param _ImageUrl: The URL of an image. (This field is not available outside the Chinese mainland.)
Supported image formats: PNG, JPG, and JPEG. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
For a non-Tencent Cloud URL, the download speed and stability may be low.
        :type ImageUrl: str
        :param _RetImage: Whether to return an image. Default value: `false`.
        :type RetImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetImage = None

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
    def RetImage(self):
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR response structure.

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
        :param _Warn: Alarm codes
-9103 Alarm for photographed certificate
-9102 Alarm for photocopied certificate
-9106 Alarm for covered certificate
-9107 Alarm for blurry image
        :type Warn: list of int
        :param _Image: Identity photo
        :type Image: str
        :param _AdvancedInfo: This is an extended field, 
with the confidence of a field recognition result returned in the following format.
{
  Field name:{
    Confidence:0.9999
  }
}
        :type AdvancedInfo: str
        :param _Type: Certificate type
MyKad  ID card
MyPR    Permanent resident card
MyTentera   Military identity card
MyKAS    Temporary ID card
POLIS  Police card
IKAD   Work permit
MyKid   Kid card
        :type Type: str
        :param _Birthday: Date of birth. This field is available only for work permits (i-Kad) and ID cards (MyKad).
        :type Birthday: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

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

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded value of image. The image cannot exceed 7 MB in size after being Base64-encoded. A resolution above 500x800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupies more than 2/3 area of the image.
        :type ImageBase64: str
        :param _RetImage: Whether to return an image. Default value: false.
        :type RetImage: bool
        """
        self._ImageBase64 = None
        self._RetImage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def RetImage(self):
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR response structure.

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
        :param _Nationality: Country/region code
        :type Nationality: str
        :param _Warn: Alarm codes
-9103 Alarm for spoofed document
-9102 Alarm for photocopied document (including black & white and color ones)
-9106 Alarm for covered card
        :type Warn: list of int
        :param _Image: Identity photo
        :type Image: str
        :param _AdvancedInfo: Extended field:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

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
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def CodeSet(self):
        return self._CodeSet

    @CodeSet.setter
    def CodeSet(self, CodeSet):
        self._CodeSet = CodeSet

    @property
    def CodeCrc(self):
        return self._CodeCrc

    @CodeCrc.setter
    def CodeCrc(self, CodeCrc):
        self._CodeCrc = CodeCrc

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
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class MachinePrintedInvoice(AbstractModel):
    """General machine-printed invoice

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Date: Date of issue
        :type Date: str
        :param _Time: Time
        :type Time: str
        :param _CheckCode: Check code
        :type CheckCode: str
        :param _Ciphertext: Ciphertext
        :type Ciphertext: str
        :param _Category: Category
        :type Category: str
        :param _PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Tax: Tax
        :type Tax: str
        :param _IndustryClass: Industry
        :type IndustryClass: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param _SellerAddrTel: Seller's address and phone number
        :type SellerAddrTel: str
        :param _SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param _BuyerAddrTel: Buyer's address and phone number
        :type BuyerAddrTel: str
        :param _BuyerBankAccount: Buyer's bank account number
        :type BuyerBankAccount: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param _ElectronicMark: Whether it is a general machine-printed invoice issued by Zhejiang or Guangdong province (0: No, 1: Yes)
        :type ElectronicMark: int
        :param _Issuer: Issuer
        :type Issuer: str
        :param _Receiptor: Payee
        :type Receiptor: str
        :param _Reviewer: Reviewer
        :type Reviewer: str
        :param _Remark: Remarks
        :type Remark: str
        :param _PaymentInfo: Operator's payment information
        :type PaymentInfo: str
        :param _TicketPickupUser: Operator-assigned invoice pickup user
        :type TicketPickupUser: str
        :param _MerchantNumber: Operator's merchant number
        :type MerchantNumber: str
        :param _OrderNumber: Operator's order number
        :type OrderNumber: str
        :param _GeneralMachineItems: Items
        :type GeneralMachineItems: list of GeneralMachineItem
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._Time = None
        self._CheckCode = None
        self._Ciphertext = None
        self._Category = None
        self._PretaxAmount = None
        self._Total = None
        self._TotalCn = None
        self._Tax = None
        self._IndustryClass = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerAddrTel = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._BuyerAddrTel = None
        self._BuyerBankAccount = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CompanySealMark = None
        self._ElectronicMark = None
        self._Issuer = None
        self._Receiptor = None
        self._Reviewer = None
        self._Remark = None
        self._PaymentInfo = None
        self._TicketPickupUser = None
        self._MerchantNumber = None
        self._OrderNumber = None
        self._GeneralMachineItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def IndustryClass(self):
        return self._IndustryClass

    @IndustryClass.setter
    def IndustryClass(self, IndustryClass):
        self._IndustryClass = IndustryClass

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddrTel(self):
        return self._SellerAddrTel

    @SellerAddrTel.setter
    def SellerAddrTel(self, SellerAddrTel):
        self._SellerAddrTel = SellerAddrTel

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def BuyerAddrTel(self):
        return self._BuyerAddrTel

    @BuyerAddrTel.setter
    def BuyerAddrTel(self, BuyerAddrTel):
        self._BuyerAddrTel = BuyerAddrTel

    @property
    def BuyerBankAccount(self):
        return self._BuyerBankAccount

    @BuyerBankAccount.setter
    def BuyerBankAccount(self, BuyerBankAccount):
        self._BuyerBankAccount = BuyerBankAccount

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def ElectronicMark(self):
        return self._ElectronicMark

    @ElectronicMark.setter
    def ElectronicMark(self, ElectronicMark):
        self._ElectronicMark = ElectronicMark

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Receiptor(self):
        return self._Receiptor

    @Receiptor.setter
    def Receiptor(self, Receiptor):
        self._Receiptor = Receiptor

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PaymentInfo(self):
        return self._PaymentInfo

    @PaymentInfo.setter
    def PaymentInfo(self, PaymentInfo):
        self._PaymentInfo = PaymentInfo

    @property
    def TicketPickupUser(self):
        return self._TicketPickupUser

    @TicketPickupUser.setter
    def TicketPickupUser(self, TicketPickupUser):
        self._TicketPickupUser = TicketPickupUser

    @property
    def MerchantNumber(self):
        return self._MerchantNumber

    @MerchantNumber.setter
    def MerchantNumber(self, MerchantNumber):
        self._MerchantNumber = MerchantNumber

    @property
    def OrderNumber(self):
        return self._OrderNumber

    @OrderNumber.setter
    def OrderNumber(self, OrderNumber):
        self._OrderNumber = OrderNumber

    @property
    def GeneralMachineItems(self):
        return self._GeneralMachineItems

    @GeneralMachineItems.setter
    def GeneralMachineItems(self, GeneralMachineItems):
        self._GeneralMachineItems = GeneralMachineItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._CheckCode = params.get("CheckCode")
        self._Ciphertext = params.get("Ciphertext")
        self._Category = params.get("Category")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Tax = params.get("Tax")
        self._IndustryClass = params.get("IndustryClass")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddrTel = params.get("SellerAddrTel")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._BuyerAddrTel = params.get("BuyerAddrTel")
        self._BuyerBankAccount = params.get("BuyerBankAccount")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CompanySealMark = params.get("CompanySealMark")
        self._ElectronicMark = params.get("ElectronicMark")
        self._Issuer = params.get("Issuer")
        self._Receiptor = params.get("Receiptor")
        self._Reviewer = params.get("Reviewer")
        self._Remark = params.get("Remark")
        self._PaymentInfo = params.get("PaymentInfo")
        self._TicketPickupUser = params.get("TicketPickupUser")
        self._MerchantNumber = params.get("MerchantNumber")
        self._OrderNumber = params.get("OrderNumber")
        if params.get("GeneralMachineItems") is not None:
            self._GeneralMachineItems = []
            for item in params.get("GeneralMachineItems"):
                obj = GeneralMachineItem()
                obj._deserialize(item)
                self._GeneralMachineItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR request structure.

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
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetProfile = None

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
    def RetProfile(self):
        return self._RetProfile

    @RetProfile.setter
    def RetProfile(self, RetProfile):
        self._RetProfile = RetProfile


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetProfile = params.get("RetProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRResponse(AbstractModel):
    """MainlandPermitOCR response structure.

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
        :param _Type: Document type
        :type Type: str
        :param _Profile: Base64-encoded profile photo, which is returned only when `RetProfile` is set to `True`
        :type Profile: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._RequestId = None

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
    def IssueAuthority(self):
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def IssueAddress(self):
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def IssueNumber(self):
        return self._IssueNumber

    @IssueNumber.setter
    def IssueNumber(self, IssueNumber):
        self._IssueNumber = IssueNumber

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class MedicalInvoice(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Title: 
        :type Title: str
        :param _Code: 
        :type Code: str
        :param _Number: 
        :type Number: str
        :param _Total: 
        :type Total: str
        :param _TotalCn: 
        :type TotalCn: str
        :param _Date: 
        :type Date: str
        :param _CheckCode: 
        :type CheckCode: str
        :param _Place: 
        :type Place: str
        :param _Reviewer: 
        :type Reviewer: str
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._TotalCn = None
        self._Date = None
        self._CheckCode = None
        self._Place = None
        self._Reviewer = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Place(self):
        return self._Place

    @Place.setter
    def Place(self, Place):
        self._Place = Place

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Date = params.get("Date")
        self._CheckCode = params.get("CheckCode")
        self._Place = params.get("Place")
        self._Reviewer = params.get("Reviewer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MotorVehicleSaleInvoice(AbstractModel):
    """Motor vehicle sales invoice

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Date: Date of issue
        :type Date: str
        :param _PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTaxID: Seller's company code
        :type SellerTaxID: str
        :param _SellerTel: Seller's phone number
        :type SellerTel: str
        :param _SellerAddress: Seller's address
        :type SellerAddress: str
        :param _SellerBank: Seller's account opening bank
        :type SellerBank: str
        :param _SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param _BuyerID: Buyer's ID number/organization code
        :type BuyerID: str
        :param _TaxAuthorities: Tax authority
        :type TaxAuthorities: str
        :param _TaxAuthoritiesCode: Code of the tax authority
        :type TaxAuthoritiesCode: str
        :param _VIN: VIN
        :type VIN: str
        :param _VehicleModel: Vehicle model
        :type VehicleModel: str
        :param _VehicleEngineCode: Engine No.
        :type VehicleEngineCode: str
        :param _CertificateNumber: No. of the certificate of conformity
        :type CertificateNumber: str
        :param _InspectionNumber: Inspection No.
        :type InspectionNumber: str
        :param _MachineID: Machine No.
        :type MachineID: str
        :param _VehicleType: Vehicle type
        :type VehicleType: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _Tax: Tax
        :type Tax: str
        :param _TaxRate: Tax rate
        :type TaxRate: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param _Tonnage: Tonnage
        :type Tonnage: str
        :param _Remark: Remarks
        :type Remark: str
        :param _FormType: Form type
        :type FormType: str
        :param _FormName: Form name
        :type FormName: str
        :param _Issuer: Issuer
        :type Issuer: str
        :param _TaxNum: Tax payment voucher number
        :type TaxNum: str
        :param _MaxPeopleNum: Passenger capacity
        :type MaxPeopleNum: str
        :param _Origin: Origin
        :type Origin: str
        :param _MachineCode: Machine-printed invoice code
        :type MachineCode: str
        :param _MachineNumber: Machine-printed invoice number
        :type MachineNumber: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._PretaxAmount = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerTel = None
        self._SellerAddress = None
        self._SellerBank = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._BuyerID = None
        self._TaxAuthorities = None
        self._TaxAuthoritiesCode = None
        self._VIN = None
        self._VehicleModel = None
        self._VehicleEngineCode = None
        self._CertificateNumber = None
        self._InspectionNumber = None
        self._MachineID = None
        self._VehicleType = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._Tax = None
        self._TaxRate = None
        self._CompanySealMark = None
        self._Tonnage = None
        self._Remark = None
        self._FormType = None
        self._FormName = None
        self._Issuer = None
        self._TaxNum = None
        self._MaxPeopleNum = None
        self._Origin = None
        self._MachineCode = None
        self._MachineNumber = None
        self._QRCodeMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def SellerBank(self):
        return self._SellerBank

    @SellerBank.setter
    def SellerBank(self, SellerBank):
        self._SellerBank = SellerBank

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def BuyerID(self):
        return self._BuyerID

    @BuyerID.setter
    def BuyerID(self, BuyerID):
        self._BuyerID = BuyerID

    @property
    def TaxAuthorities(self):
        return self._TaxAuthorities

    @TaxAuthorities.setter
    def TaxAuthorities(self, TaxAuthorities):
        self._TaxAuthorities = TaxAuthorities

    @property
    def TaxAuthoritiesCode(self):
        return self._TaxAuthoritiesCode

    @TaxAuthoritiesCode.setter
    def TaxAuthoritiesCode(self, TaxAuthoritiesCode):
        self._TaxAuthoritiesCode = TaxAuthoritiesCode

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def VehicleModel(self):
        return self._VehicleModel

    @VehicleModel.setter
    def VehicleModel(self, VehicleModel):
        self._VehicleModel = VehicleModel

    @property
    def VehicleEngineCode(self):
        return self._VehicleEngineCode

    @VehicleEngineCode.setter
    def VehicleEngineCode(self, VehicleEngineCode):
        self._VehicleEngineCode = VehicleEngineCode

    @property
    def CertificateNumber(self):
        return self._CertificateNumber

    @CertificateNumber.setter
    def CertificateNumber(self, CertificateNumber):
        self._CertificateNumber = CertificateNumber

    @property
    def InspectionNumber(self):
        return self._InspectionNumber

    @InspectionNumber.setter
    def InspectionNumber(self, InspectionNumber):
        self._InspectionNumber = InspectionNumber

    @property
    def MachineID(self):
        return self._MachineID

    @MachineID.setter
    def MachineID(self, MachineID):
        self._MachineID = MachineID

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def Tonnage(self):
        return self._Tonnage

    @Tonnage.setter
    def Tonnage(self, Tonnage):
        self._Tonnage = Tonnage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def TaxNum(self):
        return self._TaxNum

    @TaxNum.setter
    def TaxNum(self, TaxNum):
        self._TaxNum = TaxNum

    @property
    def MaxPeopleNum(self):
        return self._MaxPeopleNum

    @MaxPeopleNum.setter
    def MaxPeopleNum(self, MaxPeopleNum):
        self._MaxPeopleNum = MaxPeopleNum

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def MachineNumber(self):
        return self._MachineNumber

    @MachineNumber.setter
    def MachineNumber(self, MachineNumber):
        self._MachineNumber = MachineNumber

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerTel = params.get("SellerTel")
        self._SellerAddress = params.get("SellerAddress")
        self._SellerBank = params.get("SellerBank")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._BuyerID = params.get("BuyerID")
        self._TaxAuthorities = params.get("TaxAuthorities")
        self._TaxAuthoritiesCode = params.get("TaxAuthoritiesCode")
        self._VIN = params.get("VIN")
        self._VehicleModel = params.get("VehicleModel")
        self._VehicleEngineCode = params.get("VehicleEngineCode")
        self._CertificateNumber = params.get("CertificateNumber")
        self._InspectionNumber = params.get("InspectionNumber")
        self._MachineID = params.get("MachineID")
        self._VehicleType = params.get("VehicleType")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        self._CompanySealMark = params.get("CompanySealMark")
        self._Tonnage = params.get("Tonnage")
        self._Remark = params.get("Remark")
        self._FormType = params.get("FormType")
        self._FormName = params.get("FormName")
        self._Issuer = params.get("Issuer")
        self._TaxNum = params.get("TaxNum")
        self._MaxPeopleNum = params.get("MaxPeopleNum")
        self._Origin = params.get("Origin")
        self._MachineCode = params.get("MachineCode")
        self._MachineNumber = params.get("MachineNumber")
        self._QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxIncomeBill(AbstractModel):
    """Non-tax revenue

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Number: Invoice number
        :type Number: str
        :param _Code: Invoice code
        :type Code: str
        :param _CheckCode: Check code
        :type CheckCode: str
        :param _Date: Date of issue
        :type Date: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Buyer: Payer's name
        :type Buyer: str
        :param _BuyerTaxID: Payer's taxpayer identification number
        :type BuyerTaxID: str
        :param _Seller: Payee's name
        :type Seller: str
        :param _SellerCompany: Payee's company name
        :type SellerCompany: str
        :param _Remark: Remarks
        :type Remark: str
        :param _CurrencyCode: Currency
        :type CurrencyCode: str
        :param _Reviewer: Reviewer
        :type Reviewer: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _OtherInfo: Other information
        :type OtherInfo: str
        :param _PaymentCode: Payment code
        :type PaymentCode: str
        :param _ReceiveUnitCode: Collecting organization's code
        :type ReceiveUnitCode: str
        :param _Receiver: Collecting organization's name
        :type Receiver: str
        :param _Operator: Operator
        :type Operator: str
        :param _PayerAccount: Payer's account
        :type PayerAccount: str
        :param _PayerBank: Payer's account opening bank
        :type PayerBank: str
        :param _ReceiverAccount: Payee's account
        :type ReceiverAccount: str
        :param _ReceiverBank: Payee's account opening bank
        :type ReceiverBank: str
        :param _NonTaxItems: Items
        :type NonTaxItems: list of NonTaxItem
        """
        self._Title = None
        self._Number = None
        self._Code = None
        self._CheckCode = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Seller = None
        self._SellerCompany = None
        self._Remark = None
        self._CurrencyCode = None
        self._Reviewer = None
        self._QRCodeMark = None
        self._OtherInfo = None
        self._PaymentCode = None
        self._ReceiveUnitCode = None
        self._Receiver = None
        self._Operator = None
        self._PayerAccount = None
        self._PayerBank = None
        self._ReceiverAccount = None
        self._ReceiverBank = None
        self._NonTaxItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerCompany(self):
        return self._SellerCompany

    @SellerCompany.setter
    def SellerCompany(self, SellerCompany):
        self._SellerCompany = SellerCompany

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def OtherInfo(self):
        return self._OtherInfo

    @OtherInfo.setter
    def OtherInfo(self, OtherInfo):
        self._OtherInfo = OtherInfo

    @property
    def PaymentCode(self):
        return self._PaymentCode

    @PaymentCode.setter
    def PaymentCode(self, PaymentCode):
        self._PaymentCode = PaymentCode

    @property
    def ReceiveUnitCode(self):
        return self._ReceiveUnitCode

    @ReceiveUnitCode.setter
    def ReceiveUnitCode(self, ReceiveUnitCode):
        self._ReceiveUnitCode = ReceiveUnitCode

    @property
    def Receiver(self):
        return self._Receiver

    @Receiver.setter
    def Receiver(self, Receiver):
        self._Receiver = Receiver

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def PayerAccount(self):
        return self._PayerAccount

    @PayerAccount.setter
    def PayerAccount(self, PayerAccount):
        self._PayerAccount = PayerAccount

    @property
    def PayerBank(self):
        return self._PayerBank

    @PayerBank.setter
    def PayerBank(self, PayerBank):
        self._PayerBank = PayerBank

    @property
    def ReceiverAccount(self):
        return self._ReceiverAccount

    @ReceiverAccount.setter
    def ReceiverAccount(self, ReceiverAccount):
        self._ReceiverAccount = ReceiverAccount

    @property
    def ReceiverBank(self):
        return self._ReceiverBank

    @ReceiverBank.setter
    def ReceiverBank(self, ReceiverBank):
        self._ReceiverBank = ReceiverBank

    @property
    def NonTaxItems(self):
        return self._NonTaxItems

    @NonTaxItems.setter
    def NonTaxItems(self, NonTaxItems):
        self._NonTaxItems = NonTaxItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._Code = params.get("Code")
        self._CheckCode = params.get("CheckCode")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Seller = params.get("Seller")
        self._SellerCompany = params.get("SellerCompany")
        self._Remark = params.get("Remark")
        self._CurrencyCode = params.get("CurrencyCode")
        self._Reviewer = params.get("Reviewer")
        self._QRCodeMark = params.get("QRCodeMark")
        self._OtherInfo = params.get("OtherInfo")
        self._PaymentCode = params.get("PaymentCode")
        self._ReceiveUnitCode = params.get("ReceiveUnitCode")
        self._Receiver = params.get("Receiver")
        self._Operator = params.get("Operator")
        self._PayerAccount = params.get("PayerAccount")
        self._PayerBank = params.get("PayerBank")
        self._ReceiverAccount = params.get("ReceiverAccount")
        self._ReceiverBank = params.get("ReceiverBank")
        if params.get("NonTaxItems") is not None:
            self._NonTaxItems = []
            for item in params.get("NonTaxItems"):
                obj = NonTaxItem()
                obj._deserialize(item)
                self._NonTaxItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxItem(AbstractModel):
    """Non-tax revenue items

    """

    def __init__(self):
        r"""
        :param _ItemID: Item code
        :type ItemID: str
        :param _Name: Item name
        :type Name: str
        :param _Unit: Unit
        :type Unit: str
        :param _Quantity: Quantity
        :type Quantity: str
        :param _Standard: Standard
        :type Standard: str
        :param _Total: Amount
        :type Total: str
        """
        self._ItemID = None
        self._Name = None
        self._Unit = None
        self._Quantity = None
        self._Standard = None
        self._Total = None

    @property
    def ItemID(self):
        return self._ItemID

    @ItemID.setter
    def ItemID(self, ItemID):
        self._ItemID = ItemID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Standard(self):
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._ItemID = params.get("ItemID")
        self._Name = params.get("Name")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Standard = params.get("Standard")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoice(AbstractModel):
    """Other invoices

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Total: Amount
        :type Total: str
        :param _OtherInvoiceListItems: List
        :type OtherInvoiceListItems: list of OtherInvoiceItem
        :param _OtherInvoiceTableItems: Table
        :type OtherInvoiceTableItems: list of OtherInvoiceList
        """
        self._Title = None
        self._Total = None
        self._OtherInvoiceListItems = None
        self._OtherInvoiceTableItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def OtherInvoiceListItems(self):
        return self._OtherInvoiceListItems

    @OtherInvoiceListItems.setter
    def OtherInvoiceListItems(self, OtherInvoiceListItems):
        self._OtherInvoiceListItems = OtherInvoiceListItems

    @property
    def OtherInvoiceTableItems(self):
        return self._OtherInvoiceTableItems

    @OtherInvoiceTableItems.setter
    def OtherInvoiceTableItems(self, OtherInvoiceTableItems):
        self._OtherInvoiceTableItems = OtherInvoiceTableItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Total = params.get("Total")
        if params.get("OtherInvoiceListItems") is not None:
            self._OtherInvoiceListItems = []
            for item in params.get("OtherInvoiceListItems"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self._OtherInvoiceListItems.append(obj)
        if params.get("OtherInvoiceTableItems") is not None:
            self._OtherInvoiceTableItems = []
            for item in params.get("OtherInvoiceTableItems"):
                obj = OtherInvoiceList()
                obj._deserialize(item)
                self._OtherInvoiceTableItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceItem(AbstractModel):
    """Items of other invoices

    """

    def __init__(self):
        r"""
        :param _Name: Field name
        :type Name: str
        :param _Value: Field value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceList(AbstractModel):
    """Table of other invoices

    """

    def __init__(self):
        r"""
        :param _OtherInvoiceItemList: List
        :type OtherInvoiceItemList: list of OtherInvoiceItem
        """
        self._OtherInvoiceItemList = None

    @property
    def OtherInvoiceItemList(self):
        return self._OtherInvoiceItemList

    @OtherInvoiceItemList.setter
    def OtherInvoiceItemList(self, OtherInvoiceItemList):
        self._OtherInvoiceItemList = OtherInvoiceItemList


    def _deserialize(self, params):
        if params.get("OtherInvoiceItemList") is not None:
            self._OtherInvoiceItemList = []
            for item in params.get("OtherInvoiceItemList"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self._OtherInvoiceItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRRequest(AbstractModel):
    """PermitOCR request structure.

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
        


class PermitOCRResponse(AbstractModel):
    """PermitOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _EnglishName: Name in English
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._RequestId = None

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

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    """The coordinates of the four vertices of the text
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
        return self._LeftTop

    @LeftTop.setter
    def LeftTop(self, LeftTop):
        self._LeftTop = LeftTop

    @property
    def RightTop(self):
        return self._RightTop

    @RightTop.setter
    def RightTop(self, RightTop):
        self._RightTop = RightTop

    @property
    def RightBottom(self):
        return self._RightBottom

    @RightBottom.setter
    def RightBottom(self, RightBottom):
        self._RightBottom = RightBottom

    @property
    def LeftBottom(self):
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
        


class QuotaInvoice(AbstractModel):
    """Quota invoice

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._TotalCn = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._QRCodeMark = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._QRCodeMark = params.get("QRCodeMark")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeGeneralInvoiceRequest(AbstractModel):
    """RecognizeGeneralInvoice request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of the image.
Supported image formats: PNG, JPG, JPEG, and PDF. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Supported image pixels: 20 to 10,000
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image.
Supported image formats: PNG, JPG, JPEG, and PDF. GIF is currently not supported.
Supported image size: The downloaded image after Base64 encoding can be up to 7 MB. The download time of the image cannot exceed 3s.
Supported image pixels: 20 to 10,000
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _Types: The list of the types of invoices to be recognized. If this parameter is left empty, all types of invoices are recognized.
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
        :param _EnableOther: Whether to enable recognition of other invoices. If you enable this feature, other invoices can be recognized. Default value: `true`.	
        :type EnableOther: bool
        :param _EnablePdf: Whether to enable PDF recognition. If you enable this feature, both images and PDF files can be recognized. Default value: `true`.
        :type EnablePdf: bool
        :param _PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `EnablePdf` is `true`. Default value: 1.
        :type PdfPageNumber: int
        :param _EnableMultiplePage: Whether to enable multi-page PDF recognition. If you enable this feature, multiple pages of a PDF file can be recognized, and the recognition results of a maximum of the first 30 pages can be returned. After you enable this feature, input parameters `EnablePdf` and `PdfPageNumber` are invalid. Default value: `false`.
        :type EnableMultiplePage: bool
        :param _EnableCutImage: Whether to return the Base64-encoded value of the cropped image. Default value: `false`.
        :type EnableCutImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Types = None
        self._EnableOther = None
        self._EnablePdf = None
        self._PdfPageNumber = None
        self._EnableMultiplePage = None
        self._EnableCutImage = None

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
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def EnableOther(self):
        return self._EnableOther

    @EnableOther.setter
    def EnableOther(self, EnableOther):
        self._EnableOther = EnableOther

    @property
    def EnablePdf(self):
        return self._EnablePdf

    @EnablePdf.setter
    def EnablePdf(self, EnablePdf):
        self._EnablePdf = EnablePdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def EnableMultiplePage(self):
        return self._EnableMultiplePage

    @EnableMultiplePage.setter
    def EnableMultiplePage(self, EnableMultiplePage):
        self._EnableMultiplePage = EnableMultiplePage

    @property
    def EnableCutImage(self):
        return self._EnableCutImage

    @EnableCutImage.setter
    def EnableCutImage(self, EnableCutImage):
        self._EnableCutImage = EnableCutImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Types = params.get("Types")
        self._EnableOther = params.get("EnableOther")
        self._EnablePdf = params.get("EnablePdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._EnableMultiplePage = params.get("EnableMultiplePage")
        self._EnableCutImage = params.get("EnableCutImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeGeneralInvoiceResponse(AbstractModel):
    """RecognizeGeneralInvoice response structure.

    """

    def __init__(self):
        r"""
        :param _MixedInvoiceItems: Mixed invoice/ticket recognition result. Please click the link on the left for details.
        :type MixedInvoiceItems: list of InvoiceItem
        :param _TotalPDFCount: Total number of pages in the PDF file.
        :type TotalPDFCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MixedInvoiceItems = None
        self._TotalPDFCount = None
        self._RequestId = None

    @property
    def MixedInvoiceItems(self):
        return self._MixedInvoiceItems

    @MixedInvoiceItems.setter
    def MixedInvoiceItems(self, MixedInvoiceItems):
        self._MixedInvoiceItems = MixedInvoiceItems

    @property
    def TotalPDFCount(self):
        return self._TotalPDFCount

    @TotalPDFCount.setter
    def TotalPDFCount(self, TotalPDFCount):
        self._TotalPDFCount = TotalPDFCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self._MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = InvoiceItem()
                obj._deserialize(item)
                self._MixedInvoiceItems.append(obj)
        self._TotalPDFCount = params.get("TotalPDFCount")
        self._RequestId = params.get("RequestId")


class RecognizeIndonesiaIDCardOCRRequest(AbstractModel):
    """RecognizeIndonesiaIDCardOCR request structure.

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
        :param _Scene: The scene, which defaults to `V1`.
Valid values:
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
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
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
    """RecognizeIndonesiaIDCardOCR response structure.

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
        :param _RTRW: The street.
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
        :param _Photo: The photo.
        :type Photo: str
        :param _Provinsi: The province, which is supported when the value of `Scene` is `V2`.
        :type Provinsi: str
        :param _Kota: The city, which is supported when the value of `Scene` is `V2`.
        :type Kota: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        self._RequestId = None

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
    def Photo(self):
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

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

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class RecognizeKoreanDrivingLicenseOCRRequest(AbstractModel):
    """RecognizeKoreanDrivingLicenseOCR request structure.

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
    def ReturnHeadImage(self):
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
        


class RecognizeKoreanDrivingLicenseOCRResponse(AbstractModel):
    """RecognizeKoreanDrivingLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: The ID card number.
        :type ID: str
        :param _LicenseNumber: The license number.
        :type LicenseNumber: str
        :param _Number: The resident registration number.
        :type Number: str
        :param _Type: The license class type.
        :type Type: str
        :param _Address: The address.
        :type Address: str
        :param _Name: The name.
        :type Name: str
        :param _AptitudeTesDate: The renewal period.
        :type AptitudeTesDate: str
        :param _DateOfIssue: The issue date.
        :type DateOfIssue: str
        :param _Photo: The Base64-encoded identity photo.
        :type Photo: str
        :param _Sex: The gender.
        :type Sex: str
        :param _Birthday: The birth date in the format of dd/mm/yyyy.
        :type Birthday: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._LicenseNumber = None
        self._Number = None
        self._Type = None
        self._Address = None
        self._Name = None
        self._AptitudeTesDate = None
        self._DateOfIssue = None
        self._Photo = None
        self._Sex = None
        self._Birthday = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AptitudeTesDate(self):
        return self._AptitudeTesDate

    @AptitudeTesDate.setter
    def AptitudeTesDate(self, AptitudeTesDate):
        self._AptitudeTesDate = AptitudeTesDate

    @property
    def DateOfIssue(self):
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue

    @property
    def Photo(self):
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._LicenseNumber = params.get("LicenseNumber")
        self._Number = params.get("Number")
        self._Type = params.get("Type")
        self._Address = params.get("Address")
        self._Name = params.get("Name")
        self._AptitudeTesDate = params.get("AptitudeTesDate")
        self._DateOfIssue = params.get("DateOfIssue")
        self._Photo = params.get("Photo")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._RequestId = params.get("RequestId")


class RecognizeKoreanIDCardOCRRequest(AbstractModel):
    """RecognizeKoreanIDCardOCR request structure.

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
    def ReturnHeadImage(self):
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
        


class RecognizeKoreanIDCardOCRResponse(AbstractModel):
    """RecognizeKoreanIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: The ID card number.
        :type ID: str
        :param _Address: The address.
        :type Address: str
        :param _Name: The name.
        :type Name: str
        :param _DateOfIssue: The issue date.
        :type DateOfIssue: str
        :param _Photo: The Base64-encoded identity photo.
        :type Photo: str
        :param _Sex: The gender.
        :type Sex: str
        :param _Birthday: The birth date in the format of dd/mm/yyyy.
        :type Birthday: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._Address = None
        self._Name = None
        self._DateOfIssue = None
        self._Photo = None
        self._Sex = None
        self._Birthday = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DateOfIssue(self):
        return self._DateOfIssue

    @DateOfIssue.setter
    def DateOfIssue(self, DateOfIssue):
        self._DateOfIssue = DateOfIssue

    @property
    def Photo(self):
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Address = params.get("Address")
        self._Name = params.get("Name")
        self._DateOfIssue = params.get("DateOfIssue")
        self._Photo = params.get("Photo")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesDrivingLicenseOCRRequest(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR request structure.

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
    def ReturnHeadImage(self):
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
    """RecognizePhilippinesDrivingLicenseOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Name: The full name.
        :type Name: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: The last name.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: The first name.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: The middle name.
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Nationality: The nationality.
        :type Nationality: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Sex: The gender.
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNo: The license No.
        :type LicenseNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _ExpiresDate: The expiration date.
        :type ExpiresDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _AgencyCode: The agency code.
        :type AgencyCode: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

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

    @property
    def RequestId(self):
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
    """RecognizePhilippinesSssIDOCR request structure.

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
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

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
    """RecognizePhilippinesSssIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: The common reference number (CRN).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: The full name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The date of birth.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._LicenseNumber = None
        self._FullName = None
        self._Birthday = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

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
    def RequestId(self):
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
    """RecognizePhilippinesTinIDOCR request structure.

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
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

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
    """RecognizePhilippinesTinIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: The tax identification number (TIN).
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: The name.
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: The address.
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: The birth date.
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _IssueDate: The issue date.
        :type IssueDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

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

    @property
    def RequestId(self):
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
    """RecognizePhilippinesUMIDOCR request structure.

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
    def ReturnHeadImage(self):
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
    """RecognizePhilippinesUMIDOCR response structure.

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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
    def CRN(self):
        return self._CRN

    @CRN.setter
    def CRN(self, CRN):
        self._CRN = CRN

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def RequestId(self):
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
    """RecognizePhilippinesVoteIDOCR request structure.

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
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

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
    """RecognizePhilippinesVoteIDOCR response structure.

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: The Base64-encoded identity photo.
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _VIN: The voter's identification number (VIN).
        :type VIN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: The first name.
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: The last name.
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._VIN = None
        self._FirstName = None
        self._LastName = None
        self._Birthday = None
        self._CivilStatus = None
        self._Citizenship = None
        self._Address = None
        self._PrecinctNo = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

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

    @property
    def RequestId(self):
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
        if params.get("FirstName") is not None:
            self._FirstName = TextDetectionResult()
            self._FirstName._deserialize(params.get("FirstName"))
        if params.get("LastName") is not None:
            self._LastName = TextDetectionResult()
            self._LastName._deserialize(params.get("LastName"))
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


class RecognizeTableAccurateOCRRequest(AbstractModel):
    """RecognizeTableAccurateOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image.
The image cannot exceed 7 MB after being Base64-encoded. A resolution above 600 x 800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
Supported image pixels: 20 to 10,000
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, only `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image or PDF file.
The image or PDF file cannot exceed 7 MB after being Base64-encoded. A resolution above 600 x 800 is recommended. PNG, JPG, JPEG, BMP, and PDF formats are supported.
Supported image pixels: 20 to 10,000
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param _PdfPageNumber: The number of the PDF page that needs to be recognized. Only one single PDF page can be recognized. This parameter is valid if the uploaded file is a PDF and the value of `IsPdf` is `true`. Default value: `1`.
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._PdfPageNumber = None

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
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTableAccurateOCRResponse(AbstractModel):
    """RecognizeTableAccurateOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TableDetections: The recognized text information. Please click the link on the left for details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableDetections: list of TableInfo
        :param _Data: Base64-encoded Excel data.
        :type Data: str
        :param _PdfPageSize: The total number of pages in the PDF file.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PdfPageSize: int
        :param _Angle: Image rotation angle in degrees. 0°: The horizontal direction of the text on the image; a negative value: rotate counterclockwise. Value range: -360° to 0°.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Angle: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TableDetections = None
        self._Data = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def TableDetections(self):
        return self._TableDetections

    @TableDetections.setter
    def TableDetections(self, TableDetections):
        self._TableDetections = TableDetections

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TableDetections") is not None:
            self._TableDetections = []
            for item in params.get("TableDetections"):
                obj = TableInfo()
                obj._deserialize(item)
                self._TableDetections.append(obj)
        self._Data = params.get("Data")
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class RecognizeThaiIDCardOCRRequest(AbstractModel):
    """RecognizeThaiIDCardOCR request structure.

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
    def CropPortrait(self):
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
        


class RecognizeThaiIDCardOCRResponse(AbstractModel):
    """RecognizeThaiIDCardOCR response structure.

    """

    def __init__(self):
        r"""
        :param _ID: ID card number
        :type ID: str
        :param _ThaiName: Name in Thai
        :type ThaiName: str
        :param _EnFirstName: Name in English
        :type EnFirstName: str
        :param _Address: Address
        :type Address: str
        :param _Birthday: Date of birth
        :type Birthday: str
        :param _IssueDate: Date of issue
        :type IssueDate: str
        :param _ExpirationDate: Expiration date
        :type ExpirationDate: str
        :param _EnLastName: Name in English
        :type EnLastName: str
        :param _PortraitImage: Identity photo
        :type PortraitImage: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._ThaiName = None
        self._EnFirstName = None
        self._Address = None
        self._Birthday = None
        self._IssueDate = None
        self._ExpirationDate = None
        self._EnLastName = None
        self._PortraitImage = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ThaiName(self):
        return self._ThaiName

    @ThaiName.setter
    def ThaiName(self, ThaiName):
        self._ThaiName = ThaiName

    @property
    def EnFirstName(self):
        return self._EnFirstName

    @EnFirstName.setter
    def EnFirstName(self, EnFirstName):
        self._EnFirstName = EnFirstName

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

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def EnLastName(self):
        return self._EnLastName

    @EnLastName.setter
    def EnLastName(self, EnLastName):
        self._EnLastName = EnLastName

    @property
    def PortraitImage(self):
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ThaiName = params.get("ThaiName")
        self._EnFirstName = params.get("EnFirstName")
        self._Address = params.get("Address")
        self._Birthday = params.get("Birthday")
        self._IssueDate = params.get("IssueDate")
        self._ExpirationDate = params.get("ExpirationDate")
        self._EnLastName = params.get("EnLastName")
        self._PortraitImage = params.get("PortraitImage")
        self._RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """Coordinates

    """

    def __init__(self):
        r"""
        :param _X: X-coordinate of top-left point
        :type X: int
        :param _Y: Y-coordinate of top-left point
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
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
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
        


class SealInfo(AbstractModel):
    """Seal information

    """

    def __init__(self):
        r"""
        :param _SealBody: Seal body information
        :type SealBody: str
        :param _Location: Seal coordinates
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _OtherTexts: Other text content
        :type OtherTexts: list of str
        :param _SealShape: Seal shape. Valid values:
0: Round
1: Oval
2: Rectangle
3: Diamond
4: Triangle
        :type SealShape: str
        """
        self._SealBody = None
        self._Location = None
        self._OtherTexts = None
        self._SealShape = None

    @property
    def SealBody(self):
        return self._SealBody

    @SealBody.setter
    def SealBody(self, SealBody):
        self._SealBody = SealBody

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def OtherTexts(self):
        return self._OtherTexts

    @OtherTexts.setter
    def OtherTexts(self, OtherTexts):
        self._OtherTexts = OtherTexts

    @property
    def SealShape(self):
        return self._SealShape

    @SealShape.setter
    def SealShape(self, SealShape):
        self._SealShape = SealShape


    def _deserialize(self, params):
        self._SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self._Location = Rect()
            self._Location._deserialize(params.get("Location"))
        self._OtherTexts = params.get("OtherTexts")
        self._SealShape = params.get("SealShape")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRRequest(AbstractModel):
    """SealOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: The Base64-encoded value of an image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image.
Either `ImageUrl` or `ImageBase64` of the image must be provided. If both are provided, `ImageUrl` is used.
        :type ImageBase64: str
        :param _ImageUrl: The URL of the image. The image cannot exceed 7 MB after being Base64-encoded. A resolution above 500 x 800 is recommended. PNG, JPG, JPEG, and BMP formats are supported. It is recommended that the card part occupy more than 2/3 area of the image. The download time of the image cannot exceed 3s.
We recommend that you store the image in Tencent Cloud for higher download speed and stability.
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

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
        


class SealOCRResponse(AbstractModel):
    """SealOCR response structure.

    """

    def __init__(self):
        r"""
        :param _SealBody: Seal content
        :type SealBody: str
        :param _Location: Seal coordinates
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _OtherTexts: Other text content
        :type OtherTexts: list of str
        :param _SealInfos: All seal information
        :type SealInfos: list of SealInfo
        :param _SealShape: Seal shape. Valid values:
0: Round
1: Oval
2: Rectangle
3: Diamond
4: Triangle
        :type SealShape: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SealBody = None
        self._Location = None
        self._OtherTexts = None
        self._SealInfos = None
        self._SealShape = None
        self._RequestId = None

    @property
    def SealBody(self):
        return self._SealBody

    @SealBody.setter
    def SealBody(self, SealBody):
        self._SealBody = SealBody

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def OtherTexts(self):
        return self._OtherTexts

    @OtherTexts.setter
    def OtherTexts(self, OtherTexts):
        self._OtherTexts = OtherTexts

    @property
    def SealInfos(self):
        return self._SealInfos

    @SealInfos.setter
    def SealInfos(self, SealInfos):
        self._SealInfos = SealInfos

    @property
    def SealShape(self):
        return self._SealShape

    @SealShape.setter
    def SealShape(self, SealShape):
        self._SealShape = SealShape

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self._Location = Rect()
            self._Location._deserialize(params.get("Location"))
        self._OtherTexts = params.get("OtherTexts")
        if params.get("SealInfos") is not None:
            self._SealInfos = []
            for item in params.get("SealInfos"):
                obj = SealInfo()
                obj._deserialize(item)
                self._SealInfos.append(obj)
        self._SealShape = params.get("SealShape")
        self._RequestId = params.get("RequestId")


class ShippingInvoice(AbstractModel):
    """Ship ticket

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _UserName: Name
        :type UserName: str
        :param _Date: Date
        :type Date: str
        :param _Time: Time
        :type Time: str
        :param _StationGetOn: Departure station
        :type StationGetOn: str
        :param _StationGetOff: Destination
        :type StationGetOff: str
        :param _Total: Fare
        :type Total: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _CurrencyCode: Currency
        :type CurrencyCode: str
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._UserName = None
        self._Date = None
        self._Time = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Total = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CurrencyCode = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._UserName = params.get("UserName")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CurrencyCode = params.get("CurrencyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleInvoiceItem(AbstractModel):
    """Content of a single invoice/ticket among multiple types of invoices/tickets

    """

    def __init__(self):
        r"""
        :param _VatSpecialInvoice: Special VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatCommonInvoice: General VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicCommonInvoice: Electronic general VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicSpecialInvoice: Electronic special VAT invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicInvoiceBlockchain: Blockchain electronic invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceBlockchain: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicInvoiceToll: Electronic general VAT invoice (toll)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceToll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicSpecialInvoiceFull: Electronic invoice (special)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicSpecialInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param _VatElectronicInvoiceFull: Electronic invoice (general)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatElectronicInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param _MachinePrintedInvoice: General machine-printed invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type MachinePrintedInvoice: :class:`tencentcloud.ocr.v20181119.models.MachinePrintedInvoice`
        :param _BusInvoice: Bus ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type BusInvoice: :class:`tencentcloud.ocr.v20181119.models.BusInvoice`
        :param _ShippingInvoice: Ship ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShippingInvoice: :class:`tencentcloud.ocr.v20181119.models.ShippingInvoice`
        :param _TollInvoice: Toll receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type TollInvoice: :class:`tencentcloud.ocr.v20181119.models.TollInvoice`
        :param _OtherInvoice: Other invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type OtherInvoice: :class:`tencentcloud.ocr.v20181119.models.OtherInvoice`
        :param _MotorVehicleSaleInvoice: Motor vehicle sales invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type MotorVehicleSaleInvoice: :class:`tencentcloud.ocr.v20181119.models.MotorVehicleSaleInvoice`
        :param _UsedCarPurchaseInvoice: Used car invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsedCarPurchaseInvoice: :class:`tencentcloud.ocr.v20181119.models.UsedCarPurchaseInvoice`
        :param _VatInvoiceRoll: General VAT invoice (roll)
Note: This field may return null, indicating that no valid values can be obtained.
        :type VatInvoiceRoll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceRoll`
        :param _TaxiTicket: Taxi receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaxiTicket: :class:`tencentcloud.ocr.v20181119.models.TaxiTicket`
        :param _QuotaInvoice: Quota invoice
Note: This field may return null, indicating that no valid values can be obtained.
        :type QuotaInvoice: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoice`
        :param _AirTransport: Itinerary/Receipt of e-ticket for air transportation
Note: This field may return null, indicating that no valid values can be obtained.
        :type AirTransport: :class:`tencentcloud.ocr.v20181119.models.AirTransport`
        :param _NonTaxIncomeGeneralBill: Non-tax revenue general receipt
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonTaxIncomeGeneralBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param _NonTaxIncomeElectronicBill: Non-tax revenue unified payment voucher
Note: This field may return null, indicating that no valid values can be obtained.
        :type NonTaxIncomeElectronicBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param _TrainTicket: Train ticket
Note: This field may return null, indicating that no valid values can be obtained.
        :type TrainTicket: :class:`tencentcloud.ocr.v20181119.models.TrainTicket`
        :param _MedicalOutpatientInvoice: 
        :type MedicalOutpatientInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        :param _MedicalHospitalizedInvoice: 
        :type MedicalHospitalizedInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        """
        self._VatSpecialInvoice = None
        self._VatCommonInvoice = None
        self._VatElectronicCommonInvoice = None
        self._VatElectronicSpecialInvoice = None
        self._VatElectronicInvoiceBlockchain = None
        self._VatElectronicInvoiceToll = None
        self._VatElectronicSpecialInvoiceFull = None
        self._VatElectronicInvoiceFull = None
        self._MachinePrintedInvoice = None
        self._BusInvoice = None
        self._ShippingInvoice = None
        self._TollInvoice = None
        self._OtherInvoice = None
        self._MotorVehicleSaleInvoice = None
        self._UsedCarPurchaseInvoice = None
        self._VatInvoiceRoll = None
        self._TaxiTicket = None
        self._QuotaInvoice = None
        self._AirTransport = None
        self._NonTaxIncomeGeneralBill = None
        self._NonTaxIncomeElectronicBill = None
        self._TrainTicket = None
        self._MedicalOutpatientInvoice = None
        self._MedicalHospitalizedInvoice = None

    @property
    def VatSpecialInvoice(self):
        return self._VatSpecialInvoice

    @VatSpecialInvoice.setter
    def VatSpecialInvoice(self, VatSpecialInvoice):
        self._VatSpecialInvoice = VatSpecialInvoice

    @property
    def VatCommonInvoice(self):
        return self._VatCommonInvoice

    @VatCommonInvoice.setter
    def VatCommonInvoice(self, VatCommonInvoice):
        self._VatCommonInvoice = VatCommonInvoice

    @property
    def VatElectronicCommonInvoice(self):
        return self._VatElectronicCommonInvoice

    @VatElectronicCommonInvoice.setter
    def VatElectronicCommonInvoice(self, VatElectronicCommonInvoice):
        self._VatElectronicCommonInvoice = VatElectronicCommonInvoice

    @property
    def VatElectronicSpecialInvoice(self):
        return self._VatElectronicSpecialInvoice

    @VatElectronicSpecialInvoice.setter
    def VatElectronicSpecialInvoice(self, VatElectronicSpecialInvoice):
        self._VatElectronicSpecialInvoice = VatElectronicSpecialInvoice

    @property
    def VatElectronicInvoiceBlockchain(self):
        return self._VatElectronicInvoiceBlockchain

    @VatElectronicInvoiceBlockchain.setter
    def VatElectronicInvoiceBlockchain(self, VatElectronicInvoiceBlockchain):
        self._VatElectronicInvoiceBlockchain = VatElectronicInvoiceBlockchain

    @property
    def VatElectronicInvoiceToll(self):
        return self._VatElectronicInvoiceToll

    @VatElectronicInvoiceToll.setter
    def VatElectronicInvoiceToll(self, VatElectronicInvoiceToll):
        self._VatElectronicInvoiceToll = VatElectronicInvoiceToll

    @property
    def VatElectronicSpecialInvoiceFull(self):
        return self._VatElectronicSpecialInvoiceFull

    @VatElectronicSpecialInvoiceFull.setter
    def VatElectronicSpecialInvoiceFull(self, VatElectronicSpecialInvoiceFull):
        self._VatElectronicSpecialInvoiceFull = VatElectronicSpecialInvoiceFull

    @property
    def VatElectronicInvoiceFull(self):
        return self._VatElectronicInvoiceFull

    @VatElectronicInvoiceFull.setter
    def VatElectronicInvoiceFull(self, VatElectronicInvoiceFull):
        self._VatElectronicInvoiceFull = VatElectronicInvoiceFull

    @property
    def MachinePrintedInvoice(self):
        return self._MachinePrintedInvoice

    @MachinePrintedInvoice.setter
    def MachinePrintedInvoice(self, MachinePrintedInvoice):
        self._MachinePrintedInvoice = MachinePrintedInvoice

    @property
    def BusInvoice(self):
        return self._BusInvoice

    @BusInvoice.setter
    def BusInvoice(self, BusInvoice):
        self._BusInvoice = BusInvoice

    @property
    def ShippingInvoice(self):
        return self._ShippingInvoice

    @ShippingInvoice.setter
    def ShippingInvoice(self, ShippingInvoice):
        self._ShippingInvoice = ShippingInvoice

    @property
    def TollInvoice(self):
        return self._TollInvoice

    @TollInvoice.setter
    def TollInvoice(self, TollInvoice):
        self._TollInvoice = TollInvoice

    @property
    def OtherInvoice(self):
        return self._OtherInvoice

    @OtherInvoice.setter
    def OtherInvoice(self, OtherInvoice):
        self._OtherInvoice = OtherInvoice

    @property
    def MotorVehicleSaleInvoice(self):
        return self._MotorVehicleSaleInvoice

    @MotorVehicleSaleInvoice.setter
    def MotorVehicleSaleInvoice(self, MotorVehicleSaleInvoice):
        self._MotorVehicleSaleInvoice = MotorVehicleSaleInvoice

    @property
    def UsedCarPurchaseInvoice(self):
        return self._UsedCarPurchaseInvoice

    @UsedCarPurchaseInvoice.setter
    def UsedCarPurchaseInvoice(self, UsedCarPurchaseInvoice):
        self._UsedCarPurchaseInvoice = UsedCarPurchaseInvoice

    @property
    def VatInvoiceRoll(self):
        return self._VatInvoiceRoll

    @VatInvoiceRoll.setter
    def VatInvoiceRoll(self, VatInvoiceRoll):
        self._VatInvoiceRoll = VatInvoiceRoll

    @property
    def TaxiTicket(self):
        return self._TaxiTicket

    @TaxiTicket.setter
    def TaxiTicket(self, TaxiTicket):
        self._TaxiTicket = TaxiTicket

    @property
    def QuotaInvoice(self):
        return self._QuotaInvoice

    @QuotaInvoice.setter
    def QuotaInvoice(self, QuotaInvoice):
        self._QuotaInvoice = QuotaInvoice

    @property
    def AirTransport(self):
        return self._AirTransport

    @AirTransport.setter
    def AirTransport(self, AirTransport):
        self._AirTransport = AirTransport

    @property
    def NonTaxIncomeGeneralBill(self):
        return self._NonTaxIncomeGeneralBill

    @NonTaxIncomeGeneralBill.setter
    def NonTaxIncomeGeneralBill(self, NonTaxIncomeGeneralBill):
        self._NonTaxIncomeGeneralBill = NonTaxIncomeGeneralBill

    @property
    def NonTaxIncomeElectronicBill(self):
        return self._NonTaxIncomeElectronicBill

    @NonTaxIncomeElectronicBill.setter
    def NonTaxIncomeElectronicBill(self, NonTaxIncomeElectronicBill):
        self._NonTaxIncomeElectronicBill = NonTaxIncomeElectronicBill

    @property
    def TrainTicket(self):
        return self._TrainTicket

    @TrainTicket.setter
    def TrainTicket(self, TrainTicket):
        self._TrainTicket = TrainTicket

    @property
    def MedicalOutpatientInvoice(self):
        return self._MedicalOutpatientInvoice

    @MedicalOutpatientInvoice.setter
    def MedicalOutpatientInvoice(self, MedicalOutpatientInvoice):
        self._MedicalOutpatientInvoice = MedicalOutpatientInvoice

    @property
    def MedicalHospitalizedInvoice(self):
        return self._MedicalHospitalizedInvoice

    @MedicalHospitalizedInvoice.setter
    def MedicalHospitalizedInvoice(self, MedicalHospitalizedInvoice):
        self._MedicalHospitalizedInvoice = MedicalHospitalizedInvoice


    def _deserialize(self, params):
        if params.get("VatSpecialInvoice") is not None:
            self._VatSpecialInvoice = VatInvoiceInfo()
            self._VatSpecialInvoice._deserialize(params.get("VatSpecialInvoice"))
        if params.get("VatCommonInvoice") is not None:
            self._VatCommonInvoice = VatInvoiceInfo()
            self._VatCommonInvoice._deserialize(params.get("VatCommonInvoice"))
        if params.get("VatElectronicCommonInvoice") is not None:
            self._VatElectronicCommonInvoice = VatInvoiceInfo()
            self._VatElectronicCommonInvoice._deserialize(params.get("VatElectronicCommonInvoice"))
        if params.get("VatElectronicSpecialInvoice") is not None:
            self._VatElectronicSpecialInvoice = VatInvoiceInfo()
            self._VatElectronicSpecialInvoice._deserialize(params.get("VatElectronicSpecialInvoice"))
        if params.get("VatElectronicInvoiceBlockchain") is not None:
            self._VatElectronicInvoiceBlockchain = VatInvoiceInfo()
            self._VatElectronicInvoiceBlockchain._deserialize(params.get("VatElectronicInvoiceBlockchain"))
        if params.get("VatElectronicInvoiceToll") is not None:
            self._VatElectronicInvoiceToll = VatInvoiceInfo()
            self._VatElectronicInvoiceToll._deserialize(params.get("VatElectronicInvoiceToll"))
        if params.get("VatElectronicSpecialInvoiceFull") is not None:
            self._VatElectronicSpecialInvoiceFull = VatElectronicInfo()
            self._VatElectronicSpecialInvoiceFull._deserialize(params.get("VatElectronicSpecialInvoiceFull"))
        if params.get("VatElectronicInvoiceFull") is not None:
            self._VatElectronicInvoiceFull = VatElectronicInfo()
            self._VatElectronicInvoiceFull._deserialize(params.get("VatElectronicInvoiceFull"))
        if params.get("MachinePrintedInvoice") is not None:
            self._MachinePrintedInvoice = MachinePrintedInvoice()
            self._MachinePrintedInvoice._deserialize(params.get("MachinePrintedInvoice"))
        if params.get("BusInvoice") is not None:
            self._BusInvoice = BusInvoice()
            self._BusInvoice._deserialize(params.get("BusInvoice"))
        if params.get("ShippingInvoice") is not None:
            self._ShippingInvoice = ShippingInvoice()
            self._ShippingInvoice._deserialize(params.get("ShippingInvoice"))
        if params.get("TollInvoice") is not None:
            self._TollInvoice = TollInvoice()
            self._TollInvoice._deserialize(params.get("TollInvoice"))
        if params.get("OtherInvoice") is not None:
            self._OtherInvoice = OtherInvoice()
            self._OtherInvoice._deserialize(params.get("OtherInvoice"))
        if params.get("MotorVehicleSaleInvoice") is not None:
            self._MotorVehicleSaleInvoice = MotorVehicleSaleInvoice()
            self._MotorVehicleSaleInvoice._deserialize(params.get("MotorVehicleSaleInvoice"))
        if params.get("UsedCarPurchaseInvoice") is not None:
            self._UsedCarPurchaseInvoice = UsedCarPurchaseInvoice()
            self._UsedCarPurchaseInvoice._deserialize(params.get("UsedCarPurchaseInvoice"))
        if params.get("VatInvoiceRoll") is not None:
            self._VatInvoiceRoll = VatInvoiceRoll()
            self._VatInvoiceRoll._deserialize(params.get("VatInvoiceRoll"))
        if params.get("TaxiTicket") is not None:
            self._TaxiTicket = TaxiTicket()
            self._TaxiTicket._deserialize(params.get("TaxiTicket"))
        if params.get("QuotaInvoice") is not None:
            self._QuotaInvoice = QuotaInvoice()
            self._QuotaInvoice._deserialize(params.get("QuotaInvoice"))
        if params.get("AirTransport") is not None:
            self._AirTransport = AirTransport()
            self._AirTransport._deserialize(params.get("AirTransport"))
        if params.get("NonTaxIncomeGeneralBill") is not None:
            self._NonTaxIncomeGeneralBill = NonTaxIncomeBill()
            self._NonTaxIncomeGeneralBill._deserialize(params.get("NonTaxIncomeGeneralBill"))
        if params.get("NonTaxIncomeElectronicBill") is not None:
            self._NonTaxIncomeElectronicBill = NonTaxIncomeBill()
            self._NonTaxIncomeElectronicBill._deserialize(params.get("NonTaxIncomeElectronicBill"))
        if params.get("TrainTicket") is not None:
            self._TrainTicket = TrainTicket()
            self._TrainTicket._deserialize(params.get("TrainTicket"))
        if params.get("MedicalOutpatientInvoice") is not None:
            self._MedicalOutpatientInvoice = MedicalInvoice()
            self._MedicalOutpatientInvoice._deserialize(params.get("MedicalOutpatientInvoice"))
        if params.get("MedicalHospitalizedInvoice") is not None:
            self._MedicalHospitalizedInvoice = MedicalInvoice()
            self._MedicalHospitalizedInvoice._deserialize(params.get("MedicalHospitalizedInvoice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRV2Request(AbstractModel):
    """SmartStructuralOCRV2 request structure.

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
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ItemNames(self):
        return self._ItemNames

    @ItemNames.setter
    def ItemNames(self, ItemNames):
        self._ItemNames = ItemNames

    @property
    def ReturnFullText(self):
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
    """SmartStructuralOCRV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Angle: The rotation angle (degrees) of the text on the image. 0: The text is horizontal. Positive value: The text is rotated clockwise. Negative value: The text is rotated counterclockwise.
        :type Angle: float
        :param _StructuralList: The structural information (key-value).
        :type StructuralList: list of GroupInfo
        :param _WordList: The recognized text information.
        :type WordList: list of WordItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Angle = None
        self._StructuralList = None
        self._WordList = None
        self._RequestId = None

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def StructuralList(self):
        return self._StructuralList

    @StructuralList.setter
    def StructuralList(self, StructuralList):
        self._StructuralList = StructuralList

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
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


class TableCellInfo(AbstractModel):
    """Cell data

    """

    def __init__(self):
        r"""
        :param _ColTl: Column index of the upper-left corner of the cell
        :type ColTl: int
        :param _RowTl: Row index of the upper-left corner of the cell
        :type RowTl: int
        :param _ColBr: Column index of the lower-right corner of the cell
        :type ColBr: int
        :param _RowBr: Row index of the lower-right corner of the cell
        :type RowBr: int
        :param _Text: Recognized string text within the cell. If there are multiple lines, they are separated by "\n".
        :type Text: str
        :param _Type: Cell type
        :type Type: str
        :param _Confidence: Cell confidence
        :type Confidence: float
        :param _Polygon: Four-point coordinates of the cell in the image
        :type Polygon: list of Coord
        """
        self._ColTl = None
        self._RowTl = None
        self._ColBr = None
        self._RowBr = None
        self._Text = None
        self._Type = None
        self._Confidence = None
        self._Polygon = None

    @property
    def ColTl(self):
        return self._ColTl

    @ColTl.setter
    def ColTl(self, ColTl):
        self._ColTl = ColTl

    @property
    def RowTl(self):
        return self._RowTl

    @RowTl.setter
    def RowTl(self, RowTl):
        self._RowTl = RowTl

    @property
    def ColBr(self):
        return self._ColBr

    @ColBr.setter
    def ColBr(self, ColBr):
        self._ColBr = ColBr

    @property
    def RowBr(self):
        return self._RowBr

    @RowBr.setter
    def RowBr(self, RowBr):
        self._RowBr = RowBr

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon


    def _deserialize(self, params):
        self._ColTl = params.get("ColTl")
        self._RowTl = params.get("RowTl")
        self._ColBr = params.get("ColBr")
        self._RowBr = params.get("RowBr")
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Confidence = params.get("Confidence")
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
        


class TableInfo(AbstractModel):
    """Recognized table information

    """

    def __init__(self):
        r"""
        :param _Cells: Cell content
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Cells: list of TableCellInfo
        :param _Type: Type of text in the image. Valid values:
0: Non-table text
1: Text in a bordered table
2: Text in a borderless table
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Type: int
        :param _TableCoordPoint: The coordinates of the four vertices (upper-left, upper-right, lower-right, and lower-left) of the table body.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableCoordPoint: list of Coord
        """
        self._Cells = None
        self._Type = None
        self._TableCoordPoint = None

    @property
    def Cells(self):
        return self._Cells

    @Cells.setter
    def Cells(self, Cells):
        self._Cells = Cells

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableCoordPoint(self):
        return self._TableCoordPoint

    @TableCoordPoint.setter
    def TableCoordPoint(self, TableCoordPoint):
        self._TableCoordPoint = TableCoordPoint


    def _deserialize(self, params):
        if params.get("Cells") is not None:
            self._Cells = []
            for item in params.get("Cells"):
                obj = TableCellInfo()
                obj._deserialize(item)
                self._Cells.append(obj)
        self._Type = params.get("Type")
        if params.get("TableCoordPoint") is not None:
            self._TableCoordPoint = []
            for item in params.get("TableCoordPoint"):
                obj = Coord()
                obj._deserialize(item)
                self._TableCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRRequest(AbstractModel):
    """TableOCR request structure.

    """

    def __init__(self):
        r"""
        :param _ImageBase64: Base64-encoded value of image.
Supported image formats: PNG, JPG, JPEG. GIF is not supported at present.
Supported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
Either `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param _ImageUrl: URL address of image. (This field is not supported outside Chinese mainland)
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 3 MB after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

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
        


class TableOCRResponse(AbstractModel):
    """TableOCR response structure.

    """

    def __init__(self):
        r"""
        :param _TextDetections: Recognized text. For more information, please click the link on the left
        :type TextDetections: list of TextTable
        :param _Data: Base64-encoded Excel data.
        :type Data: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TextDetections = None
        self._Data = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextTable()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class TaxiTicket(AbstractModel):
    """Taxi receipt

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Date: Date of issue
        :type Date: str
        :param _TimeGetOn: Start time
        :type TimeGetOn: str
        :param _TimeGetOff: End time
        :type TimeGetOff: str
        :param _Price: Unit price
        :type Price: str
        :param _Mileage: Distance
        :type Mileage: str
        :param _Total: Total amount
        :type Total: str
        :param _Place: Invoice place
        :type Place: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _LicensePlate: License plate number
        :type LicensePlate: str
        :param _FuelFee: Fuel surcharge
        :type FuelFee: str
        :param _BookingCallFee: Booking fee
        :type BookingCallFee: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._TimeGetOn = None
        self._TimeGetOff = None
        self._Price = None
        self._Mileage = None
        self._Total = None
        self._Place = None
        self._Province = None
        self._City = None
        self._Kind = None
        self._LicensePlate = None
        self._FuelFee = None
        self._BookingCallFee = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def TimeGetOff(self):
        return self._TimeGetOff

    @TimeGetOff.setter
    def TimeGetOff(self, TimeGetOff):
        self._TimeGetOff = TimeGetOff

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Mileage(self):
        return self._Mileage

    @Mileage.setter
    def Mileage(self, Mileage):
        self._Mileage = Mileage

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Place(self):
        return self._Place

    @Place.setter
    def Place(self, Place):
        self._Place = Place

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

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def FuelFee(self):
        return self._FuelFee

    @FuelFee.setter
    def FuelFee(self, FuelFee):
        self._FuelFee = FuelFee

    @property
    def BookingCallFee(self):
        return self._BookingCallFee

    @BookingCallFee.setter
    def BookingCallFee(self, BookingCallFee):
        self._BookingCallFee = BookingCallFee

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._TimeGetOn = params.get("TimeGetOn")
        self._TimeGetOff = params.get("TimeGetOff")
        self._Price = params.get("Price")
        self._Mileage = params.get("Mileage")
        self._Total = params.get("Total")
        self._Place = params.get("Place")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Kind = params.get("Kind")
        self._LicensePlate = params.get("LicensePlate")
        self._FuelFee = params.get("FuelFee")
        self._BookingCallFee = params.get("BookingCallFee")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetection(AbstractModel):
    """OCR result.

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
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def ItemPolygon(self):
        return self._ItemPolygon

    @ItemPolygon.setter
    def ItemPolygon(self, ItemPolygon):
        self._ItemPolygon = ItemPolygon

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def WordCoordPoint(self):
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
    """Recognition result

    """

    def __init__(self):
        r"""
        :param _Value: The recognized text line content.
        :type Value: str
        :param _Polygon: The coordinates, represented in the coordinates of the four points.
        :type Polygon: list of Coord
        """
        self._Value = None
        self._Polygon = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
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
        


class TextTable(AbstractModel):
    """Form recognition result.

    """

    def __init__(self):
        r"""
        :param _ColTl: Column index of the top-left corner of the cell.
        :type ColTl: int
        :param _RowTl: Row index of the top-left corner of the cell.
        :type RowTl: int
        :param _ColBr: Column index of the bottom-right corner of the cell.
        :type ColBr: int
        :param _RowBr: Row index of the bottom-right corner of the cell.
        :type RowBr: int
        :param _Text: Cell text
        :type Text: str
        :param _Type: Cell type. Valid values: body, header, footer
        :type Type: str
        :param _Confidence: Confidence. Value range: 0–100
        :type Confidence: int
        :param _Polygon: Text line coordinates, which are represented as 4 vertex coordinates.
        :type Polygon: list of Coord
        :param _AdvancedInfo: Extended field
        :type AdvancedInfo: str
        """
        self._ColTl = None
        self._RowTl = None
        self._ColBr = None
        self._RowBr = None
        self._Text = None
        self._Type = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None

    @property
    def ColTl(self):
        return self._ColTl

    @ColTl.setter
    def ColTl(self, ColTl):
        self._ColTl = ColTl

    @property
    def RowTl(self):
        return self._RowTl

    @RowTl.setter
    def RowTl(self, RowTl):
        self._RowTl = RowTl

    @property
    def ColBr(self):
        return self._ColBr

    @ColBr.setter
    def ColBr(self, ColBr):
        self._ColBr = ColBr

    @property
    def RowBr(self):
        return self._RowBr

    @RowBr.setter
    def RowBr(self, RowBr):
        self._RowBr = RowBr

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo


    def _deserialize(self, params):
        self._ColTl = params.get("ColTl")
        self._RowTl = params.get("RowTl")
        self._ColBr = params.get("ColBr")
        self._RowBr = params.get("RowBr")
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoice(AbstractModel):
    """Toll receipt

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Date: Date
        :type Date: str
        :param _Time: Time
        :type Time: str
        :param _Entrance: Entrance
        :type Entrance: str
        :param _Exit: Exit
        :type Exit: str
        :param _HighwayMark: Highway mark (0: No, 1: Yes)
        :type HighwayMark: int
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._Kind = None
        self._Date = None
        self._Time = None
        self._Entrance = None
        self._Exit = None
        self._HighwayMark = None
        self._QRCodeMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Entrance(self):
        return self._Entrance

    @Entrance.setter
    def Entrance(self, Entrance):
        self._Entrance = Entrance

    @property
    def Exit(self):
        return self._Exit

    @Exit.setter
    def Exit(self, Exit):
        self._Exit = Exit

    @property
    def HighwayMark(self):
        return self._HighwayMark

    @HighwayMark.setter
    def HighwayMark(self, HighwayMark):
        self._HighwayMark = HighwayMark

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._Entrance = params.get("Entrance")
        self._Exit = params.get("Exit")
        self._HighwayMark = params.get("HighwayMark")
        self._QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainTicket(AbstractModel):
    """Train ticket

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Number: Invoice number
        :type Number: str
        :param _DateGetOn: Departure date
        :type DateGetOn: str
        :param _TimeGetOn: Departure time
        :type TimeGetOn: str
        :param _Name: Passenger's name
        :type Name: str
        :param _StationGetOn: Departure station
        :type StationGetOn: str
        :param _StationGetOff: Destination
        :type StationGetOff: str
        :param _Seat: Seat class
        :type Seat: str
        :param _Total: Total amount
        :type Total: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _SerialNumber: Serial number
        :type SerialNumber: str
        :param _UserID: ID card number
        :type UserID: str
        :param _GateNumber: Check-in gate
        :type GateNumber: str
        :param _TrainNumber: Fleet number
        :type TrainNumber: str
        :param _HandlingFee: Handling fee
        :type HandlingFee: str
        :param _OriginalFare: Original ticket price
        :type OriginalFare: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _SeatNumber: Seat No.
        :type SeatNumber: str
        :param _PickUpAddress: Ticket pickup address
        :type PickUpAddress: str
        :param _TicketChange: Ticket change information
        :type TicketChange: str
        :param _AdditionalFare: Additional fare
        :type AdditionalFare: str
        :param _ReceiptNumber: Receipt No.
        :type ReceiptNumber: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _ReimburseOnlyMark: Whether it is for reimbursement only (0: No, 1: Yes)
        :type ReimburseOnlyMark: int
        """
        self._Title = None
        self._Number = None
        self._DateGetOn = None
        self._TimeGetOn = None
        self._Name = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Seat = None
        self._Total = None
        self._Kind = None
        self._SerialNumber = None
        self._UserID = None
        self._GateNumber = None
        self._TrainNumber = None
        self._HandlingFee = None
        self._OriginalFare = None
        self._TotalCn = None
        self._SeatNumber = None
        self._PickUpAddress = None
        self._TicketChange = None
        self._AdditionalFare = None
        self._ReceiptNumber = None
        self._QRCodeMark = None
        self._ReimburseOnlyMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Seat(self):
        return self._Seat

    @Seat.setter
    def Seat(self, Seat):
        self._Seat = Seat

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def GateNumber(self):
        return self._GateNumber

    @GateNumber.setter
    def GateNumber(self, GateNumber):
        self._GateNumber = GateNumber

    @property
    def TrainNumber(self):
        return self._TrainNumber

    @TrainNumber.setter
    def TrainNumber(self, TrainNumber):
        self._TrainNumber = TrainNumber

    @property
    def HandlingFee(self):
        return self._HandlingFee

    @HandlingFee.setter
    def HandlingFee(self, HandlingFee):
        self._HandlingFee = HandlingFee

    @property
    def OriginalFare(self):
        return self._OriginalFare

    @OriginalFare.setter
    def OriginalFare(self, OriginalFare):
        self._OriginalFare = OriginalFare

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def SeatNumber(self):
        return self._SeatNumber

    @SeatNumber.setter
    def SeatNumber(self, SeatNumber):
        self._SeatNumber = SeatNumber

    @property
    def PickUpAddress(self):
        return self._PickUpAddress

    @PickUpAddress.setter
    def PickUpAddress(self, PickUpAddress):
        self._PickUpAddress = PickUpAddress

    @property
    def TicketChange(self):
        return self._TicketChange

    @TicketChange.setter
    def TicketChange(self, TicketChange):
        self._TicketChange = TicketChange

    @property
    def AdditionalFare(self):
        return self._AdditionalFare

    @AdditionalFare.setter
    def AdditionalFare(self, AdditionalFare):
        self._AdditionalFare = AdditionalFare

    @property
    def ReceiptNumber(self):
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, ReceiptNumber):
        self._ReceiptNumber = ReceiptNumber

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def ReimburseOnlyMark(self):
        return self._ReimburseOnlyMark

    @ReimburseOnlyMark.setter
    def ReimburseOnlyMark(self, ReimburseOnlyMark):
        self._ReimburseOnlyMark = ReimburseOnlyMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._DateGetOn = params.get("DateGetOn")
        self._TimeGetOn = params.get("TimeGetOn")
        self._Name = params.get("Name")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Seat = params.get("Seat")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._SerialNumber = params.get("SerialNumber")
        self._UserID = params.get("UserID")
        self._GateNumber = params.get("GateNumber")
        self._TrainNumber = params.get("TrainNumber")
        self._HandlingFee = params.get("HandlingFee")
        self._OriginalFare = params.get("OriginalFare")
        self._TotalCn = params.get("TotalCn")
        self._SeatNumber = params.get("SeatNumber")
        self._PickUpAddress = params.get("PickUpAddress")
        self._TicketChange = params.get("TicketChange")
        self._AdditionalFare = params.get("AdditionalFare")
        self._ReceiptNumber = params.get("ReceiptNumber")
        self._QRCodeMark = params.get("QRCodeMark")
        self._ReimburseOnlyMark = params.get("ReimburseOnlyMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsedCarPurchaseInvoice(AbstractModel):
    """Used car sales invoice

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _Date: Date of issue
        :type Date: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTel: Seller's phone number
        :type SellerTel: str
        :param _SellerTaxID: Seller's company code/personal ID card number
        :type SellerTaxID: str
        :param _SellerAddress: Seller's address
        :type SellerAddress: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerID: Buyer's company code/personal ID card number
        :type BuyerID: str
        :param _BuyerAddress: Buyer's address
        :type BuyerAddress: str
        :param _BuyerTel: Buyer's phone number
        :type BuyerTel: str
        :param _CompanyName: Company (used car market) name
        :type CompanyName: str
        :param _CompanyTaxID: Company's taxpayer identification number
        :type CompanyTaxID: str
        :param _CompanyBankAccount: Company's account opening bank and account number
        :type CompanyBankAccount: str
        :param _CompanyTel: Company's phone number
        :type CompanyTel: str
        :param _CompanyAddress: Company's address
        :type CompanyAddress: str
        :param _TransferAdministrationName: Name of the transfer-to department of motor vehicles
        :type TransferAdministrationName: str
        :param _LicensePlate: License plate number
        :type LicensePlate: str
        :param _RegistrationNumber: Registration certificate No.
        :type RegistrationNumber: str
        :param _VIN: VIN
        :type VIN: str
        :param _VehicleModel: Vehicle model
        :type VehicleModel: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _VehicleType: Vehicle type
        :type VehicleType: str
        :param _Remark: Remarks
        :type Remark: str
        :param _FormType: Form type
        :type FormType: str
        :param _FormName: Form name
        :type FormName: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTel = None
        self._SellerTaxID = None
        self._SellerAddress = None
        self._Buyer = None
        self._BuyerID = None
        self._BuyerAddress = None
        self._BuyerTel = None
        self._CompanyName = None
        self._CompanyTaxID = None
        self._CompanyBankAccount = None
        self._CompanyTel = None
        self._CompanyAddress = None
        self._TransferAdministrationName = None
        self._LicensePlate = None
        self._RegistrationNumber = None
        self._VIN = None
        self._VehicleModel = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._VehicleType = None
        self._Remark = None
        self._FormType = None
        self._FormName = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerID(self):
        return self._BuyerID

    @BuyerID.setter
    def BuyerID(self, BuyerID):
        self._BuyerID = BuyerID

    @property
    def BuyerAddress(self):
        return self._BuyerAddress

    @BuyerAddress.setter
    def BuyerAddress(self, BuyerAddress):
        self._BuyerAddress = BuyerAddress

    @property
    def BuyerTel(self):
        return self._BuyerTel

    @BuyerTel.setter
    def BuyerTel(self, BuyerTel):
        self._BuyerTel = BuyerTel

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyTaxID(self):
        return self._CompanyTaxID

    @CompanyTaxID.setter
    def CompanyTaxID(self, CompanyTaxID):
        self._CompanyTaxID = CompanyTaxID

    @property
    def CompanyBankAccount(self):
        return self._CompanyBankAccount

    @CompanyBankAccount.setter
    def CompanyBankAccount(self, CompanyBankAccount):
        self._CompanyBankAccount = CompanyBankAccount

    @property
    def CompanyTel(self):
        return self._CompanyTel

    @CompanyTel.setter
    def CompanyTel(self, CompanyTel):
        self._CompanyTel = CompanyTel

    @property
    def CompanyAddress(self):
        return self._CompanyAddress

    @CompanyAddress.setter
    def CompanyAddress(self, CompanyAddress):
        self._CompanyAddress = CompanyAddress

    @property
    def TransferAdministrationName(self):
        return self._TransferAdministrationName

    @TransferAdministrationName.setter
    def TransferAdministrationName(self, TransferAdministrationName):
        self._TransferAdministrationName = TransferAdministrationName

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def VehicleModel(self):
        return self._VehicleModel

    @VehicleModel.setter
    def VehicleModel(self, VehicleModel):
        self._VehicleModel = VehicleModel

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTel = params.get("SellerTel")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddress = params.get("SellerAddress")
        self._Buyer = params.get("Buyer")
        self._BuyerID = params.get("BuyerID")
        self._BuyerAddress = params.get("BuyerAddress")
        self._BuyerTel = params.get("BuyerTel")
        self._CompanyName = params.get("CompanyName")
        self._CompanyTaxID = params.get("CompanyTaxID")
        self._CompanyBankAccount = params.get("CompanyBankAccount")
        self._CompanyTel = params.get("CompanyTel")
        self._CompanyAddress = params.get("CompanyAddress")
        self._TransferAdministrationName = params.get("TransferAdministrationName")
        self._LicensePlate = params.get("LicensePlate")
        self._RegistrationNumber = params.get("RegistrationNumber")
        self._VIN = params.get("VIN")
        self._VehicleModel = params.get("VehicleModel")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._VehicleType = params.get("VehicleType")
        self._Remark = params.get("Remark")
        self._FormType = params.get("FormType")
        self._FormName = params.get("FormName")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    """Value information

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
        return self._AutoContent

    @AutoContent.setter
    def AutoContent(self, AutoContent):
        self._AutoContent = AutoContent

    @property
    def Coord(self):
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
        


class VatElectronicInfo(AbstractModel):
    """Return values for an electronic invoice

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Number: Invoice number
        :type Number: str
        :param _Date: Date of issue
        :type Date: str
        :param _PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param _Tax: Tax
        :type Tax: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param _Issuer: Issuer
        :type Issuer: str
        :param _Remark: Remarks
        :type Remark: str
        :param _SubTotal: Subtotal amount
        :type SubTotal: str
        :param _SubTax: Subtotal tax
        :type SubTax: str
        :param _VatElectronicItems: Detailed items of an electronic invoice
        :type VatElectronicItems: list of VatElectronicItemInfo
        """
        self._Title = None
        self._Number = None
        self._Date = None
        self._PretaxAmount = None
        self._Tax = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTaxID = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Issuer = None
        self._Remark = None
        self._SubTotal = None
        self._SubTax = None
        self._VatElectronicItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SubTotal(self):
        return self._SubTotal

    @SubTotal.setter
    def SubTotal(self, SubTotal):
        self._SubTotal = SubTotal

    @property
    def SubTax(self):
        return self._SubTax

    @SubTax.setter
    def SubTax(self, SubTax):
        self._SubTax = SubTax

    @property
    def VatElectronicItems(self):
        return self._VatElectronicItems

    @VatElectronicItems.setter
    def VatElectronicItems(self, VatElectronicItems):
        self._VatElectronicItems = VatElectronicItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Tax = params.get("Tax")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Issuer = params.get("Issuer")
        self._Remark = params.get("Remark")
        self._SubTotal = params.get("SubTotal")
        self._SubTax = params.get("SubTax")
        if params.get("VatElectronicItems") is not None:
            self._VatElectronicItems = []
            for item in params.get("VatElectronicItems"):
                obj = VatElectronicItemInfo()
                obj._deserialize(item)
                self._VatElectronicItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatElectronicItemInfo(AbstractModel):
    """Detailed items of an electronic invoice

    """

    def __init__(self):
        r"""
        :param _Name: Item name
        :type Name: str
        :param _Quantity: Quantity
        :type Quantity: str
        :param _Specification: Specification
        :type Specification: str
        :param _Price: Unit price
        :type Price: str
        :param _Total: Amount
        :type Total: str
        :param _TaxRate: Tax rate
        :type TaxRate: str
        :param _Tax: Tax amount
        :type Tax: str
        :param _Unit: Unit
        :type Unit: str
        :param _VehicleType: Vehicle type
        :type VehicleType: str
        :param _VehicleBrand: Vehicle No.
        :type VehicleBrand: str
        :param _DeparturePlace: Departure place
        :type DeparturePlace: str
        :param _ArrivalPlace: Destination
        :type ArrivalPlace: str
        :param _TransportItemsName: Name of the transported goods. It is returned only for a goods transport service invoice.
        :type TransportItemsName: str
        :param _PlaceOfBuildingService: Location of the construction service. It is returned only for a construction invoice.
        :type PlaceOfBuildingService: str
        :param _BuildingName: Name of the construction project. It is returned only for a construction invoice.
        :type BuildingName: str
        :param _EstateNumber: Property or real estate ownership certificate No. It is returned only for a real estate operation and leasing service invoice.
        :type EstateNumber: str
        :param _AreaUnit: Unit of area. It is returned only for a real estate operation and leasing service invoice.
        :type AreaUnit: str
        """
        self._Name = None
        self._Quantity = None
        self._Specification = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None
        self._Unit = None
        self._VehicleType = None
        self._VehicleBrand = None
        self._DeparturePlace = None
        self._ArrivalPlace = None
        self._TransportItemsName = None
        self._PlaceOfBuildingService = None
        self._BuildingName = None
        self._EstateNumber = None
        self._AreaUnit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def VehicleBrand(self):
        return self._VehicleBrand

    @VehicleBrand.setter
    def VehicleBrand(self, VehicleBrand):
        self._VehicleBrand = VehicleBrand

    @property
    def DeparturePlace(self):
        return self._DeparturePlace

    @DeparturePlace.setter
    def DeparturePlace(self, DeparturePlace):
        self._DeparturePlace = DeparturePlace

    @property
    def ArrivalPlace(self):
        return self._ArrivalPlace

    @ArrivalPlace.setter
    def ArrivalPlace(self, ArrivalPlace):
        self._ArrivalPlace = ArrivalPlace

    @property
    def TransportItemsName(self):
        return self._TransportItemsName

    @TransportItemsName.setter
    def TransportItemsName(self, TransportItemsName):
        self._TransportItemsName = TransportItemsName

    @property
    def PlaceOfBuildingService(self):
        return self._PlaceOfBuildingService

    @PlaceOfBuildingService.setter
    def PlaceOfBuildingService(self, PlaceOfBuildingService):
        self._PlaceOfBuildingService = PlaceOfBuildingService

    @property
    def BuildingName(self):
        return self._BuildingName

    @BuildingName.setter
    def BuildingName(self, BuildingName):
        self._BuildingName = BuildingName

    @property
    def EstateNumber(self):
        return self._EstateNumber

    @EstateNumber.setter
    def EstateNumber(self, EstateNumber):
        self._EstateNumber = EstateNumber

    @property
    def AreaUnit(self):
        return self._AreaUnit

    @AreaUnit.setter
    def AreaUnit(self, AreaUnit):
        self._AreaUnit = AreaUnit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Quantity = params.get("Quantity")
        self._Specification = params.get("Specification")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        self._Unit = params.get("Unit")
        self._VehicleType = params.get("VehicleType")
        self._VehicleBrand = params.get("VehicleBrand")
        self._DeparturePlace = params.get("DeparturePlace")
        self._ArrivalPlace = params.get("ArrivalPlace")
        self._TransportItemsName = params.get("TransportItemsName")
        self._PlaceOfBuildingService = params.get("PlaceOfBuildingService")
        self._BuildingName = params.get("BuildingName")
        self._EstateNumber = params.get("EstateNumber")
        self._AreaUnit = params.get("AreaUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceInfo(AbstractModel):
    """Return values for a VAT invoice

    """

    def __init__(self):
        r"""
        :param _CheckCode: Check code
        :type CheckCode: str
        :param _FormType: Form type
        :type FormType: str
        :param _TravelTax: Vehicle and vessel tax
        :type TravelTax: str
        :param _BuyerAddrTel: Buyer's address and phone number
        :type BuyerAddrTel: str
        :param _BuyerBankAccount: Buyer's bank account number
        :type BuyerBankAccount: str
        :param _CompanySealContent: Company seal content
        :type CompanySealContent: str
        :param _TaxSealContent: Tax authority seal content
        :type TaxSealContent: str
        :param _ServiceName: Service type
        :type ServiceName: str
        :param _City: City
        :type City: str
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _AgentMark: Whether there is an agent (0: No, 1: Yes)
        :type AgentMark: int
        :param _TransitMark: Whether there is a toll (0: No, 1: Yes)
        :type TransitMark: int
        :param _OilMark: Whether there is refined oil (0: No, 1: Yes)
        :type OilMark: int
        :param _Title: Invoice title
        :type Title: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _NumberConfirm: Machine-printed invoice number
        :type NumberConfirm: str
        :param _Date: Date of issue
        :type Date: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _PretaxAmount: Amount before tax
        :type PretaxAmount: str
        :param _Tax: Tax
        :type Tax: str
        :param _MachineCode: Machine No.
        :type MachineCode: str
        :param _Ciphertext: Ciphertext
        :type Ciphertext: str
        :param _Remark: Remarks
        :type Remark: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param _SellerAddrTel: Seller's address and phone number
        :type SellerAddrTel: str
        :param _SellerBankAccount: Seller's bank account number
        :type SellerBankAccount: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param _Issuer: Issuer
        :type Issuer: str
        :param _Reviewer: Reviewer
        :type Reviewer: str
        :param _Province: Province
        :type Province: str
        :param _VatInvoiceItemInfos: Information about VAT invoice items
        :type VatInvoiceItemInfos: list of VatInvoiceItemInfo
        :param _CodeConfirm: Machine-printed invoice code
        :type CodeConfirm: str
        :param _Receiptor: Payee
        :type Receiptor: str
        :param _ElectronicFullMark: 
        :type ElectronicFullMark: int
        :param _ElectronicFullNumber: 
        :type ElectronicFullNumber: str
        :param _FormName: 
        :type FormName: str
        """
        self._CheckCode = None
        self._FormType = None
        self._TravelTax = None
        self._BuyerAddrTel = None
        self._BuyerBankAccount = None
        self._CompanySealContent = None
        self._TaxSealContent = None
        self._ServiceName = None
        self._City = None
        self._QRCodeMark = None
        self._AgentMark = None
        self._TransitMark = None
        self._OilMark = None
        self._Title = None
        self._Kind = None
        self._Code = None
        self._Number = None
        self._NumberConfirm = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._PretaxAmount = None
        self._Tax = None
        self._MachineCode = None
        self._Ciphertext = None
        self._Remark = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerAddrTel = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._CompanySealMark = None
        self._Issuer = None
        self._Reviewer = None
        self._Province = None
        self._VatInvoiceItemInfos = None
        self._CodeConfirm = None
        self._Receiptor = None
        self._ElectronicFullMark = None
        self._ElectronicFullNumber = None
        self._FormName = None

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def TravelTax(self):
        return self._TravelTax

    @TravelTax.setter
    def TravelTax(self, TravelTax):
        self._TravelTax = TravelTax

    @property
    def BuyerAddrTel(self):
        return self._BuyerAddrTel

    @BuyerAddrTel.setter
    def BuyerAddrTel(self, BuyerAddrTel):
        self._BuyerAddrTel = BuyerAddrTel

    @property
    def BuyerBankAccount(self):
        return self._BuyerBankAccount

    @BuyerBankAccount.setter
    def BuyerBankAccount(self, BuyerBankAccount):
        self._BuyerBankAccount = BuyerBankAccount

    @property
    def CompanySealContent(self):
        return self._CompanySealContent

    @CompanySealContent.setter
    def CompanySealContent(self, CompanySealContent):
        self._CompanySealContent = CompanySealContent

    @property
    def TaxSealContent(self):
        return self._TaxSealContent

    @TaxSealContent.setter
    def TaxSealContent(self, TaxSealContent):
        self._TaxSealContent = TaxSealContent

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def AgentMark(self):
        return self._AgentMark

    @AgentMark.setter
    def AgentMark(self, AgentMark):
        self._AgentMark = AgentMark

    @property
    def TransitMark(self):
        return self._TransitMark

    @TransitMark.setter
    def TransitMark(self, TransitMark):
        self._TransitMark = TransitMark

    @property
    def OilMark(self):
        return self._OilMark

    @OilMark.setter
    def OilMark(self, OilMark):
        self._OilMark = OilMark

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def NumberConfirm(self):
        return self._NumberConfirm

    @NumberConfirm.setter
    def NumberConfirm(self, NumberConfirm):
        self._NumberConfirm = NumberConfirm

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddrTel(self):
        return self._SellerAddrTel

    @SellerAddrTel.setter
    def SellerAddrTel(self, SellerAddrTel):
        self._SellerAddrTel = SellerAddrTel

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def VatInvoiceItemInfos(self):
        return self._VatInvoiceItemInfos

    @VatInvoiceItemInfos.setter
    def VatInvoiceItemInfos(self, VatInvoiceItemInfos):
        self._VatInvoiceItemInfos = VatInvoiceItemInfos

    @property
    def CodeConfirm(self):
        return self._CodeConfirm

    @CodeConfirm.setter
    def CodeConfirm(self, CodeConfirm):
        self._CodeConfirm = CodeConfirm

    @property
    def Receiptor(self):
        return self._Receiptor

    @Receiptor.setter
    def Receiptor(self, Receiptor):
        self._Receiptor = Receiptor

    @property
    def ElectronicFullMark(self):
        return self._ElectronicFullMark

    @ElectronicFullMark.setter
    def ElectronicFullMark(self, ElectronicFullMark):
        self._ElectronicFullMark = ElectronicFullMark

    @property
    def ElectronicFullNumber(self):
        return self._ElectronicFullNumber

    @ElectronicFullNumber.setter
    def ElectronicFullNumber(self, ElectronicFullNumber):
        self._ElectronicFullNumber = ElectronicFullNumber

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName


    def _deserialize(self, params):
        self._CheckCode = params.get("CheckCode")
        self._FormType = params.get("FormType")
        self._TravelTax = params.get("TravelTax")
        self._BuyerAddrTel = params.get("BuyerAddrTel")
        self._BuyerBankAccount = params.get("BuyerBankAccount")
        self._CompanySealContent = params.get("CompanySealContent")
        self._TaxSealContent = params.get("TaxSealContent")
        self._ServiceName = params.get("ServiceName")
        self._City = params.get("City")
        self._QRCodeMark = params.get("QRCodeMark")
        self._AgentMark = params.get("AgentMark")
        self._TransitMark = params.get("TransitMark")
        self._OilMark = params.get("OilMark")
        self._Title = params.get("Title")
        self._Kind = params.get("Kind")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._NumberConfirm = params.get("NumberConfirm")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Tax = params.get("Tax")
        self._MachineCode = params.get("MachineCode")
        self._Ciphertext = params.get("Ciphertext")
        self._Remark = params.get("Remark")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddrTel = params.get("SellerAddrTel")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._CompanySealMark = params.get("CompanySealMark")
        self._Issuer = params.get("Issuer")
        self._Reviewer = params.get("Reviewer")
        self._Province = params.get("Province")
        if params.get("VatInvoiceItemInfos") is not None:
            self._VatInvoiceItemInfos = []
            for item in params.get("VatInvoiceItemInfos"):
                obj = VatInvoiceItemInfo()
                obj._deserialize(item)
                self._VatInvoiceItemInfos.append(obj)
        self._CodeConfirm = params.get("CodeConfirm")
        self._Receiptor = params.get("Receiptor")
        self._ElectronicFullMark = params.get("ElectronicFullMark")
        self._ElectronicFullNumber = params.get("ElectronicFullNumber")
        self._FormName = params.get("FormName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceItemInfo(AbstractModel):
    """Information about VAT invoice items

    """

    def __init__(self):
        r"""
        :param _Name: Item name
        :type Name: str
        :param _Specification: Specification
        :type Specification: str
        :param _Unit: Unit
        :type Unit: str
        :param _Quantity: Quantity
        :type Quantity: str
        :param _Price: Unit price
        :type Price: str
        :param _Total: Amount
        :type Total: str
        :param _TaxRate: Tax rate
        :type TaxRate: str
        :param _Tax: Tax amount
        :type Tax: str
        :param _DateStart: Start date
        :type DateStart: str
        :param _DateEnd: End date
        :type DateEnd: str
        :param _LicensePlate: License plate number
        :type LicensePlate: str
        :param _VehicleType: Vehicle type
        :type VehicleType: str
        """
        self._Name = None
        self._Specification = None
        self._Unit = None
        self._Quantity = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None
        self._DateStart = None
        self._DateEnd = None
        self._LicensePlate = None
        self._VehicleType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def DateStart(self):
        return self._DateStart

    @DateStart.setter
    def DateStart(self, DateStart):
        self._DateStart = DateStart

    @property
    def DateEnd(self):
        return self._DateEnd

    @DateEnd.setter
    def DateEnd(self, DateEnd):
        self._DateEnd = DateEnd

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Specification = params.get("Specification")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        self._DateStart = params.get("DateStart")
        self._DateEnd = params.get("DateEnd")
        self._LicensePlate = params.get("LicensePlate")
        self._VehicleType = params.get("VehicleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceRoll(AbstractModel):
    """General VAT invoice (roll)

    """

    def __init__(self):
        r"""
        :param _Title: Invoice title
        :type Title: str
        :param _Code: Invoice code
        :type Code: str
        :param _Number: Invoice number
        :type Number: str
        :param _NumberConfirm: Machine-printed invoice number
        :type NumberConfirm: str
        :param _Date: Date of issue
        :type Date: str
        :param _CheckCode: Check code
        :type CheckCode: str
        :param _Seller: Seller's name
        :type Seller: str
        :param _SellerTaxID: Seller's taxpayer identification number
        :type SellerTaxID: str
        :param _Buyer: Buyer's name
        :type Buyer: str
        :param _BuyerTaxID: Buyer's taxpayer identification number
        :type BuyerTaxID: str
        :param _Category: Category
        :type Category: str
        :param _Total: Total amount (in figures)
        :type Total: str
        :param _TotalCn: Total amount (in words)
        :type TotalCn: str
        :param _Kind: Invoice type
        :type Kind: str
        :param _Province: Province
        :type Province: str
        :param _City: City
        :type City: str
        :param _CompanySealMark: Whether there is a company seal (0: No, 1: Yes)
        :type CompanySealMark: int
        :param _QRCodeMark: Whether there is a QR code (0: No, 1: Yes)
        :type QRCodeMark: int
        :param _ServiceName: Service type
        :type ServiceName: str
        :param _CompanySealContent: Company seal content
        :type CompanySealContent: str
        :param _TaxSealContent: Tax authority seal content
        :type TaxSealContent: str
        :param _VatRollItems: Items
        :type VatRollItems: list of VatRollItem
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._NumberConfirm = None
        self._Date = None
        self._CheckCode = None
        self._Seller = None
        self._SellerTaxID = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Category = None
        self._Total = None
        self._TotalCn = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CompanySealMark = None
        self._QRCodeMark = None
        self._ServiceName = None
        self._CompanySealContent = None
        self._TaxSealContent = None
        self._VatRollItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def NumberConfirm(self):
        return self._NumberConfirm

    @NumberConfirm.setter
    def NumberConfirm(self, NumberConfirm):
        self._NumberConfirm = NumberConfirm

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def CompanySealContent(self):
        return self._CompanySealContent

    @CompanySealContent.setter
    def CompanySealContent(self, CompanySealContent):
        self._CompanySealContent = CompanySealContent

    @property
    def TaxSealContent(self):
        return self._TaxSealContent

    @TaxSealContent.setter
    def TaxSealContent(self, TaxSealContent):
        self._TaxSealContent = TaxSealContent

    @property
    def VatRollItems(self):
        return self._VatRollItems

    @VatRollItems.setter
    def VatRollItems(self, VatRollItems):
        self._VatRollItems = VatRollItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._NumberConfirm = params.get("NumberConfirm")
        self._Date = params.get("Date")
        self._CheckCode = params.get("CheckCode")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Category = params.get("Category")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CompanySealMark = params.get("CompanySealMark")
        self._QRCodeMark = params.get("QRCodeMark")
        self._ServiceName = params.get("ServiceName")
        self._CompanySealContent = params.get("CompanySealContent")
        self._TaxSealContent = params.get("TaxSealContent")
        if params.get("VatRollItems") is not None:
            self._VatRollItems = []
            for item in params.get("VatRollItems"):
                obj = VatRollItem()
                obj._deserialize(item)
                self._VatRollItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollItem(AbstractModel):
    """Items of a general VAT invoice (roll)

    """

    def __init__(self):
        r"""
        :param _Name: Item name
        :type Name: str
        :param _Quantity: Quantity
        :type Quantity: str
        :param _Price: Unit price
        :type Price: str
        :param _Total: Amount
        :type Total: str
        """
        self._Name = None
        self._Quantity = None
        self._Price = None
        self._Total = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRRequest(AbstractModel):
    """VinOCR request structure.

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
    """VinOCR response structure.

    """

    def __init__(self):
        r"""
        :param _Vin: The detected VIN.
        :type Vin: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Vin = None
        self._RequestId = None

    @property
    def Vin(self):
        return self._Vin

    @Vin.setter
    def Vin(self, Vin):
        self._Vin = Vin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vin = params.get("Vin")
        self._RequestId = params.get("RequestId")


class WordItem(AbstractModel):
    """The recognized text information.

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
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Coord(self):
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
        