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
        :param Text: The word in the text that is sent.
        :type Text: str
        :param BeginTime: The start timestamp of the word in the synthesized audio data, in milliseconds.
        :type BeginTime: int
        :param EndTime: The end timestamp of the word in the synthesized audio data, in milliseconds.
        :type EndTime: int
        :param BeginIndex: The start index of the character in the whole sentence, starting from 0.
        :type BeginIndex: int
        :param EndIndex: The end index of the character in the whole sentence, starting from 0.
        :type EndIndex: int
        """
        self.Text = None
        self.BeginTime = None
        self.EndTime = None
        self.BeginIndex = None
        self.EndIndex = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.BeginIndex = params.get("BeginIndex")
        self.EndIndex = params.get("EndIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceRequest(AbstractModel):
    """TextToVoice request structure.

    """

    def __init__(self):
        r"""
        :param Text: The source text for synthesizing speech, which is encoded in UTF-8.
It can contain up to 150 Chinese characters (a full-width punctuation as a Chinese character) or 500 letters ( a half-width punctuation as a letter).
        :type Text: str
        :param SessionId: The `SessionId` of a request, which will be returned as-is. We recommend that you pass characters like uuid to prevent repetition.
        :type SessionId: str
        :param Volume: Volume range: [0, 10], corresponding to 11 volume levels. 0 is the default value, indicating the normal volume. There is no mute option.
        :type Volume: float
        :param Speed: 
        :type Speed: float
        :param ProjectId: Project ID, which defaults to 0 and can be customized.
        :type ProjectId: int
        :param ModelType: Model type, with `1` for the default model.
        :type ModelType: int
        :param VoiceType: Standard voices <li>10510000-zhixiaoyao (Chinese)</li><li>1001-zhiyu (Chinese)</li><li>1002-zhiling (Chinese)</li><li>1003-zhimei (Chinese)</li><li>1004-zhiyun (Chinese)</li><li>1005-zhili (Chinese)</li><li>1007-zhina (Chinese)</li><li>1008-zhiqi (Chinese)</li><li>1009-zhiyun (Chinese)</li><li>1010-zhihua (Chinese)</li><li>1017-zhirong (Chinese)</li><li>1018-zhijing (Chinese)</li><li>1050-WeJack (English)</li><li>1051-WeRose (English)</li>Premium voices<br>Premium voices have higher fidelity and more natural-sounding quality than standard voices. For price details, see [Purchase Guide](https://intl.cloud.tencent.com/document/product/1073/34112?from_cn_redirect=1).<br><li>100510000-zhixiaoyao (Chinese)</li><li>101001-zhiyu (Chinese)</li><li>101002-zhiling (Chinese)</li><li>101003-zhimei (Chinese)</li><li>101004-zhiyun (Chinese)</li><li>101005-zhili (Chinese)</li><li>101006-zhiyan (Chinese)</li><li>101007-zhina (Chinese)</li><li>101008-zhiqi (Chinese)</li><li>101009-zhiyun (Chinese)</li><li>101010-zhihua (Chinese)</li><li>101011-zhiyan (Chinese)</li><li>101012-zhidan (Chinese)</li><li>101013-zhihui (Chinese)</li><li>101014-zhining (Chinese)</li><li>101015-zhimeng (Chinese)</li><li>101016-zhitian (Chinese)</li><li>101017-zhirong (Chinese)</li><li>101018-zhijing (Chinese)</li><li>101019-zhitong (Cantonese)</li><li>101020-zhigang (Chinese)</li><li>101021-zhirui (Chinese)</li><li>101022-zhihong (Chinese)</li><li>101023-zhixuan (Chinese)</li><li>101024-zhihao (Chinese)</li><li>101025-zhiwei (Chinese)</li><li>101026-zhixi (Chinese)</li><li>101027-zhimei (Chinese)</li><li>101028-zhijie (Chinese)</li><li>101029-zhikai (Chinese)</li><li>101030-zhike (Chinese)</li><li>101031-zhikui (Chinese)</li><li>101032-zhifang (Chinese)</li><li>101033-zhibei (Chinese)</li><li>101034-zhilian (Chinese)</li><li>101035-zhiyi (Chinese)</li><li>101040-zhichuan (Sichuan dialect)</li><li>101050-WeJack (English)</li><li>101051-WeRose (English)</li><li>101052-zhiwei (Chinese)</li>
<li>101053-zhifang (Chinese)</li>
<li>101054-zhiyou (Chinese)</li>
<li>101055-zhiyou (Chinese)</li>
<li>101056-zhilin (Dongbei dialect)</li>
        :type VoiceType: int
        :param PrimaryLanguage: Primary language type: <li>1 - Chinese (default)</li><li>2 - English</li>
        :type PrimaryLanguage: int
        :param SampleRate: Audio sample rate: <li>16000: 16k (default)</li><li>8000: 8k</li>
        :type SampleRate: int
        :param Codec: Format of returned audio. Valid values: WAV (default), MP3, and PCM.
        :type Codec: str
        :param EnableSubtitle: Whether to enable the timestamp feature. Default value: `false`.
        :type EnableSubtitle: bool
        :param SegmentRate: Segmentation rate. Valid range: [0,1,2]; default value: `0`. The higher the value, the lower the rate, and the easier the segmentation. It is recommended not to change this parameter to ensure better synthesis quality.
        :type SegmentRate: int
        """
        self.Text = None
        self.SessionId = None
        self.Volume = None
        self.Speed = None
        self.ProjectId = None
        self.ModelType = None
        self.VoiceType = None
        self.PrimaryLanguage = None
        self.SampleRate = None
        self.Codec = None
        self.EnableSubtitle = None
        self.SegmentRate = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SessionId = params.get("SessionId")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.ProjectId = params.get("ProjectId")
        self.ModelType = params.get("ModelType")
        self.VoiceType = params.get("VoiceType")
        self.PrimaryLanguage = params.get("PrimaryLanguage")
        self.SampleRate = params.get("SampleRate")
        self.Codec = params.get("Codec")
        self.EnableSubtitle = params.get("EnableSubtitle")
        self.SegmentRate = params.get("SegmentRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceResponse(AbstractModel):
    """TextToVoice response structure.

    """

    def __init__(self):
        r"""
        :param Audio: Base64-encoded WAV/MP3 audio data
        :type Audio: str
        :param SessionId: The `SessionId` of a request
        :type SessionId: str
        :param Subtitles: Timestamp information. If the timestamp feature is not enabled, an empty array will be returned.
        :type Subtitles: list of Subtitle
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Audio = None
        self.SessionId = None
        self.Subtitles = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Audio = params.get("Audio")
        self.SessionId = params.get("SessionId")
        if params.get("Subtitles") is not None:
            self.Subtitles = []
            for item in params.get("Subtitles"):
                obj = Subtitle()
                obj._deserialize(item)
                self.Subtitles.append(obj)
        self.RequestId = params.get("RequestId")