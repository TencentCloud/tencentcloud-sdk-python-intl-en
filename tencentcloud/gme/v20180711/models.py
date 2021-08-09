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
        """
        :param RealtimeSpeechStatisticsItem: Voice chat statistics
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`\n        :param VoiceMessageStatisticsItem: Voice messaging statistics
Note: This field may return null, indicating that no valid values can be obtained.\n        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`\n        :param VoiceFilterStatisticsItem: Phrase filtering statistics
Note: This field may return null, indicating that no valid values can be obtained.\n        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`\n        :param Date: Statistical period\n        :type Date: str\n        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self.RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self.RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self.VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self.VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self.VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self.VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDataStatistics(AbstractModel):
    """Application statistics

    """

    def __init__(self):
        """
        :param BizId: Application ID\n        :type BizId: int\n        :param DauDataNum: DAU data\n        :type DauDataNum: int\n        :param DauDataMainland: DAU in Chinese mainland\n        :type DauDataMainland: list of StatisticsItem\n        :param DauDataOversea: DAU outside Chinese mainland\n        :type DauDataOversea: list of StatisticsItem\n        :param DauDataSum: Total DAU\n        :type DauDataSum: list of StatisticsItem\n        :param DurationDataNum: Number of voice chat metrics\n        :type DurationDataNum: int\n        :param DurationDataMainland: Duration of voice chat in Chinese mainland in minutes\n        :type DurationDataMainland: list of StatisticsItem\n        :param DurationDataOversea: Duration of voice chat outside Chinese mainland in minutes\n        :type DurationDataOversea: list of StatisticsItem\n        :param DurationDataSum: Total duration of voice chat in minutes\n        :type DurationDataSum: list of StatisticsItem\n        :param PcuDataNum: PCU data\n        :type PcuDataNum: int\n        :param PcuDataMainland: PCU in Chinese mainland\n        :type PcuDataMainland: list of StatisticsItem\n        :param PcuDataOversea: PCU outside Chinese mainland\n        :type PcuDataOversea: list of StatisticsItem\n        :param PcuDataSum: Total PCU\n        :type PcuDataSum: list of StatisticsItem\n        """
        self.BizId = None
        self.DauDataNum = None
        self.DauDataMainland = None
        self.DauDataOversea = None
        self.DauDataSum = None
        self.DurationDataNum = None
        self.DurationDataMainland = None
        self.DurationDataOversea = None
        self.DurationDataSum = None
        self.PcuDataNum = None
        self.PcuDataMainland = None
        self.PcuDataOversea = None
        self.PcuDataSum = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.DauDataNum = params.get("DauDataNum")
        if params.get("DauDataMainland") is not None:
            self.DauDataMainland = []
            for item in params.get("DauDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataMainland.append(obj)
        if params.get("DauDataOversea") is not None:
            self.DauDataOversea = []
            for item in params.get("DauDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataOversea.append(obj)
        if params.get("DauDataSum") is not None:
            self.DauDataSum = []
            for item in params.get("DauDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataSum.append(obj)
        self.DurationDataNum = params.get("DurationDataNum")
        if params.get("DurationDataMainland") is not None:
            self.DurationDataMainland = []
            for item in params.get("DurationDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataMainland.append(obj)
        if params.get("DurationDataOversea") is not None:
            self.DurationDataOversea = []
            for item in params.get("DurationDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataOversea.append(obj)
        if params.get("DurationDataSum") is not None:
            self.DurationDataSum = []
            for item in params.get("DurationDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataSum.append(obj)
        self.PcuDataNum = params.get("PcuDataNum")
        if params.get("PcuDataMainland") is not None:
            self.PcuDataMainland = []
            for item in params.get("PcuDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataMainland.append(obj)
        if params.get("PcuDataOversea") is not None:
            self.PcuDataOversea = []
            for item in params.get("PcuDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataOversea.append(obj)
        if params.get("PcuDataSum") is not None:
            self.PcuDataSum = []
            for item in params.get("PcuDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataSum.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    """CreateApp request structure.

    """

    def __init__(self):
        """
        :param AppName: Application name\n        :type AppName: str\n        :param ProjectId: Tencent Cloud project ID. Default value: 0, which means the default project\n        :type ProjectId: int\n        :param EngineList: List of engines to be supported. All values are selected by default.\n        :type EngineList: list of str\n        :param RegionList: Service region list. All values are selected by default.\n        :type RegionList: list of str\n        :param RealtimeSpeechConf: Configuration information of voice chat\n        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`\n        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text\n        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`\n        :param VoiceFilterConf: Configuration information of phrase analysis\n        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`\n        :param Tags: List of tags to be added\n        :type Tags: list of Tag\n        """
        self.AppName = None
        self.ProjectId = None
        self.EngineList = None
        self.RegionList = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None
        self.Tags = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.EngineList = params.get("EngineList")
        self.RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp output parameters

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is automatically generated by the backend.\n        :type BizId: int\n        :param AppName: Application name, which is passed through from the `AppName` input parameter\n        :type AppName: str\n        :param ProjectId: Project ID, which is passed through from the entered `ProjectId`\n        :type ProjectId: int\n        :param SecretKey: Application key, which is used when the GME SDK is initialized\n        :type SecretKey: str\n        :param CreateTime: Service creation timestamp\n        :type CreateTime: int\n        :param RealtimeSpeechConf: Configuration information of voice chat\n        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`\n        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text\n        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`\n        :param VoiceFilterConf: Configuration information of phrase analysis\n        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`\n        """
        self.BizId = None
        self.AppName = None
        self.ProjectId = None
        self.SecretKey = None
        self.CreateTime = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.SecretKey = params.get("SecretKey")
        self.CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics request structure.

    """

    def __init__(self):
        """
        :param BizId: GME application ID\n        :type BizId: int\n        :param StartDate: Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13\n        :type StartDate: str\n        :param EndDate: Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13\n        :type EndDate: str\n        :param Services: List of services to be queried. Valid values: RealTimeSpeech, VoiceMessage, VoiceFilter\n        :type Services: list of str\n        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Services = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """Gets application usage statistics output parameters

    """

    def __init__(self):
        """
        :param AppStatistics: Application usage statistics\n        :type AppStatistics: list of AppStatisticsItem\n        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID\n        :type BizId: int\n        :param StartDate: Data start date in the format of yyyy-mm-dd, such as 2018-07-13\n        :type StartDate: str\n        :param EndDate: Data end date in the format of yyyy-mm-dd, such as 2018-07-13\n        :type EndDate: str\n        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationDataResponse(AbstractModel):
    """DescribeApplicationData response structure.

    """

    def __init__(self):
        """
        :param Data: Application statistics\n        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplicationDataStatistics()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeScanResult(AbstractModel):
    """Returned speech detection result

    """

    def __init__(self):
        """
        :param Code: Business return code\n        :type Code: int\n        :param DataId: Unique data ID\n        :type DataId: str\n        :param ScanFinishTime: Detection completion timestamp\n        :type ScanFinishTime: int\n        :param HitFlag: Whether non-compliant information is detected\n        :type HitFlag: bool\n        :param Live: Whether it is a stream\n        :type Live: bool\n        :param Msg: Business return description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Msg: str\n        :param ScanPiece: Detection result, which will be returned if `Code` is 0
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ScanPiece: list of ScanPiece\n        :param ScanStartTime: Detection task submission timestamp\n        :type ScanStartTime: int\n        :param Scenes: Speech detection scenario, which corresponds to the `Scene` at the time of request\n        :type Scenes: list of str\n        :param TaskId: Speech detection task ID, which is assigned by the backend\n        :type TaskId: str\n        :param Url: File or stream address\n        :type Url: str\n        :param Status: Detection task execution result task. Valid values:
<li>Start: task started</li>
<li>Success: task ended successfully</li>
<li>Error: exceptional</li>\n        :type Status: str\n        """
        self.Code = None
        self.DataId = None
        self.ScanFinishTime = None
        self.HitFlag = None
        self.Live = None
        self.Msg = None
        self.ScanPiece = None
        self.ScanStartTime = None
        self.Scenes = None
        self.TaskId = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.DataId = params.get("DataId")
        self.ScanFinishTime = params.get("ScanFinishTime")
        self.HitFlag = params.get("HitFlag")
        self.Live = params.get("Live")
        self.Msg = params.get("Msg")
        if params.get("ScanPiece") is not None:
            self.ScanPiece = []
            for item in params.get("ScanPiece"):
                obj = ScanPiece()
                obj._deserialize(item)
                self.ScanPiece.append(obj)
        self.ScanStartTime = params.get("ScanStartTime")
        self.Scenes = params.get("Scenes")
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is the `AppID` obtained when you create an application in the [console](https://console.cloud.tencent.com/gamegme)\n        :type BizId: int\n        :param TaskIdList: List of IDs of the tasks to be queried. Up to 100 entries can be added in the ID list.\n        :type TaskIdList: list of str\n        :param Limit: Number of task results to be returned. Default value: 10. Maximum value: 500. This parameter will be ignored for large file tasks where all results will be returned\n        :type Limit: int\n        """
        self.BizId = None
        self.TaskIdList = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskIdList = params.get("TaskIdList")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList response structure.

    """

    def __init__(self):
        """
        :param Data: Result of the speech detection task to be queried
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Data: list of DescribeScanResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeScanResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is generated and returned by the backend after application creation.\n        :type BizId: int\n        :param Status: Application status. Valid values: open, close\n        :type Status: str\n        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus API output parameters

    """

    def __init__(self):
        """
        :param BizId: GME application ID\n        :type BizId: int\n        :param Status: Application status. Valid values: open, close\n        :type Status: str\n        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class RealTimeSpeechStatisticsItem(AbstractModel):
    """Voice chat usage statistics

    """

    def __init__(self):
        """
        :param MainLandDau: DAU in Mainland China\n        :type MainLandDau: int\n        :param MainLandPcu: PCU in Mainland China\n        :type MainLandPcu: int\n        :param MainLandDuration: Total duration of use in Mainland China in minutes\n        :type MainLandDuration: int\n        :param OverseaDau: DAU outside Mainland China\n        :type OverseaDau: int\n        :param OverseaPcu: PCU outside Mainland China\n        :type OverseaPcu: int\n        :param OverseaDuration: Total duration of use outside Mainland China in minutes\n        :type OverseaDuration: int\n        """
        self.MainLandDau = None
        self.MainLandPcu = None
        self.MainLandDuration = None
        self.OverseaDau = None
        self.OverseaPcu = None
        self.OverseaDuration = None


    def _deserialize(self, params):
        self.MainLandDau = params.get("MainLandDau")
        self.MainLandPcu = params.get("MainLandPcu")
        self.MainLandDuration = params.get("MainLandDuration")
        self.OverseaDau = params.get("OverseaDau")
        self.OverseaPcu = params.get("OverseaPcu")
        self.OverseaDuration = params.get("OverseaDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeSpeechConf(AbstractModel):
    """Configuration information of voice chat

    """

    def __init__(self):
        """
        :param Status: Voice chat status. Valid values: open, close\n        :type Status: str\n        :param Quality: Voice chat sound quality type. Valid values: high (HD), ordinary (SD). Default value: high. SD sound quality is only available to allowllisted users. To try it out, please contact your Tencent Cloud rep.\n        :type Quality: str\n        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDetail(AbstractModel):
    """Speech detection details

    """

    def __init__(self):
        """
        :param Label: Violation scenario. For more information, please see the definition of <a href="https://intl.cloud.tencent.com/document/product/607/37622?from_cn_redirect=1#Label_Value">Label</a>\n        :type Label: str\n        :param Rate: Confidence score in scenario. Value range: [0.00,100.00]. The higher the score, the more likely the content is non-compliant\n        :type Rate: str\n        :param KeyWord: Non-compliant keyword\n        :type KeyWord: str\n        :param StartTime: Start time offset in milliseconds from 0 of keyword in audio\n        :type StartTime: int\n        :param EndTime: End time offset in milliseconds from 0 of keyword in audio\n        :type EndTime: int\n        """
        self.Label = None
        self.Rate = None
        self.KeyWord = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Rate = params.get("Rate")
        self.KeyWord = params.get("KeyWord")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanPiece(AbstractModel):
    """Speech detection result, which will be returned if `Code` is 0

    """

    def __init__(self):
        """
        :param DumpUrl: Audio retention address, which will be returned for stream detection. The audio will be retained for 30 minutes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DumpUrl: str\n        :param HitFlag: Whether non-compliant information is detected\n        :type HitFlag: bool\n        :param MainType: Main non-compliant content type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MainType: str\n        :param ScanDetail: Speech detection details\n        :type ScanDetail: list of ScanDetail\n        :param RoomId: GME voice chat room ID, which is the `RoomId` passed through when the task was submitted
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RoomId: str\n        :param OpenId: GME voice chat user ID, which is the `OpenId` passed through when the task was submitted
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OpenId: str\n        :param Info: Remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Info: str\n        :param Offset: Offset time in milliseconds of segment in stream during stream detection
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Offset: int\n        :param Duration: Segment duration during stream detection
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Duration: int\n        :param PieceStartTime: Segment detection start time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PieceStartTime: int\n        """
        self.DumpUrl = None
        self.HitFlag = None
        self.MainType = None
        self.ScanDetail = None
        self.RoomId = None
        self.OpenId = None
        self.Info = None
        self.Offset = None
        self.Duration = None
        self.PieceStartTime = None


    def _deserialize(self, params):
        self.DumpUrl = params.get("DumpUrl")
        self.HitFlag = params.get("HitFlag")
        self.MainType = params.get("MainType")
        if params.get("ScanDetail") is not None:
            self.ScanDetail = []
            for item in params.get("ScanDetail"):
                obj = ScanDetail()
                obj._deserialize(item)
                self.ScanDetail.append(obj)
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")
        self.Info = params.get("Info")
        self.Offset = params.get("Offset")
        self.Duration = params.get("Duration")
        self.PieceStartTime = params.get("PieceStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceRequest(AbstractModel):
    """ScanVoice request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is the `AppID` obtained when you create an application in [Console > Service Management](https://console.cloud.tencent.com/gamegme)\n        :type BizId: int\n        :param Scenes: Speech detection scenario. The value of this parameter is currently required to be `default`. Preset scenarios: abusive, pornographic, politically sensitive, advertising, terrorism, and prohibited scenarios. For specific values, please see the <a href="#Label_Value">Label description</a> above.\n        :type Scenes: list of str\n        :param Live: Whether it is a live stream. false: audio file detection, true: audio stream detection.\n        :type Live: bool\n        :param Tasks: Speech detection task list. Up to 100 tasks can be added in the list. The structure contains:
<li>DataId: unique data ID</li>
<li>Url: URL-encoded data file URL, which is a pull address if the detected speech is a stream</li>\n        :type Tasks: list of Task\n        :param Callback: Async callback address for detection result. For more information, please see the <a href="#Callback_Declare">callback description</a> above. (Note: if this field is empty, the detection result can only be obtained by calling the `DescribeScanResultList` API.)\n        :type Callback: str\n        """
        self.BizId = None
        self.Scenes = None
        self.Live = None
        self.Tasks = None
        self.Callback = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Scenes = params.get("Scenes")
        self.Live = params.get("Live")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceResponse(AbstractModel):
    """ScanVoice response structure.

    """

    def __init__(self):
        """
        :param Data: Speech detection return. The `Data` field is a JSON array where each element contains: <li>DataId: corresponding `DataId` in request.</li>
<li>TaskID: detection task ID, which is used to poll the speech detection result.</li>\n        :type Data: list of ScanVoiceResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ScanVoiceResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ScanVoiceResult(AbstractModel):
    """Returned result of speech detection

    """

    def __init__(self):
        """
        :param DataId: Data ID\n        :type DataId: str\n        :param TaskId: Task ID\n        :type TaskId: str\n        """
        self.DataId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticsItem(AbstractModel):
    """Usage data

    """

    def __init__(self):
        """
        :param StatDate: Date in the format of yyyy-mm-dd, such as 2018-07-13\n        :type StatDate: str\n        :param Data: Statistics\n        :type Data: int\n        """
        self.StatDate = None
        self.Data = None


    def _deserialize(self, params):
        self.StatDate = params.get("StatDate")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag list

    """

    def __init__(self):
        """
        :param TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TagKey: str\n        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Speech detection task list

    """

    def __init__(self):
        """
        :param DataId: Unique data ID\n        :type DataId: str\n        :param Url: URL-encoded data file URL, which is a pull address if the detected speech is a stream\n        :type Url: str\n        :param RoomId: GME voice chat room ID, which is entered during speech detection by GME voice chat\n        :type RoomId: str\n        :param OpenId: GME voice chat user ID, which is entered during speech detection by GME voice chat\n        :type OpenId: str\n        """
        self.DataId = None
        self.Url = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterConf(AbstractModel):
    """Configuration information of phrase filtering

    """

    def __init__(self):
        """
        :param Status: Phrase filtering status. Valid values: open, close\n        :type Status: str\n        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterStatisticsItem(AbstractModel):
    """Phrase filtering usage statistics

    """

    def __init__(self):
        """
        :param Duration: Total duration of phrase filtering\n        :type Duration: int\n        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageConf(AbstractModel):
    """Configuration information of voice messaging and speech-to-text

    """

    def __init__(self):
        """
        :param Status: Voice messaging and speech-to-text status. Valid values: open, close\n        :type Status: str\n        :param Language: Language supported for voice messaging and speech-to-text. Valid values: all (all languages), cnen (Chinese and English). Default value: cnen\n        :type Language: str\n        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageStatisticsItem(AbstractModel):
    """Voice messaging usage statistics

    """

    def __init__(self):
        """
        :param Dau: DAU of voice messaging and speech-to-text\n        :type Dau: int\n        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        