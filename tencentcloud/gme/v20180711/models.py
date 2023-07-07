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


class AppStatisticsItem(AbstractModel):
    """Application usage statistics

    """

    def __init__(self):
        r"""
        :param _RealtimeSpeechStatisticsItem: Voice Chat statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param _VoiceMessageStatisticsItem: Voice Message statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param _VoiceFilterStatisticsItem: Phrase Filtering statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param _Date: Reference period
        :type Date: str
        :param _AudioTextStatisticsItem: Recording-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AudioTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.AudioTextStatisticsItem`
        :param _StreamTextStatisticsItem: Stream-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StreamTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.StreamTextStatisticsItem`
        :param _OverseaTextStatisticsItem: Usage statistics of Voice-to-Text of outside-MLC requests
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OverseaTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.OverseaTextStatisticsItem`
        :param _RealtimeTextStatisticsItem: Real-time Voice-to-Text usage statistics
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RealtimeTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealtimeTextStatisticsItem`
        """
        self._RealtimeSpeechStatisticsItem = None
        self._VoiceMessageStatisticsItem = None
        self._VoiceFilterStatisticsItem = None
        self._Date = None
        self._AudioTextStatisticsItem = None
        self._StreamTextStatisticsItem = None
        self._OverseaTextStatisticsItem = None
        self._RealtimeTextStatisticsItem = None

    @property
    def RealtimeSpeechStatisticsItem(self):
        return self._RealtimeSpeechStatisticsItem

    @RealtimeSpeechStatisticsItem.setter
    def RealtimeSpeechStatisticsItem(self, RealtimeSpeechStatisticsItem):
        self._RealtimeSpeechStatisticsItem = RealtimeSpeechStatisticsItem

    @property
    def VoiceMessageStatisticsItem(self):
        return self._VoiceMessageStatisticsItem

    @VoiceMessageStatisticsItem.setter
    def VoiceMessageStatisticsItem(self, VoiceMessageStatisticsItem):
        self._VoiceMessageStatisticsItem = VoiceMessageStatisticsItem

    @property
    def VoiceFilterStatisticsItem(self):
        return self._VoiceFilterStatisticsItem

    @VoiceFilterStatisticsItem.setter
    def VoiceFilterStatisticsItem(self, VoiceFilterStatisticsItem):
        self._VoiceFilterStatisticsItem = VoiceFilterStatisticsItem

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AudioTextStatisticsItem(self):
        return self._AudioTextStatisticsItem

    @AudioTextStatisticsItem.setter
    def AudioTextStatisticsItem(self, AudioTextStatisticsItem):
        self._AudioTextStatisticsItem = AudioTextStatisticsItem

    @property
    def StreamTextStatisticsItem(self):
        return self._StreamTextStatisticsItem

    @StreamTextStatisticsItem.setter
    def StreamTextStatisticsItem(self, StreamTextStatisticsItem):
        self._StreamTextStatisticsItem = StreamTextStatisticsItem

    @property
    def OverseaTextStatisticsItem(self):
        return self._OverseaTextStatisticsItem

    @OverseaTextStatisticsItem.setter
    def OverseaTextStatisticsItem(self, OverseaTextStatisticsItem):
        self._OverseaTextStatisticsItem = OverseaTextStatisticsItem

    @property
    def RealtimeTextStatisticsItem(self):
        return self._RealtimeTextStatisticsItem

    @RealtimeTextStatisticsItem.setter
    def RealtimeTextStatisticsItem(self, RealtimeTextStatisticsItem):
        self._RealtimeTextStatisticsItem = RealtimeTextStatisticsItem


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self._RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self._RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self._VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self._VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self._VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self._VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self._Date = params.get("Date")
        if params.get("AudioTextStatisticsItem") is not None:
            self._AudioTextStatisticsItem = AudioTextStatisticsItem()
            self._AudioTextStatisticsItem._deserialize(params.get("AudioTextStatisticsItem"))
        if params.get("StreamTextStatisticsItem") is not None:
            self._StreamTextStatisticsItem = StreamTextStatisticsItem()
            self._StreamTextStatisticsItem._deserialize(params.get("StreamTextStatisticsItem"))
        if params.get("OverseaTextStatisticsItem") is not None:
            self._OverseaTextStatisticsItem = OverseaTextStatisticsItem()
            self._OverseaTextStatisticsItem._deserialize(params.get("OverseaTextStatisticsItem"))
        if params.get("RealtimeTextStatisticsItem") is not None:
            self._RealtimeTextStatisticsItem = RealtimeTextStatisticsItem()
            self._RealtimeTextStatisticsItem._deserialize(params.get("RealtimeTextStatisticsItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDataStatistics(AbstractModel):
    """Application statistics

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID
        :type BizId: int
        :param _DauDataNum: Number of DAU metrics
        :type DauDataNum: int
        :param _DauDataMainland: DAUs in the Chinese mainland
        :type DauDataMainland: list of StatisticsItem
        :param _DauDataOversea: DAUs outside the Chinese mainland
        :type DauDataOversea: list of StatisticsItem
        :param _DauDataSum: Total DAUs
        :type DauDataSum: list of StatisticsItem
        :param _DurationDataNum: Number of Voice Chat metrics
        :type DurationDataNum: int
        :param _DurationDataMainland: Duration of Voice Chat in the Chinese mainland (in minutes)
        :type DurationDataMainland: list of StatisticsItem
        :param _DurationDataOversea: Duration of Voice Chat outside the Chinese mainland (in minutes)
        :type DurationDataOversea: list of StatisticsItem
        :param _DurationDataSum: Total duration of Voice Chat (in minutes)
        :type DurationDataSum: list of StatisticsItem
        :param _PcuDataNum: Number of PCU metrics
        :type PcuDataNum: int
        :param _PcuDataMainland: PCUs in the Chinese mainland
        :type PcuDataMainland: list of StatisticsItem
        :param _PcuDataOversea: PCUs outside the Chinese mainland
        :type PcuDataOversea: list of StatisticsItem
        :param _PcuDataSum: Total PCUs
        :type PcuDataSum: list of StatisticsItem
        """
        self._BizId = None
        self._DauDataNum = None
        self._DauDataMainland = None
        self._DauDataOversea = None
        self._DauDataSum = None
        self._DurationDataNum = None
        self._DurationDataMainland = None
        self._DurationDataOversea = None
        self._DurationDataSum = None
        self._PcuDataNum = None
        self._PcuDataMainland = None
        self._PcuDataOversea = None
        self._PcuDataSum = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def DauDataNum(self):
        return self._DauDataNum

    @DauDataNum.setter
    def DauDataNum(self, DauDataNum):
        self._DauDataNum = DauDataNum

    @property
    def DauDataMainland(self):
        return self._DauDataMainland

    @DauDataMainland.setter
    def DauDataMainland(self, DauDataMainland):
        self._DauDataMainland = DauDataMainland

    @property
    def DauDataOversea(self):
        return self._DauDataOversea

    @DauDataOversea.setter
    def DauDataOversea(self, DauDataOversea):
        self._DauDataOversea = DauDataOversea

    @property
    def DauDataSum(self):
        return self._DauDataSum

    @DauDataSum.setter
    def DauDataSum(self, DauDataSum):
        self._DauDataSum = DauDataSum

    @property
    def DurationDataNum(self):
        return self._DurationDataNum

    @DurationDataNum.setter
    def DurationDataNum(self, DurationDataNum):
        self._DurationDataNum = DurationDataNum

    @property
    def DurationDataMainland(self):
        return self._DurationDataMainland

    @DurationDataMainland.setter
    def DurationDataMainland(self, DurationDataMainland):
        self._DurationDataMainland = DurationDataMainland

    @property
    def DurationDataOversea(self):
        return self._DurationDataOversea

    @DurationDataOversea.setter
    def DurationDataOversea(self, DurationDataOversea):
        self._DurationDataOversea = DurationDataOversea

    @property
    def DurationDataSum(self):
        return self._DurationDataSum

    @DurationDataSum.setter
    def DurationDataSum(self, DurationDataSum):
        self._DurationDataSum = DurationDataSum

    @property
    def PcuDataNum(self):
        return self._PcuDataNum

    @PcuDataNum.setter
    def PcuDataNum(self, PcuDataNum):
        self._PcuDataNum = PcuDataNum

    @property
    def PcuDataMainland(self):
        return self._PcuDataMainland

    @PcuDataMainland.setter
    def PcuDataMainland(self, PcuDataMainland):
        self._PcuDataMainland = PcuDataMainland

    @property
    def PcuDataOversea(self):
        return self._PcuDataOversea

    @PcuDataOversea.setter
    def PcuDataOversea(self, PcuDataOversea):
        self._PcuDataOversea = PcuDataOversea

    @property
    def PcuDataSum(self):
        return self._PcuDataSum

    @PcuDataSum.setter
    def PcuDataSum(self, PcuDataSum):
        self._PcuDataSum = PcuDataSum


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._DauDataNum = params.get("DauDataNum")
        if params.get("DauDataMainland") is not None:
            self._DauDataMainland = []
            for item in params.get("DauDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataMainland.append(obj)
        if params.get("DauDataOversea") is not None:
            self._DauDataOversea = []
            for item in params.get("DauDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataOversea.append(obj)
        if params.get("DauDataSum") is not None:
            self._DauDataSum = []
            for item in params.get("DauDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataSum.append(obj)
        self._DurationDataNum = params.get("DurationDataNum")
        if params.get("DurationDataMainland") is not None:
            self._DurationDataMainland = []
            for item in params.get("DurationDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataMainland.append(obj)
        if params.get("DurationDataOversea") is not None:
            self._DurationDataOversea = []
            for item in params.get("DurationDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataOversea.append(obj)
        if params.get("DurationDataSum") is not None:
            self._DurationDataSum = []
            for item in params.get("DurationDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataSum.append(obj)
        self._PcuDataNum = params.get("PcuDataNum")
        if params.get("PcuDataMainland") is not None:
            self._PcuDataMainland = []
            for item in params.get("PcuDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataMainland.append(obj)
        if params.get("PcuDataOversea") is not None:
            self._PcuDataOversea = []
            for item in params.get("PcuDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataOversea.append(obj)
        if params.get("PcuDataSum") is not None:
            self._PcuDataSum = []
            for item in params.get("PcuDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataSum.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrConf(AbstractModel):
    """Configuration information of Speech-to-Text

    """

    def __init__(self):
        r"""
        :param _Status: Speech-to-Text status. Valid values: `open`, `close`.
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTextStatisticsItem(AbstractModel):
    """Recording-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param _Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    """CreateApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppName: Application name
        :type AppName: str
        :param _ProjectId: Tencent Cloud project ID. Default value: 0, which means that the default project is used.
        :type ProjectId: int
        :param _EngineList: List of engines to be supported.
Valid values: `android`, `ios`, `unity`, `cocos`, `unreal`, `windows`. All values are selected by default.
        :type EngineList: list of str
        :param _RegionList: List of regions.
Valid values: `mainland` (Chinese mainland), `hmt` (Hong Kong, Macao and Taiwan (China)), `sea` (Southeast Asia), `na` (North America), `eu` (Europe), `jpkr` (Japan, Korea and Asia Pacific), `sa` (South America), `oc` (Oceania), `me` (Middle East). All values are selected by default.
        :type RegionList: list of str
        :param _RealtimeSpeechConf: Configuration information of Voice Chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param _VoiceMessageConf: Configuration information of Voice Messaging
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param _VoiceFilterConf: Configuration information of Voice Analysis Service
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param _AsrConf: Configuration information of Speech-to-Text
        :type AsrConf: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        :param _Tags: List of tags to be added
        :type Tags: list of Tag
        """
        self._AppName = None
        self._ProjectId = None
        self._EngineList = None
        self._RegionList = None
        self._RealtimeSpeechConf = None
        self._VoiceMessageConf = None
        self._VoiceFilterConf = None
        self._AsrConf = None
        self._Tags = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EngineList(self):
        return self._EngineList

    @EngineList.setter
    def EngineList(self, EngineList):
        self._EngineList = EngineList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RealtimeSpeechConf(self):
        return self._RealtimeSpeechConf

    @RealtimeSpeechConf.setter
    def RealtimeSpeechConf(self, RealtimeSpeechConf):
        self._RealtimeSpeechConf = RealtimeSpeechConf

    @property
    def VoiceMessageConf(self):
        return self._VoiceMessageConf

    @VoiceMessageConf.setter
    def VoiceMessageConf(self, VoiceMessageConf):
        self._VoiceMessageConf = VoiceMessageConf

    @property
    def VoiceFilterConf(self):
        return self._VoiceFilterConf

    @VoiceFilterConf.setter
    def VoiceFilterConf(self, VoiceFilterConf):
        self._VoiceFilterConf = VoiceFilterConf

    @property
    def AsrConf(self):
        return self._AsrConf

    @AsrConf.setter
    def AsrConf(self, AsrConf):
        self._AsrConf = AsrConf

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._ProjectId = params.get("ProjectId")
        self._EngineList = params.get("EngineList")
        self._RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self._RealtimeSpeechConf = RealtimeSpeechConf()
            self._RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self._VoiceMessageConf = VoiceMessageConf()
            self._VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self._VoiceFilterConf = VoiceFilterConf()
            self._VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("AsrConf") is not None:
            self._AsrConf = AsrConf()
            self._AsrConf._deserialize(params.get("AsrConf"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResp(AbstractModel):
    """Output parameters of `CreateApp`

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID, automatically generated by the backend.
        :type BizId: int
        :param _AppName: Application name, the input of `AppName`.
        :type AppName: str
        :param _ProjectId: Project ID, the input of `ProjectId`.
        :type ProjectId: int
        :param _SecretKey: Application key, used to initialize GME SDK.
        :type SecretKey: str
        :param _CreateTime: Timestamp, indicating when the service is created.
        :type CreateTime: int
        :param _RealtimeSpeechConf: Configuration information of Voice Chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param _VoiceMessageConf: Configuration information of Voice Messaging
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param _VoiceFilterConf: Configuration information of Voice Analysis Service
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param _AsrConf: Configuration information of Speech-to-Text
        :type AsrConf: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        """
        self._BizId = None
        self._AppName = None
        self._ProjectId = None
        self._SecretKey = None
        self._CreateTime = None
        self._RealtimeSpeechConf = None
        self._VoiceMessageConf = None
        self._VoiceFilterConf = None
        self._AsrConf = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RealtimeSpeechConf(self):
        return self._RealtimeSpeechConf

    @RealtimeSpeechConf.setter
    def RealtimeSpeechConf(self, RealtimeSpeechConf):
        self._RealtimeSpeechConf = RealtimeSpeechConf

    @property
    def VoiceMessageConf(self):
        return self._VoiceMessageConf

    @VoiceMessageConf.setter
    def VoiceMessageConf(self, VoiceMessageConf):
        self._VoiceMessageConf = VoiceMessageConf

    @property
    def VoiceFilterConf(self):
        return self._VoiceFilterConf

    @VoiceFilterConf.setter
    def VoiceFilterConf(self, VoiceFilterConf):
        self._VoiceFilterConf = VoiceFilterConf

    @property
    def AsrConf(self):
        return self._AsrConf

    @AsrConf.setter
    def AsrConf(self, AsrConf):
        self._AsrConf = AsrConf


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._AppName = params.get("AppName")
        self._ProjectId = params.get("ProjectId")
        self._SecretKey = params.get("SecretKey")
        self._CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self._RealtimeSpeechConf = RealtimeSpeechConf()
            self._RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self._VoiceMessageConf = VoiceMessageConf()
            self._VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self._VoiceFilterConf = VoiceFilterConf()
            self._VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("AsrConf") is not None:
            self._AsrConf = AsrConf()
            self._AsrConf._deserialize(params.get("AsrConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data
        :type Data: :class:`tencentcloud.gme.v20180711.models.CreateAppResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = CreateAppResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteResult(AbstractModel):
    """Result of the operation to delete a room or remove members

    """

    def __init__(self):
        r"""
        :param _Code: Status code. `0`: Succeeded. Others: Failed\
        :type Code: int
        :param _ErrorMsg: Description
        :type ErrorMsg: str
        """
        self._Code = None
        self._ErrorMsg = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberRequest(AbstractModel):
    """DeleteRoomMember request structure.

    """

    def __init__(self):
        r"""
        :param _RoomId: ID of the target room
        :type RoomId: str
        :param _Uids: List of the members to remove
        :type Uids: list of str
        :param _DeleteType: Operation type. `1`: Delete a room; `2`: Remove members
        :type DeleteType: int
        :param _BizId: Application ID
        :type BizId: int
        """
        self._RoomId = None
        self._Uids = None
        self._DeleteType = None
        self._BizId = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Uids(self):
        return self._Uids

    @Uids.setter
    def Uids(self, Uids):
        self._Uids = Uids

    @property
    def DeleteType(self):
        return self._DeleteType

    @DeleteType.setter
    def DeleteType(self, DeleteType):
        self._DeleteType = DeleteType

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Uids = params.get("Uids")
        self._DeleteType = params.get("DeleteType")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberResponse(AbstractModel):
    """DeleteRoomMember response structure.

    """

    def __init__(self):
        r"""
        :param _DeleteResult: Result of the operation to delete a room or remove a member
        :type DeleteResult: :class:`tencentcloud.gme.v20180711.models.DeleteResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeleteResult = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteResult") is not None:
            self._DeleteResult = DeleteResult()
            self._DeleteResult._deserialize(params.get("DeleteResult"))
        self._RequestId = params.get("RequestId")


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _BizId: GME application ID
        :type BizId: int
        :param _StartDate: Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13.
        :type StartDate: str
        :param _EndDate: Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13.
        :type EndDate: str
        :param _Services: List of services to be queried. Valid values: `RealTimeSpeech`, `VoiceMessage`, `VoiceFilter`, `SpeechToText`.
        :type Services: list of str
        """
        self._BizId = None
        self._StartDate = None
        self._EndDate = None
        self._Services = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResp(AbstractModel):
    """Output parameters of application usage statistics

    """

    def __init__(self):
        r"""
        :param _AppStatistics: Application usage statistics
        :type AppStatistics: list of AppStatisticsItem
        """
        self._AppStatistics = None

    @property
    def AppStatistics(self):
        return self._AppStatistics

    @AppStatistics.setter
    def AppStatistics(self, AppStatistics):
        self._AppStatistics = AppStatistics


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self._AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self._AppStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """DescribeAppStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Application usage statistics
        :type Data: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = DescribeAppStatisticsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData request structure.

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID
        :type BizId: int
        :param _StartDate: Data start date in the format of yyyy-mm-dd, such as 2018-07-13.
        :type StartDate: str
        :param _EndDate: Data end date in the format of yyyy-mm-dd, such as 2018-07-13.
        :type EndDate: str
        """
        self._BizId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationDataResponse(AbstractModel):
    """DescribeApplicationData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Application statistics
        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = ApplicationDataStatistics()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordInfoRequest(AbstractModel):
    """DescribeRecordInfo request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
        :type TaskId: int
        :param _BizId: Application ID.
        :type BizId: int
        """
        self._TaskId = None
        self._BizId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordInfoResponse(AbstractModel):
    """DescribeRecordInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RecordInfo: Information about the recording task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordInfo: list of RecordInfo
        :param _RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param _RoomId: Room ID.
        :type RoomId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RecordMode = None
        self._RoomId = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self._RecordInfo = []
            for item in params.get("RecordInfo"):
                obj = RecordInfo()
                obj._deserialize(item)
                self._RecordInfo.append(obj)
        self._RecordMode = params.get("RecordMode")
        self._RoomId = params.get("RoomId")
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo request structure.

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID.
        :type BizId: int
        :param _RoomId: Room ID.
        :type RoomId: str
        """
        self._BizId = None
        self._RoomId = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordMode: int
        :param _SubscribeRecordUserIds: Allowlist or blocklist for stream subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RecordMode = None
        self._SubscribeRecordUserIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def SubscribeRecordUserIds(self):
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        self._RequestId = params.get("RequestId")


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus request structure.

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID, which is generated and returned by the backend after the application creation.
        :type BizId: int
        :param _Status: Application status. Valid values: `open`, `close`.
        :type Status: str
        """
        self._BizId = None
        self._Status = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResp(AbstractModel):
    """Output parameters of `ModifyAppStatus`

    """

    def __init__(self):
        r"""
        :param _BizId: GME application ID
        :type BizId: int
        :param _Status: Application status. Valid values: `open`, `close`.
        :type Status: str
        """
        self._BizId = None
        self._Status = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data
        :type Data: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = ModifyAppStatusResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyRecordInfoRequest(AbstractModel):
    """ModifyRecordInfo request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the ongoing task, which is returned from the `StartRecord` API.
        :type TaskId: int
        :param _RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param _BizId: Application ID.
        :type BizId: int
        :param _SubscribeRecordUserIds: Allowlist or blocklist for stream subscription.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self._TaskId = None
        self._RecordMode = None
        self._BizId = None
        self._SubscribeRecordUserIds = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def SubscribeRecordUserIds(self):
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RecordMode = params.get("RecordMode")
        self._BizId = params.get("BizId")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordInfoResponse(AbstractModel):
    """ModifyRecordInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OverseaTextStatisticsItem(AbstractModel):
    """Usage statistics of Voice-to-Text of outside-MLC requests

    """

    def __init__(self):
        r"""
        :param _Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealTimeSpeechStatisticsItem(AbstractModel):
    """Voice Chat usage statistics

    """

    def __init__(self):
        r"""
        :param _MainLandDau: DAUs in the Chinese mainland
        :type MainLandDau: int
        :param _MainLandPcu: PCUs in the Chinese mainland
        :type MainLandPcu: int
        :param _MainLandDuration: Total duration of use in the Chinese mainland (in minutes)
        :type MainLandDuration: int
        :param _OverseaDau: DAUs outside the Chinese mainland
        :type OverseaDau: int
        :param _OverseaPcu: PCUs outside the Chinese mainland
        :type OverseaPcu: int
        :param _OverseaDuration: Total duration of use outside the Chinese mainland (in minutes)
        :type OverseaDuration: int
        """
        self._MainLandDau = None
        self._MainLandPcu = None
        self._MainLandDuration = None
        self._OverseaDau = None
        self._OverseaPcu = None
        self._OverseaDuration = None

    @property
    def MainLandDau(self):
        return self._MainLandDau

    @MainLandDau.setter
    def MainLandDau(self, MainLandDau):
        self._MainLandDau = MainLandDau

    @property
    def MainLandPcu(self):
        return self._MainLandPcu

    @MainLandPcu.setter
    def MainLandPcu(self, MainLandPcu):
        self._MainLandPcu = MainLandPcu

    @property
    def MainLandDuration(self):
        return self._MainLandDuration

    @MainLandDuration.setter
    def MainLandDuration(self, MainLandDuration):
        self._MainLandDuration = MainLandDuration

    @property
    def OverseaDau(self):
        return self._OverseaDau

    @OverseaDau.setter
    def OverseaDau(self, OverseaDau):
        self._OverseaDau = OverseaDau

    @property
    def OverseaPcu(self):
        return self._OverseaPcu

    @OverseaPcu.setter
    def OverseaPcu(self, OverseaPcu):
        self._OverseaPcu = OverseaPcu

    @property
    def OverseaDuration(self):
        return self._OverseaDuration

    @OverseaDuration.setter
    def OverseaDuration(self, OverseaDuration):
        self._OverseaDuration = OverseaDuration


    def _deserialize(self, params):
        self._MainLandDau = params.get("MainLandDau")
        self._MainLandPcu = params.get("MainLandPcu")
        self._MainLandDuration = params.get("MainLandDuration")
        self._OverseaDau = params.get("OverseaDau")
        self._OverseaPcu = params.get("OverseaPcu")
        self._OverseaDuration = params.get("OverseaDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeSpeechConf(AbstractModel):
    """Configuration information of Voice Chat

    """

    def __init__(self):
        r"""
        :param _Status: Voice Chat status. Valid values: `open`, `close`.
        :type Status: str
        :param _Quality: Voice Chat sound quality type. Valid values: `high` (HD), `ordinary` (SD).
        :type Quality: str
        """
        self._Status = None
        self._Quality = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Quality(self):
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeTextStatisticsItem(AbstractModel):
    """Real-time Voice-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param _Data: Statistical value (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """Information about the recording task in a room.
    Note: This field may return `null`, indicating that no valid values can be obtained.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID. The value is `0` in mixed streams recording mode.
        :type UserId: str
        :param _FileName: Recording filename.
        :type FileName: str
        :param _RecordBeginTime: Recording start time, which is a Unix timestamp. Example: 1234567868.
        :type RecordBeginTime: int
        :param _RecordStatus: Recording status. Valid values: `2`: recording; `10`: to be transcoded; `11`: transcoding; `12`: uploading; `13`: uploaded; `14`: user notified.
        :type RecordStatus: int
        """
        self._UserId = None
        self._FileName = None
        self._RecordBeginTime = None
        self._RecordStatus = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RecordBeginTime(self):
        return self._RecordBeginTime

    @RecordBeginTime.setter
    def RecordBeginTime(self, RecordBeginTime):
        self._RecordBeginTime = RecordBeginTime

    @property
    def RecordStatus(self):
        return self._RecordStatus

    @RecordStatus.setter
    def RecordStatus(self, RecordStatus):
        self._RecordStatus = RecordStatus


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._FileName = params.get("FileName")
        self._RecordBeginTime = params.get("RecordBeginTime")
        self._RecordStatus = params.get("RecordStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneInfo(AbstractModel):
    """Scenario information. Valid values:
    `RealTime`: Voice Chat analysis;
    `VoiceMessage`: Voice Messaging;
    `GMECloudApi`: GME cloud APIs

    """


class StartRecordRequest(AbstractModel):
    """StartRecord request structure.

    """

    def __init__(self):
        r"""
        :param _BizId: Application ID.
        :type BizId: int
        :param _RoomId: Room ID.
        :type RoomId: str
        :param _RecordMode: Recording mode. Valid values: `1`: single stream; `2`: mixed streams; `3`: single stream and mixed streams.
        :type RecordMode: int
        :param _SubscribeRecordUserIds: Allowlist or blocklist for stream subscription. If you do not specify this parameter, the audio streams of all the users in the room are subscribed to by default.
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self._BizId = None
        self._RoomId = None
        self._RecordMode = None
        self._SubscribeRecordUserIds = None

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def SubscribeRecordUserIds(self):
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        self._RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordResponse(AbstractModel):
    """StartRecord response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StatisticsItem(AbstractModel):
    """Usage data unit

    """

    def __init__(self):
        r"""
        :param _StatDate: Date in the format of yyyy-mm-dd, such as 2018-07-13
        :type StatDate: str
        :param _Data: Statistical value
        :type Data: int
        """
        self._StatDate = None
        self._Data = None

    @property
    def StatDate(self):
        return self._StatDate

    @StatDate.setter
    def StatDate(self, StatDate):
        self._StatDate = StatDate

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._StatDate = params.get("StatDate")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordRequest(AbstractModel):
    """StopRecord request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: int
        :param _BizId: Application ID.
        :type BizId: int
        """
        self._TaskId = None
        self._BizId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordResponse(AbstractModel):
    """StopRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StreamTextStatisticsItem(AbstractModel):
    """Stream-to-Text usage statistics

    """

    def __init__(self):
        r"""
        :param _Data: Usage of the service (in seconds)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeRecordUserIds(AbstractModel):
    """Allowlist or blocklist for stream subscription.

    """

    def __init__(self):
        r"""
        :param _UnSubscribeUserIds: Blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audio streams of users 1, 2, and 3. If this parameter is left empty, the audio streams of all users (max 20) in the room will not be subscribed to.
Note: You cannot specify `UnSubscribeAudioUserIds` and `SubscribeAudioUserIds` at the same time.
        :type UnSubscribeUserIds: list of str
        :param _SubscribeUserIds: Allowlist for audio subscription. For example, `["1", "2", "3"]` means to subscribe to the audio streams of users 1, 2, and 3. If this parameter is left empty, the audio streams of all users (max 20) in the room will be subscribed to.
Note: You cannot specify `UnSubscribeAudioUserIds` and `SubscribeAudioUserIds` at the same time.
        :type SubscribeUserIds: list of str
        """
        self._UnSubscribeUserIds = None
        self._SubscribeUserIds = None

    @property
    def UnSubscribeUserIds(self):
        return self._UnSubscribeUserIds

    @UnSubscribeUserIds.setter
    def UnSubscribeUserIds(self, UnSubscribeUserIds):
        self._UnSubscribeUserIds = UnSubscribeUserIds

    @property
    def SubscribeUserIds(self):
        return self._SubscribeUserIds

    @SubscribeUserIds.setter
    def SubscribeUserIds(self, SubscribeUserIds):
        self._SubscribeUserIds = SubscribeUserIds


    def _deserialize(self, params):
        self._UnSubscribeUserIds = params.get("UnSubscribeUserIds")
        self._SubscribeUserIds = params.get("SubscribeUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag list

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterConf(AbstractModel):
    """Configuration information of Phrase Filtering

    """

    def __init__(self):
        r"""
        :param _Status: Phrase Filtering status. Valid values: `open`, `close`.
        :type Status: str
        :param _SceneInfos: Scenario configuration information, such as status and callback URL.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SceneInfos: list of SceneInfo
        """
        self._Status = None
        self._SceneInfos = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SceneInfos(self):
        return self._SceneInfos

    @SceneInfos.setter
    def SceneInfos(self, SceneInfos):
        self._SceneInfos = SceneInfos


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("SceneInfos") is not None:
            self._SceneInfos = []
            for item in params.get("SceneInfos"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterStatisticsItem(AbstractModel):
    """Phrase Filtering usage statistics

    """

    def __init__(self):
        r"""
        :param _Duration: Total duration of phrase filtering (in minutes)
        :type Duration: int
        """
        self._Duration = None

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageConf(AbstractModel):
    """Configuration information of Voice Message Service

    """

    def __init__(self):
        r"""
        :param _Status: Voice Message Service status. Valid values: `open`, `close`.
        :type Status: str
        :param _Language: Language supported for Voice Message Service. Valid values: `all` (all languages), `cnen` (Chinese and English). Default value: `cnen`.
        :type Language: str
        """
        self._Status = None
        self._Language = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageStatisticsItem(AbstractModel):
    """Voice Message Service usage statistics

    """

    def __init__(self):
        r"""
        :param _Dau: DAUs of Voice Message Service
        :type Dau: int
        """
        self._Dau = None

    @property
    def Dau(self):
        return self._Dau

    @Dau.setter
    def Dau(self, Dau):
        self._Dau = Dau


    def _deserialize(self, params):
        self._Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        