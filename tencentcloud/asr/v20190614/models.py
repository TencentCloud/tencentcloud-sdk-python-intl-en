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


class CreateRecTaskRequest(AbstractModel):
    """CreateRecTask request structure.

    """

    def __init__(self):
        r"""
        :param _EngineModelType: Engine model type.
Each recognition engine adopts a specific billing plan. Engines marked with "large model version" adopt the large model billing plan. For product billing instructions, [click here] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1).


Note: If you want to recognize telecommunication audio but find that a 16k engine is required, you can use a 16k engine as described below for recognition. However, ** the 16k engines are not trained for recognizing telecommunication audio. Therefore, the recognition results cannot be guaranteed. You need to check whether the recognition results can be used. **

Engines for general scenarios:
** Note: Use 16k engines for scenarios other than telecommunication. **
** 16k_zh_large: ** Engine (large model version) for Mandarin, Chinese dialects, and English. This engine supports recognizing audio in Chinese, English, and [various Chinese dialects] (https://intl.cloud.tencent.com/document/product/1093/35682?from_cn_redirect=1). It has a large number of parameters, enhanced performance, and greatly improved recognition accuracy for low-quality audio with loud noise, too much echo, low voice volume, or faint voices. [Click here] (https://console.cloud.tencent.com/asr/demonstrate) to compare the recognition performance of the 16k_zh engine and this one.
** 16k_multi_lang: ** Engine (large model version) for multiple languages. This engine supports recognizing audio in English, Japanese, Korean, Arabic, Filipino, French, Hindi, Indonesian, Malay, Portuguese, Spanish, Thai, Turkish, Vietnamese, and German (sentence-level or paragraph-level).
** 16k_zh-PY: ** Engine for Chinese, English, and Cantonese. The engine supports recognizing audio in Mandarin, English, and Cantonese at the same time.
** 16k_ms: ** Engine for Malay.
** 16k_id: ** Engine for Indonesian.
** 16k_th: ** Engine for Thai.
        :type EngineModelType: str
        :param _ChannelNum: Number of recognition channels.
1: Mono. (16k engines only support mono. ** Do no t** set to stereo.)
2: Stereo. (Stereo is supported only for 8k engines, and the two channels should correspond to the respective communication parties.)

Note:
16k engines: Only support mono. ** ChannelNum should be set to 1 **.
8k engines: Support both mono and stereo. ** It is recommended to set ChannelNum to 2 (indicating stereo) **. Stereo can physically distinguish speakers to avoid recognition mistakes caused by overlapping speech. It can provide the best speaker separation and recognition effects. Once stereo is set, the speakers are automatically separated. ** You do not need to enable the speaker separation feature **. You can use the default values for related parameters (** SpeakerDiarization and SpeakerNumber **). For speakerId in the returned ResultDetail, the value 0 represents the left channel, and the value 1 represents the right channel.
        :type ChannelNum: int
        :param _ResTextFormat: Format of the returned recognition result.
0: The basic recognition result (containing only valid voice timestamps but no word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail)).
1: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps and speech speed value but ** no punctuation **).
2: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **).
3: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The recognition results are segmented by punctuation. ** This format applies to subtitle scenarios **.
4: ** [Value-added paid feature] ** The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The recognition results are segmented by NLP semantics. ** This format applies to scenarios such as meeting and court record transcription ** and is supported only for 8k_zh and 16k_zh engines.
5: ** [Value-added paid feature] ** Basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The oral-to-written transcription result is also output, which has excluded modal particles and consecutive identical words, optimized expressions, and corrected speech mistakes. ** This format applies to scenarios of generating minutes for online and offline meetings** and is supported only for 8k_zh and 16k_zh engines.

Notes:
If this parameter is set to 4, make sure that a [semantics-based segmentation resource package] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#97ae4aa0-29a0-4066-9f07-ccaf8856a16b) is purchased for your account or that your account has enabled post-payment. ** If post-payment is enabled and this parameter is set to 4, [automatic billing] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#d912167d-ffd5-41a9-8b1c-2e89845a6852) will apply **.
If this parameter is set to 5, make sure that an [oral-to-written resource package] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#97ae4aa0-29a0-4066-9f07-ccaf8856a16b) is purchased for your account or that your account has enabled post-payment. ** If post-payment is enabled and this parameter is set to 5, [automatic billing] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#d912167d-ffd5-41a9-8b1c-2e89845a6852) will apply **.
        :type ResTextFormat: int
        :param _SourceType: Audio source.
0: Audio URL.
1: Local audio file (body of the POST request).
        :type SourceType: int
        :param _Data: Audio file Base64 code.
** This parameter is required if SourceType is set to 1. Otherwise, it can be left blank. **

Note: The audio data size cannot exceed 5 MB.
        :type Data: str
        :param _DataLen: Data length (before Base64 encoding).
        :type DataLen: int
        :param _Url: Audio URL. (The audio should be downloadable via a public network browser.)
** This parameter is required if SourceType is set to 0. Otherwise, it can be left blank. **

Notes:
1. Make sure that the total audio duration of recording files does not exceed 5 hours. Otherwise, recognition may fail.
2. Pay attention to file download to avoid download failure.
        :type Url: str
        :param _CallbackUrl: Callback URL

User-defined service URL for receiving recognition results.
For the callback format and content, see [Callback Description] (https://intl.cloud.tencent.com/document/product/1093/52632?from_cn_redirect=1).

Notes:

- If you use the polling method to obtain recognition results, this parameter is not required.
- It is recommended to include your business ID and other information in the callback URL for handling business logic.
        :type CallbackUrl: str
        :param _SpeakerDiarization: Whether to enable speaker separation.
0: Disable.
1: Enable. (This value is supported only for the following engines: 8k_zh, 16k_zh, 16k_ms, 16k_en, 16k_id, 16k_zh_large, and 16k_zh_dialect. ChannelNum should be set to 1.)
The default value is 0.

Note:
If an 8k engine is used and ChannelNum is set to 2 (stereo), use the default values for corresponding parameters as stated in the ** ChannelNum ** parameter description.
        :type SpeakerDiarization: int
        :param _SpeakerNumber: Number of speakers to be separated.
** Speaker separation must be enabled. Otherwise, this parameter does not take effect. ** Value range: 0-10.
0: Automatic separation. (Up to 20 speakers can be separated.)
1-10: Specify the number of speakers.
The default value is 0.
        :type SpeakerNumber: int
        :param _HotwordId: This service is not available.
        :type HotwordId: str
        :param _ReinforceHotword: This service is not available.
        :type ReinforceHotword: int
        :param _CustomizationId: This service is not available.
        :type CustomizationId: str
        :param _EmotionRecognition: This service is not available.
        :type EmotionRecognition: int
        :param _EmotionalEnergy: Emotional energy value.
The value is the result of dividing the sound volume in dB by 10. Value range: [1,10]. The higher the value, the stronger the emotion.
0: Disable.
1: Enable.
The default value is 0.
        :type EmotionalEnergy: int
        :param _ConvertNumMode: Intelligent conversion into Arabic numerals (supported only for engines for recognizing audio in Mandarin).
0: Do not convert, but directly output Chinese numerals.
1: Intelligently convert into Arabic numerals based on the scenario.
3: Enable conversion for math-related letters.
The default value is 1.
        :type ConvertNumMode: int
        :param _FilterDirty: Dirty word filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out dirty words.
1: Filter out dirty words.
2: Replace dirty words with *.
The default value is 0.
        :type FilterDirty: int
        :param _FilterPunc: Punctuation filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out punctuation.
1: Filter out sentence-ending punctuation.
2: Filter out all punctuation.
The default value is 0.
        :type FilterPunc: int
        :param _FilterModal: Modal particle filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out modal particles.
1: Filter out specified modal particles.
2: Filter out all modal particles.
The default value is 0.
        :type FilterModal: int
        :param _SentenceMaxLength: The maximum number of characters per line (supported only for engines for recognizing audio in Mandarin). A punctuation mark is added if this limit is reached.
** This parameter can control the maximum number of characters per line, which applies to subtitle generation scenarios. ** Value range: [6,40].
0: Disable this feature.
The default value is 0.

Note: To enable this feature, ResTextFormat should be set to 3. The recognition result can be obtained from FinalSentence by parsing the list in the returned ResultDetail.
        :type SentenceMaxLength: int
        :param _Extra: Additional parameter. ** (This parameter is meaningless. Ignore it.) **
        :type Extra: str
        :param _HotwordList: Temporary term list. This parameter is used to improve the recognition accuracy.

- Restrictions for individual terms: The format is "term|weight". Each term can contain no more than 30 characters (or 10 Chinese characters. The weight can be in the range of [1-11] or 100. For example, "Tencent Cloud|5" or "ASR|11".

- Restrictions for the temporary term list: Multiple terms are separated by commas. The list can contain up to 128 terms. For example, "Tencent Cloud|10, Audio Recognition|5, ASR|11".

- Difference between hotword_id (term list) and hotword_list (temporary term list):

    - hotword_id: Term list. You need to create a term list in the console or by using the API first and obtain the term list ID.

    - hotword_list: Temporary term list. You can directly enter the ID of the temporary term list each time you initiate a request. The temporary term list is not retained on the cloud. This parameter applies to users with a massive number of terms.

Notes:

- If both hotword_id and hotword_list are specified, hotword_list will take effect first.

- When the weight of a term is set to 11, this term becomes a super term. It is recommended that the weight is set to 11 only for critical and necessary terms. The overall accuracy will be affected if the weight is set to 11 for too many terms.

- When the weight of a term is set to 100, the term enhancement feature is enabled to replace homophones of this term. (This feature is supported only for 8k_zh and 16k_zh engines.) For example, if you configure "mizhi 1|100", the recognized word "mizhi 2", which is a homophone of "mizhi 2", will be forcibly replaced with "mizhi 2". It is recommended that you enable this feature based on the actual needs. You can set the weight to 100 for only critical and necessary terms. The overall accuracy will be affected if the weight is set to 100 for too many terms.
        :type HotwordList: str
        :param _KeyWordLibIdList: List of keyword IDs for recognition. This parameter is left blank by default, indicating that no keyword is recognized. You can enter up to 10 IDs.

        :type KeyWordLibIdList: list of str
        """
        self._EngineModelType = None
        self._ChannelNum = None
        self._ResTextFormat = None
        self._SourceType = None
        self._Data = None
        self._DataLen = None
        self._Url = None
        self._CallbackUrl = None
        self._SpeakerDiarization = None
        self._SpeakerNumber = None
        self._HotwordId = None
        self._ReinforceHotword = None
        self._CustomizationId = None
        self._EmotionRecognition = None
        self._EmotionalEnergy = None
        self._ConvertNumMode = None
        self._FilterDirty = None
        self._FilterPunc = None
        self._FilterModal = None
        self._SentenceMaxLength = None
        self._Extra = None
        self._HotwordList = None
        self._KeyWordLibIdList = None

    @property
    def EngineModelType(self):
        """Engine model type.
Each recognition engine adopts a specific billing plan. Engines marked with "large model version" adopt the large model billing plan. For product billing instructions, [click here] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1).


Note: If you want to recognize telecommunication audio but find that a 16k engine is required, you can use a 16k engine as described below for recognition. However, ** the 16k engines are not trained for recognizing telecommunication audio. Therefore, the recognition results cannot be guaranteed. You need to check whether the recognition results can be used. **

Engines for general scenarios:
** Note: Use 16k engines for scenarios other than telecommunication. **
** 16k_zh_large: ** Engine (large model version) for Mandarin, Chinese dialects, and English. This engine supports recognizing audio in Chinese, English, and [various Chinese dialects] (https://intl.cloud.tencent.com/document/product/1093/35682?from_cn_redirect=1). It has a large number of parameters, enhanced performance, and greatly improved recognition accuracy for low-quality audio with loud noise, too much echo, low voice volume, or faint voices. [Click here] (https://console.cloud.tencent.com/asr/demonstrate) to compare the recognition performance of the 16k_zh engine and this one.
** 16k_multi_lang: ** Engine (large model version) for multiple languages. This engine supports recognizing audio in English, Japanese, Korean, Arabic, Filipino, French, Hindi, Indonesian, Malay, Portuguese, Spanish, Thai, Turkish, Vietnamese, and German (sentence-level or paragraph-level).
** 16k_zh-PY: ** Engine for Chinese, English, and Cantonese. The engine supports recognizing audio in Mandarin, English, and Cantonese at the same time.
** 16k_ms: ** Engine for Malay.
** 16k_id: ** Engine for Indonesian.
** 16k_th: ** Engine for Thai.
        :rtype: str
        """
        return self._EngineModelType

    @EngineModelType.setter
    def EngineModelType(self, EngineModelType):
        self._EngineModelType = EngineModelType

    @property
    def ChannelNum(self):
        """Number of recognition channels.
1: Mono. (16k engines only support mono. ** Do no t** set to stereo.)
2: Stereo. (Stereo is supported only for 8k engines, and the two channels should correspond to the respective communication parties.)

Note:
16k engines: Only support mono. ** ChannelNum should be set to 1 **.
8k engines: Support both mono and stereo. ** It is recommended to set ChannelNum to 2 (indicating stereo) **. Stereo can physically distinguish speakers to avoid recognition mistakes caused by overlapping speech. It can provide the best speaker separation and recognition effects. Once stereo is set, the speakers are automatically separated. ** You do not need to enable the speaker separation feature **. You can use the default values for related parameters (** SpeakerDiarization and SpeakerNumber **). For speakerId in the returned ResultDetail, the value 0 represents the left channel, and the value 1 represents the right channel.
        :rtype: int
        """
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum

    @property
    def ResTextFormat(self):
        """Format of the returned recognition result.
0: The basic recognition result (containing only valid voice timestamps but no word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail)).
1: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps and speech speed value but ** no punctuation **).
2: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **).
3: The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The recognition results are segmented by punctuation. ** This format applies to subtitle scenarios **.
4: ** [Value-added paid feature] ** The basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The recognition results are segmented by NLP semantics. ** This format applies to scenarios such as meeting and court record transcription ** and is supported only for 8k_zh and 16k_zh engines.
5: ** [Value-added paid feature] ** Basic recognition result and word-level [detailed recognition result] (https://intl.cloud.tencent.com/document/api/1093/37824?from_cn_redirect=1#SentenceDetail) (containing word-level timestamps, speech speed value, and ** punctuation **). The oral-to-written transcription result is also output, which has excluded modal particles and consecutive identical words, optimized expressions, and corrected speech mistakes. ** This format applies to scenarios of generating minutes for online and offline meetings** and is supported only for 8k_zh and 16k_zh engines.

Notes:
If this parameter is set to 4, make sure that a [semantics-based segmentation resource package] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#97ae4aa0-29a0-4066-9f07-ccaf8856a16b) is purchased for your account or that your account has enabled post-payment. ** If post-payment is enabled and this parameter is set to 4, [automatic billing] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#d912167d-ffd5-41a9-8b1c-2e89845a6852) will apply **.
If this parameter is set to 5, make sure that an [oral-to-written resource package] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#97ae4aa0-29a0-4066-9f07-ccaf8856a16b) is purchased for your account or that your account has enabled post-payment. ** If post-payment is enabled and this parameter is set to 5, [automatic billing] (https://intl.cloud.tencent.com/document/product/1093/35686?from_cn_redirect=1#d912167d-ffd5-41a9-8b1c-2e89845a6852) will apply **.
        :rtype: int
        """
        return self._ResTextFormat

    @ResTextFormat.setter
    def ResTextFormat(self, ResTextFormat):
        self._ResTextFormat = ResTextFormat

    @property
    def SourceType(self):
        """Audio source.
0: Audio URL.
1: Local audio file (body of the POST request).
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Data(self):
        """Audio file Base64 code.
** This parameter is required if SourceType is set to 1. Otherwise, it can be left blank. **

Note: The audio data size cannot exceed 5 MB.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        """Data length (before Base64 encoding).
        :rtype: int
        """
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def Url(self):
        """Audio URL. (The audio should be downloadable via a public network browser.)
** This parameter is required if SourceType is set to 0. Otherwise, it can be left blank. **

Notes:
1. Make sure that the total audio duration of recording files does not exceed 5 hours. Otherwise, recognition may fail.
2. Pay attention to file download to avoid download failure.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackUrl(self):
        """Callback URL

User-defined service URL for receiving recognition results.
For the callback format and content, see [Callback Description] (https://intl.cloud.tencent.com/document/product/1093/52632?from_cn_redirect=1).

Notes:

- If you use the polling method to obtain recognition results, this parameter is not required.
- It is recommended to include your business ID and other information in the callback URL for handling business logic.
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SpeakerDiarization(self):
        """Whether to enable speaker separation.
0: Disable.
1: Enable. (This value is supported only for the following engines: 8k_zh, 16k_zh, 16k_ms, 16k_en, 16k_id, 16k_zh_large, and 16k_zh_dialect. ChannelNum should be set to 1.)
The default value is 0.

Note:
If an 8k engine is used and ChannelNum is set to 2 (stereo), use the default values for corresponding parameters as stated in the ** ChannelNum ** parameter description.
        :rtype: int
        """
        return self._SpeakerDiarization

    @SpeakerDiarization.setter
    def SpeakerDiarization(self, SpeakerDiarization):
        self._SpeakerDiarization = SpeakerDiarization

    @property
    def SpeakerNumber(self):
        """Number of speakers to be separated.
** Speaker separation must be enabled. Otherwise, this parameter does not take effect. ** Value range: 0-10.
0: Automatic separation. (Up to 20 speakers can be separated.)
1-10: Specify the number of speakers.
The default value is 0.
        :rtype: int
        """
        return self._SpeakerNumber

    @SpeakerNumber.setter
    def SpeakerNumber(self, SpeakerNumber):
        self._SpeakerNumber = SpeakerNumber

    @property
    def HotwordId(self):
        """This service is not available.
        :rtype: str
        """
        return self._HotwordId

    @HotwordId.setter
    def HotwordId(self, HotwordId):
        self._HotwordId = HotwordId

    @property
    def ReinforceHotword(self):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        """This service is not available.
        :rtype: int
        """
        return self._ReinforceHotword

    @ReinforceHotword.setter
    def ReinforceHotword(self, ReinforceHotword):
        warnings.warn("parameter `ReinforceHotword` is deprecated", DeprecationWarning) 

        self._ReinforceHotword = ReinforceHotword

    @property
    def CustomizationId(self):
        """This service is not available.
        :rtype: str
        """
        return self._CustomizationId

    @CustomizationId.setter
    def CustomizationId(self, CustomizationId):
        self._CustomizationId = CustomizationId

    @property
    def EmotionRecognition(self):
        """This service is not available.
        :rtype: int
        """
        return self._EmotionRecognition

    @EmotionRecognition.setter
    def EmotionRecognition(self, EmotionRecognition):
        self._EmotionRecognition = EmotionRecognition

    @property
    def EmotionalEnergy(self):
        """Emotional energy value.
The value is the result of dividing the sound volume in dB by 10. Value range: [1,10]. The higher the value, the stronger the emotion.
0: Disable.
1: Enable.
The default value is 0.
        :rtype: int
        """
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def ConvertNumMode(self):
        """Intelligent conversion into Arabic numerals (supported only for engines for recognizing audio in Mandarin).
0: Do not convert, but directly output Chinese numerals.
1: Intelligently convert into Arabic numerals based on the scenario.
3: Enable conversion for math-related letters.
The default value is 1.
        :rtype: int
        """
        return self._ConvertNumMode

    @ConvertNumMode.setter
    def ConvertNumMode(self, ConvertNumMode):
        self._ConvertNumMode = ConvertNumMode

    @property
    def FilterDirty(self):
        """Dirty word filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out dirty words.
1: Filter out dirty words.
2: Replace dirty words with *.
The default value is 0.
        :rtype: int
        """
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterPunc(self):
        """Punctuation filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out punctuation.
1: Filter out sentence-ending punctuation.
2: Filter out all punctuation.
The default value is 0.
        :rtype: int
        """
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc

    @property
    def FilterModal(self):
        """Modal particle filtering (supported only for engines for recognizing audio in Mandarin).
0: Do not filter out modal particles.
1: Filter out specified modal particles.
2: Filter out all modal particles.
The default value is 0.
        :rtype: int
        """
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def SentenceMaxLength(self):
        """The maximum number of characters per line (supported only for engines for recognizing audio in Mandarin). A punctuation mark is added if this limit is reached.
** This parameter can control the maximum number of characters per line, which applies to subtitle generation scenarios. ** Value range: [6,40].
0: Disable this feature.
The default value is 0.

Note: To enable this feature, ResTextFormat should be set to 3. The recognition result can be obtained from FinalSentence by parsing the list in the returned ResultDetail.
        :rtype: int
        """
        return self._SentenceMaxLength

    @SentenceMaxLength.setter
    def SentenceMaxLength(self, SentenceMaxLength):
        self._SentenceMaxLength = SentenceMaxLength

    @property
    def Extra(self):
        """Additional parameter. ** (This parameter is meaningless. Ignore it.) **
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def HotwordList(self):
        """Temporary term list. This parameter is used to improve the recognition accuracy.

- Restrictions for individual terms: The format is "term|weight". Each term can contain no more than 30 characters (or 10 Chinese characters. The weight can be in the range of [1-11] or 100. For example, "Tencent Cloud|5" or "ASR|11".

- Restrictions for the temporary term list: Multiple terms are separated by commas. The list can contain up to 128 terms. For example, "Tencent Cloud|10, Audio Recognition|5, ASR|11".

- Difference between hotword_id (term list) and hotword_list (temporary term list):

    - hotword_id: Term list. You need to create a term list in the console or by using the API first and obtain the term list ID.

    - hotword_list: Temporary term list. You can directly enter the ID of the temporary term list each time you initiate a request. The temporary term list is not retained on the cloud. This parameter applies to users with a massive number of terms.

Notes:

- If both hotword_id and hotword_list are specified, hotword_list will take effect first.

- When the weight of a term is set to 11, this term becomes a super term. It is recommended that the weight is set to 11 only for critical and necessary terms. The overall accuracy will be affected if the weight is set to 11 for too many terms.

- When the weight of a term is set to 100, the term enhancement feature is enabled to replace homophones of this term. (This feature is supported only for 8k_zh and 16k_zh engines.) For example, if you configure "mizhi 1|100", the recognized word "mizhi 2", which is a homophone of "mizhi 2", will be forcibly replaced with "mizhi 2". It is recommended that you enable this feature based on the actual needs. You can set the weight to 100 for only critical and necessary terms. The overall accuracy will be affected if the weight is set to 100 for too many terms.
        :rtype: str
        """
        return self._HotwordList

    @HotwordList.setter
    def HotwordList(self, HotwordList):
        self._HotwordList = HotwordList

    @property
    def KeyWordLibIdList(self):
        """List of keyword IDs for recognition. This parameter is left blank by default, indicating that no keyword is recognized. You can enter up to 10 IDs.

        :rtype: list of str
        """
        return self._KeyWordLibIdList

    @KeyWordLibIdList.setter
    def KeyWordLibIdList(self, KeyWordLibIdList):
        self._KeyWordLibIdList = KeyWordLibIdList


    def _deserialize(self, params):
        self._EngineModelType = params.get("EngineModelType")
        self._ChannelNum = params.get("ChannelNum")
        self._ResTextFormat = params.get("ResTextFormat")
        self._SourceType = params.get("SourceType")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        self._Url = params.get("Url")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SpeakerDiarization = params.get("SpeakerDiarization")
        self._SpeakerNumber = params.get("SpeakerNumber")
        self._HotwordId = params.get("HotwordId")
        self._ReinforceHotword = params.get("ReinforceHotword")
        self._CustomizationId = params.get("CustomizationId")
        self._EmotionRecognition = params.get("EmotionRecognition")
        self._EmotionalEnergy = params.get("EmotionalEnergy")
        self._ConvertNumMode = params.get("ConvertNumMode")
        self._FilterDirty = params.get("FilterDirty")
        self._FilterPunc = params.get("FilterPunc")
        self._FilterModal = params.get("FilterModal")
        self._SentenceMaxLength = params.get("SentenceMaxLength")
        self._Extra = params.get("Extra")
        self._HotwordList = params.get("HotwordList")
        self._KeyWordLibIdList = params.get("KeyWordLibIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecTaskResponse(AbstractModel):
    """CreateRecTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result of the recording recognition request, containing the task ID required for querying the result.
** Note: The task ID is valid for 24 hours, and duplicate task IDs of different dates may exist. Do not use task ID as the unique ID in your business system. **

        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Returned result of the recording recognition request, containing the task ID required for querying the result.
** Note: The task ID is valid for 24 hours, and duplicate task IDs of different dates may exist. Do not use task ID as the unique ID in your business system. **

        :rtype: :class:`tencentcloud.asr.v20190614.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID obtained from the CreateRecTask API, which is used to obtain the task status and results.
** Note: A task is valid for 24 hours. Do not query the results with the tasks that have existed for more than 24 hours. **
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Task ID obtained from the CreateRecTask API, which is used to obtain the task status and results.
** Note: A task is valid for 24 hours. Do not query the results with the tasks that have existed for more than 24 hours. **
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result of the recording recognition request.
        :type Data: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Returned result of the recording recognition request.
        :rtype: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TaskStatus()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class KeyWordResult(AbstractModel):
    """Keyword recognition result.

    """

    def __init__(self):
        r"""
        :param _KeyWordLibID: Keyword library ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyWordLibID: str
        :param _KeyWordLibName: Keyword library name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyWordLibName: str
        :param _KeyWords: Matching keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyWords: list of str
        """
        self._KeyWordLibID = None
        self._KeyWordLibName = None
        self._KeyWords = None

    @property
    def KeyWordLibID(self):
        """Keyword library ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyWordLibID

    @KeyWordLibID.setter
    def KeyWordLibID(self, KeyWordLibID):
        self._KeyWordLibID = KeyWordLibID

    @property
    def KeyWordLibName(self):
        """Keyword library name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyWordLibName

    @KeyWordLibName.setter
    def KeyWordLibName(self, KeyWordLibName):
        self._KeyWordLibName = KeyWordLibName

    @property
    def KeyWords(self):
        """Matching keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords


    def _deserialize(self, params):
        self._KeyWordLibID = params.get("KeyWordLibID")
        self._KeyWordLibName = params.get("KeyWordLibName")
        self._KeyWords = params.get("KeyWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceDetail(AbstractModel):
    """Detailed recognition result of a sentence, including the time offset of individual words. This parameter generally applies to subtitle generation scenarios.

    """

    def __init__(self):
        r"""
        :param _FinalSentence: Final recognition result of a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinalSentence: str
        :param _SliceSentence: Intermediate recognition result of a sentence. The sentence is split into multiple phrases by spaces.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SliceSentence: str
        :param _WrittenText: Oral-to-written transcription result. This parameter has a value only if the corresponding feature is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WrittenText: str
        :param _StartMs: Start time of a sentence (ms).
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartMs: int
        :param _EndMs: End time of a sentence (ms).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndMs: int
        :param _WordsNum: Number of words in a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WordsNum: int
        :param _Words: Word details of a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Words: list of SentenceWords
        :param _SpeechSpeed: Speech speed of a sentence. Unit: Number of words per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpeechSpeed: float
        :param _SpeakerId: Channel or speaker ID. (If speaker_diarization is specified or ChannelNum is set to 2 (stereo) in the request, speakers or channels can be distinguished.)
Different values represent different speakers in mono mode. For the speakerId values, 0 represents the left channel, and 1 represents the right channel in stereo mode if an 8k engine is used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpeakerId: int
        :param _EmotionalEnergy: Emotional energy value. This value is the result of dividing the sound volume in dB by 10. Value range: [1,10]. The higher the value, the stronger the emotion.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmotionalEnergy: float
        :param _SilenceTime: Silent duration between the current sentence and the last sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SilenceTime: int
        :param _EmotionType: Emotion type. (This parameter may be left blank in two scenarios: 1. No corresponding resource package exists; 2. The emotion is not recognized because it is not strong enough, which is related to the emotional energy.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EmotionType: list of str
        :param _KeyWordResults: List of recognized keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyWordResults: list of KeyWordResult
        """
        self._FinalSentence = None
        self._SliceSentence = None
        self._WrittenText = None
        self._StartMs = None
        self._EndMs = None
        self._WordsNum = None
        self._Words = None
        self._SpeechSpeed = None
        self._SpeakerId = None
        self._EmotionalEnergy = None
        self._SilenceTime = None
        self._EmotionType = None
        self._KeyWordResults = None

    @property
    def FinalSentence(self):
        """Final recognition result of a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FinalSentence

    @FinalSentence.setter
    def FinalSentence(self, FinalSentence):
        self._FinalSentence = FinalSentence

    @property
    def SliceSentence(self):
        """Intermediate recognition result of a sentence. The sentence is split into multiple phrases by spaces.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SliceSentence

    @SliceSentence.setter
    def SliceSentence(self, SliceSentence):
        self._SliceSentence = SliceSentence

    @property
    def WrittenText(self):
        """Oral-to-written transcription result. This parameter has a value only if the corresponding feature is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WrittenText

    @WrittenText.setter
    def WrittenText(self, WrittenText):
        self._WrittenText = WrittenText

    @property
    def StartMs(self):
        """Start time of a sentence (ms).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StartMs

    @StartMs.setter
    def StartMs(self, StartMs):
        self._StartMs = StartMs

    @property
    def EndMs(self):
        """End time of a sentence (ms).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EndMs

    @EndMs.setter
    def EndMs(self, EndMs):
        self._EndMs = EndMs

    @property
    def WordsNum(self):
        """Number of words in a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WordsNum

    @WordsNum.setter
    def WordsNum(self, WordsNum):
        self._WordsNum = WordsNum

    @property
    def Words(self):
        """Word details of a sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SentenceWords
        """
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SpeechSpeed(self):
        """Speech speed of a sentence. Unit: Number of words per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._SpeechSpeed

    @SpeechSpeed.setter
    def SpeechSpeed(self, SpeechSpeed):
        self._SpeechSpeed = SpeechSpeed

    @property
    def SpeakerId(self):
        """Channel or speaker ID. (If speaker_diarization is specified or ChannelNum is set to 2 (stereo) in the request, speakers or channels can be distinguished.)
Different values represent different speakers in mono mode. For the speakerId values, 0 represents the left channel, and 1 represents the right channel in stereo mode if an 8k engine is used.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SpeakerId

    @SpeakerId.setter
    def SpeakerId(self, SpeakerId):
        self._SpeakerId = SpeakerId

    @property
    def EmotionalEnergy(self):
        """Emotional energy value. This value is the result of dividing the sound volume in dB by 10. Value range: [1,10]. The higher the value, the stronger the emotion.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._EmotionalEnergy

    @EmotionalEnergy.setter
    def EmotionalEnergy(self, EmotionalEnergy):
        self._EmotionalEnergy = EmotionalEnergy

    @property
    def SilenceTime(self):
        """Silent duration between the current sentence and the last sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SilenceTime

    @SilenceTime.setter
    def SilenceTime(self, SilenceTime):
        self._SilenceTime = SilenceTime

    @property
    def EmotionType(self):
        """Emotion type. (This parameter may be left blank in two scenarios: 1. No corresponding resource package exists; 2. The emotion is not recognized because it is not strong enough, which is related to the emotional energy.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._EmotionType

    @EmotionType.setter
    def EmotionType(self, EmotionType):
        self._EmotionType = EmotionType

    @property
    def KeyWordResults(self):
        """List of recognized keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyWordResult
        """
        return self._KeyWordResults

    @KeyWordResults.setter
    def KeyWordResults(self, KeyWordResults):
        self._KeyWordResults = KeyWordResults


    def _deserialize(self, params):
        self._FinalSentence = params.get("FinalSentence")
        self._SliceSentence = params.get("SliceSentence")
        self._WrittenText = params.get("WrittenText")
        self._StartMs = params.get("StartMs")
        self._EndMs = params.get("EndMs")
        self._WordsNum = params.get("WordsNum")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = SentenceWords()
                obj._deserialize(item)
                self._Words.append(obj)
        self._SpeechSpeed = params.get("SpeechSpeed")
        self._SpeakerId = params.get("SpeakerId")
        self._EmotionalEnergy = params.get("EmotionalEnergy")
        self._SilenceTime = params.get("SilenceTime")
        self._EmotionType = params.get("EmotionType")
        if params.get("KeyWordResults") is not None:
            self._KeyWordResults = []
            for item in params.get("KeyWordResults"):
                obj = KeyWordResult()
                obj._deserialize(item)
                self._KeyWordResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceWords(AbstractModel):
    """Word text in the recognition result and the corresponding time offset.

    """

    def __init__(self):
        r"""
        :param _Word: Word text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Word: str
        :param _OffsetStartMs: Start time offset in the sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OffsetStartMs: int
        :param _OffsetEndMs: End time offset in the sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OffsetEndMs: int
        """
        self._Word = None
        self._OffsetStartMs = None
        self._OffsetEndMs = None

    @property
    def Word(self):
        """Word text.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def OffsetStartMs(self):
        """Start time offset in the sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OffsetStartMs

    @OffsetStartMs.setter
    def OffsetStartMs(self, OffsetStartMs):
        self._OffsetStartMs = OffsetStartMs

    @property
    def OffsetEndMs(self):
        """End time offset in the sentence.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OffsetEndMs

    @OffsetEndMs.setter
    def OffsetEndMs(self, OffsetEndMs):
        self._OffsetEndMs = OffsetEndMs


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._OffsetStartMs = params.get("OffsetStartMs")
        self._OffsetEndMs = params.get("OffsetEndMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Returned data of the [recording recognition] (https://intl.cloud.tencent.com/document/product/1093/37823?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) or [asynchronous real-time audio recognition] (https://intl.cloud.tencent.com/document/product/1093/52061?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) request.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID. This ID can be used to obtain the recognition status and results through polling. The data type of TaskId is ** uint64 **.
** Note: The task ID is valid for 24 hours, and duplicate task IDs of different dates may exist. Do not use task ID as the unique ID in your business system. **
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Task ID. This ID can be used to obtain the recognition status and results through polling. The data type of TaskId is ** uint64 **.
** Note: The task ID is valid for 24 hours, and duplicate task IDs of different dates may exist. Do not use task ID as the unique ID in your business system. **
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """[Response parameters for obtaining recording recognition results] (https://intl.cloud.tencent.com/document/product/1093/37822?from_cn_redirect=1#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID. Note: The data type of TaskId is uint64.
        :type TaskId: int
        :param _Status: Task status code. 0: waiting; 1: in process; 2: success; 3: failed.
        :type Status: int
        :param _StatusStr: Task status. Valid values: waiting, in process, success, and failed.
        :type StatusStr: str
        :param _Result: Recognition result.
        :type Result: str
        :param _ErrorMsg: Failure cause.
        :type ErrorMsg: str
        :param _ResultDetail: Recognition result details, including word time offsets for each sentence, which is generally used in subtitle generation scenarios. (This field is not left blank when ResTextFormat in the recording recognition request is set to 1.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultDetail: list of SentenceDetail
        :param _AudioDuration: Audio duration (seconds).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AudioDuration: float
        """
        self._TaskId = None
        self._Status = None
        self._StatusStr = None
        self._Result = None
        self._ErrorMsg = None
        self._ResultDetail = None
        self._AudioDuration = None

    @property
    def TaskId(self):
        """Task ID. Note: The data type of TaskId is uint64.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """Task status code. 0: waiting; 1: in process; 2: success; 3: failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusStr(self):
        """Task status. Valid values: waiting, in process, success, and failed.
        :rtype: str
        """
        return self._StatusStr

    @StatusStr.setter
    def StatusStr(self, StatusStr):
        self._StatusStr = StatusStr

    @property
    def Result(self):
        """Recognition result.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrorMsg(self):
        """Failure cause.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ResultDetail(self):
        """Recognition result details, including word time offsets for each sentence, which is generally used in subtitle generation scenarios. (This field is not left blank when ResTextFormat in the recording recognition request is set to 1.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SentenceDetail
        """
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def AudioDuration(self):
        """Audio duration (seconds).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._AudioDuration

    @AudioDuration.setter
    def AudioDuration(self, AudioDuration):
        self._AudioDuration = AudioDuration


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._StatusStr = params.get("StatusStr")
        self._Result = params.get("Result")
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("ResultDetail") is not None:
            self._ResultDetail = []
            for item in params.get("ResultDetail"):
                obj = SentenceDetail()
                obj._deserialize(item)
                self._ResultDetail.append(obj)
        self._AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        