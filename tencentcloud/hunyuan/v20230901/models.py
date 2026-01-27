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


class ChatTranslationsRequest(AbstractModel):
    r"""ChatTranslations request structure.

    """

    def __init__(self):
        r"""
        :param _Model: Model name. optional values include hunyuan-translation.
Please read the introduction in [the product overview](https://www.tencentcloud.com/document/product/1284/75277) for model descriptions.

Note:
Different models have different pricing. according to [the purchase guide](https://www.tencentcloud.com/document/product/1284/77186), call as needed.
        :type Model: str
        :param _Stream: Streaming call switch.
Note:.
1. it defaults to non-streaming (false) when no value is passed.
2. for streaming calls, the results are incrementally returned via the SSE protocol (the return value is taken from Choices[n].Delta, and incremental data must be concatenated to obtain the complete result).
3. for non-streaming calls:.
The calling method is the same as an ordinary HTTP request.
The API response is time-consuming. if needed, set it to true for reduced latency.
Only return the final result once (return value takes the value from Choices[n].Message).

Note:.
When making an SDK call, streaming and non-streaming calls require **different ways** to obtain the return value. refer to the comments or sample code in the SDK (in the examples/hunyuan/v20230901/ directory of each language SDK code repository).
        :type Stream: bool
        :param _Text: Text to be translated.
        :type Text: str
        :param _Source: Source language.
Supported language list:. 
Simplified chinese: zh, traditional chinese: zh-TR, cantonese: yue, english: en, french: fr, portuguese: pt, spanish: es, japanese: ja, turkish: TR, russian: ru, arabic: ar, korean: ko, thai: th, italian: it, german: de, vietnamese: vi, malay: ms, indonesian: id.
The following languages are supported only by the hunyuan-translation model:.
Filipino: fil, hindi: hi, polish: pl, czech: cs, dutch: nl, khmer: km, burmese: my, persian: fa, gujarati: gu, urdu: ur, telugu: te, marathi: mr, hebrew: he, bengali: bn, tamil: ta, ukrainian: uk, tibetan: bo, kazakh: kk, mongolian: mn, uyghur: ug.
        :type Source: str
        :param _Target: Target language.
Supported language list:. 
Simplified chinese: zh, traditional chinese: zh-TR, cantonese: yue, english: en, french: fr, portuguese: pt, spanish: es, japanese: ja, turkish: TR, russian: ru, arabic: ar, korean: ko, thai: th, italian: it, german: de, vietnamese: vi, malay: ms, indonesian: id.
The following languages are supported only by the hunyuan-translation model:.
Filipino: fil, hindi: hi, polish: pl, czech: cs, dutch: nl, khmer: km, burmese: my, persian: fa, gujarati: gu, urdu: ur, telugu: te, marathi: mr, hebrew: he, bengali: bn, tamil: ta, ukrainian: uk, tibetan: bo, kazakh: kk, mongolian: mn, uyghur: ug.
        :type Target: str
        :param _Field: Domain of the text to be translated, such as game plot.
        :type Field: str
        :param _References: Reference example, up to 10.
        :type References: list of Reference
        """
        self._Model = None
        self._Stream = None
        self._Text = None
        self._Source = None
        self._Target = None
        self._Field = None
        self._References = None

    @property
    def Model(self):
        r"""Model name. optional values include hunyuan-translation.
Please read the introduction in [the product overview](https://www.tencentcloud.com/document/product/1284/75277) for model descriptions.

Note:
Different models have different pricing. according to [the purchase guide](https://www.tencentcloud.com/document/product/1284/77186), call as needed.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Stream(self):
        r"""Streaming call switch.
Note:.
1. it defaults to non-streaming (false) when no value is passed.
2. for streaming calls, the results are incrementally returned via the SSE protocol (the return value is taken from Choices[n].Delta, and incremental data must be concatenated to obtain the complete result).
3. for non-streaming calls:.
The calling method is the same as an ordinary HTTP request.
The API response is time-consuming. if needed, set it to true for reduced latency.
Only return the final result once (return value takes the value from Choices[n].Message).

Note:.
When making an SDK call, streaming and non-streaming calls require **different ways** to obtain the return value. refer to the comments or sample code in the SDK (in the examples/hunyuan/v20230901/ directory of each language SDK code repository).
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Text(self):
        r"""Text to be translated.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Source(self):
        r"""Source language.
Supported language list:. 
Simplified chinese: zh, traditional chinese: zh-TR, cantonese: yue, english: en, french: fr, portuguese: pt, spanish: es, japanese: ja, turkish: TR, russian: ru, arabic: ar, korean: ko, thai: th, italian: it, german: de, vietnamese: vi, malay: ms, indonesian: id.
The following languages are supported only by the hunyuan-translation model:.
Filipino: fil, hindi: hi, polish: pl, czech: cs, dutch: nl, khmer: km, burmese: my, persian: fa, gujarati: gu, urdu: ur, telugu: te, marathi: mr, hebrew: he, bengali: bn, tamil: ta, ukrainian: uk, tibetan: bo, kazakh: kk, mongolian: mn, uyghur: ug.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Target language.
Supported language list:. 
Simplified chinese: zh, traditional chinese: zh-TR, cantonese: yue, english: en, french: fr, portuguese: pt, spanish: es, japanese: ja, turkish: TR, russian: ru, arabic: ar, korean: ko, thai: th, italian: it, german: de, vietnamese: vi, malay: ms, indonesian: id.
The following languages are supported only by the hunyuan-translation model:.
Filipino: fil, hindi: hi, polish: pl, czech: cs, dutch: nl, khmer: km, burmese: my, persian: fa, gujarati: gu, urdu: ur, telugu: te, marathi: mr, hebrew: he, bengali: bn, tamil: ta, ukrainian: uk, tibetan: bo, kazakh: kk, mongolian: mn, uyghur: ug.
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Field(self):
        r"""Domain of the text to be translated, such as game plot.
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def References(self):
        r"""Reference example, up to 10.
        :rtype: list of Reference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Stream = params.get("Stream")
        self._Text = params.get("Text")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._Field = params.get("Field")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = Reference()
                obj._deserialize(item)
                self._References.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatTranslationsResponse(AbstractModel):
    r"""ChatTranslations response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Request'S RequestId this time.
        :type Id: str
        :param _Note: Disclaimer.
        :type Note: str
        :param _Created: Unix timestamp, in seconds.
        :type Created: int
        :param _Usage: Token statistical information.
Billing by Token quantity.
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Choices: Reply content.
        :type Choices: list of TranslationChoice
        :param _ErrorMsg: Error message.
If the service encounters an exception during streaming return, return this error.
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem. As a streaming response API, when the request is successfully completed, the RequestId will be placed in the Header "X-TC-RequestId" of the HTTP response.
        :type RequestId: str
        """
        self._Id = None
        self._Note = None
        self._Created = None
        self._Usage = None
        self._Choices = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Request'S RequestId this time.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Note(self):
        r"""Disclaimer.
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Created(self):
        r"""Unix timestamp, in seconds.
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        r"""Token statistical information.
Billing by Token quantity.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Choices(self):
        r"""Reply content.
        :rtype: list of TranslationChoice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        r"""Error message.
If the service encounters an exception during streaming return, return this error.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem. As a streaming response API, when the request is successfully completed, the RequestId will be placed in the Header "X-TC-RequestId" of the HTTP response.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Note = params.get("Note")
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = TranslationChoice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        self._RequestId = params.get("RequestId")


class Convert3DFormatRequest(AbstractModel):
    r"""Convert3DFormat request structure.

    """

    def __init__(self):
        r"""
        :param _File3D: 3D file url address. model file size not greater than 60 mb
Supports fbx, obj, and glb format 3d file input
        :type File3D: str
        :param _Format: Returns the 3D file format. valid values: 
STL, USDZ, FBX, MP4, GIF
Recommended input models below 50W, may timeout when selecting USDZ, MP4, or GIF format
Example value: STL.
        :type Format: str
        """
        self._File3D = None
        self._Format = None

    @property
    def File3D(self):
        r"""3D file url address. model file size not greater than 60 mb
Supports fbx, obj, and glb format 3d file input
        :rtype: str
        """
        return self._File3D

    @File3D.setter
    def File3D(self, File3D):
        self._File3D = File3D

    @property
    def Format(self):
        r"""Returns the 3D file format. valid values: 
STL, USDZ, FBX, MP4, GIF
Recommended input models below 50W, may timeout when selecting USDZ, MP4, or GIF format
Example value: STL.
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._File3D = params.get("File3D")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Convert3DFormatResponse(AbstractModel):
    r"""Convert3DFormat response structure.

    """

    def __init__(self):
        r"""
        :param _ResultFile3D: 3D file address
        :type ResultFile3D: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResultFile3D = None
        self._RequestId = None

    @property
    def ResultFile3D(self):
        r"""3D file address
        :rtype: str
        """
        return self._ResultFile3D

    @ResultFile3D.setter
    def ResultFile3D(self, ResultFile3D):
        self._ResultFile3D = ResultFile3D

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
        self._ResultFile3D = params.get("ResultFile3D")
        self._RequestId = params.get("RequestId")


class Describe3DSmartTopologyJobRequest(AbstractModel):
    r"""Describe3DSmartTopologyJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID.	
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""Task ID.	
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Describe3DSmartTopologyJobResponse(AbstractModel):
    r"""Describe3DSmartTopologyJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status. WAIT: waiting; RUN: running; FAIL: failed; DONE: successful. example value: RUN.	
        :type Status: str
        :param _ErrorCode: Error code.	
        :type ErrorCode: str
        :param _ErrorMessage: Error message.	
        :type ErrorMessage: str
        :param _ResultFile3Ds: File generation URL address, with a valid period of 1 day.	
        :type ResultFile3Ds: list of File3D
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status. WAIT: waiting; RUN: running; FAIL: failed; DONE: successful. example value: RUN.	
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""Error code.	
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""Error message.	
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""File generation URL address, with a valid period of 1 day.	
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class ErrorMsg(AbstractModel):
    r"""Runtime exception message.

    """

    def __init__(self):
        r"""
        :param _Msg: Error message.
        :type Msg: str
        :param _Code: Error code.
4000 internal service error.
4001 request model timeout.

        :type Code: int
        """
        self._Msg = None
        self._Code = None

    @property
    def Msg(self):
        r"""Error message.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        r"""Error code.
4000 internal service error.
4001 request model timeout.

        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File3D(AbstractModel):
    r"""3D file.

    """

    def __init__(self):
        r"""
        :param _Type: 3D file format. valid values: GIF, OBJ.
        :type Type: str
        :param _Url: Specifies the file Url (valid for 24 hours).
        :type Url: str
        :param _PreviewImageUrl: Preview image Url.
        :type PreviewImageUrl: str
        """
        self._Type = None
        self._Url = None
        self._PreviewImageUrl = None

    @property
    def Type(self):
        r"""3D file format. valid values: GIF, OBJ.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""Specifies the file Url (valid for 24 hours).
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PreviewImageUrl(self):
        r"""Preview image Url.
        :rtype: str
        """
        return self._PreviewImageUrl

    @PreviewImageUrl.setter
    def PreviewImageUrl(self, PreviewImageUrl):
        self._PreviewImageUrl = PreviewImageUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._PreviewImageUrl = params.get("PreviewImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputFile3D(AbstractModel):
    r"""3D file.

    """

    def __init__(self):
        r"""
        :param _Url: Specifies the file Url with a valid period of 24 hours.	
        :type Url: str
        :param _Type: Specifies the file format.	
        :type Type: str
        """
        self._Url = None
        self._Type = None

    @property
    def Url(self):
        r"""Specifies the file Url with a valid period of 24 hours.	
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        r"""Specifies the file format.	
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PromptTokensDetails(AbstractModel):
    r"""Specifies the detailed information of the input token.

    """

    def __init__(self):
        r"""
        :param _CachedTokens: The number of cache tokens.
        :type CachedTokens: str
        """
        self._CachedTokens = None

    @property
    def CachedTokens(self):
        r"""The number of cache tokens.
        :rtype: str
        """
        return self._CachedTokens

    @CachedTokens.setter
    def CachedTokens(self, CachedTokens):
        self._CachedTokens = CachedTokens


    def _deserialize(self, params):
        self._CachedTokens = params.get("CachedTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuan3DPartJobRequest(AbstractModel):
    r"""QueryHunyuan3DPartJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuan3DPartJobResponse(AbstractModel):
    r"""QueryHunyuan3DPartJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status:
WAIT: waiting
RUN: running
FAIL: failed
DONE: successful
Example value: RUN
        :type Status: str
        :param _ErrorCode: Error code
        :type ErrorCode: str
        :param _ErrorMessage: Error message
        :type ErrorMessage: str
        :param _ResultFile3Ds: Generates the file URL with a valid period of 1 day
        :type ResultFile3Ds: list of File3D
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status:
WAIT: waiting
RUN: running
FAIL: failed
DONE: successful
Example value: RUN
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""Error code
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""Error message
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""Generates the file URL with a valid period of 1 day
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class QueryHunyuanTo3DProJobRequest(AbstractModel):
    r"""QueryHunyuanTo3DProJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID.
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DProJobResponse(AbstractModel):
    r"""QueryHunyuanTo3DProJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status:
WAIT: waiting
RUN: running; FAIL: failed
DONE: successful
        :type Status: str
        :param _ErrorCode: Error code
        :type ErrorCode: str
        :param _ErrorMessage: Error message
        :type ErrorMessage: str
        :param _ResultFile3Ds: Describes the generated 3d file array
        :type ResultFile3Ds: list of File3D
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status:
WAIT: waiting
RUN: running; FAIL: failed
DONE: successful
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""Error code
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""Error message
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""Describes the generated 3d file array
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class QueryHunyuanTo3DRapidJobRequest(AbstractModel):
    r"""QueryHunyuanTo3DRapidJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID.	
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""Task ID.	
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DRapidJobResponse(AbstractModel):
    r"""QueryHunyuanTo3DRapidJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status:
WAIT: waiting
RUN: running
FAIL: failed
DONE: successful	
        :type Status: str
        :param _ErrorCode: Error code
        :type ErrorCode: str
        :param _ErrorMessage: Error message	
        :type ErrorMessage: str
        :param _ResultFile3Ds: Specifies the generated 3D file array
        :type ResultFile3Ds: list of File3D
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status:
WAIT: waiting
RUN: running
FAIL: failed
DONE: successful	
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""Error code
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""Error message	
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""Specifies the generated 3D file array
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class Reference(AbstractModel):
    r"""Translate dialogue reference example.

    """

    def __init__(self):
        r"""
        :param _Type: Translate text type, enumerate "sentence" means sentence, "term" means terminology.
        :type Type: str
        :param _Text: Original.
        :type Text: str
        :param _Translation: Translation.
        :type Translation: str
        """
        self._Type = None
        self._Text = None
        self._Translation = None

    @property
    def Type(self):
        r"""Translate text type, enumerate "sentence" means sentence, "term" means terminology.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Text(self):
        r"""Original.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Translation(self):
        r"""Translation.
        :rtype: str
        """
        return self._Translation

    @Translation.setter
    def Translation(self, Translation):
        self._Translation = Translation


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Text = params.get("Text")
        self._Translation = params.get("Translation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Submit3DSmartTopologyJobRequest(AbstractModel):
    r"""Submit3DSmartTopologyJob request structure.

    """

    def __init__(self):
        r"""
        :param _File3D: Source 3D file model link
Reference value:glb,obj
One of the file formats is required.
Url: file size cannot exceed 200MB.
3D model requirements: complex models and topologized models do not support face reduction. recommended input is non-topologized high-poly models, such as those generated by hunyuan 3d. high applicability categories include hard surface, game character, prop, daily objects.
        :type File3D: :class:`tencentcloud.hunyuan.v20230901.models.InputFile3D`
        :param _PolygonType: Polygon type, indicates the model surface is composed of grid components, defaults to triangle
Reference value:
triangle: triangle face
quadrilateral: triangular and quadrilateral mixed face
        :type PolygonType: str
        :param _FaceLevel: Reduction level bit type
valid values: high, medium, low
        :type FaceLevel: str
        """
        self._File3D = None
        self._PolygonType = None
        self._FaceLevel = None

    @property
    def File3D(self):
        r"""Source 3D file model link
Reference value:glb,obj
One of the file formats is required.
Url: file size cannot exceed 200MB.
3D model requirements: complex models and topologized models do not support face reduction. recommended input is non-topologized high-poly models, such as those generated by hunyuan 3d. high applicability categories include hard surface, game character, prop, daily objects.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.InputFile3D`
        """
        return self._File3D

    @File3D.setter
    def File3D(self, File3D):
        self._File3D = File3D

    @property
    def PolygonType(self):
        r"""Polygon type, indicates the model surface is composed of grid components, defaults to triangle
Reference value:
triangle: triangle face
quadrilateral: triangular and quadrilateral mixed face
        :rtype: str
        """
        return self._PolygonType

    @PolygonType.setter
    def PolygonType(self, PolygonType):
        self._PolygonType = PolygonType

    @property
    def FaceLevel(self):
        r"""Reduction level bit type
valid values: high, medium, low
        :rtype: str
        """
        return self._FaceLevel

    @FaceLevel.setter
    def FaceLevel(self, FaceLevel):
        self._FaceLevel = FaceLevel


    def _deserialize(self, params):
        if params.get("File3D") is not None:
            self._File3D = InputFile3D()
            self._File3D._deserialize(params.get("File3D"))
        self._PolygonType = params.get("PolygonType")
        self._FaceLevel = params.get("FaceLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Submit3DSmartTopologyJobResponse(AbstractModel):
    r"""Submit3DSmartTopologyJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID.	
        :type JobId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""Task ID.	
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuan3DPartJobRequest(AbstractModel):
    r"""SubmitHunyuan3DPartJob request structure.

    """

    def __init__(self):
        r"""
        :param _File: Recommends inputting 3D models generated by AIGC
Recommended file size not greater than 100MB
Face count not greater than 30,000
Only supports FBX format
        :type File: :class:`tencentcloud.hunyuan.v20230901.models.InputFile3D`
        """
        self._File = None

    @property
    def File(self):
        r"""Recommends inputting 3D models generated by AIGC
Recommended file size not greater than 100MB
Face count not greater than 30,000
Only supports FBX format
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.InputFile3D`
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        if params.get("File") is not None:
            self._File = InputFile3D()
            self._File._deserialize(params.get("File"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuan3DPartJobResponse(AbstractModel):
    r"""SubmitHunyuan3DPartJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task id (valid period: 24 hours)
        :type JobId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""Task id (valid period: 24 hours)
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanTo3DProJobRequest(AbstractModel):
    r"""SubmitHunyuanTo3DProJob request structure.

    """

    def __init__(self):
        r"""
        :param _Model: Tencent HY 3D Global model version
Defaults to 3.0, with optional choices: 3.0, 3.1
When selecting version 3.1, the [LowPoly] and [Sketch] parameter is unavailable
Example value:3.0
        :type Model: str
        :param _Prompt: Generates 3D content, describes 3D content.
Supports up to 1024 utf-8 characters.
Text-To-3D. Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :type Prompt: str
        :param _ImageBase64: Enter the Base64 code of the image.
Size: specifies the unilateral resolution requirement, not less than 128 and not greater than 5000. size should not exceed 8m (after encoding, it increases by about 30%, recommend actual input image size no more than 6m).
Input image suggestion:
1.Simple background (solid-color background) 
2.No text or blended colors
3.Single object
4.The object occupies over 50% of the frame
Valid values: jpg, png, jpeg, webp.
Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :type ImageBase64: str
        :param _ImageUrl: Input image Url.
Size: specifies the unilateral resolution requirement, not less than 128 and not greater than 5000. size should not exceed 8m (after encoding, it increases by about 30%, recommend actual input image size no more than 6m).
Input image suggestion:
1.Simple background (solid-color background) 
2.No text or blended colors
3.Single object
4.The object occupies over 50% of the frame
Valid values: jpg, png, jpeg, webp.
Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :type ImageUrl: str
        :param _MultiViewImages: Multi-Perspective model image. reference value for viewing angle:.
left: Left view;
right: Right view;
back: Rear view;
top: Top view (only supported in Model 3.1);
bottom: Bottom view (only supported in Model 3.1);
left_front: Left front 45 degree view (only supported in Model 3.1);
right_front: Right front 45 degree view (only supported in Model 3.1);

Each perspective is limited to one image.
Image size limit. the value must not exceed 8 mb after encoding.
Image resolution limitation: the unilateral resolution should be less than 5000 and greater than 128.
Supported image format: JPG or PNG
        :type MultiViewImages: list of ViewImage
        :param _EnablePBR: Specifies whether PBR material generation is enabled. default false
        :type EnablePBR: bool
        :param _FaceCount: Specifies the face count for 3D model generation. default value is 500000.
Specifies the supported face count generation range. value range: 40000-1500000
        :type FaceCount: int
        :param _GenerateType: Generation task type. default: Normal. valid values:
Normal: generates a geometric model with textures
LowPoly: specifies the model generated after intelligent polygon reduction.
Geometry: specifies whether to generate a Geometry model without textures (white model). when this task is selected, the EnablePBR parameter does not take effect
Specifies the Sketch for the generative model, allowing input of a Sketch or line drawing. in this mode, both prompt and ImageUrl/ImageBase64 can be entered together
        :type GenerateType: str
        :param _PolygonType: This parameter only takes effect when LowPoly mode is selected from GenerateType

Polygon type, indicates the number of sides in the model's surface grid, defaults to triangle. valid values:
triangle. specifies the triangular face
quadrilateral: mix quadrangle and triangle faces to generate
        :type PolygonType: str
        """
        self._Model = None
        self._Prompt = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._MultiViewImages = None
        self._EnablePBR = None
        self._FaceCount = None
        self._GenerateType = None
        self._PolygonType = None

    @property
    def Model(self):
        r"""Tencent HY 3D Global model version
Defaults to 3.0, with optional choices: 3.0, 3.1
When selecting version 3.1, the [LowPoly] and [Sketch] parameter is unavailable
Example value:3.0
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Prompt(self):
        r"""Generates 3D content, describes 3D content.
Supports up to 1024 utf-8 characters.
Text-To-3D. Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        r"""Enter the Base64 code of the image.
Size: specifies the unilateral resolution requirement, not less than 128 and not greater than 5000. size should not exceed 8m (after encoding, it increases by about 30%, recommend actual input image size no more than 6m).
Input image suggestion:
1.Simple background (solid-color background) 
2.No text or blended colors
3.Single object
4.The object occupies over 50% of the frame
Valid values: jpg, png, jpeg, webp.
Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""Input image Url.
Size: specifies the unilateral resolution requirement, not less than 128 and not greater than 5000. size should not exceed 8m (after encoding, it increases by about 30%, recommend actual input image size no more than 6m).
Input image suggestion:
1.Simple background (solid-color background) 
2.No text or blended colors
3.Single object
4.The object occupies over 50% of the frame
Valid values: jpg, png, jpeg, webp.
Specifies either ImageBase64/ImageUrl or Prompt is required. Prompt and ImageBase64/ImageUrl cannot coexist.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def MultiViewImages(self):
        r"""Multi-Perspective model image. reference value for viewing angle:.
left: Left view;
right: Right view;
back: Rear view;
top: Top view (only supported in Model 3.1);
bottom: Bottom view (only supported in Model 3.1);
left_front: Left front 45 degree view (only supported in Model 3.1);
right_front: Right front 45 degree view (only supported in Model 3.1);

Each perspective is limited to one image.
Image size limit. the value must not exceed 8 mb after encoding.
Image resolution limitation: the unilateral resolution should be less than 5000 and greater than 128.
Supported image format: JPG or PNG
        :rtype: list of ViewImage
        """
        return self._MultiViewImages

    @MultiViewImages.setter
    def MultiViewImages(self, MultiViewImages):
        self._MultiViewImages = MultiViewImages

    @property
    def EnablePBR(self):
        r"""Specifies whether PBR material generation is enabled. default false
        :rtype: bool
        """
        return self._EnablePBR

    @EnablePBR.setter
    def EnablePBR(self, EnablePBR):
        self._EnablePBR = EnablePBR

    @property
    def FaceCount(self):
        r"""Specifies the face count for 3D model generation. default value is 500000.
Specifies the supported face count generation range. value range: 40000-1500000
        :rtype: int
        """
        return self._FaceCount

    @FaceCount.setter
    def FaceCount(self, FaceCount):
        self._FaceCount = FaceCount

    @property
    def GenerateType(self):
        r"""Generation task type. default: Normal. valid values:
Normal: generates a geometric model with textures
LowPoly: specifies the model generated after intelligent polygon reduction.
Geometry: specifies whether to generate a Geometry model without textures (white model). when this task is selected, the EnablePBR parameter does not take effect
Specifies the Sketch for the generative model, allowing input of a Sketch or line drawing. in this mode, both prompt and ImageUrl/ImageBase64 can be entered together
        :rtype: str
        """
        return self._GenerateType

    @GenerateType.setter
    def GenerateType(self, GenerateType):
        self._GenerateType = GenerateType

    @property
    def PolygonType(self):
        r"""This parameter only takes effect when LowPoly mode is selected from GenerateType

Polygon type, indicates the number of sides in the model's surface grid, defaults to triangle. valid values:
triangle. specifies the triangular face
quadrilateral: mix quadrangle and triangle faces to generate
        :rtype: str
        """
        return self._PolygonType

    @PolygonType.setter
    def PolygonType(self, PolygonType):
        self._PolygonType = PolygonType


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Prompt = params.get("Prompt")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        if params.get("MultiViewImages") is not None:
            self._MultiViewImages = []
            for item in params.get("MultiViewImages"):
                obj = ViewImage()
                obj._deserialize(item)
                self._MultiViewImages.append(obj)
        self._EnablePBR = params.get("EnablePBR")
        self._FaceCount = params.get("FaceCount")
        self._GenerateType = params.get("GenerateType")
        self._PolygonType = params.get("PolygonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DProJobResponse(AbstractModel):
    r"""SubmitHunyuanTo3DProJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID (valid period: 24 hours).
        :type JobId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""Task ID (valid period: 24 hours).
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanTo3DRapidJobRequest(AbstractModel):
    r"""SubmitHunyuanTo3DRapidJob request structure.

    """

    def __init__(self):
        r"""
        :param _Prompt: Text-To-3D, description of 3D content, forward Prompt content
Supports up to 200 utf-8 characters
Either ImageBase64, ImageUrl, or Prompt is required, and Prompt cannot coexist with ImageBase64/ImageUrl
        :type Prompt: str
        :param _ImageBase64: Input image Base64 data
Size: unilateral resolution requirement not less than 128, not greater than 5000, size not greater than 6mb (after encoding, size increases by approximately 30%). format:
jpg, png, jpeg, webp
Imagebase64, imageurl, and Prompt are required, but Prompt and imagebase64/imageurl cannot coexist
        :type ImageBase64: str
        :param _ImageUrl: Input image Url size: 
Unilateral resolution requirement not less than 128, not greater than 5000. size not greater than 8mb
Format: jpg, png, jpeg, webp
Imagebase64, imageurl, and Prompt are required, and Prompt cannot coexist with imagebase64/imageurl	
        :type ImageUrl: str
        :param _EnablePBR: Specifies whether PBR material generation is enabled, false by default.	
        :type EnablePBR: bool
        :param _EnableGeometry: Specifies whether to enable the single geometry generation option
When enabled, it generates a 3D model without textures (white model)
When enabled, the generative model does not support OBJ format
Default model file format is GLB
        :type EnableGeometry: bool
        """
        self._Prompt = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._EnablePBR = None
        self._EnableGeometry = None

    @property
    def Prompt(self):
        r"""Text-To-3D, description of 3D content, forward Prompt content
Supports up to 200 utf-8 characters
Either ImageBase64, ImageUrl, or Prompt is required, and Prompt cannot coexist with ImageBase64/ImageUrl
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        r"""Input image Base64 data
Size: unilateral resolution requirement not less than 128, not greater than 5000, size not greater than 6mb (after encoding, size increases by approximately 30%). format:
jpg, png, jpeg, webp
Imagebase64, imageurl, and Prompt are required, but Prompt and imagebase64/imageurl cannot coexist
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""Input image Url size: 
Unilateral resolution requirement not less than 128, not greater than 5000. size not greater than 8mb
Format: jpg, png, jpeg, webp
Imagebase64, imageurl, and Prompt are required, and Prompt cannot coexist with imagebase64/imageurl	
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def EnablePBR(self):
        r"""Specifies whether PBR material generation is enabled, false by default.	
        :rtype: bool
        """
        return self._EnablePBR

    @EnablePBR.setter
    def EnablePBR(self, EnablePBR):
        self._EnablePBR = EnablePBR

    @property
    def EnableGeometry(self):
        r"""Specifies whether to enable the single geometry generation option
When enabled, it generates a 3D model without textures (white model)
When enabled, the generative model does not support OBJ format
Default model file format is GLB
        :rtype: bool
        """
        return self._EnableGeometry

    @EnableGeometry.setter
    def EnableGeometry(self, EnableGeometry):
        self._EnableGeometry = EnableGeometry


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._EnablePBR = params.get("EnablePBR")
        self._EnableGeometry = params.get("EnableGeometry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DRapidJobResponse(AbstractModel):
    r"""SubmitHunyuanTo3DRapidJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID (valid period: 24 hours)
        :type JobId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""Task ID (valid period: 24 hours)
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TranslationChoice(AbstractModel):
    r"""Translate the reply returned by the translation api, support multiple.

    """

    def __init__(self):
        r"""
        :param _FinishReason: End flag, can be stop or sensitive.
stop means output ends normally.
sensitive only appears when streaming output review is enabled, indicating security review not passed.
        :type FinishReason: str
        :param _Index: Index value, used when streaming.
        :type Index: int
        :param _Delta: Incremental return value used when streaming this field.
        :type Delta: :class:`tencentcloud.hunyuan.v20230901.models.TranslationDelta`
        :param _Message: Return value, used when non-streaming.
        :type Message: :class:`tencentcloud.hunyuan.v20230901.models.TranslationMessage`
        """
        self._FinishReason = None
        self._Index = None
        self._Delta = None
        self._Message = None

    @property
    def FinishReason(self):
        r"""End flag, can be stop or sensitive.
stop means output ends normally.
sensitive only appears when streaming output review is enabled, indicating security review not passed.
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Index(self):
        r"""Index value, used when streaming.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Delta(self):
        r"""Incremental return value used when streaming this field.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.TranslationDelta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def Message(self):
        r"""Return value, used when non-streaming.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.TranslationMessage`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._Index = params.get("Index")
        if params.get("Delta") is not None:
            self._Delta = TranslationDelta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = TranslationMessage()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationDelta(AbstractModel):
    r"""Translate the API response content (streaming return).

    """

    def __init__(self):
        r"""
        :param _Role: Role name.
        :type Role: str
        :param _Content: Content details.
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        r"""Role name.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""Content details.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationMessage(AbstractModel):
    r"""Translate the session content via translation api.

    """

    def __init__(self):
        r"""
        :param _Role: Role. valid values: system, user, assistant, tool.
        :type Role: str
        :param _Content: Text content.
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        r"""Role. valid values: system, user, assistant, tool.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""Text content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    r"""Token quantity.

    """

    def __init__(self):
        r"""
        :param _PromptTokens: Input Token quantity.
        :type PromptTokens: int
        :param _CompletionTokens: Output Token quantity.
        :type CompletionTokens: int
        :param _TotalTokens: Total Token quantity.
        :type TotalTokens: int
        :param _PromptTokensDetails: Details of the input token.
        :type PromptTokensDetails: :class:`tencentcloud.hunyuan.v20230901.models.PromptTokensDetails`
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None
        self._PromptTokensDetails = None

    @property
    def PromptTokens(self):
        r"""Input Token quantity.
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        r"""Output Token quantity.
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        r"""Total Token quantity.
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def PromptTokensDetails(self):
        r"""Details of the input token.
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.PromptTokensDetails`
        """
        return self._PromptTokensDetails

    @PromptTokensDetails.setter
    def PromptTokensDetails(self, PromptTokensDetails):
        self._PromptTokensDetails = PromptTokensDetails


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._CompletionTokens = params.get("CompletionTokens")
        self._TotalTokens = params.get("TotalTokens")
        if params.get("PromptTokensDetails") is not None:
            self._PromptTokensDetails = PromptTokensDetails()
            self._PromptTokensDetails._deserialize(params.get("PromptTokensDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewImage(AbstractModel):
    r"""Multi-Perspective images.

    """

    def __init__(self):
        r"""
        :param _ViewType: Specifies the viewing angle type.
Valid values: back, left, right.
        :type ViewType: str
        :param _ViewImageUrl: Image Url.
        :type ViewImageUrl: str
        :param _ViewImageBase64: base64 address of the image.
        :type ViewImageBase64: str
        """
        self._ViewType = None
        self._ViewImageUrl = None
        self._ViewImageBase64 = None

    @property
    def ViewType(self):
        r"""Specifies the viewing angle type.
Valid values: back, left, right.
        :rtype: str
        """
        return self._ViewType

    @ViewType.setter
    def ViewType(self, ViewType):
        self._ViewType = ViewType

    @property
    def ViewImageUrl(self):
        r"""Image Url.
        :rtype: str
        """
        return self._ViewImageUrl

    @ViewImageUrl.setter
    def ViewImageUrl(self, ViewImageUrl):
        self._ViewImageUrl = ViewImageUrl

    @property
    def ViewImageBase64(self):
        r"""base64 address of the image.
        :rtype: str
        """
        return self._ViewImageBase64

    @ViewImageBase64.setter
    def ViewImageBase64(self, ViewImageBase64):
        self._ViewImageBase64 = ViewImageBase64


    def _deserialize(self, params):
        self._ViewType = params.get("ViewType")
        self._ViewImageUrl = params.get("ViewImageUrl")
        self._ViewImageBase64 = params.get("ViewImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        