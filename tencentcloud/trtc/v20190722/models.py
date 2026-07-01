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


class AbnormalEvent(AbstractModel):
    r"""The information of an error event (the possible cause of an abnormal user experience).

    """

    def __init__(self):
        r"""
        :param _AbnormalEventId: Exception event ID. view the specific value in the appendix: abnormal experience ID [mapping table](https://trtc.io/document/37906)
        :type AbnormalEventId: int
        :param _PeerId: Remote user ID,"": indicates the exception event is not user-generated.
        :type PeerId: str
        """
        self._AbnormalEventId = None
        self._PeerId = None

    @property
    def AbnormalEventId(self):
        r"""Exception event ID. view the specific value in the appendix: abnormal experience ID [mapping table](https://trtc.io/document/37906)
        :rtype: int
        """
        return self._AbnormalEventId

    @AbnormalEventId.setter
    def AbnormalEventId(self, AbnormalEventId):
        self._AbnormalEventId = AbnormalEventId

    @property
    def PeerId(self):
        r"""Remote user ID,"": indicates the exception event is not user-generated.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        self._AbnormalEventId = params.get("AbnormalEventId")
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalExperience(AbstractModel):
    r"""The information of an abnormal user experience and the possible causes.

    """

    def __init__(self):
        r"""
        :param _UserId: The user ID.
        :type UserId: str
        :param _ExperienceId: The abnormal experience ID.
        :type ExperienceId: int
        :param _RoomId: The room ID (string).
        :type RoomId: str
        :param _AbnormalEventList: The possible error events.
        :type AbnormalEventList: list of AbnormalEvent
        :param _EventTime: The report time.
        :type EventTime: int
        """
        self._UserId = None
        self._ExperienceId = None
        self._RoomId = None
        self._AbnormalEventList = None
        self._EventTime = None

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ExperienceId(self):
        r"""The abnormal experience ID.
        :rtype: int
        """
        return self._ExperienceId

    @ExperienceId.setter
    def ExperienceId(self, ExperienceId):
        self._ExperienceId = ExperienceId

    @property
    def RoomId(self):
        r"""The room ID (string).
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AbnormalEventList(self):
        r"""The possible error events.
        :rtype: list of AbnormalEvent
        """
        return self._AbnormalEventList

    @AbnormalEventList.setter
    def AbnormalEventList(self, AbnormalEventList):
        self._AbnormalEventList = AbnormalEventList

    @property
    def EventTime(self):
        r"""The report time.
        :rtype: int
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._ExperienceId = params.get("ExperienceId")
        self._RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self._AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self._AbnormalEventList.append(obj)
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentConfig(AbstractModel):
    r"""Bot parameters.

    """

    def __init__(self):
        r"""
        :param _UserId: The robot's UserId is used to enter a room and initiate a task. note that this UserId cannot be duplicated with the host or audience [UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#UserId) in the current room. if multiple tasks are initiated in a room, the robot's UserId cannot be mutually duplicated. otherwise, the previous task will be interrupted. ensure the robot's UserId is unique in the room.
        :type UserId: str
        :param _UserSig: Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. for specific calculation methods, see TRTC solution for calculating.
        :type UserSig: str
        :param _TargetUserId: UserId for robot stream pulling. after fill, the robot performs stream pulling and processes in real time.
        :type TargetUserId: str
        :param _MaxIdleTime: Exceeding MaxIdleTime in the room with no streaming automatically shuts down the backend task. default value is 60s.
        :type MaxIdleTime: int
        :param _WelcomeMessage: Robot'S greeting.
        :type WelcomeMessage: str
        :param _InterruptMode: Intelligent interruption mode, defaults to 0. 0 means server-side automatic interruption. 1 means the server does not interrupt, and the client sends an interruption signal to perform interruption.
        :type InterruptMode: int
        :param _InterruptSpeechDuration: Used when InterruptMode is 0, in milliseconds, defaults to 500ms. indicates the server will interrupt when it detects continuous voice for InterruptSpeechDuration milliseconds.
        :type InterruptSpeechDuration: int
        :param _TurnDetectionMode: Controls the trigger mode for a new dialogue. default is 0.
-0 means a new dialogue is automatically triggered when the server detects a complete sentence through automatic speech recognition.
-1 indicates the client determines whether to manually send a chat signaling trigger for a new dialogue upon receiving the caption message.
        :type TurnDetectionMode: int
        :param _FilterOneWord: Whether to filter out sentences where the user only says one word. true indicates filtering, false indicates no filtering. default value is true.
        :type FilterOneWord: bool
        :param _WelcomeMessagePriority: Welcome message priority. valid values: 0 (default), 1 (high priority). high priority messages cannot be interrupted.
        :type WelcomeMessagePriority: int
        :param _FilterBracketsContent: For filtering LLM return content, do not play the content in brackets.
Chinese bracket ().
2: english parentheses.
3: chinese square brackets [].
4: english square brackets [].
5: english curly braces {}.
Empty by default, means no filtering.
        :type FilterBracketsContent: int
        :param _AmbientSound: Ambient sound settings.
        :type AmbientSound: :class:`tencentcloud.trtc.v20190722.models.AmbientSound`
        :param _VoicePrint: Voiceprint configuration.
        :type VoicePrint: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        :param _TurnDetection: Semantic sentence segmentation detection.
        :type TurnDetection: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        :param _SubtitleMode: Robot subtitle display mode.
-0 means display as soon as possible without synchronizing with audio playback. at this point, subtitles are fully delivered, and subsequent subtitles will include previous ones.
-1 indicates sentence-level real-time display, which synchronizes with audio playback. only when the current sentence's corresponding audio playback is complete will the next subtitle be delivered. at this point, subtitles are delivered incrementally, and the terminal needs to concatenate the leading and trailing subtitles to form a complete subtitle.
        :type SubtitleMode: int
        :param _InterruptWordList: Interruption word list. during AI speaking, only speak words in the list to interrupt AI speaking.
Note: interrupt words avoid triggering AI reply.
        :type InterruptWordList: list of str
        """
        self._UserId = None
        self._UserSig = None
        self._TargetUserId = None
        self._MaxIdleTime = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._TurnDetectionMode = None
        self._FilterOneWord = None
        self._WelcomeMessagePriority = None
        self._FilterBracketsContent = None
        self._AmbientSound = None
        self._VoicePrint = None
        self._TurnDetection = None
        self._SubtitleMode = None
        self._InterruptWordList = None

    @property
    def UserId(self):
        r"""The robot's UserId is used to enter a room and initiate a task. note that this UserId cannot be duplicated with the host or audience [UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#UserId) in the current room. if multiple tasks are initiated in a room, the robot's UserId cannot be mutually duplicated. otherwise, the previous task will be interrupted. ensure the robot's UserId is unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. for specific calculation methods, see TRTC solution for calculating.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def TargetUserId(self):
        r"""UserId for robot stream pulling. after fill, the robot performs stream pulling and processes in real time.
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId

    @property
    def MaxIdleTime(self):
        r"""Exceeding MaxIdleTime in the room with no streaming automatically shuts down the backend task. default value is 60s.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def WelcomeMessage(self):
        r"""Robot'S greeting.
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        r"""Intelligent interruption mode, defaults to 0. 0 means server-side automatic interruption. 1 means the server does not interrupt, and the client sends an interruption signal to perform interruption.
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        r"""Used when InterruptMode is 0, in milliseconds, defaults to 500ms. indicates the server will interrupt when it detects continuous voice for InterruptSpeechDuration milliseconds.
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def TurnDetectionMode(self):
        r"""Controls the trigger mode for a new dialogue. default is 0.
-0 means a new dialogue is automatically triggered when the server detects a complete sentence through automatic speech recognition.
-1 indicates the client determines whether to manually send a chat signaling trigger for a new dialogue upon receiving the caption message.
        :rtype: int
        """
        return self._TurnDetectionMode

    @TurnDetectionMode.setter
    def TurnDetectionMode(self, TurnDetectionMode):
        self._TurnDetectionMode = TurnDetectionMode

    @property
    def FilterOneWord(self):
        r"""Whether to filter out sentences where the user only says one word. true indicates filtering, false indicates no filtering. default value is true.
        :rtype: bool
        """
        return self._FilterOneWord

    @FilterOneWord.setter
    def FilterOneWord(self, FilterOneWord):
        self._FilterOneWord = FilterOneWord

    @property
    def WelcomeMessagePriority(self):
        r"""Welcome message priority. valid values: 0 (default), 1 (high priority). high priority messages cannot be interrupted.
        :rtype: int
        """
        return self._WelcomeMessagePriority

    @WelcomeMessagePriority.setter
    def WelcomeMessagePriority(self, WelcomeMessagePriority):
        self._WelcomeMessagePriority = WelcomeMessagePriority

    @property
    def FilterBracketsContent(self):
        r"""For filtering LLM return content, do not play the content in brackets.
Chinese bracket ().
2: english parentheses.
3: chinese square brackets [].
4: english square brackets [].
5: english curly braces {}.
Empty by default, means no filtering.
        :rtype: int
        """
        return self._FilterBracketsContent

    @FilterBracketsContent.setter
    def FilterBracketsContent(self, FilterBracketsContent):
        self._FilterBracketsContent = FilterBracketsContent

    @property
    def AmbientSound(self):
        r"""Ambient sound settings.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AmbientSound`
        """
        return self._AmbientSound

    @AmbientSound.setter
    def AmbientSound(self, AmbientSound):
        self._AmbientSound = AmbientSound

    @property
    def VoicePrint(self):
        r"""Voiceprint configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        """
        return self._VoicePrint

    @VoicePrint.setter
    def VoicePrint(self, VoicePrint):
        self._VoicePrint = VoicePrint

    @property
    def TurnDetection(self):
        r"""Semantic sentence segmentation detection.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        return self._TurnDetection

    @TurnDetection.setter
    def TurnDetection(self, TurnDetection):
        self._TurnDetection = TurnDetection

    @property
    def SubtitleMode(self):
        r"""Robot subtitle display mode.
-0 means display as soon as possible without synchronizing with audio playback. at this point, subtitles are fully delivered, and subsequent subtitles will include previous ones.
-1 indicates sentence-level real-time display, which synchronizes with audio playback. only when the current sentence's corresponding audio playback is complete will the next subtitle be delivered. at this point, subtitles are delivered incrementally, and the terminal needs to concatenate the leading and trailing subtitles to form a complete subtitle.
        :rtype: int
        """
        return self._SubtitleMode

    @SubtitleMode.setter
    def SubtitleMode(self, SubtitleMode):
        self._SubtitleMode = SubtitleMode

    @property
    def InterruptWordList(self):
        r"""Interruption word list. during AI speaking, only speak words in the list to interrupt AI speaking.
Note: interrupt words avoid triggering AI reply.
        :rtype: list of str
        """
        return self._InterruptWordList

    @InterruptWordList.setter
    def InterruptWordList(self, InterruptWordList):
        self._InterruptWordList = InterruptWordList


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._TargetUserId = params.get("TargetUserId")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._TurnDetectionMode = params.get("TurnDetectionMode")
        self._FilterOneWord = params.get("FilterOneWord")
        self._WelcomeMessagePriority = params.get("WelcomeMessagePriority")
        self._FilterBracketsContent = params.get("FilterBracketsContent")
        if params.get("AmbientSound") is not None:
            self._AmbientSound = AmbientSound()
            self._AmbientSound._deserialize(params.get("AmbientSound"))
        if params.get("VoicePrint") is not None:
            self._VoicePrint = VoicePrint()
            self._VoicePrint._deserialize(params.get("VoicePrint"))
        if params.get("TurnDetection") is not None:
            self._TurnDetection = TurnDetection()
            self._TurnDetection._deserialize(params.get("TurnDetection"))
        self._SubtitleMode = params.get("SubtitleMode")
        self._InterruptWordList = params.get("InterruptWordList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentParams(AbstractModel):
    r"""The information of the relaying robot in the room.

    """

    def __init__(self):
        r"""
        :param _UserId: The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to a login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :type UserSig: str
        :param _MaxIdleTime: The timeout period (seconds) for relaying to stop automatically after all the users whose streams are mixed leave the room. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :type MaxIdleTime: int
        """
        self._UserId = None
        self._UserSig = None
        self._MaxIdleTime = None

    @property
    def UserId(self):
        r"""The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""The signature (similar to a login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
        r"""The timeout period (seconds) for relaying to stop automatically after all the users whose streams are mixed leave the room. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlignmentItem(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _TimeBeginMs: 
        :type TimeBeginMs: int
        :param _TimeEndMs: 
        :type TimeEndMs: int
        :param _TextBegin: 
        :type TextBegin: int
        :param _TextEnd: 
        :type TextEnd: int
        """
        self._TimeBeginMs = None
        self._TimeEndMs = None
        self._TextBegin = None
        self._TextEnd = None

    @property
    def TimeBeginMs(self):
        r"""
        :rtype: int
        """
        return self._TimeBeginMs

    @TimeBeginMs.setter
    def TimeBeginMs(self, TimeBeginMs):
        self._TimeBeginMs = TimeBeginMs

    @property
    def TimeEndMs(self):
        r"""
        :rtype: int
        """
        return self._TimeEndMs

    @TimeEndMs.setter
    def TimeEndMs(self, TimeEndMs):
        self._TimeEndMs = TimeEndMs

    @property
    def TextBegin(self):
        r"""
        :rtype: int
        """
        return self._TextBegin

    @TextBegin.setter
    def TextBegin(self, TextBegin):
        self._TextBegin = TextBegin

    @property
    def TextEnd(self):
        r"""
        :rtype: int
        """
        return self._TextEnd

    @TextEnd.setter
    def TextEnd(self, TextEnd):
        self._TextEnd = TextEnd


    def _deserialize(self, params):
        self._TimeBeginMs = params.get("TimeBeginMs")
        self._TimeEndMs = params.get("TimeEndMs")
        self._TextBegin = params.get("TextBegin")
        self._TextEnd = params.get("TextEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AmbientSound(AbstractModel):
    r"""Background sound settings will add environmental sound effects during a call to make the experience more realistic. currently support the following options:.
    Coffee_shops: chat in a coffee shop communication environment with background chatter.
    busy office: customer service center.
    Street traffic: outdoors street.
    evening_mountain: outdoors mountain.

    """

    def __init__(self):
        r"""
        :param _Scene: Scenario selection.
        :type Scene: str
        :param _Volume: Control the volume of ambient sound. value ranges from [0,2]. the lower the value, the softer the ambient sound; the higher the value, the louder the ambient sound. if not set, use the default value 1.
        :type Volume: float
        """
        self._Scene = None
        self._Volume = None

    @property
    def Scene(self):
        r"""Scenario selection.
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Volume(self):
        r"""Control the volume of ambient sound. value ranges from [0,2]. the lower the value, the softer the ambient sound; the higher the value, the louder the ambient sound. if not set, use the default value 1.
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrParam(AbstractModel):
    r"""Parameters used in speech recognition

    """

    def __init__(self):
        r"""
        :param _Lang: <p>The model type used by the transcription service. Example value "bigmodel-zh". The languages supported by different package versions of speech to text are as follows:</p><ol><li>V2 version (recommended)</li></ol><p>"bigmodel-xxx": large model engine, recommended for use. "xxx" can be filled with specific languages, such as "bigmodel-zh". "xxx" can be filled with Chinese ("zh"), English ("en"), Cantonese ("yue"), Arabic ("ar"), German ("de"), French ("fr"), Spanish ("es"), Portuguese ("pt"), Indonesian ("id"), Italian ("it"), Korean ("ko"), Russian ("ru"), Thai ("th"), Vietnamese ("vi"), Japanese ("ja"), Turkish ("tr"), Hindi ("hi"), Malay ("ms"), Dutch ("nl"), Swedish ("sv"), Danish ("da"), Finnish ("fi"), Polish ("pl"), Czech ("cs"), Filipino ("fil"), Persian ("fa"), Greek ("el"), Hungarian ("hu"), Macedonian ("mk"), Romanian ("ro").</p><ol start="2"><li>V1 version (legacy version)</li></ol><p>Standard language engine:</p><ul><li>"16k_zh_large": 16k large model engine, simultaneously supports Chinese, English, and multiple Chinese dialects with accent recognition.</li><li>"16k_zh_en": latest 16k Chinese-English large model engine, simultaneously supports Chinese, English, and multiple Chinese dialects with accent recognition, optimized for Chinese-English mixed scenarios.</li></ul><p>Advanced language engine:</p><ul><li>"zh-yue": Cantonese Chinese</li><li>"vi": Vietnamese</li><li>"ja": Japanese</li><li>"ko": Korean</li><li>"id": Indonesian</li><li>"th": Thai</li><li>"pt": Portuguese</li><li>"tr": Turkish</li><li>"ar": Arabic</li><li>"es": Spanish</li><li>"hi": Hindi</li><li>"fr": French</li><li>"ms": Malay</li><li>"fil": Filipino</li><li>"de": German</li><li>"it": Italian</li><li>"ru": Russian</li><li>"sv": Swedish</li><li>"da": Danish</li><li>"no": Norwegian</li></ul><p>Note:<br>If the language you need is not available, contact our technical support.</p>
        :type Lang: str
        :param _VadSilenceTime: <p>The time when speech recognition vad ranges from 240 to 2000, with a default of 1000. The unit is ms. A smaller value enables faster sentence segmentation for speech recognition.<br>Example value: 1000</p>
        :type VadSilenceTime: int
        :param _HotWordList: <p>Temporary term list: improves recognition accuracy by biasing the ASR engine toward specific terms.</p>
<ul>
<li>Single term format: term|weight. Each term must not exceed 30 characters (or 10 Chinese characters). Weight must be an integer from [1-11] or 100. Examples: Tencent Cloud|5, ASR|11.</li>
<li>List format and limits: separate multiple terms with commas. Up to 128 terms are supported. Example: Tencent Cloud|10,speech recognition|5,ASR|11.<br>
Note:<br>
When the term weight is set to 11, the term is treated as a high-priority super term. Use weight 11 only for terms that are critical and must be recognized reliably. Setting too many terms to weight 11 may reduce overall accuracy.<br>
When the term weight is set to 100, the term enables homophone replacement. For example, when the configuration is write|100, any recognized homophone of "write" (such as "right") is forcibly replaced with "write". Enable this feature only when needed, and reserve weight 100 for terms where homophone confusion is a real problem. Setting too many terms to weight 100 may reduce overall accuracy.<br>
Terms must not contain spaces. Invalid example: ASR Tencent Cloud<br>
Example value: voice assistant|10</li>
</ul>
        :type HotWordList: str
        :param _AlternativeLanguage: <p>Fuzzy recognition is an advanced language engine feature. You can only specify advanced language engines other than zh-dialect and zh-yue. Note: You can specify up to 4 languages.</p>
        :type AlternativeLanguage: list of str
        :param _VadLevel: <p>The far-field voice suppression capacity of vad (without impacting asr recognition accuracy) ranges from [0, 3], defaulting to 0. Recommended setting is 2 for better far-field voice suppression capacity.</p>
        :type VadLevel: int
        :param _FilterDirty: <p>Whether to filter profanity (currently only support basic language engine and standard language engine), range [0, 2], default value 0.<br>0: not filter profanity; 1: filter dirty words; 2: replace with " * ".</p>
        :type FilterDirty: int
        :param _FilterModal: <p>Whether to filter modal particles (currently only support basic language engine and standard language engine). Range: [0, 2]. Default value: 0.<br>0: Do not filter modal particles; 1: Partial filtering; 2: Strict filtering.</p>
        :type FilterModal: int
        :param _FilterPunc: <p>Whether to filter periods at the end of sentences (currently only support basic language engine and standard language engine), range [0, 1], default value 0.<br>0: does not filter periods at the end of sentences; 1: filter out periods at the end of sentences.</p>
        :type FilterPunc: int
        """
        self._Lang = None
        self._VadSilenceTime = None
        self._HotWordList = None
        self._AlternativeLanguage = None
        self._VadLevel = None
        self._FilterDirty = None
        self._FilterModal = None
        self._FilterPunc = None

    @property
    def Lang(self):
        r"""<p>The model type used by the transcription service. Example value "bigmodel-zh". The languages supported by different package versions of speech to text are as follows:</p><ol><li>V2 version (recommended)</li></ol><p>"bigmodel-xxx": large model engine, recommended for use. "xxx" can be filled with specific languages, such as "bigmodel-zh". "xxx" can be filled with Chinese ("zh"), English ("en"), Cantonese ("yue"), Arabic ("ar"), German ("de"), French ("fr"), Spanish ("es"), Portuguese ("pt"), Indonesian ("id"), Italian ("it"), Korean ("ko"), Russian ("ru"), Thai ("th"), Vietnamese ("vi"), Japanese ("ja"), Turkish ("tr"), Hindi ("hi"), Malay ("ms"), Dutch ("nl"), Swedish ("sv"), Danish ("da"), Finnish ("fi"), Polish ("pl"), Czech ("cs"), Filipino ("fil"), Persian ("fa"), Greek ("el"), Hungarian ("hu"), Macedonian ("mk"), Romanian ("ro").</p><ol start="2"><li>V1 version (legacy version)</li></ol><p>Standard language engine:</p><ul><li>"16k_zh_large": 16k large model engine, simultaneously supports Chinese, English, and multiple Chinese dialects with accent recognition.</li><li>"16k_zh_en": latest 16k Chinese-English large model engine, simultaneously supports Chinese, English, and multiple Chinese dialects with accent recognition, optimized for Chinese-English mixed scenarios.</li></ul><p>Advanced language engine:</p><ul><li>"zh-yue": Cantonese Chinese</li><li>"vi": Vietnamese</li><li>"ja": Japanese</li><li>"ko": Korean</li><li>"id": Indonesian</li><li>"th": Thai</li><li>"pt": Portuguese</li><li>"tr": Turkish</li><li>"ar": Arabic</li><li>"es": Spanish</li><li>"hi": Hindi</li><li>"fr": French</li><li>"ms": Malay</li><li>"fil": Filipino</li><li>"de": German</li><li>"it": Italian</li><li>"ru": Russian</li><li>"sv": Swedish</li><li>"da": Danish</li><li>"no": Norwegian</li></ul><p>Note:<br>If the language you need is not available, contact our technical support.</p>
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def VadSilenceTime(self):
        r"""<p>The time when speech recognition vad ranges from 240 to 2000, with a default of 1000. The unit is ms. A smaller value enables faster sentence segmentation for speech recognition.<br>Example value: 1000</p>
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def HotWordList(self):
        r"""<p>Temporary term list: improves recognition accuracy by biasing the ASR engine toward specific terms.</p>
<ul>
<li>Single term format: term|weight. Each term must not exceed 30 characters (or 10 Chinese characters). Weight must be an integer from [1-11] or 100. Examples: Tencent Cloud|5, ASR|11.</li>
<li>List format and limits: separate multiple terms with commas. Up to 128 terms are supported. Example: Tencent Cloud|10,speech recognition|5,ASR|11.<br>
Note:<br>
When the term weight is set to 11, the term is treated as a high-priority super term. Use weight 11 only for terms that are critical and must be recognized reliably. Setting too many terms to weight 11 may reduce overall accuracy.<br>
When the term weight is set to 100, the term enables homophone replacement. For example, when the configuration is write|100, any recognized homophone of "write" (such as "right") is forcibly replaced with "write". Enable this feature only when needed, and reserve weight 100 for terms where homophone confusion is a real problem. Setting too many terms to weight 100 may reduce overall accuracy.<br>
Terms must not contain spaces. Invalid example: ASR Tencent Cloud<br>
Example value: voice assistant|10</li>
</ul>
        :rtype: str
        """
        return self._HotWordList

    @HotWordList.setter
    def HotWordList(self, HotWordList):
        self._HotWordList = HotWordList

    @property
    def AlternativeLanguage(self):
        r"""<p>Fuzzy recognition is an advanced language engine feature. You can only specify advanced language engines other than zh-dialect and zh-yue. Note: You can specify up to 4 languages.</p>
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def VadLevel(self):
        r"""<p>The far-field voice suppression capacity of vad (without impacting asr recognition accuracy) ranges from [0, 3], defaulting to 0. Recommended setting is 2 for better far-field voice suppression capacity.</p>
        :rtype: int
        """
        return self._VadLevel

    @VadLevel.setter
    def VadLevel(self, VadLevel):
        self._VadLevel = VadLevel

    @property
    def FilterDirty(self):
        r"""<p>Whether to filter profanity (currently only support basic language engine and standard language engine), range [0, 2], default value 0.<br>0: not filter profanity; 1: filter dirty words; 2: replace with " * ".</p>
        :rtype: int
        """
        return self._FilterDirty

    @FilterDirty.setter
    def FilterDirty(self, FilterDirty):
        self._FilterDirty = FilterDirty

    @property
    def FilterModal(self):
        r"""<p>Whether to filter modal particles (currently only support basic language engine and standard language engine). Range: [0, 2]. Default value: 0.<br>0: Do not filter modal particles; 1: Partial filtering; 2: Strict filtering.</p>
        :rtype: int
        """
        return self._FilterModal

    @FilterModal.setter
    def FilterModal(self, FilterModal):
        self._FilterModal = FilterModal

    @property
    def FilterPunc(self):
        r"""<p>Whether to filter periods at the end of sentences (currently only support basic language engine and standard language engine), range [0, 1], default value 0.<br>0: does not filter periods at the end of sentences; 1: filter out periods at the end of sentences.</p>
        :rtype: int
        """
        return self._FilterPunc

    @FilterPunc.setter
    def FilterPunc(self, FilterPunc):
        self._FilterPunc = FilterPunc


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._VadSilenceTime = params.get("VadSilenceTime")
        self._HotWordList = params.get("HotWordList")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._VadLevel = params.get("VadLevel")
        self._FilterDirty = params.get("FilterDirty")
        self._FilterModal = params.get("FilterModal")
        self._FilterPunc = params.get("FilterPunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncode(AbstractModel):
    r"""The audio encoding parameters.

    """

    def __init__(self):
        r"""
        :param _SampleRate: The audio sample rate (Hz). Valid values: 48000, 44100, 32000, 24000, 16000, 8000.
        :type SampleRate: int
        :param _Channel: The number of sound channels. Valid values: 1 (mono), 2 (dual).
        :type Channel: int
        :param _BitRate: The audio bitrate (Kbps). Value range: 8-500.
        :type BitRate: int
        :param _Codec: The audio codec. Valid values: 0 (LC-AAC), 1 (HE-AAC), 2 (HE-AACv2). The default value is 0. If this parameter is set to 2, `Channel` must be 2. If it is set to 1 or 2, `SampleRate` can only be 48000, 44100, 32000, 24000, or 16000.
        :type Codec: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None
        self._Codec = None

    @property
    def SampleRate(self):
        r"""The audio sample rate (Hz). Valid values: 48000, 44100, 32000, 24000, 16000, 8000.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""The number of sound channels. Valid values: 1 (mono), 2 (dual).
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""The audio bitrate (Kbps). Value range: 8-500.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Codec(self):
        r"""The audio codec. Valid values: 0 (LC-AAC), 1 (HE-AAC), 2 (HE-AACv2). The default value is 0. If this parameter is set to 2, `Channel` must be 2. If it is set to 1 or 2, `SampleRate` can only be 48000, 44100, 32000, 24000, or 16000.
        :rtype: int
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncodeParams(AbstractModel):
    r"""Audio transcoding parameters

    """

    def __init__(self):
        r"""
        :param _SampleRate: Audio Sample rate, Value range [48000, 44100], unit is Hz.
        :type SampleRate: int
        :param _Channel: Audio Channel number, Value range [1,2], 1 means Audio is Mono-channel, 2 means Audio is Dual-channel.
        :type Channel: int
        :param _BitRate: Audio Bitrate, Value range [8,500], unit is kbps.
        :type BitRate: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None

    @property
    def SampleRate(self):
        r"""Audio Sample rate, Value range [48000, 44100], unit is Hz.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""Audio Channel number, Value range [1,2], 1 means Audio is Mono-channel, 2 means Audio is Dual-channel.
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""Audio Bitrate, Value range [8,500], unit is kbps.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioFormat(AbstractModel):
    r"""Format of TTS audio output.

    """

    def __init__(self):
        r"""
        :param _Format: Generated audio format.

-TextToSpeechSSE streaming API.

Supports pcm. default: pcm.

-TextToSpeech non-streaming API.

Supports pcm, wav, mp3. default: pcm.
        :type Format: str
        :param _SampleRate: Generated audio sample rate. default 24000.
Selectable.
- 16000
- 24000 
        :type SampleRate: int
        :param _Bitrate: MP3 bitrate (kbps), only applicable to mp3 format. can choose: `64`, `128`, `192`, `256`. default: `128`.
        :type Bitrate: int
        """
        self._Format = None
        self._SampleRate = None
        self._Bitrate = None

    @property
    def Format(self):
        r"""Generated audio format.

-TextToSpeechSSE streaming API.

Supports pcm. default: pcm.

-TextToSpeech non-streaming API.

Supports pcm, wav, mp3. default: pcm.
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def SampleRate(self):
        r"""Generated audio sample rate. default 24000.
Selectable.
- 16000
- 24000 
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Bitrate(self):
        r"""MP3 bitrate (kbps), only applicable to mp3 format. can choose: `64`, `128`, `192`, `256`. default: `128`.
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._SampleRate = params.get("SampleRate")
        self._Bitrate = params.get("Bitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioParams(AbstractModel):
    r"""The audio transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param _SampleRate: The audio sample rate.
1: 48000 Hz (default)
2: 44100 Hz
3: 16000 Hz
        :type SampleRate: int
        :param _Channel: The number of sound channels.
1: Mono-channel
2: Dual-channel (default)
        :type Channel: int
        :param _BitRate: The audio bitrate (bps). Value range: [32000, 128000]. Default: 64000.
        :type BitRate: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None

    @property
    def SampleRate(self):
        r"""The audio sample rate.
1: 48000 Hz (default)
2: 44100 Hz
3: 16000 Hz
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""The number of sound channels.
1: Mono-channel
2: Dual-channel (default)
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""The audio bitrate (bps). Value range: [32000, 128000]. Default: 64000.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudModerationStorage(AbstractModel):
    r"""Information about Tencent COS and third-party cloud storage accounts.

    """

    def __init__(self):
        r"""
        :param _Vendor: Information about Tencent COS and third-party cloud storage accounts.
0: Tencent COS.
1: AWS S3.
2: Alibaba Cloud OSS.
Example value: 0.
        :type Vendor: int
        :param _Region: [Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of Tencent COS.
Example value: cn-shanghai-1.

[Region information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
Example value: ap-southeast-3.	
        :type Region: str
        :param _Bucket: Cloud bucket name.
        :type Bucket: str
        :param _AccessKey: access_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
Example value: test-accesskey.
        :type AccessKey: str
        :param _SecretKey: secret_key account information of cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
Example value: test-secretkey.
        :type SecretKey: str
        :param _FileNamePrefix: Specified location of the cloud bucket, which consists of arrays of strings. Value range for the strings is lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and special characters (_-). For example, under the feature of ["prefix1", "prefix2"], the audio slicing file (xxx.mp3) is stored as prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC time}.ogg, while the video frame is stored as prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC time}.png.
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""Information about Tencent COS and third-party cloud storage accounts.
0: Tencent COS.
1: AWS S3.
2: Alibaba Cloud OSS.
Example value: 0.
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""[Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of Tencent COS.
Example value: cn-shanghai-1.

[Region information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
Example value: ap-southeast-3.	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""Cloud bucket name.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""access_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
Example value: test-accesskey.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""secret_key account information of cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
Example value: test-secretkey.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""Specified location of the cloud bucket, which consists of arrays of strings. Value range for the strings is lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and special characters (_-). For example, under the feature of ["prefix1", "prefix2"], the audio slicing file (xxx.mp3) is stored as prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC time}.ogg, while the video frame is stored as prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC time}.png.
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSliceStorage(AbstractModel):
    r"""Information about Tencent COS and third-party cloud storage accounts.

    """

    def __init__(self):
        r"""
        :param _Vendor: Information about Tencent COS and third-party cloud storage accounts.
0: Tencent COS.
1: AWS S3.
2: Alibaba Cloud OSS.
Example value: 0.
        :type Vendor: int
        :param _Region: [Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of Tencent COS.
Example value: cn-shanghai-1.
[Region information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
Example value: ap-southeast-3.	
        :type Region: str
        :param _Bucket: Cloud bucket name.
        :type Bucket: str
        :param _AccessKey: access_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
Example value: test-accesskey.
        :type AccessKey: str
        :param _SecretKey: secret_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
Example value: test-secretkey.
        :type SecretKey: str
        :param _FileNamePrefix: Specified location of the cloud bucket, which consists of an array of strings. Value range for the strings is lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and special characters (_-). For example, under the feature of ["prefix1", "prefix2"], the audio slicing file (xxx.mp3) is stored as prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC time}.ogg, while the video frame is stored as prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC time}.png.
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""Information about Tencent COS and third-party cloud storage accounts.
0: Tencent COS.
1: AWS S3.
2: Alibaba Cloud OSS.
Example value: 0.
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""[Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of Tencent COS.
Example value: cn-shanghai-1.
[Region information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
Example value: ap-southeast-3.	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""Cloud bucket name.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""access_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
Example value: test-accesskey.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""secret_key account information of the cloud storage.
To store files to Tencent COS, visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
Example value: test-secretkey.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""Specified location of the cloud bucket, which consists of an array of strings. Value range for the strings is lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and special characters (_-). For example, under the feature of ["prefix1", "prefix2"], the audio slicing file (xxx.mp3) is stored as prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC time}.ogg, while the video frame is stored as prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC time}.png.
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorage(AbstractModel):
    r"""The cloud storage information.

    """

    def __init__(self):
        r"""
        :param _Vendor: The cloud storage provider.
`0`: Tencent Cloud COS; `1`: AWS storage. Other vendors are not supported currently.
        :type Vendor: int
        :param _Region: [Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of tencent cloud object storage.
Example value: cn-shanghai-1.

[Region information](https://docs.AWS.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
        :type Region: str
        :param _Bucket: The storage bucket.
        :type Bucket: str
        :param _AccessKey: access_key account information of the cloud storage.
To store files to tencent cloud object storage (COS), visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
        :type AccessKey: str
        :param _SecretKey: secret_key account information of the cloud storage.
To store files to tencent cloud object storage (COS), visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
        :type SecretKey: str
        :param _FileNamePrefix: The specified position of the cloud storage bucket consists of an array of strings. valid values: az, az, 0-9, '_', and '-'. for example, the recording file xxx.m3u8 becomes prefix1/prefix2/TaskId/xxx.m3u8 under the function of ["prefix1", "prefix2"].
        :type FileNamePrefix: list of str
        :param _EndpointUrl: If specified, the client uses this S3-compatible endpoint override instead of the default AWS S3 endpoint. This is useful for S3-compatible storage services such as Cloudflare R2. Example: "account_id.r2.cloudflarestorage.com"
        :type EndpointUrl: str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None
        self._EndpointUrl = None

    @property
    def Vendor(self):
        r"""The cloud storage provider.
`0`: Tencent Cloud COS; `1`: AWS storage. Other vendors are not supported currently.
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""[Region information](https://www.tencentcloud.com/document/product/436/6224?from_cn_redirect=1#.E5.9C.B0.E5.9F.9F) of tencent cloud object storage.
Example value: cn-shanghai-1.

[Region information](https://docs.AWS.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) of AWS S3.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""The storage bucket.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""access_key account information of the cloud storage.
To store files to tencent cloud object storage (COS), visit https://console.cloud.tencent.com/cam/capi to view or create the SecretId value corresponding to the key fields in the link.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""secret_key account information of the cloud storage.
To store files to tencent cloud object storage (COS), visit https://console.cloud.tencent.com/cam/capi to view or create the SecretKey value corresponding to the key fields in the link.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""The specified position of the cloud storage bucket consists of an array of strings. valid values: az, az, 0-9, '_', and '-'. for example, the recording file xxx.m3u8 becomes prefix1/prefix2/TaskId/xxx.m3u8 under the function of ["prefix1", "prefix2"].
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix

    @property
    def EndpointUrl(self):
        r"""If specified, the client uses this S3-compatible endpoint override instead of the default AWS S3 endpoint. This is useful for S3-compatible storage services such as Cloudflare R2. Example: "account_id.r2.cloudflarestorage.com"
        :rtype: str
        """
        return self._EndpointUrl

    @EndpointUrl.setter
    def EndpointUrl(self, EndpointUrl):
        self._EndpointUrl = EndpointUrl


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        self._EndpointUrl = params.get("EndpointUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudVod(AbstractModel):
    r"""The VOD parameters.

    """

    def __init__(self):
        r"""
        :param _TencentVod: The Tencent Cloud VOD parameters.
        :type TencentVod: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        self._TencentVod = None

    @property
    def TencentVod(self):
        r"""The Tencent Cloud VOD parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        return self._TencentVod

    @TencentVod.setter
    def TencentVod(self, TencentVod):
        self._TencentVod = TencentVod


    def _deserialize(self, params):
        if params.get("TencentVod") is not None:
            self._TencentVod = TencentVod()
            self._TencentVod._deserialize(params.get("TencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationRequest(AbstractModel):
    r"""ControlAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task unique identifier.
        :type TaskId: str
        :param _Command: Control command. currently supports the following commands: - ServerPushText: server sends text to the AI robot, and the AI robot will broadcast the text. - InvokeLLM: server sends text to the large model to trigger dialogue.
        :type Command: str
        :param _ServerPushText: Server-Sent broadcast text Command. required when Command is ServerPushText.
        :type ServerPushText: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        :param _InvokeLLM: The server sends a Command to proactively request the large model. when Command is InvokeLLM, it sends the content request to the large model and adds X-Invoke-LLM="1" to the header.
        :type InvokeLLM: :class:`tencentcloud.trtc.v20190722.models.InvokeLLM`
        """
        self._TaskId = None
        self._Command = None
        self._ServerPushText = None
        self._InvokeLLM = None

    @property
    def TaskId(self):
        r"""Task unique identifier.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Command(self):
        r"""Control command. currently supports the following commands: - ServerPushText: server sends text to the AI robot, and the AI robot will broadcast the text. - InvokeLLM: server sends text to the large model to trigger dialogue.
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServerPushText(self):
        r"""Server-Sent broadcast text Command. required when Command is ServerPushText.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        """
        return self._ServerPushText

    @ServerPushText.setter
    def ServerPushText(self, ServerPushText):
        self._ServerPushText = ServerPushText

    @property
    def InvokeLLM(self):
        r"""The server sends a Command to proactively request the large model. when Command is InvokeLLM, it sends the content request to the large model and adds X-Invoke-LLM="1" to the header.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.InvokeLLM`
        """
        return self._InvokeLLM

    @InvokeLLM.setter
    def InvokeLLM(self, InvokeLLM):
        self._InvokeLLM = InvokeLLM


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Command = params.get("Command")
        if params.get("ServerPushText") is not None:
            self._ServerPushText = ServerPushText()
            self._ServerPushText._deserialize(params.get("ServerPushText"))
        if params.get("InvokeLLM") is not None:
            self._InvokeLLM = InvokeLLM()
            self._InvokeLLM._deserialize(params.get("InvokeLLM"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationResponse(AbstractModel):
    r"""ControlAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateCloudModerationRequest(AbstractModel):
    r"""CreateCloudModeration request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) of TRTC, which is the same as the SdkAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _RoomId: [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) of TRTC, which is the RoomId corresponding to the TRTC room.
        :type RoomId: str
        :param _UserId: Chatbot's UserId, which is used to enter the room and initiate a moderation task. [*Note] This UserId should not be duplicated with the UserIds of the current anchors or audience members in the room. If multiple moderation tasks are initiated in one room, the chatbot's UserId should also be unique; otherwise, the previous moderation task is interrupted. It is recommended to include the room ID as part of the UserId, ensuring that the chatbot's UserId is unique in the room.
        :type UserId: str
        :param _UserSig: Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. For specific calculation methods, see TRTC solution for calculating UserSig.
        :type UserSig: str
        :param _ModerationParams: Control parameters for cloud moderation.
        :type ModerationParams: :class:`tencentcloud.trtc.v20190722.models.ModerationParams`
        :param _ModerationStorageParams: Parameters for uploading cloud moderation files to the cloud storage.
        :type ModerationStorageParams: :class:`tencentcloud.trtc.v20190722.models.ModerationStorageParams`
        :param _RoomIdType: Type of the TRTC room number. [*Note] It should be the same as the type of the RoomId corresponding to the recording room. 0: string type; 1: 32-bit integer type (default value). Example value: 1.
        :type RoomIdType: int
        :param _ResourceExpiredHour: Validity period for calling the task ID, which starts upon successful initiation of the task and obtaining the task ID. After the timeout, APIs such as querying, updating, or stopping cannot be called, but the moderation task is not stopped. The unit of the parameter is hours, with a default value of 24 hours (1 day). The maximum value is 72 hours (3 days), while the minimum value is 6 hours. For example, if this parameter is not specified, the validity period for calling the querying, updating, and stopping slicing APIs is 24 hours upon the successful start of slicing.
        :type ResourceExpiredHour: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._ModerationParams = None
        self._ModerationStorageParams = None
        self._RoomIdType = None
        self._ResourceExpiredHour = None

    @property
    def SdkAppId(self):
        r"""[SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) of TRTC, which is the same as the SdkAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""[RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) of TRTC, which is the RoomId corresponding to the TRTC room.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""Chatbot's UserId, which is used to enter the room and initiate a moderation task. [*Note] This UserId should not be duplicated with the UserIds of the current anchors or audience members in the room. If multiple moderation tasks are initiated in one room, the chatbot's UserId should also be unique; otherwise, the previous moderation task is interrupted. It is recommended to include the room ID as part of the UserId, ensuring that the chatbot's UserId is unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. For specific calculation methods, see TRTC solution for calculating UserSig.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def ModerationParams(self):
        r"""Control parameters for cloud moderation.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationParams`
        """
        return self._ModerationParams

    @ModerationParams.setter
    def ModerationParams(self, ModerationParams):
        self._ModerationParams = ModerationParams

    @property
    def ModerationStorageParams(self):
        r"""Parameters for uploading cloud moderation files to the cloud storage.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationStorageParams`
        """
        return self._ModerationStorageParams

    @ModerationStorageParams.setter
    def ModerationStorageParams(self, ModerationStorageParams):
        self._ModerationStorageParams = ModerationStorageParams

    @property
    def RoomIdType(self):
        r"""Type of the TRTC room number. [*Note] It should be the same as the type of the RoomId corresponding to the recording room. 0: string type; 1: 32-bit integer type (default value). Example value: 1.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def ResourceExpiredHour(self):
        r"""Validity period for calling the task ID, which starts upon successful initiation of the task and obtaining the task ID. After the timeout, APIs such as querying, updating, or stopping cannot be called, but the moderation task is not stopped. The unit of the parameter is hours, with a default value of 24 hours (1 day). The maximum value is 72 hours (3 days), while the minimum value is 6 hours. For example, if this parameter is not specified, the validity period for calling the querying, updating, and stopping slicing APIs is 24 hours upon the successful start of slicing.
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("ModerationParams") is not None:
            self._ModerationParams = ModerationParams()
            self._ModerationParams._deserialize(params.get("ModerationParams"))
        if params.get("ModerationStorageParams") is not None:
            self._ModerationStorageParams = ModerationStorageParams()
            self._ModerationStorageParams._deserialize(params.get("ModerationStorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudModerationResponse(AbstractModel):
    r"""CreateCloudModeration response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID assigned by the cloud moderation service. It is a unique identifier for the lifecycle of a moderation task, which loses its significance after the task is completed. The task ID needs to be retained by the business system as a parameter for future operations related to this task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID assigned by the cloud moderation service. It is a unique identifier for the lifecycle of a moderation task, which loses its significance after the task is completed. The task ID needs to be retained by the business system as a parameter for future operations related to this task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudRecordingRequest(AbstractModel):
    r"""CreateCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :type SdkAppId: int
        :param _RoomId: [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC, which is the RoomId corresponding to the TRTC room in the recording.
Note: the room id type defaults to integer. if the room id type is a string, specify it via RoomIdType.

        :type RoomId: str
        :param _UserId: The [user ID](https://www.tencentcloud.com/document/product/647/37714#userid) of the recording robot in the TRTC room, which cannot be identical to the user IDs of anchors in the room or other recording robots. To distinguish this user ID from others, we recommend you include the room ID in the user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to a login password) required for the recording robot to enter the room. Each user ID corresponds to a signature. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :type UserSig: str
        :param _RecordParams: The on-cloud recording parameters.
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param _StorageParams: The storage information of the recording file. Currently, you can save recording files to Tencent Cloud VOD or COS.
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param _RoomIdType: The type of the TRTC room ID, which must be the same as the ID type of the room whose streams are recorded.
0: String
1: 32-bit integer (default)
        :type RoomIdType: int
        :param _MixTranscodeParams: The stream mixing parameters, which are valid if the mixed-stream recording mode is used.
        :type MixTranscodeParams: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        :param _MixLayoutParams: The layout parameters, which are valid if the mixed-stream recording mode is used.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _ResourceExpiredHour: The amount of time (in hours) during which API requests can be made after recording starts. Calculation starts when a recording task is started (when the recording task ID is returned). Once the period elapses, the query, modification, and stop recording APIs can no longer be called, but the recording task will continue. The default value is `72` (three days), and the maximum and minimum values allowed are `720` (30 days) and `6` respectively. If you do not set this parameter, the query, modification, and stop recording APIs can be called within 72 hours after recording starts.
        :type ResourceExpiredHour: int
        :param _PrivateMapKey: The permission ticket for a TRTC room. This parameter is required if advanced permission control is enabled in the console, in which case the TRTC backend will verify users' [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1), which include an encrypted room ID and permission bit list. A user providing only `UserSig` and not `PrivateMapKey` will be unable to enter the room.
        :type PrivateMapKey: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._RecordParams = None
        self._StorageParams = None
        self._RoomIdType = None
        self._MixTranscodeParams = None
        self._MixLayoutParams = None
        self._ResourceExpiredHour = None
        self._PrivateMapKey = None

    @property
    def SdkAppId(self):
        r"""The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""[RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC, which is the RoomId corresponding to the TRTC room in the recording.
Note: the room id type defaults to integer. if the room id type is a string, specify it via RoomIdType.

        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""The [user ID](https://www.tencentcloud.com/document/product/647/37714#userid) of the recording robot in the TRTC room, which cannot be identical to the user IDs of anchors in the room or other recording robots. To distinguish this user ID from others, we recommend you include the room ID in the user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""The signature (similar to a login password) required for the recording robot to enter the room. Each user ID corresponds to a signature. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RecordParams(self):
        r"""The on-cloud recording parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        """
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams

    @property
    def StorageParams(self):
        r"""The storage information of the recording file. Currently, you can save recording files to Tencent Cloud VOD or COS.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        """
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def RoomIdType(self):
        r"""The type of the TRTC room ID, which must be the same as the ID type of the room whose streams are recorded.
0: String
1: 32-bit integer (default)
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def MixTranscodeParams(self):
        r"""The stream mixing parameters, which are valid if the mixed-stream recording mode is used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        """
        return self._MixTranscodeParams

    @MixTranscodeParams.setter
    def MixTranscodeParams(self, MixTranscodeParams):
        self._MixTranscodeParams = MixTranscodeParams

    @property
    def MixLayoutParams(self):
        r"""The layout parameters, which are valid if the mixed-stream recording mode is used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def ResourceExpiredHour(self):
        r"""The amount of time (in hours) during which API requests can be made after recording starts. Calculation starts when a recording task is started (when the recording task ID is returned). Once the period elapses, the query, modification, and stop recording APIs can no longer be called, but the recording task will continue. The default value is `72` (three days), and the maximum and minimum values allowed are `720` (30 days) and `6` respectively. If you do not set this parameter, the query, modification, and stop recording APIs can be called within 72 hours after recording starts.
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
        r"""The permission ticket for a TRTC room. This parameter is required if advanced permission control is enabled in the console, in which case the TRTC backend will verify users' [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1), which include an encrypted room ID and permission bit list. A user providing only `UserSig` and not `PrivateMapKey` will be unable to enter the room.
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("RecordParams") is not None:
            self._RecordParams = RecordParams()
            self._RecordParams._deserialize(params.get("RecordParams"))
        if params.get("StorageParams") is not None:
            self._StorageParams = StorageParams()
            self._StorageParams._deserialize(params.get("StorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        if params.get("MixTranscodeParams") is not None:
            self._MixTranscodeParams = MixTranscodeParams()
            self._MixTranscodeParams._deserialize(params.get("MixTranscodeParams"))
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        self._PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    r"""CreateCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends. After a recording task starts, if you want to perform other actions on the task, you need to specify the task ID when making API requests.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends. After a recording task starts, if you want to perform other actions on the task, you need to specify the task ID when making API requests.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudSliceTaskRequest(AbstractModel):
    r"""CreateCloudSliceTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) of TRTC, which is the same as the SdkAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _RoomId: [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) of TRTC, which is the RoomId corresponding to the TRTC room.
        :type RoomId: str
        :param _UserId: Chatbot's UserId, which is used to enter the room and initiate a slicing task. [*note] This UserId should not be duplicated with the UserIds of the current anchors or audience members in the room. If multiple slicing tasks are initiated in one room, the chatbot's UserId should also be unique; otherwise, the previous slicing task is interrupted. It is recommended to include the room ID as part of the UserId, ensuring that the chatbot's UserId is unique in the room.
        :type UserId: str
        :param _UserSig: Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. For specific calculation methods, see TRTC solution for calculating UserSig.
        :type UserSig: str
        :param _SliceParams: Control parameters for cloud slicing.
        :type SliceParams: :class:`tencentcloud.trtc.v20190722.models.SliceParams`
        :param _SliceStorageParams: Parameters for uploading cloud slicing files to the cloud storage.
        :type SliceStorageParams: :class:`tencentcloud.trtc.v20190722.models.SliceStorageParams`
        :param _RoomIdType: Type of the TRTC room number. [*Note] It should be the same as the type of the RoomId corresponding to the recording room. 0: string type; 1: 32-bit integer type (default value). Example value: 1.
        :type RoomIdType: int
        :param _ResourceExpiredHour: Validity period for calling the API, which starts upon successful initiation of recording and obtaining the task ID. After the timeout, APIs such as querying, updating, or stopping cannot be called, but the recording task is not stopped. The unit of the parameter is hours, with a default value of 72 hours (3 days). The maximum value is 720 hours (30 days), while the minimum value is 6 hours. For example, if this parameter is not specified, the validity period for calling the querying, updating, and stopping recording APIs is 72 hours upon the successful start of recording. Example value: 24.
        :type ResourceExpiredHour: int
        :param _PrivateMapKey: TRTC room permission encryption string, which is required only when advanced permission control is enabled in the TRTC console. After enabling, the TRTC backend service system verifies a "permission ticket" called [PrivateMapKey], which contains an encrypted RoomId and an encrypted "permission bit list". Since the PrivateMapKey includes the RoomId, the specified room cannot be entered if only UserSig is provided and PrivateMapKey is not provided. Example value: eJw1jcEKgkAURX9FZlvY****fL9rfNX4_.
        :type PrivateMapKey: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._SliceParams = None
        self._SliceStorageParams = None
        self._RoomIdType = None
        self._ResourceExpiredHour = None
        self._PrivateMapKey = None

    @property
    def SdkAppId(self):
        r"""[SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid) of TRTC, which is the same as the SdkAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""[RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid) of TRTC, which is the RoomId corresponding to the TRTC room.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""Chatbot's UserId, which is used to enter the room and initiate a slicing task. [*note] This UserId should not be duplicated with the UserIds of the current anchors or audience members in the room. If multiple slicing tasks are initiated in one room, the chatbot's UserId should also be unique; otherwise, the previous slicing task is interrupted. It is recommended to include the room ID as part of the UserId, ensuring that the chatbot's UserId is unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""Signature verification corresponding to the chatbot's UserId, namely, the UserId and UserSig serve as the login password for the chatbot to enter the room. For specific calculation methods, see TRTC solution for calculating UserSig.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def SliceParams(self):
        r"""Control parameters for cloud slicing.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SliceParams`
        """
        return self._SliceParams

    @SliceParams.setter
    def SliceParams(self, SliceParams):
        self._SliceParams = SliceParams

    @property
    def SliceStorageParams(self):
        r"""Parameters for uploading cloud slicing files to the cloud storage.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SliceStorageParams`
        """
        return self._SliceStorageParams

    @SliceStorageParams.setter
    def SliceStorageParams(self, SliceStorageParams):
        self._SliceStorageParams = SliceStorageParams

    @property
    def RoomIdType(self):
        r"""Type of the TRTC room number. [*Note] It should be the same as the type of the RoomId corresponding to the recording room. 0: string type; 1: 32-bit integer type (default value). Example value: 1.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def ResourceExpiredHour(self):
        r"""Validity period for calling the API, which starts upon successful initiation of recording and obtaining the task ID. After the timeout, APIs such as querying, updating, or stopping cannot be called, but the recording task is not stopped. The unit of the parameter is hours, with a default value of 72 hours (3 days). The maximum value is 720 hours (30 days), while the minimum value is 6 hours. For example, if this parameter is not specified, the validity period for calling the querying, updating, and stopping recording APIs is 72 hours upon the successful start of recording. Example value: 24.
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
        r"""TRTC room permission encryption string, which is required only when advanced permission control is enabled in the TRTC console. After enabling, the TRTC backend service system verifies a "permission ticket" called [PrivateMapKey], which contains an encrypted RoomId and an encrypted "permission bit list". Since the PrivateMapKey includes the RoomId, the specified room cannot be entered if only UserSig is provided and PrivateMapKey is not provided. Example value: eJw1jcEKgkAURX9FZlvY****fL9rfNX4_.
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("SliceParams") is not None:
            self._SliceParams = SliceParams()
            self._SliceParams._deserialize(params.get("SliceParams"))
        if params.get("SliceStorageParams") is not None:
            self._SliceStorageParams = SliceStorageParams()
            self._SliceStorageParams._deserialize(params.get("SliceStorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        self._PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudSliceTaskResponse(AbstractModel):
    r"""CreateCloudSliceTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID assigned by the cloud slicing service. It is a unique identifier for the lifecycle of a slicing task, which loses its significance after the task is completed. The task ID needs to be retained by the business system as a parameter for future operations related to this task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID assigned by the cloud slicing service. It is a unique identifier for the lifecycle of a slicing task, which loses its significance after the task is completed. The task ID needs to be retained by the business system as a parameter for future operations related to this task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudTranscriptionRequest(AbstractModel):
    r"""CreateCloudTranscription request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: <p>The <a href="https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid">SdkAppId</a> of TRTC is the same as the SdkAppId corresponding to the transcribe room.</p>
        :type SdkAppId: int
        :param _RoomId: <p>The <a href="https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid">RoomId</a> of TRTC, which is the RoomId corresponding to the transcribed TRTC room. Note: The room ID type defaults to integer. If the room ID type is string, specify it through RoomIdType.</p>
        :type RoomId: str
        :param _RoomIdType: <p>The room information RoomType must be identical to the data type of the RoomId corresponding to the transcribed room. 0 indicates an integer room number, and 1 indicates a string Room Number.</p>
        :type RoomIdType: int
        :param _TranscriptionParam: <p>Parameters for the transcribe service to join TRTC room.</p>
        :type TranscriptionParam: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParam`
        :param _AsrParam: <p>Parameters used by the ASR transcribe service.</p>
        :type AsrParam: :class:`tencentcloud.trtc.v20190722.models.AsrParam`
        :param _TranslationParam: <p>Parameters used to transcribe the translation service.</p>
        :type TranslationParam: :class:`tencentcloud.trtc.v20190722.models.TranslationParam`
        :param _TTSParam: <p>Parameters used by the TTS transcribe service.</p>
        :type TTSParam: list of TTSParam
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._TranscriptionParam = None
        self._AsrParam = None
        self._TranslationParam = None
        self._TTSParam = None

    @property
    def SdkAppId(self):
        r"""<p>The <a href="https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#sdkappid">SdkAppId</a> of TRTC is the same as the SdkAppId corresponding to the transcribe room.</p>
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""<p>The <a href="https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#roomid">RoomId</a> of TRTC, which is the RoomId corresponding to the transcribed TRTC room. Note: The room ID type defaults to integer. If the room ID type is string, specify it through RoomIdType.</p>
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""<p>The room information RoomType must be identical to the data type of the RoomId corresponding to the transcribed room. 0 indicates an integer room number, and 1 indicates a string Room Number.</p>
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def TranscriptionParam(self):
        r"""<p>Parameters for the transcribe service to join TRTC room.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParam`
        """
        return self._TranscriptionParam

    @TranscriptionParam.setter
    def TranscriptionParam(self, TranscriptionParam):
        self._TranscriptionParam = TranscriptionParam

    @property
    def AsrParam(self):
        r"""<p>Parameters used by the ASR transcribe service.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AsrParam`
        """
        return self._AsrParam

    @AsrParam.setter
    def AsrParam(self, AsrParam):
        self._AsrParam = AsrParam

    @property
    def TranslationParam(self):
        r"""<p>Parameters used to transcribe the translation service.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranslationParam`
        """
        return self._TranslationParam

    @TranslationParam.setter
    def TranslationParam(self, TranslationParam):
        self._TranslationParam = TranslationParam

    @property
    def TTSParam(self):
        r"""<p>Parameters used by the TTS transcribe service.</p>
        :rtype: list of TTSParam
        """
        return self._TTSParam

    @TTSParam.setter
    def TTSParam(self, TTSParam):
        self._TTSParam = TTSParam


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("TranscriptionParam") is not None:
            self._TranscriptionParam = TranscriptionParam()
            self._TranscriptionParam._deserialize(params.get("TranscriptionParam"))
        if params.get("AsrParam") is not None:
            self._AsrParam = AsrParam()
            self._AsrParam._deserialize(params.get("AsrParam"))
        if params.get("TranslationParam") is not None:
            self._TranslationParam = TranslationParam()
            self._TranslationParam._deserialize(params.get("TranslationParam"))
        if params.get("TTSParam") is not None:
            self._TTSParam = []
            for item in params.get("TTSParam"):
                obj = TTSParam()
                obj._deserialize(item)
                self._TTSParam.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudTranscriptionResponse(AbstractModel):
    r"""CreateCloudTranscription response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>A unique identifier for the transcription task, generated by the Tencent Cloud server. The TaskID parameter is required for all subsequent query and stop requests.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>A unique identifier for the transcription task, generated by the Tencent Cloud server. The TaskID parameter is required for all subsequent query and stop requests.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudModerationRequest(AbstractModel):
    r"""DeleteCloudModeration request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the moderation task, which is returned after the task is started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudModerationResponse(AbstractModel):
    r"""DeleteCloudModeration response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the moderation task, which is returned after the task is started.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    r"""DeleteCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    r"""DeleteCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudSliceTaskRequest(AbstractModel):
    r"""DeleteCloudSliceTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudSliceTaskResponse(AbstractModel):
    r"""DeleteCloudSliceTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudTranscriptionRequest(AbstractModel):
    r"""DeleteCloudTranscription request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId of the room being transcribed.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the task will be returned upon success.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId of the room being transcribed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique Id of the task will be returned upon success.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudTranscriptionResponse(AbstractModel):
    r"""DeleteCloudTranscription response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID of the service allocation for transcribing. The task ID is the unique identifier for a transcription lifecycle process and loses its meaning once the transcription is complete.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID of the service allocation for transcribing. The task ID is the unique identifier for a transcription lifecycle process and loses its meaning once the transcription is complete.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAIConversationRequest(AbstractModel):
    r"""DescribeAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the task.
        :type TaskId: str
        :param _SessionId: The SessionId filled in when starting the task. 
        :type SessionId: str
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        r"""TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique ID of the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""The SessionId filled in when starting the task. 
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIConversationResponse(AbstractModel):
    r"""DescribeAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The time when the task starts.
        :type StartTime: str
        :param _Status: Task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :type Status: str
        :param _TaskId: The unique ID of the task, generated when the task is started
        :type TaskId: str
        :param _SessionId: The SessionId filled in when opening the conversation task.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""The time when the task starts.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""Task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""The unique ID of the task, generated when the task is started
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""The SessionId filled in when opening the conversation task.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeAITranscriptionRequest(AbstractModel):
    r"""DescribeAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Query the task status. If not in use, pass in an empty string. There are two query methods: 1. Fill in only TaskId. This method uses TaskId to query tasks. 2. TaskId is an empty string. Fill in SdkAppId and SessionId. This method does not require TaskId to query tasks.
        :type TaskId: str
        :param _SdkAppId: TRTC's SdkAppId is used together with SessionId.
        :type SdkAppId: int
        :param _SessionId: The SessionId passed in when starting the transcription task is used together with the SdkAppId.
        :type SessionId: str
        """
        self._TaskId = None
        self._SdkAppId = None
        self._SessionId = None

    @property
    def TaskId(self):
        r"""Query the task status. If not in use, pass in an empty string. There are two query methods: 1. Fill in only TaskId. This method uses TaskId to query tasks. 2. TaskId is an empty string. Fill in SdkAppId and SessionId. This method does not require TaskId to query tasks.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SdkAppId(self):
        r"""TRTC's SdkAppId is used together with SessionId.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        r"""The SessionId passed in when starting the transcription task is used together with the SdkAppId.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITranscriptionResponse(AbstractModel):
    r"""DescribeAITranscription response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The time when the task starts.
        :type StartTime: str
        :param _Status: Transcription task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :type Status: str
        :param _TaskId: Uniquely identifies a task.
        :type TaskId: str
        :param _SessionId: The SessionId filled in when starting the transcription task. If not filled in, nothing is returned.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""The time when the task starts.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""Transcription task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Uniquely identifies a task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""The SessionId filled in when starting the transcription task. If not filled in, nothing is returned.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeCallDetailInfoRequest(AbstractModel):
    r"""DescribeCallDetailInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If `DataType` is not null, the end time and start time cannot be more than one hour apart; if `DataType` is null, the end time and start time cannot be more than four hours apart.
        :type EndTime: int
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _UserIds: The users to query. If you do not specify this, the data of six users will be returned.
        :type UserIds: list of str
        :param _DataType: The metrics to query. If you do not specify this, only the user list will be returned. If you pass in `all`, all metrics will be returned.
`appCpu`: The CPU utilization of the application.
`sysCpu`: The CPU utilization of the system.
`aBit`: The upstream/downstream audio bitrate (bps).
`aBlock`: The audio stutter duration (ms).
`bigvBit`: The upstream/downstream video bitrate (bps).
`bigvCapFps`: The frame rate for capturing videos.
`bigvEncFps`: The frame rate for sending videos.
`bigvDecFps`: The rendering frame rate.
`bigvBlock`: The video stutter duration (ms).
`aLoss`: The upstream/downstream audio packet loss.
`bigvLoss`: The upstream/downstream video packet loss.
`bigvWidth`: The upstream/downstream resolution (width).
`bigvHeight`: The upstream/downstream resolution (height).
        :type DataType: list of str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `6`.
Value range: 1-100.
Note: If `DataType` is not null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `6`.
If `DataType` is null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `100`.
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._DataType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        r"""The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If `DataType` is not null, the end time and start time cannot be more than one hour apart; if `DataType` is null, the end time and start time cannot be more than four hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        r"""The users to query. If you do not specify this, the data of six users will be returned.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def DataType(self):
        r"""The metrics to query. If you do not specify this, only the user list will be returned. If you pass in `all`, all metrics will be returned.
`appCpu`: The CPU utilization of the application.
`sysCpu`: The CPU utilization of the system.
`aBit`: The upstream/downstream audio bitrate (bps).
`aBlock`: The audio stutter duration (ms).
`bigvBit`: The upstream/downstream video bitrate (bps).
`bigvCapFps`: The frame rate for capturing videos.
`bigvEncFps`: The frame rate for sending videos.
`bigvDecFps`: The rendering frame rate.
`bigvBlock`: The video stutter duration (ms).
`aLoss`: The upstream/downstream audio packet loss.
`bigvLoss`: The upstream/downstream video packet loss.
`bigvWidth`: The upstream/downstream resolution (width).
`bigvHeight`: The upstream/downstream resolution (height).
        :rtype: list of str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PageNumber(self):
        r"""The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""The number of records per page. The default is `6`.
Value range: 1-100.
Note: If `DataType` is not null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `6`.
If `DataType` is null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `100`.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._DataType = params.get("DataType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallDetailInfoResponse(AbstractModel):
    r"""DescribeCallDetailInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _UserList: The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param _Data: The call quality data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of QualityData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        r"""The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Data(self):
        r"""The call quality data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of QualityData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudModerationRequest(AbstractModel):
    r"""DescribeCloudModeration request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the recording room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the cloud moderation task, which is returned after the task is started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the recording room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the cloud moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudModerationResponse(AbstractModel):
    r"""DescribeCloudModeration response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the moderation task, which is returned after the task is started.
        :type TaskId: str
        :param _Status: Information about the status of the cloud moderation task. Idle: indicates the current task is idle; InProgress: indicates the current task is in progress; Exited: indicates the current task is being exited.
        :type Status: str
        :param _SubscribeStreamUserIds: Subscription blocklist and allowlist.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._SubscribeStreamUserIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""Information about the status of the cloud moderation task. Idle: indicates the current task is idle; InProgress: indicates the current task is in progress; Exited: indicates the current task is being exited.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubscribeStreamUserIds(self):
        r"""Subscription blocklist and allowlist.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeModerationUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._RequestId = params.get("RequestId")


class DescribeCloudRecordingRequest(AbstractModel):
    r"""DescribeCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRecordingResponse(AbstractModel):
    r"""DescribeCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The unique ID of the recording task.
        :type TaskId: str
        :param _Status: The status of the on-cloud recording task.
Idle: The task is idle.
InProgress: The task is in progress.
Exited: The task is being ended.
        :type Status: str
        :param _StorageFileList: The information of the recording files.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StorageFileList: list of StorageFile
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._StorageFileList = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The unique ID of the recording task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""The status of the on-cloud recording task.
Idle: The task is idle.
InProgress: The task is in progress.
Exited: The task is being ended.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StorageFileList(self):
        r"""The information of the recording files.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of StorageFile
        """
        return self._StorageFileList

    @StorageFileList.setter
    def StorageFileList(self, StorageFileList):
        self._StorageFileList = StorageFileList

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("StorageFileList") is not None:
            self._StorageFileList = []
            for item in params.get("StorageFileList"):
                obj = StorageFile()
                obj._deserialize(item)
                self._StorageFileList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudSliceTaskRequest(AbstractModel):
    r"""DescribeCloudSliceTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the recording room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the recording room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudSliceTaskResponse(AbstractModel):
    r"""DescribeCloudSliceTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        :param _Status: Information about the status of the cloud slicing task. Idle: indicates the current task is idle; InProgress: indicates the current task is in progress; Exited: indicates the current task is being exited.
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""Information about the status of the cloud slicing task. Idle: indicates the current task is idle; InProgress: indicates the current task is in progress; Exited: indicates the current task is being exited.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeCloudTranscriptionRequest(AbstractModel):
    r"""DescribeCloudTranscription request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId of the room being transcribed.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the transcription task will be returned upon successful startup.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId of the room being transcribed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique Id of the transcription task will be returned upon successful startup.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudTranscriptionResponse(AbstractModel):
    r"""DescribeCloudTranscription response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Time of starting the transcription task.
        :type StartTime: int
        :param _Status: Transcription task status. 

- Idle: Indicates the current transcription task is idle. 
- InProgress: Indicates the current transcription task is in progress. 
- Exited: Indicates the current transcription task is in the process of exiting.
        :type Status: str
        :param _TaskId: Unique Id of the transcribe task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""Time of starting the transcription task.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""Transcription task status. 

- Idle: Indicates the current transcription task is idle. 
- InProgress: Indicates the current transcription task is in progress. 
- Exited: Indicates the current transcription task is in the process of exiting.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Unique Id of the transcribe task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeMixTranscodingUsageRequest(AbstractModel):
    r"""DescribeMixTranscodingUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMixTranscodingUsageResponse(AbstractModel):
    r"""DescribeMixTranscodingUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordingUsageRequest(AbstractModel):
    r"""DescribeRecordingUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _MixType: Whether to query single-stream or mixed-stream recording. Valid values: `single`, `multi`.
        :type MixType: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._MixType = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MixType(self):
        r"""Whether to query single-stream or mixed-stream recording. Valid values: `single`, `multi`.
        :rtype: str
        """
        return self._MixType

    @MixType.setter
    def MixType(self, MixType):
        self._MixType = MixType

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MixType = params.get("MixType")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingUsageResponse(AbstractModel):
    r"""DescribeRecordingUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRelayUsageRequest(AbstractModel):
    r"""DescribeRelayUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelayUsageResponse(AbstractModel):
    r"""DescribeRelayUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    r"""DescribeRoomInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than 24 hours apart.
        :type EndTime: int
        :param _RoomId: The room ID, such as `223`.
        :type RoomId: str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, 10 records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `10`.
Value range: 1-100.
        :type PageSize: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        r"""The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than 24 hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""The room ID, such as `223`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PageNumber(self):
        r"""The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, 10 records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""The number of records per page. The default is `10`.
Value range: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    r"""DescribeRoomInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _RoomList: The room information.
        :type RoomList: list of RoomState
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._RoomList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RoomList(self):
        r"""The room information.
        :rtype: list of RoomState
        """
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

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
        self._Total = params.get("Total")
        if params.get("RoomList") is not None:
            self._RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self._RoomList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScaleInfoRequest(AbstractModel):
    r"""DescribeScaleInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time should preferably be more than 24 hours apart.
Note: Data is collected on a daily basis. To query the data of a day, make sure the end time is later than 00:00 on that day. Otherwise, no data will be returned. For example, to query the data on the 20th, the end time must be later than 00:00 on the 20th.
        :type EndTime: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        r"""The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time should preferably be more than 24 hours apart.
Note: Data is collected on a daily basis. To query the data of a day, make sure the end time is later than 00:00 on that day. Otherwise, no data will be returned. For example, to query the data on the 20th, the end time must be later than 00:00 on the 20th.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScaleInfoResponse(AbstractModel):
    r"""DescribeScaleInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _ScaleList: The returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScaleList: list of ScaleInfomation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ScaleList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ScaleList(self):
        r"""The returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ScaleInfomation
        """
        return self._ScaleList

    @ScaleList.setter
    def ScaleList(self, ScaleList):
        self._ScaleList = ScaleList

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
        self._Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self._ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self._ScaleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamIngestRequest(AbstractModel):
    r"""DescribeStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the task, will return after successfully starting the task.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique Id of the task, will return after successfully starting the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamIngestResponse(AbstractModel):
    r"""DescribeStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketQualityDataRequest(AbstractModel):
    r"""DescribeTRTCMarketQualityData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SdkAppId (for example: 1400xxxxxx).
        :type SdkAppId: str
        :param _StartTime: Query start time, and the format is YYYY-MM-DD. (query time range is based on the monitoring dashboard feature version. the basic version supports querying the last 30 days, and the advanced version supports querying the last 60 days).
        :type StartTime: str
        :param _EndTime: Query end time in YYYY-MM-DD format.
        :type EndTime: str
        :param _Period: The granularity of returned data supports the following values:.
d: day. at this time, return the data of UTC time at zero point within a specified time range.
h: billed hourly. at this point, return the data of full hour UTC time within a specified time range.
        :type Period: str
        :param _IsFloat: Whether the returned data is a decimal.
        :type IsFloat: bool
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._IsFloat = None

    @property
    def SdkAppId(self):
        r"""User SdkAppId (for example: 1400xxxxxx).
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""Query start time, and the format is YYYY-MM-DD. (query time range is based on the monitoring dashboard feature version. the basic version supports querying the last 30 days, and the advanced version supports querying the last 60 days).
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time in YYYY-MM-DD format.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""The granularity of returned data supports the following values:.
d: day. at this time, return the data of UTC time at zero point within a specified time range.
h: billed hourly. at this point, return the data of full hour UTC time within a specified time range.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def IsFloat(self):
        r"""Whether the returned data is a decimal.
        :rtype: bool
        """
        return self._IsFloat

    @IsFloat.setter
    def IsFloat(self, IsFloat):
        self._IsFloat = IsFloat


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._IsFloat = params.get("IsFloat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketQualityDataResponse(AbstractModel):
    r"""DescribeTRTCMarketQualityData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC monitoring data output parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC monitoring data output parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketScaleDataRequest(AbstractModel):
    r"""DescribeTRTCMarketScaleData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId
        :type SdkAppId: str
        :param _StartTime: Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 60 days)
        :type StartTime: str
        :param _EndTime: Query end time, format is YYYY-MM-DD.
        :type EndTime: str
        :param _Period: The granularity of the returned data, which can be set to the following values:
 d: by day. This returns data for the entire UTC day of the query time range.
 h: by hour. This returns data for the entire UTC hour of the query time range.
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        r"""User SDKAppId
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 60 days)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time, format is YYYY-MM-DD.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""The granularity of the returned data, which can be set to the following values:
 d: by day. This returns data for the entire UTC day of the query time range.
 h: by hour. This returns data for the entire UTC hour of the query time range.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketScaleDataResponse(AbstractModel):
    r"""DescribeTRTCMarketScaleData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Data Dashboard output parameters
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC Data Dashboard output parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeQualityDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeQualityData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId (e.g., 1400xxxxxx)
        :type SdkAppId: str
        :param _StartTime: Start time, unix timestamp, Unit: seconds (Query time range depends on the monitoring dashboard function version, standard edition can query the last 3 hours, premium edition can query the last 12 hours)
        :type StartTime: int
        :param _EndTime: End time, unix timestamp, Unit: seconds
        :type EndTime: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""User SDKAppId (e.g., 1400xxxxxx)
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""Start time, unix timestamp, Unit: seconds (Query time range depends on the monitoring dashboard function version, standard edition can query the last 3 hours, premium edition can query the last 12 hours)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time, unix timestamp, Unit: seconds
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeQualityDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeQualityData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Real- Time Monitoring output parameters
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC Real- Time Monitoring output parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeScaleDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeScaleData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId (e.g., 1400xxxxxx)
        :type SdkAppId: str
        :param _StartTime: Start time, unix timestamp, Unit: seconds (Query time range depends on the function version of the monitoring dashboard, premium edition can query up to 1 hours)
        :type StartTime: int
        :param _EndTime: End time, unix timestamp, Unit: seconds
        :type EndTime: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""User SDKAppId (e.g., 1400xxxxxx)
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""Start time, unix timestamp, Unit: seconds (Query time range depends on the function version of the monitoring dashboard, premium edition can query up to 1 hours)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time, unix timestamp, Unit: seconds
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeScaleDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeScaleData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Real- Time Monitoring
 output parameter
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC Real- Time Monitoring
 output parameter
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTrtcRoomUsageRequest(AbstractModel):
    r"""DescribeTrtcRoomUsage request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppid: The `SDKAppID` of the room.
        :type SdkAppid: int
        :param _StartTime: The start time in the format of `YYYY-MM-DD HH:MM` (accurate to the minute).
        :type StartTime: str
        :param _EndTime: The end time in the format of `YYYY-MM-DD HH:MM`. The start and end time cannot be more than 24 hours apart.
        :type EndTime: str
        """
        self._SdkAppid = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppid(self):
        r"""The `SDKAppID` of the room.
        :rtype: int
        """
        return self._SdkAppid

    @SdkAppid.setter
    def SdkAppid(self, SdkAppid):
        self._SdkAppid = SdkAppid

    @property
    def StartTime(self):
        r"""The start time in the format of `YYYY-MM-DD HH:MM` (accurate to the minute).
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time in the format of `YYYY-MM-DD HH:MM`. The start and end time cannot be more than 24 hours apart.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppid = params.get("SdkAppid")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcRoomUsageResponse(AbstractModel):
    r"""DescribeTrtcRoomUsage response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The usage data grouped by room, in CSV format.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""The usage data grouped by room, in CSV format.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._RequestId = params.get("RequestId")


class DescribeTrtcUsageRequest(AbstractModel):
    r"""DescribeTrtcUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcUsageResponse(AbstractModel):
    r"""DescribeTrtcUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUnusualEventRequest(AbstractModel):
    r"""DescribeUnusualEvent request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SdkAppId (for example: 1400xxxxxx).
        :type SdkAppId: int
        :param _StartTime: Query start time, local unix timestamp, in seconds (for example: 1590065777).
Note: support querying data within the last 14 days.
        :type StartTime: int
        :param _EndTime: Query end time, local unix timestamp, in seconds (for example, 1590065877). note: the time interval from StartTime should be no more than 1 hour.
        :type EndTime: int
        :param _RoomId: Room number. query up to 20 abnormal experience events in the room.
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""User SdkAppId (for example: 1400xxxxxx).
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""Query start time, local unix timestamp, in seconds (for example: 1590065777).
Note: support querying data within the last 14 days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time, local unix timestamp, in seconds (for example, 1590065877). note: the time interval from StartTime should be no more than 1 hour.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""Room number. query up to 20 abnormal experience events in the room.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnusualEventResponse(AbstractModel):
    r"""DescribeUnusualEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of returned data entries.
Value range: [0, 20].
        :type Total: int
        :param _AbnormalExperienceList: Abnormal experience list.
        :type AbnormalExperienceList: list of AbnormalExperience
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._AbnormalExperienceList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total number of returned data entries.
Value range: [0, 20].
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AbnormalExperienceList(self):
        r"""Abnormal experience list.
        :rtype: list of AbnormalExperience
        """
        return self._AbnormalExperienceList

    @AbnormalExperienceList.setter
    def AbnormalExperienceList(self, AbnormalExperienceList):
        self._AbnormalExperienceList = AbnormalExperienceList

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
        self._Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self._AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self._AbnormalExperienceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserEventRequest(AbstractModel):
    r"""DescribeUserEvent request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If you pass in an end time later than the room end time, the room end time will be used.
        :type EndTime: int
        :param _UserId: The user ID.
        :type UserId: str
        :param _RoomId: The room ID, such as `223`.
        :type RoomId: str
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None
        self._RoomId = None
        self._SdkAppId = None

    @property
    def CommId(self):
        r"""The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If you pass in an end time later than the room end time, the room end time will be used.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        r"""The room ID, such as `223`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserEventResponse(AbstractModel):
    r"""DescribeUserEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The event list. An empty array will be returned if no data is obtained.
        :type Data: list of EventList
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""The event list. An empty array will be returned if no data is obtained.
        :rtype: list of EventList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    r"""DescribeUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than four hours apart.
        :type EndTime: int
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _UserIds: The users to query. If you do not specify this, the information of six users will be returned.
Array length: 1-100.
        :type UserIds: list of str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `6`.
Array length: 1-100.
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        r"""The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than four hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        r"""The users to query. If you do not specify this, the information of six users will be returned.
Array length: 1-100.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def PageNumber(self):
        r"""The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""The number of records per page. The default is `6`.
Array length: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    r"""DescribeUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _UserList: The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        r"""The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

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
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWebRecordRequest(AbstractModel):
    r"""DescribeWebRecord request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID returned when starting web-page recording
        :type TaskId: str
        :param _SdkAppId: SdkAppId passed when initiating web-page recording
        :type SdkAppId: int
        :param _RecordId: RecordId passed when initiating recording. When passing this value, you need to pass SdkAppId
        :type RecordId: str
        """
        self._TaskId = None
        self._SdkAppId = None
        self._RecordId = None

    @property
    def TaskId(self):
        r"""The task ID returned when starting web-page recording
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SdkAppId(self):
        r"""SdkAppId passed when initiating web-page recording
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RecordId(self):
        r"""RecordId passed when initiating recording. When passing this value, you need to pass SdkAppId
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SdkAppId = params.get("SdkAppId")
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebRecordResponse(AbstractModel):
    r"""DescribeWebRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 1: Recording
        :type Status: int
        :param _TaskId: Returns when querying using RecordId
        :type TaskId: str
        :param _RecordId: Returned when querying using TaskId
        :type RecordId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RecordId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""1: Recording
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""Returns when querying using RecordId
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordId(self):
        r"""Returned when querying using TaskId
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

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
        self._TaskId = params.get("TaskId")
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    r"""DismissRoomByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""`SDKAppId` of TRTC
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    r"""DismissRoomByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    r"""DismissRoom request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param _RoomId: Room number.
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""`SDKAppId` of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""Room number.
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    r"""DismissRoom response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class EmulateMobileParams(AbstractModel):
    r"""Render the mobile mode parameter. do not set this parameter when not rendering mobile mode.

    """

    def __init__(self):
        r"""
        :param _MobileDeviceType: Mobile device type.
Mobile phone.
Tablet.
        :type MobileDeviceType: int
        :param _ScreenOrientation: Screen orientation.
Portrait mode.
Landscape mode.
        :type ScreenOrientation: int
        """
        self._MobileDeviceType = None
        self._ScreenOrientation = None

    @property
    def MobileDeviceType(self):
        r"""Mobile device type.
Mobile phone.
Tablet.
        :rtype: int
        """
        return self._MobileDeviceType

    @MobileDeviceType.setter
    def MobileDeviceType(self, MobileDeviceType):
        self._MobileDeviceType = MobileDeviceType

    @property
    def ScreenOrientation(self):
        r"""Screen orientation.
Portrait mode.
Landscape mode.
        :rtype: int
        """
        return self._ScreenOrientation

    @ScreenOrientation.setter
    def ScreenOrientation(self, ScreenOrientation):
        self._ScreenOrientation = ScreenOrientation


    def _deserialize(self, params):
        self._MobileDeviceType = params.get("MobileDeviceType")
        self._ScreenOrientation = params.get("ScreenOrientation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventList(AbstractModel):
    r"""A list of SDK or WebRTC events.

    """

    def __init__(self):
        r"""
        :param _Content: The event information.
        :type Content: list of EventMessage
        :param _PeerId: The user ID of the sender.
        :type PeerId: str
        """
        self._Content = None
        self._PeerId = None

    @property
    def Content(self):
        r"""The event information.
        :rtype: list of EventMessage
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PeerId(self):
        r"""The user ID of the sender.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self._Content.append(obj)
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventMessage(AbstractModel):
    r"""The event information, including the timestamp and event ID.

    """

    def __init__(self):
        r"""
        :param _Type: The video stream type. Valid values:
`0`: A non-video event
`2`: The big video
`3`: The small video
`7`: A relayed video
        :type Type: int
        :param _Time: The event reporting time in the format of UNIX timestamp (milliseconds), such as `1589891188801`.
        :type Time: int
        :param _EventId: The event ID. Events are classified into SDK events and WebRTC events. For more information, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :type EventId: int
        :param _ParamOne: The first event parameter, such as the video width.
        :type ParamOne: int
        :param _ParamTwo: The second event parameter, such as the video height.
        :type ParamTwo: int
        """
        self._Type = None
        self._Time = None
        self._EventId = None
        self._ParamOne = None
        self._ParamTwo = None

    @property
    def Type(self):
        r"""The video stream type. Valid values:
`0`: A non-video event
`2`: The big video
`3`: The small video
`7`: A relayed video
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        r"""The event reporting time in the format of UNIX timestamp (milliseconds), such as `1589891188801`.
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventId(self):
        r"""The event ID. Events are classified into SDK events and WebRTC events. For more information, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def ParamOne(self):
        r"""The first event parameter, such as the video width.
        :rtype: int
        """
        return self._ParamOne

    @ParamOne.setter
    def ParamOne(self, ParamOne):
        self._ParamOne = ParamOne

    @property
    def ParamTwo(self):
        r"""The second event parameter, such as the video height.
        :rtype: int
        """
        return self._ParamTwo

    @ParamTwo.setter
    def ParamTwo(self, ParamTwo):
        self._ParamTwo = ParamTwo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._EventId = params.get("EventId")
        self._ParamOne = params.get("ParamOne")
        self._ParamTwo = params.get("ParamTwo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeLLM(AbstractModel):
    r"""Service calling actively initiates requests to the LLM.

    """

    def __init__(self):
        r"""
        :param _Content: Request the content of LLM.
        :type Content: str
        :param _Interrupt: Whether to allow the text to interrupt the robot's speaking.
        :type Interrupt: bool
        """
        self._Content = None
        self._Interrupt = None

    @property
    def Content(self):
        r"""Request the content of LLM.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Interrupt(self):
        r"""Whether to allow the text to interrupt the robot's speaking.
        :rtype: bool
        """
        return self._Interrupt

    @Interrupt.setter
    def Interrupt(self, Interrupt):
        self._Interrupt = Interrupt


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Interrupt = params.get("Interrupt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxVideoUser(AbstractModel):
    r"""The information of the large video in screen sharing or floating layout mode.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        r"""The stream information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuAudioParams(AbstractModel):
    r"""The audio parameters for relaying.

    """

    def __init__(self):
        r"""
        :param _AudioEncode: The audio encoding parameters.
        :type AudioEncode: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        :param _SubscribeAudioList: The audio user allowlist. for start, being empty or not filled means mixing all anchor audio; filling a specific value means mixing specified anchor audio. for update, not filling means does not update; being empty means update to mixing all anchor audio; filling a specific value means update to mixing specified anchor audio.
When using blocklist and allowlist, both must be filled in simultaneously. if left empty, it means the list does not update. if the same user is in both lists, the blocklist takes precedence.
Note: if it is cross-room pk, the cross-room mix requires specifying the audio allowlist, otherwise the pk host's audio uplink will be pulled twice, causing accent.
        :type SubscribeAudioList: list of McuUserInfoParams
        :param _UnSubscribeAudioList: The audio mix blocklist. If you do not pass this parameter or leave it empty, there won’t be a blocklist. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current blocklist; if you pass in an empty string, the blocklist will be reset.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :type UnSubscribeAudioList: list of McuUserInfoParams
        """
        self._AudioEncode = None
        self._SubscribeAudioList = None
        self._UnSubscribeAudioList = None

    @property
    def AudioEncode(self):
        r"""The audio encoding parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        """
        return self._AudioEncode

    @AudioEncode.setter
    def AudioEncode(self, AudioEncode):
        self._AudioEncode = AudioEncode

    @property
    def SubscribeAudioList(self):
        r"""The audio user allowlist. for start, being empty or not filled means mixing all anchor audio; filling a specific value means mixing specified anchor audio. for update, not filling means does not update; being empty means update to mixing all anchor audio; filling a specific value means update to mixing specified anchor audio.
When using blocklist and allowlist, both must be filled in simultaneously. if left empty, it means the list does not update. if the same user is in both lists, the blocklist takes precedence.
Note: if it is cross-room pk, the cross-room mix requires specifying the audio allowlist, otherwise the pk host's audio uplink will be pulled twice, causing accent.
        :rtype: list of McuUserInfoParams
        """
        return self._SubscribeAudioList

    @SubscribeAudioList.setter
    def SubscribeAudioList(self, SubscribeAudioList):
        self._SubscribeAudioList = SubscribeAudioList

    @property
    def UnSubscribeAudioList(self):
        r"""The audio mix blocklist. If you do not pass this parameter or leave it empty, there won’t be a blocklist. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current blocklist; if you pass in an empty string, the blocklist will be reset.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :rtype: list of McuUserInfoParams
        """
        return self._UnSubscribeAudioList

    @UnSubscribeAudioList.setter
    def UnSubscribeAudioList(self, UnSubscribeAudioList):
        self._UnSubscribeAudioList = UnSubscribeAudioList


    def _deserialize(self, params):
        if params.get("AudioEncode") is not None:
            self._AudioEncode = AudioEncode()
            self._AudioEncode._deserialize(params.get("AudioEncode"))
        if params.get("SubscribeAudioList") is not None:
            self._SubscribeAudioList = []
            for item in params.get("SubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._SubscribeAudioList.append(obj)
        if params.get("UnSubscribeAudioList") is not None:
            self._UnSubscribeAudioList = []
            for item in params.get("UnSubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._UnSubscribeAudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuBackgroundCustomRender(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Width: 
        :type Width: int
        :param _Height: 
        :type Height: int
        :param _Radius: 
        :type Radius: int
        """
        self._Width = None
        self._Height = None
        self._Radius = None

    @property
    def Width(self):
        r"""
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Radius(self):
        r"""
        :rtype: int
        """
        return self._Radius

    @Radius.setter
    def Radius(self, Radius):
        self._Radius = Radius


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Radius = params.get("Radius")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCloudVod(AbstractModel):
    r"""Mcu relay recording. on-demand video related parameters.

    """

    def __init__(self):
        r"""
        :param _McuTencentVod: Parameters of tencent cloud video on demand (vod).	
        :type McuTencentVod: :class:`tencentcloud.trtc.v20190722.models.McuTencentVod`
        """
        self._McuTencentVod = None

    @property
    def McuTencentVod(self):
        r"""Parameters of tencent cloud video on demand (vod).	
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuTencentVod`
        """
        return self._McuTencentVod

    @McuTencentVod.setter
    def McuTencentVod(self, McuTencentVod):
        self._McuTencentVod = McuTencentVod


    def _deserialize(self, params):
        if params.get("McuTencentVod") is not None:
            self._McuTencentVod = McuTencentVod()
            self._McuTencentVod._deserialize(params.get("McuTencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCustomCrop(AbstractModel):
    r"""The cropping parameters for mixed videos.

    """

    def __init__(self):
        r"""
        :param _LocationX: The horizontal offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationY: int
        :param _Width: The video width (pixels) after cropping. The sum of this parameter and `LocationX` cannot be greater than 10000.
        :type Width: int
        :param _Height: The video height (pixels) after cropping. The sum of this parameter and `LocationY` cannot be greater than 10000.
        :type Height: int
        """
        self._LocationX = None
        self._LocationY = None
        self._Width = None
        self._Height = None

    @property
    def LocationX(self):
        r"""The horizontal offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""The vertical offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def Width(self):
        r"""The video width (pixels) after cropping. The sum of this parameter and `LocationX` cannot be greater than 10000.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""The video height (pixels) after cropping. The sum of this parameter and `LocationY` cannot be greater than 10000.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuFeedBackRoomParams(AbstractModel):
    r"""Parameters for relaying to a TRTC room.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: str
        :param _RoomIdType: The ID type of the room to which streams are relayed. `0` indicates integer, and `1` indicates string.
        :type RoomIdType: int
        :param _UserId: The [user ID](https://www.tencentcloud.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://www.tencentcloud.com/document/product/647/38104).
        :type UserSig: str
        """
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None

    @property
    def RoomId(self):
        r"""The room ID.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""The ID type of the room to which streams are relayed. `0` indicates integer, and `1` indicates string.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        r"""The [user ID](https://www.tencentcloud.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""The signature (similar to login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://www.tencentcloud.com/document/product/647/38104).
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayout(AbstractModel):
    r"""The layout parameters.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: User media stream parameters. if left blank, tencent cloud backend fills them automatically by the room entry sequence of the uplink host.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        :param _ImageWidth: The width of the sub-screen in the output, unit: pixel value. defaults to 0 if left blank.
        :type ImageWidth: int
        :param _ImageHeight: The height of the sub-screen in the output, in pixel values. default is 0.
        :type ImageHeight: int
        :param _LocationX: The X-axis offset of the sub-screen in the output, unit: pixel value. the sum of LocationX and ImageWidth must not exceed the total width of the mixed stream output. default is 0.
        :type LocationX: int
        :param _LocationY: The Y-axis offset of the sub-screen in the output, unit: pixel value. the sum of LocationY and ImageHeight must not exceed the total height of the mixed stream output. default is 0 if left blank.
        :type LocationY: int
        :param _ZOrder: The hierarchy of the sub-screen in the output. default is 0.
        :type ZOrder: int
        :param _RenderMode: The display mode of the sub-screen in the output: 0 for crop, 1 for scale and display background, 2 for scale and display black background. defaults to 0 if left blank.
        :type RenderMode: int
        :param _BackGroundColor: [This parameter configuration is invalid and not currently supported] the background color of the sub-picture. commonly used colors are:.
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999.
        :type BackGroundColor: str
        :param _BackgroundImageUrl: The url of the placeholder image for the sub-window. fill in this parameter to specify the image displayed in the layout position when the user turns the camera off or has not joined the TRTC room. if the specified image has a different size ratio from the layout position, it will be stretched. this parameter has a higher priority than BackGroundColor. supported formats include png, jpg, jpeg, bmp, gif, and webm. the image size limit is no more than 5MB.
Note:.
1. make sure the image link is accessible. the backend single download timeout period is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the placeholder image will not take effect.
2. supported character sets for urls: ['0-9', 'a-z', 'a-z', '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if characters outside the supported character sets exist, the placeholder image will not take effect.
        :type BackgroundImageUrl: str
        :param _CustomCrop: Customer custom crop, targeting the input stream.
        :type CustomCrop: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        :param _BackgroundRenderMode: The display mode of the sub-background image in the output: 0 for crop, 1 for scale and display background, 2 for scale and display black background, 3 for variable-scale scaling, 4 for custom rendering. defaults to 3 if left blank.
        :type BackgroundRenderMode: int
        :param _TransparentUrl: The sub-screen template url points to a template image with an alpha channel. fill in this parameter, and the backend will extract the alpha channel of the template image during compositing, scale it as the alpha channel of the target frame, and mix it with other frames. you can use the transparent template to achieve a semi-transparent effect and arbitrary shape cropping (such as rounded corners, stars, hearts) for the target frame. png format is supported. the image size limit is no more than 5MB.
Note:.
1. the image aspect ratio of the template should be close to the target frame aspect ratio to avoid deformation of the template effect when scaling to fit the target frame. 2. the transparent template only takes effect when RenderMode is 0 (crop). 3. make sure the image link is accessible. the backend single download timeout period is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the transparent template will not take effect.
2. url supported character sets: ['0-9','a-z','a-z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if characters outside the supported character sets exist, the transparent template will not take effect.
        :type TransparentUrl: str
        :param _BackgroundCustomRender: 
        :type BackgroundCustomRender: :class:`tencentcloud.trtc.v20190722.models.McuBackgroundCustomRender`
        :param _BackGroundColorMode: Sub-Background color effective mode. default value 0 means disabled.
bit0 specifies whether placeholder image scaling takes effect.
bit1 specifies whether upstream flow scaling takes effect.
You can set the corresponding bit position to 1 to start up and take effect, such as:.
0(00) means the sub background color is disabled.
1(01) indicates the sub-background color is valid only when placeholder image scaling is enabled.
2(10) means the sub background color is valid only when upstream flow scaling.
3(11) indicates the sub-background color takes effect in both placeholder image scaling and upstream flow scaling.

        :type BackGroundColorMode: int
        """
        self._UserMediaStream = None
        self._ImageWidth = None
        self._ImageHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._RenderMode = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._CustomCrop = None
        self._BackgroundRenderMode = None
        self._TransparentUrl = None
        self._BackgroundCustomRender = None
        self._BackGroundColorMode = None

    @property
    def UserMediaStream(self):
        r"""User media stream parameters. if left blank, tencent cloud backend fills them automatically by the room entry sequence of the uplink host.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream

    @property
    def ImageWidth(self):
        r"""The width of the sub-screen in the output, unit: pixel value. defaults to 0 if left blank.
        :rtype: int
        """
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        r"""The height of the sub-screen in the output, in pixel values. default is 0.
        :rtype: int
        """
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        r"""The X-axis offset of the sub-screen in the output, unit: pixel value. the sum of LocationX and ImageWidth must not exceed the total width of the mixed stream output. default is 0.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""The Y-axis offset of the sub-screen in the output, unit: pixel value. the sum of LocationY and ImageHeight must not exceed the total height of the mixed stream output. default is 0 if left blank.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        r"""The hierarchy of the sub-screen in the output. default is 0.
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def RenderMode(self):
        r"""The display mode of the sub-screen in the output: 0 for crop, 1 for scale and display background, 2 for scale and display black background. defaults to 0 if left blank.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def BackGroundColor(self):
        r"""[This parameter configuration is invalid and not currently supported] the background color of the sub-picture. commonly used colors are:.
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999.
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        r"""The url of the placeholder image for the sub-window. fill in this parameter to specify the image displayed in the layout position when the user turns the camera off or has not joined the TRTC room. if the specified image has a different size ratio from the layout position, it will be stretched. this parameter has a higher priority than BackGroundColor. supported formats include png, jpg, jpeg, bmp, gif, and webm. the image size limit is no more than 5MB.
Note:.
1. make sure the image link is accessible. the backend single download timeout period is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the placeholder image will not take effect.
2. supported character sets for urls: ['0-9', 'a-z', 'a-z', '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if characters outside the supported character sets exist, the placeholder image will not take effect.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def CustomCrop(self):
        r"""Customer custom crop, targeting the input stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        """
        return self._CustomCrop

    @CustomCrop.setter
    def CustomCrop(self, CustomCrop):
        self._CustomCrop = CustomCrop

    @property
    def BackgroundRenderMode(self):
        r"""The display mode of the sub-background image in the output: 0 for crop, 1 for scale and display background, 2 for scale and display black background, 3 for variable-scale scaling, 4 for custom rendering. defaults to 3 if left blank.
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode

    @property
    def TransparentUrl(self):
        r"""The sub-screen template url points to a template image with an alpha channel. fill in this parameter, and the backend will extract the alpha channel of the template image during compositing, scale it as the alpha channel of the target frame, and mix it with other frames. you can use the transparent template to achieve a semi-transparent effect and arbitrary shape cropping (such as rounded corners, stars, hearts) for the target frame. png format is supported. the image size limit is no more than 5MB.
Note:.
1. the image aspect ratio of the template should be close to the target frame aspect ratio to avoid deformation of the template effect when scaling to fit the target frame. 2. the transparent template only takes effect when RenderMode is 0 (crop). 3. make sure the image link is accessible. the backend single download timeout period is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the transparent template will not take effect.
2. url supported character sets: ['0-9','a-z','a-z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if characters outside the supported character sets exist, the transparent template will not take effect.
        :rtype: str
        """
        return self._TransparentUrl

    @TransparentUrl.setter
    def TransparentUrl(self, TransparentUrl):
        self._TransparentUrl = TransparentUrl

    @property
    def BackgroundCustomRender(self):
        r"""
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuBackgroundCustomRender`
        """
        return self._BackgroundCustomRender

    @BackgroundCustomRender.setter
    def BackgroundCustomRender(self, BackgroundCustomRender):
        self._BackgroundCustomRender = BackgroundCustomRender

    @property
    def BackGroundColorMode(self):
        r"""Sub-Background color effective mode. default value 0 means disabled.
bit0 specifies whether placeholder image scaling takes effect.
bit1 specifies whether upstream flow scaling takes effect.
You can set the corresponding bit position to 1 to start up and take effect, such as:.
0(00) means the sub background color is disabled.
1(01) indicates the sub-background color is valid only when placeholder image scaling is enabled.
2(10) means the sub background color is valid only when upstream flow scaling.
3(11) indicates the sub-background color takes effect in both placeholder image scaling and upstream flow scaling.

        :rtype: int
        """
        return self._BackGroundColorMode

    @BackGroundColorMode.setter
    def BackGroundColorMode(self, BackGroundColorMode):
        self._BackGroundColorMode = BackGroundColorMode


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._RenderMode = params.get("RenderMode")
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("CustomCrop") is not None:
            self._CustomCrop = McuCustomCrop()
            self._CustomCrop._deserialize(params.get("CustomCrop"))
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        self._TransparentUrl = params.get("TransparentUrl")
        if params.get("BackgroundCustomRender") is not None:
            self._BackgroundCustomRender = McuBackgroundCustomRender()
            self._BackgroundCustomRender._deserialize(params.get("BackgroundCustomRender"))
        self._BackGroundColorMode = params.get("BackGroundColorMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutParams(AbstractModel):
    r"""The layout parameters.

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: Layout mode: dynamic layout (1: floating layout (default), 2: screen sharing layout, 3: nine-grid layout), static layout (4: custom layout). supports up to 16 mixed media streams. if the user only sends upstream audio, it will be counted as one stream. in custom layout, if the sub-screen only uses placeholder images, it will also be counted as one stream.
        :type MixLayoutMode: int
        :param _PureAudioHoldPlaceMode: Whether to display users who publish only audio. 0: No; 1: Yes. This parameter is valid only if a dynamic layout is used. If you do not pass this parameter, 0 will be used.
        :type PureAudioHoldPlaceMode: int
        :param _MixLayoutList: Valid in custom template. specifies the position of designated user video in mixed display. supports setting up to 16 input streams.
        :type MixLayoutList: list of McuLayout
        :param _MaxVideoUser: The information of the large video in screen sharing or floating layout mode.
        :type MaxVideoUser: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        :param _RenderMode: The image fill mode. This parameter is valid if the layout mode is screen sharing, floating, or grid. `0`: The image will be cropped. `1`: The image will be scaled. `2`: The image will be scaled and there may be black bars.
        :type RenderMode: int
        """
        self._MixLayoutMode = None
        self._PureAudioHoldPlaceMode = None
        self._MixLayoutList = None
        self._MaxVideoUser = None
        self._RenderMode = None

    @property
    def MixLayoutMode(self):
        r"""Layout mode: dynamic layout (1: floating layout (default), 2: screen sharing layout, 3: nine-grid layout), static layout (4: custom layout). supports up to 16 mixed media streams. if the user only sends upstream audio, it will be counted as one stream. in custom layout, if the sub-screen only uses placeholder images, it will also be counted as one stream.
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def PureAudioHoldPlaceMode(self):
        r"""Whether to display users who publish only audio. 0: No; 1: Yes. This parameter is valid only if a dynamic layout is used. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._PureAudioHoldPlaceMode

    @PureAudioHoldPlaceMode.setter
    def PureAudioHoldPlaceMode(self, PureAudioHoldPlaceMode):
        self._PureAudioHoldPlaceMode = PureAudioHoldPlaceMode

    @property
    def MixLayoutList(self):
        r"""Valid in custom template. specifies the position of designated user video in mixed display. supports setting up to 16 input streams.
        :rtype: list of McuLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def MaxVideoUser(self):
        r"""The information of the large video in screen sharing or floating layout mode.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        """
        return self._MaxVideoUser

    @MaxVideoUser.setter
    def MaxVideoUser(self, MaxVideoUser):
        self._MaxVideoUser = MaxVideoUser

    @property
    def RenderMode(self):
        r"""The image fill mode. This parameter is valid if the layout mode is screen sharing, floating, or grid. `0`: The image will be cropped. `1`: The image will be scaled. `2`: The image will be scaled and there may be black bars.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        self._PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = McuLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        if params.get("MaxVideoUser") is not None:
            self._MaxVideoUser = MaxVideoUser()
            self._MaxVideoUser._deserialize(params.get("MaxVideoUser"))
        self._RenderMode = params.get("RenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutVolume(AbstractModel):
    r"""The SEI parameters for audio volume layout. You can specify the `AppData` and `PayloadType`.
    This parameter may be empty, in which case the default SEI parameters for audio volume layout will be used.

    """

    def __init__(self):
        r"""
        :param _AppData: The application data, which will be embedded in the `app_data` field of the custom SEI. It must be shorter than 4,096 characters.
        :type AppData: str
        :param _PayloadType: The payload type of the SEI message. The default is 100. Value range: 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :type PayloadType: int
        :param _Interval: The SEI sending interval (milliseconds). The default value is 1000.
        :type Interval: int
        :param _FollowIdr: Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :type FollowIdr: int
        """
        self._AppData = None
        self._PayloadType = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def AppData(self):
        r"""The application data, which will be embedded in the `app_data` field of the custom SEI. It must be shorter than 4,096 characters.
        :rtype: str
        """
        return self._AppData

    @AppData.setter
    def AppData(self, AppData):
        self._AppData = AppData

    @property
    def PayloadType(self):
        r"""The payload type of the SEI message. The default is 100. Value range: 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def Interval(self):
        r"""The SEI sending interval (milliseconds). The default value is 1000.
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        r"""Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._AppData = params.get("AppData")
        self._PayloadType = params.get("PayloadType")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPassThrough(AbstractModel):
    r"""The custom pass-through SEI.

    """

    def __init__(self):
        r"""
        :param _PayloadContent: The payload of the pass-through SEI.
        :type PayloadContent: str
        :param _PayloadType: PayloadType of SEI message. valid values: 5, 100-254 (exclusion: 244, which is internal custom timestamp SEI).
Note: some players may not support the standard type with PayloadType 5 and PayloadUuid. recommend using another PayloadType.
        :type PayloadType: int
        :param _PayloadUuid: This parameter is required only if `PayloadType` is 5. It must be a 32-character hexadecimal string. If `PayloadType` is not 5, this parameter will be ignored.
        :type PayloadUuid: str
        :param _Interval: The SEI sending interval (milliseconds). The default value is 1000.
        :type Interval: int
        :param _FollowIdr: Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :type FollowIdr: int
        """
        self._PayloadContent = None
        self._PayloadType = None
        self._PayloadUuid = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def PayloadContent(self):
        r"""The payload of the pass-through SEI.
        :rtype: str
        """
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def PayloadType(self):
        r"""PayloadType of SEI message. valid values: 5, 100-254 (exclusion: 244, which is internal custom timestamp SEI).
Note: some players may not support the standard type with PayloadType 5 and PayloadUuid. recommend using another PayloadType.
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def PayloadUuid(self):
        r"""This parameter is required only if `PayloadType` is 5. It must be a 32-character hexadecimal string. If `PayloadType` is not 5, this parameter will be ignored.
        :rtype: str
        """
        return self._PayloadUuid

    @PayloadUuid.setter
    def PayloadUuid(self, PayloadUuid):
        self._PayloadUuid = PayloadUuid

    @property
    def Interval(self):
        r"""The SEI sending interval (milliseconds). The default value is 1000.
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        r"""Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._PayloadContent = params.get("PayloadContent")
        self._PayloadType = params.get("PayloadType")
        self._PayloadUuid = params.get("PayloadUuid")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPublishCdnParam(AbstractModel):
    r"""The relaying parameters.

    """

    def __init__(self):
        r"""
        :param _PublishCdnUrl: The URLs of the CDNs to relay to.
        :type PublishCdnUrl: str
        :param _IsTencentCdn: Whether to relay to Tencent Cloud’s CDN. `0`: Third-party CDN; `1` (default): Tencent Cloud’s CDN. Relaying to a third-party CDN will incur fees. To avoid unexpected charges, we recommend you pass in a specific value. For details, see the API document.
        :type IsTencentCdn: int
        """
        self._PublishCdnUrl = None
        self._IsTencentCdn = None

    @property
    def PublishCdnUrl(self):
        r"""The URLs of the CDNs to relay to.
        :rtype: str
        """
        return self._PublishCdnUrl

    @PublishCdnUrl.setter
    def PublishCdnUrl(self, PublishCdnUrl):
        self._PublishCdnUrl = PublishCdnUrl

    @property
    def IsTencentCdn(self):
        r"""Whether to relay to Tencent Cloud’s CDN. `0`: Third-party CDN; `1` (default): Tencent Cloud’s CDN. Relaying to a third-party CDN will incur fees. To avoid unexpected charges, we recommend you pass in a specific value. For details, see the API document.
        :rtype: int
        """
        return self._IsTencentCdn

    @IsTencentCdn.setter
    def IsTencentCdn(self, IsTencentCdn):
        self._IsTencentCdn = IsTencentCdn


    def _deserialize(self, params):
        self._PublishCdnUrl = params.get("PublishCdnUrl")
        self._IsTencentCdn = params.get("IsTencentCdn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuRecordParams(AbstractModel):
    r"""Relay recording parameters.

    """

    def __init__(self):
        r"""
        :param _UniRecord: Retweet recording mode. 
0/Leave blank: not currently supported; behavior is undefined.
1: disable recording.
2: enable recording (via console automatic recording template parameters.
3: enable recording (use API to specify parameter).
        :type UniRecord: int
        :param _RecordKey: Recording task key, identifies a recording task. you can record multiple relay tasks into a file by specifying this parameter. if this parameter is not specified, only the current relay task is recorded.
Limit length to 128 bytes, only allow a combination of uppercase and lowercase letters (a-zA-Z), digits (0-9), underscores (_), and hyphens (-).
        :type RecordKey: str
        :param _RecordWaitTime: [Valid only when UniRecord=3.].
Resume recording waiting time, corresponding to the "wait time for resumption" in the recording template, unit: seconds. the value must be greater than or equal to 5 and less than or equal to 86400 (24 hours), with a default value of 30. when resumption is enabled, the recording task ends automatically if idle for a duration exceeding RecordWaitTime.
        :type RecordWaitTime: int
        :param _RecordFormat: [Valid only when UniRecord=3.].
The list of output file formats for recording corresponds to the "file format" in the recording template. it supports three formats: "hls", "mp4", and "aac". the default value is "mp4". among them, "mp4" and "aac" formats cannot be specified simultaneously.
Record only the mp4 format, example value: ["mp4"]. record both mp4 and HLS formats simultaneously, example value: ["mp4","HLS"].
        :type RecordFormat: list of str
        :param _MaxMediaFileDuration: [Valid only when UniRecord=3.].
Single file recording duration, corresponding to the "max recording time per file" in the recording template, unit: minutes. the value must be greater than or equal to 1 and less than or equal to 1440 (24 hours), with a default value of 1440. it only takes effect for "mp4" or "aac" format. the actual single file recording duration is also limited by the file size not exceeding 2G. if it exceeds 2G, the file will be forcibly split.
        :type MaxMediaFileDuration: int
        :param _StreamType: [Valid only when UniRecord=3.].
The audio and video type of the recording corresponds to the "recording format" in the recording template. valid values: 0 (audio and video), 1 (pure audio), 2 (video only). the final recording file content is the intersection of the specified type and the relayed content.
        :type StreamType: int
        :param _UserDefineRecordPrefix: Recording file name prefix, no more than 64 characters. this parameter is valid only when store is vod.
Limit length to 64 bytes, only allow a combination of uppercase and lowercase letters (a-zA-Z), digits (0-9), underscores (_), and hyphens (-).
        :type UserDefineRecordPrefix: str
        :param _McuStorageParams: [Valid only when UniRecord=3.].
Recording files storage parameters, corresponding console "storage location" and related parameters. currently supports VOD and COS storage methods. only one can be filled.
        :type McuStorageParams: :class:`tencentcloud.trtc.v20190722.models.McuStorageParams`
        """
        self._UniRecord = None
        self._RecordKey = None
        self._RecordWaitTime = None
        self._RecordFormat = None
        self._MaxMediaFileDuration = None
        self._StreamType = None
        self._UserDefineRecordPrefix = None
        self._McuStorageParams = None

    @property
    def UniRecord(self):
        r"""Retweet recording mode. 
0/Leave blank: not currently supported; behavior is undefined.
1: disable recording.
2: enable recording (via console automatic recording template parameters.
3: enable recording (use API to specify parameter).
        :rtype: int
        """
        return self._UniRecord

    @UniRecord.setter
    def UniRecord(self, UniRecord):
        self._UniRecord = UniRecord

    @property
    def RecordKey(self):
        r"""Recording task key, identifies a recording task. you can record multiple relay tasks into a file by specifying this parameter. if this parameter is not specified, only the current relay task is recorded.
Limit length to 128 bytes, only allow a combination of uppercase and lowercase letters (a-zA-Z), digits (0-9), underscores (_), and hyphens (-).
        :rtype: str
        """
        return self._RecordKey

    @RecordKey.setter
    def RecordKey(self, RecordKey):
        self._RecordKey = RecordKey

    @property
    def RecordWaitTime(self):
        r"""[Valid only when UniRecord=3.].
Resume recording waiting time, corresponding to the "wait time for resumption" in the recording template, unit: seconds. the value must be greater than or equal to 5 and less than or equal to 86400 (24 hours), with a default value of 30. when resumption is enabled, the recording task ends automatically if idle for a duration exceeding RecordWaitTime.
        :rtype: int
        """
        return self._RecordWaitTime

    @RecordWaitTime.setter
    def RecordWaitTime(self, RecordWaitTime):
        self._RecordWaitTime = RecordWaitTime

    @property
    def RecordFormat(self):
        r"""[Valid only when UniRecord=3.].
The list of output file formats for recording corresponds to the "file format" in the recording template. it supports three formats: "hls", "mp4", and "aac". the default value is "mp4". among them, "mp4" and "aac" formats cannot be specified simultaneously.
Record only the mp4 format, example value: ["mp4"]. record both mp4 and HLS formats simultaneously, example value: ["mp4","HLS"].
        :rtype: list of str
        """
        return self._RecordFormat

    @RecordFormat.setter
    def RecordFormat(self, RecordFormat):
        self._RecordFormat = RecordFormat

    @property
    def MaxMediaFileDuration(self):
        r"""[Valid only when UniRecord=3.].
Single file recording duration, corresponding to the "max recording time per file" in the recording template, unit: minutes. the value must be greater than or equal to 1 and less than or equal to 1440 (24 hours), with a default value of 1440. it only takes effect for "mp4" or "aac" format. the actual single file recording duration is also limited by the file size not exceeding 2G. if it exceeds 2G, the file will be forcibly split.
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def StreamType(self):
        r"""[Valid only when UniRecord=3.].
The audio and video type of the recording corresponds to the "recording format" in the recording template. valid values: 0 (audio and video), 1 (pure audio), 2 (video only). the final recording file content is the intersection of the specified type and the relayed content.
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def UserDefineRecordPrefix(self):
        r"""Recording file name prefix, no more than 64 characters. this parameter is valid only when store is vod.
Limit length to 64 bytes, only allow a combination of uppercase and lowercase letters (a-zA-Z), digits (0-9), underscores (_), and hyphens (-).
        :rtype: str
        """
        return self._UserDefineRecordPrefix

    @UserDefineRecordPrefix.setter
    def UserDefineRecordPrefix(self, UserDefineRecordPrefix):
        self._UserDefineRecordPrefix = UserDefineRecordPrefix

    @property
    def McuStorageParams(self):
        r"""[Valid only when UniRecord=3.].
Recording files storage parameters, corresponding console "storage location" and related parameters. currently supports VOD and COS storage methods. only one can be filled.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuStorageParams`
        """
        return self._McuStorageParams

    @McuStorageParams.setter
    def McuStorageParams(self, McuStorageParams):
        self._McuStorageParams = McuStorageParams


    def _deserialize(self, params):
        self._UniRecord = params.get("UniRecord")
        self._RecordKey = params.get("RecordKey")
        self._RecordWaitTime = params.get("RecordWaitTime")
        self._RecordFormat = params.get("RecordFormat")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._StreamType = params.get("StreamType")
        self._UserDefineRecordPrefix = params.get("UserDefineRecordPrefix")
        if params.get("McuStorageParams") is not None:
            self._McuStorageParams = McuStorageParams()
            self._McuStorageParams._deserialize(params.get("McuStorageParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuSeiParams(AbstractModel):
    r"""The stream mixing SEI parameters.

    """

    def __init__(self):
        r"""
        :param _LayoutVolume: The audio volume layout SEI.
        :type LayoutVolume: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        :param _PassThrough: The pass-through SEI.
        :type PassThrough: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        self._LayoutVolume = None
        self._PassThrough = None

    @property
    def LayoutVolume(self):
        r"""The audio volume layout SEI.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        """
        return self._LayoutVolume

    @LayoutVolume.setter
    def LayoutVolume(self, LayoutVolume):
        self._LayoutVolume = LayoutVolume

    @property
    def PassThrough(self):
        r"""The pass-through SEI.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        return self._PassThrough

    @PassThrough.setter
    def PassThrough(self, PassThrough):
        self._PassThrough = PassThrough


    def _deserialize(self, params):
        if params.get("LayoutVolume") is not None:
            self._LayoutVolume = McuLayoutVolume()
            self._LayoutVolume._deserialize(params.get("LayoutVolume"))
        if params.get("PassThrough") is not None:
            self._PassThrough = McuPassThrough()
            self._PassThrough._deserialize(params.get("PassThrough"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuStorageParams(AbstractModel):
    r"""Mcu relay recording. third-party object storage parameters.

    """

    def __init__(self):
        r"""
        :param _CloudStorage: Account information for third-party cloud storage (special note: if you select storage to cloud object storage (COS), there will be a charge for shipping recorded files to COS. for details, see cloud recording pricing information. storing to VOD will incur no charge for this item.).
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param _McuCloudVod: Account information of tencent cloud vod.
        :type McuCloudVod: :class:`tencentcloud.trtc.v20190722.models.McuCloudVod`
        """
        self._CloudStorage = None
        self._McuCloudVod = None

    @property
    def CloudStorage(self):
        r"""Account information for third-party cloud storage (special note: if you select storage to cloud object storage (COS), there will be a charge for shipping recorded files to COS. for details, see cloud recording pricing information. storing to VOD will incur no charge for this item.).
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def McuCloudVod(self):
        r"""Account information of tencent cloud vod.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuCloudVod`
        """
        return self._McuCloudVod

    @McuCloudVod.setter
    def McuCloudVod(self, McuCloudVod):
        self._McuCloudVod = McuCloudVod


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("McuCloudVod") is not None:
            self._McuCloudVod = McuCloudVod()
            self._McuCloudVod._deserialize(params.get("McuCloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuTencentVod(AbstractModel):
    r"""Mcu relay recording. tencent cloud video on demand (vod) related parameters.

    """

    def __init__(self):
        r"""
        :param _Procedure: Subsequent media task processing operations allow automatic task initiation after media upload is completed. the parameter value is the task flow template name. VOD (video on demand) supports creating task flow templates and template naming.
        :type Procedure: str
        :param _ExpireTime: Media file expiry time is the absolute expiration time from the current system time. to save for one day, enter "86400". to retain permanently, enter "0". the default is permanent preservation.
        :type ExpireTime: int
        :param _StorageRegion: Specify the upload park, applicable only to the user with special requirement for upload region.
        :type StorageRegion: str
        :param _ClassId: Category ID is used to categorize and manage media. you can create a category and obtain the category ID through the create category api.
The default value is 0, indicating other categories.
        :type ClassId: int
        :param _SubAppId: Subapplication ID for video-on-demand (vod). if you need to access resources belonging to a subapplication, fill in this field with the subapplication ID. otherwise, this field is not required.
        :type SubAppId: int
        :param _SessionContext: Task flow context, passed through when task complete.
        :type SessionContext: str
        :param _SourceContext: Upload context, passed through on upload completion callback.
        :type SourceContext: str
        """
        self._Procedure = None
        self._ExpireTime = None
        self._StorageRegion = None
        self._ClassId = None
        self._SubAppId = None
        self._SessionContext = None
        self._SourceContext = None

    @property
    def Procedure(self):
        r"""Subsequent media task processing operations allow automatic task initiation after media upload is completed. the parameter value is the task flow template name. VOD (video on demand) supports creating task flow templates and template naming.
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        r"""Media file expiry time is the absolute expiration time from the current system time. to save for one day, enter "86400". to retain permanently, enter "0". the default is permanent preservation.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        r"""Specify the upload park, applicable only to the user with special requirement for upload region.
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        r"""Category ID is used to categorize and manage media. you can create a category and obtain the category ID through the create category api.
The default value is 0, indicating other categories.
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        r"""Subapplication ID for video-on-demand (vod). if you need to access resources belonging to a subapplication, fill in this field with the subapplication ID. otherwise, this field is not required.
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        r"""Task flow context, passed through when task complete.
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        r"""Upload context, passed through on upload completion callback.
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext


    def _deserialize(self, params):
        self._Procedure = params.get("Procedure")
        self._ExpireTime = params.get("ExpireTime")
        self._StorageRegion = params.get("StorageRegion")
        self._ClassId = params.get("ClassId")
        self._SubAppId = params.get("SubAppId")
        self._SessionContext = params.get("SessionContext")
        self._SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuUserInfoParams(AbstractModel):
    r"""The users whose streams are mixed.

    """

    def __init__(self):
        r"""
        :param _UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param _SoundLevel: Audio mix volume adjustment. value ranges from 0 to 100. 100 indicates the original uplink volume. the default value is 100 if left blank. a lower value results in a lower volume.
Note: this parameter takes effect only when configured in the volume allowlist and is unavailable in other scenarios.
        :type SoundLevel: int
        """
        self._UserInfo = None
        self._SoundLevel = None

    @property
    def UserInfo(self):
        r"""The user information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def SoundLevel(self):
        r"""Audio mix volume adjustment. value ranges from 0 to 100. 100 indicates the original uplink volume. the default value is 100 if left blank. a lower value results in a lower volume.
Note: this parameter takes effect only when configured in the volume allowlist and is unavailable in other scenarios.
        :rtype: int
        """
        return self._SoundLevel

    @SoundLevel.setter
    def SoundLevel(self, SoundLevel):
        self._SoundLevel = SoundLevel


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._SoundLevel = params.get("SoundLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuVideoParams(AbstractModel):
    r"""The video parameters for relaying.

    """

    def __init__(self):
        r"""
        :param _VideoEncode: Video encoding parameter for the output stream.
        :type VideoEncode: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        :param _LayoutParams: Stream mixing layout parameter.
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        :param _BackGroundColor: The entire canvas background color. commonly used colors:.
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999.
        :type BackGroundColor: str
        :param _BackgroundImageUrl: The url of the background image for the entire canvas. priority is higher than BackGroundColor. supports png, jpg, and jpeg formats. image size limit is not more than 5MB.
Note:.
1. make sure the image link is accessible. the backend download timeout is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the background image will not take effect.
2. url supported character sets: ['0-9','a-z','a-z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if any character outside the supported character sets exists, the background image will not take effect.
        :type BackgroundImageUrl: str
        :param _WaterMarkList: Watermark parameters for the stream mixing layout.
        :type WaterMarkList: list of McuWaterMarkParams
        :param _BackgroundRenderMode: The display mode of the background image in the output: 0 for crop, 1 for scale and display black background, 2 for variable-scale scaling. the backend defaults to variable-scale scaling.
        :type BackgroundRenderMode: int
        """
        self._VideoEncode = None
        self._LayoutParams = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._WaterMarkList = None
        self._BackgroundRenderMode = None

    @property
    def VideoEncode(self):
        r"""Video encoding parameter for the output stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        """
        return self._VideoEncode

    @VideoEncode.setter
    def VideoEncode(self, VideoEncode):
        self._VideoEncode = VideoEncode

    @property
    def LayoutParams(self):
        r"""Stream mixing layout parameter.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        """
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackGroundColor(self):
        r"""The entire canvas background color. commonly used colors:.
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999.
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        r"""The url of the background image for the entire canvas. priority is higher than BackGroundColor. supports png, jpg, and jpeg formats. image size limit is not more than 5MB.
Note:.
1. make sure the image link is accessible. the backend download timeout is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the background image will not take effect.
2. url supported character sets: ['0-9','a-z','a-z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if any character outside the supported character sets exists, the background image will not take effect.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def WaterMarkList(self):
        r"""Watermark parameters for the stream mixing layout.
        :rtype: list of McuWaterMarkParams
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def BackgroundRenderMode(self):
        r"""The display mode of the background image in the output: 0 for crop, 1 for scale and display black background, 2 for variable-scale scaling. the backend defaults to variable-scale scaling.
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode


    def _deserialize(self, params):
        if params.get("VideoEncode") is not None:
            self._VideoEncode = VideoEncode()
            self._VideoEncode._deserialize(params.get("VideoEncode"))
        if params.get("LayoutParams") is not None:
            self._LayoutParams = McuLayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = McuWaterMarkParams()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkImage(AbstractModel):
    r"""The information of the watermark image.

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: Watermark image URL address. supports png, jpg, and jpeg formats. image size limit not more than 5MB.
Note:.
Make sure the image link has data accessibility. the backend download timeout is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the watermark image will not take effect.
2. supported character sets for urls: ['0-9', 'a-z', 'a-z', '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if any characters exist outside the supported character sets, the watermark image will not take effect.
        :type WaterMarkUrl: str
        :param _WaterMarkWidth: The watermark width (pixels).
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: The watermark height (pixels).
        :type WaterMarkHeight: int
        :param _LocationX: The horizontal offset (pixels) of the watermark.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the watermark.
        :type LocationY: int
        :param _ZOrder: The image layer of the watermark. If you do not pass this parameter, 0 will be used.
        :type ZOrder: int
        :param _DynamicPosType: 
        :type DynamicPosType: int
        """
        self._WaterMarkUrl = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._DynamicPosType = None

    @property
    def WaterMarkUrl(self):
        r"""Watermark image URL address. supports png, jpg, and jpeg formats. image size limit not more than 5MB.
Note:.
Make sure the image link has data accessibility. the backend download timeout is 10 seconds with a maximum of 3 retries. if the image download fails eventually, the watermark image will not take effect.
2. supported character sets for urls: ['0-9', 'a-z', 'a-z', '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|']. make sure url characters are within the supported character sets. if any characters exist outside the supported character sets, the watermark image will not take effect.
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def WaterMarkWidth(self):
        r"""The watermark width (pixels).
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        r"""The watermark height (pixels).
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        r"""The horizontal offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""The vertical offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        r"""The image layer of the watermark. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def DynamicPosType(self):
        r"""
        :rtype: int
        """
        return self._DynamicPosType

    @DynamicPosType.setter
    def DynamicPosType(self, DynamicPosType):
        self._DynamicPosType = DynamicPosType


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._DynamicPosType = params.get("DynamicPosType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkParams(AbstractModel):
    r"""The Watermark information.

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: The watermark type. Valid values: `0` (default): Image; `1`: Text.
        :type WaterMarkType: int
        :param _WaterMarkImage: The watermark image information. This parameter is required if `WaterMarkType` is 0.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        :param _WaterMarkText: The text watermark configuration. This parameter is required if `WaterMarkType` is `1`.
        :type WaterMarkText: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkText = None

    @property
    def WaterMarkType(self):
        r"""The watermark type. Valid values: `0` (default): Image; `1`: Text.
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        r"""The watermark image information. This parameter is required if `WaterMarkType` is 0.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkText(self):
        r"""The text watermark configuration. This parameter is required if `WaterMarkType` is `1`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        return self._WaterMarkText

    @WaterMarkText.setter
    def WaterMarkText(self, WaterMarkText):
        self._WaterMarkText = WaterMarkText


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = McuWaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkText") is not None:
            self._WaterMarkText = McuWaterMarkText()
            self._WaterMarkText._deserialize(params.get("WaterMarkText"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkText(AbstractModel):
    r"""The text watermark configuration.

    """

    def __init__(self):
        r"""
        :param _Text: The text.
        :type Text: str
        :param _WaterMarkWidth: The watermark width (pixels).
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: The watermark height (pixels).
        :type WaterMarkHeight: int
        :param _LocationX: The horizontal offset (pixels) of the watermark.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the watermark.
        :type LocationY: int
        :param _FontSize: The font size.
        :type FontSize: int
        :param _FontColor: The text color. The default color is white. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :type FontColor: str
        :param _BackGroundColor: The text fill color. If you do not specify this parameter, the fill color will be transparent. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :type BackGroundColor: str
        :param _DynamicPosType: 
        :type DynamicPosType: int
        :param _ZOrder: 
        :type ZOrder: int
        :param _Font: Watermark font, by default if left blank is Tencent. valid values: Tencent (default), SourceHanSans.
        :type Font: str
        """
        self._Text = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None
        self._DynamicPosType = None
        self._ZOrder = None
        self._Font = None

    @property
    def Text(self):
        r"""The text.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def WaterMarkWidth(self):
        r"""The watermark width (pixels).
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        r"""The watermark height (pixels).
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        r"""The horizontal offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""The vertical offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def FontSize(self):
        r"""The font size.
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        r"""The text color. The default color is white. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        r"""The text fill color. If you do not specify this parameter, the fill color will be transparent. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def DynamicPosType(self):
        r"""
        :rtype: int
        """
        return self._DynamicPosType

    @DynamicPosType.setter
    def DynamicPosType(self, DynamicPosType):
        self._DynamicPosType = DynamicPosType

    @property
    def ZOrder(self):
        r"""
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def Font(self):
        r"""Watermark font, by default if left blank is Tencent. valid values: Tencent (default), SourceHanSans.
        :rtype: str
        """
        return self._Font

    @Font.setter
    def Font(self, Font):
        self._Font = Font


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        self._DynamicPosType = params.get("DynamicPosType")
        self._ZOrder = params.get("ZOrder")
        self._Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayout(AbstractModel):
    r"""The custom layout parameters.

    """

    def __init__(self):
        r"""
        :param _Top: The Y axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas height.
        :type Top: int
        :param _Left: The X axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas width.
        :type Left: int
        :param _Width: The relative width of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param _Height: The relative height of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        :param _UserId: The user ID (string) of the anchor whose video is shown in the window. If you do not set this parameter, anchors’ videos will be shown in their room entry sequence.
        :type UserId: str
        :param _Alpha: The degree of transparency of the canvas. Value range: [0, 255]. 0 means fully opaque, and 255 means fully transparent.
        :type Alpha: int
        :param _RenderMode: 0: Stretch. In this mode, the image is stretched to fill the space available. The whole image is visible after scaling. However, if the original aspect ratio is different from the target, the image may be distorted.

1: Crop (default). In this mode, if the original aspect ratio is different from the target, the image will be cropped according to the target before being stretched to fill the space available. The image will not be distorted.

2: Blank. This mode stretches the image while keeping its original aspect ratio. If the original aspect ratio is different from the target, there may be blank spaces to the top and bottom or to the left and right of the window.

3: Smart stretch. This mode is similar to the crop mode, except that it restricts cropping to 20% of the image’s width or height at most.
        :type RenderMode: int
        :param _MediaId: The type of the stream subscribed to.
0: Primary stream (default)
1: Substream
        :type MediaId: int
        :param _ImageLayer: The image layer. 0 is the default value and means the bottommost layer.
        :type ImageLayer: int
        :param _SubBackgroundImage: The image url supports only jpg, png, and jpeg formats. the resolution limitation is no more than 2K, and the image size limit is no more than 5MB. note that the url must carry the format extension. the url supports only specific strings within the range of a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', and '='.
        :type SubBackgroundImage: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._UserId = None
        self._Alpha = None
        self._RenderMode = None
        self._MediaId = None
        self._ImageLayer = None
        self._SubBackgroundImage = None

    @property
    def Top(self):
        r"""The Y axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas height.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""The X axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas width.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""The relative width of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""The relative height of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def UserId(self):
        r"""The user ID (string) of the anchor whose video is shown in the window. If you do not set this parameter, anchors’ videos will be shown in their room entry sequence.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Alpha(self):
        r"""The degree of transparency of the canvas. Value range: [0, 255]. 0 means fully opaque, and 255 means fully transparent.
        :rtype: int
        """
        return self._Alpha

    @Alpha.setter
    def Alpha(self, Alpha):
        self._Alpha = Alpha

    @property
    def RenderMode(self):
        r"""0: Stretch. In this mode, the image is stretched to fill the space available. The whole image is visible after scaling. However, if the original aspect ratio is different from the target, the image may be distorted.

1: Crop (default). In this mode, if the original aspect ratio is different from the target, the image will be cropped according to the target before being stretched to fill the space available. The image will not be distorted.

2: Blank. This mode stretches the image while keeping its original aspect ratio. If the original aspect ratio is different from the target, there may be blank spaces to the top and bottom or to the left and right of the window.

3: Smart stretch. This mode is similar to the crop mode, except that it restricts cropping to 20% of the image’s width or height at most.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MediaId(self):
        r"""The type of the stream subscribed to.
0: Primary stream (default)
1: Substream
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def ImageLayer(self):
        r"""The image layer. 0 is the default value and means the bottommost layer.
        :rtype: int
        """
        return self._ImageLayer

    @ImageLayer.setter
    def ImageLayer(self, ImageLayer):
        self._ImageLayer = ImageLayer

    @property
    def SubBackgroundImage(self):
        r"""The image url supports only jpg, png, and jpeg formats. the resolution limitation is no more than 2K, and the image size limit is no more than 5MB. note that the url must carry the format extension. the url supports only specific strings within the range of a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', and '='.
        :rtype: str
        """
        return self._SubBackgroundImage

    @SubBackgroundImage.setter
    def SubBackgroundImage(self, SubBackgroundImage):
        self._SubBackgroundImage = SubBackgroundImage


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._UserId = params.get("UserId")
        self._Alpha = params.get("Alpha")
        self._RenderMode = params.get("RenderMode")
        self._MediaId = params.get("MediaId")
        self._ImageLayer = params.get("ImageLayer")
        self._SubBackgroundImage = params.get("SubBackgroundImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayoutParams(AbstractModel):
    r"""The layout parameters for mixed-stream recording.

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: Layout mode.
1: floating layout.
2: screen sharing layout.
3: nine-grid layout.
4: custom layout.

Floating layout: by default, the video footage of the first host who enters the room (or a specified host) fills the entire screen. other hosts' video images are arranged horizontally from the bottom-left corner in the room entry sequence, displayed as small pictures floating above the large screen. when the number of screens is less than or equal to 17, each line has 4 (4 x 4 arrangement). when the number of screens exceeds 17, the small pictures are rearranged with 5 per line (5 x 5 arrangement). a maximum of 25 screens are supported. if the user only sends audio, it still occupies a screen position.

Screen sharing layout: specifies a large screen position on the left side for one host (if not specified, the large screen position uses the background color). other hosts are arranged vertically on the right side from top to bottom. when the number of screens is less than 17, each column on the right supports up to 8 hosts, occupying a maximum of two columns. when the number of screens exceeds 17, hosts beyond the 17th are arranged horizontally starting from the bottom-left corner. a maximum of 25 screens is supported. if a host only sends audio, it still occupies a screen position.

Nine-Grid layout: automatically adjust the size of each frame based on the number of hosts. each host's frame size is the same, supporting up to 25 frames.

Custom layout: customize the layout of each host's video as needed in MixLayoutList.
        :type MixLayoutMode: int
        :param _MixLayoutList: The custom layout details. This parameter is valid if `MixLayoutMode` is set to `4`. Up to 25 videos can be displayed.
        :type MixLayoutList: list of MixLayout
        :param _BackGroundColor: The background color, which is a hexadecimal value (starting with "#", followed by the color value) converted from an 8-bit RGB value. For example, the RGB value of orange is `R:255 G:165 B:0`, and its hexadecimal value is `#FFA500`. The default color is black.
        :type BackGroundColor: str
        :param _MaxResolutionUserId: The user whose video is displayed in the big window. This parameter is valid if `MixLayoutMode` is set to `1` (floating) or `2` (screen sharing). If it is left empty, the first anchor entering the room is displayed in the big window in the floating mode and the canvas background is displayed in the screen sharing mode.
        :type MaxResolutionUserId: str
        :param _MediaId: The stream type.
0: Primary stream (default)
1: Substream (screen sharing stream)
This parameter specifies the type of the stream displayed in the big window. If it appears in `MixLayoutList`, it indicates the type of the stream of a specified user.
        :type MediaId: int
        :param _BackgroundImageUrl: The image url supports only jpg, png, and jpeg. the image resolution is limited to no more than 2K, and the image size limit is no more than 5MB. note that the url must carry the format extension, and only specific strings are supported in the url, including a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', and '='.
        :type BackgroundImageUrl: str
        :param _PlaceHolderMode: Set to 1 to enable the placeholder image function, and 0 to disable it. default is 0. when enabled, the corresponding placeholder image can be displayed in the preset position if the user has no upload audio and video.
        :type PlaceHolderMode: int
        :param _BackgroundImageRenderMode: Handling solution when the background image aspect ratio is not the same, consistent with the RenderMode defined in MixLayoutList.
        :type BackgroundImageRenderMode: int
        :param _DefaultSubBackgroundImage: Sub-Picture placeholder image url supports only jpg, png, jpeg. resolution limitation is no more than 2K. image size limit is no more than 5MB. note that the url must carry format extension and supports only specific string literals within the range of a-z a-z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='.
        :type DefaultSubBackgroundImage: str
        :param _WaterMarkList: The watermark layout. Up to 25 watermarks are supported.
        :type WaterMarkList: list of WaterMark
        :param _RenderMode: When the aspect ratio of the background image does not match in the template layout, the handling solution is applied. the custom layout is disabled and aligns with the RenderMode defined in MixLayoutList.
        :type RenderMode: int
        :param _MaxResolutionUserAlign: This parameter is valid only if the screen sharing layout is used. If you set it to `1`, the large video window will appear on the right and the small window on the left. The default value is `0`.
        :type MaxResolutionUserAlign: int
        :param _PureAudioDisableLayout: Controls whether audio users inside the room occupy the stream mixing layout. this takes effect only in mixed stream recording and template layout. true: represents that audio users do not occupy placeholders. false: represents that audio users occupy placeholders (false by default).
        :type PureAudioDisableLayout: bool
        """
        self._MixLayoutMode = None
        self._MixLayoutList = None
        self._BackGroundColor = None
        self._MaxResolutionUserId = None
        self._MediaId = None
        self._BackgroundImageUrl = None
        self._PlaceHolderMode = None
        self._BackgroundImageRenderMode = None
        self._DefaultSubBackgroundImage = None
        self._WaterMarkList = None
        self._RenderMode = None
        self._MaxResolutionUserAlign = None
        self._PureAudioDisableLayout = None

    @property
    def MixLayoutMode(self):
        r"""Layout mode.
1: floating layout.
2: screen sharing layout.
3: nine-grid layout.
4: custom layout.

Floating layout: by default, the video footage of the first host who enters the room (or a specified host) fills the entire screen. other hosts' video images are arranged horizontally from the bottom-left corner in the room entry sequence, displayed as small pictures floating above the large screen. when the number of screens is less than or equal to 17, each line has 4 (4 x 4 arrangement). when the number of screens exceeds 17, the small pictures are rearranged with 5 per line (5 x 5 arrangement). a maximum of 25 screens are supported. if the user only sends audio, it still occupies a screen position.

Screen sharing layout: specifies a large screen position on the left side for one host (if not specified, the large screen position uses the background color). other hosts are arranged vertically on the right side from top to bottom. when the number of screens is less than 17, each column on the right supports up to 8 hosts, occupying a maximum of two columns. when the number of screens exceeds 17, hosts beyond the 17th are arranged horizontally starting from the bottom-left corner. a maximum of 25 screens is supported. if a host only sends audio, it still occupies a screen position.

Nine-Grid layout: automatically adjust the size of each frame based on the number of hosts. each host's frame size is the same, supporting up to 25 frames.

Custom layout: customize the layout of each host's video as needed in MixLayoutList.
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def MixLayoutList(self):
        r"""The custom layout details. This parameter is valid if `MixLayoutMode` is set to `4`. Up to 25 videos can be displayed.
        :rtype: list of MixLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def BackGroundColor(self):
        r"""The background color, which is a hexadecimal value (starting with "#", followed by the color value) converted from an 8-bit RGB value. For example, the RGB value of orange is `R:255 G:165 B:0`, and its hexadecimal value is `#FFA500`. The default color is black.
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def MaxResolutionUserId(self):
        r"""The user whose video is displayed in the big window. This parameter is valid if `MixLayoutMode` is set to `1` (floating) or `2` (screen sharing). If it is left empty, the first anchor entering the room is displayed in the big window in the floating mode and the canvas background is displayed in the screen sharing mode.
        :rtype: str
        """
        return self._MaxResolutionUserId

    @MaxResolutionUserId.setter
    def MaxResolutionUserId(self, MaxResolutionUserId):
        self._MaxResolutionUserId = MaxResolutionUserId

    @property
    def MediaId(self):
        r"""The stream type.
0: Primary stream (default)
1: Substream (screen sharing stream)
This parameter specifies the type of the stream displayed in the big window. If it appears in `MixLayoutList`, it indicates the type of the stream of a specified user.
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def BackgroundImageUrl(self):
        r"""The image url supports only jpg, png, and jpeg. the image resolution is limited to no more than 2K, and the image size limit is no more than 5MB. note that the url must carry the format extension, and only specific strings are supported in the url, including a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', and '='.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def PlaceHolderMode(self):
        r"""Set to 1 to enable the placeholder image function, and 0 to disable it. default is 0. when enabled, the corresponding placeholder image can be displayed in the preset position if the user has no upload audio and video.
        :rtype: int
        """
        return self._PlaceHolderMode

    @PlaceHolderMode.setter
    def PlaceHolderMode(self, PlaceHolderMode):
        self._PlaceHolderMode = PlaceHolderMode

    @property
    def BackgroundImageRenderMode(self):
        r"""Handling solution when the background image aspect ratio is not the same, consistent with the RenderMode defined in MixLayoutList.
        :rtype: int
        """
        return self._BackgroundImageRenderMode

    @BackgroundImageRenderMode.setter
    def BackgroundImageRenderMode(self, BackgroundImageRenderMode):
        self._BackgroundImageRenderMode = BackgroundImageRenderMode

    @property
    def DefaultSubBackgroundImage(self):
        r"""Sub-Picture placeholder image url supports only jpg, png, jpeg. resolution limitation is no more than 2K. image size limit is no more than 5MB. note that the url must carry format extension and supports only specific string literals within the range of a-z a-z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='.
        :rtype: str
        """
        return self._DefaultSubBackgroundImage

    @DefaultSubBackgroundImage.setter
    def DefaultSubBackgroundImage(self, DefaultSubBackgroundImage):
        self._DefaultSubBackgroundImage = DefaultSubBackgroundImage

    @property
    def WaterMarkList(self):
        r"""The watermark layout. Up to 25 watermarks are supported.
        :rtype: list of WaterMark
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def RenderMode(self):
        r"""When the aspect ratio of the background image does not match in the template layout, the handling solution is applied. the custom layout is disabled and aligns with the RenderMode defined in MixLayoutList.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MaxResolutionUserAlign(self):
        r"""This parameter is valid only if the screen sharing layout is used. If you set it to `1`, the large video window will appear on the right and the small window on the left. The default value is `0`.
        :rtype: int
        """
        return self._MaxResolutionUserAlign

    @MaxResolutionUserAlign.setter
    def MaxResolutionUserAlign(self, MaxResolutionUserAlign):
        self._MaxResolutionUserAlign = MaxResolutionUserAlign

    @property
    def PureAudioDisableLayout(self):
        r"""Controls whether audio users inside the room occupy the stream mixing layout. this takes effect only in mixed stream recording and template layout. true: represents that audio users do not occupy placeholders. false: represents that audio users occupy placeholders (false by default).
        :rtype: bool
        """
        return self._PureAudioDisableLayout

    @PureAudioDisableLayout.setter
    def PureAudioDisableLayout(self, PureAudioDisableLayout):
        self._PureAudioDisableLayout = PureAudioDisableLayout


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = MixLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        self._BackGroundColor = params.get("BackGroundColor")
        self._MaxResolutionUserId = params.get("MaxResolutionUserId")
        self._MediaId = params.get("MediaId")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        self._PlaceHolderMode = params.get("PlaceHolderMode")
        self._BackgroundImageRenderMode = params.get("BackgroundImageRenderMode")
        self._DefaultSubBackgroundImage = params.get("DefaultSubBackgroundImage")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = WaterMark()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._RenderMode = params.get("RenderMode")
        self._MaxResolutionUserAlign = params.get("MaxResolutionUserAlign")
        self._PureAudioDisableLayout = params.get("PureAudioDisableLayout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixTranscodeParams(AbstractModel):
    r"""The audio and video parameters for recording.

    """

    def __init__(self):
        r"""
        :param _VideoParams: The video transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        :param _AudioParams: The audio transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        self._VideoParams = None
        self._AudioParams = None

    @property
    def VideoParams(self):
        r"""The video transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def AudioParams(self):
        r"""The audio transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams


    def _deserialize(self, params):
        if params.get("VideoParams") is not None:
            self._VideoParams = VideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("AudioParams") is not None:
            self._AudioParams = AudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixUserInfo(AbstractModel):
    r"""The user information.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _RoomId: If a dynamic layout is used, the value of this parameter should be the ID of the main room. If a custom layout is used, the value of this parameter should be the same as the room ID in `MixLayoutList`.
        :type RoomId: str
        :param _RoomIdType: Room id type. 0 indicates integer room number. 1 indicates string room number.
        :type RoomIdType: int
        """
        self._UserId = None
        self._RoomId = None
        self._RoomIdType = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        r"""If a dynamic layout is used, the value of this parameter should be the ID of the main room. If a custom layout is used, the value of this parameter should be the same as the room ID in `MixLayoutList`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""Room id type. 0 indicates integer room number. 1 indicates string room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationParams(AbstractModel):
    r"""Control parameters for cloud moderation.

    """

    def __init__(self):
        r"""
        :param _ModerationType: Moderation task type. 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio slicing moderation + video frame extraction moderation; 4: audio stream moderation; 5: audio stream moderation + video frame extraction moderation. The default value is 1. (Support from suppliers is required for stream moderation to take effect.)
        :type ModerationType: int
        :param _MaxIdleTime: Slicing is stopped automatically when there is no user (anchor) performing upstream push in the room for more than MaxIdleTime. Unit: seconds. Default value: 30 seconds. This value needs to be greater than or equal to 5 seconds and less than or equal to 1800 seconds (0.5 hours). Example value: 30.
        :type MaxIdleTime: int
        :param _SliceAudio: Audio slicing duration. Default value: 15s. Example value: 15.
        :type SliceAudio: int
        :param _SliceVideo: Interval for video frame extraction. Default value: 5s.
        :type SliceVideo: int
        :param _ModerationSupplier: Enumeration values for suppliers.
tianyu: Tencent Tianyu content security. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
ace: ACE content security. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
shumei: shumei moderation. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
Yidun: NetEase Yidun moderation. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
        :type ModerationSupplier: str
        :param _ModerationSupplierParam: Configuration information required for submitting content to the third-party moderation supplier.
        :type ModerationSupplierParam: :class:`tencentcloud.trtc.v20190722.models.ModerationSupplierParam`
        :param _SaveModerationFile: Whether to save file. 0: not save by default; 1: save; 2 save the hit file.
        :type SaveModerationFile: int
        :param _CallbackAllResults: Whether to call back all moderation results: 0: call back all results by default; 1: only call back hit results.
        :type CallbackAllResults: int
        :param _SubscribeStreamUserIds: Specifies the allowlist or blocklist for the subscription stream.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        self._ModerationType = None
        self._MaxIdleTime = None
        self._SliceAudio = None
        self._SliceVideo = None
        self._ModerationSupplier = None
        self._ModerationSupplierParam = None
        self._SaveModerationFile = None
        self._CallbackAllResults = None
        self._SubscribeStreamUserIds = None

    @property
    def ModerationType(self):
        r"""Moderation task type. 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio slicing moderation + video frame extraction moderation; 4: audio stream moderation; 5: audio stream moderation + video frame extraction moderation. The default value is 1. (Support from suppliers is required for stream moderation to take effect.)
        :rtype: int
        """
        return self._ModerationType

    @ModerationType.setter
    def ModerationType(self, ModerationType):
        self._ModerationType = ModerationType

    @property
    def MaxIdleTime(self):
        r"""Slicing is stopped automatically when there is no user (anchor) performing upstream push in the room for more than MaxIdleTime. Unit: seconds. Default value: 30 seconds. This value needs to be greater than or equal to 5 seconds and less than or equal to 1800 seconds (0.5 hours). Example value: 30.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def SliceAudio(self):
        r"""Audio slicing duration. Default value: 15s. Example value: 15.
        :rtype: int
        """
        return self._SliceAudio

    @SliceAudio.setter
    def SliceAudio(self, SliceAudio):
        self._SliceAudio = SliceAudio

    @property
    def SliceVideo(self):
        r"""Interval for video frame extraction. Default value: 5s.
        :rtype: int
        """
        return self._SliceVideo

    @SliceVideo.setter
    def SliceVideo(self, SliceVideo):
        self._SliceVideo = SliceVideo

    @property
    def ModerationSupplier(self):
        r"""Enumeration values for suppliers.
tianyu: Tencent Tianyu content security. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
ace: ACE content security. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
shumei: shumei moderation. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
Yidun: NetEase Yidun moderation. (Valid values: 1: audio slicing moderation; 2: video frame extraction moderation; 3: audio-visual slicing moderation + video frame extraction moderation.)
        :rtype: str
        """
        return self._ModerationSupplier

    @ModerationSupplier.setter
    def ModerationSupplier(self, ModerationSupplier):
        self._ModerationSupplier = ModerationSupplier

    @property
    def ModerationSupplierParam(self):
        r"""Configuration information required for submitting content to the third-party moderation supplier.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationSupplierParam`
        """
        return self._ModerationSupplierParam

    @ModerationSupplierParam.setter
    def ModerationSupplierParam(self, ModerationSupplierParam):
        self._ModerationSupplierParam = ModerationSupplierParam

    @property
    def SaveModerationFile(self):
        r"""Whether to save file. 0: not save by default; 1: save; 2 save the hit file.
        :rtype: int
        """
        return self._SaveModerationFile

    @SaveModerationFile.setter
    def SaveModerationFile(self, SaveModerationFile):
        self._SaveModerationFile = SaveModerationFile

    @property
    def CallbackAllResults(self):
        r"""Whether to call back all moderation results: 0: call back all results by default; 1: only call back hit results.
        :rtype: int
        """
        return self._CallbackAllResults

    @CallbackAllResults.setter
    def CallbackAllResults(self, CallbackAllResults):
        self._CallbackAllResults = CallbackAllResults

    @property
    def SubscribeStreamUserIds(self):
        r"""Specifies the allowlist or blocklist for the subscription stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._ModerationType = params.get("ModerationType")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._SliceAudio = params.get("SliceAudio")
        self._SliceVideo = params.get("SliceVideo")
        self._ModerationSupplier = params.get("ModerationSupplier")
        if params.get("ModerationSupplierParam") is not None:
            self._ModerationSupplierParam = ModerationSupplierParam()
            self._ModerationSupplierParam._deserialize(params.get("ModerationSupplierParam"))
        self._SaveModerationFile = params.get("SaveModerationFile")
        self._CallbackAllResults = params.get("CallbackAllResults")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeModerationUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationStorageParams(AbstractModel):
    r"""Moderation file storage parameters.

    """

    def __init__(self):
        r"""
        :param _CloudModerationStorage: Information about Tencent COS and third-party cloud storage accounts.
        :type CloudModerationStorage: :class:`tencentcloud.trtc.v20190722.models.CloudModerationStorage`
        """
        self._CloudModerationStorage = None

    @property
    def CloudModerationStorage(self):
        r"""Information about Tencent COS and third-party cloud storage accounts.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudModerationStorage`
        """
        return self._CloudModerationStorage

    @CloudModerationStorage.setter
    def CloudModerationStorage(self, CloudModerationStorage):
        self._CloudModerationStorage = CloudModerationStorage


    def _deserialize(self, params):
        if params.get("CloudModerationStorage") is not None:
            self._CloudModerationStorage = CloudModerationStorage()
            self._CloudModerationStorage._deserialize(params.get("CloudModerationStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationSupplierParam(AbstractModel):
    r"""Parameters required for submitting content to the third-party moderation supplier.

    """

    def __init__(self):
        r"""
        :param _AppID: Moderation supplier account ID. For Tencent Tianyu, the value is not null; for NETEASE Yidun, the value is null.
        :type AppID: str
        :param _SecretId: Moderation supplier key ID.
        :type SecretId: str
        :param _SecretKey: Moderation supplier key.
        :type SecretKey: str
        :param _AudioBizType: Audio scenario. Policy ID or businessId.
        :type AudioBizType: str
        :param _ImageBizType: Image scenario. Policy ID or businessId.
        :type ImageBizType: str
        """
        self._AppID = None
        self._SecretId = None
        self._SecretKey = None
        self._AudioBizType = None
        self._ImageBizType = None

    @property
    def AppID(self):
        r"""Moderation supplier account ID. For Tencent Tianyu, the value is not null; for NETEASE Yidun, the value is null.
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def SecretId(self):
        r"""Moderation supplier key ID.
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        r"""Moderation supplier key.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def AudioBizType(self):
        r"""Audio scenario. Policy ID or businessId.
        :rtype: str
        """
        return self._AudioBizType

    @AudioBizType.setter
    def AudioBizType(self, AudioBizType):
        self._AudioBizType = AudioBizType

    @property
    def ImageBizType(self):
        r"""Image scenario. Policy ID or businessId.
        :rtype: str
        """
        return self._ImageBizType

    @ImageBizType.setter
    def ImageBizType(self, ImageBizType):
        self._ImageBizType = ImageBizType


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._AudioBizType = params.get("AudioBizType")
        self._ImageBizType = params.get("ImageBizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudModerationRequest(AbstractModel):
    r"""ModifyCloudModeration request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the moderation task, which is returned after the task is started.
        :type TaskId: str
        :param _SubscribeStreamUserIds: Specifies the allowlist or blocklist for the subscription stream.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SubscribeStreamUserIds(self):
        r"""Specifies the allowlist or blocklist for the subscription stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudModerationResponse(AbstractModel):
    r"""ModifyCloudModeration response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the moderation task, which is returned after the task is started.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the moderation task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyCloudRecordingRequest(AbstractModel):
    r"""ModifyCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        :param _MixLayoutParams: The new stream mixing layout to use.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _SubscribeStreamUserIds: The allowlist/blocklist for stream subscription.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._MixLayoutParams = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MixLayoutParams(self):
        r"""The new stream mixing layout to use.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def SubscribeStreamUserIds(self):
        r"""The allowlist/blocklist for stream subscription.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingResponse(AbstractModel):
    r"""ModifyCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyCloudSliceTaskRequest(AbstractModel):
    r"""ModifyCloudSliceTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :type SdkAppId: int
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        :param _SubscribeStreamUserIds: Specifies the allowlist or blocklist for the subscription stream.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the TRTC room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SubscribeStreamUserIds(self):
        r"""Specifies the allowlist or blocklist for the subscription stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudSliceTaskResponse(AbstractModel):
    r"""ModifyCloudSliceTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the slicing task, which is returned after the task is started.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique ID of the slicing task, which is returned after the task is started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PronunciationDict(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Word: 
        :type Word: str
        :param _Pronunciation: 
        :type Pronunciation: str
        """
        self._Word = None
        self._Pronunciation = None

    @property
    def Word(self):
        r"""
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Pronunciation(self):
        r"""
        :rtype: str
        """
        return self._Pronunciation

    @Pronunciation.setter
    def Pronunciation(self, Pronunciation):
        self._Pronunciation = Pronunciation


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._Pronunciation = params.get("Pronunciation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityData(AbstractModel):
    r"""The quality data returned by ES.

    """

    def __init__(self):
        r"""
        :param _Content: The quality data.
        :type Content: list of TimeValue
        :param _UserId: The user ID.
        :type UserId: str
        :param _PeerId: The remote user ID. An empty string indicates that the data is upstream data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        :param _DataType: The data type.
        :type DataType: str
        """
        self._Content = None
        self._UserId = None
        self._PeerId = None
        self._DataType = None

    @property
    def Content(self):
        r"""The quality data.
        :rtype: list of TimeValue
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PeerId(self):
        r"""The remote user ID. An empty string indicates that the data is upstream data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def DataType(self):
        r"""The data type.
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self._Content.append(obj)
        self._UserId = params.get("UserId")
        self._PeerId = params.get("PeerId")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeConfig(AbstractModel):
    r"""Configuration for speech recognition usage.

    """

    def __init__(self):
        r"""
        :param _Language: Convert speech to text supported languages, "zh" chinese is selected by default.

You can unlock different languages by purchasing the "AI intelligent recognition duration package" or claiming the trial version of the monthly subscription package. 

Supported languages for different speech to text package versions are as follows:.

Basic language engine:.
-"zh": chinese (simplified).

**Standard language engine:**.
-"8k_zh_large": engine (large model version) for telecommunication. the current model supports chinese and other language recognition, has a large number of parameters, and features language model performance enhancement. it greatly improves recognition accuracy for telephone audio in various scenarios and chinese dialects.
-"16k_zh_large": large model engine for mandarin, chinese dialects, and english. the current model supports language recognition for chinese, english, and multiple chinese dialects. it has a large number of parameters and enhanced language model performance, targeting low-quality audio such as loud noise, strong echo, low voice volume, and voice from far away with greatly improved recognition accuracy.
-"16k_zh_en": chinese-english large model engine. the current model simultaneously supports chinese and english recognition, has a large number of parameters, and features language model performance enhancement. it greatly improves recognition accuracy for low-quality audio such as loud noise, strong echo, low voice volume, and voice from far away.

**Advanced language engine:**.
-"zh-dialect": chinese dialect.
-"zh-yue": cantonese in china.
-"Vi": "vietnamese.".
-"Ja": "japanese.".
-"Ko": "korean.".
-"id": "indonesian".
-"Th": thai.
-"pt": portuguese.
-"tr": "turkish.".
-"Ar": "arabic".
-"es": "spanish".
-"Hi": "hindi".
-"Fr": "french.".
-"ms": malay.
-"Fil": filipino.
-"de": german.
-`It`: italian.
-"Ru": russian.
-"sv": "swedish.".
-"Da": "danish.".
-"No": norwegian.

**Note**:.
If the language you need is not available, contact our technical staff.
        :type Language: str
        :param _AlternativeLanguage: **Fuzzy recognition is an advanced edition capacity, charged as advanced edition by default, and only supports filling in basic version and advanced edition language.**.
Note: does not support entering "zh-dialect".
        :type AlternativeLanguage: list of str
        :param _HotWordList: Hot word list: this parameter is used for improving recognition accuracy. each hot word is limited to "term|weight", with no more than 30 characters (a maximum of 10 chinese characters) per term. weight ranges from 1 to 11 or 100, for example: "tencent cloud|5" or "ASR|11". hot word list limitation: multiple terms separated by commas, supports up to 300 hot words, for example: "tencent cloud|10, speech recognition|5, ASR|11".
        :type HotWordList: str
        :param _VadSilenceTime: Specifies the time when automatic speech recognition (asr) vad is active. value range: 240-2000. default: 1000. unit: ms. a smaller value enables faster speech recognition sentence segmentation.
        :type VadSilenceTime: int
        :param _VadLevel: The vad far-field voice suppression capacity (does not impact asr recognition performance) ranges from 0 to 3, with a default value of 0. recommended setting is 2 for better far-field voice suppression.
        :type VadLevel: int
        """
        self._Language = None
        self._AlternativeLanguage = None
        self._HotWordList = None
        self._VadSilenceTime = None
        self._VadLevel = None

    @property
    def Language(self):
        r"""Convert speech to text supported languages, "zh" chinese is selected by default.

You can unlock different languages by purchasing the "AI intelligent recognition duration package" or claiming the trial version of the monthly subscription package. 

Supported languages for different speech to text package versions are as follows:.

Basic language engine:.
-"zh": chinese (simplified).

**Standard language engine:**.
-"8k_zh_large": engine (large model version) for telecommunication. the current model supports chinese and other language recognition, has a large number of parameters, and features language model performance enhancement. it greatly improves recognition accuracy for telephone audio in various scenarios and chinese dialects.
-"16k_zh_large": large model engine for mandarin, chinese dialects, and english. the current model supports language recognition for chinese, english, and multiple chinese dialects. it has a large number of parameters and enhanced language model performance, targeting low-quality audio such as loud noise, strong echo, low voice volume, and voice from far away with greatly improved recognition accuracy.
-"16k_zh_en": chinese-english large model engine. the current model simultaneously supports chinese and english recognition, has a large number of parameters, and features language model performance enhancement. it greatly improves recognition accuracy for low-quality audio such as loud noise, strong echo, low voice volume, and voice from far away.

**Advanced language engine:**.
-"zh-dialect": chinese dialect.
-"zh-yue": cantonese in china.
-"Vi": "vietnamese.".
-"Ja": "japanese.".
-"Ko": "korean.".
-"id": "indonesian".
-"Th": thai.
-"pt": portuguese.
-"tr": "turkish.".
-"Ar": "arabic".
-"es": "spanish".
-"Hi": "hindi".
-"Fr": "french.".
-"ms": malay.
-"Fil": filipino.
-"de": german.
-`It`: italian.
-"Ru": russian.
-"sv": "swedish.".
-"Da": "danish.".
-"No": norwegian.

**Note**:.
If the language you need is not available, contact our technical staff.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        r"""**Fuzzy recognition is an advanced edition capacity, charged as advanced edition by default, and only supports filling in basic version and advanced edition language.**.
Note: does not support entering "zh-dialect".
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def HotWordList(self):
        r"""Hot word list: this parameter is used for improving recognition accuracy. each hot word is limited to "term|weight", with no more than 30 characters (a maximum of 10 chinese characters) per term. weight ranges from 1 to 11 or 100, for example: "tencent cloud|5" or "ASR|11". hot word list limitation: multiple terms separated by commas, supports up to 300 hot words, for example: "tencent cloud|10, speech recognition|5, ASR|11".
        :rtype: str
        """
        return self._HotWordList

    @HotWordList.setter
    def HotWordList(self, HotWordList):
        self._HotWordList = HotWordList

    @property
    def VadSilenceTime(self):
        r"""Specifies the time when automatic speech recognition (asr) vad is active. value range: 240-2000. default: 1000. unit: ms. a smaller value enables faster speech recognition sentence segmentation.
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def VadLevel(self):
        r"""The vad far-field voice suppression capacity (does not impact asr recognition performance) ranges from 0 to 3, with a default value of 0. recommended setting is 2 for better far-field voice suppression.
        :rtype: int
        """
        return self._VadLevel

    @VadLevel.setter
    def VadLevel(self, VadLevel):
        self._VadLevel = VadLevel


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._HotWordList = params.get("HotWordList")
        self._VadSilenceTime = params.get("VadSilenceTime")
        self._VadLevel = params.get("VadLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParams(AbstractModel):
    r"""The on-cloud recording parameters.

    """

    def __init__(self):
        r"""
        :param _RecordMode: Recording mode:.
1: single stream recording, record the audio and video of the subscribed UserId in the room separately, and upload the recording files to cloud storage.
2: mixed-stream recording. mix the audio and video of the subscribed UserId in the room into an audio-video file and upload the recording file to cloud storage.
        :type RecordMode: int
        :param _MaxIdleTime: Recording stops automatically when there is no host inside the room for a duration exceeding MaxIdleTime. measurement unit: second. default value: 30 seconds. the value must be greater than or equal to 5 seconds and less than or equal to 86400 seconds (24 hours).
        :type MaxIdleTime: int
        :param _StreamType: Media stream type for recording.
0: recording audio and video streams (default).
1: record audio streams only.
2: record video stream only.
        :type StreamType: int
        :param _SubscribeStreamUserIds: Specifies the allowlist or blocklist for the subscription stream.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param _OutputFormat: Output file format (valid when stored in third-party storage such as COS). 0: (default) output file is in hls format. 1: output file format is hls+mp4. 2: output file format is hls+aac. 3: output file format is mp4. 4: output file format is aac.

This parameter is invalid when storing in VOD. when storing in VOD, set MediaType in TencentVod (https://www.tencentcloud.com/document/api/647/44055?from_cn_redirect=1#TencentVod).
        :type OutputFormat: int
        :param _AvMerge: In single-stream recording mode, determine whether to merge the user's audio and video. 0: do not merge the audio and video of a stream (default). 1: merge the audio and video of a stream into one ts. in mixed-stream recording, this parameter is not required, and the audio and video are merged by default.
        :type AvMerge: int
        :param _MaxMediaFileDuration: If the file format is aac or mp4, the system will automatically split the video file when the length limit is exceeded. measurement unit: minute. defaults to 1440 min (24h). value range: 1-1440. [single file limit is 2G. if file size exceeds 2G or recording duration exceeds 24h, the file will be automatically split.].
Hls format recording. this parameter is not effective.
        :type MaxMediaFileDuration: int
        :param _MediaId: Specify recording streams. 0: mainstream + auxiliary stream (default); 1: mainstream; 2: auxiliary stream.
        :type MediaId: int
        :param _FillType: Specifies the type of frame to fill when the upstream video stream stops:
- 0: Fill with the last frame (freeze the last video frame)
- 1: Fill with black frames
        :type FillType: int
        :param _SubscribeAbility: Specifies whether the recording task subscribes to the stream published by the Mixed Stream Robot. 

- 1: Subscribe. 
- 0: Do not subscribe (default).
> Note: 
When this option is enabled, it is recommended to use the "Subscription Allowlist." Avoid subscribing to both the stream published by the Mixed Stream Robot and the streams published by the hosts simultaneously; otherwise, it will result in audio echoing (duplicate audio) in the recorded file.
        :type SubscribeAbility: int
        """
        self._RecordMode = None
        self._MaxIdleTime = None
        self._StreamType = None
        self._SubscribeStreamUserIds = None
        self._OutputFormat = None
        self._AvMerge = None
        self._MaxMediaFileDuration = None
        self._MediaId = None
        self._FillType = None
        self._SubscribeAbility = None

    @property
    def RecordMode(self):
        r"""Recording mode:.
1: single stream recording, record the audio and video of the subscribed UserId in the room separately, and upload the recording files to cloud storage.
2: mixed-stream recording. mix the audio and video of the subscribed UserId in the room into an audio-video file and upload the recording file to cloud storage.
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def MaxIdleTime(self):
        r"""Recording stops automatically when there is no host inside the room for a duration exceeding MaxIdleTime. measurement unit: second. default value: 30 seconds. the value must be greater than or equal to 5 seconds and less than or equal to 86400 seconds (24 hours).
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def StreamType(self):
        r"""Media stream type for recording.
0: recording audio and video streams (default).
1: record audio streams only.
2: record video stream only.
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def SubscribeStreamUserIds(self):
        r"""Specifies the allowlist or blocklist for the subscription stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def OutputFormat(self):
        r"""Output file format (valid when stored in third-party storage such as COS). 0: (default) output file is in hls format. 1: output file format is hls+mp4. 2: output file format is hls+aac. 3: output file format is mp4. 4: output file format is aac.

This parameter is invalid when storing in VOD. when storing in VOD, set MediaType in TencentVod (https://www.tencentcloud.com/document/api/647/44055?from_cn_redirect=1#TencentVod).
        :rtype: int
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def AvMerge(self):
        r"""In single-stream recording mode, determine whether to merge the user's audio and video. 0: do not merge the audio and video of a stream (default). 1: merge the audio and video of a stream into one ts. in mixed-stream recording, this parameter is not required, and the audio and video are merged by default.
        :rtype: int
        """
        return self._AvMerge

    @AvMerge.setter
    def AvMerge(self, AvMerge):
        self._AvMerge = AvMerge

    @property
    def MaxMediaFileDuration(self):
        r"""If the file format is aac or mp4, the system will automatically split the video file when the length limit is exceeded. measurement unit: minute. defaults to 1440 min (24h). value range: 1-1440. [single file limit is 2G. if file size exceeds 2G or recording duration exceeds 24h, the file will be automatically split.].
Hls format recording. this parameter is not effective.
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def MediaId(self):
        r"""Specify recording streams. 0: mainstream + auxiliary stream (default); 1: mainstream; 2: auxiliary stream.
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def FillType(self):
        r"""Specifies the type of frame to fill when the upstream video stream stops:
- 0: Fill with the last frame (freeze the last video frame)
- 1: Fill with black frames
        :rtype: int
        """
        return self._FillType

    @FillType.setter
    def FillType(self, FillType):
        self._FillType = FillType

    @property
    def SubscribeAbility(self):
        r"""Specifies whether the recording task subscribes to the stream published by the Mixed Stream Robot. 

- 1: Subscribe. 
- 0: Do not subscribe (default).
> Note: 
When this option is enabled, it is recommended to use the "Subscription Allowlist." Avoid subscribing to both the stream published by the Mixed Stream Robot and the streams published by the hosts simultaneously; otherwise, it will result in audio echoing (duplicate audio) in the recorded file.
        :rtype: int
        """
        return self._SubscribeAbility

    @SubscribeAbility.setter
    def SubscribeAbility(self, SubscribeAbility):
        self._SubscribeAbility = SubscribeAbility


    def _deserialize(self, params):
        self._RecordMode = params.get("RecordMode")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._OutputFormat = params.get("OutputFormat")
        self._AvMerge = params.get("AvMerge")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._MediaId = params.get("MediaId")
        self._FillType = params.get("FillType")
        self._SubscribeAbility = params.get("SubscribeAbility")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdRequest(AbstractModel):
    r"""RemoveUserByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param _RoomId: Room ID
        :type RoomId: str
        :param _UserIds: List of up to 10 users to be removed
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        r"""`SDKAppId` of TRTC
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        r"""List of up to 10 users to be removed
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    r"""RemoveUserByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    r"""RemoveUser request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param _RoomId: Room number.
        :type RoomId: int
        :param _UserIds: List of up to 10 users to be removed.
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        r"""`SDKAppId` of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""Room number.
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        r"""List of up to 10 users to be removed.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    r"""RemoveUser response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    r"""The room information.

    """

    def __init__(self):
        r"""
        :param _CommId: The call ID, which uniquely identifies a call.
        :type CommId: str
        :param _RoomString: The room ID.
        :type RoomString: str
        :param _CreateTime: The room creation time.
        :type CreateTime: int
        :param _DestroyTime: The room termination time.
        :type DestroyTime: int
        :param _IsFinished: Whether the room is terminated.
        :type IsFinished: bool
        :param _UserId: The user ID of the room creator.
        :type UserId: str
        """
        self._CommId = None
        self._RoomString = None
        self._CreateTime = None
        self._DestroyTime = None
        self._IsFinished = None
        self._UserId = None

    @property
    def CommId(self):
        r"""The call ID, which uniquely identifies a call.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def RoomString(self):
        r"""The room ID.
        :rtype: str
        """
        return self._RoomString

    @RoomString.setter
    def RoomString(self, RoomString):
        self._RoomString = RoomString

    @property
    def CreateTime(self):
        r"""The room creation time.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DestroyTime(self):
        r"""The room termination time.
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def IsFinished(self):
        r"""Whether the room is terminated.
        :rtype: bool
        """
        return self._IsFinished

    @IsFinished.setter
    def IsFinished(self, IsFinished):
        self._IsFinished = IsFinished

    @property
    def UserId(self):
        r"""The user ID of the room creator.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._RoomString = params.get("RoomString")
        self._CreateTime = params.get("CreateTime")
        self._DestroyTime = params.get("DestroyTime")
        self._IsFinished = params.get("IsFinished")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowValues(AbstractModel):
    r"""Two-dimensional array of SeriesInfo type

    """

    def __init__(self):
        r"""
        :param _RowValue: Data value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowValue: list of int
        :param _RowValueFloat: Data value.
        :type RowValueFloat: list of float
        """
        self._RowValue = None
        self._RowValueFloat = None

    @property
    def RowValue(self):
        r"""Data value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._RowValue

    @RowValue.setter
    def RowValue(self, RowValue):
        self._RowValue = RowValue

    @property
    def RowValueFloat(self):
        r"""Data value.
        :rtype: list of float
        """
        return self._RowValueFloat

    @RowValueFloat.setter
    def RowValueFloat(self, RowValueFloat):
        self._RowValueFloat = RowValueFloat


    def _deserialize(self, params):
        self._RowValue = params.get("RowValue")
        self._RowValueFloat = params.get("RowValueFloat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class STTConfig(AbstractModel):
    r"""Convert speech to text parameter.

    """

    def __init__(self):
        r"""
        :param _Language: Convert speech to text supported languages, "zh" chinese is selected by default.

You can unlock different languages by purchasing the "AI intelligent recognition duration package" or claiming the trial version of the monthly subscription package. 

Supported languages for different speech to text package versions are as follows:.

- "zh": chinese (simplified).
- "zh-TW": chinese (traditional).
- "en": english.
- "zh-yue": cantonese in china.
- "vi": "vietnamese.".
- "ja": "japanese.".
- "ko": "korean.".
- "id": "indonesian".
- "th": thai.
- "pt": portuguese.
- "tr": "turkish.".
- "ar": "arabic".
- "es": "spanish".
- "hi": "hindi".
- "ft": "french.".
- "ms": malay.
- "fil": filipino.
- "de": german.
-`it`: italian.
- "ru": russian.
- "sv": "swedish.".
- "da": "danish.".
- "no": norwegian.
- "pl": polski.
-"af-ZA": afrikaans.
- "nl-NL": dutch.
- "nl-BE": flemish.
- "uz": uzbek.
- "hu": hungarian.
- "he": hebrew.
- "ur": urdu.

**Note**:.
If the language you need is not available, contact our technical staff.
        :type Language: str
        :param _AlternativeLanguage: **Fuzzy recognition is an advanced edition capacity, charged by default as the advanced edition.**.
        :type AlternativeLanguage: list of str
        :param _CustomParam: Custom parameter. contact for background usage.

        :type CustomParam: str
        :param _VadSilenceTime: Specifies the time when automatic speech recognition (asr) vad is active. value range: 240-2000. default: 1000. unit: ms. a smaller value enables faster speech recognition sentence segmentation.
        :type VadSilenceTime: int
        :param _VadLevel: The vad far-field voice suppression capacity (without impacting asr recognition performance) ranges from 0 to 5, with a default value of 0, indicating disabled far-field voice suppression. the recommended setting is 2 for better far-field voice suppression. in a noisy office environment, it can be set to 3, and in more noisy environments, 4 and 5 are available for use. note that a higher VadLevel may suppress single words as noise.
        :type VadLevel: int
        """
        self._Language = None
        self._AlternativeLanguage = None
        self._CustomParam = None
        self._VadSilenceTime = None
        self._VadLevel = None

    @property
    def Language(self):
        r"""Convert speech to text supported languages, "zh" chinese is selected by default.

You can unlock different languages by purchasing the "AI intelligent recognition duration package" or claiming the trial version of the monthly subscription package. 

Supported languages for different speech to text package versions are as follows:.

- "zh": chinese (simplified).
- "zh-TW": chinese (traditional).
- "en": english.
- "zh-yue": cantonese in china.
- "vi": "vietnamese.".
- "ja": "japanese.".
- "ko": "korean.".
- "id": "indonesian".
- "th": thai.
- "pt": portuguese.
- "tr": "turkish.".
- "ar": "arabic".
- "es": "spanish".
- "hi": "hindi".
- "ft": "french.".
- "ms": malay.
- "fil": filipino.
- "de": german.
-`it`: italian.
- "ru": russian.
- "sv": "swedish.".
- "da": "danish.".
- "no": norwegian.
- "pl": polski.
-"af-ZA": afrikaans.
- "nl-NL": dutch.
- "nl-BE": flemish.
- "uz": uzbek.
- "hu": hungarian.
- "he": hebrew.
- "ur": urdu.

**Note**:.
If the language you need is not available, contact our technical staff.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        r"""**Fuzzy recognition is an advanced edition capacity, charged by default as the advanced edition.**.
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def CustomParam(self):
        r"""Custom parameter. contact for background usage.

        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def VadSilenceTime(self):
        r"""Specifies the time when automatic speech recognition (asr) vad is active. value range: 240-2000. default: 1000. unit: ms. a smaller value enables faster speech recognition sentence segmentation.
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def VadLevel(self):
        r"""The vad far-field voice suppression capacity (without impacting asr recognition performance) ranges from 0 to 5, with a default value of 0, indicating disabled far-field voice suppression. the recommended setting is 2 for better far-field voice suppression. in a noisy office environment, it can be set to 3, and in more noisy environments, 4 and 5 are available for use. note that a higher VadLevel may suppress single words as noise.
        :rtype: int
        """
        return self._VadLevel

    @VadLevel.setter
    def VadLevel(self, VadLevel):
        self._VadLevel = VadLevel


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._CustomParam = params.get("CustomParam")
        self._VadSilenceTime = params.get("VadSilenceTime")
        self._VadLevel = params.get("VadLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInfomation(AbstractModel):
    r"""The room and user number.

    """

    def __init__(self):
        r"""
        :param _Time: Start time for each day
        :type Time: int
        :param _UserNumber: The number of users. If a user enters a room multiple times, it will be counted as one user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserNumber: int
        :param _UserCount: The number of room entries. Every time a user enters a room, it will be counted as one room entry.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserCount: int
        :param _RoomNumbers: The total number of rooms of the application on a day.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomNumbers: int
        """
        self._Time = None
        self._UserNumber = None
        self._UserCount = None
        self._RoomNumbers = None

    @property
    def Time(self):
        r"""Start time for each day
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserNumber(self):
        r"""The number of users. If a user enters a room multiple times, it will be counted as one user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber

    @property
    def UserCount(self):
        r"""The number of room entries. Every time a user enters a room, it will be counted as one room entry.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def RoomNumbers(self):
        r"""The total number of rooms of the application on a day.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RoomNumbers

    @RoomNumbers.setter
    def RoomNumbers(self, RoomNumbers):
        self._RoomNumbers = RoomNumbers


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._UserNumber = params.get("UserNumber")
        self._UserCount = params.get("UserCount")
        self._RoomNumbers = params.get("RoomNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeriesInfos(AbstractModel):
    r"""SeriesInfos type

    """

    def __init__(self):
        r"""
        :param _Columns: Data column
Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of str
        :param _Values: Data value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Values: list of RowValues
        """
        self._Columns = None
        self._Values = None

    @property
    def Columns(self):
        r"""Data column
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Values(self):
        r"""Data value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RowValues
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Columns = params.get("Columns")
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = RowValues()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerPushText(AbstractModel):
    r"""The server controls the chatbot to broadcast the specified text.

    """

    def __init__(self):
        r"""
        :param _Text: Server push broadcast text.
        :type Text: str
        :param _Interrupt: Whether to allow the text to interrupt the robot's speaking.
        :type Interrupt: bool
        :param _StopAfterPlay: Broadcast the text and automatically close the dialogue task.
        :type StopAfterPlay: bool
        :param _Audio: Server push broadcast audio.
Format description: audio must be mono, sampling rate must be consistent with the corresponding TTS sampling rate, and coded as a Base64 string.
Input rule: when the Audio field is provided, the system will not accept user-submitted input in the Text field. the system will play the Audio content in the Audio field directly.
        :type Audio: str
        :param _DropMode: Defaults to 0. valid at that time only when Interrupt is false.
-0 means drop messages with Interrupt set to false during the occurrence of interaction.
-1 indicates that during the occurrence of an interaction, messages with Interrupt as false will not be dropped but cached, waiting to be processed when finished.

Note: if DropMode is 1, multiple messages can be cached. if an interruption occurs subsequently, the cache of messages will be cleared.
        :type DropMode: int
        :param _Priority: The message priority of ServerPushText. 0 means interruptible, 1 means not interruptible. currently only support 0. if you need to input 1, submit a ticket to contact us to grant permission.
Note: after receiving a message with Priority=1, any other messages will be ignored (including messages with Priority=1) until the message processing of Priority=1 is complete. this field can be used together with the Interrupt and DropMode fields.
Example:.
-Priority=1, Interrupt=true, interrupts existing interaction and broadcasts immediately. the broadcast will not be interrupted during the process.
-Priority=1, Interrupt=false, DropMode=1. wait for the current interaction to complete before broadcasting. the broadcast will not be interrupted during the process.

        :type Priority: int
        :param _AddHistory: Whether to add the text to the llm history context.
        :type AddHistory: bool
        :param _MetaInfo: If filled, it will be bound to the subtitle and sent to the terminal. note that the content must be a json string.
        :type MetaInfo: str
        """
        self._Text = None
        self._Interrupt = None
        self._StopAfterPlay = None
        self._Audio = None
        self._DropMode = None
        self._Priority = None
        self._AddHistory = None
        self._MetaInfo = None

    @property
    def Text(self):
        r"""Server push broadcast text.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Interrupt(self):
        r"""Whether to allow the text to interrupt the robot's speaking.
        :rtype: bool
        """
        return self._Interrupt

    @Interrupt.setter
    def Interrupt(self, Interrupt):
        self._Interrupt = Interrupt

    @property
    def StopAfterPlay(self):
        r"""Broadcast the text and automatically close the dialogue task.
        :rtype: bool
        """
        return self._StopAfterPlay

    @StopAfterPlay.setter
    def StopAfterPlay(self, StopAfterPlay):
        self._StopAfterPlay = StopAfterPlay

    @property
    def Audio(self):
        r"""Server push broadcast audio.
Format description: audio must be mono, sampling rate must be consistent with the corresponding TTS sampling rate, and coded as a Base64 string.
Input rule: when the Audio field is provided, the system will not accept user-submitted input in the Text field. the system will play the Audio content in the Audio field directly.
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def DropMode(self):
        r"""Defaults to 0. valid at that time only when Interrupt is false.
-0 means drop messages with Interrupt set to false during the occurrence of interaction.
-1 indicates that during the occurrence of an interaction, messages with Interrupt as false will not be dropped but cached, waiting to be processed when finished.

Note: if DropMode is 1, multiple messages can be cached. if an interruption occurs subsequently, the cache of messages will be cleared.
        :rtype: int
        """
        return self._DropMode

    @DropMode.setter
    def DropMode(self, DropMode):
        self._DropMode = DropMode

    @property
    def Priority(self):
        r"""The message priority of ServerPushText. 0 means interruptible, 1 means not interruptible. currently only support 0. if you need to input 1, submit a ticket to contact us to grant permission.
Note: after receiving a message with Priority=1, any other messages will be ignored (including messages with Priority=1) until the message processing of Priority=1 is complete. this field can be used together with the Interrupt and DropMode fields.
Example:.
-Priority=1, Interrupt=true, interrupts existing interaction and broadcasts immediately. the broadcast will not be interrupted during the process.
-Priority=1, Interrupt=false, DropMode=1. wait for the current interaction to complete before broadcasting. the broadcast will not be interrupted during the process.

        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def AddHistory(self):
        r"""Whether to add the text to the llm history context.
        :rtype: bool
        """
        return self._AddHistory

    @AddHistory.setter
    def AddHistory(self, AddHistory):
        self._AddHistory = AddHistory

    @property
    def MetaInfo(self):
        r"""If filled, it will be bound to the subtitle and sent to the terminal. note that the content must be a json string.
        :rtype: str
        """
        return self._MetaInfo

    @MetaInfo.setter
    def MetaInfo(self, MetaInfo):
        self._MetaInfo = MetaInfo


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Interrupt = params.get("Interrupt")
        self._StopAfterPlay = params.get("StopAfterPlay")
        self._Audio = params.get("Audio")
        self._DropMode = params.get("DropMode")
        self._Priority = params.get("Priority")
        self._AddHistory = params.get("AddHistory")
        self._MetaInfo = params.get("MetaInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedByStrRoomIdRequest(AbstractModel):
    r"""SetUserBlockedByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _StrRoomId: The room ID (string).
        :type StrRoomId: str
        :param _UserId: The user ID.
        :type UserId: str
        :param _IsMute: Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._StrRoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        r"""The application ID.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StrRoomId(self):
        r"""The room ID (string).
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
        r"""Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :rtype: int
        """
        return self._IsMute

    @IsMute.setter
    def IsMute(self, IsMute):
        self._IsMute = IsMute


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StrRoomId = params.get("StrRoomId")
        self._UserId = params.get("UserId")
        self._IsMute = params.get("IsMute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedByStrRoomIdResponse(AbstractModel):
    r"""SetUserBlockedByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SetUserBlockedRequest(AbstractModel):
    r"""SetUserBlocked request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _RoomId: The room ID (number).
        :type RoomId: int
        :param _UserId: The user ID.
        :type UserId: str
        :param _IsMute: Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        r"""The application ID.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""The room ID (number).
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
        r"""Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :rtype: int
        """
        return self._IsMute

    @IsMute.setter
    def IsMute(self, IsMute):
        self._IsMute = IsMute


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._IsMute = params.get("IsMute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedResponse(AbstractModel):
    r"""SetUserBlocked response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SingleSubscribeParams(AbstractModel):
    r"""The information of a single stream relayed.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        r"""The stream information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SliceParams(AbstractModel):
    r"""Control parameters for cloud slicing.

    """

    def __init__(self):
        r"""
        :param _SliceType: Slicing task type.
1: audio slicing;
2: video frame extraction;
3: audio/video slicing + video frame extraction.
Example value: 1.
        :type SliceType: int
        :param _MaxIdleTime: Recording is stopped automatically when there is no anchor in the room for more than MaxIdleTime. Unit: seconds. Default value: 30 seconds. This value needs to be greater than or equal to 5 seconds and less than or equal to 86,400 seconds (24 hours).
Example value: 30.
        :type MaxIdleTime: int
        :param _SliceAudio: Audio slicing duration. Default value: 15s. Example value: 15.
        :type SliceAudio: int
        :param _SliceVideo: Interval for video frame extraction. Default value: 5s. Example value: 5.
        :type SliceVideo: int
        :param _SubscribeStreamUserIds: Specifies the allowlist or blocklist for the subscription stream.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param _SliceCallbackUrl: Depreciated. The callback URL is configured in the console.
        :type SliceCallbackUrl: str
        """
        self._SliceType = None
        self._MaxIdleTime = None
        self._SliceAudio = None
        self._SliceVideo = None
        self._SubscribeStreamUserIds = None
        self._SliceCallbackUrl = None

    @property
    def SliceType(self):
        r"""Slicing task type.
1: audio slicing;
2: video frame extraction;
3: audio/video slicing + video frame extraction.
Example value: 1.
        :rtype: int
        """
        return self._SliceType

    @SliceType.setter
    def SliceType(self, SliceType):
        self._SliceType = SliceType

    @property
    def MaxIdleTime(self):
        r"""Recording is stopped automatically when there is no anchor in the room for more than MaxIdleTime. Unit: seconds. Default value: 30 seconds. This value needs to be greater than or equal to 5 seconds and less than or equal to 86,400 seconds (24 hours).
Example value: 30.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def SliceAudio(self):
        r"""Audio slicing duration. Default value: 15s. Example value: 15.
        :rtype: int
        """
        return self._SliceAudio

    @SliceAudio.setter
    def SliceAudio(self, SliceAudio):
        self._SliceAudio = SliceAudio

    @property
    def SliceVideo(self):
        r"""Interval for video frame extraction. Default value: 5s. Example value: 5.
        :rtype: int
        """
        return self._SliceVideo

    @SliceVideo.setter
    def SliceVideo(self, SliceVideo):
        self._SliceVideo = SliceVideo

    @property
    def SubscribeStreamUserIds(self):
        r"""Specifies the allowlist or blocklist for the subscription stream.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def SliceCallbackUrl(self):
        r"""Depreciated. The callback URL is configured in the console.
        :rtype: str
        """
        return self._SliceCallbackUrl

    @SliceCallbackUrl.setter
    def SliceCallbackUrl(self, SliceCallbackUrl):
        self._SliceCallbackUrl = SliceCallbackUrl


    def _deserialize(self, params):
        self._SliceType = params.get("SliceType")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._SliceAudio = params.get("SliceAudio")
        self._SliceVideo = params.get("SliceVideo")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._SliceCallbackUrl = params.get("SliceCallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SliceStorageParams(AbstractModel):
    r"""Storage parameters for the slicing files.

    """

    def __init__(self):
        r"""
        :param _CloudSliceStorage: Information about Tencent COS and third-party cloud storage accounts.
        :type CloudSliceStorage: :class:`tencentcloud.trtc.v20190722.models.CloudSliceStorage`
        """
        self._CloudSliceStorage = None

    @property
    def CloudSliceStorage(self):
        r"""Information about Tencent COS and third-party cloud storage accounts.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudSliceStorage`
        """
        return self._CloudSliceStorage

    @CloudSliceStorage.setter
    def CloudSliceStorage(self, CloudSliceStorage):
        self._CloudSliceStorage = CloudSliceStorage


    def _deserialize(self, params):
        if params.get("CloudSliceStorage") is not None:
            self._CloudSliceStorage = CloudSliceStorage()
            self._CloudSliceStorage._deserialize(params.get("CloudSliceStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationRequest(AbstractModel):
    r"""StartAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId used by the room with transcription task enabled.
        :type SdkAppId: int
        :param _RoomId: [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC refers to the room number that enables the conversation task.
        :type RoomId: str
        :param _AgentConfig: Bot parameters.
        :type AgentConfig: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        :param _SessionId: The unique Id passed by the caller can be used to prevent duplication of task initiation on the client side as well as query task status through this field.
        :type SessionId: str
        :param _RoomIdType: Type of the TRTC room number. 0 indicates digit room number, 1 indicates string room number. by default if left blank, it is digit room number.
        :type RoomIdType: int
        :param _STTConfig: Speech recognition configuration.
        :type STTConfig: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        :param _LLMConfig: Required parameter, LLM configuration. it must comply with the openai standard and be a JSON String. example: <pre> { <br> &emsp;  "LLMType": "Model type",  // String required, for example: "openai" <br> &emsp;  "Model": "your Model name", // String required, specifies the Model to be used<br>    "APIKey": "your LLM API key", // String required <br> &emsp;  "APIUrl": "https://API.xxx.com/chat/completions", // String required, the URL for LLM API access<br> &emsp;  "History": 10, // Integer optional, sets the context rounds for LLM, default value is 0, maximum value is 50<br> &emsp;  "HistoryMode": 1, // Integer optional, 1 means the content in the LLM context will synchronize with playback audio, and text corresponding to unplayed audio will not appear in the context. 0 means no synchronization, default value is 0<br> &emsp;  "Streaming": true // Boolean optional, whether to use Streaming<br> &emsp;} </pre>.
        :type LLMConfig: str
        :param _TTSConfig: Required parameter, TTS configuration. it is a JSON string: TRTC TTS configuration as follows:.  
<pre> { <br> &emsp;  "TTSType": "flow",  // [required] fixed to this value.  <br> &emsp;  "VoiceId": "v-female-R2s4N9qJ", // [required] premium timbre ID/clone voice ID. selectable different timbres. refer to the following timbre list for ID library.   <br> &emsp;  "Model": "flow_01_turbo", // (required) current default TTS Model version (corresponds to Flash version).  <br> &emsp;  "Speed": 1.0,    // [option] adjust the speaking rate. value range [0.5-2.0]. default 1.0. the larger the value, the faster the speech speed. <br> &emsp;  "Volume": 1.0,   // [optional] adjust volume [0,10]. default: 1.0. a larger value indicates higher volume.   <br> &emsp;  "Pitch": 0,   // [optional] adjusts the tone [-12,12]. default value is 0. among them, 0 outputs the original voice type. <br> &emsp;  "Language": "zh" // [optional] recommend filling in. currently supports filling in chinese: zh, english: en, cantonese dialect: yue. parameter reference: (ISO 639-1). <br> &emsp;} </pre>
        :type TTSConfig: str
        :param _ExperimentalParams: Experimental parameter, contact for background usage.
        :type ExperimentalParams: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._AgentConfig = None
        self._SessionId = None
        self._RoomIdType = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None
        self._ExperimentalParams = None

    @property
    def SdkAppId(self):
        r"""[SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId used by the room with transcription task enabled.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""[RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC refers to the room number that enables the conversation task.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AgentConfig(self):
        r"""Bot parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        """
        return self._AgentConfig

    @AgentConfig.setter
    def AgentConfig(self, AgentConfig):
        self._AgentConfig = AgentConfig

    @property
    def SessionId(self):
        r"""The unique Id passed by the caller can be used to prevent duplication of task initiation on the client side as well as query task status through this field.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        r"""Type of the TRTC room number. 0 indicates digit room number, 1 indicates string room number. by default if left blank, it is digit room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def STTConfig(self):
        r"""Speech recognition configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        r"""Required parameter, LLM configuration. it must comply with the openai standard and be a JSON String. example: <pre> { <br> &emsp;  "LLMType": "Model type",  // String required, for example: "openai" <br> &emsp;  "Model": "your Model name", // String required, specifies the Model to be used<br>    "APIKey": "your LLM API key", // String required <br> &emsp;  "APIUrl": "https://API.xxx.com/chat/completions", // String required, the URL for LLM API access<br> &emsp;  "History": 10, // Integer optional, sets the context rounds for LLM, default value is 0, maximum value is 50<br> &emsp;  "HistoryMode": 1, // Integer optional, 1 means the content in the LLM context will synchronize with playback audio, and text corresponding to unplayed audio will not appear in the context. 0 means no synchronization, default value is 0<br> &emsp;  "Streaming": true // Boolean optional, whether to use Streaming<br> &emsp;} </pre>.
        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""Required parameter, TTS configuration. it is a JSON string: TRTC TTS configuration as follows:.  
<pre> { <br> &emsp;  "TTSType": "flow",  // [required] fixed to this value.  <br> &emsp;  "VoiceId": "v-female-R2s4N9qJ", // [required] premium timbre ID/clone voice ID. selectable different timbres. refer to the following timbre list for ID library.   <br> &emsp;  "Model": "flow_01_turbo", // (required) current default TTS Model version (corresponds to Flash version).  <br> &emsp;  "Speed": 1.0,    // [option] adjust the speaking rate. value range [0.5-2.0]. default 1.0. the larger the value, the faster the speech speed. <br> &emsp;  "Volume": 1.0,   // [optional] adjust volume [0,10]. default: 1.0. a larger value indicates higher volume.   <br> &emsp;  "Pitch": 0,   // [optional] adjusts the tone [-12,12]. default value is 0. among them, 0 outputs the original voice type. <br> &emsp;  "Language": "zh" // [optional] recommend filling in. currently supports filling in chinese: zh, english: en, cantonese dialect: yue. parameter reference: (ISO 639-1). <br> &emsp;} </pre>
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def ExperimentalParams(self):
        r"""Experimental parameter, contact for background usage.
        :rtype: str
        """
        return self._ExperimentalParams

    @ExperimentalParams.setter
    def ExperimentalParams(self, ExperimentalParams):
        self._ExperimentalParams = ExperimentalParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("AgentConfig") is not None:
            self._AgentConfig = AgentConfig()
            self._AgentConfig._deserialize(params.get("AgentConfig"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("STTConfig") is not None:
            self._STTConfig = STTConfig()
            self._STTConfig._deserialize(params.get("STTConfig"))
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        self._ExperimentalParams = params.get("ExperimentalParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationResponse(AbstractModel):
    r"""StartAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: For uniquely identifying a conversation task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""For uniquely identifying a conversation task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartAITranscriptionRequest(AbstractModel):
    r"""StartAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId used by the room with transcription task enabled.
        :type SdkAppId: int
        :param _RoomId: [RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC refers to the room number that enables the transcription task.
        :type RoomId: str
        :param _TranscriptionParams: Transcription robot parameters.
        :type TranscriptionParams: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        :param _SessionId: Unique Id passed by the caller, used by the server for task deduplication. duplicate tasks will fail to initiate. the server uses SdkAppId+RoomId+RoomIdType+RobotUserId for deduplication by default. if SessionId is provided, it will also be used for deduplication.
Note:.
When TranscriptionMode is 0, ensure only one task is initiated in a room. if multiple tasks are initiated, robots will subscribe to each other. unless the task is stopped proactively, it will timeout exit after 10 hours. in such cases, it is advisable to fill in SessionId to ensure subsequent repeated tasks fail.
        :type SessionId: str
        :param _RoomIdType: Type of the TRTC room number. 0 indicates digit room number, 1 indicates string room number. by default if left blank, it is digit room number.
        :type RoomIdType: int
        :param _RecognizeConfig: Speech recognition configuration.
        :type RecognizeConfig: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        :param _TranslationConfig: Translate configuration details.
        :type TranslationConfig: :class:`tencentcloud.trtc.v20190722.models.TranslationConfig`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TranscriptionParams = None
        self._SessionId = None
        self._RoomIdType = None
        self._RecognizeConfig = None
        self._TranslationConfig = None

    @property
    def SdkAppId(self):
        r"""[SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId used by the room with transcription task enabled.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""[RoomId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#RoomId) of TRTC refers to the room number that enables the transcription task.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TranscriptionParams(self):
        r"""Transcription robot parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        """
        return self._TranscriptionParams

    @TranscriptionParams.setter
    def TranscriptionParams(self, TranscriptionParams):
        self._TranscriptionParams = TranscriptionParams

    @property
    def SessionId(self):
        r"""Unique Id passed by the caller, used by the server for task deduplication. duplicate tasks will fail to initiate. the server uses SdkAppId+RoomId+RoomIdType+RobotUserId for deduplication by default. if SessionId is provided, it will also be used for deduplication.
Note:.
When TranscriptionMode is 0, ensure only one task is initiated in a room. if multiple tasks are initiated, robots will subscribe to each other. unless the task is stopped proactively, it will timeout exit after 10 hours. in such cases, it is advisable to fill in SessionId to ensure subsequent repeated tasks fail.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        r"""Type of the TRTC room number. 0 indicates digit room number, 1 indicates string room number. by default if left blank, it is digit room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def RecognizeConfig(self):
        r"""Speech recognition configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        """
        return self._RecognizeConfig

    @RecognizeConfig.setter
    def RecognizeConfig(self, RecognizeConfig):
        self._RecognizeConfig = RecognizeConfig

    @property
    def TranslationConfig(self):
        r"""Translate configuration details.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranslationConfig`
        """
        return self._TranslationConfig

    @TranslationConfig.setter
    def TranslationConfig(self, TranslationConfig):
        self._TranslationConfig = TranslationConfig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("TranscriptionParams") is not None:
            self._TranscriptionParams = TranscriptionParams()
            self._TranscriptionParams._deserialize(params.get("TranscriptionParams"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("RecognizeConfig") is not None:
            self._RecognizeConfig = RecognizeConfig()
            self._RecognizeConfig._deserialize(params.get("RecognizeConfig"))
        if params.get("TranslationConfig") is not None:
            self._TranslationConfig = TranslationConfig()
            self._TranslationConfig._deserialize(params.get("TranslationConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAITranscriptionResponse(AbstractModel):
    r"""StartAITranscription response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: For unique identification of transcription task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""For unique identification of transcription task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartPublishCdnStreamRequest(AbstractModel):
    r"""StartPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: [SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId corresponding to the relayed room.
        :type SdkAppId: int
        :param _RoomId: Main room information RoomId, the RoomId corresponding to the TRTC room for relay.
        :type RoomId: str
        :param _RoomIdType: Main room information RoomType must be the same as the RoomId type of the relayed room. 0 indicates integer type room id, and 1 indicates string room number.
        :type RoomIdType: int
        :param _AgentParams: Relay service bot parameters for joining TRTC room.
        :type AgentParams: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        :param _WithTranscoding: Whether to transcode. 0 indicates no need to transcode, 1 indicates requirement to transcode. whether to charge transcoding fee is determined by the WithTranscoding parameter. WithTranscoding set to 0 means bypass forwarding and no transcoding costs will be incurred. WithTranscoding set to 1 means mixed-stream relay and transcoding costs will be charged.
Note: transcoding is required for stream mixing, and this parameter must be set to 1.
        :type WithTranscoding: int
        :param _AudioParams: Audio encoding parameters for stream retransmission. since audio must be transcoded (no transcoding costs will be incurred), this field is required when starting a task.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: Video encoding parameters for the relay stream. leave blank for audio-only relay.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: The user uplink parameters require single stream bypass forwarding. WithTranscoding needs to be set to 0 for single stream bypass forwarding.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: The CDN parameters for relay push support up to 10 push urls for a task. there must be one pushback room parameter.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: Stream mixing SEI parameter.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: Push back room information. a task supports up to 10 push rooms, and there must be one forward CDN parameter. note: use SDK version 10.4 or higher to push room. if you need assistance, contact tencent cloud technical support.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        :param _RecordParams: Relay recording parameters. refer to the reference document (https://www.tencentcloud.com/document/product/647/111748?from_cn_redirect=1).
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.McuRecordParams`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._AgentParams = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None
        self._RecordParams = None

    @property
    def SdkAppId(self):
        r"""[SdkAppId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#SdkAppId) of TRTC, which is the same as the SdkAppId corresponding to the relayed room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""Main room information RoomId, the RoomId corresponding to the TRTC room for relay.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""Main room information RoomType must be the same as the RoomId type of the relayed room. 0 indicates integer type room id, and 1 indicates string room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def AgentParams(self):
        r"""Relay service bot parameters for joining TRTC room.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        """
        return self._AgentParams

    @AgentParams.setter
    def AgentParams(self, AgentParams):
        self._AgentParams = AgentParams

    @property
    def WithTranscoding(self):
        r"""Whether to transcode. 0 indicates no need to transcode, 1 indicates requirement to transcode. whether to charge transcoding fee is determined by the WithTranscoding parameter. WithTranscoding set to 0 means bypass forwarding and no transcoding costs will be incurred. WithTranscoding set to 1 means mixed-stream relay and transcoding costs will be charged.
Note: transcoding is required for stream mixing, and this parameter must be set to 1.
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        r"""Audio encoding parameters for stream retransmission. since audio must be transcoded (no transcoding costs will be incurred), this field is required when starting a task.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        r"""Video encoding parameters for the relay stream. leave blank for audio-only relay.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        r"""The user uplink parameters require single stream bypass forwarding. WithTranscoding needs to be set to 0 for single stream bypass forwarding.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        r"""The CDN parameters for relay push support up to 10 push urls for a task. there must be one pushback room parameter.
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        r"""Stream mixing SEI parameter.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        r"""Push back room information. a task supports up to 10 push rooms, and there must be one forward CDN parameter. note: use SDK version 10.4 or higher to push room. if you need assistance, contact tencent cloud technical support.
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams

    @property
    def RecordParams(self):
        r"""Relay recording parameters. refer to the reference document (https://www.tencentcloud.com/document/product/647/111748?from_cn_redirect=1).
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuRecordParams`
        """
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("AgentParams") is not None:
            self._AgentParams = AgentParams()
            self._AgentParams._deserialize(params.get("AgentParams"))
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        if params.get("RecordParams") is not None:
            self._RecordParams = McuRecordParams()
            self._RecordParams._deserialize(params.get("RecordParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishCdnStreamResponse(AbstractModel):
    r"""StartPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Used to uniquely identify the forwarding task, generated by the tencent cloud server. you need to carry the TaskID parameter for follow-up updates and to stop the request.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Used to uniquely identify the forwarding task, generated by the tencent cloud server. you need to carry the TaskID parameter for follow-up updates and to stop the request.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartStreamIngestRequest(AbstractModel):
    r"""StartStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#sdkappid), the same as the SdkAppId corresponding to the Record room.
        :type SdkAppId: int
        :param _RoomId: TRTC's [RoomId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#roomid), the RoomId corresponding to the Record TRTC room.
        :type RoomId: str
        :param _RoomIdType: Type of TRTC RoomId. [*Note] Must be the same as the RoomId type corresponding to the Record room: 0: String type RoomId 1: 32-bit Integer type RoomId (default)
        :type RoomIdType: int
        :param _UserId: UserId of the Pull stream Relay Robot, used to enter the room and initiate the Pull stream Relay Task.
        :type UserId: str
        :param _UserSig: UserSig corresponding to the Pull stream Relay Robot UserId, i.e., UserId and UserSig are equivalent to the Robot's Login password for entering the room. For the specific Calculation method, please refer to the TRTC [UserSig](https://www.tencentcloud.com/zh/document/product/647/39074) Scheme.
        :type UserSig: str
        :param _StreamUrl: The Url of the media resource.
        :type StreamUrl: str
        :param _PrivateMapKey: TRTC room permission Encryption ticket, only needed when advanced permission control is enabled in the Console. After enabling advanced permission control in the TRTC Console, TRTC's backend service system will verify a so-called [PrivateMapKey] 'Permission ticket', which contains an encrypted RoomId and an encrypted 'Permission bit list'. Since PrivateMapKey contains RoomId, providing only UserSig without PrivateMapKey does not allow entry into the specified room.
        :type PrivateMapKey: str
        :param _VideoEncodeParams: Video Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type VideoEncodeParams: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        :param _AudioEncodeParams: Audio Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type AudioEncodeParams: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        :param _SourceUrl: 	
Source URL. Example value: https://a.b/test.mp4
        :type SourceUrl: list of str
        :param _SeekSecond: Specify that the video plays from a specific second timestamp.
        :type SeekSecond: int
        :param _AutoPush: Enable auto relay to cdn, please make sure that this feature has been enabled in the console.
        :type AutoPush: bool
        :param _RepeatNum: Loop playback count, value range: [-1, 1000], default is 1 time. - 0 is an invalid value - -1 is for loop playback, task termination requires actively calling the stop interface or setting MaxDuration.
        :type RepeatNum: int
        :param _MaxDuration: Loop playback maximum duration, only effective when RepeatNum is set to -1, valid value range: [1, 10080], unit: minutes
        :type MaxDuration: int
        :param _Volume: Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :type Volume: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None
        self._StreamUrl = None
        self._PrivateMapKey = None
        self._VideoEncodeParams = None
        self._AudioEncodeParams = None
        self._SourceUrl = None
        self._SeekSecond = None
        self._AutoPush = None
        self._RepeatNum = None
        self._MaxDuration = None
        self._Volume = None

    @property
    def SdkAppId(self):
        r"""TRTC's [SdkAppId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#sdkappid), the same as the SdkAppId corresponding to the Record room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC's [RoomId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#roomid), the RoomId corresponding to the Record TRTC room.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""Type of TRTC RoomId. [*Note] Must be the same as the RoomId type corresponding to the Record room: 0: String type RoomId 1: 32-bit Integer type RoomId (default)
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        r"""UserId of the Pull stream Relay Robot, used to enter the room and initiate the Pull stream Relay Task.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""UserSig corresponding to the Pull stream Relay Robot UserId, i.e., UserId and UserSig are equivalent to the Robot's Login password for entering the room. For the specific Calculation method, please refer to the TRTC [UserSig](https://www.tencentcloud.com/zh/document/product/647/39074) Scheme.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def StreamUrl(self):
        r"""The Url of the media resource.
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def PrivateMapKey(self):
        r"""TRTC room permission Encryption ticket, only needed when advanced permission control is enabled in the Console. After enabling advanced permission control in the TRTC Console, TRTC's backend service system will verify a so-called [PrivateMapKey] 'Permission ticket', which contains an encrypted RoomId and an encrypted 'Permission bit list'. Since PrivateMapKey contains RoomId, providing only UserSig without PrivateMapKey does not allow entry into the specified room.
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoEncodeParams(self):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        r"""Video Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        """
        return self._VideoEncodeParams

    @VideoEncodeParams.setter
    def VideoEncodeParams(self, VideoEncodeParams):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        self._VideoEncodeParams = VideoEncodeParams

    @property
    def AudioEncodeParams(self):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        r"""Audio Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        """
        return self._AudioEncodeParams

    @AudioEncodeParams.setter
    def AudioEncodeParams(self, AudioEncodeParams):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        self._AudioEncodeParams = AudioEncodeParams

    @property
    def SourceUrl(self):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        r"""	
Source URL. Example value: https://a.b/test.mp4
        :rtype: list of str
        """
        return self._SourceUrl

    @SourceUrl.setter
    def SourceUrl(self, SourceUrl):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        self._SourceUrl = SourceUrl

    @property
    def SeekSecond(self):
        r"""Specify that the video plays from a specific second timestamp.
        :rtype: int
        """
        return self._SeekSecond

    @SeekSecond.setter
    def SeekSecond(self, SeekSecond):
        self._SeekSecond = SeekSecond

    @property
    def AutoPush(self):
        r"""Enable auto relay to cdn, please make sure that this feature has been enabled in the console.
        :rtype: bool
        """
        return self._AutoPush

    @AutoPush.setter
    def AutoPush(self, AutoPush):
        self._AutoPush = AutoPush

    @property
    def RepeatNum(self):
        r"""Loop playback count, value range: [-1, 1000], default is 1 time. - 0 is an invalid value - -1 is for loop playback, task termination requires actively calling the stop interface or setting MaxDuration.
        :rtype: int
        """
        return self._RepeatNum

    @RepeatNum.setter
    def RepeatNum(self, RepeatNum):
        self._RepeatNum = RepeatNum

    @property
    def MaxDuration(self):
        r"""Loop playback maximum duration, only effective when RepeatNum is set to -1, valid value range: [1, 10080], unit: minutes
        :rtype: int
        """
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Volume(self):
        r"""Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._StreamUrl = params.get("StreamUrl")
        self._PrivateMapKey = params.get("PrivateMapKey")
        if params.get("VideoEncodeParams") is not None:
            self._VideoEncodeParams = VideoEncodeParams()
            self._VideoEncodeParams._deserialize(params.get("VideoEncodeParams"))
        if params.get("AudioEncodeParams") is not None:
            self._AudioEncodeParams = AudioEncodeParams()
            self._AudioEncodeParams._deserialize(params.get("AudioEncodeParams"))
        self._SourceUrl = params.get("SourceUrl")
        self._SeekSecond = params.get("SeekSecond")
        self._AutoPush = params.get("AutoPush")
        self._RepeatNum = params.get("RepeatNum")
        self._MaxDuration = params.get("MaxDuration")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamIngestResponse(AbstractModel):
    r"""StartStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The Task ID of the Pull stream Relay. The Task ID is a unique identifier for a Pull stream Relay lifecycle process, and it loses its meaning when the task ends. The Task ID needs to be saved by the business as a parameter for the next operation on this task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The Task ID of the Pull stream Relay. The Task ID is a unique identifier for a Pull stream Relay lifecycle process, and it loses its meaning when the task ends. The Task ID needs to be saved by the business as a parameter for the next operation on this task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartWebRecordRequest(AbstractModel):
    r"""StartWebRecord request structure.

    """

    def __init__(self):
        r"""
        :param _RecordUrl: [Required] webpage URL that needs to be recorded.
        :type RecordUrl: str
        :param _StorageParams: [Required] cloud storage related parameters. currently supports tencent cloud object storage as well as VOD. no support for third-party cloud storage. the storage format of the output file is only supported for hls or mp4.
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param _SdkAppId: [Required] the SdkAppId of TRTC.
        :type SdkAppId: int
        :param _MaxDurationLimit: Maximum recording duration limit in seconds. valid values [1800, 86400]. default 86400s (24 hr).
        :type MaxDurationLimit: int
        :param _WebRecordVideoParams: Page recording video parameter.
        :type WebRecordVideoParams: :class:`tencentcloud.trtc.v20190722.models.WebRecordVideoParams`
        :param _RecordId: When sensitive to repetition tasks, pay attention to this value: to avoid triggering tasks repeatedly in a short time frame, which may lead to task duplication.
Import the recording RecordId to identify the task, less than 32 bytes. if carrying RecordId initiates start recording requests more than twice, only one task will start up, and the second will report error FailedOperation.TaskExist. note that when StartWebRecord call fails instead of FailedOperation.TaskExist error, change RecordId and re-initiate the request.
        :type RecordId: str
        :param _PublishCdnParams: If you want to push stream to CDN, you can configure parameters in PublishCdnParams.N. it supports streaming simultaneously to up to 10 CDN addresses. if the relay address is tencent cloud CDN, set IsTencentCdn to 1.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _ReadyTimeout: Timeout period for recording page resource loading, unit: second. default value is 0, which must be greater than or equal to 0 and less than or equal to 60. do not set this parameter when page loading timeout detection is disabled for the recording page.
        :type ReadyTimeout: int
        :param _EmulateMobileParams: Render the mobile mode parameter. do not set this parameter when not preparing to render the mobile mode webpage.
        :type EmulateMobileParams: :class:`tencentcloud.trtc.v20190722.models.EmulateMobileParams`
        """
        self._RecordUrl = None
        self._StorageParams = None
        self._SdkAppId = None
        self._MaxDurationLimit = None
        self._WebRecordVideoParams = None
        self._RecordId = None
        self._PublishCdnParams = None
        self._ReadyTimeout = None
        self._EmulateMobileParams = None

    @property
    def RecordUrl(self):
        r"""[Required] webpage URL that needs to be recorded.
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def StorageParams(self):
        r"""[Required] cloud storage related parameters. currently supports tencent cloud object storage as well as VOD. no support for third-party cloud storage. the storage format of the output file is only supported for hls or mp4.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        """
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def SdkAppId(self):
        r"""[Required] the SdkAppId of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MaxDurationLimit(self):
        r"""Maximum recording duration limit in seconds. valid values [1800, 86400]. default 86400s (24 hr).
        :rtype: int
        """
        return self._MaxDurationLimit

    @MaxDurationLimit.setter
    def MaxDurationLimit(self, MaxDurationLimit):
        self._MaxDurationLimit = MaxDurationLimit

    @property
    def WebRecordVideoParams(self):
        r"""Page recording video parameter.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WebRecordVideoParams`
        """
        return self._WebRecordVideoParams

    @WebRecordVideoParams.setter
    def WebRecordVideoParams(self, WebRecordVideoParams):
        self._WebRecordVideoParams = WebRecordVideoParams

    @property
    def RecordId(self):
        r"""When sensitive to repetition tasks, pay attention to this value: to avoid triggering tasks repeatedly in a short time frame, which may lead to task duplication.
Import the recording RecordId to identify the task, less than 32 bytes. if carrying RecordId initiates start recording requests more than twice, only one task will start up, and the second will report error FailedOperation.TaskExist. note that when StartWebRecord call fails instead of FailedOperation.TaskExist error, change RecordId and re-initiate the request.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def PublishCdnParams(self):
        r"""If you want to push stream to CDN, you can configure parameters in PublishCdnParams.N. it supports streaming simultaneously to up to 10 CDN addresses. if the relay address is tencent cloud CDN, set IsTencentCdn to 1.
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def ReadyTimeout(self):
        r"""Timeout period for recording page resource loading, unit: second. default value is 0, which must be greater than or equal to 0 and less than or equal to 60. do not set this parameter when page loading timeout detection is disabled for the recording page.
        :rtype: int
        """
        return self._ReadyTimeout

    @ReadyTimeout.setter
    def ReadyTimeout(self, ReadyTimeout):
        self._ReadyTimeout = ReadyTimeout

    @property
    def EmulateMobileParams(self):
        r"""Render the mobile mode parameter. do not set this parameter when not preparing to render the mobile mode webpage.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.EmulateMobileParams`
        """
        return self._EmulateMobileParams

    @EmulateMobileParams.setter
    def EmulateMobileParams(self, EmulateMobileParams):
        self._EmulateMobileParams = EmulateMobileParams


    def _deserialize(self, params):
        self._RecordUrl = params.get("RecordUrl")
        if params.get("StorageParams") is not None:
            self._StorageParams = StorageParams()
            self._StorageParams._deserialize(params.get("StorageParams"))
        self._SdkAppId = params.get("SdkAppId")
        self._MaxDurationLimit = params.get("MaxDurationLimit")
        if params.get("WebRecordVideoParams") is not None:
            self._WebRecordVideoParams = WebRecordVideoParams()
            self._WebRecordVideoParams._deserialize(params.get("WebRecordVideoParams"))
        self._RecordId = params.get("RecordId")
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        self._ReadyTimeout = params.get("ReadyTimeout")
        if params.get("EmulateMobileParams") is not None:
            self._EmulateMobileParams = EmulateMobileParams()
            self._EmulateMobileParams._deserialize(params.get("EmulateMobileParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWebRecordResponse(AbstractModel):
    r"""StartWebRecord response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique Id of the recording task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Unique Id of the recording task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopAIConversationRequest(AbstractModel):
    r"""StopAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task Unique ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task Unique ID
        :rtype: str
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
        


class StopAIConversationResponse(AbstractModel):
    r"""StopAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopAITranscriptionRequest(AbstractModel):
    r"""StopAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Uniquely identifies a transcription task.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Uniquely identifies a transcription task.
        :rtype: str
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
        


class StopAITranscriptionResponse(AbstractModel):
    r"""StopAITranscription response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopPublishCdnStreamRequest(AbstractModel):
    r"""StopPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param _TaskId: The task ID.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishCdnStreamResponse(AbstractModel):
    r"""StopPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopStreamIngestRequest(AbstractModel):
    r"""StopStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the task's room.
        :type SdkAppId: int
        :param _TaskId: The unique Task ID, which will be returned after the task is successfully started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""The SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the task's room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique Task ID, which will be returned after the task is successfully started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamIngestResponse(AbstractModel):
    r"""StopStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopWebRecordRequest(AbstractModel):
    r"""StopWebRecord request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The ID of the task that needs to be stopped
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""The ID of the task that needs to be stopped
        :rtype: str
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
        


class StopWebRecordResponse(AbstractModel):
    r"""StopWebRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StorageFile(AbstractModel):
    r"""The information of the recording files, which is returned by the `DescribeCloudRecording` API.

    """

    def __init__(self):
        r"""
        :param _UserId: The user whose stream is recorded into the file. In the mixed-stream recording mode, this parameter will be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UserId: str
        :param _FileName: The filename.
        :type FileName: str
        :param _TrackType: The type of the media recorded.
video
audio
audio_video
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TrackType: str
        :param _BeginTimeStamp: The start time (Unix timestamp) of the recording file.
        :type BeginTimeStamp: int
        """
        self._UserId = None
        self._FileName = None
        self._TrackType = None
        self._BeginTimeStamp = None

    @property
    def UserId(self):
        r"""The user whose stream is recorded into the file. In the mixed-stream recording mode, this parameter will be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        r"""The filename.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def TrackType(self):
        r"""The type of the media recorded.
video
audio
audio_video
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def BeginTimeStamp(self):
        r"""The start time (Unix timestamp) of the recording file.
        :rtype: int
        """
        return self._BeginTimeStamp

    @BeginTimeStamp.setter
    def BeginTimeStamp(self, BeginTimeStamp):
        self._BeginTimeStamp = BeginTimeStamp


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._FileName = params.get("FileName")
        self._TrackType = params.get("TrackType")
        self._BeginTimeStamp = params.get("BeginTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageParams(AbstractModel):
    r"""The storage parameters.

    """

    def __init__(self):
        r"""
        :param _CloudStorage: The account information for third-party storage. Please note that if you save files to COS, a recording-to-COS fee will be incurred. For details, see the document "Billing of On-Cloud Recording". If you save files to VOD, there won't be such a fee.
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param _CloudVod: The account information for VOD storage.
        :type CloudVod: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        self._CloudStorage = None
        self._CloudVod = None

    @property
    def CloudStorage(self):
        r"""The account information for third-party storage. Please note that if you save files to COS, a recording-to-COS fee will be incurred. For details, see the document "Billing of On-Cloud Recording". If you save files to VOD, there won't be such a fee.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def CloudVod(self):
        r"""The account information for VOD storage.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        return self._CloudVod

    @CloudVod.setter
    def CloudVod(self, CloudVod):
        self._CloudVod = CloudVod


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("CloudVod") is not None:
            self._CloudVod = CloudVod()
            self._CloudVod._deserialize(params.get("CloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeModerationUserIds(AbstractModel):
    r"""Specifies the subscription stream allowlist or blocklist. The audio allowlist and blocklist cannot be set simultaneously, and this also applies to video. Additionally, up to 25 concurrently subscribed media streams are supported, and up to 24 video screens are supported in mixed stream scenarios. It is also supported to use the ".*$" wildcard for prefix matching of UserId in the blocklist and allowlist. Note that if there are user IDs in the room that match the wildcard rule, specific users are subscribed, causing the prefix rule to become ineffective.

    """

    def __init__(self):
        r"""
        :param _SubscribeAudioUserIds: Subscription audio stream allowlist. It specifies which UserIds' audio streams to subscribe to, for example, ["1", "2", "3"] indicates subscriptions to the audio streams of UserId 1, 2, and 3; ["1.*$"] indicates subscription to audio streams with UserId prefixes starting with 1. If this parameter is left unspecified, all audio streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeAudioUserIds: list of str
        :param _UnSubscribeAudioUserIds: Subscription audio stream blocklist. It specifies which UserIds' audio streams not to subscribe to, for example, ["1", "2", "3"] indicates that the audio streams of UserId 1, 2, and 3 are not subscribed to; ["1.*$"] indicates that audio streams with UserId prefixes starting with 1 are not subscribed to. If this parameter is left unspecified, all audio streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnSubscribeAudioUserIds: list of str
        :param _SubscribeVideoUserIds: Subscription video stream allowlist. It specifies which UserIds' video streams to subscribe to, for example, ["1", "2", "3"] indicates subscriptions to the video streams of UserId 1, 2, and 3; ["1.*$"] indicates subscription to video streams with UserId prefixes starting with 1. If this parameter is left unspecified, all video streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeVideoUserIds: list of str
        :param _UnSubscribeVideoUserIds: Subscription video stream blocklist. It specifies which UserIds' video streams not to subscribe to, for example, ["1", "2", "3"] indicates that the video streams of UserId 1, 2, and 3 are not subscribed to; ["1.*$"] indicates that video streams with UserId prefixes starting with 1 are not subscribed to. If this parameter is left unspecified, all video streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnSubscribeVideoUserIds: list of str
        """
        self._SubscribeAudioUserIds = None
        self._UnSubscribeAudioUserIds = None
        self._SubscribeVideoUserIds = None
        self._UnSubscribeVideoUserIds = None

    @property
    def SubscribeAudioUserIds(self):
        r"""Subscription audio stream allowlist. It specifies which UserIds' audio streams to subscribe to, for example, ["1", "2", "3"] indicates subscriptions to the audio streams of UserId 1, 2, and 3; ["1.*$"] indicates subscription to audio streams with UserId prefixes starting with 1. If this parameter is left unspecified, all audio streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        r"""Subscription audio stream blocklist. It specifies which UserIds' audio streams not to subscribe to, for example, ["1", "2", "3"] indicates that the audio streams of UserId 1, 2, and 3 are not subscribed to; ["1.*$"] indicates that audio streams with UserId prefixes starting with 1 are not subscribed to. If this parameter is left unspecified, all audio streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        r"""Subscription video stream allowlist. It specifies which UserIds' video streams to subscribe to, for example, ["1", "2", "3"] indicates subscriptions to the video streams of UserId 1, 2, and 3; ["1.*$"] indicates subscription to video streams with UserId prefixes starting with 1. If this parameter is left unspecified, all video streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
        r"""Subscription video stream blocklist. It specifies which UserIds' video streams not to subscribe to, for example, ["1", "2", "3"] indicates that the video streams of UserId 1, 2, and 3 are not subscribed to; ["1.*$"] indicates that video streams with UserId prefixes starting with 1 are not subscribed to. If this parameter is left unspecified, all video streams in the room are subscribed to by default. The number of users in the subscription list should not exceed 32.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._UnSubscribeVideoUserIds

    @UnSubscribeVideoUserIds.setter
    def UnSubscribeVideoUserIds(self, UnSubscribeVideoUserIds):
        self._UnSubscribeVideoUserIds = UnSubscribeVideoUserIds


    def _deserialize(self, params):
        self._SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self._UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self._SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self._UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeStreamUserIds(AbstractModel):
    r"""The subscription allowlist/blocklist. You cannot specify an allowlist and a blocklist for audio/video subscription at the same time. The maximum number of streams one can receive at the same time is 25. When streams are mixed, up to 24 videos are supported. You can use `.*$` to specify user IDs with the same prefix, but make sure there aren’t users whose IDs contain ".*$" and are exactly the same as the prefix you pass in. If there are, TRTC will only allow or block those users.

    """

    def __init__(self):
        r"""
        :param _SubscribeAudioUserIds: The allowlist for audio subscription. For example, `["1", "2", "3"]` means to only subscribe to the audios of users 1, 2, and 3, and ["1.*$"] means to only subscribe to the audios of users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeAudioUserIds: list of str
        :param _UnSubscribeAudioUserIds: The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeAudioUserIds: list of str
        :param _SubscribeVideoUserIds: The allowlist for video subscription. For example, `["1", "2", "3"]` means to only subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to only subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeVideoUserIds: list of str
        :param _UnSubscribeVideoUserIds: The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeVideoUserIds: list of str
        """
        self._SubscribeAudioUserIds = None
        self._UnSubscribeAudioUserIds = None
        self._SubscribeVideoUserIds = None
        self._UnSubscribeVideoUserIds = None

    @property
    def SubscribeAudioUserIds(self):
        r"""The allowlist for audio subscription. For example, `["1", "2", "3"]` means to only subscribe to the audios of users 1, 2, and 3, and ["1.*$"] means to only subscribe to the audios of users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        r"""The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        r"""The allowlist for video subscription. For example, `["1", "2", "3"]` means to only subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to only subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
        r"""The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._UnSubscribeVideoUserIds

    @UnSubscribeVideoUserIds.setter
    def UnSubscribeVideoUserIds(self, UnSubscribeVideoUserIds):
        self._UnSubscribeVideoUserIds = UnSubscribeVideoUserIds


    def _deserialize(self, params):
        self._SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self._UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self._SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self._UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCDataResult(AbstractModel):
    r"""TRTC Data Dashboard/Real-Time Monitoring API output parameters

    """

    def __init__(self):
        r"""
        :param _StatementID: The StatementID value is fixed as 0 in the monitoring dashboard.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatementID: int
        :param _Series: Query result data is returned in Columns-Values format.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Series: list of SeriesInfos
        :param _Total: The Total value is fixed as 1 in the dashboard feature monitoring.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        """
        self._StatementID = None
        self._Series = None
        self._Total = None

    @property
    def StatementID(self):
        r"""The StatementID value is fixed as 0 in the monitoring dashboard.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def Series(self):
        r"""Query result data is returned in Columns-Values format.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SeriesInfos
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Total(self):
        r"""The Total value is fixed as 1 in the dashboard feature monitoring.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._StatementID = params.get("StatementID")
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = SeriesInfos()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TTSConfig(AbstractModel):
    r"""TTS configuration.

    """

    def __init__(self):
        r"""
        :param _VoiceId: Voice type ID.
        :type VoiceId: str
        :param _Model: TTS model: flow_01_turbo is selected by default. options: [flow_01_turbo, flow_01_ex].
        :type Model: str
        :param _Speed: Speaking rate. value range: 0.5-2.0. default: 1.0.
        :type Speed: float
        :param _Volume: Value range: (0, 10]. default value: 1.0.
        :type Volume: float
        """
        self._VoiceId = None
        self._Model = None
        self._Speed = None
        self._Volume = None

    @property
    def VoiceId(self):
        r"""Voice type ID.
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Model(self):
        r"""TTS model: flow_01_turbo is selected by default. options: [flow_01_turbo, flow_01_ex].
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Speed(self):
        r"""Speaking rate. value range: 0.5-2.0. default: 1.0.
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""Value range: (0, 10]. default value: 1.0.
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._Model = params.get("Model")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TTSParam(AbstractModel):
    r"""Transcription TTS parameter

    """

    def __init__(self):
        r"""
        :param _Model: <p>TTS model</p>
        :type Model: str
        :param _Language: <p>TTS language must be in the TargetLang list of TranslationParam.</p>
        :type Language: str
        :param _TargetUser: <p>The user requesting TTS playback. They must be on the subscription allowlist and not on the blocklist.</p>
        :type TargetUser: :class:`tencentcloud.trtc.v20190722.models.TranscriptionUserInfoParams`
        :param _TTSRobotUser: <p>The robot user that pushes TTS audio back into the room.</p>
        :type TTSRobotUser: :class:`tencentcloud.trtc.v20190722.models.TranscriptionUserInfoParams`
        :param _Voice: <p>TTS configuration parameters.</p>
        :type Voice: :class:`tencentcloud.trtc.v20190722.models.TTSVoice`
        """
        self._Model = None
        self._Language = None
        self._TargetUser = None
        self._TTSRobotUser = None
        self._Voice = None

    @property
    def Model(self):
        r"""<p>TTS model</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""<p>TTS language must be in the TargetLang list of TranslationParam.</p>
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def TargetUser(self):
        r"""<p>The user requesting TTS playback. They must be on the subscription allowlist and not on the blocklist.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionUserInfoParams`
        """
        return self._TargetUser

    @TargetUser.setter
    def TargetUser(self, TargetUser):
        self._TargetUser = TargetUser

    @property
    def TTSRobotUser(self):
        r"""<p>The robot user that pushes TTS audio back into the room.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionUserInfoParams`
        """
        return self._TTSRobotUser

    @TTSRobotUser.setter
    def TTSRobotUser(self, TTSRobotUser):
        self._TTSRobotUser = TTSRobotUser

    @property
    def Voice(self):
        r"""<p>TTS configuration parameters.</p>
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TTSVoice`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        if params.get("TargetUser") is not None:
            self._TargetUser = TranscriptionUserInfoParams()
            self._TargetUser._deserialize(params.get("TargetUser"))
        if params.get("TTSRobotUser") is not None:
            self._TTSRobotUser = TranscriptionUserInfoParams()
            self._TTSRobotUser._deserialize(params.get("TTSRobotUser"))
        if params.get("Voice") is not None:
            self._Voice = TTSVoice()
            self._Voice._deserialize(params.get("Voice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TTSVoice(AbstractModel):
    r"""Speech parameter configuration for companion transcription TTS

    """

    def __init__(self):
        r"""
        :param _VoiceId: <p>Voice ID.</p>
        :type VoiceId: str
        :param _Speed: <p>Speech speed. 0.5 for half speed, 2.0 for 2x speed, 1.0 for normal speed. Value range: [0.5, 2.0]. Default: 1.0.</p>
        :type Speed: float
        :param _Volume: <p>Audio volume. 0 is mute, 10 is maximum volume. It is recommended to keep the default value to 1.0. Value range: [0, 10]. Default: 1.0.</p>
        :type Volume: float
        :param _Pitch: <p>Pitch. Negative value makes the sound low and deep, positive value makes it sharper. 0 indicates the original pitch. Value range: [-12, 12]. Default 0.</p>
        :type Pitch: int
        """
        self._VoiceId = None
        self._Speed = None
        self._Volume = None
        self._Pitch = None

    @property
    def VoiceId(self):
        r"""<p>Voice ID.</p>
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Speed(self):
        r"""<p>Speech speed. 0.5 for half speed, 2.0 for 2x speed, 1.0 for normal speed. Value range: [0.5, 2.0]. Default: 1.0.</p>
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""<p>Audio volume. 0 is mute, 10 is maximum volume. It is recommended to keep the default value to 1.0. Value range: [0, 10]. Default: 1.0.</p>
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Pitch(self):
        r"""<p>Pitch. Negative value makes the sound low and deep, positive value makes it sharper. 0 indicates the original pitch. Value range: [-12, 12]. Default 0.</p>
        :rtype: int
        """
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        self._Pitch = params.get("Pitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TencentVod(AbstractModel):
    r"""The Tencent Cloud VOD parameters.

    """

    def __init__(self):
        r"""
        :param _Procedure: Subsequent media task processing operations allow automatic task initiation after media upload is completed. the parameter value is the task flow template name. VOD (video on demand) supports creating task flow templates and template naming.
        :type Procedure: str
        :param _ExpireTime: Media file expiry time is the absolute expiration time from the current system time. to save for one day, enter "86400". to retain permanently, enter "0". the default is permanent preservation.
        :type ExpireTime: int
        :param _StorageRegion: Specify the upload park, applicable only to the user with special requirement for upload region.
        :type StorageRegion: str
        :param _ClassId: Category ID is used to categorize and manage media. you can create a category and obtain the category ID through the create category api.
The default value is 0, indicating other categories.
        :type ClassId: int
        :param _SubAppId: Subapplication ID for video-on-demand (vod). if you need to access resources belonging to a subapplication, fill in this field with the subapplication ID. otherwise, this field is not required.
        :type SubAppId: int
        :param _SessionContext: Task flow context, passed through when task complete.
        :type SessionContext: str
        :param _SourceContext: Upload context, passed through on upload completion callback.
        :type SourceContext: str
        :param _MediaType: The recording file format type uploaded to the vod platform. valid values: 0: mp4 (default), 1: hls, 2: aac (valid at that time when StreamType=1 for audio-only recording).
3: hls+mp4, 4: hls+aac (valid at that time when StreamType=1 is audio-only recording).
        :type MediaType: int
        :param _UserDefineRecordId: Only supports API recording upload to vod. this parameter indicates you can customize the recording file name prefix. [length limit: 64 bytes, only allows a combination of uppercase and lowercase letters (a-zA-Z), numbers (0-9), underline, and hyphen]. the prefix is separated from the automatically generated recording file name by `__UserDefine_u_`.
        :type UserDefineRecordId: str
        """
        self._Procedure = None
        self._ExpireTime = None
        self._StorageRegion = None
        self._ClassId = None
        self._SubAppId = None
        self._SessionContext = None
        self._SourceContext = None
        self._MediaType = None
        self._UserDefineRecordId = None

    @property
    def Procedure(self):
        r"""Subsequent media task processing operations allow automatic task initiation after media upload is completed. the parameter value is the task flow template name. VOD (video on demand) supports creating task flow templates and template naming.
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        r"""Media file expiry time is the absolute expiration time from the current system time. to save for one day, enter "86400". to retain permanently, enter "0". the default is permanent preservation.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        r"""Specify the upload park, applicable only to the user with special requirement for upload region.
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        r"""Category ID is used to categorize and manage media. you can create a category and obtain the category ID through the create category api.
The default value is 0, indicating other categories.
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        r"""Subapplication ID for video-on-demand (vod). if you need to access resources belonging to a subapplication, fill in this field with the subapplication ID. otherwise, this field is not required.
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        r"""Task flow context, passed through when task complete.
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        r"""Upload context, passed through on upload completion callback.
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext

    @property
    def MediaType(self):
        r"""The recording file format type uploaded to the vod platform. valid values: 0: mp4 (default), 1: hls, 2: aac (valid at that time when StreamType=1 for audio-only recording).
3: hls+mp4, 4: hls+aac (valid at that time when StreamType=1 is audio-only recording).
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def UserDefineRecordId(self):
        r"""Only supports API recording upload to vod. this parameter indicates you can customize the recording file name prefix. [length limit: 64 bytes, only allows a combination of uppercase and lowercase letters (a-zA-Z), numbers (0-9), underline, and hyphen]. the prefix is separated from the automatically generated recording file name by `__UserDefine_u_`.
        :rtype: str
        """
        return self._UserDefineRecordId

    @UserDefineRecordId.setter
    def UserDefineRecordId(self, UserDefineRecordId):
        self._UserDefineRecordId = UserDefineRecordId


    def _deserialize(self, params):
        self._Procedure = params.get("Procedure")
        self._ExpireTime = params.get("ExpireTime")
        self._StorageRegion = params.get("StorageRegion")
        self._ClassId = params.get("ClassId")
        self._SubAppId = params.get("SubAppId")
        self._SessionContext = params.get("SessionContext")
        self._SourceContext = params.get("SourceContext")
        self._MediaType = params.get("MediaType")
        self._UserDefineRecordId = params.get("UserDefineRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TermPair(AbstractModel):
    r"""Glossary phrase pairs for transcription

    """

    def __init__(self):
        r"""
        :param _Source: <p>Source terms.</p>
        :type Source: str
        :param _Target: <p>Translated terms in target language.</p>
        :type Target: str
        """
        self._Source = None
        self._Target = None

    @property
    def Source(self):
        r"""<p>Source terms.</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""<p>Translated terms in target language.</p>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Terminology(AbstractModel):
    r"""Translate terminology.

    """

    def __init__(self):
        r"""
        :param _Source: Source terminology.
        :type Source: str
        :param _Target: Terminology translation result.
        :type Target: str
        """
        self._Source = None
        self._Target = None

    @property
    def Source(self):
        r"""Source terminology.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""Terminology translation result.
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminologyItem(AbstractModel):
    r"""Transcription companion terminology table entry

    """

    def __init__(self):
        r"""
        :param _TargetLang: <p>Target language.</p>
        :type TargetLang: str
        :param _Terminology: <p>Terminology configuration.</p>
        :type Terminology: list of TermPair
        """
        self._TargetLang = None
        self._Terminology = None

    @property
    def TargetLang(self):
        r"""<p>Target language.</p>
        :rtype: str
        """
        return self._TargetLang

    @TargetLang.setter
    def TargetLang(self, TargetLang):
        self._TargetLang = TargetLang

    @property
    def Terminology(self):
        r"""<p>Terminology configuration.</p>
        :rtype: list of TermPair
        """
        return self._Terminology

    @Terminology.setter
    def Terminology(self, Terminology):
        self._Terminology = Terminology


    def _deserialize(self, params):
        self._TargetLang = params.get("TargetLang")
        if params.get("Terminology") is not None:
            self._Terminology = []
            for item in params.get("Terminology"):
                obj = TermPair()
                obj._deserialize(item)
                self._Terminology.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechRequest(AbstractModel):
    r"""TextToSpeech request structure.

    """

    def __init__(self):
        r"""
        :param _Text: Text to be converted to speech. length range: [1, 255].
        :type Text: str
        :param _Voice: Audio configuration for text-to-speech.
        :type Voice: :class:`tencentcloud.trtc.v20190722.models.Voice`
        :param _SdkAppId: Specifies the SdkAppId of TRTC.
        :type SdkAppId: int
        :param _AudioFormat: Specifies the output audio format for text-to-speech.
        :type AudioFormat: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        :param _APIKey: API key for TTS.
        :type APIKey: str
        :param _Model: TTS model, current fixed value: flow_01_turbo.
        :type Model: str
        :param _Language: Language to be synthesised (ISO 639-1). supports zh (chinese), en (english), yue (cantonese), ja (japanese), and ko (korean). defaults to auto-identification.
        :type Language: str
        :param _PronunciationDict: 
        :type PronunciationDict: list of PronunciationDict
        :param _AlignmentMode: 
        :type AlignmentMode: int
        """
        self._Text = None
        self._Voice = None
        self._SdkAppId = None
        self._AudioFormat = None
        self._APIKey = None
        self._Model = None
        self._Language = None
        self._PronunciationDict = None
        self._AlignmentMode = None

    @property
    def Text(self):
        r"""Text to be converted to speech. length range: [1, 255].
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Voice(self):
        r"""Audio configuration for text-to-speech.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.Voice`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SdkAppId(self):
        r"""Specifies the SdkAppId of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioFormat(self):
        r"""Specifies the output audio format for text-to-speech.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def APIKey(self):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        r"""API key for TTS.
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        self._APIKey = APIKey

    @property
    def Model(self):
        r"""TTS model, current fixed value: flow_01_turbo.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""Language to be synthesised (ISO 639-1). supports zh (chinese), en (english), yue (cantonese), ja (japanese), and ko (korean). defaults to auto-identification.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def PronunciationDict(self):
        r"""
        :rtype: list of PronunciationDict
        """
        return self._PronunciationDict

    @PronunciationDict.setter
    def PronunciationDict(self, PronunciationDict):
        self._PronunciationDict = PronunciationDict

    @property
    def AlignmentMode(self):
        r"""
        :rtype: int
        """
        return self._AlignmentMode

    @AlignmentMode.setter
    def AlignmentMode(self, AlignmentMode):
        self._AlignmentMode = AlignmentMode


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Voice") is not None:
            self._Voice = Voice()
            self._Voice._deserialize(params.get("Voice"))
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioFormat") is not None:
            self._AudioFormat = AudioFormat()
            self._AudioFormat._deserialize(params.get("AudioFormat"))
        self._APIKey = params.get("APIKey")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        if params.get("PronunciationDict") is not None:
            self._PronunciationDict = []
            for item in params.get("PronunciationDict"):
                obj = PronunciationDict()
                obj._deserialize(item)
                self._PronunciationDict.append(obj)
        self._AlignmentMode = params.get("AlignmentMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechResponse(AbstractModel):
    r"""TextToSpeech response structure.

    """

    def __init__(self):
        r"""
        :param _Audio: Base64-Encoded audio data.
        :type Audio: str
        :param _Alignments: 
        :type Alignments: list of AlignmentItem
        :param _TotalDurationMs: 
        :type TotalDurationMs: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Audio = None
        self._Alignments = None
        self._TotalDurationMs = None
        self._RequestId = None

    @property
    def Audio(self):
        r"""Base64-Encoded audio data.
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def Alignments(self):
        r"""
        :rtype: list of AlignmentItem
        """
        return self._Alignments

    @Alignments.setter
    def Alignments(self, Alignments):
        self._Alignments = Alignments

    @property
    def TotalDurationMs(self):
        r"""
        :rtype: int
        """
        return self._TotalDurationMs

    @TotalDurationMs.setter
    def TotalDurationMs(self, TotalDurationMs):
        self._TotalDurationMs = TotalDurationMs

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
        self._Audio = params.get("Audio")
        if params.get("Alignments") is not None:
            self._Alignments = []
            for item in params.get("Alignments"):
                obj = AlignmentItem()
                obj._deserialize(item)
                self._Alignments.append(obj)
        self._TotalDurationMs = params.get("TotalDurationMs")
        self._RequestId = params.get("RequestId")


class TextToSpeechSSERequest(AbstractModel):
    r"""TextToSpeechSSE request structure.

    """

    def __init__(self):
        r"""
        :param _Text: Text to be converted to speech. length range: [1, 255].
        :type Text: str
        :param _Voice: Audio configuration for text-to-speech.
        :type Voice: :class:`tencentcloud.trtc.v20190722.models.Voice`
        :param _SdkAppId: Specifies the SdkAppId of TRTC.
        :type SdkAppId: int
        :param _AudioFormat: Specifies the output audio format for text-to-speech.
        :type AudioFormat: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        :param _APIKey: API key for TTS.
        :type APIKey: str
        :param _Model: TTS model, current fixed value: flow_01_turbo.
        :type Model: str
        :param _Language: Language to be synthesised (ISO 639-1). supports zh (chinese), en (english), yue (cantonese), ja (japanese), and ko (korean). defaults to auto-identification.
        :type Language: str
        :param _PronunciationDict: 
        :type PronunciationDict: list of PronunciationDict
        :param _AlignmentMode: 
        :type AlignmentMode: int
        """
        self._Text = None
        self._Voice = None
        self._SdkAppId = None
        self._AudioFormat = None
        self._APIKey = None
        self._Model = None
        self._Language = None
        self._PronunciationDict = None
        self._AlignmentMode = None

    @property
    def Text(self):
        r"""Text to be converted to speech. length range: [1, 255].
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Voice(self):
        r"""Audio configuration for text-to-speech.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.Voice`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SdkAppId(self):
        r"""Specifies the SdkAppId of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioFormat(self):
        r"""Specifies the output audio format for text-to-speech.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def APIKey(self):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        r"""API key for TTS.
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        self._APIKey = APIKey

    @property
    def Model(self):
        r"""TTS model, current fixed value: flow_01_turbo.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""Language to be synthesised (ISO 639-1). supports zh (chinese), en (english), yue (cantonese), ja (japanese), and ko (korean). defaults to auto-identification.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def PronunciationDict(self):
        r"""
        :rtype: list of PronunciationDict
        """
        return self._PronunciationDict

    @PronunciationDict.setter
    def PronunciationDict(self, PronunciationDict):
        self._PronunciationDict = PronunciationDict

    @property
    def AlignmentMode(self):
        r"""
        :rtype: int
        """
        return self._AlignmentMode

    @AlignmentMode.setter
    def AlignmentMode(self, AlignmentMode):
        self._AlignmentMode = AlignmentMode


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Voice") is not None:
            self._Voice = Voice()
            self._Voice._deserialize(params.get("Voice"))
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioFormat") is not None:
            self._AudioFormat = AudioFormat()
            self._AudioFormat._deserialize(params.get("AudioFormat"))
        self._APIKey = params.get("APIKey")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        if params.get("PronunciationDict") is not None:
            self._PronunciationDict = []
            for item in params.get("PronunciationDict"):
                obj = PronunciationDict()
                obj._deserialize(item)
                self._PronunciationDict.append(obj)
        self._AlignmentMode = params.get("AlignmentMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechSSEResponse(AbstractModel):
    r"""TextToSpeechSSE response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem. As a streaming response API, when the request is successfully completed, the RequestId will be placed in the Header "X-TC-RequestId" of the HTTP response.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class TimeValue(AbstractModel):
    r"""The quality data, which consists of the `time` and `value` parameters.

    """

    def __init__(self):
        r"""
        :param _Time: The UNIX timestamp (seconds), such as `1590065877`.
        :type Time: int
        :param _Value: The metric value. For example, if the video capturing frame rate (`bigvCapFps`) at the time `1590065877` is `0`, the value of this parameter will be `0`.
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        r"""The UNIX timestamp (seconds), such as `1590065877`.
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        r"""The metric value. For example, if the video capturing frame rate (`bigvCapFps`) at the time `1590065877` is `0`, the value of this parameter will be `0`.
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscriptionParam(AbstractModel):
    r"""Parameters for the transcription service to join TRTC room.

    """

    def __init__(self):
        r"""
        :param _UserId: [UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#userid) used by the transcription service in the TRTC room. Note that this userId cannot duplicate those already used by other TRTC or transcription services etc. You may use the room ID as part of the user identification.
        :type UserId: str
        :param _UserSig: User signature for the transcription service to join a TRTC room. The signature verification corresponding to the current UserId serves as the login password. For specific details, see TRTC solution for calculating [UserSig](https://intl.cloud.tencent.com/zh/document/product/647/38104).
        :type UserSig: str
        :param _SubscribeList: Allowlist of user IDs whose audio will be transcribed.
Specifies which anchor audio streams to transcribe when the service starts. If left empty or omitted, audio from all anchors will be transcribed. If one or more values are provided, only audio from the specified anchors will be transcribed.

> Note: If a user ID appears in both the `SubscribeList` and `UnSubscribeList`, the `UnSubscribeList` takes precedence.
        :type SubscribeList: list of TranscriptionUserInfoParams
        :param _UnSubscribeList: Blocklist of user IDs whose audio will be excluded from transcription. 
Leave empty or omit to disable the blocklist. Provide specific values to exclude the specified anchors' audio from transcription.

        :type UnSubscribeList: list of TranscriptionUserInfoParams
        :param _MaxIdleTime: Maximum idle duration before the transcription task is automatically stopped, in seconds.
If all anchors being transcribed continuously leave the TRTC room or switch to the audience role for longer than this value, the transcription task stops automatically.
- Default: 30
- Range: 5 - 86400 (24 hours)
        :type MaxIdleTime: int
        :param _SendCustomMode: Custom data mode: 0 indicates disabled, 1 indicates enabled.
Leave blank defaults to 0, meaning custom data is disabled.
        :type SendCustomMode: int
        """
        self._UserId = None
        self._UserSig = None
        self._SubscribeList = None
        self._UnSubscribeList = None
        self._MaxIdleTime = None
        self._SendCustomMode = None

    @property
    def UserId(self):
        r"""[UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#userid) used by the transcription service in the TRTC room. Note that this userId cannot duplicate those already used by other TRTC or transcription services etc. You may use the room ID as part of the user identification.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""User signature for the transcription service to join a TRTC room. The signature verification corresponding to the current UserId serves as the login password. For specific details, see TRTC solution for calculating [UserSig](https://intl.cloud.tencent.com/zh/document/product/647/38104).
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def SubscribeList(self):
        r"""Allowlist of user IDs whose audio will be transcribed.
Specifies which anchor audio streams to transcribe when the service starts. If left empty or omitted, audio from all anchors will be transcribed. If one or more values are provided, only audio from the specified anchors will be transcribed.

> Note: If a user ID appears in both the `SubscribeList` and `UnSubscribeList`, the `UnSubscribeList` takes precedence.
        :rtype: list of TranscriptionUserInfoParams
        """
        return self._SubscribeList

    @SubscribeList.setter
    def SubscribeList(self, SubscribeList):
        self._SubscribeList = SubscribeList

    @property
    def UnSubscribeList(self):
        r"""Blocklist of user IDs whose audio will be excluded from transcription. 
Leave empty or omit to disable the blocklist. Provide specific values to exclude the specified anchors' audio from transcription.

        :rtype: list of TranscriptionUserInfoParams
        """
        return self._UnSubscribeList

    @UnSubscribeList.setter
    def UnSubscribeList(self, UnSubscribeList):
        self._UnSubscribeList = UnSubscribeList

    @property
    def MaxIdleTime(self):
        r"""Maximum idle duration before the transcription task is automatically stopped, in seconds.
If all anchors being transcribed continuously leave the TRTC room or switch to the audience role for longer than this value, the transcription task stops automatically.
- Default: 30
- Range: 5 - 86400 (24 hours)
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def SendCustomMode(self):
        r"""Custom data mode: 0 indicates disabled, 1 indicates enabled.
Leave blank defaults to 0, meaning custom data is disabled.
        :rtype: int
        """
        return self._SendCustomMode

    @SendCustomMode.setter
    def SendCustomMode(self, SendCustomMode):
        self._SendCustomMode = SendCustomMode


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("SubscribeList") is not None:
            self._SubscribeList = []
            for item in params.get("SubscribeList"):
                obj = TranscriptionUserInfoParams()
                obj._deserialize(item)
                self._SubscribeList.append(obj)
        if params.get("UnSubscribeList") is not None:
            self._UnSubscribeList = []
            for item in params.get("UnSubscribeList"):
                obj = TranscriptionUserInfoParams()
                obj._deserialize(item)
                self._UnSubscribeList.append(obj)
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._SendCustomMode = params.get("SendCustomMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscriptionParams(AbstractModel):
    r"""AI transcribe parameters.

    """

    def __init__(self):
        r"""
        :param _UserId: The transcription robot's UserId is used to enter the room and trigger a transcription task. note that this UserId cannot be the same as the host or audience [UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#UserId) in the current room. if multiple transcription tasks are initiated in a room, the robot's UserId must also be unique to avoid interrupting the previous task. ensure the transcription robot's UserId is unique in the room.
        :type UserId: str
        :param _UserSig: Verification signature corresponding to the transcription bot's UserId, namely, the UserId and UserSig serve as the login password for the transcription bot to enter the room. for specific calculation methods, see TRTC solution for calculating.
        :type UserSig: str
        :param _MaxIdleTime: After all push users exit the room and exceed MaxIdleTime seconds, the backend automation shuts down the transcription task. default value is 60s.
        :type MaxIdleTime: int
        :param _TranscriptionMode: 1 means the robot subscribes to the stream of an individual, and 0 means the robot subscribes to the stream of the entire room. if left empty, it defaults to subscribing to the stream of the entire room.
        :type TranscriptionMode: int
        :param _TargetUserId: Required when TranscriptionMode is 1, the robot only pulls streams from this userid and ignores other users in the room.
        :type TargetUserId: str
        :param _VoicePrint: Voiceprint configuration.
        :type VoicePrint: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        :param _TurnDetection: Semantic sentence segmentation detection.
        :type TurnDetection: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        self._UserId = None
        self._UserSig = None
        self._MaxIdleTime = None
        self._TranscriptionMode = None
        self._TargetUserId = None
        self._VoicePrint = None
        self._TurnDetection = None

    @property
    def UserId(self):
        r"""The transcription robot's UserId is used to enter the room and trigger a transcription task. note that this UserId cannot be the same as the host or audience [UserId](https://www.tencentcloud.com/document/product/647/46351?from_cn_redirect=1#UserId) in the current room. if multiple transcription tasks are initiated in a room, the robot's UserId must also be unique to avoid interrupting the previous task. ensure the transcription robot's UserId is unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""Verification signature corresponding to the transcription bot's UserId, namely, the UserId and UserSig serve as the login password for the transcription bot to enter the room. for specific calculation methods, see TRTC solution for calculating.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
        r"""After all push users exit the room and exceed MaxIdleTime seconds, the backend automation shuts down the transcription task. default value is 60s.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def TranscriptionMode(self):
        r"""1 means the robot subscribes to the stream of an individual, and 0 means the robot subscribes to the stream of the entire room. if left empty, it defaults to subscribing to the stream of the entire room.
        :rtype: int
        """
        return self._TranscriptionMode

    @TranscriptionMode.setter
    def TranscriptionMode(self, TranscriptionMode):
        self._TranscriptionMode = TranscriptionMode

    @property
    def TargetUserId(self):
        r"""Required when TranscriptionMode is 1, the robot only pulls streams from this userid and ignores other users in the room.
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId

    @property
    def VoicePrint(self):
        r"""Voiceprint configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        """
        return self._VoicePrint

    @VoicePrint.setter
    def VoicePrint(self, VoicePrint):
        self._VoicePrint = VoicePrint

    @property
    def TurnDetection(self):
        r"""Semantic sentence segmentation detection.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        return self._TurnDetection

    @TurnDetection.setter
    def TurnDetection(self, TurnDetection):
        self._TurnDetection = TurnDetection


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._TranscriptionMode = params.get("TranscriptionMode")
        self._TargetUserId = params.get("TargetUserId")
        if params.get("VoicePrint") is not None:
            self._VoicePrint = VoicePrint()
            self._VoicePrint._deserialize(params.get("VoicePrint"))
        if params.get("TurnDetection") is not None:
            self._TurnDetection = TurnDetection()
            self._TurnDetection._deserialize(params.get("TurnDetection"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscriptionUserInfoParams(AbstractModel):
    r"""Transcribe user information

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationConfig(AbstractModel):
    r"""Translate configuration.

    """

    def __init__(self):
        r"""
        :param _TargetLanguages: Target language for translation, target language list (ISO 639-1).

        :type TargetLanguages: list of str
        :param _Mode: 1: text translation only 2: speech simultaneous interpretation.

        :type Mode: int
        :param _TTSConfig: Speech simultaneous interpretation configuration. when enabling simultaneous interpretation, transmission is required.
        :type TTSConfig: :class:`tencentcloud.trtc.v20190722.models.TTSConfig`
        :param _Terminology: Translation terminology collection.
        :type Terminology: list of Terminology
        """
        self._TargetLanguages = None
        self._Mode = None
        self._TTSConfig = None
        self._Terminology = None

    @property
    def TargetLanguages(self):
        r"""Target language for translation, target language list (ISO 639-1).

        :rtype: list of str
        """
        return self._TargetLanguages

    @TargetLanguages.setter
    def TargetLanguages(self, TargetLanguages):
        self._TargetLanguages = TargetLanguages

    @property
    def Mode(self):
        r"""1: text translation only 2: speech simultaneous interpretation.

        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def TTSConfig(self):
        r"""Speech simultaneous interpretation configuration. when enabling simultaneous interpretation, transmission is required.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TTSConfig`
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def Terminology(self):
        r"""Translation terminology collection.
        :rtype: list of Terminology
        """
        return self._Terminology

    @Terminology.setter
    def Terminology(self, Terminology):
        self._Terminology = Terminology


    def _deserialize(self, params):
        self._TargetLanguages = params.get("TargetLanguages")
        self._Mode = params.get("Mode")
        if params.get("TTSConfig") is not None:
            self._TTSConfig = TTSConfig()
            self._TTSConfig._deserialize(params.get("TTSConfig"))
        if params.get("Terminology") is not None:
            self._Terminology = []
            for item in params.get("Terminology"):
                obj = Terminology()
                obj._deserialize(item)
                self._Terminology.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationParam(AbstractModel):
    r"""Translation parameters

    """

    def __init__(self):
        r"""
        :param _TargetLang: <p>Target language for translation, example value ["en", "ja"]. Target language list [Chinese "zh", English "en", Vietnamese "vi", Japanese "ja", Korean "ko", Indonesian "id", Thai "th", Portuguese "pt", Arabic "ar", Spanish "es", French "fr", Malay "ms", German "de", Italian "it", Russian "ru"].</p>
        :type TargetLang: list of str
        :param _Terminologies: <p>Glossary configuration.</p>
        :type Terminologies: list of TerminologyItem
        """
        self._TargetLang = None
        self._Terminologies = None

    @property
    def TargetLang(self):
        r"""<p>Target language for translation, example value ["en", "ja"]. Target language list [Chinese "zh", English "en", Vietnamese "vi", Japanese "ja", Korean "ko", Indonesian "id", Thai "th", Portuguese "pt", Arabic "ar", Spanish "es", French "fr", Malay "ms", German "de", Italian "it", Russian "ru"].</p>
        :rtype: list of str
        """
        return self._TargetLang

    @TargetLang.setter
    def TargetLang(self, TargetLang):
        self._TargetLang = TargetLang

    @property
    def Terminologies(self):
        r"""<p>Glossary configuration.</p>
        :rtype: list of TerminologyItem
        """
        return self._Terminologies

    @Terminologies.setter
    def Terminologies(self, Terminologies):
        self._Terminologies = Terminologies


    def _deserialize(self, params):
        self._TargetLang = params.get("TargetLang")
        if params.get("Terminologies") is not None:
            self._Terminologies = []
            for item in params.get("Terminologies"):
                obj = TerminologyItem()
                obj._deserialize(item)
                self._Terminologies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrtcUsage(AbstractModel):
    r"""The TRTC audio/video duration generated in a certain time period.

    """

    def __init__(self):
        r"""
        :param _TimeKey: The time point in the format of `YYYY-MM-DD HH:mm:ss`. If more than one day is queried, `HH:mm:ss` is `00:00:00`.
        :type TimeKey: str
        :param _UsageValue: The usage (minutes). Each element of this parameter corresponds to an element of `UsageKey` in the order they are listed.
        :type UsageValue: list of float
        """
        self._TimeKey = None
        self._UsageValue = None

    @property
    def TimeKey(self):
        r"""The time point in the format of `YYYY-MM-DD HH:mm:ss`. If more than one day is queried, `HH:mm:ss` is `00:00:00`.
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def UsageValue(self):
        r"""The usage (minutes). Each element of this parameter corresponds to an element of `UsageKey` in the order they are listed.
        :rtype: list of float
        """
        return self._UsageValue

    @UsageValue.setter
    def UsageValue(self, UsageValue):
        self._UsageValue = UsageValue


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._UsageValue = params.get("UsageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnDetection(AbstractModel):
    r"""Sentence segmentation configuration.

    """

    def __init__(self):
        r"""
        :param _SemanticEagerness: This parameter is valid only when TurnDetectionMode is 3, indicating the sensitivity of sentence segmentation.


Feature description: determines whether the user has finished speaking to separate the audio.


Optional: "low" | "medium" | "high" | "auto".


auto is the default value, same as medium.
low will give users sufficient time to speak.
high will perform audio chunking as soon as possible.


If you wish the model to respond more frequently in conversation mode, you can set SemanticEagerness to high.
If you wish the AI to wait a moment when the user pauses, set SemanticEagerness to low.
Regardless of the mode, it will eventually split and send to a large model for reply.

        :type SemanticEagerness: str
        """
        self._SemanticEagerness = None

    @property
    def SemanticEagerness(self):
        r"""This parameter is valid only when TurnDetectionMode is 3, indicating the sensitivity of sentence segmentation.


Feature description: determines whether the user has finished speaking to separate the audio.


Optional: "low" | "medium" | "high" | "auto".


auto is the default value, same as medium.
low will give users sufficient time to speak.
high will perform audio chunking as soon as possible.


If you wish the model to respond more frequently in conversation mode, you can set SemanticEagerness to high.
If you wish the AI to wait a moment when the user pauses, set SemanticEagerness to low.
Regardless of the mode, it will eventually split and send to a large model for reply.

        :rtype: str
        """
        return self._SemanticEagerness

    @SemanticEagerness.setter
    def SemanticEagerness(self, SemanticEagerness):
        self._SemanticEagerness = SemanticEagerness


    def _deserialize(self, params):
        self._SemanticEagerness = params.get("SemanticEagerness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationRequest(AbstractModel):
    r"""UpdateAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task Unique ID
        :type TaskId: str
        :param _WelcomeMessage: If you do not fill in the form, no update will be performed. Welcome message from the robot
        :type WelcomeMessage: str
        :param _InterruptMode: If not filled in, no update will be performed. Intelligent interruption mode, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :type InterruptMode: int
        :param _InterruptSpeechDuration: If not filled in, no update will be performed. Used when InterruptMode is 0, the unit is milliseconds, and the default is 500ms. It means that the server will interrupt when it detects a voice that lasts for InterruptSpeechDuration milliseconds.
        :type InterruptSpeechDuration: int
        :param _LLMConfig: If not filled in, no update will be performed. For LLM configuration, see the StartAIConversation API for details.
        :type LLMConfig: str
        :param _TTSConfig: If not filled in, no update will be performed. For TTS configuration, see the StartAIConversation API for details.
        :type TTSConfig: str
        """
        self._TaskId = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._LLMConfig = None
        self._TTSConfig = None

    @property
    def TaskId(self):
        r"""Task Unique ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def WelcomeMessage(self):
        r"""If you do not fill in the form, no update will be performed. Welcome message from the robot
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        r"""If not filled in, no update will be performed. Intelligent interruption mode, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        r"""If not filled in, no update will be performed. Used when InterruptMode is 0, the unit is milliseconds, and the default is 500ms. It means that the server will interrupt when it detects a voice that lasts for InterruptSpeechDuration milliseconds.
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def LLMConfig(self):
        r"""If not filled in, no update will be performed. For LLM configuration, see the StartAIConversation API for details.
        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""If not filled in, no update will be performed. For TTS configuration, see the StartAIConversation API for details.
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationResponse(AbstractModel):
    r"""UpdateAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdatePublishCdnStreamRequest(AbstractModel):
    r"""UpdatePublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _SequenceNumber: The sequence of a request. This parameter ensures the requests to change the parameters of the same relaying task are in the correct order. It increases each time a new request is made.
        :type SequenceNumber: int
        :param _WithTranscoding: Whether to transcode the streams. 0: No; 1: Yes.
        :type WithTranscoding: int
        :param _AudioParams: Pass this parameter to change the users whose audios are mixed. If you do not pass this parameter, no changes will be made.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: Pass this parameter to change video parameters other than the codec, including the video layout, background image, background color, and watermark information. This parameter is valid only if streams are transcoded. If you do not pass it, no changes will be made.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: Pass this parameter to change the single stream that is relayed. This parameter is valid only if streams are not transcoded. If you do not pass this parameter, no changes will be made.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: Pass this parameter to change the CDNs to relay to. If you do not pass this parameter, no changes will be made.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: The stream mixing SEI parameters.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: The information of the room to which streams are relayed.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SequenceNumber = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None

    @property
    def SdkAppId(self):
        r"""The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SequenceNumber(self):
        r"""The sequence of a request. This parameter ensures the requests to change the parameters of the same relaying task are in the correct order. It increases each time a new request is made.
        :rtype: int
        """
        return self._SequenceNumber

    @SequenceNumber.setter
    def SequenceNumber(self, SequenceNumber):
        self._SequenceNumber = SequenceNumber

    @property
    def WithTranscoding(self):
        r"""Whether to transcode the streams. 0: No; 1: Yes.
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        r"""Pass this parameter to change the users whose audios are mixed. If you do not pass this parameter, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        r"""Pass this parameter to change video parameters other than the codec, including the video layout, background image, background color, and watermark information. This parameter is valid only if streams are transcoded. If you do not pass it, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        r"""Pass this parameter to change the single stream that is relayed. This parameter is valid only if streams are not transcoded. If you do not pass this parameter, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        r"""Pass this parameter to change the CDNs to relay to. If you do not pass this parameter, no changes will be made.
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        r"""The stream mixing SEI parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        r"""The information of the room to which streams are relayed.
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SequenceNumber = params.get("SequenceNumber")
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePublishCdnStreamResponse(AbstractModel):
    r"""UpdatePublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpdateStreamIngestRequest(AbstractModel):
    r"""UpdateStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the task, will return after successfully starting the task.
        :type TaskId: str
        :param _StreamUrl: The new url of the media resource.
        :type StreamUrl: str
        :param _Volume: Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :type Volume: int
        :param _IsPause: Whether to pause, the default value of false indicates no pause. During the pause, the task is still in progress and is billed. If you want to terminate the task, please call the stop interface.
        :type IsPause: bool
        """
        self._SdkAppId = None
        self._TaskId = None
        self._StreamUrl = None
        self._Volume = None
        self._IsPause = None

    @property
    def SdkAppId(self):
        r"""The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""The unique Id of the task, will return after successfully starting the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StreamUrl(self):
        r"""The new url of the media resource.
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def Volume(self):
        r"""Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def IsPause(self):
        r"""Whether to pause, the default value of false indicates no pause. During the pause, the task is still in progress and is billed. If you want to terminate the task, please call the stop interface.
        :rtype: bool
        """
        return self._IsPause

    @IsPause.setter
    def IsPause(self, IsPause):
        self._IsPause = IsPause


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._StreamUrl = params.get("StreamUrl")
        self._Volume = params.get("Volume")
        self._IsPause = params.get("IsPause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStreamIngestResponse(AbstractModel):
    r"""UpdateStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._RequestId = params.get("RequestId")


class UserInformation(AbstractModel):
    r"""The user information, including when the user entered/left the room.

    """

    def __init__(self):
        r"""
        :param _RoomStr: The room ID.
        :type RoomStr: str
        :param _UserId: The user ID.
        :type UserId: str
        :param _JoinTs: The time when the user entered the room.
        :type JoinTs: int
        :param _LeaveTs: The time when the user left the room. If the user is still in the room, the current time will be returned.
        :type LeaveTs: int
        :param _DeviceType: The device type.
        :type DeviceType: str
        :param _SdkVersion: The SDK version number.
        :type SdkVersion: str
        :param _ClientIp: The client IP address.
        :type ClientIp: str
        :param _Finished: Whether a user has left the room.
        :type Finished: bool
        """
        self._RoomStr = None
        self._UserId = None
        self._JoinTs = None
        self._LeaveTs = None
        self._DeviceType = None
        self._SdkVersion = None
        self._ClientIp = None
        self._Finished = None

    @property
    def RoomStr(self):
        r"""The room ID.
        :rtype: str
        """
        return self._RoomStr

    @RoomStr.setter
    def RoomStr(self, RoomStr):
        self._RoomStr = RoomStr

    @property
    def UserId(self):
        r"""The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def JoinTs(self):
        r"""The time when the user entered the room.
        :rtype: int
        """
        return self._JoinTs

    @JoinTs.setter
    def JoinTs(self, JoinTs):
        self._JoinTs = JoinTs

    @property
    def LeaveTs(self):
        r"""The time when the user left the room. If the user is still in the room, the current time will be returned.
        :rtype: int
        """
        return self._LeaveTs

    @LeaveTs.setter
    def LeaveTs(self, LeaveTs):
        self._LeaveTs = LeaveTs

    @property
    def DeviceType(self):
        r"""The device type.
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SdkVersion(self):
        r"""The SDK version number.
        :rtype: str
        """
        return self._SdkVersion

    @SdkVersion.setter
    def SdkVersion(self, SdkVersion):
        self._SdkVersion = SdkVersion

    @property
    def ClientIp(self):
        r"""The client IP address.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Finished(self):
        r"""Whether a user has left the room.
        :rtype: bool
        """
        return self._Finished

    @Finished.setter
    def Finished(self, Finished):
        self._Finished = Finished


    def _deserialize(self, params):
        self._RoomStr = params.get("RoomStr")
        self._UserId = params.get("UserId")
        self._JoinTs = params.get("JoinTs")
        self._LeaveTs = params.get("LeaveTs")
        self._DeviceType = params.get("DeviceType")
        self._SdkVersion = params.get("SdkVersion")
        self._ClientIp = params.get("ClientIp")
        self._Finished = params.get("Finished")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMediaStream(AbstractModel):
    r"""The stream information.

    """

    def __init__(self):
        r"""
        :param _UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param _StreamType: The stream type. 0: Camera; 1: Screen sharing. If you do not pass this parameter, 0 will be used.
        :type StreamType: int
        """
        self._UserInfo = None
        self._StreamType = None

    @property
    def UserInfo(self):
        r"""The user information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def StreamType(self):
        r"""The stream type. 0: Camera; 1: Screen sharing. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._StreamType = params.get("StreamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncode(AbstractModel):
    r"""The video encoding parameters.

    """

    def __init__(self):
        r"""
        :param _Width: The width of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1920].
        :type Width: int
        :param _Height: Output stream is high and required for audio and video output. value ranges from 0 to 1920. unit: pixel value.
        :type Height: int
        :param _Fps: The frame rate (fps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 60].
        :type Fps: int
        :param _BitRate: The bitrate (Kbps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 10000].
        :type BitRate: int
        :param _Gop: The GOP (seconds) of the output stream. This parameter is required if audio and video are relayed. Value range: [1, 5].
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""The width of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1920].
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""Output stream is high and required for audio and video output. value ranges from 0 to 1920. unit: pixel value.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""The frame rate (fps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 60].
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""The bitrate (Kbps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 10000].
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""The GOP (seconds) of the output stream. This parameter is required if audio and video are relayed. Value range: [1, 5].
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodeParams(AbstractModel):
    r"""Video transcoding parameters

    """

    def __init__(self):
        r"""
        :param _Width: Width. Value range [0,1920], unit is pixel value.
        :type Width: int
        :param _Height: Height. Value range [0,1080], unit is pixel value.
        :type Height: int
        :param _Fps: Frame Rate. Value range [1,60], indicating that the frame rate can be selected from 1 to 60fps.
        :type Fps: int
        :param _BitRate: Bitrate. Value range [1,10000], unit is kbps.
        :type BitRate: int
        :param _Gop: Gop. Value range [1,2], unit is second.
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""Width. Value range [0,1920], unit is pixel value.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""Height. Value range [0,1080], unit is pixel value.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""Frame Rate. Value range [1,60], indicating that the frame rate can be selected from 1 to 60fps.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""Bitrate. Value range [1,10000], unit is kbps.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""Gop. Value range [1,2], unit is second.
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    r"""The video transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param _Width: The video width in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `360`.
        :type Width: int
        :param _Height: The video height in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `640`.
        :type Height: int
        :param _Fps: The video frame rate. Value range: [1, 60]. Default: 15.
        :type Fps: int
        :param _BitRate: The video bitrate (bps). Value range: [64000, 8192000]. Default: 550000.
        :type BitRate: int
        :param _Gop: The keyframe interval (seconds). Default value: 10.
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""The video width in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `360`.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""The video height in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `640`.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""The video frame rate. Value range: [1, 60]. Default: 15.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""The video bitrate (bps). Value range: [64000, 8192000]. Default: 550000.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""The keyframe interval (seconds). Default value: 10.
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Voice(AbstractModel):
    r"""TTS sound parameter configuration.

    """

    def __init__(self):
        r"""
        :param _VoiceId: Voice ID, can be obtained from the timbre list or use a custom voice ID generated by sound clone.
        :type VoiceId: str
        :param _Speed: Speech speed adjustment. 0.5 for half speed, 2.0 for 2x speed, and 1.0 for normal speed. value range: [0.5, 2.0]. default: 1.0.
        :type Speed: float
        :param _Volume: Audio volume adjustment, where 0 indicates mute and 10 indicates maximum volume. recommended to keep the default value of 1.0. value range: [0,10]. default: 1.0.
        :type Volume: float
        :param _Pitch: Pitch adjustment. negative value makes the sound deeper, positive value makes the sound sharper. 0 indicates the original pitch. value range: [-12, 12]. default: 0.
        :type Pitch: int
        """
        self._VoiceId = None
        self._Speed = None
        self._Volume = None
        self._Pitch = None

    @property
    def VoiceId(self):
        r"""Voice ID, can be obtained from the timbre list or use a custom voice ID generated by sound clone.
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Speed(self):
        r"""Speech speed adjustment. 0.5 for half speed, 2.0 for 2x speed, and 1.0 for normal speed. value range: [0.5, 2.0]. default: 1.0.
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""Audio volume adjustment, where 0 indicates mute and 10 indicates maximum volume. recommended to keep the default value of 1.0. value range: [0,10]. default: 1.0.
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Pitch(self):
        r"""Pitch adjustment. negative value makes the sound deeper, positive value makes the sound sharper. 0 indicates the original pitch. value range: [-12, 12]. default: 0.
        :rtype: int
        """
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        self._Pitch = params.get("Pitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceCloneRequest(AbstractModel):
    r"""VoiceClone request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Specifies the SdkAppId of TRTC.
        :type SdkAppId: int
        :param _VoiceName: Sound clone name. only digits, letters, and underscores are allowed with a maximum of 36 characters.
        :type VoiceName: str
        :param _PromptAudio: The reference audio for voice cloning must be a base64 string of a 16k mono wav file with length between 10–180 seconds.
        :type PromptAudio: str
        :param _APIKey: API key for TTS.
        :type APIKey: str
        :param _PromptText: Reference text for voice cloning. specifies the text corresponding to the reference audio.
        :type PromptText: str
        :param _Model: TTS model: flow_01_turbo, flow_01_ex.
        :type Model: str
        :param _Language: Language parameter, empty by default. see: (ISO 639-1).
        :type Language: str
        """
        self._SdkAppId = None
        self._VoiceName = None
        self._PromptAudio = None
        self._APIKey = None
        self._PromptText = None
        self._Model = None
        self._Language = None

    @property
    def SdkAppId(self):
        r"""Specifies the SdkAppId of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def VoiceName(self):
        r"""Sound clone name. only digits, letters, and underscores are allowed with a maximum of 36 characters.
        :rtype: str
        """
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def PromptAudio(self):
        r"""The reference audio for voice cloning must be a base64 string of a 16k mono wav file with length between 10–180 seconds.
        :rtype: str
        """
        return self._PromptAudio

    @PromptAudio.setter
    def PromptAudio(self, PromptAudio):
        self._PromptAudio = PromptAudio

    @property
    def APIKey(self):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        r"""API key for TTS.
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        self._APIKey = APIKey

    @property
    def PromptText(self):
        r"""Reference text for voice cloning. specifies the text corresponding to the reference audio.
        :rtype: str
        """
        return self._PromptText

    @PromptText.setter
    def PromptText(self, PromptText):
        self._PromptText = PromptText

    @property
    def Model(self):
        r"""TTS model: flow_01_turbo, flow_01_ex.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""Language parameter, empty by default. see: (ISO 639-1).
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._VoiceName = params.get("VoiceName")
        self._PromptAudio = params.get("PromptAudio")
        self._APIKey = params.get("APIKey")
        self._PromptText = params.get("PromptText")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceCloneResponse(AbstractModel):
    r"""VoiceClone response structure.

    """

    def __init__(self):
        r"""
        :param _VoiceId: Cloned voice type ID. specifies the ID for performing text to speech.
        :type VoiceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VoiceId = None
        self._RequestId = None

    @property
    def VoiceId(self):
        r"""Cloned voice type ID. specifies the ID for performing text to speech.
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

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
        self._VoiceId = params.get("VoiceId")
        self._RequestId = params.get("RequestId")


class VoicePrint(AbstractModel):
    r"""Voiceprint configuration parameters.

    """

    def __init__(self):
        r"""
        :param _Mode: The default is 0, which means voiceprint is not enabled. 1 means voiceprint is enabled, at which point you need to fill in the voiceprint id.
        :type Mode: int
        :param _IdList: VoicePrint Mode requires filling in when set to 1. currently only support a VoicePrint id.
        :type IdList: list of str
        """
        self._Mode = None
        self._IdList = None

    @property
    def Mode(self):
        r"""The default is 0, which means voiceprint is not enabled. 1 means voiceprint is enabled, at which point you need to fill in the voiceprint id.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def IdList(self):
        r"""VoicePrint Mode requires filling in when set to 1. currently only support a VoicePrint id.
        :rtype: list of str
        """
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMark(AbstractModel):
    r"""The watermark layout.

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: The watermark type. 0 (default): image; 1: text; 2: timestamp.
        :type WaterMarkType: int
        :param _WaterMarkImage: The information of watermark images. This parameter is required if the watermark type is image.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        :param _WaterMarkChar: The information of the text watermark. This parameter is required if `WaterMarkType` is `1`.
        :type WaterMarkChar: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        :param _WaterMarkTimestamp: The information of the timestamp watermark. This parameter is required if `WaterMarkType` is `2`.
        :type WaterMarkTimestamp: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkChar = None
        self._WaterMarkTimestamp = None

    @property
    def WaterMarkType(self):
        r"""The watermark type. 0 (default): image; 1: text; 2: timestamp.
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        r"""The information of watermark images. This parameter is required if the watermark type is image.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkChar(self):
        r"""The information of the text watermark. This parameter is required if `WaterMarkType` is `1`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        """
        return self._WaterMarkChar

    @WaterMarkChar.setter
    def WaterMarkChar(self, WaterMarkChar):
        self._WaterMarkChar = WaterMarkChar

    @property
    def WaterMarkTimestamp(self):
        r"""The information of the timestamp watermark. This parameter is required if `WaterMarkType` is `2`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        return self._WaterMarkTimestamp

    @WaterMarkTimestamp.setter
    def WaterMarkTimestamp(self, WaterMarkTimestamp):
        self._WaterMarkTimestamp = WaterMarkTimestamp


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = WaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkChar") is not None:
            self._WaterMarkChar = WaterMarkChar()
            self._WaterMarkChar._deserialize(params.get("WaterMarkChar"))
        if params.get("WaterMarkTimestamp") is not None:
            self._WaterMarkTimestamp = WaterMarkTimestamp()
            self._WaterMarkTimestamp._deserialize(params.get("WaterMarkTimestamp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkChar(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Top: The Y coordinate of the text watermark from the top left.
        :type Top: int
        :param _Left: The X coordinate of the text watermark from the top left.
        :type Left: int
        :param _Width: The watermark width (pixels).
        :type Width: int
        :param _Height: The watermark height (pixels).
        :type Height: int
        :param _Chars: The text.
        :type Chars: str
        :param _FontSize: The font size (pixels). The default value is `14`.
        :type FontSize: int
        :param _FontColor: The text color. The default color is white.
        :type FontColor: str
        :param _BackGroundColor: The background color. If this parameter is empty, the background will be transparent (default).
        :type BackGroundColor: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._Chars = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None

    @property
    def Top(self):
        r"""The Y coordinate of the text watermark from the top left.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""The X coordinate of the text watermark from the top left.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""The watermark width (pixels).
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""The watermark height (pixels).
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Chars(self):
        r"""The text.
        :rtype: str
        """
        return self._Chars

    @Chars.setter
    def Chars(self, Chars):
        self._Chars = Chars

    @property
    def FontSize(self):
        r"""The font size (pixels). The default value is `14`.
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        r"""The text color. The default color is white.
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        r"""The background color. If this parameter is empty, the background will be transparent (default).
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Chars = params.get("Chars")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkImage(AbstractModel):
    r"""The information of watermark images.

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: The download url address supports only jpg, png, and jpeg with a size limit of no more than 5M. note that the url must carry the format extension and supports only specific strings within the range of a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '='.
        :type WaterMarkUrl: str
        :param _Top: The Y axis of the image's top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas height.
        :type Top: int
        :param _Left: The X axis of the image’s top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas width.
        :type Left: int
        :param _Width: The relative width of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param _Height: The relative height of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        """
        self._WaterMarkUrl = None
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None

    @property
    def WaterMarkUrl(self):
        r"""The download url address supports only jpg, png, and jpeg with a size limit of no more than 5M. note that the url must carry the format extension and supports only specific strings within the range of a-z, a-z, 0-9, '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!', '&', '(', ')', '*', '+', ',', '%', '='.
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def Top(self):
        r"""The Y axis of the image's top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas height.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""The X axis of the image’s top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas width.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""The relative width of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""The relative height of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkTimestamp(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Pos: The position of the timestamp watermark. Valid values: `0` (top left), `1` (top right), `2` (bottom left), `3` (bottom right), `4` (top center), `5` (bottom center), `6` (center).
        :type Pos: int
        :param _TimeZone: The time zone. The default is UTC+8.
        :type TimeZone: int
        """
        self._Pos = None
        self._TimeZone = None

    @property
    def Pos(self):
        r"""The position of the timestamp watermark. Valid values: `0` (top left), `1` (top right), `2` (bottom left), `3` (bottom right), `4` (top center), `5` (bottom center), `6` (center).
        :rtype: int
        """
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos

    @property
    def TimeZone(self):
        r"""The time zone. The default is UTC+8.
        :rtype: int
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Pos = params.get("Pos")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebRecordVideoParams(AbstractModel):
    r"""Recording control parameters.

    """

    def __init__(self):
        r"""
        :param _Width: Recording image width defaults to 1280, with a value range of [0, 1920].
        :type Width: int
        :param _Height: Recording image height, defaults to 720, in the range of [0, 1080].
        :type Height: int
        :param _Format: Specify output format. valid values: hls, mp4. this parameter is invalid when storing in VOD. to store in VOD, set MediaType in TencentVod (https://www.tencentcloud.comom/document/api/647/44055?from_cn_redirect=1#TencentVod).

        :type Format: str
        :param _MaxMediaFileDuration: If the file format is aac or mp4, the system will automatically split the video file when the length limit is exceeded. measurement unit: minute. defaults to 1440 min (24h). value range: 1-1440. [single file limit is 2G. if file size exceeds 2G or recording duration exceeds 24h, the file will be automatically split.].
Hls format recording. this parameter is not effective.
Example value: 1440.
        :type MaxMediaFileDuration: int
        """
        self._Width = None
        self._Height = None
        self._Format = None
        self._MaxMediaFileDuration = None

    @property
    def Width(self):
        r"""Recording image width defaults to 1280, with a value range of [0, 1920].
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""Recording image height, defaults to 720, in the range of [0, 1080].
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Format(self):
        r"""Specify output format. valid values: hls, mp4. this parameter is invalid when storing in VOD. to store in VOD, set MediaType in TencentVod (https://www.tencentcloud.comom/document/api/647/44055?from_cn_redirect=1#TencentVod).

        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def MaxMediaFileDuration(self):
        r"""If the file format is aac or mp4, the system will automatically split the video file when the length limit is exceeded. measurement unit: minute. defaults to 1440 min (24h). value range: 1-1440. [single file limit is 2G. if file size exceeds 2G or recording duration exceeds 24h, the file will be automatically split.].
Hls format recording. this parameter is not effective.
Example value: 1440.
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Format = params.get("Format")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        