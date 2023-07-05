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


class Subtitle(AbstractModel):
    """The information about the timestamps.

    """

    def __init__(self):
        r"""
        :param _Text: The word in the text that is sent.
        :type Text: str
        :param _BeginTime: The start timestamp of the word in the synthesized audio data, in milliseconds.
        :type BeginTime: int
        :param _EndTime: The end timestamp of the word in the synthesized audio data, in milliseconds.
        :type EndTime: int
        :param _BeginIndex: The start index of the character in the whole sentence, starting from 0.
        :type BeginIndex: int
        :param _EndIndex: The end index of the character in the whole sentence, starting from 0.
        :type EndIndex: int
        :param _Phoneme: The phonemes of the word.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Phoneme: str
        """
        self._Text = None
        self._BeginTime = None
        self._EndTime = None
        self._BeginIndex = None
        self._EndIndex = None
        self._Phoneme = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BeginIndex(self):
        return self._BeginIndex

    @BeginIndex.setter
    def BeginIndex(self, BeginIndex):
        self._BeginIndex = BeginIndex

    @property
    def EndIndex(self):
        return self._EndIndex

    @EndIndex.setter
    def EndIndex(self, EndIndex):
        self._EndIndex = EndIndex

    @property
    def Phoneme(self):
        return self._Phoneme

    @Phoneme.setter
    def Phoneme(self, Phoneme):
        self._Phoneme = Phoneme


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._BeginIndex = params.get("BeginIndex")
        self._EndIndex = params.get("EndIndex")
        self._Phoneme = params.get("Phoneme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceRequest(AbstractModel):
    """TextToVoice request structure.

    """

    def __init__(self):
        r"""
        :param _Text: The source text for synthesizing speech, which is encoded in UTF-8.
It can contain up to 150 Chinese characters (a full-width punctuation as a Chinese character) or 500 letters ( a half-width punctuation as a letter).
        :type Text: str
        :param _SessionId: The `SessionId` of a request, which will be returned as-is. We recommend that you pass characters like uuid to prevent repetition.
        :type SessionId: str
        :param _Volume: Volume range: [0, 10], corresponding to 11 volume levels. 0 is the default value, indicating the normal volume. There is no mute option.
        :type Volume: float
        :param _Speed: Speed range: [-2, 6], corresponding to different speeds<li>-2 for 0.6 times</li><li>-1 for 0.8 times</li><li>0 for 1.0 time (default)</li><li>1 for 1.2 times</li><li>2 for 1.5 times</li><li>6 for 2.5 times</li>To set finer-grained speed levels, keep one decimal place, such as 0.5, 1.1, and 1.8.<br>
        :type Speed: float
        :param _ProjectId: Project ID, which defaults to 0 and can be customized.
        :type ProjectId: int
        :param _ModelType: Model type, with `1` for the default model.
        :type ModelType: int
        :param _VoiceType: Standard voices <li>10510000-zhixiaoyao (Chinese)</li><li>1001-zhiyu (Chinese)</li><li>1002-zhiling (Chinese)</li><li>1003-zhimei (Chinese)</li><li>1004-zhiyun (Chinese)</li><li>1005-zhili (Chinese)</li><li>1007-zhina (Chinese)</li><li>1008-zhiqi (Chinese)</li><li>1009-zhiyun (Chinese)</li><li>1010-zhihua (Chinese)</li><li>1017-zhirong (Chinese)</li><li>1018-zhijing (Chinese)</li><li>1050-WeJack (English)</li><li>1051-WeRose (English)</li>Premium voices<br>Premium voices have higher fidelity and more natural-sounding quality than standard voices. For price details, see [Purchase Guide](https://www.tencentcloud.com/document/product/1154/47874).<br><li>100510000-zhixiaoyao (Chinese)</li><li>101001-zhiyu (Chinese)</li><li>101002-zhiling (Chinese)</li><li>101003-zhimei (Chinese)</li><li>101004-zhiyun (Chinese)</li><li>101005-zhili (Chinese)</li><li>101006-zhiyan (Chinese)</li><li>101007-zhina (Chinese)</li><li>101008-zhiqi (Chinese)</li><li>101009-zhiyun (Chinese)</li><li>101010-zhihua (Chinese)</li><li>101011-zhiyan (Chinese)</li><li>101012-zhidan (Chinese)</li><li>101013-zhihui (Chinese)</li><li>101014-zhining (Chinese)</li><li>101015-zhimeng (Chinese)</li><li>101016-zhitian (Chinese)</li><li>101017-zhirong (Chinese)</li><li>101018-zhijing (Chinese)</li><li>101019-zhitong (Cantonese)</li><li>101020-zhigang (Chinese)</li><li>101021-zhirui (Chinese)</li><li>101022-zhihong (Chinese)</li><li>101023-zhixuan (Chinese)</li><li>101024-zhihao (Chinese)</li><li>101025-zhiwei (Chinese)</li><li>101026-zhixi (Chinese)</li><li>101027-zhimei (Chinese)</li><li>101028-zhijie (Chinese)</li><li>101029-zhikai (Chinese)</li><li>101030-zhike (Chinese)</li><li>101031-zhikui (Chinese)</li><li>101032-zhifang (Chinese)</li><li>101033-zhibei (Chinese)</li><li>101034-zhilian (Chinese)</li><li>101035-zhiyi (Chinese)</li><li>101040-zhichuan (Sichuan dialect)</li><li>101050-WeJack (English)</li><li>101051-WeRose (English)</li><li>101052-zhiwei (Chinese)</li>
<li>101053-zhifang (Chinese)</li>
<li>101054-zhiyou (Chinese)</li>
<li>101055-zhiyou (Chinese)</li>
<li>101056-zhilin (Northeastern Mandarin)</li>
        :type VoiceType: int
        :param _PrimaryLanguage: Primary language type: <li>1 - Chinese (default)</li><li>2 - English</li>
        :type PrimaryLanguage: int
        :param _SampleRate: Audio sample rate: <li>16000: 16k (default)</li><li>8000: 8k</li>
        :type SampleRate: int
        :param _Codec: Format of returned audio. Valid values: WAV (default), MP3, and PCM.
        :type Codec: str
        :param _EnableSubtitle: Whether to enable the timestamp feature. Default value: `false`.
        :type EnableSubtitle: bool
        :param _SegmentRate: The threshold of speech segmentation sensibility, which can be `0` (default), `1`, or `2`. A larger value indicates fewer segments, and the model tends to only segment sentences based on punctuation marks. We recommend you not change this parameter to avoid adverse effect on speech synthesis.
        :type SegmentRate: int
        """
        self._Text = None
        self._SessionId = None
        self._Volume = None
        self._Speed = None
        self._ProjectId = None
        self._ModelType = None
        self._VoiceType = None
        self._PrimaryLanguage = None
        self._SampleRate = None
        self._Codec = None
        self._EnableSubtitle = None
        self._SegmentRate = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Speed(self):
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def VoiceType(self):
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def PrimaryLanguage(self):
        return self._PrimaryLanguage

    @PrimaryLanguage.setter
    def PrimaryLanguage(self, PrimaryLanguage):
        self._PrimaryLanguage = PrimaryLanguage

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def EnableSubtitle(self):
        return self._EnableSubtitle

    @EnableSubtitle.setter
    def EnableSubtitle(self, EnableSubtitle):
        self._EnableSubtitle = EnableSubtitle

    @property
    def SegmentRate(self):
        return self._SegmentRate

    @SegmentRate.setter
    def SegmentRate(self, SegmentRate):
        self._SegmentRate = SegmentRate


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SessionId = params.get("SessionId")
        self._Volume = params.get("Volume")
        self._Speed = params.get("Speed")
        self._ProjectId = params.get("ProjectId")
        self._ModelType = params.get("ModelType")
        self._VoiceType = params.get("VoiceType")
        self._PrimaryLanguage = params.get("PrimaryLanguage")
        self._SampleRate = params.get("SampleRate")
        self._Codec = params.get("Codec")
        self._EnableSubtitle = params.get("EnableSubtitle")
        self._SegmentRate = params.get("SegmentRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceResponse(AbstractModel):
    """TextToVoice response structure.

    """

    def __init__(self):
        r"""
        :param _Audio: Base64-encoded WAV/MP3 audio data
        :type Audio: str
        :param _SessionId: The `SessionId` of a request
        :type SessionId: str
        :param _Subtitles: Timestamp information. If the timestamp feature is not enabled, an empty array will be returned.
        :type Subtitles: list of Subtitle
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Audio = None
        self._SessionId = None
        self._Subtitles = None
        self._RequestId = None

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Subtitles(self):
        return self._Subtitles

    @Subtitles.setter
    def Subtitles(self, Subtitles):
        self._Subtitles = Subtitles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Audio = params.get("Audio")
        self._SessionId = params.get("SessionId")
        if params.get("Subtitles") is not None:
            self._Subtitles = []
            for item in params.get("Subtitles"):
                obj = Subtitle()
                obj._deserialize(item)
                self._Subtitles.append(obj)
        self._RequestId = params.get("RequestId")