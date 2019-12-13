# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AppStatisticsItem(AbstractModel):
    """Application usage statistics

    """

    def __init__(self):
        """
        :param RealtimeSpeechStatisticsItem: Voice chat statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param VoiceMessageStatisticsItem: Voice messaging statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param VoiceFilterStatisticsItem: Phrase filtering statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param Date: Statistical period
        :type Date: str
        """
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


class CreateAppRequest(AbstractModel):
    """CreateApp request structure.

    """

    def __init__(self):
        """
        :param AppName: Application name
        :type AppName: str
        :param ProjectId: Tencent Cloud project ID. Default value: 0, which means that the default project is used
        :type ProjectId: int
        :param EngineList: List of engines to be supported. Valid values: android, ios, unity, cocos, unreal, windows. All values are selected by default.
        :type EngineList: list of str
        :param RegionList: List of service regions. Valid values: mainland (Mainland China), sa (South America), eu (Europe), oc (Australia), me (Middle East). All values are selected by default.
        :type RegionList: list of str
        :param RealtimeSpeechConf: Configuration information of voice chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of phrase analysis
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param Tags: List of tags to be added
        :type Tags: list of Tag
        """
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


class CreateAppResponse(AbstractModel):
    """CreateApp output parameters

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is automatically generated by the backend
        :type BizId: int
        :param AppName: Application name, which is passed through from the `AppName` input parameter
        :type AppName: str
        :param ProjectId: Project ID, which is passed through from the entered `ProjectId`
        :type ProjectId: int
        :param SecretKey: Application key, which is used when the GME SDK is initialized
        :type SecretKey: str
        :param CreateTime: Service creation timestamp
        :type CreateTime: int
        :param RealtimeSpeechConf: Configuration information of voice chat
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: Configuration information of voice messaging and speech-to-text
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: Configuration information of phrase analysis
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        """
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
        :param BizId: GME application ID
        :type BizId: int
        :param StartDate: Data start date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13
        :type StartDate: str
        :param EndDate: Data end date (GMT+8) in the format of yyyy-mm-dd, such as 2018-07-13
        :type EndDate: str
        :param Services: List of services to be queried. Valid values: RealTimeSpeech, VoiceMessage, VoiceFilter
        :type Services: list of str
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Services = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Services = params.get("Services")


class DescribeAppStatisticsResponse(AbstractModel):
    """Gets application usage statistics output parameters

    """

    def __init__(self):
        """
        :param AppStatistics: Application usage statistics
        :type AppStatistics: list of AppStatisticsItem
        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus request structure.

    """

    def __init__(self):
        """
        :param BizId: Application ID, which is generated and returned by the backend after application creation
        :type BizId: int
        :param Status: Application status. Valid values: open, close
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus API output parameters

    """

    def __init__(self):
        """
        :param BizId: GME application ID
        :type BizId: int
        :param Status: Application status. Valid values: open, close
        :type Status: str
        """
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
        :param MainLandDau: DAU in Mainland China
        :type MainLandDau: int
        :param MainLandPcu: PCU in Mainland China
        :type MainLandPcu: int
        :param MainLandDuration: Total duration of use in Mainland China in minutes
        :type MainLandDuration: int
        :param OverseaDau: DAU outside Mainland China
        :type OverseaDau: int
        :param OverseaPcu: PCU outside Mainland China
        :type OverseaPcu: int
        :param OverseaDuration: Total duration of use outside Mainland China in minutes
        :type OverseaDuration: int
        """
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


class RealtimeSpeechConf(AbstractModel):
    """Configuration information of voice chat

    """

    def __init__(self):
        """
        :param Status: Voice chat status. Valid values: open, close
        :type Status: str
        :param Quality: Voice Chat sound quality type. Valid values: high (HD), ordinary (SD). Default value: ordinary
        :type Quality: str
        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")


class Tag(AbstractModel):
    """Tag list

    """

    def __init__(self):
        """
        :param TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class VoiceFilterConf(AbstractModel):
    """Configuration information of phrase filtering

    """

    def __init__(self):
        """
        :param Status: Phrase filtering status. Valid values: open, close
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class VoiceFilterStatisticsItem(AbstractModel):
    """Phrase filtering usage statistics

    """

    def __init__(self):
        """
        :param Duration: Total duration of phrase filtering
        :type Duration: int
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")


class VoiceMessageConf(AbstractModel):
    """Configuration information of voice messaging and speech-to-text

    """

    def __init__(self):
        """
        :param Status: Voice messaging and speech-to-text status. Valid values: open, close
        :type Status: str
        :param Language: Language supported for voice messaging and speech-to-text. Valid values: all (all languages), cnen (Chinese and English). Default value: cnen
        :type Language: str
        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")


class VoiceMessageStatisticsItem(AbstractModel):
    """Voice messaging usage statistics

    """

    def __init__(self):
        """
        :param Dau: DAU of voice messaging and speech-to-text
        :type Dau: int
        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")