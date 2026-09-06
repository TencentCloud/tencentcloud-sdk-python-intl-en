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


class AgentInfo(AbstractModel):
    r"""Agent information.

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Name: <p>Agent name</p>
        :type Name: str
        :param _Description: <p>Agent description</p>
        :type Description: str
        :param _Category: <p>Agent Category.</p>
        :type Category: str
        :param _Status: <p>Status: draft/configured/running/standby/disabled</p>
        :type Status: str
        :param _SkillIds: <p>List of associated skill IDs.</p>
        :type SkillIds: list of str
        :param _ResourceMapId: <p>Associated resource map ID.</p>
        :type ResourceMapId: str
        :param _MCPIds: <p>Associated mcp id.</p>
        :type MCPIds: list of str
        :param _CamTags: <p>Resource Tag.</p>
        :type CamTags: list of Tag
        :param _EnvVars: <p>Environment variables required by the agent at runtime</p>
        :type EnvVars: list of EnvVar
        """
        self._AgentId = None
        self._Name = None
        self._Description = None
        self._Category = None
        self._Status = None
        self._SkillIds = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._CamTags = None
        self._EnvVars = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        r"""<p>Agent name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Agent description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Category(self):
        r"""<p>Agent Category.</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Status(self):
        r"""<p>Status: draft/configured/running/standby/disabled</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SkillIds(self):
        r"""<p>List of associated skill IDs.</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def ResourceMapId(self):
        r"""<p>Associated resource map ID.</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>Associated mcp id.</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def CamTags(self):
        r"""<p>Resource Tag.</p>
        :rtype: list of Tag
        """
        return self._CamTags

    @CamTags.setter
    def CamTags(self, CamTags):
        self._CamTags = CamTags

    @property
    def EnvVars(self):
        r"""<p>Environment variables required by the agent at runtime</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Status = params.get("Status")
        self._SkillIds = params.get("SkillIds")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("CamTags") is not None:
            self._CamTags = []
            for item in params.get("CamTags"):
                obj = Tag()
                obj._deserialize(item)
                self._CamTags.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmLable(AbstractModel):
    r"""Alarming Label

    """

    def __init__(self):
        r"""
        :param _Name: label name
        :type Name: str
        :param _Value: label value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""label name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""label value
        :rtype: str
        """
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
        


class AlarmNotifyHistory(AbstractModel):
    r"""Notification history for each alert

    """

    def __init__(self):
        r"""
        :param _NotifyId: Unique notification ID.
        :type NotifyId: str
        :param _PolicyId: Alert policy ID
        :type PolicyId: str
        :param _SessionId: Alarm cycle iD
        :type SessionId: str
        :param _NotifyTime: Notification time in Unix timestamp (in seconds).
        :type NotifyTime: int
        :param _TriggerTime: Trigger time in Unix timestamp (in seconds).
        :type TriggerTime: int
        :param _TriggerLevel: Alarm severity level. Valid values: None, Note, Warn, and Serious.
        :type TriggerLevel: str
        :param _AlarmContent: alert content
        :type AlarmContent: str
        :param _AlarmObject: Alarm object
        :type AlarmObject: str
        :param _ChannelSet: Alarm notification channel collection involved this time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelSet: list of str
        :param _ChannelsReceivers: Recipient information of the channel
        :type ChannelsReceivers: list of ChannelsReceivers
        :param _PolicyName: Alarm policy name
        :type PolicyName: str
        :param _PromeInstanceID: Prometheus Instance ID, valid only when MT_PROME
        :type PromeInstanceID: str
        :param _PromeInstanceRegion: Region of the Prometheus Instance. Valid at that time only for MT_PROME.
        :type PromeInstanceRegion: str
        :param _Notices: Notification template related configuration information
        :type Notices: list of NotifyRelatedNotice
        :param _TriggerStatus: Alarm trigger status. Valid values: Trigger and Recovery.
        :type TriggerStatus: str
        :param _PromeConsoleURL: Console page address related to the present Prometheus notification history, valid only when MR_PROME
        :type PromeConsoleURL: str
        :param _Labels: Alarm label
        :type Labels: list of AlarmLable
        """
        self._NotifyId = None
        self._PolicyId = None
        self._SessionId = None
        self._NotifyTime = None
        self._TriggerTime = None
        self._TriggerLevel = None
        self._AlarmContent = None
        self._AlarmObject = None
        self._ChannelSet = None
        self._ChannelsReceivers = None
        self._PolicyName = None
        self._PromeInstanceID = None
        self._PromeInstanceRegion = None
        self._Notices = None
        self._TriggerStatus = None
        self._PromeConsoleURL = None
        self._Labels = None

    @property
    def NotifyId(self):
        r"""Unique notification ID.
        :rtype: str
        """
        return self._NotifyId

    @NotifyId.setter
    def NotifyId(self, NotifyId):
        self._NotifyId = NotifyId

    @property
    def PolicyId(self):
        r"""Alert policy ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def SessionId(self):
        r"""Alarm cycle iD
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def NotifyTime(self):
        r"""Notification time in Unix timestamp (in seconds).
        :rtype: int
        """
        return self._NotifyTime

    @NotifyTime.setter
    def NotifyTime(self, NotifyTime):
        self._NotifyTime = NotifyTime

    @property
    def TriggerTime(self):
        r"""Trigger time in Unix timestamp (in seconds).
        :rtype: int
        """
        return self._TriggerTime

    @TriggerTime.setter
    def TriggerTime(self, TriggerTime):
        self._TriggerTime = TriggerTime

    @property
    def TriggerLevel(self):
        r"""Alarm severity level. Valid values: None, Note, Warn, and Serious.
        :rtype: str
        """
        return self._TriggerLevel

    @TriggerLevel.setter
    def TriggerLevel(self, TriggerLevel):
        self._TriggerLevel = TriggerLevel

    @property
    def AlarmContent(self):
        r"""alert content
        :rtype: str
        """
        return self._AlarmContent

    @AlarmContent.setter
    def AlarmContent(self, AlarmContent):
        self._AlarmContent = AlarmContent

    @property
    def AlarmObject(self):
        r"""Alarm object
        :rtype: str
        """
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def ChannelSet(self):
        r"""Alarm notification channel collection involved this time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ChannelSet

    @ChannelSet.setter
    def ChannelSet(self, ChannelSet):
        self._ChannelSet = ChannelSet

    @property
    def ChannelsReceivers(self):
        r"""Recipient information of the channel
        :rtype: list of ChannelsReceivers
        """
        return self._ChannelsReceivers

    @ChannelsReceivers.setter
    def ChannelsReceivers(self, ChannelsReceivers):
        self._ChannelsReceivers = ChannelsReceivers

    @property
    def PolicyName(self):
        r"""Alarm policy name
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PromeInstanceID(self):
        r"""Prometheus Instance ID, valid only when MT_PROME
        :rtype: str
        """
        return self._PromeInstanceID

    @PromeInstanceID.setter
    def PromeInstanceID(self, PromeInstanceID):
        self._PromeInstanceID = PromeInstanceID

    @property
    def PromeInstanceRegion(self):
        r"""Region of the Prometheus Instance. Valid at that time only for MT_PROME.
        :rtype: str
        """
        return self._PromeInstanceRegion

    @PromeInstanceRegion.setter
    def PromeInstanceRegion(self, PromeInstanceRegion):
        self._PromeInstanceRegion = PromeInstanceRegion

    @property
    def Notices(self):
        r"""Notification template related configuration information
        :rtype: list of NotifyRelatedNotice
        """
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def TriggerStatus(self):
        r"""Alarm trigger status. Valid values: Trigger and Recovery.
        :rtype: str
        """
        return self._TriggerStatus

    @TriggerStatus.setter
    def TriggerStatus(self, TriggerStatus):
        self._TriggerStatus = TriggerStatus

    @property
    def PromeConsoleURL(self):
        r"""Console page address related to the present Prometheus notification history, valid only when MR_PROME
        :rtype: str
        """
        return self._PromeConsoleURL

    @PromeConsoleURL.setter
    def PromeConsoleURL(self, PromeConsoleURL):
        self._PromeConsoleURL = PromeConsoleURL

    @property
    def Labels(self):
        r"""Alarm label
        :rtype: list of AlarmLable
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._NotifyId = params.get("NotifyId")
        self._PolicyId = params.get("PolicyId")
        self._SessionId = params.get("SessionId")
        self._NotifyTime = params.get("NotifyTime")
        self._TriggerTime = params.get("TriggerTime")
        self._TriggerLevel = params.get("TriggerLevel")
        self._AlarmContent = params.get("AlarmContent")
        self._AlarmObject = params.get("AlarmObject")
        self._ChannelSet = params.get("ChannelSet")
        if params.get("ChannelsReceivers") is not None:
            self._ChannelsReceivers = []
            for item in params.get("ChannelsReceivers"):
                obj = ChannelsReceivers()
                obj._deserialize(item)
                self._ChannelsReceivers.append(obj)
        self._PolicyName = params.get("PolicyName")
        self._PromeInstanceID = params.get("PromeInstanceID")
        self._PromeInstanceRegion = params.get("PromeInstanceRegion")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = NotifyRelatedNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._TriggerStatus = params.get("TriggerStatus")
        self._PromeConsoleURL = params.get("PromeConsoleURL")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AlarmLable()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArtifactInfo(AbstractModel):
    r"""Product entity

    """

    def __init__(self):
        r"""
        :param _ArtifactId: <p>Product ID</p>
        :type ArtifactId: str
        :param _Name: <p>Product name</p>
        :type Name: str
        :param _MimeType: <p>Physical type</p>
        :type MimeType: str
        :param _SizeBytes: <p>File size (byte)</p>
        :type SizeBytes: int
        :param _IsGlobal: <p>Whether it is public</p>
        :type IsGlobal: bool
        :param _CreatedAt: <p>Creation time (Unix timestamp in seconds).</p>
        :type CreatedAt: int
        :param _UpdatedAt: <p>Modification time.</p>
        :type UpdatedAt: int
        :param _AgentId: <p>Agent ID that generated the artifact</p>
        :type AgentId: str
        :param _SkillId: <p>Skill ID that generates the artifact</p>
        :type SkillId: str
        :param _StoragePath: <p>For parsing calls to the download API</p>
        :type StoragePath: str
        """
        self._ArtifactId = None
        self._Name = None
        self._MimeType = None
        self._SizeBytes = None
        self._IsGlobal = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._AgentId = None
        self._SkillId = None
        self._StoragePath = None

    @property
    def ArtifactId(self):
        r"""<p>Product ID</p>
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId

    @property
    def Name(self):
        r"""<p>Product name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MimeType(self):
        r"""<p>Physical type</p>
        :rtype: str
        """
        return self._MimeType

    @MimeType.setter
    def MimeType(self, MimeType):
        self._MimeType = MimeType

    @property
    def SizeBytes(self):
        r"""<p>File size (byte)</p>
        :rtype: int
        """
        return self._SizeBytes

    @SizeBytes.setter
    def SizeBytes(self, SizeBytes):
        self._SizeBytes = SizeBytes

    @property
    def IsGlobal(self):
        r"""<p>Whether it is public</p>
        :rtype: bool
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def CreatedAt(self):
        r"""<p>Creation time (Unix timestamp in seconds).</p>
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>Modification time.</p>
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def AgentId(self):
        r"""<p>Agent ID that generated the artifact</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def SkillId(self):
        r"""<p>Skill ID that generates the artifact</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def StoragePath(self):
        r"""<p>For parsing calls to the download API</p>
        :rtype: str
        """
        return self._StoragePath

    @StoragePath.setter
    def StoragePath(self, StoragePath):
        self._StoragePath = StoragePath


    def _deserialize(self, params):
        self._ArtifactId = params.get("ArtifactId")
        self._Name = params.get("Name")
        self._MimeType = params.get("MimeType")
        self._SizeBytes = params.get("SizeBytes")
        self._IsGlobal = params.get("IsGlobal")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._AgentId = params.get("AgentId")
        self._SkillId = params.get("SkillId")
        self._StoragePath = params.get("StoragePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIWorkbenchChatRequest(AbstractModel):
    r"""CancelAIWorkbenchChat request structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Session id.</p>
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""<p>Session id.</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIWorkbenchChatResponse(AbstractModel):
    r"""CancelAIWorkbenchChat response structure.

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


class ChannelsReceivers(AbstractModel):
    r"""Receiver details

    """

    def __init__(self):
        r"""
        :param _ChannelName: Notification channel name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelName: str
        :param _Receivers: Recipient.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Receivers: list of str
        :param _SendStatus: Sending result. Valid values: 0, (invalid), 1 (successful), 2 (failed), and 3 (no sending required).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SendStatus: str
        """
        self._ChannelName = None
        self._Receivers = None
        self._SendStatus = None

    @property
    def ChannelName(self):
        r"""Notification channel name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        r"""Recipient.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def SendStatus(self):
        r"""Sending result. Valid values: 0, (invalid), 1 (successful), 2 (failed), and 3 (no sending required).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._SendStatus = params.get("SendStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentBlockInfo(AbstractModel):
    r"""Each ContentBlockInfo corresponds to an AGUI event converted from a downstream ContentBlock.

    """

    def __init__(self):
        r"""
        :param _Type: <p>Type.</p>
        :type Type: str
        :param _Data: <p>Data content.</p>
        :type Data: str
        """
        self._Type = None
        self._Data = None

    @property
    def Type(self):
        r"""<p>Type.</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        r"""<p>Data content.</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchAgentRequest(AbstractModel):
    r"""CreateAIWorkbenchAgent request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Agent Name</p>
        :type Name: str
        :param _Description: <p>Agent description</p>
        :type Description: str
        :param _Category: <p>Agent Category</p>
        :type Category: str
        :param _Tags: <p>Agent tag</p>
        :type Tags: list of str
        :param _Instruction: <p>Agent prompt content</p>
        :type Instruction: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        :param _SkillIds: <p>List of associated skill IDs.</p>
        :type SkillIds: list of str
        :param _Source: <p>Source: builtin / custom</p>
        :type Source: str
        :param _ResourceMapId: <p>Map ID of the associated resource</p>
        :type ResourceMapId: str
        :param _MCPIds: <p>Associated mcp tool</p>
        :type MCPIds: list of str
        :param _CamTags: <p>Resource tag</p>
        :type CamTags: list of Tag
        :param _EnvVars: <p>agent runtime environment variable</p>
        :type EnvVars: list of EnvVar
        """
        self._Name = None
        self._Description = None
        self._Category = None
        self._Tags = None
        self._Instruction = None
        self._SkillIds = None
        self._Source = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._CamTags = None
        self._EnvVars = None

    @property
    def Name(self):
        r"""<p>Agent Name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Agent description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Category(self):
        r"""<p>Agent Category</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Tags(self):
        r"""<p>Agent tag</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Instruction(self):
        r"""<p>Agent prompt content</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        """
        return self._Instruction

    @Instruction.setter
    def Instruction(self, Instruction):
        self._Instruction = Instruction

    @property
    def SkillIds(self):
        r"""<p>List of associated skill IDs.</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def Source(self):
        r"""<p>Source: builtin / custom</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def ResourceMapId(self):
        r"""<p>Map ID of the associated resource</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>Associated mcp tool</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def CamTags(self):
        r"""<p>Resource tag</p>
        :rtype: list of Tag
        """
        return self._CamTags

    @CamTags.setter
    def CamTags(self, CamTags):
        self._CamTags = CamTags

    @property
    def EnvVars(self):
        r"""<p>agent runtime environment variable</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Tags = params.get("Tags")
        if params.get("Instruction") is not None:
            self._Instruction = InstructionConfig()
            self._Instruction._deserialize(params.get("Instruction"))
        self._SkillIds = params.get("SkillIds")
        self._Source = params.get("Source")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("CamTags") is not None:
            self._CamTags = []
            for item in params.get("CamTags"):
                obj = Tag()
                obj._deserialize(item)
                self._CamTags.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchAgentResponse(AbstractModel):
    r"""CreateAIWorkbenchAgent response structure.

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

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
        self._AgentId = params.get("AgentId")
        self._RequestId = params.get("RequestId")


class CreateAIWorkbenchTaskRequest(AbstractModel):
    r"""CreateAIWorkbenchTask request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Task Name</p>
        :type Name: str
        :param _Description: <p>Task description</p>
        :type Description: str
        :param _AgentId: <p>Associated Agent ID</p>
        :type AgentId: str
        :param _PromptTemplate: <p>Prompt Template</p>
        :type PromptTemplate: str
        :param _OutputFormat: <p>Output format: markdown / json</p>
        :type OutputFormat: str
        :param _TriggerType: <p>Trigger type: manual / cron / webhook</p>
        :type TriggerType: str
        :param _CronExpr: <p>Cron expression</p>
        :type CronExpr: str
        :param _CronTimezone: <p>Cron time zone</p>
        :type CronTimezone: str
        :param _ResourceMapId: <p>Associated resource map ID</p>
        :type ResourceMapId: str
        :param _SkillIds: <p>Skill ID list</p>
        :type SkillIds: list of str
        :param _McpEndpointIds: <p>MCP endpoint ID list</p>
        :type McpEndpointIds: list of str
        :param _TimeoutSec: <p>Timeout (seconds)</p>
        :type TimeoutSec: int
        :param _RetryCount: <p>Retry count</p>
        :type RetryCount: int
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._Name = None
        self._Description = None
        self._AgentId = None
        self._PromptTemplate = None
        self._OutputFormat = None
        self._TriggerType = None
        self._CronExpr = None
        self._CronTimezone = None
        self._ResourceMapId = None
        self._SkillIds = None
        self._McpEndpointIds = None
        self._TimeoutSec = None
        self._RetryCount = None
        self._Enabled = None

    @property
    def Name(self):
        r"""<p>Task Name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Task description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AgentId(self):
        r"""<p>Associated Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def PromptTemplate(self):
        r"""<p>Prompt Template</p>
        :rtype: str
        """
        return self._PromptTemplate

    @PromptTemplate.setter
    def PromptTemplate(self, PromptTemplate):
        self._PromptTemplate = PromptTemplate

    @property
    def OutputFormat(self):
        r"""<p>Output format: markdown / json</p>
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def TriggerType(self):
        r"""<p>Trigger type: manual / cron / webhook</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def CronExpr(self):
        r"""<p>Cron expression</p>
        :rtype: str
        """
        return self._CronExpr

    @CronExpr.setter
    def CronExpr(self, CronExpr):
        self._CronExpr = CronExpr

    @property
    def CronTimezone(self):
        r"""<p>Cron time zone</p>
        :rtype: str
        """
        return self._CronTimezone

    @CronTimezone.setter
    def CronTimezone(self, CronTimezone):
        self._CronTimezone = CronTimezone

    @property
    def ResourceMapId(self):
        r"""<p>Associated resource map ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def SkillIds(self):
        r"""<p>Skill ID list</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def McpEndpointIds(self):
        r"""<p>MCP endpoint ID list</p>
        :rtype: list of str
        """
        return self._McpEndpointIds

    @McpEndpointIds.setter
    def McpEndpointIds(self, McpEndpointIds):
        self._McpEndpointIds = McpEndpointIds

    @property
    def TimeoutSec(self):
        r"""<p>Timeout (seconds)</p>
        :rtype: int
        """
        return self._TimeoutSec

    @TimeoutSec.setter
    def TimeoutSec(self, TimeoutSec):
        self._TimeoutSec = TimeoutSec

    @property
    def RetryCount(self):
        r"""<p>Retry count</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AgentId = params.get("AgentId")
        self._PromptTemplate = params.get("PromptTemplate")
        self._OutputFormat = params.get("OutputFormat")
        self._TriggerType = params.get("TriggerType")
        self._CronExpr = params.get("CronExpr")
        self._CronTimezone = params.get("CronTimezone")
        self._ResourceMapId = params.get("ResourceMapId")
        self._SkillIds = params.get("SkillIds")
        self._McpEndpointIds = params.get("McpEndpointIds")
        self._TimeoutSec = params.get("TimeoutSec")
        self._RetryCount = params.get("RetryCount")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIWorkbenchTaskResponse(AbstractModel):
    r"""CreateAIWorkbenchTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
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


class DeleteAIWorkbenchAgentRequest(AbstractModel):
    r"""DeleteAIWorkbenchAgent request structure.

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIWorkbenchAgentResponse(AbstractModel):
    r"""DeleteAIWorkbenchAgent response structure.

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


class DeleteAIWorkbenchTaskRequest(AbstractModel):
    r"""DeleteAIWorkbenchTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
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
        


class DeleteAIWorkbenchTaskResponse(AbstractModel):
    r"""DeleteAIWorkbenchTask response structure.

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


class DescribeAIWorkbenchAgentRequest(AbstractModel):
    r"""DescribeAIWorkbenchAgent request structure.

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchAgentResponse(AbstractModel):
    r"""DescribeAIWorkbenchAgent response structure.

    """

    def __init__(self):
        r"""
        :param _Agent: <p>Agent Information</p>
        :type Agent: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Agent = None
        self._RequestId = None

    @property
    def Agent(self):
        r"""<p>Agent Information</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = AgentInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchArtifactRequest(AbstractModel):
    r"""DescribeAIWorkbenchArtifact request structure.

    """

    def __init__(self):
        r"""
        :param _ArtifactId: <p>Product ID</p>
        :type ArtifactId: str
        :param _NeedDownloadURL: <p>Whether to download the URL</p><p><code>1</code> = required, <code>0</code> or not passed = not required</p>
        :type NeedDownloadURL: int
        """
        self._ArtifactId = None
        self._NeedDownloadURL = None

    @property
    def ArtifactId(self):
        r"""<p>Product ID</p>
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId

    @property
    def NeedDownloadURL(self):
        r"""<p>Whether to download the URL</p><p><code>1</code> = required, <code>0</code> or not passed = not required</p>
        :rtype: int
        """
        return self._NeedDownloadURL

    @NeedDownloadURL.setter
    def NeedDownloadURL(self, NeedDownloadURL):
        self._NeedDownloadURL = NeedDownloadURL


    def _deserialize(self, params):
        self._ArtifactId = params.get("ArtifactId")
        self._NeedDownloadURL = params.get("NeedDownloadURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchArtifactResponse(AbstractModel):
    r"""DescribeAIWorkbenchArtifact response structure.

    """

    def __init__(self):
        r"""
        :param _Artifact: <p>Product information</p>
        :type Artifact: :class:`tencentcloud.monitor.v20230616.models.ArtifactInfo`
        :param _DownloadURL: <p>COS pre-signed download URL</p>
        :type DownloadURL: str
        :param _DownloadURLExpiredAt: <p>Download URL expiration time (in RFC3339 format)</p>
        :type DownloadURLExpiredAt: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Artifact = None
        self._DownloadURL = None
        self._DownloadURLExpiredAt = None
        self._RequestId = None

    @property
    def Artifact(self):
        r"""<p>Product information</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ArtifactInfo`
        """
        return self._Artifact

    @Artifact.setter
    def Artifact(self, Artifact):
        self._Artifact = Artifact

    @property
    def DownloadURL(self):
        r"""<p>COS pre-signed download URL</p>
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def DownloadURLExpiredAt(self):
        r"""<p>Download URL expiration time (in RFC3339 format)</p>
        :rtype: str
        """
        return self._DownloadURLExpiredAt

    @DownloadURLExpiredAt.setter
    def DownloadURLExpiredAt(self, DownloadURLExpiredAt):
        self._DownloadURLExpiredAt = DownloadURLExpiredAt

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
        if params.get("Artifact") is not None:
            self._Artifact = ArtifactInfo()
            self._Artifact._deserialize(params.get("Artifact"))
        self._DownloadURL = params.get("DownloadURL")
        self._DownloadURLExpiredAt = params.get("DownloadURLExpiredAt")
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchExecutionRequest(AbstractModel):
    r"""DescribeAIWorkbenchExecution request structure.

    """

    def __init__(self):
        r"""
        :param _ExecutionId: <p>Execution ID</p>
        :type ExecutionId: str
        """
        self._ExecutionId = None

    @property
    def ExecutionId(self):
        r"""<p>Execution ID</p>
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId


    def _deserialize(self, params):
        self._ExecutionId = params.get("ExecutionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchExecutionResponse(AbstractModel):
    r"""DescribeAIWorkbenchExecution response structure.

    """

    def __init__(self):
        r"""
        :param _Execution: <p>Execution Record</p>
        :type Execution: :class:`tencentcloud.monitor.v20230616.models.ExecutionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        r"""<p>Execution Record</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ExecutionInfo`
        """
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

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
        if params.get("Execution") is not None:
            self._Execution = ExecutionInfo()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSessionRequest(AbstractModel):
    r"""DescribeAIWorkbenchSession request structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Session ID</p>
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""<p>Session ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSessionResponse(AbstractModel):
    r"""DescribeAIWorkbenchSession response structure.

    """

    def __init__(self):
        r"""
        :param _Session: <p>Session information</p>
        :type Session: :class:`tencentcloud.monitor.v20230616.models.SessionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        r"""<p>Session information</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.SessionInfo`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

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
        if params.get("Session") is not None:
            self._Session = SessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DescribeAIWorkbenchSkillRequest(AbstractModel):
    r"""DescribeAIWorkbenchSkill request structure.

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>Skill ID</p>
        :type SkillId: str
        """
        self._SkillId = None

    @property
    def SkillId(self):
        r"""<p>Skill ID</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIWorkbenchSkillResponse(AbstractModel):
    r"""DescribeAIWorkbenchSkill response structure.

    """

    def __init__(self):
        r"""
        :param _Skill: <p>Skill information.</p>
        :type Skill: :class:`tencentcloud.monitor.v20230616.models.SkillInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Skill = None
        self._RequestId = None

    @property
    def Skill(self):
        r"""<p>Skill information.</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.SkillInfo`
        """
        return self._Skill

    @Skill.setter
    def Skill(self, Skill):
        self._Skill = Skill

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
        if params.get("Skill") is not None:
            self._Skill = SkillInfo()
            self._Skill._deserialize(params.get("Skill"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmNotifyHistoriesRequest(AbstractModel):
    r"""DescribeAlarmNotifyHistories request structure.

    """

    def __init__(self):
        r"""
        :param _MonitorType: Monitoring type
        :type MonitorType: str
        :param _QueryBaseTime: Start time, used as a Unix timestamp in seconds.
        :type QueryBaseTime: int
        :param _QueryBeforeSeconds: Period to query before QueryBaseTime, in seconds.
        :type QueryBeforeSeconds: int
        :param _PageParams: Pagination parameter.
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        :param _Namespace: Fill in when the monitoring type is MT_QCE. Namespace of the affiliation.
        :type Namespace: str
        :param _ModelName: Fill in when the monitoring type is MT_QCE. Alarm policy type
        :type ModelName: str
        :param _PolicyId: Query the notification history of a policy
        :type PolicyId: str
        """
        self._MonitorType = None
        self._QueryBaseTime = None
        self._QueryBeforeSeconds = None
        self._PageParams = None
        self._Namespace = None
        self._ModelName = None
        self._PolicyId = None

    @property
    def MonitorType(self):
        r"""Monitoring type
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def QueryBaseTime(self):
        r"""Start time, used as a Unix timestamp in seconds.
        :rtype: int
        """
        return self._QueryBaseTime

    @QueryBaseTime.setter
    def QueryBaseTime(self, QueryBaseTime):
        self._QueryBaseTime = QueryBaseTime

    @property
    def QueryBeforeSeconds(self):
        r"""Period to query before QueryBaseTime, in seconds.
        :rtype: int
        """
        return self._QueryBeforeSeconds

    @QueryBeforeSeconds.setter
    def QueryBeforeSeconds(self, QueryBeforeSeconds):
        self._QueryBeforeSeconds = QueryBeforeSeconds

    @property
    def PageParams(self):
        r"""Pagination parameter.
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams

    @property
    def Namespace(self):
        r"""Fill in when the monitoring type is MT_QCE. Namespace of the affiliation.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ModelName(self):
        r"""Fill in when the monitoring type is MT_QCE. Alarm policy type
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PolicyId(self):
        r"""Query the notification history of a policy
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._QueryBaseTime = params.get("QueryBaseTime")
        self._QueryBeforeSeconds = params.get("QueryBeforeSeconds")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNoParams()
            self._PageParams._deserialize(params.get("PageParams"))
        self._Namespace = params.get("Namespace")
        self._ModelName = params.get("ModelName")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNotifyHistoriesResponse(AbstractModel):
    r"""DescribeAlarmNotifyHistories response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyHistoryList: Alarm history
        :type AlarmNotifyHistoryList: list of AlarmNotifyHistory
        :param _PageResult: Pagination condition
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmNotifyHistoryList = None
        self._PageResult = None
        self._RequestId = None

    @property
    def AlarmNotifyHistoryList(self):
        r"""Alarm history
        :rtype: list of AlarmNotifyHistory
        """
        return self._AlarmNotifyHistoryList

    @AlarmNotifyHistoryList.setter
    def AlarmNotifyHistoryList(self, AlarmNotifyHistoryList):
        self._AlarmNotifyHistoryList = AlarmNotifyHistoryList

    @property
    def PageResult(self):
        r"""Pagination condition
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("AlarmNotifyHistoryList") is not None:
            self._AlarmNotifyHistoryList = []
            for item in params.get("AlarmNotifyHistoryList"):
                obj = AlarmNotifyHistory()
                obj._deserialize(item)
                self._AlarmNotifyHistoryList.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNoResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class EnvEntry(AbstractModel):
    r"""Environment variable entry

    """

    def __init__(self):
        r"""
        :param _Value: <p>Environment variable value</p>
        :type Value: str
        :param _Sensitive: <p>Whether to mask</p>
        :type Sensitive: bool
        """
        self._Value = None
        self._Sensitive = None

    @property
    def Value(self):
        r"""<p>Environment variable value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Sensitive(self):
        r"""<p>Whether to mask</p>
        :rtype: bool
        """
        return self._Sensitive

    @Sensitive.setter
    def Sensitive(self, Sensitive):
        self._Sensitive = Sensitive


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Sensitive = params.get("Sensitive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    r"""Environment variables required by the agent at runtime

    """

    def __init__(self):
        r"""
        :param _Key: <p>Environment variable key</p>
        :type Key: str
        :param _Value: <p>Environment variable value</p>
        :type Value: :class:`tencentcloud.monitor.v20230616.models.EnvEntry`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>Environment variable key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Environment variable value</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.EnvEntry`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = EnvEntry()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionInfo(AbstractModel):
    r"""Execution record entity

    """

    def __init__(self):
        r"""
        :param _Name: <p>Task name</p>
        :type Name: str
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _ExecutionId: <p>Execution ID</p>
        :type ExecutionId: str
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _SessionId: <p>Session ID</p>
        :type SessionId: str
        :param _TriggerType: <p>Trigger type: manual / cron / webhook</p>
        :type TriggerType: str
        :param _Status: <p>Status: pending/running/completed/failed/timeout/cancelled</p>
        :type Status: str
        :param _Summary: <p>Execution Abstract</p>
        :type Summary: str
        :param _DurationMs: <p>Execution time (ms)</p>
        :type DurationMs: int
        """
        self._Name = None
        self._TaskId = None
        self._ExecutionId = None
        self._AgentId = None
        self._SessionId = None
        self._TriggerType = None
        self._Status = None
        self._Summary = None
        self._DurationMs = None

    @property
    def Name(self):
        r"""<p>Task name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ExecutionId(self):
        r"""<p>Execution ID</p>
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def SessionId(self):
        r"""<p>Session ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def TriggerType(self):
        r"""<p>Trigger type: manual / cron / webhook</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Status(self):
        r"""<p>Status: pending/running/completed/failed/timeout/cancelled</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Summary(self):
        r"""<p>Execution Abstract</p>
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def DurationMs(self):
        r"""<p>Execution time (ms)</p>
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._ExecutionId = params.get("ExecutionId")
        self._AgentId = params.get("AgentId")
        self._SessionId = params.get("SessionId")
        self._TriggerType = params.get("TriggerType")
        self._Status = params.get("Status")
        self._Summary = params.get("Summary")
        self._DurationMs = params.get("DurationMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAIWorkbenchArtifactDownloadURLRequest(AbstractModel):
    r"""GetAIWorkbenchArtifactDownloadURL request structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Session ID.</p>
        :type SessionId: str
        :param _ArtifactId: <p>Artifact ID</p>
        :type ArtifactId: str
        """
        self._SessionId = None
        self._ArtifactId = None

    @property
    def SessionId(self):
        r"""<p>Session ID.</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ArtifactId(self):
        r"""<p>Artifact ID</p>
        :rtype: str
        """
        return self._ArtifactId

    @ArtifactId.setter
    def ArtifactId(self, ArtifactId):
        self._ArtifactId = ArtifactId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._ArtifactId = params.get("ArtifactId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAIWorkbenchArtifactDownloadURLResponse(AbstractModel):
    r"""GetAIWorkbenchArtifactDownloadURL response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadURL: <p>COS pre-signed HTTPS download URL</p>
        :type DownloadURL: str
        :param _ExpiredAt: <p>URL expiration time (RFC3339 format)</p>
        :type ExpiredAt: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadURL = None
        self._ExpiredAt = None
        self._RequestId = None

    @property
    def DownloadURL(self):
        r"""<p>COS pre-signed HTTPS download URL</p>
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def ExpiredAt(self):
        r"""<p>URL expiration time (RFC3339 format)</p>
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

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
        self._DownloadURL = params.get("DownloadURL")
        self._ExpiredAt = params.get("ExpiredAt")
        self._RequestId = params.get("RequestId")


class InstructionConfig(AbstractModel):
    r"""Clone prompt configuration

    """

    def __init__(self):
        r"""
        :param _RolePosition: <p>Role definition</p>
        :type RolePosition: str
        :param _CoreDuty: <p>Core responsibility</p>
        :type CoreDuty: str
        :param _CoreTruths: <p>Core principle</p>
        :type CoreTruths: str
        :param _Vibe: <p>Style constraints</p>
        :type Vibe: str
        :param _Boundaries: <p>Notes</p>
        :type Boundaries: str
        """
        self._RolePosition = None
        self._CoreDuty = None
        self._CoreTruths = None
        self._Vibe = None
        self._Boundaries = None

    @property
    def RolePosition(self):
        r"""<p>Role definition</p>
        :rtype: str
        """
        return self._RolePosition

    @RolePosition.setter
    def RolePosition(self, RolePosition):
        self._RolePosition = RolePosition

    @property
    def CoreDuty(self):
        r"""<p>Core responsibility</p>
        :rtype: str
        """
        return self._CoreDuty

    @CoreDuty.setter
    def CoreDuty(self, CoreDuty):
        self._CoreDuty = CoreDuty

    @property
    def CoreTruths(self):
        r"""<p>Core principle</p>
        :rtype: str
        """
        return self._CoreTruths

    @CoreTruths.setter
    def CoreTruths(self, CoreTruths):
        self._CoreTruths = CoreTruths

    @property
    def Vibe(self):
        r"""<p>Style constraints</p>
        :rtype: str
        """
        return self._Vibe

    @Vibe.setter
    def Vibe(self, Vibe):
        self._Vibe = Vibe

    @property
    def Boundaries(self):
        r"""<p>Notes</p>
        :rtype: str
        """
        return self._Boundaries

    @Boundaries.setter
    def Boundaries(self, Boundaries):
        self._Boundaries = Boundaries


    def _deserialize(self, params):
        self._RolePosition = params.get("RolePosition")
        self._CoreDuty = params.get("CoreDuty")
        self._CoreTruths = params.get("CoreTruths")
        self._Vibe = params.get("Vibe")
        self._Boundaries = params.get("Boundaries")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchAgentsRequest(AbstractModel):
    r"""ListAIWorkbenchAgents request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _Status: <p>Status filtering</p>
        :type Status: str
        :param _Category: <p>Category filtering</p>
        :type Category: str
        :param _Keyword: <p>Search keyword</p>
        :type Keyword: str
        :param _Source: <p>Filter by source</p>
        :type Source: str
        :param _AgentIds: <p>Agent ID list filtering</p>
        :type AgentIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._Status = None
        self._Category = None
        self._Keyword = None
        self._Source = None
        self._AgentIds = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Status(self):
        r"""<p>Status filtering</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Category(self):
        r"""<p>Category filtering</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Keyword(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Source(self):
        r"""<p>Filter by source</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AgentIds(self):
        r"""<p>Agent ID list filtering</p>
        :rtype: list of str
        """
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Status = params.get("Status")
        self._Category = params.get("Category")
        self._Keyword = params.get("Keyword")
        self._Source = params.get("Source")
        self._AgentIds = params.get("AgentIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchAgentsResponse(AbstractModel):
    r"""ListAIWorkbenchAgents response structure.

    """

    def __init__(self):
        r"""
        :param _Agents: <p>Agent list</p>
        :type Agents: list of AgentInfo
        :param _PageResult: <p>Pagination result</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Agents = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Agents(self):
        r"""<p>Agent list</p>
        :rtype: list of AgentInfo
        """
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def PageResult(self):
        r"""<p>Pagination result</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = AgentInfo()
                obj._deserialize(item)
                self._Agents.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchArtifactsRequest(AbstractModel):
    r"""ListAIWorkbenchArtifacts request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _SessionIds: <p>Session ID.</p>
        :type SessionIds: list of str
        :param _MimeTypes: <p>Message content type</p>
        :type MimeTypes: list of str
        :param _OrderDirection: <p>Sorting order</p><p>Enumeration values:</p><ul><li>ASC: ascending order</li><li>DESC: descending order</li></ul>
        :type OrderDirection: str
        """
        self._PerPage = None
        self._PageNo = None
        self._SessionIds = None
        self._MimeTypes = None
        self._OrderDirection = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def SessionIds(self):
        r"""<p>Session ID.</p>
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds

    @property
    def MimeTypes(self):
        r"""<p>Message content type</p>
        :rtype: list of str
        """
        return self._MimeTypes

    @MimeTypes.setter
    def MimeTypes(self, MimeTypes):
        self._MimeTypes = MimeTypes

    @property
    def OrderDirection(self):
        r"""<p>Sorting order</p><p>Enumeration values:</p><ul><li>ASC: ascending order</li><li>DESC: descending order</li></ul>
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._SessionIds = params.get("SessionIds")
        self._MimeTypes = params.get("MimeTypes")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchArtifactsResponse(AbstractModel):
    r"""ListAIWorkbenchArtifacts response structure.

    """

    def __init__(self):
        r"""
        :param _Artifacts: <p>Product list</p>
        :type Artifacts: list of ArtifactInfo
        :param _PageResult: <p>Pagination result.</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Artifacts = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Artifacts(self):
        r"""<p>Product list</p>
        :rtype: list of ArtifactInfo
        """
        return self._Artifacts

    @Artifacts.setter
    def Artifacts(self, Artifacts):
        self._Artifacts = Artifacts

    @property
    def PageResult(self):
        r"""<p>Pagination result.</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Artifacts") is not None:
            self._Artifacts = []
            for item in params.get("Artifacts"):
                obj = ArtifactInfo()
                obj._deserialize(item)
                self._Artifacts.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchExecutionsRequest(AbstractModel):
    r"""ListAIWorkbenchExecutions request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _AgentId: <p>Filter by Agent</p>
        :type AgentId: str
        :param _Status: <p>Filter by status</p>
        :type Status: str
        :param _ExecutionIds: <p>Execution ID list filter</p>
        :type ExecutionIds: list of str
        :param _TaskIds: <p>Task ID.</p>
        :type TaskIds: list of str
        :param _TriggerType: <p>Trigger mode</p>
        :type TriggerType: str
        :param _Keyword: <p>Key value</p>
        :type Keyword: str
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._Status = None
        self._ExecutionIds = None
        self._TaskIds = None
        self._TriggerType = None
        self._Keyword = None
        self._Enabled = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>Filter by Agent</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Status(self):
        r"""<p>Filter by status</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExecutionIds(self):
        r"""<p>Execution ID list filter</p>
        :rtype: list of str
        """
        return self._ExecutionIds

    @ExecutionIds.setter
    def ExecutionIds(self, ExecutionIds):
        self._ExecutionIds = ExecutionIds

    @property
    def TaskIds(self):
        r"""<p>Task ID.</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def TriggerType(self):
        r"""<p>Trigger mode</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Keyword(self):
        r"""<p>Key value</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._Status = params.get("Status")
        self._ExecutionIds = params.get("ExecutionIds")
        self._TaskIds = params.get("TaskIds")
        self._TriggerType = params.get("TriggerType")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchExecutionsResponse(AbstractModel):
    r"""ListAIWorkbenchExecutions response structure.

    """

    def __init__(self):
        r"""
        :param _Executions: <p>Execution list.</p>
        :type Executions: list of ExecutionInfo
        :param _PageResult: <p>Pagination result.</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Executions = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Executions(self):
        r"""<p>Execution list.</p>
        :rtype: list of ExecutionInfo
        """
        return self._Executions

    @Executions.setter
    def Executions(self, Executions):
        self._Executions = Executions

    @property
    def PageResult(self):
        r"""<p>Pagination result.</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Executions") is not None:
            self._Executions = []
            for item in params.get("Executions"):
                obj = ExecutionInfo()
                obj._deserialize(item)
                self._Executions.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchMCPsRequest(AbstractModel):
    r"""ListAIWorkbenchMCPs request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _Transport: <p>Filter by transmission protocol</p>
        :type Transport: str
        :param _Keyword: <p>Search keyword</p>
        :type Keyword: str
        :param _Enabled: <p>Whether to enable filter</p>
        :type Enabled: bool
        :param _MCPIds: <p>Associated mcp</p>
        :type MCPIds: list of str
        :param _Type: <p>MCP type (built-in/private)</p><p>Enumeration values:</p><ul><li>builtin: platform built-in</li><li>private: user-customized</li></ul>
        :type Type: str
        """
        self._PerPage = None
        self._PageNo = None
        self._Transport = None
        self._Keyword = None
        self._Enabled = None
        self._MCPIds = None
        self._Type = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Transport(self):
        r"""<p>Filter by transmission protocol</p>
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def Keyword(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>Whether to enable filter</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MCPIds(self):
        r"""<p>Associated mcp</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def Type(self):
        r"""<p>MCP type (built-in/private)</p><p>Enumeration values:</p><ul><li>builtin: platform built-in</li><li>private: user-customized</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Transport = params.get("Transport")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        self._MCPIds = params.get("MCPIds")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchMCPsResponse(AbstractModel):
    r"""ListAIWorkbenchMCPs response structure.

    """

    def __init__(self):
        r"""
        :param _MCPs: <p>MCP list</p>
        :type MCPs: list of MCPInfo
        :param _PageResult: <p>Pagination result.</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MCPs = None
        self._PageResult = None
        self._RequestId = None

    @property
    def MCPs(self):
        r"""<p>MCP list</p>
        :rtype: list of MCPInfo
        """
        return self._MCPs

    @MCPs.setter
    def MCPs(self, MCPs):
        self._MCPs = MCPs

    @property
    def PageResult(self):
        r"""<p>Pagination result.</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("MCPs") is not None:
            self._MCPs = []
            for item in params.get("MCPs"):
                obj = MCPInfo()
                obj._deserialize(item)
                self._MCPs.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchMessagesRequest(AbstractModel):
    r"""ListAIWorkbenchMessages request structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Conversation ID</p>
        :type SessionId: str
        :param _Cursor: <p>Tag for cursor pagination</p>
        :type Cursor: str
        :param _Limit: <p>Window size</p>
        :type Limit: int
        :param _Direction: <p>Pull sequence</p>
        :type Direction: str
        """
        self._SessionId = None
        self._Cursor = None
        self._Limit = None
        self._Direction = None

    @property
    def SessionId(self):
        r"""<p>Conversation ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Cursor(self):
        r"""<p>Tag for cursor pagination</p>
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        r"""<p>Window size</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Direction(self):
        r"""<p>Pull sequence</p>
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchMessagesResponse(AbstractModel):
    r"""ListAIWorkbenchMessages response structure.

    """

    def __init__(self):
        r"""
        :param _Messages: <p>Message list.</p>
        :type Messages: list of MessageInfo
        :param _NextCursor: <p>Next cursor</p>
        :type NextCursor: str
        :param _HasMore: <p>Is there a follow-up?</p>
        :type HasMore: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Messages = None
        self._NextCursor = None
        self._HasMore = None
        self._RequestId = None

    @property
    def Messages(self):
        r"""<p>Message list.</p>
        :rtype: list of MessageInfo
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def NextCursor(self):
        r"""<p>Next cursor</p>
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def HasMore(self):
        r"""<p>Is there a follow-up?</p>
        :rtype: bool
        """
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

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
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageInfo()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchResourceInstancesRequest(AbstractModel):
    r"""ListAIWorkbenchResourceInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceMapId: <p>Resource map ID</p>
        :type ResourceMapId: str
        :param _PageParams: <p>Pagination parameters</p>
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNumParams`
        """
        self._ResourceMapId = None
        self._PageParams = None

    @property
    def ResourceMapId(self):
        r"""<p>Resource map ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def PageParams(self):
        r"""<p>Pagination parameters</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams


    def _deserialize(self, params):
        self._ResourceMapId = params.get("ResourceMapId")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNumParams()
            self._PageParams._deserialize(params.get("PageParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchResourceInstancesResponse(AbstractModel):
    r"""ListAIWorkbenchResourceInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: <p>Resource instance list</p>
        :type Instances: list of ResourceInstance
        :param _PageResult: <p>Pagination result</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""<p>Resource instance list</p>
        :rtype: list of ResourceInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def PageResult(self):
        r"""<p>Pagination result</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ResourceInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchResourceMapsRequest(AbstractModel):
    r"""ListAIWorkbenchResourceMaps request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _Keyword: <p>Search by name</p>
        :type Keyword: str
        """
        self._PerPage = None
        self._PageNo = None
        self._Keyword = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Keyword(self):
        r"""<p>Search by name</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchResourceMapsResponse(AbstractModel):
    r"""ListAIWorkbenchResourceMaps response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceMaps: <p>Resource map list</p>
        :type ResourceMaps: list of ResourceMapInfo
        :param _PageResult: <p>Pagination result.</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceMaps = None
        self._PageResult = None
        self._RequestId = None

    @property
    def ResourceMaps(self):
        r"""<p>Resource map list</p>
        :rtype: list of ResourceMapInfo
        """
        return self._ResourceMaps

    @ResourceMaps.setter
    def ResourceMaps(self, ResourceMaps):
        self._ResourceMaps = ResourceMaps

    @property
    def PageResult(self):
        r"""<p>Pagination result.</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("ResourceMaps") is not None:
            self._ResourceMaps = []
            for item in params.get("ResourceMaps"):
                obj = ResourceMapInfo()
                obj._deserialize(item)
                self._ResourceMaps.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchSessionsRequest(AbstractModel):
    r"""ListAIWorkbenchSessions request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _AgentId: <p>Filter by Agent</p>
        :type AgentId: str
        :param _Keyword: <p>Search keyword</p>
        :type Keyword: str
        :param _SessionIds: <p>Session ID list filtering</p>
        :type SessionIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._Keyword = None
        self._SessionIds = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>Filter by Agent</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Keyword(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SessionIds(self):
        r"""<p>Session ID list filtering</p>
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._Keyword = params.get("Keyword")
        self._SessionIds = params.get("SessionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchSessionsResponse(AbstractModel):
    r"""ListAIWorkbenchSessions response structure.

    """

    def __init__(self):
        r"""
        :param _Sessions: <p>Session list</p>
        :type Sessions: list of SessionInfo
        :param _PageResult: <p>Pagination result</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Sessions = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Sessions(self):
        r"""<p>Session list</p>
        :rtype: list of SessionInfo
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

    @property
    def PageResult(self):
        r"""<p>Pagination result</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = SessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchSkillsRequest(AbstractModel):
    r"""ListAIWorkbenchSkills request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _Type: <p>Filter by type</p>
        :type Type: str
        :param _Keyword: <p>Search keyword</p>
        :type Keyword: str
        :param _Enabled: <p>Whether to enable filter</p>
        :type Enabled: bool
        :param _SkillIds: <p>Skill ID list filter</p>
        :type SkillIds: list of str
        """
        self._PerPage = None
        self._PageNo = None
        self._Type = None
        self._Keyword = None
        self._Enabled = None
        self._SkillIds = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Type(self):
        r"""<p>Filter by type</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Keyword(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Enabled(self):
        r"""<p>Whether to enable filter</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def SkillIds(self):
        r"""<p>Skill ID list filter</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._Type = params.get("Type")
        self._Keyword = params.get("Keyword")
        self._Enabled = params.get("Enabled")
        self._SkillIds = params.get("SkillIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchSkillsResponse(AbstractModel):
    r"""ListAIWorkbenchSkills response structure.

    """

    def __init__(self):
        r"""
        :param _Skills: <p>List of skills</p>
        :type Skills: list of SkillInfo
        :param _PageResult: <p>Pagination result</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Skills = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Skills(self):
        r"""<p>List of skills</p>
        :rtype: list of SkillInfo
        """
        return self._Skills

    @Skills.setter
    def Skills(self, Skills):
        self._Skills = Skills

    @property
    def PageResult(self):
        r"""<p>Pagination result</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Skills") is not None:
            self._Skills = []
            for item in params.get("Skills"):
                obj = SkillInfo()
                obj._deserialize(item)
                self._Skills.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class ListAIWorkbenchTasksRequest(AbstractModel):
    r"""ListAIWorkbenchTasks request structure.

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number.</p>
        :type PageNo: int
        :param _AgentId: <p>Filter by Agent</p>
        :type AgentId: str
        :param _TriggerType: <p>Filter by trigger type</p>
        :type TriggerType: str
        :param _Keyword: <p>Search keyword</p>
        :type Keyword: str
        :param _TaskIds: <p>Task ID list filter</p>
        :type TaskIds: list of str
        :param _Enabled: <p>Whether to enable filter criteria</p>
        :type Enabled: bool
        """
        self._PerPage = None
        self._PageNo = None
        self._AgentId = None
        self._TriggerType = None
        self._Keyword = None
        self._TaskIds = None
        self._Enabled = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def AgentId(self):
        r"""<p>Filter by Agent</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def TriggerType(self):
        r"""<p>Filter by trigger type</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Keyword(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TaskIds(self):
        r"""<p>Task ID list filter</p>
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Enabled(self):
        r"""<p>Whether to enable filter criteria</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        self._AgentId = params.get("AgentId")
        self._TriggerType = params.get("TriggerType")
        self._Keyword = params.get("Keyword")
        self._TaskIds = params.get("TaskIds")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAIWorkbenchTasksResponse(AbstractModel):
    r"""ListAIWorkbenchTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: <p>Task List</p>
        :type Tasks: list of TaskInfo
        :param _PageResult: <p>Pagination result</p>
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._PageResult = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""<p>Task List</p>
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def PageResult(self):
        r"""<p>Pagination result</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNumResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNumResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class MCPInfo(AbstractModel):
    r"""MCP entity

    """

    def __init__(self):
        r"""
        :param _MCPId: <p>mcp ID</p>
        :type MCPId: str
        :param _Name: <p>MCP name</p>
        :type Name: str
        :param _Description: <p>MCP description</p>
        :type Description: str
        :param _Url: <p>MCP URL</p>
        :type Url: str
        :param _Transport: <p>Transport protocol: sse / streamable_http / stdio</p>
        :type Transport: str
        :param _AuthType: <p>Authentication type: none / bearer / basic / api_key</p>
        :type AuthType: str
        :param _AuthSecret: <p>Authentication key (masked in the response)</p>
        :type AuthSecret: str
        :param _Timeout: <p>Timeout (s)</p>
        :type Timeout: int
        :param _RetryCount: <p>Retry count</p>
        :type RetryCount: int
        :param _Headers: <p>Request header JSON</p>
        :type Headers: str
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._MCPId = None
        self._Name = None
        self._Description = None
        self._Url = None
        self._Transport = None
        self._AuthType = None
        self._AuthSecret = None
        self._Timeout = None
        self._RetryCount = None
        self._Headers = None
        self._Enabled = None

    @property
    def MCPId(self):
        r"""<p>mcp ID</p>
        :rtype: str
        """
        return self._MCPId

    @MCPId.setter
    def MCPId(self, MCPId):
        self._MCPId = MCPId

    @property
    def Name(self):
        r"""<p>MCP name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>MCP description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Url(self):
        r"""<p>MCP URL</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Transport(self):
        r"""<p>Transport protocol: sse / streamable_http / stdio</p>
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def AuthType(self):
        r"""<p>Authentication type: none / bearer / basic / api_key</p>
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AuthSecret(self):
        r"""<p>Authentication key (masked in the response)</p>
        :rtype: str
        """
        return self._AuthSecret

    @AuthSecret.setter
    def AuthSecret(self, AuthSecret):
        self._AuthSecret = AuthSecret

    @property
    def Timeout(self):
        r"""<p>Timeout (s)</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def RetryCount(self):
        r"""<p>Retry count</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def Headers(self):
        r"""<p>Request header JSON</p>
        :rtype: str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._MCPId = params.get("MCPId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Url = params.get("Url")
        self._Transport = params.get("Transport")
        self._AuthType = params.get("AuthType")
        self._AuthSecret = params.get("AuthSecret")
        self._Timeout = params.get("Timeout")
        self._RetryCount = params.get("RetryCount")
        self._Headers = params.get("Headers")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageInfo(AbstractModel):
    r"""Message entity

    """

    def __init__(self):
        r"""
        :param _EntryId: <p>Entity id</p>
        :type EntryId: str
        :param _SessionId: <p>Conversation ID</p>
        :type SessionId: str
        :param _Role: <p>Role: user / assistant</p>
        :type Role: str
        :param _Content: <p>Message content</p>
        :type Content: str
        :param _Status: <p>Status.</p>
        :type Status: str
        :param _ContentBlocks: <p>Block content.</p>
        :type ContentBlocks: list of ContentBlockInfo
        """
        self._EntryId = None
        self._SessionId = None
        self._Role = None
        self._Content = None
        self._Status = None
        self._ContentBlocks = None

    @property
    def EntryId(self):
        r"""<p>Entity id</p>
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SessionId(self):
        r"""<p>Conversation ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Role(self):
        r"""<p>Role: user / assistant</p>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""<p>Message content</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Status(self):
        r"""<p>Status.</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ContentBlocks(self):
        r"""<p>Block content.</p>
        :rtype: list of ContentBlockInfo
        """
        return self._ContentBlocks

    @ContentBlocks.setter
    def ContentBlocks(self, ContentBlocks):
        self._ContentBlocks = ContentBlocks


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SessionId = params.get("SessionId")
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._Status = params.get("Status")
        if params.get("ContentBlocks") is not None:
            self._ContentBlocks = []
            for item in params.get("ContentBlocks"):
                obj = ContentBlockInfo()
                obj._deserialize(item)
                self._ContentBlocks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyRelatedNotice(AbstractModel):
    r"""Notification template information associated with notification history

    """

    def __init__(self):
        r"""
        :param _NoticeId: Notification template ID
        :type NoticeId: str
        :param _NoticeName: Name of the notification template
        :type NoticeName: str
        """
        self._NoticeId = None
        self._NoticeName = None

    @property
    def NoticeId(self):
        r"""Notification template ID
        :rtype: str
        """
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def NoticeName(self):
        r"""Name of the notification template
        :rtype: str
        """
        return self._NoticeName

    @NoticeName.setter
    def NoticeName(self, NoticeName):
        self._NoticeName = NoticeName


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._NoticeName = params.get("NoticeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoParams(AbstractModel):
    r"""Pagination request parameters

    """

    def __init__(self):
        r"""
        :param _PerPage: Number of items per page.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PerPage: int
        :param _PageNo: Page number, starting from 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: str
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""Number of items per page.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""Page number, starting from 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoResult(AbstractModel):
    r"""Pagination result parameters

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _TotalPage: Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPage: int
        :param _CurrentPageNo: Current page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentPageNo: int
        :param _IsEnd: [Deprecated] Whether it has reached the end.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsEnd: bool
        :param _End: Whether it has traversed to the end.
        :type End: bool
        """
        self._TotalCount = None
        self._TotalPage = None
        self._CurrentPageNo = None
        self._IsEnd = None
        self._End = None

    @property
    def TotalCount(self):
        r"""Total data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPage(self):
        r"""Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def CurrentPageNo(self):
        r"""Current page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentPageNo

    @CurrentPageNo.setter
    def CurrentPageNo(self, CurrentPageNo):
        self._CurrentPageNo = CurrentPageNo

    @property
    def IsEnd(self):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        r"""[Deprecated] Whether it has reached the end.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        self._IsEnd = IsEnd

    @property
    def End(self):
        r"""Whether it has traversed to the end.
        :rtype: bool
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPage = params.get("TotalPage")
        self._CurrentPageNo = params.get("CurrentPageNo")
        self._IsEnd = params.get("IsEnd")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNumParams(AbstractModel):
    r"""Input parameter for paginating by which page

    """

    def __init__(self):
        r"""
        :param _PerPage: <p>Number of items per page</p>
        :type PerPage: int
        :param _PageNo: <p>Page number, starting from 1</p>
        :type PageNo: int
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""<p>Page number, starting from 1</p>
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNumResult(AbstractModel):
    r"""Pagination result parameters

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total number of data</p>
        :type TotalCount: int
        :param _TotalPage: <p>Total number of pages</p>
        :type TotalPage: int
        :param _CurrentPageNo: <p>Current page number</p>
        :type CurrentPageNo: int
        """
        self._TotalCount = None
        self._TotalPage = None
        self._CurrentPageNo = None

    @property
    def TotalCount(self):
        r"""<p>Total number of data</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPage(self):
        r"""<p>Total number of pages</p>
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def CurrentPageNo(self):
        r"""<p>Current page number</p>
        :rtype: int
        """
        return self._CurrentPageNo

    @CurrentPageNo.setter
    def CurrentPageNo(self, CurrentPageNo):
        self._CurrentPageNo = CurrentPageNo


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPage = params.get("TotalPage")
        self._CurrentPageNo = params.get("CurrentPageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInstance(AbstractModel):
    r"""Resource instance

    """

    def __init__(self):
        r"""
        :param _Id: <p>Instance ID</p>
        :type Id: str
        :param _Service: <p>Service name</p>
        :type Service: str
        :param _Region: <p>Region.</p>
        :type Region: str
        :param _IsReady: <p>Ready?</p>
        :type IsReady: bool
        """
        self._Id = None
        self._Service = None
        self._Region = None
        self._IsReady = None

    @property
    def Id(self):
        r"""<p>Instance ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Service(self):
        r"""<p>Service name</p>
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Region(self):
        r"""<p>Region.</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IsReady(self):
        r"""<p>Ready?</p>
        :rtype: bool
        """
        return self._IsReady

    @IsReady.setter
    def IsReady(self, IsReady):
        self._IsReady = IsReady


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Service = params.get("Service")
        self._Region = params.get("Region")
        self._IsReady = params.get("IsReady")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceMapInfo(AbstractModel):
    r"""Resource map entity

    """

    def __init__(self):
        r"""
        :param _ResourceMapId: <p>Resource map ID</p>
        :type ResourceMapId: str
        :param _Name: <p>Resource map name</p>
        :type Name: str
        :param _Description: <p>Resource map description</p>
        :type Description: str
        :param _InstanceCount: <p>Total number of instances</p>
        :type InstanceCount: int
        """
        self._ResourceMapId = None
        self._Name = None
        self._Description = None
        self._InstanceCount = None

    @property
    def ResourceMapId(self):
        r"""<p>Resource map ID</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def Name(self):
        r"""<p>Resource map name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Resource map description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceCount(self):
        r"""<p>Total number of instances</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._ResourceMapId = params.get("ResourceMapId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    r"""Session entity

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Session ID</p>
        :type SessionId: str
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Title: <p>Session title</p>
        :type Title: str
        :param _Status: <p>Status: active / archived / deleted</p>
        :type Status: str
        :param _TaskId: <p>If the session is triggered by a task, carry the task ID that triggers the session.</p>
        :type TaskId: str
        """
        self._SessionId = None
        self._AgentId = None
        self._Title = None
        self._Status = None
        self._TaskId = None

    @property
    def SessionId(self):
        r"""<p>Session ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Title(self):
        r"""<p>Session title</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        r"""<p>Status: active / archived / deleted</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""<p>If the session is triggered by a task, carry the task ID that triggers the session.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillInfo(AbstractModel):
    r"""Skill entity

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>Skill ID</p>
        :type SkillId: str
        :param _Name: <p>Skill name</p>
        :type Name: str
        :param _Description: <p>Skill description.</p>
        :type Description: str
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._SkillId = None
        self._Name = None
        self._Description = None
        self._Enabled = None

    @property
    def SkillId(self):
        r"""<p>Skill ID</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def Name(self):
        r"""<p>Skill name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Skill description.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tag.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Tag key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    r"""Task entity

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _Name: <p>Task name</p>
        :type Name: str
        :param _Description: <p>Task description</p>
        :type Description: str
        :param _AgentId: <p>Associated Agent ID</p>
        :type AgentId: str
        :param _PromptTemplate: <p>Prompt Template</p>
        :type PromptTemplate: str
        :param _OutputFormat: <p>Output format: markdown / json</p>
        :type OutputFormat: str
        :param _TriggerType: <p>Trigger type: manual / cron / webhook</p>
        :type TriggerType: str
        :param _CronExpr: <p>Cron expression</p>
        :type CronExpr: str
        :param _CronTimezone: <p>Cron time zone</p>
        :type CronTimezone: str
        :param _SkillIds: <p>List of associated skill IDs.</p>
        :type SkillIds: list of str
        :param _McpEndpointIds: <p>Associated MCP endpoint ID list</p>
        :type McpEndpointIds: list of str
        :param _TimeoutSec: <p>Timeout (seconds)</p>
        :type TimeoutSec: int
        :param _RetryCount: <p>Retry count</p>
        :type RetryCount: int
        :param _NotifyIds: <p>Notification id</p>
        :type NotifyIds: list of str
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._TaskId = None
        self._Name = None
        self._Description = None
        self._AgentId = None
        self._PromptTemplate = None
        self._OutputFormat = None
        self._TriggerType = None
        self._CronExpr = None
        self._CronTimezone = None
        self._SkillIds = None
        self._McpEndpointIds = None
        self._TimeoutSec = None
        self._RetryCount = None
        self._NotifyIds = None
        self._Enabled = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        r"""<p>Task name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Task description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AgentId(self):
        r"""<p>Associated Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def PromptTemplate(self):
        r"""<p>Prompt Template</p>
        :rtype: str
        """
        return self._PromptTemplate

    @PromptTemplate.setter
    def PromptTemplate(self, PromptTemplate):
        self._PromptTemplate = PromptTemplate

    @property
    def OutputFormat(self):
        r"""<p>Output format: markdown / json</p>
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def TriggerType(self):
        r"""<p>Trigger type: manual / cron / webhook</p>
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def CronExpr(self):
        r"""<p>Cron expression</p>
        :rtype: str
        """
        return self._CronExpr

    @CronExpr.setter
    def CronExpr(self, CronExpr):
        self._CronExpr = CronExpr

    @property
    def CronTimezone(self):
        r"""<p>Cron time zone</p>
        :rtype: str
        """
        return self._CronTimezone

    @CronTimezone.setter
    def CronTimezone(self, CronTimezone):
        self._CronTimezone = CronTimezone

    @property
    def SkillIds(self):
        r"""<p>List of associated skill IDs.</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def McpEndpointIds(self):
        r"""<p>Associated MCP endpoint ID list</p>
        :rtype: list of str
        """
        return self._McpEndpointIds

    @McpEndpointIds.setter
    def McpEndpointIds(self, McpEndpointIds):
        self._McpEndpointIds = McpEndpointIds

    @property
    def TimeoutSec(self):
        r"""<p>Timeout (seconds)</p>
        :rtype: int
        """
        return self._TimeoutSec

    @TimeoutSec.setter
    def TimeoutSec(self, TimeoutSec):
        self._TimeoutSec = TimeoutSec

    @property
    def RetryCount(self):
        r"""<p>Retry count</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def NotifyIds(self):
        r"""<p>Notification id</p>
        :rtype: list of str
        """
        return self._NotifyIds

    @NotifyIds.setter
    def NotifyIds(self, NotifyIds):
        self._NotifyIds = NotifyIds

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AgentId = params.get("AgentId")
        self._PromptTemplate = params.get("PromptTemplate")
        self._OutputFormat = params.get("OutputFormat")
        self._TriggerType = params.get("TriggerType")
        self._CronExpr = params.get("CronExpr")
        self._CronTimezone = params.get("CronTimezone")
        self._SkillIds = params.get("SkillIds")
        self._McpEndpointIds = params.get("McpEndpointIds")
        self._TimeoutSec = params.get("TimeoutSec")
        self._RetryCount = params.get("RetryCount")
        self._NotifyIds = params.get("NotifyIds")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAIWorkbenchTaskRequest(AbstractModel):
    r"""TriggerAIWorkbenchTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
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
        


class TriggerAIWorkbenchTaskResponse(AbstractModel):
    r"""TriggerAIWorkbenchTask response structure.

    """

    def __init__(self):
        r"""
        :param _ExecutionId: <p>Execution ID.</p>
        :type ExecutionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExecutionId = None
        self._RequestId = None

    @property
    def ExecutionId(self):
        r"""<p>Execution ID.</p>
        :rtype: str
        """
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

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
        self._ExecutionId = params.get("ExecutionId")
        self._RequestId = params.get("RequestId")


class UpdateAIWorkbenchAgentRequest(AbstractModel):
    r"""UpdateAIWorkbenchAgent request structure.

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Name: <p>Agent name</p>
        :type Name: str
        :param _Description: <p>Agent description</p>
        :type Description: str
        :param _Category: <p>Agent Category.</p>
        :type Category: str
        :param _Tags: <p>Agent Tag.</p>
        :type Tags: list of str
        :param _Instruction: <p>Agent prompt</p>
        :type Instruction: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        :param _SkillIds: <p>List of associated skill IDs.</p>
        :type SkillIds: list of str
        :param _Source: <p>Source</p>
        :type Source: str
        :param _Status: <p>Status.</p>
        :type Status: str
        :param _ResourceMapId: <p>ID of the associated resource map</p>
        :type ResourceMapId: str
        :param _MCPIds: <p>Associated mcp</p>
        :type MCPIds: list of str
        :param _EnvVars: <p>Environment variables required by the agent at runtime</p>
        :type EnvVars: list of EnvVar
        """
        self._AgentId = None
        self._Name = None
        self._Description = None
        self._Category = None
        self._Tags = None
        self._Instruction = None
        self._SkillIds = None
        self._Source = None
        self._Status = None
        self._ResourceMapId = None
        self._MCPIds = None
        self._EnvVars = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        r"""<p>Agent name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Agent description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Category(self):
        r"""<p>Agent Category.</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Tags(self):
        r"""<p>Agent Tag.</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Instruction(self):
        r"""<p>Agent prompt</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.InstructionConfig`
        """
        return self._Instruction

    @Instruction.setter
    def Instruction(self, Instruction):
        self._Instruction = Instruction

    @property
    def SkillIds(self):
        r"""<p>List of associated skill IDs.</p>
        :rtype: list of str
        """
        return self._SkillIds

    @SkillIds.setter
    def SkillIds(self, SkillIds):
        self._SkillIds = SkillIds

    @property
    def Source(self):
        r"""<p>Source</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Status(self):
        r"""<p>Status.</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceMapId(self):
        r"""<p>ID of the associated resource map</p>
        :rtype: str
        """
        return self._ResourceMapId

    @ResourceMapId.setter
    def ResourceMapId(self, ResourceMapId):
        self._ResourceMapId = ResourceMapId

    @property
    def MCPIds(self):
        r"""<p>Associated mcp</p>
        :rtype: list of str
        """
        return self._MCPIds

    @MCPIds.setter
    def MCPIds(self, MCPIds):
        self._MCPIds = MCPIds

    @property
    def EnvVars(self):
        r"""<p>Environment variables required by the agent at runtime</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Category = params.get("Category")
        self._Tags = params.get("Tags")
        if params.get("Instruction") is not None:
            self._Instruction = InstructionConfig()
            self._Instruction._deserialize(params.get("Instruction"))
        self._SkillIds = params.get("SkillIds")
        self._Source = params.get("Source")
        self._Status = params.get("Status")
        self._ResourceMapId = params.get("ResourceMapId")
        self._MCPIds = params.get("MCPIds")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIWorkbenchAgentResponse(AbstractModel):
    r"""UpdateAIWorkbenchAgent response structure.

    """

    def __init__(self):
        r"""
        :param _Agent: <p>Agent information after the update</p>
        :type Agent: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Agent = None
        self._RequestId = None

    @property
    def Agent(self):
        r"""<p>Agent information after the update</p>
        :rtype: :class:`tencentcloud.monitor.v20230616.models.AgentInfo`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = AgentInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._RequestId = params.get("RequestId")