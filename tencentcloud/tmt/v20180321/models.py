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


class BoundingBox(AbstractModel):
    r"""Paragraph text box location: x, y represent the top-left corner, width and height represent width and height.

    """

    def __init__(self):
        r"""
        :param _X: <p>x-coordinate of the top-left corner</p>
        :type X: int
        :param _Y: <p>y-coordinate of the top-left corner</p>
        :type Y: int
        :param _Width: <p>Width.</p><p>Unit: px.</p>
        :type Width: int
        :param _Height: <p>High.</p><p>Unit: px.</p>
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""<p>x-coordinate of the top-left corner</p>
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""<p>y-coordinate of the top-left corner</p>
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""<p>Width.</p><p>Unit: px.</p>
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""<p>High.</p><p>Unit: px.</p>
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
        


class Coord(AbstractModel):
    r"""Coordinate details

    """

    def __init__(self):
        r"""
        :param _X: X coordinate
        :type X: int
        :param _Y: Y-axis coordinate
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""X coordinate
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y-axis coordinate
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
        


class ImageTranslateLLMRequest(AbstractModel):
    r"""ImageTranslateLLM request structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Base64 string of the image data, no more than 9M after Base64 encoding. A resolution of 600*800 or higher is recommended. PNG, JPG, and JPEG formats are supported.</p>
        :type Data: str
        :param _Target: <p>Target language, supported languages:</p><ul><li>Chinese: zh</li><li>Traditional (Taiwan): zh-TW</li><li>Traditional (Hong Kong (China)): zh-HK</li><li>English: en</li><li>Japanese: ja</li><li>Korean: ko</li><li>Thai: th</li><li>Vietnamese: vi</li><li>Russian: ru</li><li>German: de</li><li>French: fr</li><li>Arabic: ar</li><li>Spanish: es</li><li>Italian: it</li><li>Indonesian: id</li><li>Malay language: ms</li><li>Portuguese: pt</li><li>Turkish: tr<br>-</li></ul>
        :type Target: str
        :param _Url: <p>Enter image Url. When using a Url, the Data parameter requires the input of "". Image restrictions: less than 10MB, resolution recommendation 600*800 or higher, format support jpg, jpeg, png.</p>
        :type Url: str
        :param _Mode: <p>Invocation method.</p><p>Enumeration value:</p><ul><li>0: End-to-end image translation large model pro version</li><li>1: End-to-end image translation large model lite version</li></ul><p>Default value: 0</p>
        :type Mode: int
        """
        self._Data = None
        self._Target = None
        self._Url = None
        self._Mode = None

    @property
    def Data(self):
        r"""<p>Base64 string of the image data, no more than 9M after Base64 encoding. A resolution of 600*800 or higher is recommended. PNG, JPG, and JPEG formats are supported.</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Target(self):
        r"""<p>Target language, supported languages:</p><ul><li>Chinese: zh</li><li>Traditional (Taiwan): zh-TW</li><li>Traditional (Hong Kong (China)): zh-HK</li><li>English: en</li><li>Japanese: ja</li><li>Korean: ko</li><li>Thai: th</li><li>Vietnamese: vi</li><li>Russian: ru</li><li>German: de</li><li>French: fr</li><li>Arabic: ar</li><li>Spanish: es</li><li>Italian: it</li><li>Indonesian: id</li><li>Malay language: ms</li><li>Portuguese: pt</li><li>Turkish: tr<br>-</li></ul>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Url(self):
        r"""<p>Enter image Url. When using a Url, the Data parameter requires the input of "". Image restrictions: less than 10MB, resolution recommendation 600*800 or higher, format support jpg, jpeg, png.</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Mode(self):
        r"""<p>Invocation method.</p><p>Enumeration value:</p><ul><li>0: End-to-end image translation large model pro version</li><li>1: End-to-end image translation large model lite version</li></ul><p>Default value: 0</p>
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Target = params.get("Target")
        self._Url = params.get("Url")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateLLMResponse(AbstractModel):
    r"""ImageTranslateLLM response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Base64 string of the image data. The output format is JPG.</p>
        :type Data: str
        :param _Source: <p>Primary source language.</p>
        :type Source: str
        :param _Target: <p>Target translation language.</p>
        :type Target: str
        :param _SourceText: <p>All original text in the image.</p>
        :type SourceText: str
        :param _TargetText: <p>All translations in the image.</p>
        :type TargetText: str
        :param _Angle: <p>Image angle counterclockwise, value range 0-359</p>
        :type Angle: float
        :param _TransDetails: <p>Translation detailed information</p>
        :type TransDetails: list of TransDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Source = None
        self._Target = None
        self._SourceText = None
        self._TargetText = None
        self._Angle = None
        self._TransDetails = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Base64 string of the image data. The output format is JPG.</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Source(self):
        r"""<p>Primary source language.</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""<p>Target translation language.</p>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def SourceText(self):
        r"""<p>All original text in the image.</p>
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""<p>All translations in the image.</p>
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Angle(self):
        r"""<p>Image angle counterclockwise, value range 0-359</p>
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def TransDetails(self):
        r"""<p>Translation detailed information</p>
        :rtype: list of TransDetail
        """
        return self._TransDetails

    @TransDetails.setter
    def TransDetails(self, TransDetails):
        self._TransDetails = TransDetails

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
        self._Data = params.get("Data")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._Angle = params.get("Angle")
        if params.get("TransDetails") is not None:
            self._TransDetails = []
            for item in params.get("TransDetails"):
                obj = TransDetail()
                obj._deserialize(item)
                self._TransDetails.append(obj)
        self._RequestId = params.get("RequestId")


class RotateParagraphRect(AbstractModel):
    r"""Paragraph text rotation information

    """

    def __init__(self):
        r"""
        :param _Coord: Paragraph text coordinates
        :type Coord: list of Coord
        :param _TiltAngle: Rotation angle
        :type TiltAngle: float
        :param _Valid: Whether the paragraph text information is valid
        :type Valid: bool
        """
        self._Coord = None
        self._TiltAngle = None
        self._Valid = None

    @property
    def Coord(self):
        r"""Paragraph text coordinates
        :rtype: list of Coord
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord

    @property
    def TiltAngle(self):
        r"""Rotation angle
        :rtype: float
        """
        return self._TiltAngle

    @TiltAngle.setter
    def TiltAngle(self, TiltAngle):
        self._TiltAngle = TiltAngle

    @property
    def Valid(self):
        r"""Whether the paragraph text information is valid
        :rtype: bool
        """
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid


    def _deserialize(self, params):
        if params.get("Coord") is not None:
            self._Coord = []
            for item in params.get("Coord"):
                obj = Coord()
                obj._deserialize(item)
                self._Coord.append(obj)
        self._TiltAngle = params.get("TiltAngle")
        self._Valid = params.get("Valid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransDetail(AbstractModel):
    r"""Large model image translation detailed information

    """

    def __init__(self):
        r"""
        :param _SourceLineText: <p>Original text of the current row</p>
        :type SourceLineText: str
        :param _TargetLineText: <p>Translation of the current row</p>
        :type TargetLineText: str
        :param _BoundingBox: <p>Paragraph text box location</p>
        :type BoundingBox: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        :param _LinesCount: <p>Row count</p>
        :type LinesCount: int
        :param _LineHeight: <p>Line height.</p><p>Unit: px.</p>
        :type LineHeight: int
        :param _SpamCode: <p>The spam_code field is 0 in a normal paragraph; if the spam_code field exists and its value is above 0 (1: hit garbage check; 2: hit security policy; 3: another.), then the security check hit is filtered.</p>
        :type SpamCode: int
        :param _RotateParagraphRect: <p>Rotation information of paragraph text. Coordinates are valid only when valid is true.</p>
        :type RotateParagraphRect: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        self._SourceLineText = None
        self._TargetLineText = None
        self._BoundingBox = None
        self._LinesCount = None
        self._LineHeight = None
        self._SpamCode = None
        self._RotateParagraphRect = None

    @property
    def SourceLineText(self):
        r"""<p>Original text of the current row</p>
        :rtype: str
        """
        return self._SourceLineText

    @SourceLineText.setter
    def SourceLineText(self, SourceLineText):
        self._SourceLineText = SourceLineText

    @property
    def TargetLineText(self):
        r"""<p>Translation of the current row</p>
        :rtype: str
        """
        return self._TargetLineText

    @TargetLineText.setter
    def TargetLineText(self, TargetLineText):
        self._TargetLineText = TargetLineText

    @property
    def BoundingBox(self):
        r"""<p>Paragraph text box location</p>
        :rtype: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        """
        return self._BoundingBox

    @BoundingBox.setter
    def BoundingBox(self, BoundingBox):
        self._BoundingBox = BoundingBox

    @property
    def LinesCount(self):
        r"""<p>Row count</p>
        :rtype: int
        """
        return self._LinesCount

    @LinesCount.setter
    def LinesCount(self, LinesCount):
        self._LinesCount = LinesCount

    @property
    def LineHeight(self):
        r"""<p>Line height.</p><p>Unit: px.</p>
        :rtype: int
        """
        return self._LineHeight

    @LineHeight.setter
    def LineHeight(self, LineHeight):
        self._LineHeight = LineHeight

    @property
    def SpamCode(self):
        r"""<p>The spam_code field is 0 in a normal paragraph; if the spam_code field exists and its value is above 0 (1: hit garbage check; 2: hit security policy; 3: another.), then the security check hit is filtered.</p>
        :rtype: int
        """
        return self._SpamCode

    @SpamCode.setter
    def SpamCode(self, SpamCode):
        self._SpamCode = SpamCode

    @property
    def RotateParagraphRect(self):
        r"""<p>Rotation information of paragraph text. Coordinates are valid only when valid is true.</p>
        :rtype: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        return self._RotateParagraphRect

    @RotateParagraphRect.setter
    def RotateParagraphRect(self, RotateParagraphRect):
        self._RotateParagraphRect = RotateParagraphRect


    def _deserialize(self, params):
        self._SourceLineText = params.get("SourceLineText")
        self._TargetLineText = params.get("TargetLineText")
        if params.get("BoundingBox") is not None:
            self._BoundingBox = BoundingBox()
            self._BoundingBox._deserialize(params.get("BoundingBox"))
        self._LinesCount = params.get("LinesCount")
        self._LineHeight = params.get("LineHeight")
        self._SpamCode = params.get("SpamCode")
        if params.get("RotateParagraphRect") is not None:
            self._RotateParagraphRect = RotateParagraphRect()
            self._RotateParagraphRect._deserialize(params.get("RotateParagraphRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        