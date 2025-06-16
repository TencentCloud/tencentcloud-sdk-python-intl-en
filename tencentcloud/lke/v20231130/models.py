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


class AICallConfig(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _EnableVoiceInteract: 
        :type EnableVoiceInteract: bool
        :param _EnableVoiceCall: 
        :type EnableVoiceCall: bool
        :param _EnableDigitalHuman: 
        :type EnableDigitalHuman: bool
        :param _Voice: 
        :type Voice: :class:`tencentcloud.lke.v20231130.models.VoiceConfig`
        :param _DigitalHuman: 
        :type DigitalHuman: :class:`tencentcloud.lke.v20231130.models.DigitalHumanConfig`
        """
        self._EnableVoiceInteract = None
        self._EnableVoiceCall = None
        self._EnableDigitalHuman = None
        self._Voice = None
        self._DigitalHuman = None

    @property
    def EnableVoiceInteract(self):
        """
        :rtype: bool
        """
        return self._EnableVoiceInteract

    @EnableVoiceInteract.setter
    def EnableVoiceInteract(self, EnableVoiceInteract):
        self._EnableVoiceInteract = EnableVoiceInteract

    @property
    def EnableVoiceCall(self):
        """
        :rtype: bool
        """
        return self._EnableVoiceCall

    @EnableVoiceCall.setter
    def EnableVoiceCall(self, EnableVoiceCall):
        self._EnableVoiceCall = EnableVoiceCall

    @property
    def EnableDigitalHuman(self):
        """
        :rtype: bool
        """
        return self._EnableDigitalHuman

    @EnableDigitalHuman.setter
    def EnableDigitalHuman(self, EnableDigitalHuman):
        self._EnableDigitalHuman = EnableDigitalHuman

    @property
    def Voice(self):
        """
        :rtype: :class:`tencentcloud.lke.v20231130.models.VoiceConfig`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def DigitalHuman(self):
        """
        :rtype: :class:`tencentcloud.lke.v20231130.models.DigitalHumanConfig`
        """
        return self._DigitalHuman

    @DigitalHuman.setter
    def DigitalHuman(self, DigitalHuman):
        self._DigitalHuman = DigitalHuman


    def _deserialize(self, params):
        self._EnableVoiceInteract = params.get("EnableVoiceInteract")
        self._EnableVoiceCall = params.get("EnableVoiceCall")
        self._EnableDigitalHuman = params.get("EnableDigitalHuman")
        if params.get("Voice") is not None:
            self._Voice = VoiceConfig()
            self._Voice._deserialize(params.get("Voice"))
        if params.get("DigitalHuman") is not None:
            self._DigitalHuman = DigitalHumanConfig()
            self._DigitalHuman._deserialize(params.get("DigitalHuman"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDebugInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Input: 
        :type Input: str
        :param _Output: 
        :type Output: str
        """
        self._Input = None
        self._Output = None

    @property
    def Input(self):
        """
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        """
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentProcedure(AbstractModel):
    """Process information of the thought event.

    """

    def __init__(self):
        r"""
        :param _Index: Index.
        :type Index: int
        :param _Name: English name of the execution process.
        :type Name: str
        :param _Title: Chinese name for display.
        :type Title: str
        :param _Status: Status constant: processing; success; failed.
        :type Status: str
        :param _Icon: Icon.
        :type Icon: str
        :param _Debugging: Agent debugging information.
        :type Debugging: :class:`tencentcloud.lke.v20231130.models.AgentProcedureDebugging`
        :param _Switch: Whether to switch to Agent. The value can be "main" or "workflow". Leave it blank for no switch.
        :type Switch: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _Elapsed: Current request execution time, in milliseconds.
        :type Elapsed: int
        :param _NodeName: Workflow node name.
        :type NodeName: str
        :param _ReplyIndex: Used to display in which reply bubble the thoughts are placed.
        :type ReplyIndex: int
        :param _SourceAgentName: Main agent.
        :type SourceAgentName: str
        :param _TargetAgentName: Registration agent.
        :type TargetAgentName: str
        :param _AgentIcon: Icon of Agent.
        :type AgentIcon: str
        """
        self._Index = None
        self._Name = None
        self._Title = None
        self._Status = None
        self._Icon = None
        self._Debugging = None
        self._Switch = None
        self._WorkflowName = None
        self._Elapsed = None
        self._NodeName = None
        self._ReplyIndex = None
        self._SourceAgentName = None
        self._TargetAgentName = None
        self._AgentIcon = None

    @property
    def Index(self):
        """Index.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        """English name of the execution process.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """Chinese name for display.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        """Status constant: processing; success; failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Icon(self):
        """Icon.
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Debugging(self):
        """Agent debugging information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentProcedureDebugging`
        """
        return self._Debugging

    @Debugging.setter
    def Debugging(self, Debugging):
        self._Debugging = Debugging

    @property
    def Switch(self):
        """Whether to switch to Agent. The value can be "main" or "workflow". Leave it blank for no switch.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def WorkflowName(self):
        """Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Elapsed(self):
        """Current request execution time, in milliseconds.
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def NodeName(self):
        """Workflow node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def ReplyIndex(self):
        """Used to display in which reply bubble the thoughts are placed.
        :rtype: int
        """
        return self._ReplyIndex

    @ReplyIndex.setter
    def ReplyIndex(self, ReplyIndex):
        self._ReplyIndex = ReplyIndex

    @property
    def SourceAgentName(self):
        """Main agent.
        :rtype: str
        """
        return self._SourceAgentName

    @SourceAgentName.setter
    def SourceAgentName(self, SourceAgentName):
        self._SourceAgentName = SourceAgentName

    @property
    def TargetAgentName(self):
        """Registration agent.
        :rtype: str
        """
        return self._TargetAgentName

    @TargetAgentName.setter
    def TargetAgentName(self, TargetAgentName):
        self._TargetAgentName = TargetAgentName

    @property
    def AgentIcon(self):
        """Icon of Agent.
        :rtype: str
        """
        return self._AgentIcon

    @AgentIcon.setter
    def AgentIcon(self, AgentIcon):
        self._AgentIcon = AgentIcon


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._Icon = params.get("Icon")
        if params.get("Debugging") is not None:
            self._Debugging = AgentProcedureDebugging()
            self._Debugging._deserialize(params.get("Debugging"))
        self._Switch = params.get("Switch")
        self._WorkflowName = params.get("WorkflowName")
        self._Elapsed = params.get("Elapsed")
        self._NodeName = params.get("NodeName")
        self._ReplyIndex = params.get("ReplyIndex")
        self._SourceAgentName = params.get("SourceAgentName")
        self._TargetAgentName = params.get("TargetAgentName")
        self._AgentIcon = params.get("AgentIcon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentProcedureDebugging(AbstractModel):
    """Debugging information of the agent thinking process.

    """

    def __init__(self):
        r"""
        :param _Content: Model thinking content.
        :type Content: str
        :param _DisplayContent: The specific text content to be displayed.
        :type DisplayContent: str
        :param _DisplayType: Display type.
        :type DisplayType: int
        :param _QuoteInfos: Index displayed by the search engine.
        :type QuoteInfos: list of QuoteInfo
        :param _References: Specific reference source.
        :type References: list of AgentReference
        :param _DisplayStatus: Display the ongoing status.
        :type DisplayStatus: str
        :param _SandboxUrl: URL of cloud desktop.
        :type SandboxUrl: str
        :param _DisplayUrl: URL opened through the browser in cloud desktop.
        :type DisplayUrl: str
        """
        self._Content = None
        self._DisplayContent = None
        self._DisplayType = None
        self._QuoteInfos = None
        self._References = None
        self._DisplayStatus = None
        self._SandboxUrl = None
        self._DisplayUrl = None

    @property
    def Content(self):
        """Model thinking content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DisplayContent(self):
        """The specific text content to be displayed.
        :rtype: str
        """
        return self._DisplayContent

    @DisplayContent.setter
    def DisplayContent(self, DisplayContent):
        self._DisplayContent = DisplayContent

    @property
    def DisplayType(self):
        """Display type.
        :rtype: int
        """
        return self._DisplayType

    @DisplayType.setter
    def DisplayType(self, DisplayType):
        self._DisplayType = DisplayType

    @property
    def QuoteInfos(self):
        """Index displayed by the search engine.
        :rtype: list of QuoteInfo
        """
        return self._QuoteInfos

    @QuoteInfos.setter
    def QuoteInfos(self, QuoteInfos):
        self._QuoteInfos = QuoteInfos

    @property
    def References(self):
        """Specific reference source.
        :rtype: list of AgentReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def DisplayStatus(self):
        """Display the ongoing status.
        :rtype: str
        """
        return self._DisplayStatus

    @DisplayStatus.setter
    def DisplayStatus(self, DisplayStatus):
        self._DisplayStatus = DisplayStatus

    @property
    def SandboxUrl(self):
        """URL of cloud desktop.
        :rtype: str
        """
        return self._SandboxUrl

    @SandboxUrl.setter
    def SandboxUrl(self, SandboxUrl):
        self._SandboxUrl = SandboxUrl

    @property
    def DisplayUrl(self):
        """URL opened through the browser in cloud desktop.
        :rtype: str
        """
        return self._DisplayUrl

    @DisplayUrl.setter
    def DisplayUrl(self, DisplayUrl):
        self._DisplayUrl = DisplayUrl


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._DisplayContent = params.get("DisplayContent")
        self._DisplayType = params.get("DisplayType")
        if params.get("QuoteInfos") is not None:
            self._QuoteInfos = []
            for item in params.get("QuoteInfos"):
                obj = QuoteInfo()
                obj._deserialize(item)
                self._QuoteInfos.append(obj)
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = AgentReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._DisplayStatus = params.get("DisplayStatus")
        self._SandboxUrl = params.get("SandboxUrl")
        self._DisplayUrl = params.get("DisplayUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentReference(AbstractModel):
    """Reference source in agent.

    """

    def __init__(self):
        r"""
        :param _DocId: Source document ID.
        :type DocId: str
        :param _Id: ID.
        :type Id: str
        :param _Name: Name.
        :type Name: str
        :param _Type: Type.
        :type Type: int
        :param _Url: URL.
        :type Url: str
        :param _DocBizId: Document business ID.
        :type DocBizId: str
        :param _DocName: Document name.
        :type DocName: str
        :param _QaBizId: Q&A business ID.
        :type QaBizId: str
        :param _Index: Index of search engine.
        :type Index: int
        :param _Title: Title.
        :type Title: str
        """
        self._DocId = None
        self._Id = None
        self._Name = None
        self._Type = None
        self._Url = None
        self._DocBizId = None
        self._DocName = None
        self._QaBizId = None
        self._Index = None
        self._Title = None

    @property
    def DocId(self):
        """Source document ID.
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def Id(self):
        """ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Type.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """URL.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DocBizId(self):
        """Document business ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def DocName(self):
        """Document name.
        :rtype: str
        """
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def QaBizId(self):
        """Q&A business ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Index(self):
        """Index of search engine.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Title(self):
        """Title.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._DocId = params.get("DocId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._DocBizId = params.get("DocBizId")
        self._DocName = params.get("DocName")
        self._QaBizId = params.get("QaBizId")
        self._Index = params.get("Index")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentThought(AbstractModel):
    """The thinking process of Agent.

    """

    def __init__(self):
        r"""
        :param _SessionId: Session ID.
        :type SessionId: str
        :param _RequestId: Request ID
        :type RequestId: str
        :param _RecordId: It corresponds to a session, session ID, used for message storage in answering. It can be generated in advance and used when saving messages.
        :type RecordId: str
        :param _Elapsed: Current request execution time, in milliseconds.
        :type Elapsed: int
        :param _IsWorkflow: Whether it is a workflow currently.
        :type IsWorkflow: bool
        :param _WorkflowName: If it is a workflow, workflow name.
        :type WorkflowName: str
        :param _Procedures: Detailed thinking process.
        :type Procedures: list of AgentProcedure
        :param _TraceId: TraceId.
        :type TraceId: str
        :param _Files: File information
        :type Files: list of FileInfo
        """
        self._SessionId = None
        self._RequestId = None
        self._RecordId = None
        self._Elapsed = None
        self._IsWorkflow = None
        self._WorkflowName = None
        self._Procedures = None
        self._TraceId = None
        self._Files = None

    @property
    def SessionId(self):
        """Session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """Request ID
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RecordId(self):
        """It corresponds to a session, session ID, used for message storage in answering. It can be generated in advance and used when saving messages.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Elapsed(self):
        """Current request execution time, in milliseconds.
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def IsWorkflow(self):
        """Whether it is a workflow currently.
        :rtype: bool
        """
        return self._IsWorkflow

    @IsWorkflow.setter
    def IsWorkflow(self, IsWorkflow):
        self._IsWorkflow = IsWorkflow

    @property
    def WorkflowName(self):
        """If it is a workflow, workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Procedures(self):
        """Detailed thinking process.
        :rtype: list of AgentProcedure
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TraceId(self):
        """TraceId.
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def Files(self):
        """File information
        :rtype: list of FileInfo
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")
        self._RecordId = params.get("RecordId")
        self._Elapsed = params.get("Elapsed")
        self._IsWorkflow = params.get("IsWorkflow")
        self._WorkflowName = params.get("WorkflowName")
        if params.get("Procedures") is not None:
            self._Procedures = []
            for item in params.get("Procedures"):
                obj = AgentProcedure()
                obj._deserialize(item)
                self._Procedures.append(obj)
        self._TraceId = params.get("TraceId")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiVarAttrInfo(AbstractModel):
    """Data of custom variable and label relationship.

    """

    def __init__(self):
        r"""
        :param _ApiVarId: Custom variable ID.
        :type ApiVarId: str
        :param _AttrBizId: Label ID.
        :type AttrBizId: str
        """
        self._ApiVarId = None
        self._AttrBizId = None

    @property
    def ApiVarId(self):
        """Custom variable ID.
        :rtype: str
        """
        return self._ApiVarId

    @ApiVarId.setter
    def ApiVarId(self, ApiVarId):
        self._ApiVarId = ApiVarId

    @property
    def AttrBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId


    def _deserialize(self, params):
        self._ApiVarId = params.get("ApiVarId")
        self._AttrBizId = params.get("AttrBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppConfig(AbstractModel):
    """Application configuration.

    """

    def __init__(self):
        r"""
        :param _KnowledgeQa: Knowledge Q&A management application configuration
        :type KnowledgeQa: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaConfig`
        :param _Summary: Knowledge summary application configuration.
        :type Summary: :class:`tencentcloud.lke.v20231130.models.SummaryConfig`
        :param _Classify: Label extraction application configuration.
        :type Classify: :class:`tencentcloud.lke.v20231130.models.ClassifyConfig`
        """
        self._KnowledgeQa = None
        self._Summary = None
        self._Classify = None

    @property
    def KnowledgeQa(self):
        """Knowledge Q&A management application configuration
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaConfig`
        """
        return self._KnowledgeQa

    @KnowledgeQa.setter
    def KnowledgeQa(self, KnowledgeQa):
        self._KnowledgeQa = KnowledgeQa

    @property
    def Summary(self):
        """Knowledge summary application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.SummaryConfig`
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Classify(self):
        """Label extraction application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ClassifyConfig`
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify


    def _deserialize(self, params):
        if params.get("KnowledgeQa") is not None:
            self._KnowledgeQa = KnowledgeQaConfig()
            self._KnowledgeQa._deserialize(params.get("KnowledgeQa"))
        if params.get("Summary") is not None:
            self._Summary = SummaryConfig()
            self._Summary._deserialize(params.get("Summary"))
        if params.get("Classify") is not None:
            self._Classify = ClassifyConfig()
            self._Classify._deserialize(params.get("Classify"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppInfo(AbstractModel):
    """Application details

    """

    def __init__(self):
        r"""
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _AppTypeDesc: Application type description.
        :type AppTypeDesc: str
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _Name: Application name.
        :type Name: str
        :param _Avatar: Application avatar.
        :type Avatar: str
        :param _Desc: Application description.
        :type Desc: str
        :param _AppStatus: Application status. 1: offline; 2: running; 3: disabled.
        :type AppStatus: int
        :param _AppStatusDesc: Status description.
        :type AppStatusDesc: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Operator: Last modifier.
        :type Operator: str
        :param _ModelName: Model name.
        :type ModelName: str
        :param _ModelAliasName: Alias of the generative model.
        :type ModelAliasName: str
        :param _Pattern: Application mode: standard; agent; single_workflow.
        :type Pattern: str
        :param _ThoughtModelAliasName: Alias of the thought model.
        :type ThoughtModelAliasName: str
        """
        self._AppType = None
        self._AppTypeDesc = None
        self._AppBizId = None
        self._Name = None
        self._Avatar = None
        self._Desc = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._UpdateTime = None
        self._Operator = None
        self._ModelName = None
        self._ModelAliasName = None
        self._Pattern = None
        self._ThoughtModelAliasName = None

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        """Application type description.
        :rtype: str
        """
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Name(self):
        """Application name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        """Application avatar.
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        """Application description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def AppStatus(self):
        """Application status. 1: offline; 2: running; 3: disabled.
        :rtype: int
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        """Status description.
        :rtype: str
        """
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        """Last modifier.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ModelName(self):
        """Model name.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelAliasName(self):
        """Alias of the generative model.
        :rtype: str
        """
        return self._ModelAliasName

    @ModelAliasName.setter
    def ModelAliasName(self, ModelAliasName):
        self._ModelAliasName = ModelAliasName

    @property
    def Pattern(self):
        """Application mode: standard; agent; single_workflow.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ThoughtModelAliasName(self):
        """Alias of the thought model.
        :rtype: str
        """
        return self._ThoughtModelAliasName

    @ThoughtModelAliasName.setter
    def ThoughtModelAliasName(self, ThoughtModelAliasName):
        self._ThoughtModelAliasName = ThoughtModelAliasName


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        self._AppBizId = params.get("AppBizId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._ModelName = params.get("ModelName")
        self._ModelAliasName = params.get("ModelAliasName")
        self._Pattern = params.get("Pattern")
        self._ThoughtModelAliasName = params.get("ThoughtModelAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppModel(AbstractModel):
    """Application model configuration.

    """

    def __init__(self):
        r"""
        :param _Name: Model name.
        :type Name: str
        :param _Desc: Model description.
        :type Desc: str
        :param _ContextLimit: The round referenced by the context.
        :type ContextLimit: int
        :param _AliasName: Model alias.
        :type AliasName: str
        :param _TokenBalance: Remaining token quota.
        :type TokenBalance: float
        :param _IsUseContext: Whether to use the round referenced by the context.
        :type IsUseContext: bool
        :param _HistoryLimit: The number of context memory rounds.
        :type HistoryLimit: int
        :param _UsageType: Usage type.
        :type UsageType: str
        :param _Temperature: Model temperature.
        :type Temperature: str
        :param _TopP: Model TopP.
        :type TopP: str
        :param _ResourceStatus: Model resource status: 1: available; 2: exhausted.
        :type ResourceStatus: int
        """
        self._Name = None
        self._Desc = None
        self._ContextLimit = None
        self._AliasName = None
        self._TokenBalance = None
        self._IsUseContext = None
        self._HistoryLimit = None
        self._UsageType = None
        self._Temperature = None
        self._TopP = None
        self._ResourceStatus = None

    @property
    def Name(self):
        """Model name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Model description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ContextLimit(self):
        """The round referenced by the context.
        :rtype: int
        """
        return self._ContextLimit

    @ContextLimit.setter
    def ContextLimit(self, ContextLimit):
        self._ContextLimit = ContextLimit

    @property
    def AliasName(self):
        """Model alias.
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TokenBalance(self):
        """Remaining token quota.
        :rtype: float
        """
        return self._TokenBalance

    @TokenBalance.setter
    def TokenBalance(self, TokenBalance):
        self._TokenBalance = TokenBalance

    @property
    def IsUseContext(self):
        """Whether to use the round referenced by the context.
        :rtype: bool
        """
        return self._IsUseContext

    @IsUseContext.setter
    def IsUseContext(self, IsUseContext):
        self._IsUseContext = IsUseContext

    @property
    def HistoryLimit(self):
        """The number of context memory rounds.
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def UsageType(self):
        """Usage type.
        :rtype: str
        """
        return self._UsageType

    @UsageType.setter
    def UsageType(self, UsageType):
        self._UsageType = UsageType

    @property
    def Temperature(self):
        """Model temperature.
        :rtype: str
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        """Model TopP.
        :rtype: str
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def ResourceStatus(self):
        """Model resource status: 1: available; 2: exhausted.
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ContextLimit = params.get("ContextLimit")
        self._AliasName = params.get("AliasName")
        self._TokenBalance = params.get("TokenBalance")
        self._IsUseContext = params.get("IsUseContext")
        self._HistoryLimit = params.get("HistoryLimit")
        self._UsageType = params.get("UsageType")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabel(AbstractModel):
    """Label details.

    """

    def __init__(self):
        r"""
        :param _Source: Label source.
        :type Source: int
        :param _AttrBizId: Label ID.
        :type AttrBizId: str
        :param _AttrKey: Label identification.
        :type AttrKey: str
        :param _AttrName: Label name.
        :type AttrName: str
        :param _Labels: Label value.
        :type Labels: list of Label
        """
        self._Source = None
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._Labels = None

    @property
    def Source(self):
        """Label source.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttrBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        """Label identification.
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        """Label name.
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        """Label value.
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelDetail(AbstractModel):
    """Label details.

    """

    def __init__(self):
        r"""
        :param _AttrBizId: Label ID.
        :type AttrBizId: str
        :param _AttrKey: Label identification.
        :type AttrKey: str
        :param _AttrName: Label name.
        :type AttrName: str
        :param _LabelNames: Label value name.
        :type LabelNames: list of str
        :param _IsUpdating: Whether the label is being updated.
        :type IsUpdating: bool
        :param _Status: Status.
        :type Status: int
        :param _StatusDesc: Status description.
        :type StatusDesc: str
        :param _LabelTotalCount: Total number of label values.
        :type LabelTotalCount: str
        """
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNames = None
        self._IsUpdating = None
        self._Status = None
        self._StatusDesc = None
        self._LabelTotalCount = None

    @property
    def AttrBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        """Label identification.
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        """Label name.
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNames(self):
        """Label value name.
        :rtype: list of str
        """
        return self._LabelNames

    @LabelNames.setter
    def LabelNames(self, LabelNames):
        self._LabelNames = LabelNames

    @property
    def IsUpdating(self):
        """Whether the label is being updated.
        :rtype: bool
        """
        return self._IsUpdating

    @IsUpdating.setter
    def IsUpdating(self, IsUpdating):
        self._IsUpdating = IsUpdating

    @property
    def Status(self):
        """Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def LabelTotalCount(self):
        """Total number of label values.
        :rtype: str
        """
        return self._LabelTotalCount

    @LabelTotalCount.setter
    def LabelTotalCount(self, LabelTotalCount):
        self._LabelTotalCount = LabelTotalCount


    def _deserialize(self, params):
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNames = params.get("LabelNames")
        self._IsUpdating = params.get("IsUpdating")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._LabelTotalCount = params.get("LabelTotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelRefer(AbstractModel):
    """Label reference information.

    """

    def __init__(self):
        r"""
        :param _Source: Label source, 1: label.
        :type Source: int
        :param _AttributeBizId: Label ID.
        :type AttributeBizId: str
        :param _LabelBizIds: Label value ID.
        :type LabelBizIds: list of str
        """
        self._Source = None
        self._AttributeBizId = None
        self._LabelBizIds = None

    @property
    def Source(self):
        """Label source, 1: label.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttributeBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LabelBizIds(self):
        """Label value ID.
        :rtype: list of str
        """
        return self._LabelBizIds

    @LabelBizIds.setter
    def LabelBizIds(self, LabelBizIds):
        self._LabelBizIds = LabelBizIds


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LabelBizIds = params.get("LabelBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeFilters(AbstractModel):
    """Export knowledge label filter.

    """

    def __init__(self):
        r"""
        :param _Query: Retrieve, attribute or label name.
        :type Query: str
        """
        self._Query = None

    @property
    def Query(self):
        """Retrieve, attribute or label name.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeLabel(AbstractModel):
    """Label value.

    """

    def __init__(self):
        r"""
        :param _LabelBizId: Standard word ID.
        :type LabelBizId: str
        :param _LabelName: Standard word name.
        :type LabelName: str
        :param _SimilarLabels: Synonym name.
        :type SimilarLabels: list of str
        """
        self._LabelBizId = None
        self._LabelName = None
        self._SimilarLabels = None

    @property
    def LabelBizId(self):
        """Standard word ID.
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        """Standard word name.
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def SimilarLabels(self):
        """Synonym name.
        :rtype: list of str
        """
        return self._SimilarLabels

    @SimilarLabels.setter
    def SimilarLabels(self, SimilarLabels):
        self._SimilarLabels = SimilarLabels


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        self._SimilarLabels = params.get("SimilarLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseConfig(AbstractModel):
    """Application basic configuration.

    """

    def __init__(self):
        r"""
        :param _Name: Application name.
        :type Name: str
        :param _Avatar: Application avatar url, required as an input parameter in "CreateApp" and "ModifyApp". Description of input parameter: 1. The image of input URL must be jpeg or png, with a size no more than 500kb, and the URL must allow head requests. 2. If the user does not have object storage, use the "Obtain temporary file upload key" (DescribeStorageCredential) API to obtain the COS temporary key and upload path. Upload the avatar to COS by yourself and get the access link.
        :type Avatar: str
        :param _Desc: Application description.
        :type Desc: str
        """
        self._Name = None
        self._Avatar = None
        self._Desc = None

    @property
    def Name(self):
        """Application name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        """Application avatar url, required as an input parameter in "CreateApp" and "ModifyApp". Description of input parameter: 1. The image of input URL must be jpeg or png, with a size no more than 500kb, and the URL must allow head requests. 2. If the user does not have object storage, use the "Obtain temporary file upload key" (DescribeStorageCredential) API to obtain the COS temporary key and upload path. Upload the avatar to COS by yourself and get the access link.
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        """Application description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDetail(AbstractModel):
    """Call type.

    """

    def __init__(self):
        r"""
        :param _Id: Associated ID.
        :type Id: str
        :param _CallTime: Call time.
        :type CallTime: str
        :param _TotalTokenUsage: Total token consumption.
        :type TotalTokenUsage: float
        :param _InputTokenUsage: Token consumption for input.
        :type InputTokenUsage: float
        :param _OutputTokenUsage: Token consumption for output.
        :type OutputTokenUsage: float
        :param _SearchUsage: Number of search service calls.
        :type SearchUsage: int
        :param _ModelName: Model name.
        :type ModelName: str
        :param _CallType: Call type.
        :type CallType: str
        :param _UinAccount: Account.
        :type UinAccount: str
        :param _AppName: Application name.
        :type AppName: str
        :param _PageUsage: Total number of consumed pages.
        :type PageUsage: int
        :param _SubScene: Filter sub-scenario.
        :type SubScene: str
        """
        self._Id = None
        self._CallTime = None
        self._TotalTokenUsage = None
        self._InputTokenUsage = None
        self._OutputTokenUsage = None
        self._SearchUsage = None
        self._ModelName = None
        self._CallType = None
        self._UinAccount = None
        self._AppName = None
        self._PageUsage = None
        self._SubScene = None

    @property
    def Id(self):
        """Associated ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CallTime(self):
        """Call time.
        :rtype: str
        """
        return self._CallTime

    @CallTime.setter
    def CallTime(self, CallTime):
        self._CallTime = CallTime

    @property
    def TotalTokenUsage(self):
        """Total token consumption.
        :rtype: float
        """
        return self._TotalTokenUsage

    @TotalTokenUsage.setter
    def TotalTokenUsage(self, TotalTokenUsage):
        self._TotalTokenUsage = TotalTokenUsage

    @property
    def InputTokenUsage(self):
        """Token consumption for input.
        :rtype: float
        """
        return self._InputTokenUsage

    @InputTokenUsage.setter
    def InputTokenUsage(self, InputTokenUsage):
        self._InputTokenUsage = InputTokenUsage

    @property
    def OutputTokenUsage(self):
        """Token consumption for output.
        :rtype: float
        """
        return self._OutputTokenUsage

    @OutputTokenUsage.setter
    def OutputTokenUsage(self, OutputTokenUsage):
        self._OutputTokenUsage = OutputTokenUsage

    @property
    def SearchUsage(self):
        """Number of search service calls.
        :rtype: int
        """
        return self._SearchUsage

    @SearchUsage.setter
    def SearchUsage(self, SearchUsage):
        self._SearchUsage = SearchUsage

    @property
    def ModelName(self):
        """Model name.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def CallType(self):
        """Call type.
        :rtype: str
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def UinAccount(self):
        """Account.
        :rtype: str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def AppName(self):
        """Application name.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PageUsage(self):
        """Total number of consumed pages.
        :rtype: int
        """
        return self._PageUsage

    @PageUsage.setter
    def PageUsage(self, PageUsage):
        self._PageUsage = PageUsage

    @property
    def SubScene(self):
        """Filter sub-scenario.
        :rtype: str
        """
        return self._SubScene

    @SubScene.setter
    def SubScene(self, SubScene):
        self._SubScene = SubScene


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CallTime = params.get("CallTime")
        self._TotalTokenUsage = params.get("TotalTokenUsage")
        self._InputTokenUsage = params.get("InputTokenUsage")
        self._OutputTokenUsage = params.get("OutputTokenUsage")
        self._SearchUsage = params.get("SearchUsage")
        self._ModelName = params.get("ModelName")
        self._CallType = params.get("CallType")
        self._UinAccount = params.get("UinAccount")
        self._AppName = params.get("AppName")
        self._PageUsage = params.get("PageUsage")
        self._SubScene = params.get("SubScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CateInfo(AbstractModel):
    """Category information.

    """

    def __init__(self):
        r"""
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _Name: Category name.
        :type Name: str
        :param _Total: Quantity of records (such as documents, synonyms, etc.) under the category.
        :type Total: int
        :param _CanAdd: Whether it is possible to add.
        :type CanAdd: bool
        :param _CanEdit: Whether it can be edited.
        :type CanEdit: bool
        :param _CanDelete: Whether it can be deleted.
        :type CanDelete: bool
        :param _Children: Subcategory.
        :type Children: list of CateInfo
        """
        self._CateBizId = None
        self._Name = None
        self._Total = None
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._Children = None

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Name(self):
        """Category name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        """Quantity of records (such as documents, synonyms, etc.) under the category.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CanAdd(self):
        """Whether it is possible to add.
        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        """Whether it can be edited.
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        """Whether it can be deleted.
        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Children(self):
        """Subcategory.
        :rtype: list of CateInfo
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._CateBizId = params.get("CateBizId")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = CateInfo()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistRequest(AbstractModel):
    """CheckAttributeLabelExist request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _LabelName: Attribute name.
        :type LabelName: str
        :param _AttributeBizId: Attribute ID.
        :type AttributeBizId: str
        :param _LoginUin: Log in to the user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to the user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _LastLabelBizId: Scroll loading, the last attribute label ID.
        :type LastLabelBizId: str
        """
        self._BotBizId = None
        self._LabelName = None
        self._AttributeBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LastLabelBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LabelName(self):
        """Attribute name.
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def AttributeBizId(self):
        """Attribute ID.
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LoginUin(self):
        """Log in to the user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to the user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LastLabelBizId(self):
        """Scroll loading, the last attribute label ID.
        :rtype: str
        """
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LabelName = params.get("LabelName")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LastLabelBizId = params.get("LastLabelBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistResponse(AbstractModel):
    """CheckAttributeLabelExist response structure.

    """

    def __init__(self):
        r"""
        :param _IsExist: Whether it exists.
        :type IsExist: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsExist = None
        self._RequestId = None

    @property
    def IsExist(self):
        """Whether it exists.
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

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
        self._IsExist = params.get("IsExist")
        self._RequestId = params.get("RequestId")


class CheckAttributeLabelReferRequest(AbstractModel):
    """CheckAttributeLabelRefer request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _LoginUin: Log in to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _LabelBizId: Attribute label.
        :type LabelBizId: str
        :param _AttributeBizId: Attribute ID.
        :type AttributeBizId: list of str
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LabelBizId = None
        self._AttributeBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        """Log in to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LabelBizId(self):
        """Attribute label.
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def AttributeBizId(self):
        """Attribute ID.
        :rtype: list of str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LabelBizId = params.get("LabelBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelReferResponse(AbstractModel):
    """CheckAttributeLabelRefer response structure.

    """

    def __init__(self):
        r"""
        :param _IsRefer: Whether to reference.
        :type IsRefer: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsRefer = None
        self._RequestId = None

    @property
    def IsRefer(self):
        """Whether to reference.
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

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
        self._IsRefer = params.get("IsRefer")
        self._RequestId = params.get("RequestId")


class ClassifyConfig(AbstractModel):
    """Label extraction configuration.

    """

    def __init__(self):
        r"""
        :param _Model: Model configuration.
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Labels: Label list.
        :type Labels: list of ClassifyLabel
        :param _Greeting: Welcome words, within 200 characters.
        :type Greeting: str
        """
        self._Model = None
        self._Labels = None
        self._Greeting = None

    @property
    def Model(self):
        """Model configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Labels(self):
        """Label list.
        :rtype: list of ClassifyLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Greeting(self):
        """Welcome words, within 200 characters.
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = ClassifyLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyLabel(AbstractModel):
    """Label information.

    """

    def __init__(self):
        r"""
        :param _Name: Label name.
        :type Name: str
        :param _Description: Label description.
        :type Description: str
        :param _Values: Label value range.
        :type Values: list of str
        """
        self._Name = None
        self._Description = None
        self._Values = None

    @property
    def Name(self):
        """Label name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Label description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Values(self):
        """Label value range.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Context(AbstractModel):
    """Obtain response of unsatisfied reply context.

    """

    def __init__(self):
        r"""
        :param _RecordBizId: Message record ID.
        :type RecordBizId: str
        :param _IsVisitor: Whether it is a user.
        :type IsVisitor: bool
        :param _NickName: Nickname.
        :type NickName: str
        :param _Avatar: Avatar.
        :type Avatar: str
        :param _Content: Message content.
        :type Content: str
        :param _FileInfos: Document information.
        :type FileInfos: list of MsgFileInfo
        :param _ReplyMethod: Response method, 15: clarification confirmation response.
        :type ReplyMethod: int
        """
        self._RecordBizId = None
        self._IsVisitor = None
        self._NickName = None
        self._Avatar = None
        self._Content = None
        self._FileInfos = None
        self._ReplyMethod = None

    @property
    def RecordBizId(self):
        """Message record ID.
        :rtype: str
        """
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def IsVisitor(self):
        """Whether it is a user.
        :rtype: bool
        """
        return self._IsVisitor

    @IsVisitor.setter
    def IsVisitor(self, IsVisitor):
        self._IsVisitor = IsVisitor

    @property
    def NickName(self):
        """Nickname.
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Avatar(self):
        """Avatar.
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Content(self):
        """Message content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileInfos(self):
        """Document information.
        :rtype: list of MsgFileInfo
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def ReplyMethod(self):
        """Response method, 15: clarification confirmation response.
        :rtype: int
        """
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod


    def _deserialize(self, params):
        self._RecordBizId = params.get("RecordBizId")
        self._IsVisitor = params.get("IsVisitor")
        self._NickName = params.get("NickName")
        self._Avatar = params.get("Avatar")
        self._Content = params.get("Content")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = MsgFileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        self._ReplyMethod = params.get("ReplyMethod")
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
        :param _AppType: Application type; knowledge_qa - knowledge qa management.
        :type AppType: str
        :param _BaseConfig: Basic application configuration.
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        self._AppType = None
        self._BaseConfig = None

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge qa management.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        """Basic application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
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
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _IsCustomList: Whether the account application list permissions are customized. A user interaction prompt.
        :type IsCustomList: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppBizId = None
        self._IsCustomList = None
        self._RequestId = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def IsCustomList(self):
        """Whether the account application list permissions are customized. A user interaction prompt.
        :rtype: bool
        """
        return self._IsCustomList

    @IsCustomList.setter
    def IsCustomList(self, IsCustomList):
        self._IsCustomList = IsCustomList

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
        self._AppBizId = params.get("AppBizId")
        self._IsCustomList = params.get("IsCustomList")
        self._RequestId = params.get("RequestId")


class CreateAttributeLabelRequest(AbstractModel):
    """CreateAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _AttrName: Label name.
        :type AttrName: str
        :param _Labels: Label value.
        :type Labels: list of AttributeLabel
        :param _AttrKey: Label identification (not effective, no need to fill in) . Abolished.
        :type AttrKey: str
        :param _LoginUin: Log in to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttrName = None
        self._Labels = None
        self._AttrKey = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttrName(self):
        """Label name.
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        """Label value.
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def AttrKey(self):
        """Label identification (not effective, no need to fill in) . Abolished.
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def LoginUin(self):
        """Log in to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._AttrKey = params.get("AttrKey")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttributeLabelResponse(AbstractModel):
    """CreateAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _AttrBizId: Label ID.
        :type AttrBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttrBizId = None
        self._RequestId = None

    @property
    def AttrBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

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
        self._AttrBizId = params.get("AttrBizId")
        self._RequestId = params.get("RequestId")


class CreateCorpRequest(AbstractModel):
    """CreateCorp request structure.

    """

    def __init__(self):
        r"""
        :param _FullName: Full name of the corporate.
        :type FullName: str
        :param _ContactName: Contact person's name.
        :type ContactName: str
        :param _Email: Contact person's mailbox.
        :type Email: str
        :param _Telephone: Contact person's mobile phone number.
        :type Telephone: str
        """
        self._FullName = None
        self._ContactName = None
        self._Email = None
        self._Telephone = None

    @property
    def FullName(self):
        """Full name of the corporate.
        :rtype: str
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def ContactName(self):
        """Contact person's name.
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def Email(self):
        """Contact person's mailbox.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Telephone(self):
        """Contact person's mobile phone number.
        :rtype: str
        """
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._ContactName = params.get("ContactName")
        self._Email = params.get("Email")
        self._Telephone = params.get("Telephone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpResponse(AbstractModel):
    """CreateCorp response structure.

    """

    def __init__(self):
        r"""
        :param _CorpBizId: Corporate ID.
        :type CorpBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CorpBizId = None
        self._RequestId = None

    @property
    def CorpBizId(self):
        """Corporate ID.
        :rtype: str
        """
        return self._CorpBizId

    @CorpBizId.setter
    def CorpBizId(self, CorpBizId):
        self._CorpBizId = CorpBizId

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
        self._CorpBizId = params.get("CorpBizId")
        self._RequestId = params.get("RequestId")


class CreateDocCateRequest(AbstractModel):
    """CreateDocCate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _ParentBizId: Parent business ID.
        :type ParentBizId: str
        :param _Name: Category name.

        :type Name: str
        """
        self._BotBizId = None
        self._ParentBizId = None
        self._Name = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ParentBizId(self):
        """Parent business ID.
        :rtype: str
        """
        return self._ParentBizId

    @ParentBizId.setter
    def ParentBizId(self, ParentBizId):
        self._ParentBizId = ParentBizId

    @property
    def Name(self):
        """Category name.

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ParentBizId = params.get("ParentBizId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocCateResponse(AbstractModel):
    """CreateDocCate response structure.

    """

    def __init__(self):
        r"""
        :param _CanAdd: Whether it is possible to add.

        :type CanAdd: bool
        :param _CanEdit: Whether it is editable.
        :type CanEdit: bool
        :param _CanDelete: Whether it can be deleted.

        :type CanDelete: bool
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def CanAdd(self):
        """Whether it is possible to add.

        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        """Whether it is editable.
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        """Whether it can be deleted.

        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class CreateQACateRequest(AbstractModel):
    """CreateQACate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _ParentBizId: Parent business id. pass the string "0" when creating a top-level category.
        :type ParentBizId: str
        :param _Name: Category name.

        :type Name: str
        """
        self._BotBizId = None
        self._ParentBizId = None
        self._Name = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ParentBizId(self):
        """Parent business id. pass the string "0" when creating a top-level category.
        :rtype: str
        """
        return self._ParentBizId

    @ParentBizId.setter
    def ParentBizId(self, ParentBizId):
        self._ParentBizId = ParentBizId

    @property
    def Name(self):
        """Category name.

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ParentBizId = params.get("ParentBizId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQACateResponse(AbstractModel):
    """CreateQACate response structure.

    """

    def __init__(self):
        r"""
        :param _CanAdd: Whether it is possible to add.

        :type CanAdd: bool
        :param _CanEdit: Whether it is editable.
        :type CanEdit: bool
        :param _CanDelete: Whether it can be deleted.

        :type CanDelete: bool
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def CanAdd(self):
        """Whether it is possible to add.

        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        """Whether it is editable.
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        """Whether it can be deleted.

        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class CreateQARequest(AbstractModel):
    """CreateQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _Question: Question.
        :type Question: str
        :param _Answer: Answer.
        :type Answer: str
        :param _AttrRange: Applicable scope of labels: 1. all; 2. by conditions.
        :type AttrRange: int
        :param _CustomParam: Custom parameter.
        :type CustomParam: str
        :param _AttrLabels: Label reference.
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _SimilarQuestions: Similar question content.
        :type SimilarQuestions: list of str
        :param _QuestionDesc: Question description.
        :type QuestionDesc: str
        """
        self._BotBizId = None
        self._Question = None
        self._Answer = None
        self._AttrRange = None
        self._CustomParam = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestions = None
        self._QuestionDesc = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttrRange(self):
        """Applicable scope of labels: 1. all; 2. by conditions.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def CustomParam(self):
        """Custom parameter.
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrLabels(self):
        """Label reference.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestions(self):
        """Similar question content.
        :rtype: list of str
        """
        return self._SimilarQuestions

    @SimilarQuestions.setter
    def SimilarQuestions(self, SimilarQuestions):
        self._SimilarQuestions = SimilarQuestions

    @property
    def QuestionDesc(self):
        """Question description.
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._AttrRange = params.get("AttrRange")
        self._CustomParam = params.get("CustomParam")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._SimilarQuestions = params.get("SimilarQuestions")
        self._QuestionDesc = params.get("QuestionDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQAResponse(AbstractModel):
    """CreateQA response structure.

    """

    def __init__(self):
        r"""
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QaBizId = None
        self._RequestId = None

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

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
        self._QaBizId = params.get("QaBizId")
        self._RequestId = params.get("RequestId")


class CreateReconstructDocumentFlowConfig(AbstractModel):
    """Configuration information for creating a smart document parsing task.

    """

    def __init__(self):
        r"""
        :param _TableResultType: The returned form of a table in a markdown file: 
0: the table is returned in MD format;
1: the table is returned in HTML form.
The default is 1.
        :type TableResultType: str
        :param _ResultType: The format of smart document parsing results:
0: only return full-text MD;
1: only return OCR original JSON of each page;.
2: only return MD of each page;
3: return full-text MD + OCR original JSON of each page;.
4: return full-text MD + MD of each page.
The default value is 3 (return full-text MD + OCR original JSON of each page).

        :type ResultType: str
        """
        self._TableResultType = None
        self._ResultType = None

    @property
    def TableResultType(self):
        """The returned form of a table in a markdown file: 
0: the table is returned in MD format;
1: the table is returned in HTML form.
The default is 1.
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        """The format of smart document parsing results:
0: only return full-text MD;
1: only return OCR original JSON of each page;.
2: only return MD of each page;
3: return full-text MD + OCR original JSON of each page;.
4: return full-text MD + MD of each page.
The default value is 3 (return full-text MD + OCR original JSON of each page).

        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowRequest(AbstractModel):
    """CreateReconstructDocumentFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FileType: File type. Supported file types: pdf, doc, docx, ppt, pptx, md, txt, xls, xlsx, csv, png, jpg, jpeg, bmp, gif, webp, heic, eps, icns, im, pcx, ppm, tiff, xbm, heif, jp2.
        :type FileType: str
        :param _FileBase64: The base64 value of the file. File size limit: the downloaded file does not exceed 8m after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :type FileBase64: str
        :param _FileUrl: <p>File URL. The file download time does not exceed 15 seconds. Supported image pixels: the length of a single side is between 20-10000px. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. The downloaded file shall not exceed the supported file size after Base64 encoding: </p><table> <tbody> <tr> <td>File Type</td> <td>Supported File Size</td> </tr> <tr> <td>PDF</td> <td>200M</td> </tr> <tr> <td>DOC</td> <td>200M</td> </tr> <tr> <td>DOCX</td> <td>200M</td> </tr> <tr> <td>PPT</td> <td>200M</td> </tr> <tr> <td>PPTX</td> <td>200M</td> </tr> <tr> <td>MD</td> <td>10M</td> </tr> <tr> <td>TXT</td> <td>10M</td> </tr> <tr> <td>XLS</td> <td>20M</td> </tr> <tr> <td>XLSX</td> <td>20M</td> </tr> <tr> <td>CSV</td> <td>20M</td> </tr> <tr> <td>PNG</td> <td>20M</td> </tr> <tr> <td>JPG</td> <td>20M</td> </tr> <tr> <td>JPEG</td> <td>20M</td> </tr> <tr> <td>BMP</td> <td>20M</td> </tr> <tr> <td>GIF</td> <td>20M</td> </tr> <tr> <td>WEBP</td> <td>20M</td> </tr> <tr> <td>HEIC</td> <td>20M</td> </tr> <tr> <td>EPS</td> <td>20M</td> </tr> <tr> <td>ICNS</td> <td>20M</td> </tr> <tr> <td>IM</td> <td>20M</td> </tr> <tr> <td>PCX</td> <td>20M</td> </tr> <tr> <td>PPM</td> <td>20M</td> </tr> <tr> <td>TIFF</td> <td>20M</td> </tr> <tr> <td>XBM</td> <td>20M</td> </tr> <tr> <td>HEIF</td> <td>20M</td> </tr> <tr> <td>JP2</td> <td>20M</td> </tr> </tbody> <colgroup> <col> <col> </colgroup></table>
        :type FileUrl: str
        :param _FileStartPageNumber: When type of the uploaded file is pdf, doc, docx, ppt, or pptx, it specifies the starting page number for file recognition, including the current value. The default is 1, indicating recognition starts from the first page of the file.
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: When type of the uploaded file is pdf, doc, docx, orppt, pptx, it specifies the end page number for file recognition, including the current value. The default is 100, indicating recognition up to page 100 of the file. a single call supports recognition of up to 1000 pages, i.e., FileEndPageNumber-FileStartPageNumber should be no more than 1000.
        :type FileEndPageNumber: int
        :param _Config: Configuration information for creating a document parsing task.
        :type Config: :class:`tencentcloud.lke.v20231130.models.CreateReconstructDocumentFlowConfig`
        """
        self._FileType = None
        self._FileBase64 = None
        self._FileUrl = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """File type. Supported file types: pdf, doc, docx, ppt, pptx, md, txt, xls, xlsx, csv, png, jpg, jpeg, bmp, gif, webp, heic, eps, icns, im, pcx, ppm, tiff, xbm, heif, jp2.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileBase64(self):
        """The base64 value of the file. File size limit: the downloaded file does not exceed 8m after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileUrl(self):
        """<p>File URL. The file download time does not exceed 15 seconds. Supported image pixels: the length of a single side is between 20-10000px. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. The downloaded file shall not exceed the supported file size after Base64 encoding: </p><table> <tbody> <tr> <td>File Type</td> <td>Supported File Size</td> </tr> <tr> <td>PDF</td> <td>200M</td> </tr> <tr> <td>DOC</td> <td>200M</td> </tr> <tr> <td>DOCX</td> <td>200M</td> </tr> <tr> <td>PPT</td> <td>200M</td> </tr> <tr> <td>PPTX</td> <td>200M</td> </tr> <tr> <td>MD</td> <td>10M</td> </tr> <tr> <td>TXT</td> <td>10M</td> </tr> <tr> <td>XLS</td> <td>20M</td> </tr> <tr> <td>XLSX</td> <td>20M</td> </tr> <tr> <td>CSV</td> <td>20M</td> </tr> <tr> <td>PNG</td> <td>20M</td> </tr> <tr> <td>JPG</td> <td>20M</td> </tr> <tr> <td>JPEG</td> <td>20M</td> </tr> <tr> <td>BMP</td> <td>20M</td> </tr> <tr> <td>GIF</td> <td>20M</td> </tr> <tr> <td>WEBP</td> <td>20M</td> </tr> <tr> <td>HEIC</td> <td>20M</td> </tr> <tr> <td>EPS</td> <td>20M</td> </tr> <tr> <td>ICNS</td> <td>20M</td> </tr> <tr> <td>IM</td> <td>20M</td> </tr> <tr> <td>PCX</td> <td>20M</td> </tr> <tr> <td>PPM</td> <td>20M</td> </tr> <tr> <td>TIFF</td> <td>20M</td> </tr> <tr> <td>XBM</td> <td>20M</td> </tr> <tr> <td>HEIF</td> <td>20M</td> </tr> <tr> <td>JP2</td> <td>20M</td> </tr> </tbody> <colgroup> <col> <col> </colgroup></table>
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileStartPageNumber(self):
        """When type of the uploaded file is pdf, doc, docx, ppt, or pptx, it specifies the starting page number for file recognition, including the current value. The default is 1, indicating recognition starts from the first page of the file.
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """When type of the uploaded file is pdf, doc, docx, orppt, pptx, it specifies the end page number for file recognition, including the current value. The default is 100, indicating recognition up to page 100 of the file. a single call supports recognition of up to 1000 pages, i.e., FileEndPageNumber-FileStartPageNumber should be no more than 1000.
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """Configuration information for creating a document parsing task.
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateReconstructDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileBase64 = params.get("FileBase64")
        self._FileUrl = params.get("FileUrl")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateReconstructDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowResponse(AbstractModel):
    """CreateReconstructDocumentFlow response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID. The processing result corresponding to TaskId can be queried through the API [GetReconstructDocumentResult](https://cloud.tencent.com/document/product/1759/107505) within 30 days.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Unique task ID. The processing result corresponding to TaskId can be queried through the API [GetReconstructDocumentResult](https://cloud.tencent.com/document/product/1759/107505) within 30 days.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateRejectedQuestionRequest(AbstractModel):
    """CreateRejectedQuestion request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _Question: Rejected question
        :type Question: str
        :param _BusinessSource: Unique ID of the data source for the rejected question - "2" will be returned when the rejected question is not satisfied - The rejected question comes from manual addition.
        :type BusinessSource: int
        :param _BusinessId: Unique ID of the data source for the rejected question.


        :type BusinessId: str
        """
        self._BotBizId = None
        self._Question = None
        self._BusinessSource = None
        self._BusinessId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        """Rejected question
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def BusinessSource(self):
        """Unique ID of the data source for the rejected question - "2" will be returned when the rejected question is not satisfied - The rejected question comes from manual addition.
        :rtype: int
        """
        return self._BusinessSource

    @BusinessSource.setter
    def BusinessSource(self, BusinessSource):
        self._BusinessSource = BusinessSource

    @property
    def BusinessId(self):
        """Unique ID of the data source for the rejected question.


        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._BusinessSource = params.get("BusinessSource")
        self._BusinessId = params.get("BusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRejectedQuestionResponse(AbstractModel):
    """CreateRejectedQuestion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateReleaseRequest(AbstractModel):
    """CreateRelease request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Robot ID.
        :type BotBizId: str
        :param _Desc: Release description.
        :type Desc: str
        """
        self._BotBizId = None
        self._Desc = None

    @property
    def BotBizId(self):
        """Robot ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Desc(self):
        """Release description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseResponse(AbstractModel):
    """CreateRelease response structure.

    """

    def __init__(self):
        r"""
        :param _ReleaseBizId: Release ID.
        :type ReleaseBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReleaseBizId = None
        self._RequestId = None

    @property
    def ReleaseBizId(self):
        """Release ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

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
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """Temporary key structure.

    """

    def __init__(self):
        r"""
        :param _Token: Token.
        :type Token: str
        :param _TmpSecretId: Temporary license key ID.
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary license key.
        :type TmpSecretKey: str
        :param _AppId: Temporary license appid.
        :type AppId: int
        """
        self._Token = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._AppId = None

    @property
    def Token(self):
        """Token.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def TmpSecretId(self):
        """Temporary license key ID.
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Temporary license key.
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def AppId(self):
        """Temporary license appid.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppRequest(AbstractModel):
    """DeleteApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        """
        self._AppBizId = None
        self._AppType = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppResponse(AbstractModel):
    """DeleteApp response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteAttributeLabelRequest(AbstractModel):
    """DeleteAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _AttributeBizIds: Label ID.
        :type AttributeBizIds: list of str
        :param _LoginUin: Log in to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttributeBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizIds(self):
        """Label ID.
        :rtype: list of str
        """
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def LoginUin(self):
        """Log in to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizIds = params.get("AttributeBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttributeLabelResponse(AbstractModel):
    """DeleteAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDocCateRequest(AbstractModel):
    """DeleteDocCate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocCateResponse(AbstractModel):
    """DeleteDocCate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDocRequest(AbstractModel):
    """DeleteDoc request structure.

    """

    def __init__(self):
        r"""
        :param _DocBizIds: List of document business IDs.
        :type DocBizIds: list of str
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._DocBizIds = None
        self._BotBizId = None

    @property
    def DocBizIds(self):
        """List of document business IDs.
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._DocBizIds = params.get("DocBizIds")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocResponse(AbstractModel):
    """DeleteDoc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteQACateRequest(AbstractModel):
    """DeleteQACate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQACateResponse(AbstractModel):
    """DeleteQACate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteQARequest(AbstractModel):
    """DeleteQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _QaBizIds: Q&A ID.
        :type QaBizIds: list of str
        """
        self._BotBizId = None
        self._QaBizIds = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        """Q&A ID.
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQAResponse(AbstractModel):
    """DeleteQA response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRejectedQuestionRequest(AbstractModel):
    """DeleteRejectedQuestion request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _RejectedBizIds: The unique ID of the data source for the rejected question.



        :type RejectedBizIds: list of str
        """
        self._BotBizId = None
        self._RejectedBizIds = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def RejectedBizIds(self):
        """The unique ID of the data source for the rejected question.



        :rtype: list of str
        """
        return self._RejectedBizIds

    @RejectedBizIds.setter
    def RejectedBizIds(self, RejectedBizIds):
        self._RejectedBizIds = RejectedBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._RejectedBizIds = params.get("RejectedBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRejectedQuestionResponse(AbstractModel):
    """DeleteRejectedQuestion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeAppRequest(AbstractModel):
    """DescribeApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _IsRelease: Whether it is the configuration after release.
        :type IsRelease: bool
        """
        self._AppBizId = None
        self._AppType = None
        self._IsRelease = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def IsRelease(self):
        """Whether it is the configuration after release.
        :rtype: bool
        """
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._IsRelease = params.get("IsRelease")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppResponse(AbstractModel):
    """DescribeApp response structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _AppTypeDesc: Application type description.
        :type AppTypeDesc: str
        :param _BaseConfig: Application type description.
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _AppConfig: Application configuration.
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        :param _AvatarInAppeal: Whether the avatar is under appeal.
        :type AvatarInAppeal: bool
        :param _RoleInAppeal: Whether the role description is under appeal.
        :type RoleInAppeal: bool
        :param _NameInAppeal: Whether the name is under appeal.
        :type NameInAppeal: bool
        :param _GreetingInAppeal: Whether the welcome words are under appeal.
        :type GreetingInAppeal: bool
        :param _BareAnswerInAppeal: Whether the response message for unknown questions is under appeal.
        :type BareAnswerInAppeal: bool
        :param _AppKey: App key of the application.
        :type AppKey: str
        :param _AppStatus: Application status. 1: offline; 2: running; 3: disabled.
        :type AppStatus: int
        :param _AppStatusDesc: Status description.
        :type AppStatusDesc: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppBizId = None
        self._AppType = None
        self._AppTypeDesc = None
        self._BaseConfig = None
        self._AppConfig = None
        self._AvatarInAppeal = None
        self._RoleInAppeal = None
        self._NameInAppeal = None
        self._GreetingInAppeal = None
        self._BareAnswerInAppeal = None
        self._AppKey = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._RequestId = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        """Application type description.
        :rtype: str
        """
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def BaseConfig(self):
        """Application type description.
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def AppConfig(self):
        """Application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        """
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def AvatarInAppeal(self):
        """Whether the avatar is under appeal.
        :rtype: bool
        """
        return self._AvatarInAppeal

    @AvatarInAppeal.setter
    def AvatarInAppeal(self, AvatarInAppeal):
        self._AvatarInAppeal = AvatarInAppeal

    @property
    def RoleInAppeal(self):
        """Whether the role description is under appeal.
        :rtype: bool
        """
        return self._RoleInAppeal

    @RoleInAppeal.setter
    def RoleInAppeal(self, RoleInAppeal):
        self._RoleInAppeal = RoleInAppeal

    @property
    def NameInAppeal(self):
        """Whether the name is under appeal.
        :rtype: bool
        """
        return self._NameInAppeal

    @NameInAppeal.setter
    def NameInAppeal(self, NameInAppeal):
        self._NameInAppeal = NameInAppeal

    @property
    def GreetingInAppeal(self):
        """Whether the welcome words are under appeal.
        :rtype: bool
        """
        return self._GreetingInAppeal

    @GreetingInAppeal.setter
    def GreetingInAppeal(self, GreetingInAppeal):
        self._GreetingInAppeal = GreetingInAppeal

    @property
    def BareAnswerInAppeal(self):
        """Whether the response message for unknown questions is under appeal.
        :rtype: bool
        """
        return self._BareAnswerInAppeal

    @BareAnswerInAppeal.setter
    def BareAnswerInAppeal(self, BareAnswerInAppeal):
        self._BareAnswerInAppeal = BareAnswerInAppeal

    @property
    def AppKey(self):
        """App key of the application.
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppStatus(self):
        """Application status. 1: offline; 2: running; 3: disabled.
        :rtype: int
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        """Status description.
        :rtype: str
        """
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

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
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        self._AvatarInAppeal = params.get("AvatarInAppeal")
        self._RoleInAppeal = params.get("RoleInAppeal")
        self._NameInAppeal = params.get("NameInAppeal")
        self._GreetingInAppeal = params.get("GreetingInAppeal")
        self._BareAnswerInAppeal = params.get("BareAnswerInAppeal")
        self._AppKey = params.get("AppKey")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._RequestId = params.get("RequestId")


class DescribeAttributeLabelRequest(AbstractModel):
    """DescribeAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _AttributeBizId: Attribute ID.
        :type AttributeBizId: str
        :param _Limit: Quantity loaded each time. 
        :type Limit: int
        :param _LoginUin: Log in to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _Query: Query a label or similar labels.
        :type Query: str
        :param _LastLabelBizId: The label ID of the scroll loading cursor.
        :type LastLabelBizId: str
        :param _QueryScope: Query scope: 
all (or leave it blank): standard words and similar words 
standard: standard words 
similar: similar words
        :type QueryScope: str
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._Limit = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._LastLabelBizId = None
        self._QueryScope = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        """Attribute ID.
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def Limit(self):
        """Quantity loaded each time. 
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoginUin(self):
        """Log in to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        """Query a label or similar labels.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LastLabelBizId(self):
        """The label ID of the scroll loading cursor.
        :rtype: str
        """
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId

    @property
    def QueryScope(self):
        """Query scope: 
all (or leave it blank): standard words and similar words 
standard: standard words 
similar: similar words
        :rtype: str
        """
        return self._QueryScope

    @QueryScope.setter
    def QueryScope(self, QueryScope):
        self._QueryScope = QueryScope


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._Limit = params.get("Limit")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._LastLabelBizId = params.get("LastLabelBizId")
        self._QueryScope = params.get("QueryScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttributeLabelResponse(AbstractModel):
    """DescribeAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _AttributeBizId: Attribute ID.
        :type AttributeBizId: str
        :param _AttrKey: Attribute identifier.
        :type AttrKey: str
        :param _AttrName: Attribute name.
        :type AttrName: str
        :param _LabelNumber: Quantity of labels.
        :type LabelNumber: str
        :param _Labels: Label name.
        :type Labels: list of AttributeLabel
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AttributeBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNumber = None
        self._Labels = None
        self._RequestId = None

    @property
    def AttributeBizId(self):
        """Attribute ID.
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrKey(self):
        """Attribute identifier.
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        """Attribute name.
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNumber(self):
        """Quantity of labels.
        :rtype: str
        """
        return self._LabelNumber

    @LabelNumber.setter
    def LabelNumber(self, LabelNumber):
        self._LabelNumber = LabelNumber

    @property
    def Labels(self):
        """Label name.
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

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
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNumber = params.get("LabelNumber")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallStatsGraphRequest(AbstractModel):
    """DescribeCallStatsGraph request structure.

    """

    def __init__(self):
        r"""
        :param _UinAccount: uin
        :type UinAccount: list of str
        :param _LoginUin: Log in to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Log in to user's root sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _SubBizType: Sub-business type.
        :type SubBizType: str
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds.
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds.
        :type EndTime: str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        :param _SubScenes: Filter sub-scenarios (used in document parsing scenarios).
        :type SubScenes: list of str
        """
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SubScenes = None

    @property
    def UinAccount(self):
        """uin
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        """Log in to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Log in to user's root sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        """Sub-business type.
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SubScenes(self):
        """Filter sub-scenarios (used in document parsing scenarios).
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SubScenes = params.get("SubScenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallStatsGraphResponse(AbstractModel):
    """DescribeCallStatsGraph response structure.

    """

    def __init__(self):
        r"""
        :param _List: Statistical information of API calls.
        :type List: list of Stat
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Statistical information of API calls.
        :rtype: list of Stat
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Stat()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConcurrencyUsageGraphRequest(AbstractModel):
    """DescribeConcurrencyUsageGraph request structure.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds.
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds.
        :type EndTime: str
        :param _UinAccount: uin
        :type UinAccount: list of str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _SubBizType: Sub-business type.
        :type SubBizType: str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        """
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._AppBizIds = None

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UinAccount(self):
        """uin
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        """Sub-business type.
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrencyUsageGraphResponse(AbstractModel):
    """DescribeConcurrencyUsageGraph response structure.

    """

    def __init__(self):
        r"""
        :param _X: X-axis: time zone; returns two interval ranges of "minute/hour/day" according to the granularity of query conditions.
        :type X: list of str
        :param _AvailableY: Available concurrent Y-axis coordinate.
        :type AvailableY: list of int
        :param _SuccessCallY: Succeeded to call the concurrent Y-axis coordinate.
        :type SuccessCallY: list of int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._X = None
        self._AvailableY = None
        self._SuccessCallY = None
        self._RequestId = None

    @property
    def X(self):
        """X-axis: time zone; returns two interval ranges of "minute/hour/day" according to the granularity of query conditions.
        :rtype: list of str
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def AvailableY(self):
        """Available concurrent Y-axis coordinate.
        :rtype: list of int
        """
        return self._AvailableY

    @AvailableY.setter
    def AvailableY(self, AvailableY):
        self._AvailableY = AvailableY

    @property
    def SuccessCallY(self):
        """Succeeded to call the concurrent Y-axis coordinate.
        :rtype: list of int
        """
        return self._SuccessCallY

    @SuccessCallY.setter
    def SuccessCallY(self, SuccessCallY):
        self._SuccessCallY = SuccessCallY

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
        self._X = params.get("X")
        self._AvailableY = params.get("AvailableY")
        self._SuccessCallY = params.get("SuccessCallY")
        self._RequestId = params.get("RequestId")


class DescribeConcurrencyUsageRequest(AbstractModel):
    """DescribeConcurrencyUsage request structure.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model identification.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds.
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds.
        :type EndTime: str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        """
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None

    @property
    def ModelName(self):
        """Model identification.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrencyUsageResponse(AbstractModel):
    """DescribeConcurrencyUsage response structure.

    """

    def __init__(self):
        r"""
        :param _AvailableConcurrency: The upper limit of available concurrency.
        :type AvailableConcurrency: int
        :param _ConcurrencyPeak: Peak concurrent value.
        :type ConcurrencyPeak: int
        :param _ExceedUsageTime: The number of times exceeding the capacity limit of available concurrency.
        :type ExceedUsageTime: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AvailableConcurrency = None
        self._ConcurrencyPeak = None
        self._ExceedUsageTime = None
        self._RequestId = None

    @property
    def AvailableConcurrency(self):
        """The upper limit of available concurrency.
        :rtype: int
        """
        return self._AvailableConcurrency

    @AvailableConcurrency.setter
    def AvailableConcurrency(self, AvailableConcurrency):
        self._AvailableConcurrency = AvailableConcurrency

    @property
    def ConcurrencyPeak(self):
        """Peak concurrent value.
        :rtype: int
        """
        return self._ConcurrencyPeak

    @ConcurrencyPeak.setter
    def ConcurrencyPeak(self, ConcurrencyPeak):
        self._ConcurrencyPeak = ConcurrencyPeak

    @property
    def ExceedUsageTime(self):
        """The number of times exceeding the capacity limit of available concurrency.
        :rtype: int
        """
        return self._ExceedUsageTime

    @ExceedUsageTime.setter
    def ExceedUsageTime(self, ExceedUsageTime):
        self._ExceedUsageTime = ExceedUsageTime

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
        self._AvailableConcurrency = params.get("AvailableConcurrency")
        self._ConcurrencyPeak = params.get("ConcurrencyPeak")
        self._ExceedUsageTime = params.get("ExceedUsageTime")
        self._RequestId = params.get("RequestId")


class DescribeCorpRequest(AbstractModel):
    """DescribeCorp request structure.

    """


class DescribeCorpResponse(AbstractModel):
    """DescribeCorp response structure.

    """

    def __init__(self):
        r"""
        :param _CorpBizId: Corporate ID.

        :type CorpBizId: str
        :param _RobotQuota: Application quota.
        :type RobotQuota: int
        :param _FullName: Full name of the corporate.

        :type FullName: str
        :param _IsTrial: Whether to try out.
        :type IsTrial: bool
        :param _IsTrialExpired: Whether the trial has expired.
        :type IsTrialExpired: bool
        :param _AvailableAppQuota: Quantity of available applications.
        :type AvailableAppQuota: int
        :param _IsSupportCustomModel: Whether custom model configuration is supported.
        :type IsSupportCustomModel: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CorpBizId = None
        self._RobotQuota = None
        self._FullName = None
        self._IsTrial = None
        self._IsTrialExpired = None
        self._AvailableAppQuota = None
        self._IsSupportCustomModel = None
        self._RequestId = None

    @property
    def CorpBizId(self):
        """Corporate ID.

        :rtype: str
        """
        return self._CorpBizId

    @CorpBizId.setter
    def CorpBizId(self, CorpBizId):
        self._CorpBizId = CorpBizId

    @property
    def RobotQuota(self):
        """Application quota.
        :rtype: int
        """
        return self._RobotQuota

    @RobotQuota.setter
    def RobotQuota(self, RobotQuota):
        self._RobotQuota = RobotQuota

    @property
    def FullName(self):
        """Full name of the corporate.

        :rtype: str
        """
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def IsTrial(self):
        """Whether to try out.
        :rtype: bool
        """
        return self._IsTrial

    @IsTrial.setter
    def IsTrial(self, IsTrial):
        self._IsTrial = IsTrial

    @property
    def IsTrialExpired(self):
        """Whether the trial has expired.
        :rtype: bool
        """
        return self._IsTrialExpired

    @IsTrialExpired.setter
    def IsTrialExpired(self, IsTrialExpired):
        self._IsTrialExpired = IsTrialExpired

    @property
    def AvailableAppQuota(self):
        """Quantity of available applications.
        :rtype: int
        """
        return self._AvailableAppQuota

    @AvailableAppQuota.setter
    def AvailableAppQuota(self, AvailableAppQuota):
        self._AvailableAppQuota = AvailableAppQuota

    @property
    def IsSupportCustomModel(self):
        """Whether custom model configuration is supported.
        :rtype: bool
        """
        return self._IsSupportCustomModel

    @IsSupportCustomModel.setter
    def IsSupportCustomModel(self, IsSupportCustomModel):
        self._IsSupportCustomModel = IsSupportCustomModel

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
        self._CorpBizId = params.get("CorpBizId")
        self._RobotQuota = params.get("RobotQuota")
        self._FullName = params.get("FullName")
        self._IsTrial = params.get("IsTrial")
        self._IsTrialExpired = params.get("IsTrialExpired")
        self._AvailableAppQuota = params.get("AvailableAppQuota")
        self._IsSupportCustomModel = params.get("IsSupportCustomModel")
        self._RequestId = params.get("RequestId")


class DescribeDocRequest(AbstractModel):
    """DescribeDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocResponse(AbstractModel):
    """DescribeDoc response structure.

    """

    def __init__(self):
        r"""
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _FileName: File name.
        :type FileName: str
        :param _FileType: File type.
        :type FileType: str
        :param _CosUrl: COS path.
        :type CosUrl: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Status: Document status : 1: not generated; 2: generating; 3: generation successful; 4: generation failed; 5: deleting; 6: deleted successfully; 7: under review; 8: review failed; 9: review successful; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 15: updating; 16: update failed; 17: parsing; 18: parsing failed; 19: import failed; 20: expired; 21: excessive invalid; 22: excessive invalid recovered.
        :type Status: int
        :param _StatusDesc: Document status description.
        :type StatusDesc: str
        :param _Reason: Reason for generation failure.
        :type Reason: str
        :param _IsRefer: Whether to refer in the answer.
        :type IsRefer: bool
        :param _QaNum: Number of Q&A pairs.
        :type QaNum: int
        :param _IsDeleted: Whether to delete.
        :type IsDeleted: bool
        :param _Source: Document source.
        :type Source: int
        :param _SourceDesc: Document source description.
        :type SourceDesc: str
        :param _IsAllowRestart: Whether regeneration is allowed.
        :type IsAllowRestart: bool
        :param _IsDeletedQa: Whether Q&A has been deleted.
        :type IsDeletedQa: bool
        :param _IsCreatingQa: Whether Q&A is being generated.
        :type IsCreatingQa: bool
        :param _IsAllowDelete: Whether deletion is allowed.
        :type IsAllowDelete: bool
        :param _IsAllowRefer: Whether to allow operation reference switch.
        :type IsAllowRefer: bool
        :param _IsCreatedQa: Whether Q&A has been generated.
        :type IsCreatedQa: bool
        :param _DocCharSize: Document character count.
        :type DocCharSize: str
        :param _IsAllowEdit: Whether editing is allowed.
        :type IsAllowEdit: bool
        :param _AttrRange: Applicable scope of labels 1: all, 2: by condition range.
        :type AttrRange: int
        :param _AttrLabels: Label.
        :type AttrLabels: list of AttrLabel
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._IsAllowEdit = None
        self._AttrRange = None
        self._AttrLabels = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        """File name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        """COS path.
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Document status : 1: not generated; 2: generating; 3: generation successful; 4: generation failed; 5: deleting; 6: deleted successfully; 7: under review; 8: review failed; 9: review successful; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 15: updating; 16: update failed; 17: parsing; 18: parsing failed; 19: import failed; 20: expired; 21: excessive invalid; 22: excessive invalid recovered.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Document status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        """Reason for generation failure.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        """Whether to refer in the answer.
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        """Number of Q&A pairs.
        :rtype: int
        """
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        """Whether to delete.
        :rtype: bool
        """
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        """Document source.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        """Document source description.
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        """Whether regeneration is allowed.
        :rtype: bool
        """
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        """Whether Q&A has been deleted.
        :rtype: bool
        """
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        """Whether Q&A is being generated.
        :rtype: bool
        """
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        """Whether deletion is allowed.
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        """Whether to allow operation reference switch.
        :rtype: bool
        """
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        """Whether Q&A has been generated.
        :rtype: bool
        """
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        """Document character count.
        :rtype: str
        """
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def IsAllowEdit(self):
        """Whether editing is allowed.
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def AttrRange(self):
        """Applicable scope of labels 1: all, 2: by condition range.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Label.
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

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
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeUsagePieGraphRequest(AbstractModel):
    """DescribeKnowledgeUsagePieGraph request structure.

    """

    def __init__(self):
        r"""
        :param _AppBizIds: Application id array.
        :type AppBizIds: list of str
        """
        self._AppBizIds = None

    @property
    def AppBizIds(self):
        """Application id array.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeUsagePieGraphResponse(AbstractModel):
    """DescribeKnowledgeUsagePieGraph response structure.

    """

    def __init__(self):
        r"""
        :param _AvailableCharSize: Total number of characters used by all applications.
        :type AvailableCharSize: str
        :param _List: List of application pie chart details.
        :type List: list of KnowledgeCapacityPieGraphDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AvailableCharSize = None
        self._List = None
        self._RequestId = None

    @property
    def AvailableCharSize(self):
        """Total number of characters used by all applications.
        :rtype: str
        """
        return self._AvailableCharSize

    @AvailableCharSize.setter
    def AvailableCharSize(self, AvailableCharSize):
        self._AvailableCharSize = AvailableCharSize

    @property
    def List(self):
        """List of application pie chart details.
        :rtype: list of KnowledgeCapacityPieGraphDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._AvailableCharSize = params.get("AvailableCharSize")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = KnowledgeCapacityPieGraphDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeUsageRequest(AbstractModel):
    """DescribeKnowledgeUsage request structure.

    """


class DescribeKnowledgeUsageResponse(AbstractModel):
    """DescribeKnowledgeUsage response structure.

    """

    def __init__(self):
        r"""
        :param _AvailableCharSize: The upper limit of available characters.
        :type AvailableCharSize: str
        :param _ExceedCharSize: Number of characters exceeding the capacity limit of available characters.
        :type ExceedCharSize: str
        :param _UsedCharSize: Total number of characters used in the knowledge library.
        :type UsedCharSize: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AvailableCharSize = None
        self._ExceedCharSize = None
        self._UsedCharSize = None
        self._RequestId = None

    @property
    def AvailableCharSize(self):
        """The upper limit of available characters.
        :rtype: str
        """
        return self._AvailableCharSize

    @AvailableCharSize.setter
    def AvailableCharSize(self, AvailableCharSize):
        self._AvailableCharSize = AvailableCharSize

    @property
    def ExceedCharSize(self):
        """Number of characters exceeding the capacity limit of available characters.
        :rtype: str
        """
        return self._ExceedCharSize

    @ExceedCharSize.setter
    def ExceedCharSize(self, ExceedCharSize):
        self._ExceedCharSize = ExceedCharSize

    @property
    def UsedCharSize(self):
        """Total number of characters used in the knowledge library.
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

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
        self._AvailableCharSize = params.get("AvailableCharSize")
        self._ExceedCharSize = params.get("ExceedCharSize")
        self._UsedCharSize = params.get("UsedCharSize")
        self._RequestId = params.get("RequestId")


class DescribeQARequest(AbstractModel):
    """DescribeQA request structure.

    """

    def __init__(self):
        r"""
        :param _QaBizId: Q&A business ID.

        :type QaBizId: str
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._QaBizId = None
        self._BotBizId = None

    @property
    def QaBizId(self):
        """Q&A business ID.

        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQAResponse(AbstractModel):
    """DescribeQA response structure.

    """

    def __init__(self):
        r"""
        :param _QaBizId: Q&A business ID.

        :type QaBizId: str
        :param _Question: Question.

        :type Question: str
        :param _Answer: Answer.

        :type Answer: str
        :param _CustomParam: Custom parameter.
        :type CustomParam: str
        :param _Source: Source:
1 - Q&A pairs generated from documents.
2 - Q&A pairs imported in batches.
3 - Q&A pairs input manually one by one.


        :type Source: int
        :param _SourceDesc: Source description.

        :type SourceDesc: str
        :param _UpdateTime: Update time.


        :type UpdateTime: str
        :param _Status: Status<br>1 - pending verification; 2 - not released; 3 - releasing; 4 - released; 5 - release failed; 6 - not approved; 7 - under review; 8 - review failed, 9 - review failed, pending manual review after appeal; 11 - review failed, manual review not passed after appeal; 12 - expired; 13 - excessive invalid; 14 - excessive invalid recovered; 19 - learning; 20 - learning failed.


        :type Status: int
        :param _StatusDesc: Status description.


        :type StatusDesc: str
        :param _CateBizId: Category ID.

        :type CateBizId: str
        :param _IsAllowAccept: Whether verification is allowed.

        :type IsAllowAccept: bool
        :param _IsAllowDelete: Whether deletion is allowed.

        :type IsAllowDelete: bool
        :param _IsAllowEdit: Whether editing is allowed.

        :type IsAllowEdit: bool
        :param _DocBizId: Document ID.

        :type DocBizId: str
        :param _FileName: Document name.

        :type FileName: str
        :param _FileType: Document type.

        :type FileType: str
        :param _SegmentBizId: Segment ID.

        :type SegmentBizId: str
        :param _PageContent: Segment content.
        :type PageContent: str
        :param _Highlights: Segment highlight content.
        :type Highlights: list of Highlight
        :param _OrgData: Segment content.

        :type OrgData: str
        :param _AttrRange: Applicable scope of label.
        :type AttrRange: int
        :param _AttrLabels: Label.
        :type AttrLabels: list of AttrLabel
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _SimilarQuestions: Similar question list information.
        :type SimilarQuestions: list of SimilarQuestion
        :param _QaAuditStatus: Review status of Q&A text: 1 - review failed.
        :type QaAuditStatus: int
        :param _PicAuditStatus: Review status of image in Q&A: 1-review failed.
        :type PicAuditStatus: int
        :param _VideoAuditStatus: Review status of video in Q&A: 1 - review failed.
        :type VideoAuditStatus: int
        :param _QuestionDesc: Question description.
        :type QuestionDesc: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._CateBizId = None
        self._IsAllowAccept = None
        self._IsAllowDelete = None
        self._IsAllowEdit = None
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._SegmentBizId = None
        self._PageContent = None
        self._Highlights = None
        self._OrgData = None
        self._AttrRange = None
        self._AttrLabels = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestions = None
        self._QaAuditStatus = None
        self._PicAuditStatus = None
        self._VideoAuditStatus = None
        self._QuestionDesc = None
        self._RequestId = None

    @property
    def QaBizId(self):
        """Q&A business ID.

        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        """Question.

        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.

        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        """Custom parameter.
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def Source(self):
        """Source:
1 - Q&A pairs generated from documents.
2 - Q&A pairs imported in batches.
3 - Q&A pairs input manually one by one.


        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        """Source description.

        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        """Update time.


        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Status<br>1 - pending verification; 2 - not released; 3 - releasing; 4 - released; 5 - release failed; 6 - not approved; 7 - under review; 8 - review failed, 9 - review failed, pending manual review after appeal; 11 - review failed, manual review not passed after appeal; 12 - expired; 13 - excessive invalid; 14 - excessive invalid recovered; 19 - learning; 20 - learning failed.


        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Status description.


        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CateBizId(self):
        """Category ID.

        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsAllowAccept(self):
        """Whether verification is allowed.

        :rtype: bool
        """
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def IsAllowDelete(self):
        """Whether deletion is allowed.

        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowEdit(self):
        """Whether editing is allowed.

        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def DocBizId(self):
        """Document ID.

        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        """Document name.

        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """Document type.

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SegmentBizId(self):
        """Segment ID.

        :rtype: str
        """
        return self._SegmentBizId

    @SegmentBizId.setter
    def SegmentBizId(self, SegmentBizId):
        self._SegmentBizId = SegmentBizId

    @property
    def PageContent(self):
        """Segment content.
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Highlights(self):
        """Segment highlight content.
        :rtype: list of Highlight
        """
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        """Segment content.

        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def AttrRange(self):
        """Applicable scope of label.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Label.
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestions(self):
        """Similar question list information.
        :rtype: list of SimilarQuestion
        """
        return self._SimilarQuestions

    @SimilarQuestions.setter
    def SimilarQuestions(self, SimilarQuestions):
        self._SimilarQuestions = SimilarQuestions

    @property
    def QaAuditStatus(self):
        """Review status of Q&A text: 1 - review failed.
        :rtype: int
        """
        return self._QaAuditStatus

    @QaAuditStatus.setter
    def QaAuditStatus(self, QaAuditStatus):
        self._QaAuditStatus = QaAuditStatus

    @property
    def PicAuditStatus(self):
        """Review status of image in Q&A: 1-review failed.
        :rtype: int
        """
        return self._PicAuditStatus

    @PicAuditStatus.setter
    def PicAuditStatus(self, PicAuditStatus):
        self._PicAuditStatus = PicAuditStatus

    @property
    def VideoAuditStatus(self):
        """Review status of video in Q&A: 1 - review failed.
        :rtype: int
        """
        return self._VideoAuditStatus

    @VideoAuditStatus.setter
    def VideoAuditStatus(self, VideoAuditStatus):
        self._VideoAuditStatus = VideoAuditStatus

    @property
    def QuestionDesc(self):
        """Question description.
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc

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
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CateBizId = params.get("CateBizId")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._SegmentBizId = params.get("SegmentBizId")
        self._PageContent = params.get("PageContent")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        if params.get("SimilarQuestions") is not None:
            self._SimilarQuestions = []
            for item in params.get("SimilarQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._SimilarQuestions.append(obj)
        self._QaAuditStatus = params.get("QaAuditStatus")
        self._PicAuditStatus = params.get("PicAuditStatus")
        self._VideoAuditStatus = params.get("VideoAuditStatus")
        self._QuestionDesc = params.get("QuestionDesc")
        self._RequestId = params.get("RequestId")


class DescribeReferRequest(AbstractModel):
    """DescribeRefer request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _ReferBizIds: Quota ID
        :type ReferBizIds: list of str
        :param _LoginUin: Log in to the user's root account (required in the integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login user sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReferBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReferBizIds(self):
        """Quota ID
        :rtype: list of str
        """
        return self._ReferBizIds

    @ReferBizIds.setter
    def ReferBizIds(self, ReferBizIds):
        self._ReferBizIds = ReferBizIds

    @property
    def LoginUin(self):
        """Log in to the user's root account (required in the integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login user sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReferBizIds = params.get("ReferBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReferResponse(AbstractModel):
    """DescribeRefer response structure.

    """

    def __init__(self):
        r"""
        :param _List: Reference list.
        :type List: list of ReferDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Reference list.
        :rtype: list of ReferDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReferDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseInfoRequest(AbstractModel):
    """DescribeReleaseInfo request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseInfoResponse(AbstractModel):
    """DescribeReleaseInfo response structure.

    """

    def __init__(self):
        r"""
        :param _LastTime: The last release time.
        :type LastTime: str
        :param _Status: Release status: 1: pending release; 2: releasing; 3: release successful; 4: release failed; 5: under review; 6: review successful; 7: review failed; 8: release successful, callback processing; 9: release paused; 10: appeal under review; 11: appeal approved; 12: appeal rejected.
        :type Status: int
        :param _IsUpdated: Whether it has been edited. When it is true, it means it can be released.
        :type IsUpdated: bool
        :param _Msg: Reason for failure.

        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LastTime = None
        self._Status = None
        self._IsUpdated = None
        self._Msg = None
        self._RequestId = None

    @property
    def LastTime(self):
        """The last release time.
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def Status(self):
        """Release status: 1: pending release; 2: releasing; 3: release successful; 4: release failed; 5: under review; 6: review successful; 7: review failed; 8: release successful, callback processing; 9: release paused; 10: appeal under review; 11: appeal approved; 12: appeal rejected.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsUpdated(self):
        """Whether it has been edited. When it is true, it means it can be released.
        :rtype: bool
        """
        return self._IsUpdated

    @IsUpdated.setter
    def IsUpdated(self, IsUpdated):
        self._IsUpdated = IsUpdated

    @property
    def Msg(self):
        """Reason for failure.

        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._LastTime = params.get("LastTime")
        self._Status = params.get("Status")
        self._IsUpdated = params.get("IsUpdated")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeReleaseRequest(AbstractModel):
    """DescribeRelease request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _ReleaseBizId: Release details.
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        """Release details.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseResponse(AbstractModel):
    """DescribeRelease response structure.

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _Description: Publish description.
        :type Description: str
        :param _Status: Release status (1. pending release; 2. releasing; 3. release successful; 4. release failed; 5. releasing (under review); 6. releasing (review completed); 7. release failed; 9. release paused).
        :type Status: int
        :param _StatusDesc: Release status description.
        :type StatusDesc: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CreateTime = None
        self._Description = None
        self._Status = None
        self._StatusDesc = None
        self._RequestId = None

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        """Publish description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """Release status (1. pending release; 2. releasing; 3. release successful; 4. release failed; 5. releasing (under review); 6. releasing (review completed); 7. release failed; 9. release paused).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Release status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

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
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._RequestId = params.get("RequestId")


class DescribeRobotBizIDByAppKeyRequest(AbstractModel):
    """DescribeRobotBizIDByAppKey request structure.

    """

    def __init__(self):
        r"""
        :param _AppKey: Application appkey.
        :type AppKey: str
        """
        self._AppKey = None

    @property
    def AppKey(self):
        """Application appkey.
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey


    def _deserialize(self, params):
        self._AppKey = params.get("AppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRobotBizIDByAppKeyResponse(AbstractModel):
    """DescribeRobotBizIDByAppKey response structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application business ID.
        :type BotBizId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BotBizId = None
        self._RequestId = None

    @property
    def BotBizId(self):
        """Application business ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

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
        self._BotBizId = params.get("BotBizId")
        self._RequestId = params.get("RequestId")


class DescribeSearchStatsGraphRequest(AbstractModel):
    """DescribeSearchStatsGraph request structure.

    """

    def __init__(self):
        r"""
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _UinAccount: Uin list.
        :type UinAccount: list of str
        :param _SubBizType: Sub-business type.
        :type SubBizType: str
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds.
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds.
        :type EndTime: str
        :param _AppBizIds: Application id list.
        :type AppBizIds: list of str
        """
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._UinAccount = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def UinAccount(self):
        """Uin list.
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def SubBizType(self):
        """Sub-business type.
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        """Application id list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._UinAccount = params.get("UinAccount")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchStatsGraphResponse(AbstractModel):
    """DescribeSearchStatsGraph response structure.

    """

    def __init__(self):
        r"""
        :param _List: The statistical result.
        :type List: list of Stat
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """The statistical result.
        :rtype: list of Stat
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Stat()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSegmentsRequest(AbstractModel):
    """DescribeSegments request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _SegBizId: Document fragment ID.
        :type SegBizId: list of str
        """
        self._BotBizId = None
        self._SegBizId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def SegBizId(self):
        """Document fragment ID.
        :rtype: list of str
        """
        return self._SegBizId

    @SegBizId.setter
    def SegBizId(self, SegBizId):
        self._SegBizId = SegBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._SegBizId = params.get("SegBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSegmentsResponse(AbstractModel):
    """DescribeSegments response structure.

    """

    def __init__(self):
        r"""
        :param _List: Fragment list.
        :type List: list of DocSegment
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Fragment list.
        :rtype: list of DocSegment
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DocSegment()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStorageCredentialRequest(AbstractModel):
    """DescribeStorageCredential request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID. The parameter still needs to be filled in. Different combinations of parameters will result in different permissions. For details, see https://cloud.tencent.com/document/product/1759/116238.
        :type BotBizId: str
        :param _FileType: File type, normal file name type suffixes, such as xlsx, pdf, docx, png, etc.
        :type FileType: str
        :param _IsPublic: This parameter is used to select a scenario when uploading a file or an image. When uploading an image in a chat, "Ispublic" is "true." When uploading a file (including files in the document library, images, etc. and files in a chat), "Ispublic" is "false."

        :type IsPublic: bool
        :param _TypeKey: Storage type: offline - offline file; realtime - real-time file. If empty, it defaults to offline.
        :type TypeKey: str
        """
        self._BotBizId = None
        self._FileType = None
        self._IsPublic = None
        self._TypeKey = None

    @property
    def BotBizId(self):
        """Application ID. The parameter still needs to be filled in. Different combinations of parameters will result in different permissions. For details, see https://cloud.tencent.com/document/product/1759/116238.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileType(self):
        """File type, normal file name type suffixes, such as xlsx, pdf, docx, png, etc.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IsPublic(self):
        """This parameter is used to select a scenario when uploading a file or an image. When uploading an image in a chat, "Ispublic" is "true." When uploading a file (including files in the document library, images, etc. and files in a chat), "Ispublic" is "false."

        :rtype: bool
        """
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TypeKey(self):
        """Storage type: offline - offline file; realtime - real-time file. If empty, it defaults to offline.
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileType = params.get("FileType")
        self._IsPublic = params.get("IsPublic")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageCredentialResponse(AbstractModel):
    """DescribeStorageCredential response structure.

    """

    def __init__(self):
        r"""
        :param _Credentials: Key information.
        :type Credentials: :class:`tencentcloud.lke.v20231130.models.Credentials`
        :param _ExpiredTime: Expiration time.
        :type ExpiredTime: int
        :param _StartTime: Start time.
        :type StartTime: int
        :param _Bucket: Cloud object storage bucket.
        :type Bucket: str
        :param _Region: COS availability zone.
        :type Region: str
        :param _FilePath: Cloud file storage directory.
        :type FilePath: str
        :param _Type: Storage type.
        :type Type: str
        :param _CorpUin: Primary account.
        :type CorpUin: str
        :param _ImagePath: Image storage directory.
        :type ImagePath: str
        :param _UploadPath: Upload storage path to a specific file.
        :type UploadPath: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._StartTime = None
        self._Bucket = None
        self._Region = None
        self._FilePath = None
        self._Type = None
        self._CorpUin = None
        self._ImagePath = None
        self._UploadPath = None
        self._RequestId = None

    @property
    def Credentials(self):
        """Key information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        """Expiration time.
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def StartTime(self):
        """Start time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Bucket(self):
        """Cloud object storage bucket.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """COS availability zone.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FilePath(self):
        """Cloud file storage directory.
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        """Storage type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CorpUin(self):
        """Primary account.
        :rtype: str
        """
        return self._CorpUin

    @CorpUin.setter
    def CorpUin(self, CorpUin):
        self._CorpUin = CorpUin

    @property
    def ImagePath(self):
        """Image storage directory.
        :rtype: str
        """
        return self._ImagePath

    @ImagePath.setter
    def ImagePath(self, ImagePath):
        self._ImagePath = ImagePath

    @property
    def UploadPath(self):
        """Upload storage path to a specific file.
        :rtype: str
        """
        return self._UploadPath

    @UploadPath.setter
    def UploadPath(self, UploadPath):
        self._UploadPath = UploadPath

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
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._StartTime = params.get("StartTime")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._FilePath = params.get("FilePath")
        self._Type = params.get("Type")
        self._CorpUin = params.get("CorpUin")
        self._ImagePath = params.get("ImagePath")
        self._UploadPath = params.get("UploadPath")
        self._RequestId = params.get("RequestId")


class DescribeTokenUsageGraphRequest(AbstractModel):
    """DescribeTokenUsageGraph request structure.

    """

    def __init__(self):
        r"""
        :param _UinAccount: Root account of Tencent Cloud.
        :type UinAccount: list of str
        :param _SubBizType: Sub-business types of Tencent Cloud Agent Development Platform/TCADP: fileparse (document parsing), Embedding, Rewrite (multi-round rewriting), Concurrency, KnowledgeSummary (knowledge summary), KnowledgeQA (knowledge Q&A), KnowledgeCapacity (knowledge base capacity), SearchEngine (search engine).
        :type SubBizType: str
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds.
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds.
        :type EndTime: str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        """
        self._UinAccount = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None

    @property
    def UinAccount(self):
        """Root account of Tencent Cloud.
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def SubBizType(self):
        """Sub-business types of Tencent Cloud Agent Development Platform/TCADP: fileparse (document parsing), Embedding, Rewrite (multi-round rewriting), Concurrency, KnowledgeSummary (knowledge summary), KnowledgeQA (knowledge Q&A), KnowledgeCapacity (knowledge base capacity), SearchEngine (search engine).
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenUsageGraphResponse(AbstractModel):
    """DescribeTokenUsageGraph response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total amount of token consumption.
        :type Total: list of Stat
        :param _Input: Input token consumption.
        :type Input: list of Stat
        :param _Output: Output token consumption.
        :type Output: list of Stat
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Input = None
        self._Output = None
        self._RequestId = None

    @property
    def Total(self):
        """Total amount of token consumption.
        :rtype: list of Stat
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Input(self):
        """Input token consumption.
        :rtype: list of Stat
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        """Output token consumption.
        :rtype: list of Stat
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

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
        if params.get("Total") is not None:
            self._Total = []
            for item in params.get("Total"):
                obj = Stat()
                obj._deserialize(item)
                self._Total.append(obj)
        if params.get("Input") is not None:
            self._Input = []
            for item in params.get("Input"):
                obj = Stat()
                obj._deserialize(item)
                self._Input.append(obj)
        if params.get("Output") is not None:
            self._Output = []
            for item in params.get("Output"):
                obj = Stat()
                obj._deserialize(item)
                self._Output.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTokenUsageRequest(AbstractModel):
    """DescribeTokenUsage request structure.

    """

    def __init__(self):
        r"""
        :param _UinAccount: Root account of Tencent Cloud.
        :type UinAccount: list of str
        :param _LoginUin: Log in to user's root account (required in the integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _SubBizType: Sub-business types of Tencent Cloud Agent Development Platform/TCADP: FileParse (document parsing), embedding, Rewrite (multi-round rewriting), Concurrency, KnowledgeSummary (knowledge summary), KnowledgeQA (knowledge Q&A), KnowledgeCapacity (knowledge base capacity), SearchEngine (search engine).
        :type SubBizType: str
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start timestamp, in seconds (default value: 0).
        :type StartTime: str
        :param _EndTime: End timestamp, in seconds (default value: 0, must be greater than the start timestamp).
        :type EndTime: str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        :param _SubScenes: Filter sub-scenario (used in document parsing scenario).
        :type SubScenes: list of str
        """
        self._UinAccount = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._SubBizType = None
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._AppBizIds = None
        self._SubScenes = None

    @property
    def UinAccount(self):
        """Root account of Tencent Cloud.
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def LoginUin(self):
        """Log in to user's root account (required in the integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def SubBizType(self):
        """Sub-business types of Tencent Cloud Agent Development Platform/TCADP: FileParse (document parsing), embedding, Rewrite (multi-round rewriting), Concurrency, KnowledgeSummary (knowledge summary), KnowledgeQA (knowledge Q&A), KnowledgeCapacity (knowledge base capacity), SearchEngine (search engine).
        :rtype: str
        """
        return self._SubBizType

    @SubBizType.setter
    def SubBizType(self, SubBizType):
        self._SubBizType = SubBizType

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start timestamp, in seconds (default value: 0).
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End timestamp, in seconds (default value: 0, must be greater than the start timestamp).
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def SubScenes(self):
        """Filter sub-scenario (used in document parsing scenario).
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes


    def _deserialize(self, params):
        self._UinAccount = params.get("UinAccount")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._SubBizType = params.get("SubBizType")
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizIds = params.get("AppBizIds")
        self._SubScenes = params.get("SubScenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenUsageResponse(AbstractModel):
    """DescribeTokenUsage response structure.

    """

    def __init__(self):
        r"""
        :param _TotalTokenUsage: Total token consumption.
        :type TotalTokenUsage: float
        :param _InputTokenUsage: Input token consumption.
        :type InputTokenUsage: float
        :param _OutputTokenUsage: Output token consumption.
        :type OutputTokenUsage: float
        :param _ApiCallStats: Number of API calls.
        :type ApiCallStats: int
        :param _SearchUsage: Number of search service calls.
        :type SearchUsage: float
        :param _PageUsage: Number of pages consumed by document parsing.
        :type PageUsage: int
        :param _SplitTokenUsage: Token consumption by splitting.
        :type SplitTokenUsage: float
        :param _RagSearchUsage: Number of Rag retrievals.
        :type RagSearchUsage: float
        :param _InternetSearchUsage: Number of online searches.
        :type InternetSearchUsage: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalTokenUsage = None
        self._InputTokenUsage = None
        self._OutputTokenUsage = None
        self._ApiCallStats = None
        self._SearchUsage = None
        self._PageUsage = None
        self._SplitTokenUsage = None
        self._RagSearchUsage = None
        self._InternetSearchUsage = None
        self._RequestId = None

    @property
    def TotalTokenUsage(self):
        """Total token consumption.
        :rtype: float
        """
        return self._TotalTokenUsage

    @TotalTokenUsage.setter
    def TotalTokenUsage(self, TotalTokenUsage):
        self._TotalTokenUsage = TotalTokenUsage

    @property
    def InputTokenUsage(self):
        """Input token consumption.
        :rtype: float
        """
        return self._InputTokenUsage

    @InputTokenUsage.setter
    def InputTokenUsage(self, InputTokenUsage):
        self._InputTokenUsage = InputTokenUsage

    @property
    def OutputTokenUsage(self):
        """Output token consumption.
        :rtype: float
        """
        return self._OutputTokenUsage

    @OutputTokenUsage.setter
    def OutputTokenUsage(self, OutputTokenUsage):
        self._OutputTokenUsage = OutputTokenUsage

    @property
    def ApiCallStats(self):
        """Number of API calls.
        :rtype: int
        """
        return self._ApiCallStats

    @ApiCallStats.setter
    def ApiCallStats(self, ApiCallStats):
        self._ApiCallStats = ApiCallStats

    @property
    def SearchUsage(self):
        """Number of search service calls.
        :rtype: float
        """
        return self._SearchUsage

    @SearchUsage.setter
    def SearchUsage(self, SearchUsage):
        self._SearchUsage = SearchUsage

    @property
    def PageUsage(self):
        """Number of pages consumed by document parsing.
        :rtype: int
        """
        return self._PageUsage

    @PageUsage.setter
    def PageUsage(self, PageUsage):
        self._PageUsage = PageUsage

    @property
    def SplitTokenUsage(self):
        """Token consumption by splitting.
        :rtype: float
        """
        return self._SplitTokenUsage

    @SplitTokenUsage.setter
    def SplitTokenUsage(self, SplitTokenUsage):
        self._SplitTokenUsage = SplitTokenUsage

    @property
    def RagSearchUsage(self):
        """Number of Rag retrievals.
        :rtype: float
        """
        return self._RagSearchUsage

    @RagSearchUsage.setter
    def RagSearchUsage(self, RagSearchUsage):
        self._RagSearchUsage = RagSearchUsage

    @property
    def InternetSearchUsage(self):
        """Number of online searches.
        :rtype: float
        """
        return self._InternetSearchUsage

    @InternetSearchUsage.setter
    def InternetSearchUsage(self, InternetSearchUsage):
        self._InternetSearchUsage = InternetSearchUsage

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
        self._TotalTokenUsage = params.get("TotalTokenUsage")
        self._InputTokenUsage = params.get("InputTokenUsage")
        self._OutputTokenUsage = params.get("OutputTokenUsage")
        self._ApiCallStats = params.get("ApiCallStats")
        self._SearchUsage = params.get("SearchUsage")
        self._PageUsage = params.get("PageUsage")
        self._SplitTokenUsage = params.get("SplitTokenUsage")
        self._RagSearchUsage = params.get("RagSearchUsage")
        self._InternetSearchUsage = params.get("InternetSearchUsage")
        self._RequestId = params.get("RequestId")


class DescribeUnsatisfiedReplyContextRequest(AbstractModel):
    """DescribeUnsatisfiedReplyContext request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _ReplyBizId: Response ID.
        :type ReplyBizId: str
        :param _LoginUin: Log in to user's root account (required in the integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizId(self):
        """Response ID.
        :rtype: str
        """
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def LoginUin(self):
        """Log in to user's root account (required in the integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizId = params.get("ReplyBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnsatisfiedReplyContextResponse(AbstractModel):
    """DescribeUnsatisfiedReplyContext response structure.

    """

    def __init__(self):
        r"""
        :param _List: Context of dissatisfied responses.
        :type List: list of Context
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Context of dissatisfied responses.
        :rtype: list of Context
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Context()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DigitalHumanConfig(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _AssetKey: 
        :type AssetKey: str
        :param _Name: 
        :type Name: str
        :param _Avatar: 
        :type Avatar: str
        """
        self._AssetKey = None
        self._Name = None
        self._Avatar = None

    @property
    def AssetKey(self):
        """
        :rtype: str
        """
        return self._AssetKey

    @AssetKey.setter
    def AssetKey(self, AssetKey):
        self._AssetKey = AssetKey

    @property
    def Name(self):
        """
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        """
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._AssetKey = params.get("AssetKey")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocFilterFlag(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Flag: 
        :type Flag: str
        :param _Value: 
        :type Value: bool
        """
        self._Flag = None
        self._Value = None

    @property
    def Flag(self):
        """
        :rtype: str
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Value(self):
        """
        :rtype: bool
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Flag = params.get("Flag")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocSegment(AbstractModel):
    """Document fragment.

    """

    def __init__(self):
        r"""
        :param _Id: Fragment ID.
        :type Id: str
        :param _BusinessId: Business ID.
        :type BusinessId: str
        :param _FileType: File type (markdown, word, txt).
        :type FileType: str
        :param _SegmentType: Document segment type (segment, table).
        :type SegmentType: str
        :param _Title: Title.
        :type Title: str
        :param _PageContent: Paragraph content.
        :type PageContent: str
        :param _OrgData: Original paragraph.
        :type OrgData: str
        :param _DocId: Article ID.
        :type DocId: str
        :param _DocBizId: Document business ID.
        :type DocBizId: str
        :param _DocUrl: Document URL.
        :type DocUrl: str
        """
        self._Id = None
        self._BusinessId = None
        self._FileType = None
        self._SegmentType = None
        self._Title = None
        self._PageContent = None
        self._OrgData = None
        self._DocId = None
        self._DocBizId = None
        self._DocUrl = None

    @property
    def Id(self):
        """Fragment ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BusinessId(self):
        """Business ID.
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileType(self):
        """File type (markdown, word, txt).
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SegmentType(self):
        """Document segment type (segment, table).
        :rtype: str
        """
        return self._SegmentType

    @SegmentType.setter
    def SegmentType(self, SegmentType):
        self._SegmentType = SegmentType

    @property
    def Title(self):
        """Title.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def PageContent(self):
        """Paragraph content.
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def OrgData(self):
        """Original paragraph.
        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def DocId(self):
        """Article ID.
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def DocBizId(self):
        """Document business ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def DocUrl(self):
        """Document URL.
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BusinessId = params.get("BusinessId")
        self._FileType = params.get("FileType")
        self._SegmentType = params.get("SegmentType")
        self._Title = params.get("Title")
        self._PageContent = params.get("PageContent")
        self._OrgData = params.get("OrgData")
        self._DocId = params.get("DocId")
        self._DocBizId = params.get("DocBizId")
        self._DocUrl = params.get("DocUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelRequest(AbstractModel):
    """ExportAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _AttributeBizIds: Attribute ID.
        :type AttributeBizIds: list of str
        :param _Filters: Export according to the filtered data.
        :type Filters: :class:`tencentcloud.lke.v20231130.models.AttributeFilters`
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttributeBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttributeBizIds(self):
        """Attribute ID.
        :rtype: list of str
        """
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def Filters(self):
        """Export according to the filtered data.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AttributeFilters`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._AttributeBizIds = params.get("AttributeBizIds")
        if params.get("Filters") is not None:
            self._Filters = AttributeFilters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelResponse(AbstractModel):
    """ExportAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Export task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Export task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportQAListRequest(AbstractModel):
    """ExportQAList request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _QaBizIds: Q&A business ID.
        :type QaBizIds: list of str
        :param _Filters: Query parameter.
        :type Filters: :class:`tencentcloud.lke.v20231130.models.QAQuery`
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        """Q&A business ID.
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def Filters(self):
        """Query parameter.
        :rtype: :class:`tencentcloud.lke.v20231130.models.QAQuery`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        if params.get("Filters") is not None:
            self._Filters = QAQuery()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportQAListResponse(AbstractModel):
    """ExportQAList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ExportUnsatisfiedReplyRequest(AbstractModel):
    """ExportUnsatisfiedReply request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _ReplyBizIds: Check to export ID list.
        :type ReplyBizIds: list of str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _Filters: Retrieve filter.
        :type Filters: :class:`tencentcloud.lke.v20231130.models.Filters`
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Filters = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        """Check to export ID list.
        :rtype: list of str
        """
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Filters(self):
        """Retrieve filter.
        :rtype: :class:`tencentcloud.lke.v20231130.models.Filters`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("Filters") is not None:
            self._Filters = Filters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportUnsatisfiedReplyResponse(AbstractModel):
    """ExportUnsatisfiedReply response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ExtraInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _EChartsInfo: 
        :type EChartsInfo: list of str
        """
        self._EChartsInfo = None

    @property
    def EChartsInfo(self):
        """
        :rtype: list of str
        """
        return self._EChartsInfo

    @EChartsInfo.setter
    def EChartsInfo(self, EChartsInfo):
        self._EChartsInfo = EChartsInfo


    def _deserialize(self, params):
        self._EChartsInfo = params.get("EChartsInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """Real-Time uploaded file information.

    """

    def __init__(self):
        r"""
        :param _FileName: File name.
        :type FileName: str
        :param _FileSize: File size.
        :type FileSize: str
        :param _FileUrl: URL of the file, address of COS.
        :type FileUrl: str
        :param _FileType: File type.
        :type FileType: str
        :param _DocId: DocID returned after parsing.
        :type DocId: str
        :param _CreatedAt: Creation time.
        :type CreatedAt: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None
        self._CreatedAt = None

    @property
    def FileName(self):
        """File name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """File size.
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        """URL of the file, address of COS.
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        """DocID returned after parsing.
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def CreatedAt(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """Retrieve and filter dissatisfied responses.

    """

    def __init__(self):
        r"""
        :param _Query: Retrieve user question or answer.
        :type Query: str
        :param _Reasons: Incorrect retrieval type.

        :type Reasons: list of str
        """
        self._Query = None
        self._Reasons = None

    @property
    def Query(self):
        """Retrieve user question or answer.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        """Incorrect retrieval type.

        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQARequest(AbstractModel):
    """GenerateQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _DocBizIds: Document ID.
        :type DocBizIds: list of str
        """
        self._BotBizId = None
        self._DocBizIds = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        """Document ID.
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQAResponse(AbstractModel):
    """GenerateQA response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class GetAnswerTypeDataCountRequest(AbstractModel):
    """GetAnswerTypeDataCount request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start date.
        :type StartTime: int
        :param _EndTime: End date.
        :type EndTime: int
        :param _AppBizId: Application ID.
        :type AppBizId: list of str
        :param _Type: Message source (1. shared from user end; 2. chat API; 3. chat test, 4. application evaluation).
        :type Type: int
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        """Start date.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End date.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: list of str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        """Message source (1. shared from user end; 2. chat API; 3. chat test, 4. application evaluation).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAnswerTypeDataCountResponse(AbstractModel):
    """GetAnswerTypeDataCount response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of messages.
        :type Total: int
        :param _ModelReplyCount: Total number of direct responses by the large model.
        :type ModelReplyCount: int
        :param _KnowledgeCount: Total number of knowledge-based responses.
        :type KnowledgeCount: int
        :param _TaskFlowCount: Total number of task flow responses.
        :type TaskFlowCount: int
        :param _SearchEngineCount: Total number of search engine responses.
        :type SearchEngineCount: int
        :param _ImageUnderstandingCount: Total number of image understanding responses.
        :type ImageUnderstandingCount: int
        :param _RejectCount: Total number of responses to rejected questions.
        :type RejectCount: int
        :param _SensitiveCount: Total number of sensitive responses.
        :type SensitiveCount: int
        :param _ConcurrentLimitCount: Total number of responses for concurrency exceeded.
        :type ConcurrentLimitCount: int
        :param _UnknownIssuesCount: Total number of unknown question responses.
        :type UnknownIssuesCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ModelReplyCount = None
        self._KnowledgeCount = None
        self._TaskFlowCount = None
        self._SearchEngineCount = None
        self._ImageUnderstandingCount = None
        self._RejectCount = None
        self._SensitiveCount = None
        self._ConcurrentLimitCount = None
        self._UnknownIssuesCount = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of messages.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ModelReplyCount(self):
        """Total number of direct responses by the large model.
        :rtype: int
        """
        return self._ModelReplyCount

    @ModelReplyCount.setter
    def ModelReplyCount(self, ModelReplyCount):
        self._ModelReplyCount = ModelReplyCount

    @property
    def KnowledgeCount(self):
        """Total number of knowledge-based responses.
        :rtype: int
        """
        return self._KnowledgeCount

    @KnowledgeCount.setter
    def KnowledgeCount(self, KnowledgeCount):
        self._KnowledgeCount = KnowledgeCount

    @property
    def TaskFlowCount(self):
        """Total number of task flow responses.
        :rtype: int
        """
        return self._TaskFlowCount

    @TaskFlowCount.setter
    def TaskFlowCount(self, TaskFlowCount):
        self._TaskFlowCount = TaskFlowCount

    @property
    def SearchEngineCount(self):
        """Total number of search engine responses.
        :rtype: int
        """
        return self._SearchEngineCount

    @SearchEngineCount.setter
    def SearchEngineCount(self, SearchEngineCount):
        self._SearchEngineCount = SearchEngineCount

    @property
    def ImageUnderstandingCount(self):
        """Total number of image understanding responses.
        :rtype: int
        """
        return self._ImageUnderstandingCount

    @ImageUnderstandingCount.setter
    def ImageUnderstandingCount(self, ImageUnderstandingCount):
        self._ImageUnderstandingCount = ImageUnderstandingCount

    @property
    def RejectCount(self):
        """Total number of responses to rejected questions.
        :rtype: int
        """
        return self._RejectCount

    @RejectCount.setter
    def RejectCount(self, RejectCount):
        self._RejectCount = RejectCount

    @property
    def SensitiveCount(self):
        """Total number of sensitive responses.
        :rtype: int
        """
        return self._SensitiveCount

    @SensitiveCount.setter
    def SensitiveCount(self, SensitiveCount):
        self._SensitiveCount = SensitiveCount

    @property
    def ConcurrentLimitCount(self):
        """Total number of responses for concurrency exceeded.
        :rtype: int
        """
        return self._ConcurrentLimitCount

    @ConcurrentLimitCount.setter
    def ConcurrentLimitCount(self, ConcurrentLimitCount):
        self._ConcurrentLimitCount = ConcurrentLimitCount

    @property
    def UnknownIssuesCount(self):
        """Total number of unknown question responses.
        :rtype: int
        """
        return self._UnknownIssuesCount

    @UnknownIssuesCount.setter
    def UnknownIssuesCount(self, UnknownIssuesCount):
        self._UnknownIssuesCount = UnknownIssuesCount

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
        self._Total = params.get("Total")
        self._ModelReplyCount = params.get("ModelReplyCount")
        self._KnowledgeCount = params.get("KnowledgeCount")
        self._TaskFlowCount = params.get("TaskFlowCount")
        self._SearchEngineCount = params.get("SearchEngineCount")
        self._ImageUnderstandingCount = params.get("ImageUnderstandingCount")
        self._RejectCount = params.get("RejectCount")
        self._SensitiveCount = params.get("SensitiveCount")
        self._ConcurrentLimitCount = params.get("ConcurrentLimitCount")
        self._UnknownIssuesCount = params.get("UnknownIssuesCount")
        self._RequestId = params.get("RequestId")


class GetAppKnowledgeCountRequest(AbstractModel):
    """GetAppKnowledgeCount request structure.

    """

    def __init__(self):
        r"""
        :param _Type: Type: doc - document; qa - Q&A pair.
        :type Type: str
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _LoginUin: Login to user's root account (required in integrator mode).	
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._Type = None
        self._AppBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def Type(self):
        """Type: doc - document; qa - Q&A pair.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppBizId = params.get("AppBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppKnowledgeCountResponse(AbstractModel):
    """GetAppKnowledgeCount response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetAppSecretRequest(AbstractModel):
    """GetAppSecret request structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application ID.
        :type AppBizId: str
        """
        self._AppBizId = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppSecretResponse(AbstractModel):
    """GetAppSecret response structure.

    """

    def __init__(self):
        r"""
        :param _AppKey: Application key.
        :type AppKey: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _IsRelease: Whether to release.
        :type IsRelease: bool
        :param _HasPermission: Whether there is permission to view.
        :type HasPermission: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppKey = None
        self._CreateTime = None
        self._IsRelease = None
        self._HasPermission = None
        self._RequestId = None

    @property
    def AppKey(self):
        """Application key.
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsRelease(self):
        """Whether to release.
        :rtype: bool
        """
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease

    @property
    def HasPermission(self):
        """Whether there is permission to view.
        :rtype: bool
        """
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

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
        self._AppKey = params.get("AppKey")
        self._CreateTime = params.get("CreateTime")
        self._IsRelease = params.get("IsRelease")
        self._HasPermission = params.get("HasPermission")
        self._RequestId = params.get("RequestId")


class GetDocPreviewRequest(AbstractModel):
    """GetDocPreview request structure.

    """

    def __init__(self):
        r"""
        :param _DocBizId: Document BizID.
        :type DocBizId: str
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _TypeKey: Storage type: offline - offline file; realtime - real-time file. If empty, it defaults to offline.
        :type TypeKey: str
        """
        self._DocBizId = None
        self._BotBizId = None
        self._TypeKey = None

    @property
    def DocBizId(self):
        """Document BizID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def TypeKey(self):
        """Storage type: offline - offline file; realtime - real-time file. If empty, it defaults to offline.
        :rtype: str
        """
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._BotBizId = params.get("BotBizId")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocPreviewResponse(AbstractModel):
    """GetDocPreview response structure.

    """

    def __init__(self):
        r"""
        :param _FileName: Filename. The release end always uses this name.
        :type FileName: str
        :param _FileType: File type.
        :type FileType: str
        :param _CosUrl: COS path.

        :type CosUrl: str
        :param _Url: COS temporary url.

        :type Url: str
        :param _Bucket: COS bucket.

        :type Bucket: str
        :param _NewName: It is the new name in the case of document renaming. It shall be used preferentially on the evaluation end.
        :type NewName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._Url = None
        self._Bucket = None
        self._NewName = None
        self._RequestId = None

    @property
    def FileName(self):
        """Filename. The release end always uses this name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        """COS path.

        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def Url(self):
        """COS temporary url.

        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Bucket(self):
        """COS bucket.

        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def NewName(self):
        """It is the new name in the case of document renaming. It shall be used preferentially on the evaluation end.
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

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
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._Url = params.get("Url")
        self._Bucket = params.get("Bucket")
        self._NewName = params.get("NewName")
        self._RequestId = params.get("RequestId")


class GetLikeDataCountRequest(AbstractModel):
    """GetLikeDataCount request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start date.
        :type StartTime: int
        :param _EndTime: End date.
        :type EndTime: int
        :param _AppBizId: Application ID.
        :type AppBizId: list of str
        :param _Type: Message source (1. shared from user end, 2. chat api).
        :type Type: int
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        """Start date.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End date.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: list of str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        """Message source (1. shared from user end, 2. chat api).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLikeDataCountResponse(AbstractModel):
    """GetLikeDataCount response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of messages that can be evaluated.
        :type Total: int
        :param _AppraisalTotal: Number of comments.
        :type AppraisalTotal: int
        :param _ParticipationRate: Participation rate.
        :type ParticipationRate: float
        :param _LikeTotal: Number of likes.
        :type LikeTotal: int
        :param _LikeRate: Like rate.
        :type LikeRate: float
        :param _DislikeTotal: Number of dislikes.
        :type DislikeTotal: int
        :param _DislikeRate: Dislike rate.
        :type DislikeRate: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._AppraisalTotal = None
        self._ParticipationRate = None
        self._LikeTotal = None
        self._LikeRate = None
        self._DislikeTotal = None
        self._DislikeRate = None
        self._RequestId = None

    @property
    def Total(self):
        """Number of messages that can be evaluated.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AppraisalTotal(self):
        """Number of comments.
        :rtype: int
        """
        return self._AppraisalTotal

    @AppraisalTotal.setter
    def AppraisalTotal(self, AppraisalTotal):
        self._AppraisalTotal = AppraisalTotal

    @property
    def ParticipationRate(self):
        """Participation rate.
        :rtype: float
        """
        return self._ParticipationRate

    @ParticipationRate.setter
    def ParticipationRate(self, ParticipationRate):
        self._ParticipationRate = ParticipationRate

    @property
    def LikeTotal(self):
        """Number of likes.
        :rtype: int
        """
        return self._LikeTotal

    @LikeTotal.setter
    def LikeTotal(self, LikeTotal):
        self._LikeTotal = LikeTotal

    @property
    def LikeRate(self):
        """Like rate.
        :rtype: float
        """
        return self._LikeRate

    @LikeRate.setter
    def LikeRate(self, LikeRate):
        self._LikeRate = LikeRate

    @property
    def DislikeTotal(self):
        """Number of dislikes.
        :rtype: int
        """
        return self._DislikeTotal

    @DislikeTotal.setter
    def DislikeTotal(self, DislikeTotal):
        self._DislikeTotal = DislikeTotal

    @property
    def DislikeRate(self):
        """Dislike rate.
        :rtype: float
        """
        return self._DislikeRate

    @DislikeRate.setter
    def DislikeRate(self, DislikeRate):
        self._DislikeRate = DislikeRate

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
        self._Total = params.get("Total")
        self._AppraisalTotal = params.get("AppraisalTotal")
        self._ParticipationRate = params.get("ParticipationRate")
        self._LikeTotal = params.get("LikeTotal")
        self._LikeRate = params.get("LikeRate")
        self._DislikeTotal = params.get("DislikeTotal")
        self._DislikeRate = params.get("DislikeRate")
        self._RequestId = params.get("RequestId")


class GetMsgRecordRequest(AbstractModel):
    """GetMsgRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Type: Type.
        :type Type: int
        :param _Count: Quantity.
        :type Count: int
        :param _SessionId: Session ID.
        :type SessionId: str
        :param _BotAppKey: Application AppKey. When Type=5 [API Visitor], this field is required. </br> How to obtain it: </br> 1. After the application is released, obtain it at [Application Page]-[Release Management]-[Call Information]-[API Management]. </br> 2. Refer to item 2 in https://cloud.tencent.com/document/product/1759/109469.
        :type BotAppKey: str
        :param _Scene: Scenario, experience: 1; formal: 2.
        :type Scene: int
        :param _LastRecordId: Last record ID. Retrieve messages in reverse order. You can only select either MidRecordId or LastRecordId.
        :type LastRecordId: str
        :param _MidRecordId: If this value is input, it means pulling a total of count message records before and after the record ID. You can only select either MidRecordId or LastRecordId.
        :type MidRecordId: str
        """
        self._Type = None
        self._Count = None
        self._SessionId = None
        self._BotAppKey = None
        self._Scene = None
        self._LastRecordId = None
        self._MidRecordId = None

    @property
    def Type(self):
        """Type.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        """Quantity.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SessionId(self):
        """Session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def BotAppKey(self):
        """Application AppKey. When Type=5 [API Visitor], this field is required. </br> How to obtain it: </br> 1. After the application is released, obtain it at [Application Page]-[Release Management]-[Call Information]-[API Management]. </br> 2. Refer to item 2 in https://cloud.tencent.com/document/product/1759/109469.
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def Scene(self):
        """Scenario, experience: 1; formal: 2.
        :rtype: int
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LastRecordId(self):
        """Last record ID. Retrieve messages in reverse order. You can only select either MidRecordId or LastRecordId.
        :rtype: str
        """
        return self._LastRecordId

    @LastRecordId.setter
    def LastRecordId(self, LastRecordId):
        self._LastRecordId = LastRecordId

    @property
    def MidRecordId(self):
        """If this value is input, it means pulling a total of count message records before and after the record ID. You can only select either MidRecordId or LastRecordId.
        :rtype: str
        """
        return self._MidRecordId

    @MidRecordId.setter
    def MidRecordId(self, MidRecordId):
        self._MidRecordId = MidRecordId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._SessionId = params.get("SessionId")
        self._BotAppKey = params.get("BotAppKey")
        self._Scene = params.get("Scene")
        self._LastRecordId = params.get("LastRecordId")
        self._MidRecordId = params.get("MidRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMsgRecordResponse(AbstractModel):
    """GetMsgRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Records: Session record.
        :type Records: list of MsgRecord
        :param _SessionDisassociatedTimestamp: The time when session cleared associated context, in milliseconds.
        :type SessionDisassociatedTimestamp: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Records = None
        self._SessionDisassociatedTimestamp = None
        self._RequestId = None

    @property
    def Records(self):
        """Session record.
        :rtype: list of MsgRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def SessionDisassociatedTimestamp(self):
        """The time when session cleared associated context, in milliseconds.
        :rtype: str
        """
        return self._SessionDisassociatedTimestamp

    @SessionDisassociatedTimestamp.setter
    def SessionDisassociatedTimestamp(self, SessionDisassociatedTimestamp):
        self._SessionDisassociatedTimestamp = SessionDisassociatedTimestamp

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = MsgRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._SessionDisassociatedTimestamp = params.get("SessionDisassociatedTimestamp")
        self._RequestId = params.get("RequestId")


class GetReconstructDocumentResultRequest(AbstractModel):
    """GetReconstructDocumentResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the task. It is the TaskId returned by [CreateReconstructDocumentFlow](https://cloud.tencent.com/document/product/1759/107506).
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Unique ID of the task. It is the TaskId returned by [CreateReconstructDocumentFlow](https://cloud.tencent.com/document/product/1759/107506).
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
        


class GetReconstructDocumentResultResponse(AbstractModel):
    """GetReconstructDocumentResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status: success - execution completed; processing - executing; failed - execution failed; waitexecute - waiting to execute.
        :type Status: str
        :param _DocumentRecognizeResultUrl: The result file of this document parsing task, stored in the download url of Tencent Cloud cos. The valid period of the download url is 10 minutes.
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: Page number information where document parsing failed this time.
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status: success - execution completed; processing - executing; failed - execution failed; waitexecute - waiting to execute.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        """The result file of this document parsing task, stored in the download url of Tencent Cloud cos. The valid period of the download url is 10 minutes.
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        """Page number information where document parsing failed this time.
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

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
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._RequestId = params.get("RequestId")


class GetTaskStatusRequest(AbstractModel):
    """GetTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _TaskType: Task type.
        :type TaskType: str
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._BotBizId = None

    @property
    def TaskId(self):
        """Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        """Task type.
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStatusResponse(AbstractModel):
    """GetTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _TaskType: Task type.
        :type TaskType: str
        :param _Status: Task status.
        :type Status: str
        :param _Message: Task messages.
        :type Message: str
        :param _Params: Task parameters.
        :type Params: :class:`tencentcloud.lke.v20231130.models.TaskParams`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._Status = None
        self._Message = None
        self._Params = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        """Task type.
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        """Task status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """Task messages.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Params(self):
        """Task parameters.
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskParams`
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

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
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        if params.get("Params") is not None:
            self._Params = TaskParams()
            self._Params._deserialize(params.get("Params"))
        self._RequestId = params.get("RequestId")


class GetWsTokenReq_Label(AbstractModel):
    """Obtain ws token label.

    """

    def __init__(self):
        r"""
        :param _Name: Label name.
        :type Name: str
        :param _Values: Label value.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Label name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Label value.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWsTokenRequest(AbstractModel):
    """GetWsToken request structure.

    """

    def __init__(self):
        r"""
        :param _Type: Access type, 5 - API visitor .
        :type Type: int
        :param _BotAppKey: Application AppKey</br>
How to Obtain It:</br>
1. After the application is released, obtain it at [Release Management] - [Call Information] - [API Management] on the application page.</br>
2. See the second item in https://cloud.tencent.com/document/product/1759/109469.
        :type BotAppKey: str
        :param _VisitorBizId: Visitor ID (external input, recommended to be unique, identifies the user currently accessing the session). Length Limit: string(64).
        :type VisitorBizId: str
        :param _VisitorLabels: Knowledge label, used for search filter in the knowledge base. This field is about to be deactivated. Please use the custom_variables field in the dialogue endpoint API to replace this field.
        :type VisitorLabels: list of GetWsTokenReq_Label
        """
        self._Type = None
        self._BotAppKey = None
        self._VisitorBizId = None
        self._VisitorLabels = None

    @property
    def Type(self):
        """Access type, 5 - API visitor .
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BotAppKey(self):
        """Application AppKey</br>
How to Obtain It:</br>
1. After the application is released, obtain it at [Release Management] - [Call Information] - [API Management] on the application page.</br>
2. See the second item in https://cloud.tencent.com/document/product/1759/109469.
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def VisitorBizId(self):
        """Visitor ID (external input, recommended to be unique, identifies the user currently accessing the session). Length Limit: string(64).
        :rtype: str
        """
        return self._VisitorBizId

    @VisitorBizId.setter
    def VisitorBizId(self, VisitorBizId):
        self._VisitorBizId = VisitorBizId

    @property
    def VisitorLabels(self):
        """Knowledge label, used for search filter in the knowledge base. This field is about to be deactivated. Please use the custom_variables field in the dialogue endpoint API to replace this field.
        :rtype: list of GetWsTokenReq_Label
        """
        return self._VisitorLabels

    @VisitorLabels.setter
    def VisitorLabels(self, VisitorLabels):
        self._VisitorLabels = VisitorLabels


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._BotAppKey = params.get("BotAppKey")
        self._VisitorBizId = params.get("VisitorBizId")
        if params.get("VisitorLabels") is not None:
            self._VisitorLabels = []
            for item in params.get("VisitorLabels"):
                obj = GetWsTokenReq_Label()
                obj._deserialize(item)
                self._VisitorLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWsTokenResponse(AbstractModel):
    """GetWsToken response structure.

    """

    def __init__(self):
        r"""
        :param _Token: Token value (valid for 60 seconds, valid only once, multiple validations will report an error).
        :type Token: str
        :param _Balance: Balance. The balance is valid if it is greater than 0.
        :type Balance: float
        :param _InputLenLimit: The character limit for input in the chat window.
        :type InputLenLimit: int
        :param _Pattern: Application mode: standard; agent; single_workflow.
        :type Pattern: str
        :param _SingleWorkflow: SingleWorkflow.
        :type SingleWorkflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Token = None
        self._Balance = None
        self._InputLenLimit = None
        self._Pattern = None
        self._SingleWorkflow = None
        self._RequestId = None

    @property
    def Token(self):
        """Token value (valid for 60 seconds, valid only once, multiple validations will report an error).
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Balance(self):
        """Balance. The balance is valid if it is greater than 0.
        :rtype: float
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def InputLenLimit(self):
        """The character limit for input in the chat window.
        :rtype: int
        """
        return self._InputLenLimit

    @InputLenLimit.setter
    def InputLenLimit(self, InputLenLimit):
        self._InputLenLimit = InputLenLimit

    @property
    def Pattern(self):
        """Application mode: standard; agent; single_workflow.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def SingleWorkflow(self):
        """SingleWorkflow.
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        """
        return self._SingleWorkflow

    @SingleWorkflow.setter
    def SingleWorkflow(self, SingleWorkflow):
        self._SingleWorkflow = SingleWorkflow

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
        self._Token = params.get("Token")
        self._Balance = params.get("Balance")
        self._InputLenLimit = params.get("InputLenLimit")
        self._Pattern = params.get("Pattern")
        if params.get("SingleWorkflow") is not None:
            self._SingleWorkflow = KnowledgeQaSingleWorkflow()
            self._SingleWorkflow._deserialize(params.get("SingleWorkflow"))
        self._RequestId = params.get("RequestId")


class GroupDocRequest(AbstractModel):
    """GroupDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _BizIds: List of business IDs of operation objects.
        :type BizIds: list of str
        :param _CateBizId: Group ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._BizIds = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def BizIds(self):
        """List of business IDs of operation objects.
        :rtype: list of str
        """
        return self._BizIds

    @BizIds.setter
    def BizIds(self, BizIds):
        self._BizIds = BizIds

    @property
    def CateBizId(self):
        """Group ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._BizIds = params.get("BizIds")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupDocResponse(AbstractModel):
    """GroupDoc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class GroupQARequest(AbstractModel):
    """GroupQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _QaBizIds: List of QaBizIDs.
        :type QaBizIds: list of str
        :param _CateBizId: Group ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        """List of QaBizIDs.
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def CateBizId(self):
        """Group ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupQAResponse(AbstractModel):
    """GroupQA response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Highlight(AbstractModel):
    """Fragment highlight content.

    """

    def __init__(self):
        r"""
        :param _StartPos: Highlight starting position.
        :type StartPos: str
        :param _EndPos: Highlight end position.
        :type EndPos: str
        :param _Text: Highlight subtext.
        :type Text: str
        """
        self._StartPos = None
        self._EndPos = None
        self._Text = None

    @property
    def StartPos(self):
        """Highlight starting position.
        :rtype: str
        """
        return self._StartPos

    @StartPos.setter
    def StartPos(self, StartPos):
        self._StartPos = StartPos

    @property
    def EndPos(self):
        """Highlight end position.
        :rtype: str
        """
        return self._EndPos

    @EndPos.setter
    def EndPos(self, EndPos):
        self._EndPos = EndPos

    @property
    def Text(self):
        """Highlight subtext.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._StartPos = params.get("StartPos")
        self._EndPos = params.get("EndPos")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistorySummary(AbstractModel):
    """Multiple rounds of historical information.

    """

    def __init__(self):
        r"""
        :param _Assistant: Assistant.
        :type Assistant: str
        :param _User: User.
        :type User: str
        """
        self._Assistant = None
        self._User = None

    @property
    def Assistant(self):
        """Assistant.
        :rtype: str
        """
        return self._Assistant

    @Assistant.setter
    def Assistant(self, Assistant):
        self._Assistant = Assistant

    @property
    def User(self):
        """User.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._Assistant = params.get("Assistant")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyRequest(AbstractModel):
    """IgnoreUnsatisfiedReply request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _ReplyBizIds: Dissatisfied response ID.
        :type ReplyBizIds: list of str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        """Dissatisfied response ID.
        :rtype: list of str
        """
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyResponse(AbstractModel):
    """IgnoreUnsatisfiedReply response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class IntentAchievement(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Name: 
        :type Name: str
        :param _Desc: 
        :type Desc: str
        """
        self._Name = None
        self._Desc = None

    @property
    def Name(self):
        """
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeAPI(AbstractModel):
    """Information of the requested API.

    """

    def __init__(self):
        r"""
        :param _Method: Request method, such as get/post.
        :type Method: str
        :param _Url: Request address.
        :type Url: str
        :param _HeaderValues: Header parameter.
        :type HeaderValues: list of StrValue
        :param _QueryValues: Input parameter Query.
        :type QueryValues: list of StrValue
        :param _RequestPostBody: Original data of a Post request.
        :type RequestPostBody: str
        :param _ResponseBody: Returned original data.
        :type ResponseBody: str
        :param _ResponseValues: Output parameter.
        :type ResponseValues: list of ValueInfo
        :param _FailMessage: Exception information.
        :type FailMessage: str
        """
        self._Method = None
        self._Url = None
        self._HeaderValues = None
        self._QueryValues = None
        self._RequestPostBody = None
        self._ResponseBody = None
        self._ResponseValues = None
        self._FailMessage = None

    @property
    def Method(self):
        """Request method, such as get/post.
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Url(self):
        """Request address.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def HeaderValues(self):
        """Header parameter.
        :rtype: list of StrValue
        """
        return self._HeaderValues

    @HeaderValues.setter
    def HeaderValues(self, HeaderValues):
        self._HeaderValues = HeaderValues

    @property
    def QueryValues(self):
        """Input parameter Query.
        :rtype: list of StrValue
        """
        return self._QueryValues

    @QueryValues.setter
    def QueryValues(self, QueryValues):
        self._QueryValues = QueryValues

    @property
    def RequestPostBody(self):
        """Original data of a Post request.
        :rtype: str
        """
        return self._RequestPostBody

    @RequestPostBody.setter
    def RequestPostBody(self, RequestPostBody):
        self._RequestPostBody = RequestPostBody

    @property
    def ResponseBody(self):
        """Returned original data.
        :rtype: str
        """
        return self._ResponseBody

    @ResponseBody.setter
    def ResponseBody(self, ResponseBody):
        self._ResponseBody = ResponseBody

    @property
    def ResponseValues(self):
        """Output parameter.
        :rtype: list of ValueInfo
        """
        return self._ResponseValues

    @ResponseValues.setter
    def ResponseValues(self, ResponseValues):
        self._ResponseValues = ResponseValues

    @property
    def FailMessage(self):
        """Exception information.
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Url = params.get("Url")
        if params.get("HeaderValues") is not None:
            self._HeaderValues = []
            for item in params.get("HeaderValues"):
                obj = StrValue()
                obj._deserialize(item)
                self._HeaderValues.append(obj)
        if params.get("QueryValues") is not None:
            self._QueryValues = []
            for item in params.get("QueryValues"):
                obj = StrValue()
                obj._deserialize(item)
                self._QueryValues.append(obj)
        self._RequestPostBody = params.get("RequestPostBody")
        self._ResponseBody = params.get("ResponseBody")
        if params.get("ResponseValues") is not None:
            self._ResponseValues = []
            for item in params.get("ResponseValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._ResponseValues.append(obj)
        self._FailMessage = params.get("FailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeCapacityPieGraphDetail(AbstractModel):
    """Detailed information of a knowledge library capacity pie chart.

    """

    def __init__(self):
        r"""
        :param _AppName: Current application name.
        :type AppName: str
        :param _UsedCharSize: Number of characters used by the current application.
        :type UsedCharSize: str
        :param _Proportion: Proportion of the current application in total usage.
        :type Proportion: float
        """
        self._AppName = None
        self._UsedCharSize = None
        self._Proportion = None

    @property
    def AppName(self):
        """Current application name.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UsedCharSize(self):
        """Number of characters used by the current application.
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

    @property
    def Proportion(self):
        """Proportion of the current application in total usage.
        :rtype: float
        """
        return self._Proportion

    @Proportion.setter
    def Proportion(self, Proportion):
        self._Proportion = Proportion


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UsedCharSize = params.get("UsedCharSize")
        self._Proportion = params.get("Proportion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeDetail(AbstractModel):
    """Application usage details of knowledge library capacity.

    """

    def __init__(self):
        r"""
        :param _AppName: Application name.
        :type AppName: str
        :param _UsedCharSize: Number of used characters.
        :type UsedCharSize: str
        :param _Proportion: Usage proportion.
        :type Proportion: float
        :param _ExceedCharSize: Exceeding character count.
        :type ExceedCharSize: str
        """
        self._AppName = None
        self._UsedCharSize = None
        self._Proportion = None
        self._ExceedCharSize = None

    @property
    def AppName(self):
        """Application name.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UsedCharSize(self):
        """Number of used characters.
        :rtype: str
        """
        return self._UsedCharSize

    @UsedCharSize.setter
    def UsedCharSize(self, UsedCharSize):
        self._UsedCharSize = UsedCharSize

    @property
    def Proportion(self):
        """Usage proportion.
        :rtype: float
        """
        return self._Proportion

    @Proportion.setter
    def Proportion(self, Proportion):
        self._Proportion = Proportion

    @property
    def ExceedCharSize(self):
        """Exceeding character count.
        :rtype: str
        """
        return self._ExceedCharSize

    @ExceedCharSize.setter
    def ExceedCharSize(self, ExceedCharSize):
        self._ExceedCharSize = ExceedCharSize


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UsedCharSize = params.get("UsedCharSize")
        self._Proportion = params.get("Proportion")
        self._ExceedCharSize = params.get("ExceedCharSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaConfig(AbstractModel):
    """Knowledge Q&A configuration.

    """

    def __init__(self):
        r"""
        :param _Greeting: Welcome words, within 200 characters.
        :type Greeting: str
        :param _RoleDescription: Character description, within 4,000 characters. By filling out the description, set the #Character Name, #Style Characteristics, and reachable #Intent of the application. It is recommended to fill in according to the following template, with custom intents no more than 5. 
#Character Name:
#Style Characteristics:
#Output Requirements:
#Ability Limitations:
The following user intents can be reached.
##Intent Name:
##Intent Description:
##Intent Example:
##Intent Implementation:
        :type RoleDescription: str
        :param _Model: Generative model configuration.
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Search: Knowledge search configuration.
        :type Search: list of KnowledgeQaSearch
        :param _Output: Knowledge management output configuration.
        :type Output: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaOutput`
        :param _Workflow: Workflow configuration.
        :type Workflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeWorkflow`
        :param _SearchRange: Retrieval range.
        :type SearchRange: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        :param _Pattern: Application modes: standard, agent, single_workflow.
        :type Pattern: str
        :param _SearchStrategy: Retrieve a policy.
        :type SearchStrategy: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        :param _SingleWorkflow: Single workflow ID, which is entered when Pattern is single_workflow.
        :type SingleWorkflow: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        :param _Plugins: Application associated plug-in.
        :type Plugins: list of KnowledgeQaPlugin
        :param _ThoughtModel: Thinking model configuration.
        :type ThoughtModel: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _IntentAchievements: Priority of intent achievement methods.
        :type IntentAchievements: list of IntentAchievement
        :param _ImageTextRetrieval: Whether to enable Image-Text Search.
        :type ImageTextRetrieval: bool
        :param _AiCall: Configure voice call parameters.
        :type AiCall: :class:`tencentcloud.lke.v20231130.models.AICallConfig`
        :param _EnableAudit: Session content moderation switch. Note: 1. This feature is enabled by default if no value is input. 2. Tencent Cloud provides a content pre-filtering feature to help filter high-risk or illegal content. If you do not use our filtering feature, you can disable it here. We hereby remind you that you are responsible for ensuring that your content complies with platform policies and laws and regulations, and that you should fulfill your content moderation obligations.
        :type EnableAudit: bool
        """
        self._Greeting = None
        self._RoleDescription = None
        self._Model = None
        self._Search = None
        self._Output = None
        self._Workflow = None
        self._SearchRange = None
        self._Pattern = None
        self._SearchStrategy = None
        self._SingleWorkflow = None
        self._Plugins = None
        self._ThoughtModel = None
        self._IntentAchievements = None
        self._ImageTextRetrieval = None
        self._AiCall = None
        self._EnableAudit = None

    @property
    def Greeting(self):
        """Welcome words, within 200 characters.
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def RoleDescription(self):
        """Character description, within 4,000 characters. By filling out the description, set the #Character Name, #Style Characteristics, and reachable #Intent of the application. It is recommended to fill in according to the following template, with custom intents no more than 5. 
#Character Name:
#Style Characteristics:
#Output Requirements:
#Ability Limitations:
The following user intents can be reached.
##Intent Name:
##Intent Description:
##Intent Example:
##Intent Implementation:
        :rtype: str
        """
        return self._RoleDescription

    @RoleDescription.setter
    def RoleDescription(self, RoleDescription):
        self._RoleDescription = RoleDescription

    @property
    def Model(self):
        """Generative model configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Search(self):
        """Knowledge search configuration.
        :rtype: list of KnowledgeQaSearch
        """
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def Output(self):
        """Knowledge management output configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Workflow(self):
        """Workflow configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeWorkflow`
        """
        return self._Workflow

    @Workflow.setter
    def Workflow(self, Workflow):
        self._Workflow = Workflow

    @property
    def SearchRange(self):
        """Retrieval range.
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchRange`
        """
        return self._SearchRange

    @SearchRange.setter
    def SearchRange(self, SearchRange):
        self._SearchRange = SearchRange

    @property
    def Pattern(self):
        """Application modes: standard, agent, single_workflow.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def SearchStrategy(self):
        """Retrieve a policy.
        :rtype: :class:`tencentcloud.lke.v20231130.models.SearchStrategy`
        """
        return self._SearchStrategy

    @SearchStrategy.setter
    def SearchStrategy(self, SearchStrategy):
        self._SearchStrategy = SearchStrategy

    @property
    def SingleWorkflow(self):
        """Single workflow ID, which is entered when Pattern is single_workflow.
        :rtype: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaSingleWorkflow`
        """
        return self._SingleWorkflow

    @SingleWorkflow.setter
    def SingleWorkflow(self, SingleWorkflow):
        self._SingleWorkflow = SingleWorkflow

    @property
    def Plugins(self):
        """Application associated plug-in.
        :rtype: list of KnowledgeQaPlugin
        """
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def ThoughtModel(self):
        """Thinking model configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._ThoughtModel

    @ThoughtModel.setter
    def ThoughtModel(self, ThoughtModel):
        self._ThoughtModel = ThoughtModel

    @property
    def IntentAchievements(self):
        """Priority of intent achievement methods.
        :rtype: list of IntentAchievement
        """
        return self._IntentAchievements

    @IntentAchievements.setter
    def IntentAchievements(self, IntentAchievements):
        self._IntentAchievements = IntentAchievements

    @property
    def ImageTextRetrieval(self):
        """Whether to enable Image-Text Search.
        :rtype: bool
        """
        return self._ImageTextRetrieval

    @ImageTextRetrieval.setter
    def ImageTextRetrieval(self, ImageTextRetrieval):
        self._ImageTextRetrieval = ImageTextRetrieval

    @property
    def AiCall(self):
        """Configure voice call parameters.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AICallConfig`
        """
        return self._AiCall

    @AiCall.setter
    def AiCall(self, AiCall):
        self._AiCall = AiCall

    @property
    def EnableAudit(self):
        """Session content moderation switch. Note: 1. This feature is enabled by default if no value is input. 2. Tencent Cloud provides a content pre-filtering feature to help filter high-risk or illegal content. If you do not use our filtering feature, you can disable it here. We hereby remind you that you are responsible for ensuring that your content complies with platform policies and laws and regulations, and that you should fulfill your content moderation obligations.
        :rtype: bool
        """
        return self._EnableAudit

    @EnableAudit.setter
    def EnableAudit(self, EnableAudit):
        self._EnableAudit = EnableAudit


    def _deserialize(self, params):
        self._Greeting = params.get("Greeting")
        self._RoleDescription = params.get("RoleDescription")
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = KnowledgeQaSearch()
                obj._deserialize(item)
                self._Search.append(obj)
        if params.get("Output") is not None:
            self._Output = KnowledgeQaOutput()
            self._Output._deserialize(params.get("Output"))
        if params.get("Workflow") is not None:
            self._Workflow = KnowledgeWorkflow()
            self._Workflow._deserialize(params.get("Workflow"))
        if params.get("SearchRange") is not None:
            self._SearchRange = SearchRange()
            self._SearchRange._deserialize(params.get("SearchRange"))
        self._Pattern = params.get("Pattern")
        if params.get("SearchStrategy") is not None:
            self._SearchStrategy = SearchStrategy()
            self._SearchStrategy._deserialize(params.get("SearchStrategy"))
        if params.get("SingleWorkflow") is not None:
            self._SingleWorkflow = KnowledgeQaSingleWorkflow()
            self._SingleWorkflow._deserialize(params.get("SingleWorkflow"))
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = KnowledgeQaPlugin()
                obj._deserialize(item)
                self._Plugins.append(obj)
        if params.get("ThoughtModel") is not None:
            self._ThoughtModel = AppModel()
            self._ThoughtModel._deserialize(params.get("ThoughtModel"))
        if params.get("IntentAchievements") is not None:
            self._IntentAchievements = []
            for item in params.get("IntentAchievements"):
                obj = IntentAchievement()
                obj._deserialize(item)
                self._IntentAchievements.append(obj)
        self._ImageTextRetrieval = params.get("ImageTextRetrieval")
        if params.get("AiCall") is not None:
            self._AiCall = AICallConfig()
            self._AiCall._deserialize(params.get("AiCall"))
        self._EnableAudit = params.get("EnableAudit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaOutput(AbstractModel):
    """Application management output configuration.

    """

    def __init__(self):
        r"""
        :param _Method: Output method, 1: streaming 2: non-streaming.
        :type Method: int
        :param _UseGeneralKnowledge: General model response.
        :type UseGeneralKnowledge: bool
        :param _BareAnswer: Unknown response, within 300 characters.
        :type BareAnswer: str
        :param _ShowQuestionClarify: Whether to display the question clarification switch.
        :type ShowQuestionClarify: bool
        :param _UseQuestionClarify: Whether to enable question clarification.
        :type UseQuestionClarify: bool
        :param _QuestionClarifyKeywords: List of keywords for question clarification.
        :type QuestionClarifyKeywords: list of str
        :param _UseRecommended: Whether to enable recommended questions.
        :type UseRecommended: bool
        """
        self._Method = None
        self._UseGeneralKnowledge = None
        self._BareAnswer = None
        self._ShowQuestionClarify = None
        self._UseQuestionClarify = None
        self._QuestionClarifyKeywords = None
        self._UseRecommended = None

    @property
    def Method(self):
        """Output method, 1: streaming 2: non-streaming.
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UseGeneralKnowledge(self):
        """General model response.
        :rtype: bool
        """
        return self._UseGeneralKnowledge

    @UseGeneralKnowledge.setter
    def UseGeneralKnowledge(self, UseGeneralKnowledge):
        self._UseGeneralKnowledge = UseGeneralKnowledge

    @property
    def BareAnswer(self):
        """Unknown response, within 300 characters.
        :rtype: str
        """
        return self._BareAnswer

    @BareAnswer.setter
    def BareAnswer(self, BareAnswer):
        self._BareAnswer = BareAnswer

    @property
    def ShowQuestionClarify(self):
        """Whether to display the question clarification switch.
        :rtype: bool
        """
        return self._ShowQuestionClarify

    @ShowQuestionClarify.setter
    def ShowQuestionClarify(self, ShowQuestionClarify):
        self._ShowQuestionClarify = ShowQuestionClarify

    @property
    def UseQuestionClarify(self):
        """Whether to enable question clarification.
        :rtype: bool
        """
        return self._UseQuestionClarify

    @UseQuestionClarify.setter
    def UseQuestionClarify(self, UseQuestionClarify):
        self._UseQuestionClarify = UseQuestionClarify

    @property
    def QuestionClarifyKeywords(self):
        """List of keywords for question clarification.
        :rtype: list of str
        """
        return self._QuestionClarifyKeywords

    @QuestionClarifyKeywords.setter
    def QuestionClarifyKeywords(self, QuestionClarifyKeywords):
        self._QuestionClarifyKeywords = QuestionClarifyKeywords

    @property
    def UseRecommended(self):
        """Whether to enable recommended questions.
        :rtype: bool
        """
        return self._UseRecommended

    @UseRecommended.setter
    def UseRecommended(self, UseRecommended):
        self._UseRecommended = UseRecommended


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._UseGeneralKnowledge = params.get("UseGeneralKnowledge")
        self._BareAnswer = params.get("BareAnswer")
        self._ShowQuestionClarify = params.get("ShowQuestionClarify")
        self._UseQuestionClarify = params.get("UseQuestionClarify")
        self._QuestionClarifyKeywords = params.get("QuestionClarifyKeywords")
        self._UseRecommended = params.get("UseRecommended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaPlugin(AbstractModel):
    """Information of application-associated plug-in.

    """

    def __init__(self):
        r"""
        :param _PluginId: Plugin ID.
        :type PluginId: str
        :param _PluginName: Plugin name.
        :type PluginName: str
        :param _PluginIcon: Plugin icon.
        :type PluginIcon: str
        :param _ToolId: Tool ID.
        :type ToolId: str
        :param _ToolName: Tool name.
        :type ToolName: str
        :param _ToolDesc: Tool description.
        :type ToolDesc: str
        :param _Inputs: Tool input parameter.
        :type Inputs: list of PluginToolReqParam
        :param _IsBindingKnowledge: Whether the plugin is bound to the knowledge library.
        :type IsBindingKnowledge: bool
        """
        self._PluginId = None
        self._PluginName = None
        self._PluginIcon = None
        self._ToolId = None
        self._ToolName = None
        self._ToolDesc = None
        self._Inputs = None
        self._IsBindingKnowledge = None

    @property
    def PluginId(self):
        """Plugin ID.
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        """Plugin name.
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginIcon(self):
        """Plugin icon.
        :rtype: str
        """
        return self._PluginIcon

    @PluginIcon.setter
    def PluginIcon(self, PluginIcon):
        self._PluginIcon = PluginIcon

    @property
    def ToolId(self):
        """Tool ID.
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        """Tool name.
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolDesc(self):
        """Tool description.
        :rtype: str
        """
        return self._ToolDesc

    @ToolDesc.setter
    def ToolDesc(self, ToolDesc):
        self._ToolDesc = ToolDesc

    @property
    def Inputs(self):
        """Tool input parameter.
        :rtype: list of PluginToolReqParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def IsBindingKnowledge(self):
        """Whether the plugin is bound to the knowledge library.
        :rtype: bool
        """
        return self._IsBindingKnowledge

    @IsBindingKnowledge.setter
    def IsBindingKnowledge(self, IsBindingKnowledge):
        self._IsBindingKnowledge = IsBindingKnowledge


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._PluginIcon = params.get("PluginIcon")
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ToolDesc = params.get("ToolDesc")
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        self._IsBindingKnowledge = params.get("IsBindingKnowledge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaSearch(AbstractModel):
    """Retrieval configuration.

    """

    def __init__(self):
        r"""
        :param _Type: Knowledge source: doc (document), qa (question & answering), taskflow (business process), search (search enhancement).
        :type Type: str
        :param _ReplyFlexibility: Q&A - reply flexibility, 1: directly reply if the answer has been accepted. 2: reply after the accepted answer has been polished.
        :type ReplyFlexibility: int
        :param _UseSearchEngine: Search enhancement - search engine status.
        :type UseSearchEngine: bool
        :param _ShowSearchEngine: Whether to display the search engine retrieval status.
        :type ShowSearchEngine: bool
        :param _IsEnabled: Knowledge source, whether to select.
        :type IsEnabled: bool
        :param _QaTopN: Maximum number of Q&A recalls, defaults to 2, limited to 5.
        :type QaTopN: int
        :param _DocTopN: Maximum number of documents recalls, defaults to 3, limited to 5.
        :type DocTopN: int
        :param _Confidence: Retrieval confidence degree, valid for documents and Q&A. Value range: 0.01 - 0.99.
        :type Confidence: float
        :param _ResourceStatus: Resource status, 1: the resource is available; 2: the resource is exhausted.
        :type ResourceStatus: int
        """
        self._Type = None
        self._ReplyFlexibility = None
        self._UseSearchEngine = None
        self._ShowSearchEngine = None
        self._IsEnabled = None
        self._QaTopN = None
        self._DocTopN = None
        self._Confidence = None
        self._ResourceStatus = None

    @property
    def Type(self):
        """Knowledge source: doc (document), qa (question & answering), taskflow (business process), search (search enhancement).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ReplyFlexibility(self):
        """Q&A - reply flexibility, 1: directly reply if the answer has been accepted. 2: reply after the accepted answer has been polished.
        :rtype: int
        """
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def UseSearchEngine(self):
        """Search enhancement - search engine status.
        :rtype: bool
        """
        return self._UseSearchEngine

    @UseSearchEngine.setter
    def UseSearchEngine(self, UseSearchEngine):
        self._UseSearchEngine = UseSearchEngine

    @property
    def ShowSearchEngine(self):
        """Whether to display the search engine retrieval status.
        :rtype: bool
        """
        return self._ShowSearchEngine

    @ShowSearchEngine.setter
    def ShowSearchEngine(self, ShowSearchEngine):
        self._ShowSearchEngine = ShowSearchEngine

    @property
    def IsEnabled(self):
        """Knowledge source, whether to select.
        :rtype: bool
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def QaTopN(self):
        """Maximum number of Q&A recalls, defaults to 2, limited to 5.
        :rtype: int
        """
        return self._QaTopN

    @QaTopN.setter
    def QaTopN(self, QaTopN):
        self._QaTopN = QaTopN

    @property
    def DocTopN(self):
        """Maximum number of documents recalls, defaults to 3, limited to 5.
        :rtype: int
        """
        return self._DocTopN

    @DocTopN.setter
    def DocTopN(self, DocTopN):
        self._DocTopN = DocTopN

    @property
    def Confidence(self):
        """Retrieval confidence degree, valid for documents and Q&A. Value range: 0.01 - 0.99.
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ResourceStatus(self):
        """Resource status, 1: the resource is available; 2: the resource is exhausted.
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ReplyFlexibility = params.get("ReplyFlexibility")
        self._UseSearchEngine = params.get("UseSearchEngine")
        self._ShowSearchEngine = params.get("ShowSearchEngine")
        self._IsEnabled = params.get("IsEnabled")
        self._QaTopN = params.get("QaTopN")
        self._DocTopN = params.get("DocTopN")
        self._Confidence = params.get("Confidence")
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaSingleWorkflow(AbstractModel):
    """Specifies the single workflow configuration in Q&A knowledge library single workflow mode.

    """

    def __init__(self):
        r"""
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _WorkflowDesc: Workflow description.
        :type WorkflowDesc: str
        :param _Status: Workflow status, publishing status (UNPUBLISHED; PUBLISHING; PUBLISHED; FAIL).
        :type Status: str
        :param _IsEnable: Whether to enable workflow.
        :type IsEnable: bool
        :param _AsyncWorkflow: Whether to enable asynchronous call of the workflow.
        :type AsyncWorkflow: bool
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowDesc = None
        self._Status = None
        self._IsEnable = None
        self._AsyncWorkflow = None

    @property
    def WorkflowId(self):
        """Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        """Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowDesc(self):
        """Workflow description.
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def Status(self):
        """Workflow status, publishing status (UNPUBLISHED; PUBLISHING; PUBLISHED; FAIL).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsEnable(self):
        """Whether to enable workflow.
        :rtype: bool
        """
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable

    @property
    def AsyncWorkflow(self):
        """Whether to enable asynchronous call of the workflow.
        :rtype: bool
        """
        return self._AsyncWorkflow

    @AsyncWorkflow.setter
    def AsyncWorkflow(self, AsyncWorkflow):
        self._AsyncWorkflow = AsyncWorkflow


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._Status = params.get("Status")
        self._IsEnable = params.get("IsEnable")
        self._AsyncWorkflow = params.get("AsyncWorkflow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSummary(AbstractModel):
    """Retrieve knowledge.

    """

    def __init__(self):
        r"""
        :param _Type: 1: Q&A; 2: document fragment.
        :type Type: int
        :param _Content: Knowledge content.
        :type Content: str
        """
        self._Type = None
        self._Content = None

    @property
    def Type(self):
        """1: Q&A; 2: document fragment.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        """Knowledge content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeWorkflow(AbstractModel):
    """Q&A knowledge library workflow configuration.

    """

    def __init__(self):
        r"""
        :param _IsEnabled: Whether to enable the workflow.
        :type IsEnabled: bool
        :param _UsePdl: Whether to enable PDL.
        :type UsePdl: bool
        """
        self._IsEnabled = None
        self._UsePdl = None

    @property
    def IsEnabled(self):
        """Whether to enable the workflow.
        :rtype: bool
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def UsePdl(self):
        """Whether to enable PDL.
        :rtype: bool
        """
        return self._UsePdl

    @UsePdl.setter
    def UsePdl(self, UsePdl):
        self._UsePdl = UsePdl


    def _deserialize(self, params):
        self._IsEnabled = params.get("IsEnabled")
        self._UsePdl = params.get("UsePdl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """Label ID.

    """

    def __init__(self):
        r"""
        :param _LabelBizId: Label ID.
        :type LabelBizId: str
        :param _LabelName: Label name.
        :type LabelName: str
        """
        self._LabelBizId = None
        self._LabelName = None

    @property
    def LabelBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        """Label name.
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppCategoryRequest(AbstractModel):
    """ListAppCategory request structure.

    """


class ListAppCategoryResponse(AbstractModel):
    """ListAppCategory response structure.

    """

    def __init__(self):
        r"""
        :param _List: Application type list.
        :type List: list of ListAppCategoryRspOption
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Application type list.
        :rtype: list of ListAppCategoryRspOption
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListAppCategoryRspOption()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAppCategoryRspOption(AbstractModel):
    """Application type details.

    """

    def __init__(self):
        r"""
        :param _Text: Type name.
        :type Text: str
        :param _Value: Type value.
        :type Value: str
        :param _Logo: Type log.
        :type Logo: str
        """
        self._Text = None
        self._Value = None
        self._Logo = None

    @property
    def Text(self):
        """Type name.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        """Type value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Logo(self):
        """Type log.
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        self._Logo = params.get("Logo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppKnowledgeDetailRequest(AbstractModel):
    """ListAppKnowledgeDetail request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Page size.
        :type PageSize: int
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        """
        self._PageNumber = None
        self._PageSize = None
        self._AppBizIds = None

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Page size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._AppBizIds = params.get("AppBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppKnowledgeDetailResponse(AbstractModel):
    """ListAppKnowledgeDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of lists.
        :type Total: int
        :param _List: Details of knowledge base capacity usage by application.
        :type List: list of KnowledgeDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of lists.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """Details of knowledge base capacity usage by application.
        :rtype: list of KnowledgeDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = KnowledgeDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAppRequest(AbstractModel):
    """ListApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _PageSize: Number of items per page, integer.
        :type PageSize: int
        :param _PageNumber: Page number, integer.
        :type PageNumber: int
        :param _Keyword: Keywords: application / modifier.
        :type Keyword: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._AppType = None
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None
        self._LoginSubAccountUin = None

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def PageSize(self):
        """Number of items per page, integer.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number, integer.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        """Keywords: application / modifier.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppResponse(AbstractModel):
    """ListApp response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Quantity.
        :type Total: str
        :param _List: Label list.
        :type List: list of AppInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Quantity.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """Label list.
        :rtype: list of AppInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AppInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttributeLabelRequest(AbstractModel):
    """ListAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Quantity per page.
        :type PageSize: int
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _Query: Query content.
        :type Query: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Quantity per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttributeLabelResponse(AbstractModel):
    """ListAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: str
        :param _List: List.
        :type List: list of AttrLabelDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List.
        :rtype: list of AttrLabelDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttrLabelDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocCateRequest(AbstractModel):
    """ListDocCate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocCateResponse(AbstractModel):
    """ListDocCate response structure.

    """

    def __init__(self):
        r"""
        :param _List: List.
        :type List: list of CateInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """List.
        :rtype: list of CateInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CateInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocItem(AbstractModel):
    """Description of document list details.

    """

    def __init__(self):
        r"""
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _FileName: File name.
        :type FileName: str
        :param _NewName: The new document name after renaming. This name remains until the document is published after the renaming submission.
        :type NewName: str
        :param _FileType: File type.
        :type FileType: str
        :param _CosUrl: COS path.
        :type CosUrl: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Status: Document status.
        :type Status: int
        :param _StatusDesc: Document status description.
        :type StatusDesc: str
        :param _Reason: Reason.
        :type Reason: str
        :param _IsRefer: Whether to refer to an answer.
        :type IsRefer: bool
        :param _QaNum: Quantity of Q&A pairs.
        :type QaNum: int
        :param _IsDeleted: Whether it has been deleted.
        :type IsDeleted: bool
        :param _Source: Document source.
        :type Source: int
        :param _SourceDesc: Document source description.
        :type SourceDesc: str
        :param _IsAllowRestart: Whether regeneration is allowed.
        :type IsAllowRestart: bool
        :param _IsDeletedQa: Whether the Q&A has been deleted.
        :type IsDeletedQa: bool
        :param _IsCreatingQa: Whether the Q&A is being generated.
        :type IsCreatingQa: bool
        :param _IsAllowDelete: Whether deletion is allowed.
        :type IsAllowDelete: bool
        :param _IsAllowRefer: Whether to allow operation reference switch.
        :type IsAllowRefer: bool
        :param _IsCreatedQa: Whether Q&A has been generated.
        :type IsCreatedQa: bool
        :param _DocCharSize: Document character count.
        :type DocCharSize: str
        :param _AttrRange: Applicable range of attribute label.
        :type AttrRange: int
        :param _AttrLabels: Attribute label.
        :type AttrLabels: list of AttrLabel
        :param _IsAllowEdit: Whether editing is allowed.
        :type IsAllowEdit: bool
        :param _ReferUrlType: External reference URL type, 0: system URL; 1: custom URL.
When the value is 1, the WebUrl field cannot be empty; otherwise, it will not take effect.
        :type ReferUrlType: int
        :param _WebUrl: Web page URL (or custom URL) .
        :type WebUrl: str
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _IsAllowRetry: Whether retries are allowed, 0: no, 1: yes.
        :type IsAllowRetry: bool
        :param _Processing: 0: document comparison processing; 1: Q&A generation from document.
        :type Processing: list of int
        :param _CreateTime: Time when the document was created and stored into the database.
        :type CreateTime: str
        :param _CateBizId: ID of the document's category.
        :type CateBizId: str
        :param _CustomerKnowledgeId: User-defined ID of the document.
        :type CustomerKnowledgeId: str
        :param _AttributeFlags: Attribute label of the document. 0: Do not perform external user permission verification.
        :type AttributeFlags: list of int non-negative
        """
        self._DocBizId = None
        self._FileName = None
        self._NewName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._AttrRange = None
        self._AttrLabels = None
        self._IsAllowEdit = None
        self._ReferUrlType = None
        self._WebUrl = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._IsAllowRetry = None
        self._Processing = None
        self._CreateTime = None
        self._CateBizId = None
        self._CustomerKnowledgeId = None
        self._AttributeFlags = None

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        """File name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def NewName(self):
        """The new document name after renaming. This name remains until the document is published after the renaming submission.
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        """COS path.
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Document status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Document status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        """Reason.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        """Whether to refer to an answer.
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        """Quantity of Q&A pairs.
        :rtype: int
        """
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        """Whether it has been deleted.
        :rtype: bool
        """
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        """Document source.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        """Document source description.
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        """Whether regeneration is allowed.
        :rtype: bool
        """
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        """Whether the Q&A has been deleted.
        :rtype: bool
        """
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        """Whether the Q&A is being generated.
        :rtype: bool
        """
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        """Whether deletion is allowed.
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        """Whether to allow operation reference switch.
        :rtype: bool
        """
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        """Whether Q&A has been generated.
        :rtype: bool
        """
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        """Document character count.
        :rtype: str
        """
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def AttrRange(self):
        """Applicable range of attribute label.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Attribute label.
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def IsAllowEdit(self):
        """Whether editing is allowed.
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def ReferUrlType(self):
        """External reference URL type, 0: system URL; 1: custom URL.
When the value is 1, the WebUrl field cannot be empty; otherwise, it will not take effect.
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def WebUrl(self):
        """Web page URL (or custom URL) .
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def IsAllowRetry(self):
        """Whether retries are allowed, 0: no, 1: yes.
        :rtype: bool
        """
        return self._IsAllowRetry

    @IsAllowRetry.setter
    def IsAllowRetry(self, IsAllowRetry):
        self._IsAllowRetry = IsAllowRetry

    @property
    def Processing(self):
        """0: document comparison processing; 1: Q&A generation from document.
        :rtype: list of int
        """
        return self._Processing

    @Processing.setter
    def Processing(self, Processing):
        self._Processing = Processing

    @property
    def CreateTime(self):
        """Time when the document was created and stored into the database.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CateBizId(self):
        """ID of the document's category.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def CustomerKnowledgeId(self):
        """User-defined ID of the document.
        :rtype: str
        """
        return self._CustomerKnowledgeId

    @CustomerKnowledgeId.setter
    def CustomerKnowledgeId(self, CustomerKnowledgeId):
        self._CustomerKnowledgeId = CustomerKnowledgeId

    @property
    def AttributeFlags(self):
        """Attribute label of the document. 0: Do not perform external user permission verification.
        :rtype: list of int non-negative
        """
        return self._AttributeFlags

    @AttributeFlags.setter
    def AttributeFlags(self, AttributeFlags):
        self._AttributeFlags = AttributeFlags


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._NewName = params.get("NewName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._ReferUrlType = params.get("ReferUrlType")
        self._WebUrl = params.get("WebUrl")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._IsAllowRetry = params.get("IsAllowRetry")
        self._Processing = params.get("Processing")
        self._CreateTime = params.get("CreateTime")
        self._CateBizId = params.get("CateBizId")
        self._CustomerKnowledgeId = params.get("CustomerKnowledgeId")
        self._AttributeFlags = params.get("AttributeFlags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocRequest(AbstractModel):
    """ListDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Quantity per page.
        :type PageSize: int
        :param _Query: Query content.
        :type Query: str
        :param _Status: Document status : 1: not generated; 2: generating; 3: generation successful; 4: generation failed; 5: deleting; 6: deleted successfully; 7: under review; 8: review failed; 9: review successful; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 15: updating; 16: update failed; 17: parsing; 18: parsing failed; 19: import failed; 20: expired; 21: excessive invalid; 22: excessive invalid recovered.
        :type Status: list of int
        :param _QueryType: Query type: filename - document; attribute - label.
        :type QueryType: str
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _FileTypes: File type classification and filtering.
        :type FileTypes: list of str
        :param _FilterFlag: Document list filter flag
        :type FilterFlag: list of DocFilterFlag
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._Status = None
        self._QueryType = None
        self._CateBizId = None
        self._FileTypes = None
        self._FilterFlag = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Quantity per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Status(self):
        """Document status : 1: not generated; 2: generating; 3: generation successful; 4: generation failed; 5: deleting; 6: deleted successfully; 7: under review; 8: review failed; 9: review successful; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 15: updating; 16: update failed; 17: parsing; 18: parsing failed; 19: import failed; 20: expired; 21: excessive invalid; 22: excessive invalid recovered.
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def QueryType(self):
        """Query type: filename - document; attribute - label.
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def FileTypes(self):
        """File type classification and filtering.
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def FilterFlag(self):
        """Document list filter flag
        :rtype: list of DocFilterFlag
        """
        return self._FilterFlag

    @FilterFlag.setter
    def FilterFlag(self, FilterFlag):
        self._FilterFlag = FilterFlag


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._Status = params.get("Status")
        self._QueryType = params.get("QueryType")
        self._CateBizId = params.get("CateBizId")
        self._FileTypes = params.get("FileTypes")
        if params.get("FilterFlag") is not None:
            self._FilterFlag = []
            for item in params.get("FilterFlag"):
                obj = DocFilterFlag()
                obj._deserialize(item)
                self._FilterFlag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocResponse(AbstractModel):
    """ListDoc response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Quantity of documents.
        :type Total: str
        :param _List: List of documents.
        :type List: list of ListDocItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Quantity of documents.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List of documents.
        :rtype: list of ListDocItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListDocItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListModelRequest(AbstractModel):
    """ListModel request structure.

    """

    def __init__(self):
        r"""
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _Pattern: Application mode standard: standard; agent; single_workflow.
        :type Pattern: str
        :param _ModelCategory: Model category: 
Generate: Generative model
Thought: Thinking model
        :type ModelCategory: str
        :param _LoginUin: Login to user's root account (required in integrator mode).	
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._AppType = None
        self._Pattern = None
        self._ModelCategory = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def Pattern(self):
        """Application mode standard: standard; agent; single_workflow.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ModelCategory(self):
        """Model category: 
Generate: Generative model
Thought: Thinking model
        :rtype: str
        """
        return self._ModelCategory

    @ModelCategory.setter
    def ModelCategory(self, ModelCategory):
        self._ModelCategory = ModelCategory

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._Pattern = params.get("Pattern")
        self._ModelCategory = params.get("ModelCategory")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListModelResponse(AbstractModel):
    """ListModel response structure.

    """

    def __init__(self):
        r"""
        :param _List: Model list.
        :type List: list of ModelInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Model list.
        :rtype: list of ModelInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ModelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQACateRequest(AbstractModel):
    """ListQACate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQACateResponse(AbstractModel):
    """ListQACate response structure.

    """

    def __init__(self):
        r"""
        :param _List: List.
        :type List: list of QACate
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """List.
        :rtype: list of QACate
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QACate()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQARequest(AbstractModel):
    """ListQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Page size.
        :type PageSize: int
        :param _Query: Query a question.
        :type Query: str
        :param _AcceptStatus: Verification status (1: not verified 2: adopted 3: not adopted).
        :type AcceptStatus: list of int
        :param _ReleaseStatus: Release status (2: pending release; 3: releasing; 4: released; 7: under review; 8: review failed; 9: under manual appeal; 11: manual appeal failed; 12: expired; 13: excessive invalid; 14: excessive invalid recovered).
        :type ReleaseStatus: list of int
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _Source: Source (1: generated from document; 2: import in batches; 3: manually added).
        :type Source: int
        :param _QueryAnswer: Query an answer.
        :type QueryAnswer: str
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _QaBizIds: Q&A business ID list.
        :type QaBizIds: list of str
        :param _QueryType: Query type: filename; attribute label.
        :type QueryType: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._Source = None
        self._QueryAnswer = None
        self._CateBizId = None
        self._QaBizIds = None
        self._QueryType = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Page size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query a question.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def AcceptStatus(self):
        """Verification status (1: not verified 2: adopted 3: not adopted).
        :rtype: list of int
        """
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        """Release status (2: pending release; 3: releasing; 4: released; 7: under review; 8: review failed; 9: under manual appeal; 11: manual appeal failed; 12: expired; 13: excessive invalid; 14: excessive invalid recovered).
        :rtype: list of int
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def Source(self):
        """Source (1: generated from document; 2: import in batches; 3: manually added).
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        """Query an answer.
        :rtype: str
        """
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def QaBizIds(self):
        """Q&A business ID list.
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def QueryType(self):
        """Query type: filename; attribute label.
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        self._CateBizId = params.get("CateBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQAResponse(AbstractModel):
    """ListQA response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Q&A quantity.
        :type Total: str
        :param _WaitVerifyTotal: Quantity of pending verification Q&As.
        :type WaitVerifyTotal: str
        :param _NotAcceptedTotal: Quantity of not adopted Q&As.
        :type NotAcceptedTotal: str
        :param _AcceptedTotal: Quantity of adopted Q&As.
        :type AcceptedTotal: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _List: Q&As details.
        :type List: list of ListQaItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._WaitVerifyTotal = None
        self._NotAcceptedTotal = None
        self._AcceptedTotal = None
        self._PageNumber = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Q&A quantity.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def WaitVerifyTotal(self):
        """Quantity of pending verification Q&As.
        :rtype: str
        """
        return self._WaitVerifyTotal

    @WaitVerifyTotal.setter
    def WaitVerifyTotal(self, WaitVerifyTotal):
        self._WaitVerifyTotal = WaitVerifyTotal

    @property
    def NotAcceptedTotal(self):
        """Quantity of not adopted Q&As.
        :rtype: str
        """
        return self._NotAcceptedTotal

    @NotAcceptedTotal.setter
    def NotAcceptedTotal(self, NotAcceptedTotal):
        self._NotAcceptedTotal = NotAcceptedTotal

    @property
    def AcceptedTotal(self):
        """Quantity of adopted Q&As.
        :rtype: str
        """
        return self._AcceptedTotal

    @AcceptedTotal.setter
    def AcceptedTotal(self, AcceptedTotal):
        self._AcceptedTotal = AcceptedTotal

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def List(self):
        """Q&As details.
        :rtype: list of ListQaItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        self._WaitVerifyTotal = params.get("WaitVerifyTotal")
        self._NotAcceptedTotal = params.get("NotAcceptedTotal")
        self._AcceptedTotal = params.get("AcceptedTotal")
        self._PageNumber = params.get("PageNumber")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListQaItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQaItem(AbstractModel):
    """Q&A details data.

    """

    def __init__(self):
        r"""
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _Question: Question.
        :type Question: str
        :param _Answer: Answer.
        :type Answer: str
        :param _Source: Source.
        :type Source: int
        :param _SourceDesc: Source description.
        :type SourceDesc: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Status: Status.
        :type Status: int
        :param _StatusDesc: Status description.
        :type StatusDesc: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _IsAllowEdit: Whether editing is allowed.
        :type IsAllowEdit: bool
        :param _IsAllowDelete: Whether deletion is allowed.
        :type IsAllowDelete: bool
        :param _IsAllowAccept: Whether verification is allowed.
        :type IsAllowAccept: bool
        :param _FileName: Document name.
        :type FileName: str
        :param _FileType: Document type.
        :type FileType: str
        :param _QaCharSize: Number of Q&A characters.
        :type QaCharSize: str
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _AttrRange: Applicable range of attribute label, 1: all, 2: by conditions.
        :type AttrRange: int
        :param _AttrLabels: Attribute label.
        :type AttrLabels: list of AttrLabel
        :param _SimilarQuestionNum: Count of similar questions.
        :type SimilarQuestionNum: int
        :param _SimilarQuestionTips: Return similar questions associated with the Q&A and perform linked search. Only one similar question will be displayed.
        :type SimilarQuestionTips: str
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._DocBizId = None
        self._CreateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None
        self._IsAllowAccept = None
        self._FileName = None
        self._FileType = None
        self._QaCharSize = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._AttrRange = None
        self._AttrLabels = None
        self._SimilarQuestionNum = None
        self._SimilarQuestionTips = None

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Source(self):
        """Source.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        """Source description.
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsAllowEdit(self):
        """Whether editing is allowed.
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        """Whether deletion is allowed.
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowAccept(self):
        """Whether verification is allowed.
        :rtype: bool
        """
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def FileName(self):
        """Document name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """Document type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def QaCharSize(self):
        """Number of Q&A characters.
        :rtype: str
        """
        return self._QaCharSize

    @QaCharSize.setter
    def QaCharSize(self, QaCharSize):
        self._QaCharSize = QaCharSize

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def AttrRange(self):
        """Applicable range of attribute label, 1: all, 2: by conditions.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Attribute label.
        :rtype: list of AttrLabel
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def SimilarQuestionNum(self):
        """Count of similar questions.
        :rtype: int
        """
        return self._SimilarQuestionNum

    @SimilarQuestionNum.setter
    def SimilarQuestionNum(self, SimilarQuestionNum):
        self._SimilarQuestionNum = SimilarQuestionNum

    @property
    def SimilarQuestionTips(self):
        """Return similar questions associated with the Q&A and perform linked search. Only one similar question will be displayed.
        :rtype: str
        """
        return self._SimilarQuestionTips

    @SimilarQuestionTips.setter
    def SimilarQuestionTips(self, SimilarQuestionTips):
        self._SimilarQuestionTips = SimilarQuestionTips


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DocBizId = params.get("DocBizId")
        self._CreateTime = params.get("CreateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._QaCharSize = params.get("QaCharSize")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._SimilarQuestionNum = params.get("SimilarQuestionNum")
        self._SimilarQuestionTips = params.get("SimilarQuestionTips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionPreviewRequest(AbstractModel):
    """ListRejectedQuestionPreview request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _Query: Query content.
        :type Query: str
        :param _ReleaseBizId: Release ticket ID.
        :type ReleaseBizId: str
        :param _Actions: Status (1: newly-added; 2: updated; 3:  deleted).
        :type Actions: list of int non-negative
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        """Release ticket ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        """Status (1: newly-added; 2: updated; 3:  deleted).
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionPreviewResponse(AbstractModel):
    """ListRejectedQuestionPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Quantity of documents.
        :type Total: str
        :param _List: List of documents.
        :type List: list of ReleaseRejectedQuestion
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Quantity of documents.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List of documents.
        :rtype: list of ReleaseRejectedQuestion
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseRejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListRejectedQuestionRequest(AbstractModel):
    """ListRejectedQuestion request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.


        :type PageNumber: int
        :param _PageSize: Number of items per page.

        :type PageSize: int
        :param _Query: Query content.

        :type Query: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.


        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.

        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionResponse(AbstractModel):
    """ListRejectedQuestion response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: str
        :param _List: List of rejected questions.
        :type List: list of RejectedQuestion
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List of rejected questions.
        :rtype: list of RejectedQuestion
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseConfigPreviewRequest(AbstractModel):
    """ListReleaseConfigPreview request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Robot ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _Query: Query content.
        :type Query: str
        :param _ReleaseBizId: Release ticket ID.
        :type ReleaseBizId: str
        :param _Actions: Status (1: newly-added; 2: updated; 3: deleted).
        :type Actions: list of int non-negative
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _ReleaseStatus: Release status.
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        """Robot ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        """Release ticket ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        """Status (1: newly-added; 2: updated; 3: deleted).
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReleaseStatus(self):
        """Release status.
        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseConfigPreviewResponse(AbstractModel):
    """ListReleaseConfigPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Quantity.
        :type Total: str
        :param _List: Configuration item list.
        :type List: list of ReleaseConfigs
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Quantity.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """Configuration item list.
        :rtype: list of ReleaseConfigs
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseConfigs()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseDocPreviewRequest(AbstractModel):
    """ListReleaseDocPreview request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _Query: Query content.
        :type Query: str
        :param _ReleaseBizId: Release ticket ID.
        :type ReleaseBizId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Actions: Status (1: newly-added; 2: modified; 3: deleted).
        :type Actions: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        """Release ticket ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        """Status (1: newly-added; 2: modified; 3: deleted).
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseDocPreviewResponse(AbstractModel):
    """ListReleaseDocPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Document quantity.
        :type Total: str
        :param _List: Document list.
        :type List: list of ReleaseDoc
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Document quantity.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """Document list.
        :rtype: list of ReleaseDoc
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseDoc()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseItem(AbstractModel):
    """Details of release list.

    """

    def __init__(self):
        r"""
        :param _ReleaseBizId: Version ID.
        :type ReleaseBizId: str
        :param _Operator: Releaser.
        :type Operator: str
        :param _Desc: Release description.
        :type Desc: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Status: Release status.
        :type Status: int
        :param _StatusDesc: Release status description.
        :type StatusDesc: str
        :param _Reason: Reason for failure.
        :type Reason: str
        :param _SuccessCount: Number of successful releases.
        :type SuccessCount: int
        :param _FailCount: Number of failed releases.
        :type FailCount: int
        """
        self._ReleaseBizId = None
        self._Operator = None
        self._Desc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._SuccessCount = None
        self._FailCount = None

    @property
    def ReleaseBizId(self):
        """Version ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Operator(self):
        """Releaser.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Desc(self):
        """Release description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """Release status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Release status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        """Reason for failure.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def SuccessCount(self):
        """Number of successful releases.
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        """Number of failed releases.
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount


    def _deserialize(self, params):
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Operator = params.get("Operator")
        self._Desc = params.get("Desc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewRequest(AbstractModel):
    """ListReleaseQAPreview request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _Query: Query content.
        :type Query: str
        :param _ReleaseBizId: Release ticket ID.
        :type ReleaseBizId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Actions: Status (1: newly-added; 2: modified; 3: deleted).
        :type Actions: list of int non-negative
        :param _ReleaseStatus: Release status (4: release successful; 5: release failed).
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        """Release ticket ID.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        """Status (1: newly-added; 2: modified; 3: deleted).
        :rtype: list of int non-negative
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def ReleaseStatus(self):
        """Release status (4: release successful; 5: release failed).
        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewResponse(AbstractModel):
    """ListReleaseQAPreview response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Document quantity.
        :type Total: str
        :param _List: The list of documents.
        :type List: list of ReleaseQA
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Document quantity.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """The list of documents.
        :rtype: list of ReleaseQA
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseQA()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseRequest(AbstractModel):
    """ListRelease request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Robot ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def BotBizId(self):
        """Robot ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseResponse(AbstractModel):
    """ListRelease response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of release lists.
        :type Total: str
        :param _List: Release list.
        :type List: list of ListReleaseItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Number of release lists.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """Release list.
        :rtype: list of ListReleaseItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListReleaseItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListSelectDocRequest(AbstractModel):
    """ListSelectDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _FileName: Document name.

        :type FileName: str
        :param _Status: Document status: 7: under review; 8: review failed; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 20: expired.
        :type Status: list of int
        """
        self._BotBizId = None
        self._FileName = None
        self._Status = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        """Document name.

        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Status(self):
        """Document status: 7: under review; 8: review failed; 10: pending release; 11: releasing; 12: released; 13: learning; 14: learning failed; 20: expired.
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSelectDocResponse(AbstractModel):
    """ListSelectDoc response structure.

    """

    def __init__(self):
        r"""
        :param _List: Dropdown content.
        :type List: list of Option
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """Dropdown content.
        :rtype: list of Option
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Option()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListUnsatisfiedReplyRequest(AbstractModel):
    """ListUnsatisfiedReply request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _Query: User request (question or answer).
        :type Query: str
        :param _Reasons: Error type retrieval.
        :type Reasons: list of str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._Reasons = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        """User request (question or answer).
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        """Error type retrieval.
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUnsatisfiedReplyResponse(AbstractModel):
    """ListUnsatisfiedReply response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: str
        :param _List: List of dissatisfied responses.
        :type List: list of UnsatisfiedReply
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number.
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List of dissatisfied responses.
        :rtype: list of UnsatisfiedReply
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UnsatisfiedReply()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsageCallDetailRequest(AbstractModel):
    """ListUsageCallDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model identifier.
        :type ModelName: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Number of items per page.
        :type PageSize: int
        :param _UinAccount: Uin list.
        :type UinAccount: list of str
        :param _AppBizIds: Application ID list.
        :type AppBizIds: list of str
        :param _CallType: Call type list.
        :type CallType: str
        :param _SubScenes: Filter sub-scenario.
        :type SubScenes: list of str
        """
        self._ModelName = None
        self._StartTime = None
        self._EndTime = None
        self._PageNumber = None
        self._PageSize = None
        self._UinAccount = None
        self._AppBizIds = None
        self._CallType = None
        self._SubScenes = None

    @property
    def ModelName(self):
        """Model identifier.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def StartTime(self):
        """Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UinAccount(self):
        """Uin list.
        :rtype: list of str
        """
        return self._UinAccount

    @UinAccount.setter
    def UinAccount(self, UinAccount):
        self._UinAccount = UinAccount

    @property
    def AppBizIds(self):
        """Application ID list.
        :rtype: list of str
        """
        return self._AppBizIds

    @AppBizIds.setter
    def AppBizIds(self, AppBizIds):
        self._AppBizIds = AppBizIds

    @property
    def CallType(self):
        """Call type list.
        :rtype: str
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def SubScenes(self):
        """Filter sub-scenario.
        :rtype: list of str
        """
        return self._SubScenes

    @SubScenes.setter
    def SubScenes(self, SubScenes):
        self._SubScenes = SubScenes


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._UinAccount = params.get("UinAccount")
        self._AppBizIds = params.get("AppBizIds")
        self._CallType = params.get("CallType")
        self._SubScenes = params.get("SubScenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsageCallDetailResponse(AbstractModel):
    """ListUsageCallDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total count of lists.
        :type Total: int
        :param _List: List.
        :type List: list of CallDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """Total count of lists.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """List.
        :rtype: list of CallDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CallDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ModelInfo(AbstractModel):
    """Model information.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model name.
        :type ModelName: str
        :param _ModelDesc: Model description.
        :type ModelDesc: str
        :param _AliasName: Model name.
        :type AliasName: str
        :param _ResourceStatus: Resource status, 1: available; 2: exhausted.
        :type ResourceStatus: int
        :param _PromptWordsLimit: Character limit of prompt content.
        :type PromptWordsLimit: str
        :param _TopP: By controlling the diversity of content generation through core sampling, a higher Top P value will lead to more diverse content generation.
        :type TopP: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _Temperature: Temperature control randomness.
        :type Temperature: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _MaxTokens: Maximum quantity of tokens that can be generated.
        :type MaxTokens: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        :param _Source: Model source, Hunyuan: Tencent Hunyuan; Industry: Tencent Cloud industry large model; Experience: new model experience.
        :type Source: str
        :param _Icon: Model icon.
        :type Icon: str
        :param _IsFree: Whether it is free.
        :type IsFree: bool
        :param _InputLenLimit: Maximum characters input in the model dialog box.
        :type InputLenLimit: int
        :param _SupportWorkflowStatus: Workflow support levels:
0 - Not supported by the model;
1 - Supported by the model;
2 - Poorly supported by the model.
        :type SupportWorkflowStatus: int
        :param _ModelCategory: Model categories:
Generate: Generative model
Thought: Thinking model
        :type ModelCategory: str
        :param _IsDefault: Whether it is the default model.
        :type IsDefault: bool
        :param _RoleLenLimit: Maximum characters of role prompt words.
        :type RoleLenLimit: int
        :param _IsExclusive: Whether it is an exclusive concurrency model.
        :type IsExclusive: bool
        :param _SupportAiCallStatus: The model supports intelligent call effects.
        :type SupportAiCallStatus: int
        """
        self._ModelName = None
        self._ModelDesc = None
        self._AliasName = None
        self._ResourceStatus = None
        self._PromptWordsLimit = None
        self._TopP = None
        self._Temperature = None
        self._MaxTokens = None
        self._Source = None
        self._Icon = None
        self._IsFree = None
        self._InputLenLimit = None
        self._SupportWorkflowStatus = None
        self._ModelCategory = None
        self._IsDefault = None
        self._RoleLenLimit = None
        self._IsExclusive = None
        self._SupportAiCallStatus = None

    @property
    def ModelName(self):
        """Model name.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelDesc(self):
        """Model description.
        :rtype: str
        """
        return self._ModelDesc

    @ModelDesc.setter
    def ModelDesc(self, ModelDesc):
        self._ModelDesc = ModelDesc

    @property
    def AliasName(self):
        """Model name.
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def ResourceStatus(self):
        """Resource status, 1: available; 2: exhausted.
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def PromptWordsLimit(self):
        """Character limit of prompt content.
        :rtype: str
        """
        return self._PromptWordsLimit

    @PromptWordsLimit.setter
    def PromptWordsLimit(self, PromptWordsLimit):
        self._PromptWordsLimit = PromptWordsLimit

    @property
    def TopP(self):
        """By controlling the diversity of content generation through core sampling, a higher Top P value will lead to more diverse content generation.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        """Temperature control randomness.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def MaxTokens(self):
        """Maximum quantity of tokens that can be generated.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModelParameter`
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def Source(self):
        """Model source, Hunyuan: Tencent Hunyuan; Industry: Tencent Cloud industry large model; Experience: new model experience.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Icon(self):
        """Model icon.
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def IsFree(self):
        """Whether it is free.
        :rtype: bool
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def InputLenLimit(self):
        """Maximum characters input in the model dialog box.
        :rtype: int
        """
        return self._InputLenLimit

    @InputLenLimit.setter
    def InputLenLimit(self, InputLenLimit):
        self._InputLenLimit = InputLenLimit

    @property
    def SupportWorkflowStatus(self):
        """Workflow support levels:
0 - Not supported by the model;
1 - Supported by the model;
2 - Poorly supported by the model.
        :rtype: int
        """
        return self._SupportWorkflowStatus

    @SupportWorkflowStatus.setter
    def SupportWorkflowStatus(self, SupportWorkflowStatus):
        self._SupportWorkflowStatus = SupportWorkflowStatus

    @property
    def ModelCategory(self):
        """Model categories:
Generate: Generative model
Thought: Thinking model
        :rtype: str
        """
        return self._ModelCategory

    @ModelCategory.setter
    def ModelCategory(self, ModelCategory):
        self._ModelCategory = ModelCategory

    @property
    def IsDefault(self):
        """Whether it is the default model.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def RoleLenLimit(self):
        """Maximum characters of role prompt words.
        :rtype: int
        """
        return self._RoleLenLimit

    @RoleLenLimit.setter
    def RoleLenLimit(self, RoleLenLimit):
        self._RoleLenLimit = RoleLenLimit

    @property
    def IsExclusive(self):
        """Whether it is an exclusive concurrency model.
        :rtype: bool
        """
        return self._IsExclusive

    @IsExclusive.setter
    def IsExclusive(self, IsExclusive):
        self._IsExclusive = IsExclusive

    @property
    def SupportAiCallStatus(self):
        """The model supports intelligent call effects.
        :rtype: int
        """
        return self._SupportAiCallStatus

    @SupportAiCallStatus.setter
    def SupportAiCallStatus(self, SupportAiCallStatus):
        self._SupportAiCallStatus = SupportAiCallStatus


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._ModelDesc = params.get("ModelDesc")
        self._AliasName = params.get("AliasName")
        self._ResourceStatus = params.get("ResourceStatus")
        self._PromptWordsLimit = params.get("PromptWordsLimit")
        if params.get("TopP") is not None:
            self._TopP = ModelParameter()
            self._TopP._deserialize(params.get("TopP"))
        if params.get("Temperature") is not None:
            self._Temperature = ModelParameter()
            self._Temperature._deserialize(params.get("Temperature"))
        if params.get("MaxTokens") is not None:
            self._MaxTokens = ModelParameter()
            self._MaxTokens._deserialize(params.get("MaxTokens"))
        self._Source = params.get("Source")
        self._Icon = params.get("Icon")
        self._IsFree = params.get("IsFree")
        self._InputLenLimit = params.get("InputLenLimit")
        self._SupportWorkflowStatus = params.get("SupportWorkflowStatus")
        self._ModelCategory = params.get("ModelCategory")
        self._IsDefault = params.get("IsDefault")
        self._RoleLenLimit = params.get("RoleLenLimit")
        self._IsExclusive = params.get("IsExclusive")
        self._SupportAiCallStatus = params.get("SupportAiCallStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelParameter(AbstractModel):
    """Model parameter value range.

    """

    def __init__(self):
        r"""
        :param _Default: Default value.
        :type Default: float
        :param _Min: Minimum value.
        :type Min: float
        :param _Max: Maximum value.
        :type Max: float
        """
        self._Default = None
        self._Min = None
        self._Max = None

    @property
    def Default(self):
        """Default value.
        :rtype: float
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Min(self):
        """Minimum value.
        :rtype: float
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        """Maximum value.
        :rtype: float
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    """ModifyApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application ID.
        :type AppBizId: str
        :param _AppType: Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :type AppType: str
        :param _BaseConfig: Basic application configuration.
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _AppConfig: Application configuration.
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        """
        self._AppBizId = None
        self._AppType = None
        self._BaseConfig = None
        self._AppConfig = None
        self._LoginSubAccountUin = None

    @property
    def AppBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        """Application type; knowledge_qa - knowledge Q&A management; summary - knowledge summary; classifys - knowledge label extraction.
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        """Basic application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def AppConfig(self):
        """Application configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        """
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    """ModifyApp response structure.

    """

    def __init__(self):
        r"""
        :param _AppBizId: Application.
        :type AppBizId: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppBizId = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppBizId(self):
        """Application.
        :rtype: str
        """
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._AppBizId = params.get("AppBizId")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ModifyAttributeLabelRequest(AbstractModel):
    """ModifyAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _AttributeBizId: Label ID.
        :type AttributeBizId: str
        :param _AttrName: Label name.
        :type AttrName: str
        :param _AttrKey: Label identifier (abolished).
        :type AttrKey: str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _DeleteLabelBizIds: Deleted label value.
        :type DeleteLabelBizIds: list of str
        :param _Labels: Newly-added or edited label.
        :type Labels: list of AttributeLabel
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._AttrName = None
        self._AttrKey = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._DeleteLabelBizIds = None
        self._Labels = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        """Label ID.
        :rtype: str
        """
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrName(self):
        """Label name.
        :rtype: str
        """
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def AttrKey(self):
        """Label identifier (abolished).
        :rtype: str
        """
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def DeleteLabelBizIds(self):
        """Deleted label value.
        :rtype: list of str
        """
        return self._DeleteLabelBizIds

    @DeleteLabelBizIds.setter
    def DeleteLabelBizIds(self, DeleteLabelBizIds):
        self._DeleteLabelBizIds = DeleteLabelBizIds

    @property
    def Labels(self):
        """Newly-added or edited label.
        :rtype: list of AttributeLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrName = params.get("AttrName")
        self._AttrKey = params.get("AttrKey")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._DeleteLabelBizIds = params.get("DeleteLabelBizIds")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAttributeLabelResponse(AbstractModel):
    """ModifyAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDocAttrRangeRequest(AbstractModel):
    """ModifyDocAttrRange request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _DocBizIds: Document ID.
        :type DocBizIds: list of str
        :param _AttrRange: Attribute label applicable scope: 1: all, 2: by conditions.
        :type AttrRange: int
        :param _AttrLabels: Attribute label reference.
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._DocBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        """Document ID.
        :rtype: list of str
        """
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def AttrRange(self):
        """Attribute label applicable scope: 1: all, 2: by conditions.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Attribute label reference.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocAttrRangeResponse(AbstractModel):
    """ModifyDocAttrRange response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyDocCateRequest(AbstractModel):
    """ModifyDocCate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _Name: Category name.

        :type Name: str
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._Name = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Name(self):
        """Category name.

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Name = params.get("Name")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocCateResponse(AbstractModel):
    """ModifyDocCate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyDocRequest(AbstractModel):
    """ModifyDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _IsRefer: Whether to reference a link.
        :type IsRefer: bool
        :param _AttrRange: Applicable scope of labels: 1: all; 2: by condition.
        :type AttrRange: int
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        :param _AttrLabels: Associated labels.
        :type AttrLabels: list of AttrLabelRefer
        :param _WebUrl: Web page (or custom link) address.
        :type WebUrl: str
        :param _ReferUrlType: External reference link type: 0: system link 1: custom link.
When the value is 1, the weburl field cannot be empty; otherwise, it will not take effect.
        :type ReferUrlType: int
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _CateBizId: Category ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None
        self._IsRefer = None
        self._AttrRange = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttrLabels = None
        self._WebUrl = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def IsRefer(self):
        """Whether to reference a link.
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def AttrRange(self):
        """Applicable scope of labels: 1: all; 2: by condition.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttrLabels(self):
        """Associated labels.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def WebUrl(self):
        """Web page (or custom link) address.
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ReferUrlType(self):
        """External reference link type: 0: system link 1: custom link.
When the value is 1, the weburl field cannot be empty; otherwise, it will not take effect.
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._IsRefer = params.get("IsRefer")
        self._AttrRange = params.get("AttrRange")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._WebUrl = params.get("WebUrl")
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocResponse(AbstractModel):
    """ModifyDoc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyQAAttrRangeRequest(AbstractModel):
    """ModifyQAAttrRange request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _QaBizIds: Q&A ID.
        :type QaBizIds: list of str
        :param _AttrRange: Applicable scope of attribute label: 1: all, 2: by conditions.
        :type AttrRange: int
        :param _AttrLabels: Attribute label reference.
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        """Q&A ID.
        :rtype: list of str
        """
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def AttrRange(self):
        """Applicable scope of attribute label: 1: all, 2: by conditions.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Attribute label reference.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAAttrRangeResponse(AbstractModel):
    """ModifyQAAttrRange response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyQACateRequest(AbstractModel):
    """ModifyQACate request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _Name: Category name.

        :type Name: str
        :param _CateBizId: Category business ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._Name = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Name(self):
        """Category name.

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CateBizId(self):
        """Category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Name = params.get("Name")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQACateResponse(AbstractModel):
    """ModifyQACate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyQARequest(AbstractModel):
    """ModifyQA request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _Question: Question.
        :type Question: str
        :param _Answer: Answer.
        :type Answer: str
        :param _CustomParam: Custom parameter.
        :type CustomParam: str
        :param _AttrRange: Applicable scope of labels: 1. all; 2. by conditions.
        :type AttrRange: int
        :param _AttrLabels: Label reference.
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp, 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _SimilarQuestionModify: Similar question modification information (not passed if there is no modification to the similar question).
        :type SimilarQuestionModify: :class:`tencentcloud.lke.v20231130.models.SimilarQuestionModify`
        :param _QuestionDesc: Problem description.
        :type QuestionDesc: str
        """
        self._BotBizId = None
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._AttrRange = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._SimilarQuestionModify = None
        self._QuestionDesc = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        """Custom parameter.
        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrRange(self):
        """Applicable scope of labels: 1. all; 2. by conditions.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        """Label reference.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp, 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def SimilarQuestionModify(self):
        """Similar question modification information (not passed if there is no modification to the similar question).
        :rtype: :class:`tencentcloud.lke.v20231130.models.SimilarQuestionModify`
        """
        return self._SimilarQuestionModify

    @SimilarQuestionModify.setter
    def SimilarQuestionModify(self, SimilarQuestionModify):
        self._SimilarQuestionModify = SimilarQuestionModify

    @property
    def QuestionDesc(self):
        """Problem description.
        :rtype: str
        """
        return self._QuestionDesc

    @QuestionDesc.setter
    def QuestionDesc(self, QuestionDesc):
        self._QuestionDesc = QuestionDesc


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        if params.get("SimilarQuestionModify") is not None:
            self._SimilarQuestionModify = SimilarQuestionModify()
            self._SimilarQuestionModify._deserialize(params.get("SimilarQuestionModify"))
        self._QuestionDesc = params.get("QuestionDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAResponse(AbstractModel):
    """ModifyQA response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyRejectedQuestionRequest(AbstractModel):
    """ModifyRejectedQuestion request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _Question: Rejected question.


        :type Question: str
        :param _RejectedBizId: Unique id of the data source for the rejected question source.



        :type RejectedBizId: str
        """
        self._BotBizId = None
        self._Question = None
        self._RejectedBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        """Rejected question.


        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def RejectedBizId(self):
        """Unique id of the data source for the rejected question source.



        :rtype: str
        """
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._RejectedBizId = params.get("RejectedBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRejectedQuestionResponse(AbstractModel):
    """ModifyRejectedQuestion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class MsgFileInfo(AbstractModel):
    """Document information.

    """

    def __init__(self):
        r"""
        :param _FileName: Document name.
        :type FileName: str
        :param _FileSize: Document size.
        :type FileSize: str
        :param _FileUrl: Document URL.
        :type FileUrl: str
        :param _FileType: Document type.
        :type FileType: str
        :param _DocId: Document ID.
        :type DocId: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None

    @property
    def FileName(self):
        """Document name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """Document size.
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        """Document URL.
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        """Document type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecord(AbstractModel):
    """Message details.

    """

    def __init__(self):
        r"""
        :param _Content: Content.
        :type Content: str
        :param _SessionId: The Session ID corresponding to the current record.
        :type SessionId: str
        :param _RecordId: Record ID.
        :type RecordId: str
        :param _RelatedRecordId: Associated record ID.
        :type RelatedRecordId: str
        :param _IsFromSelf: Whether it is from oneself.
        :type IsFromSelf: bool
        :param _FromName: Sender name.
        :type FromName: str
        :param _FromAvatar: Avatar of the sender.
        :type FromAvatar: str
        :param _Timestamp: Timestamp.
        :type Timestamp: str
        :param _HasRead: Whether it is read.
        :type HasRead: bool
        :param _Score: Evaluation.
        :type Score: int
        :param _CanRating: Whether to rate.
        :type CanRating: bool
        :param _CanFeedback: Whether to display the feedback button.
        :type CanFeedback: bool
        :param _Type: Record type.
        :type Type: int
        :param _References: Reference source.
        :type References: list of MsgRecordReference
        :param _Reasons: Reason for evaluation.
        :type Reasons: list of str
        :param _IsLlmGenerated: Whether it is a large model.
        :type IsLlmGenerated: bool
        :param _ImageUrls: Image URL, which can be public read.
        :type ImageUrls: list of str
        :param _TokenStat: Statistical information of the current token.
        :type TokenStat: :class:`tencentcloud.lke.v20231130.models.TokenStat`
        :param _ReplyMethod: Response method.
1: Large model directly replies.
2: Conservative reply, reply to unknown questions.
3: Reply to rejected question.
4: Sensitive response.
5: Directly reply to Q&A pairs. Priority will be given to answering the adopted Q&A pairs.
6: Reply with welcome words.
7: Reply for concurrency limit exceeded.
8: Global intervention knowledge.
9: Reply during the task flow process. When task_flow.type = 0 in history, it is a response from the large model.
10: Reply with task flow answer.
11: Reply from the search engine.
12: Reply after knowledge polishing.
13: Reply with image understanding.
14: Reply based on real-time document.
        :type ReplyMethod: int
        :param _OptionCards: Option tab, used for multi-round dialogue.
        :type OptionCards: list of str
        :param _TaskFlow: Task information.
        :type TaskFlow: :class:`tencentcloud.lke.v20231130.models.TaskFlowInfo`
        :param _FileInfos: File information passed in by the user.
        :type FileInfos: list of FileInfo
        :param _QuoteInfos: Location information of reference source .
        :type QuoteInfos: list of QuoteInfo
        :param _AgentThought: Information on the thinking process of the agent.
        :type AgentThought: :class:`tencentcloud.lke.v20231130.models.AgentThought`
        :param _ExtraInfo: Expanded information.
        :type ExtraInfo: :class:`tencentcloud.lke.v20231130.models.ExtraInfo`
        :param _WorkFlow: Workflow information.
        :type WorkFlow: :class:`tencentcloud.lke.v20231130.models.WorkflowInfo`
        """
        self._Content = None
        self._SessionId = None
        self._RecordId = None
        self._RelatedRecordId = None
        self._IsFromSelf = None
        self._FromName = None
        self._FromAvatar = None
        self._Timestamp = None
        self._HasRead = None
        self._Score = None
        self._CanRating = None
        self._CanFeedback = None
        self._Type = None
        self._References = None
        self._Reasons = None
        self._IsLlmGenerated = None
        self._ImageUrls = None
        self._TokenStat = None
        self._ReplyMethod = None
        self._OptionCards = None
        self._TaskFlow = None
        self._FileInfos = None
        self._QuoteInfos = None
        self._AgentThought = None
        self._ExtraInfo = None
        self._WorkFlow = None

    @property
    def Content(self):
        """Content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SessionId(self):
        """The Session ID corresponding to the current record.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RecordId(self):
        """Record ID.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RelatedRecordId(self):
        """Associated record ID.
        :rtype: str
        """
        return self._RelatedRecordId

    @RelatedRecordId.setter
    def RelatedRecordId(self, RelatedRecordId):
        self._RelatedRecordId = RelatedRecordId

    @property
    def IsFromSelf(self):
        """Whether it is from oneself.
        :rtype: bool
        """
        return self._IsFromSelf

    @IsFromSelf.setter
    def IsFromSelf(self, IsFromSelf):
        self._IsFromSelf = IsFromSelf

    @property
    def FromName(self):
        """Sender name.
        :rtype: str
        """
        return self._FromName

    @FromName.setter
    def FromName(self, FromName):
        self._FromName = FromName

    @property
    def FromAvatar(self):
        """Avatar of the sender.
        :rtype: str
        """
        return self._FromAvatar

    @FromAvatar.setter
    def FromAvatar(self, FromAvatar):
        self._FromAvatar = FromAvatar

    @property
    def Timestamp(self):
        """Timestamp.
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def HasRead(self):
        """Whether it is read.
        :rtype: bool
        """
        return self._HasRead

    @HasRead.setter
    def HasRead(self, HasRead):
        self._HasRead = HasRead

    @property
    def Score(self):
        """Evaluation.
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def CanRating(self):
        """Whether to rate.
        :rtype: bool
        """
        return self._CanRating

    @CanRating.setter
    def CanRating(self, CanRating):
        self._CanRating = CanRating

    @property
    def CanFeedback(self):
        """Whether to display the feedback button.
        :rtype: bool
        """
        return self._CanFeedback

    @CanFeedback.setter
    def CanFeedback(self, CanFeedback):
        self._CanFeedback = CanFeedback

    @property
    def Type(self):
        """Record type.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def References(self):
        """Reference source.
        :rtype: list of MsgRecordReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Reasons(self):
        """Reason for evaluation.
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def IsLlmGenerated(self):
        """Whether it is a large model.
        :rtype: bool
        """
        return self._IsLlmGenerated

    @IsLlmGenerated.setter
    def IsLlmGenerated(self, IsLlmGenerated):
        self._IsLlmGenerated = IsLlmGenerated

    @property
    def ImageUrls(self):
        """Image URL, which can be public read.
        :rtype: list of str
        """
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls

    @property
    def TokenStat(self):
        """Statistical information of the current token.
        :rtype: :class:`tencentcloud.lke.v20231130.models.TokenStat`
        """
        return self._TokenStat

    @TokenStat.setter
    def TokenStat(self, TokenStat):
        self._TokenStat = TokenStat

    @property
    def ReplyMethod(self):
        """Response method.
1: Large model directly replies.
2: Conservative reply, reply to unknown questions.
3: Reply to rejected question.
4: Sensitive response.
5: Directly reply to Q&A pairs. Priority will be given to answering the adopted Q&A pairs.
6: Reply with welcome words.
7: Reply for concurrency limit exceeded.
8: Global intervention knowledge.
9: Reply during the task flow process. When task_flow.type = 0 in history, it is a response from the large model.
10: Reply with task flow answer.
11: Reply from the search engine.
12: Reply after knowledge polishing.
13: Reply with image understanding.
14: Reply based on real-time document.
        :rtype: int
        """
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod

    @property
    def OptionCards(self):
        """Option tab, used for multi-round dialogue.
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def TaskFlow(self):
        """Task information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskFlowInfo`
        """
        return self._TaskFlow

    @TaskFlow.setter
    def TaskFlow(self, TaskFlow):
        self._TaskFlow = TaskFlow

    @property
    def FileInfos(self):
        """File information passed in by the user.
        :rtype: list of FileInfo
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def QuoteInfos(self):
        """Location information of reference source .
        :rtype: list of QuoteInfo
        """
        return self._QuoteInfos

    @QuoteInfos.setter
    def QuoteInfos(self, QuoteInfos):
        self._QuoteInfos = QuoteInfos

    @property
    def AgentThought(self):
        """Information on the thinking process of the agent.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentThought`
        """
        return self._AgentThought

    @AgentThought.setter
    def AgentThought(self, AgentThought):
        self._AgentThought = AgentThought

    @property
    def ExtraInfo(self):
        """Expanded information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def WorkFlow(self):
        """Workflow information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.WorkflowInfo`
        """
        return self._WorkFlow

    @WorkFlow.setter
    def WorkFlow(self, WorkFlow):
        self._WorkFlow = WorkFlow


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._SessionId = params.get("SessionId")
        self._RecordId = params.get("RecordId")
        self._RelatedRecordId = params.get("RelatedRecordId")
        self._IsFromSelf = params.get("IsFromSelf")
        self._FromName = params.get("FromName")
        self._FromAvatar = params.get("FromAvatar")
        self._Timestamp = params.get("Timestamp")
        self._HasRead = params.get("HasRead")
        self._Score = params.get("Score")
        self._CanRating = params.get("CanRating")
        self._CanFeedback = params.get("CanFeedback")
        self._Type = params.get("Type")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = MsgRecordReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._Reasons = params.get("Reasons")
        self._IsLlmGenerated = params.get("IsLlmGenerated")
        self._ImageUrls = params.get("ImageUrls")
        if params.get("TokenStat") is not None:
            self._TokenStat = TokenStat()
            self._TokenStat._deserialize(params.get("TokenStat"))
        self._ReplyMethod = params.get("ReplyMethod")
        self._OptionCards = params.get("OptionCards")
        if params.get("TaskFlow") is not None:
            self._TaskFlow = TaskFlowInfo()
            self._TaskFlow._deserialize(params.get("TaskFlow"))
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        if params.get("QuoteInfos") is not None:
            self._QuoteInfos = []
            for item in params.get("QuoteInfos"):
                obj = QuoteInfo()
                obj._deserialize(item)
                self._QuoteInfos.append(obj)
        if params.get("AgentThought") is not None:
            self._AgentThought = AgentThought()
            self._AgentThought._deserialize(params.get("AgentThought"))
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        if params.get("WorkFlow") is not None:
            self._WorkFlow = WorkflowInfo()
            self._WorkFlow._deserialize(params.get("WorkFlow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordReference(AbstractModel):
    """Chat details Refer.

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: str
        :param _Url: URL.
        :type Url: str
        :param _Type: Type.
        :type Type: int
        :param _Name: Name.
        :type Name: str
        :param _DocId: Source document ID.
        :type DocId: str
        """
        self._Id = None
        self._Url = None
        self._Type = None
        self._Name = None
        self._DocId = None

    @property
    def Id(self):
        """ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """URL.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        """Type.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DocId(self):
        """Source document ID.
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    """Dropdown options.

    """

    def __init__(self):
        r"""
        :param _Text: Text.
        :type Text: str
        :param _Value: Value.
        :type Value: str
        :param _CharSize: Number of characters in a file.
        :type CharSize: str
        :param _FileType: File type.
        :type FileType: str
        """
        self._Text = None
        self._Value = None
        self._CharSize = None
        self._FileType = None

    @property
    def Text(self):
        """Text.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        """Value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def CharSize(self):
        """Number of characters in a file.
        :rtype: str
        """
        return self._CharSize

    @CharSize.setter
    def CharSize(self, CharSize):
        self._CharSize = CharSize

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        self._CharSize = params.get("CharSize")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginToolReqParam(AbstractModel):
    """Plugin parameter request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name.
        :type Name: str
        :param _Desc: Parameter description.
        :type Desc: str
        :param _Type: Parameter type, 0: string; 1: int; 2: float; 3: bool; 4: object; 5: array_string; 6: array_int; 7: array_float; 8: array_bool; 9: array_object, 99: null, 100: upspecified.
        :type Type: int
        :param _IsRequired: Whether the parameter is required.
        :type IsRequired: bool
        :param _DefaultValue: Parameter default value.
        :type DefaultValue: str
        :param _SubParams: Sub-parameter. "ParamType" is useful when it is "OBJECT " or "ARRAY<>" type.
        :type SubParams: list of PluginToolReqParam
        :param _GlobalHidden: Whether the plugin parameter configuration is hidden and invisible. true - Hidden and invisible; false - Visible.
        :type GlobalHidden: bool
        :param _OneOf: OneOf type parameter.
        :type OneOf: list of PluginToolReqParam
        :param _AnyOf: AnyOf type parameter.
        :type AnyOf: list of PluginToolReqParam
        """
        self._Name = None
        self._Desc = None
        self._Type = None
        self._IsRequired = None
        self._DefaultValue = None
        self._SubParams = None
        self._GlobalHidden = None
        self._OneOf = None
        self._AnyOf = None

    @property
    def Name(self):
        """Parameter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Parameter description.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Type(self):
        """Parameter type, 0: string; 1: int; 2: float; 3: bool; 4: object; 5: array_string; 6: array_int; 7: array_float; 8: array_bool; 9: array_object, 99: null, 100: upspecified.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsRequired(self):
        """Whether the parameter is required.
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def DefaultValue(self):
        """Parameter default value.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def SubParams(self):
        """Sub-parameter. "ParamType" is useful when it is "OBJECT " or "ARRAY<>" type.
        :rtype: list of PluginToolReqParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def GlobalHidden(self):
        """Whether the plugin parameter configuration is hidden and invisible. true - Hidden and invisible; false - Visible.
        :rtype: bool
        """
        return self._GlobalHidden

    @GlobalHidden.setter
    def GlobalHidden(self, GlobalHidden):
        self._GlobalHidden = GlobalHidden

    @property
    def OneOf(self):
        """OneOf type parameter.
        :rtype: list of PluginToolReqParam
        """
        return self._OneOf

    @OneOf.setter
    def OneOf(self, OneOf):
        self._OneOf = OneOf

    @property
    def AnyOf(self):
        """AnyOf type parameter.
        :rtype: list of PluginToolReqParam
        """
        return self._AnyOf

    @AnyOf.setter
    def AnyOf(self, AnyOf):
        self._AnyOf = AnyOf


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Type = params.get("Type")
        self._IsRequired = params.get("IsRequired")
        self._DefaultValue = params.get("DefaultValue")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._GlobalHidden = params.get("GlobalHidden")
        if params.get("OneOf") is not None:
            self._OneOf = []
            for item in params.get("OneOf"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._OneOf.append(obj)
        if params.get("AnyOf") is not None:
            self._AnyOf = []
            for item in params.get("AnyOf"):
                obj = PluginToolReqParam()
                obj._deserialize(item)
                self._AnyOf.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Procedure(AbstractModel):
    """Execution process information log.

    """

    def __init__(self):
        r"""
        :param _Name: English name of execution process.
        :type Name: str
        :param _Title: Chinese name for display.
        :type Title: str
        :param _Status: Status: processing, success, failed.
        :type Status: str
        :param _Count: Number of consumed tokens.
        :type Count: int
        :param _Debugging: Debugging information.
        :type Debugging: :class:`tencentcloud.lke.v20231130.models.ProcedureDebugging`
        :param _ResourceStatus: Billing resource status, 1: available; 2: unavailable.
        :type ResourceStatus: int
        """
        self._Name = None
        self._Title = None
        self._Status = None
        self._Count = None
        self._Debugging = None
        self._ResourceStatus = None

    @property
    def Name(self):
        """English name of execution process.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """Chinese name for display.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        """Status: processing, success, failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        """Number of consumed tokens.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Debugging(self):
        """Debugging information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.ProcedureDebugging`
        """
        return self._Debugging

    @Debugging.setter
    def Debugging(self, Debugging):
        self._Debugging = Debugging

    @property
    def ResourceStatus(self):
        """Billing resource status, 1: available; 2: unavailable.
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        if params.get("Debugging") is not None:
            self._Debugging = ProcedureDebugging()
            self._Debugging._deserialize(params.get("Debugging"))
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedureDebugging(AbstractModel):
    """Debug information.

    """

    def __init__(self):
        r"""
        :param _Content: Retrieve query.
        :type Content: str
        :param _System: System prompt.
        :type System: str
        :param _Histories: Multiple rounds of historical information.
        :type Histories: list of HistorySummary
        :param _Knowledge: Retrieve knowledge.
        :type Knowledge: list of KnowledgeSummary
        :param _TaskFlow: Task process.
        :type TaskFlow: :class:`tencentcloud.lke.v20231130.models.TaskFlowSummary`
        :param _WorkFlow: Workflow debugging information.
        :type WorkFlow: :class:`tencentcloud.lke.v20231130.models.WorkFlowSummary`
        :param _Agent: Agent debugging information.
        :type Agent: :class:`tencentcloud.lke.v20231130.models.AgentDebugInfo`
        :param _CustomVariables: Custom parameter.
        :type CustomVariables: list of str
        """
        self._Content = None
        self._System = None
        self._Histories = None
        self._Knowledge = None
        self._TaskFlow = None
        self._WorkFlow = None
        self._Agent = None
        self._CustomVariables = None

    @property
    def Content(self):
        """Retrieve query.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def System(self):
        """System prompt.
        :rtype: str
        """
        return self._System

    @System.setter
    def System(self, System):
        self._System = System

    @property
    def Histories(self):
        """Multiple rounds of historical information.
        :rtype: list of HistorySummary
        """
        return self._Histories

    @Histories.setter
    def Histories(self, Histories):
        self._Histories = Histories

    @property
    def Knowledge(self):
        """Retrieve knowledge.
        :rtype: list of KnowledgeSummary
        """
        return self._Knowledge

    @Knowledge.setter
    def Knowledge(self, Knowledge):
        self._Knowledge = Knowledge

    @property
    def TaskFlow(self):
        """Task process.
        :rtype: :class:`tencentcloud.lke.v20231130.models.TaskFlowSummary`
        """
        return self._TaskFlow

    @TaskFlow.setter
    def TaskFlow(self, TaskFlow):
        self._TaskFlow = TaskFlow

    @property
    def WorkFlow(self):
        """Workflow debugging information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.WorkFlowSummary`
        """
        return self._WorkFlow

    @WorkFlow.setter
    def WorkFlow(self, WorkFlow):
        self._WorkFlow = WorkFlow

    @property
    def Agent(self):
        """Agent debugging information.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AgentDebugInfo`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def CustomVariables(self):
        """Custom parameter.
        :rtype: list of str
        """
        return self._CustomVariables

    @CustomVariables.setter
    def CustomVariables(self, CustomVariables):
        self._CustomVariables = CustomVariables


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._System = params.get("System")
        if params.get("Histories") is not None:
            self._Histories = []
            for item in params.get("Histories"):
                obj = HistorySummary()
                obj._deserialize(item)
                self._Histories.append(obj)
        if params.get("Knowledge") is not None:
            self._Knowledge = []
            for item in params.get("Knowledge"):
                obj = KnowledgeSummary()
                obj._deserialize(item)
                self._Knowledge.append(obj)
        if params.get("TaskFlow") is not None:
            self._TaskFlow = TaskFlowSummary()
            self._TaskFlow._deserialize(params.get("TaskFlow"))
        if params.get("WorkFlow") is not None:
            self._WorkFlow = WorkFlowSummary()
            self._WorkFlow._deserialize(params.get("WorkFlow"))
        if params.get("Agent") is not None:
            self._Agent = AgentDebugInfo()
            self._Agent._deserialize(params.get("Agent"))
        self._CustomVariables = params.get("CustomVariables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QACate(AbstractModel):
    """Obtain Q&A category group.

    """

    def __init__(self):
        r"""
        :param _CateBizId: Q&A category business ID.
        :type CateBizId: str
        :param _Name: Category name.
        :type Name: str
        :param _Total: Quantity of Q&As under the category.
        :type Total: int
        :param _CanAdd: Whether it is possible to add.
        :type CanAdd: bool
        :param _CanEdit: Whether it can be edited.
        :type CanEdit: bool
        :param _CanDelete: Whether it can be deleted.
        :type CanDelete: bool
        :param _Children: Subcategory.
        :type Children: list of QACate
        """
        self._CateBizId = None
        self._Name = None
        self._Total = None
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._Children = None

    @property
    def CateBizId(self):
        """Q&A category business ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Name(self):
        """Category name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        """Quantity of Q&As under the category.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CanAdd(self):
        """Whether it is possible to add.
        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        """Whether it can be edited.
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        """Whether it can be deleted.
        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Children(self):
        """Subcategory.
        :rtype: list of QACate
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._CateBizId = params.get("CateBizId")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = QACate()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAList(AbstractModel):
    """Q&A list.

    """

    def __init__(self):
        r"""
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _IsAccepted: Whether to accept.
        :type IsAccepted: bool
        :param _CateBizId: Category ID.
        :type CateBizId: str
        :param _Question: Question.
        :type Question: str
        :param _Answer: Answer.
        :type Answer: str
        """
        self._QaBizId = None
        self._IsAccepted = None
        self._CateBizId = None
        self._Question = None
        self._Answer = None

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def IsAccepted(self):
        """Whether to accept.
        :rtype: bool
        """
        return self._IsAccepted

    @IsAccepted.setter
    def IsAccepted(self, IsAccepted):
        self._IsAccepted = IsAccepted

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._IsAccepted = params.get("IsAccepted")
        self._CateBizId = params.get("CateBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAQuery(AbstractModel):
    """Q&A query parameter.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number.




        :type PageNumber: int
        :param _PageSize: Number of items per page.

        :type PageSize: int
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _Query: Query content.

        :type Query: str
        :param _CateBizId: Category ID.

        :type CateBizId: str
        :param _AcceptStatus: Verification status.

        :type AcceptStatus: list of int non-negative
        :param _ReleaseStatus: Release status.

        :type ReleaseStatus: list of int non-negative
        :param _DocBizId: Document ID.

        :type DocBizId: str
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _Source: Source.


        :type Source: int
        :param _QueryAnswer: Query an answer.

        :type QueryAnswer: str
        :param _QueryType: Query type: filename, attribute label.
        :type QueryType: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._BotBizId = None
        self._Query = None
        self._CateBizId = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._QaBizId = None
        self._Source = None
        self._QueryAnswer = None
        self._QueryType = None

    @property
    def PageNumber(self):
        """Page number.




        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Number of items per page.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Query(self):
        """Query content.

        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def CateBizId(self):
        """Category ID.

        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def AcceptStatus(self):
        """Verification status.

        :rtype: list of int non-negative
        """
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        """Release status.

        :rtype: list of int non-negative
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        """Document ID.

        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Source(self):
        """Source.


        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        """Query an answer.

        :rtype: str
        """
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer

    @property
    def QueryType(self):
        """Query type: filename, attribute label.
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._BotBizId = params.get("BotBizId")
        self._Query = params.get("Query")
        self._CateBizId = params.get("CateBizId")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._QaBizId = params.get("QaBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        self._QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuoteInfo(AbstractModel):
    """Search engine reference source index.

    """

    def __init__(self):
        r"""
        :param _Position: Reference source location.
        :type Position: int
        :param _Index: Reference source index sequence.
        :type Index: str
        """
        self._Position = None
        self._Index = None

    @property
    def Position(self):
        """Reference source location.
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Index(self):
        """Reference source index sequence.
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Position = params.get("Position")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateMsgRecordRequest(AbstractModel):
    """RateMsgRecord request structure.

    """

    def __init__(self):
        r"""
        :param _BotAppKey: Application appkey.
        :type BotAppKey: str
        :param _RecordId: Message ID.
        :type RecordId: str
        :param _Score: 1: like; 2: dislike.
        :type Score: int
        :param _Reasons: Reason.
        :type Reasons: list of str
        """
        self._BotAppKey = None
        self._RecordId = None
        self._Score = None
        self._Reasons = None

    @property
    def BotAppKey(self):
        """Application appkey.
        :rtype: str
        """
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def RecordId(self):
        """Message ID.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Score(self):
        """1: like; 2: dislike.
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Reasons(self):
        """Reason.
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._BotAppKey = params.get("BotAppKey")
        self._RecordId = params.get("RecordId")
        self._Score = params.get("Score")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateMsgRecordResponse(AbstractModel):
    """RateMsgRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ReconstructDocumentFailedPage(AbstractModel):
    """Document parsing failure record.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Failure page number.
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        """Failure page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferDetail(AbstractModel):
    """Reference source details.

    """

    def __init__(self):
        r"""
        :param _ReferBizId: Reference ID.
        :type ReferBizId: str
        :param _DocType: Document type (1: Q&A; 2: document paragraph).
        :type DocType: int
        :param _DocName: Document name.
        :type DocName: str
        :param _PageContent: Fragment content.
        :type PageContent: str
        :param _Question: Question.
        :type Question: str
        :param _Answer: Answer.
        :type Answer: str
        :param _Confidence: Confidence.
        :type Confidence: float
        :param _Mark: Mark.
        :type Mark: int
        :param _Highlights: Fragment highlight content.
        :type Highlights: list of Highlight
        :param _OrgData: Original content.
        :type OrgData: str
        :param _PageInfos: Page number information.
        :type PageInfos: list of int non-negative
        :param _SheetInfos: Sheet information.
        :type SheetInfos: list of str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        """
        self._ReferBizId = None
        self._DocType = None
        self._DocName = None
        self._PageContent = None
        self._Question = None
        self._Answer = None
        self._Confidence = None
        self._Mark = None
        self._Highlights = None
        self._OrgData = None
        self._PageInfos = None
        self._SheetInfos = None
        self._DocBizId = None

    @property
    def ReferBizId(self):
        """Reference ID.
        :rtype: str
        """
        return self._ReferBizId

    @ReferBizId.setter
    def ReferBizId(self, ReferBizId):
        self._ReferBizId = ReferBizId

    @property
    def DocType(self):
        """Document type (1: Q&A; 2: document paragraph).
        :rtype: int
        """
        return self._DocType

    @DocType.setter
    def DocType(self, DocType):
        self._DocType = DocType

    @property
    def DocName(self):
        """Document name.
        :rtype: str
        """
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def PageContent(self):
        """Fragment content.
        :rtype: str
        """
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Answer.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Confidence(self):
        """Confidence.
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Mark(self):
        """Mark.
        :rtype: int
        """
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Highlights(self):
        """Fragment highlight content.
        :rtype: list of Highlight
        """
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        """Original content.
        :rtype: str
        """
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def PageInfos(self):
        """Page number information.
        :rtype: list of int non-negative
        """
        return self._PageInfos

    @PageInfos.setter
    def PageInfos(self, PageInfos):
        self._PageInfos = PageInfos

    @property
    def SheetInfos(self):
        """Sheet information.
        :rtype: list of str
        """
        return self._SheetInfos

    @SheetInfos.setter
    def SheetInfos(self, SheetInfos):
        self._SheetInfos = SheetInfos

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._ReferBizId = params.get("ReferBizId")
        self._DocType = params.get("DocType")
        self._DocName = params.get("DocName")
        self._PageContent = params.get("PageContent")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Confidence = params.get("Confidence")
        self._Mark = params.get("Mark")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        self._PageInfos = params.get("PageInfos")
        self._SheetInfos = params.get("SheetInfos")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectedQuestion(AbstractModel):
    """Release rejected questions.

    """

    def __init__(self):
        r"""
        :param _RejectedBizId: Reject question ID.
        :type RejectedBizId: str
        :param _Question: The question that has been rejected.
        :type Question: str
        :param _Status: Status.
        :type Status: int
        :param _StatusDesc: Status description.
        :type StatusDesc: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _IsAllowEdit: Whether editing is allowed.
        :type IsAllowEdit: bool
        :param _IsAllowDelete: Whether deletion is allowed.
        :type IsAllowDelete: bool
        """
        self._RejectedBizId = None
        self._Question = None
        self._Status = None
        self._StatusDesc = None
        self._UpdateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None

    @property
    def RejectedBizId(self):
        """Reject question ID.
        :rtype: str
        """
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId

    @property
    def Question(self):
        """The question that has been rejected.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Status(self):
        """Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Status description.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowEdit(self):
        """Whether editing is allowed.
        :rtype: bool
        """
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        """Whether deletion is allowed.
        :rtype: bool
        """
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete


    def _deserialize(self, params):
        self._RejectedBizId = params.get("RejectedBizId")
        self._Question = params.get("Question")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseConfigs(AbstractModel):
    """Release configuration items.

    """

    def __init__(self):
        r"""
        :param _ConfigItem: Configuration item description.
        :type ConfigItem: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Action: Status.
        :type Action: int
        :param _Value: Content after modification.
        :type Value: str
        :param _LastValue: Content before modification.
        :type LastValue: str
        :param _Content: Modified content (display "content" with priority. If "content" is empty, take "value").
        :type Content: str
        :param _Message: Reason for failure.
        :type Message: str
        """
        self._ConfigItem = None
        self._UpdateTime = None
        self._Action = None
        self._Value = None
        self._LastValue = None
        self._Content = None
        self._Message = None

    @property
    def ConfigItem(self):
        """Configuration item description.
        :rtype: str
        """
        return self._ConfigItem

    @ConfigItem.setter
    def ConfigItem(self, ConfigItem):
        self._ConfigItem = ConfigItem

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        """Status.
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        """Content after modification.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def LastValue(self):
        """Content before modification.
        :rtype: str
        """
        return self._LastValue

    @LastValue.setter
    def LastValue(self, LastValue):
        self._LastValue = LastValue

    @property
    def Content(self):
        """Modified content (display "content" with priority. If "content" is empty, take "value").
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Message(self):
        """Reason for failure.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._ConfigItem = params.get("ConfigItem")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        self._LastValue = params.get("LastValue")
        self._Content = params.get("Content")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseDoc(AbstractModel):
    """Release document details.

    """

    def __init__(self):
        r"""
        :param _FileName: File name.
        :type FileName: str
        :param _FileType: File type.
        :type FileType: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Action: Status.
        :type Action: int
        :param _ActionDesc: Status description.
        :type ActionDesc: str
        :param _Message: Reason for failure.
        :type Message: str
        :param _DocBizId: Document business ID.
        :type DocBizId: str
        """
        self._FileName = None
        self._FileType = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None
        self._DocBizId = None

    @property
    def FileName(self):
        """File name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """File type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        """Status.
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        """Status description.
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        """Reason for failure.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DocBizId(self):
        """Document business ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseQA(AbstractModel):
    """Release Q&A.

    """

    def __init__(self):
        r"""
        :param _Question: Question.
        :type Question: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Action: Status.
        :type Action: int
        :param _ActionDesc: Status description.
        :type ActionDesc: str
        :param _Source: Source, 1: documentation generation; 2: batch import; 3: manual addition.
        :type Source: int
        :param _SourceDesc: Source description.
        :type SourceDesc: str
        :param _FileName: Filename.
        :type FileName: str
        :param _FileType: Document type.
        :type FileType: str
        :param _Message: Reason for failure
        :type Message: str
        :param _ReleaseStatus: Release status.
        :type ReleaseStatus: int
        :param _QaBizId: Q&A ID.
        :type QaBizId: str
        :param _DocBizId: Document business ID.
        :type DocBizId: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Source = None
        self._SourceDesc = None
        self._FileName = None
        self._FileType = None
        self._Message = None
        self._ReleaseStatus = None
        self._QaBizId = None
        self._DocBizId = None

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        """Status.
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        """Status description.
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Source(self):
        """Source, 1: documentation generation; 2: batch import; 3: manual addition.
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        """Source description.
        :rtype: str
        """
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def FileName(self):
        """Filename.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """Document type.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Message(self):
        """Reason for failure
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReleaseStatus(self):
        """Release status.
        :rtype: int
        """
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def QaBizId(self):
        """Q&A ID.
        :rtype: str
        """
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def DocBizId(self):
        """Document business ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._Message = params.get("Message")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._QaBizId = params.get("QaBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseRejectedQuestion(AbstractModel):
    """Release rejected questions.

    """

    def __init__(self):
        r"""
        :param _Question: Question.
        :type Question: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Action: Status.
        :type Action: int
        :param _ActionDesc: Status description.
        :type ActionDesc: str
        :param _Message: Reason for failure.
        :type Message: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None

    @property
    def Question(self):
        """Question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def UpdateTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        """Status.
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        """Status description.
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        """Reason for failure.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameDocRequest(AbstractModel):
    """RenameDoc request structure.

    """

    def __init__(self):
        r"""
        :param _LoginUin: Login to user's root account (required in integrator mode).	
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).	
        :type LoginSubAccountUin: str
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _NewName: New document name, which needs to include the suffix.
        :type NewName: str
        """
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._BotBizId = None
        self._DocBizId = None
        self._NewName = None

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).	
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def NewName(self):
        """New document name, which needs to include the suffix.
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameDocResponse(AbstractModel):
    """RenameDoc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RetryDocAuditRequest(AbstractModel):
    """RetryDocAudit request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocAuditResponse(AbstractModel):
    """RetryDocAudit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RetryDocParseRequest(AbstractModel):
    """RetryDocParse request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        """Application ID
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocParseResponse(AbstractModel):
    """RetryDocParse response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RetryReleaseRequest(AbstractModel):
    """RetryRelease request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Robot ID.
        :type BotBizId: str
        :param _ReleaseBizId: Release business id.
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        """Robot ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        """Release business id.
        :rtype: str
        """
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryReleaseResponse(AbstractModel):
    """RetryRelease response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunNodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type, 0: unspecified; 1: start node; 2: api node; 3: inquiry node; 4: answer node.
        :type NodeType: int
        :param _NodeId: Node ID.
        :type NodeId: str
        :param _NodeName: Node name.
        :type NodeName: str
        :param _InvokeApi: Requested API.
        :type InvokeApi: :class:`tencentcloud.lke.v20231130.models.InvokeAPI`
        :param _SlotValues: Values of all slots of the current node, key: SlotID. Return an Null even if there is no value.
        :type SlotValues: list of ValueInfo
        """
        self._NodeType = None
        self._NodeId = None
        self._NodeName = None
        self._InvokeApi = None
        self._SlotValues = None

    @property
    def NodeType(self):
        """Node type, 0: unspecified; 1: start node; 2: api node; 3: inquiry node; 4: answer node.
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        """Node ID.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        """Node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def InvokeApi(self):
        """Requested API.
        :rtype: :class:`tencentcloud.lke.v20231130.models.InvokeAPI`
        """
        return self._InvokeApi

    @InvokeApi.setter
    def InvokeApi(self, InvokeApi):
        self._InvokeApi = InvokeApi

    @property
    def SlotValues(self):
        """Values of all slots of the current node, key: SlotID. Return an Null even if there is no value.
        :rtype: list of ValueInfo
        """
        return self._SlotValues

    @SlotValues.setter
    def SlotValues(self, SlotValues):
        self._SlotValues = SlotValues


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        if params.get("InvokeApi") is not None:
            self._InvokeApi = InvokeAPI()
            self._InvokeApi._deserialize(params.get("InvokeApi"))
        if params.get("SlotValues") is not None:
            self._SlotValues = []
            for item in params.get("SlotValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._SlotValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDocRequest(AbstractModel):
    """SaveDoc request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _FileName: File name.
        :type FileName: str
        :param _FileType: File type (md|txt|docx|pdf|xlsx).
        :type FileType: str
        :param _CosUrl: The cos path of the platform, consistent with the UploadPath parameter queried by the DescribeStorageCredential api.
        :type CosUrl: str
        :param _ETag: ETag, short for entity tag, is an information tag that identifies the content of an object when it is created and can be used to check whether the content of the object has changed.
        :type ETag: str
        :param _CosHash: Verify the consistency of the uploaded file on the cloud and the local file by validating the crc64 encoding in the cos_hash x-cos-hash-crc64ecma header.<br> After the COS is successfully uploaded, obtain it from the response header.
        :type CosHash: str
        :param _Size: File size.
        :type Size: str
        :param _AttrRange: Applicable scope of labels: 1: all; 2: by conditional range.
        :type AttrRange: int
        :param _Source: Source (0: source file import; 1: web page import).
        :type Source: int
        :param _WebUrl: Web page (or custom link) address.
        :type WebUrl: str
        :param _AttrLabels: Label reference.
        :type AttrLabels: list of AttrLabelRefer
        :param _ReferUrlType: External reference link type: 0: system link; 1: custom link.
When the value is 1, the weburl field cannot be empty; otherwise, it will not take effect.
        :type ReferUrlType: int
        :param _ExpireStart: Effective start time, unix timestamp.
        :type ExpireStart: str
        :param _ExpireEnd: Effective end time, unix timestamp. 0 indicates permanent validity.
        :type ExpireEnd: str
        :param _IsRefer: Whether to reference a link.
        :type IsRefer: bool
        :param _Opt: Document operation type: 1: batch import (import Q&A pairs in batches); 2: document import (normally import a single document). The default value is 1.<br>Please note that when opt = 1, please download the Excel template from the Tencent Cloud Agent Development Platform/TCADP page.
        :type Opt: int
        :param _CateBizId: Category ID.
        :type CateBizId: str
        """
        self._BotBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._ETag = None
        self._CosHash = None
        self._Size = None
        self._AttrRange = None
        self._Source = None
        self._WebUrl = None
        self._AttrLabels = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._IsRefer = None
        self._Opt = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        """File name.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """File type (md|txt|docx|pdf|xlsx).
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        """The cos path of the platform, consistent with the UploadPath parameter queried by the DescribeStorageCredential api.
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def ETag(self):
        """ETag, short for entity tag, is an information tag that identifies the content of an object when it is created and can be used to check whether the content of the object has changed.
        :rtype: str
        """
        return self._ETag

    @ETag.setter
    def ETag(self, ETag):
        self._ETag = ETag

    @property
    def CosHash(self):
        """Verify the consistency of the uploaded file on the cloud and the local file by validating the crc64 encoding in the cos_hash x-cos-hash-crc64ecma header.<br> After the COS is successfully uploaded, obtain it from the response header.
        :rtype: str
        """
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        """File size.
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AttrRange(self):
        """Applicable scope of labels: 1: all; 2: by conditional range.
        :rtype: int
        """
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def Source(self):
        """Source (0: source file import; 1: web page import).
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def WebUrl(self):
        """Web page (or custom link) address.
        :rtype: str
        """
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def AttrLabels(self):
        """Label reference.
        :rtype: list of AttrLabelRefer
        """
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ReferUrlType(self):
        """External reference link type: 0: system link; 1: custom link.
When the value is 1, the weburl field cannot be empty; otherwise, it will not take effect.
        :rtype: int
        """
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        """Effective start time, unix timestamp.
        :rtype: str
        """
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        """Effective end time, unix timestamp. 0 indicates permanent validity.
        :rtype: str
        """
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def IsRefer(self):
        """Whether to reference a link.
        :rtype: bool
        """
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def Opt(self):
        """Document operation type: 1: batch import (import Q&A pairs in batches); 2: document import (normally import a single document). The default value is 1.<br>Please note that when opt = 1, please download the Excel template from the Tencent Cloud Agent Development Platform/TCADP page.
        :rtype: int
        """
        return self._Opt

    @Opt.setter
    def Opt(self, Opt):
        self._Opt = Opt

    @property
    def CateBizId(self):
        """Category ID.
        :rtype: str
        """
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._ETag = params.get("ETag")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._AttrRange = params.get("AttrRange")
        self._Source = params.get("Source")
        self._WebUrl = params.get("WebUrl")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._IsRefer = params.get("IsRefer")
        self._Opt = params.get("Opt")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDocResponse(AbstractModel):
    """SaveDoc response structure.

    """

    def __init__(self):
        r"""
        :param _DocBizId: Document ID.
        :type DocBizId: str
        :param _ErrorMsg: Import error message.
        :type ErrorMsg: str
        :param _ErrorLink: Error link.
        :type ErrorLink: str
        :param _ErrorLinkText: Error link text.
        :type ErrorLinkText: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DocBizId = None
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._RequestId = None

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def ErrorMsg(self):
        """Import error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        """Error link.
        :rtype: str
        """
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        """Error link text.
        :rtype: str
        """
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

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
        self._DocBizId = params.get("DocBizId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._RequestId = params.get("RequestId")


class SearchRange(AbstractModel):
    """Retrieval range configuration.

    """

    def __init__(self):
        r"""
        :param _Condition: Search criteria and/or.
        :type Condition: str
        :param _ApiVarAttrInfos: Custom variable and label relational data.
        :type ApiVarAttrInfos: list of ApiVarAttrInfo
        """
        self._Condition = None
        self._ApiVarAttrInfos = None

    @property
    def Condition(self):
        """Search criteria and/or.
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ApiVarAttrInfos(self):
        """Custom variable and label relational data.
        :rtype: list of ApiVarAttrInfo
        """
        return self._ApiVarAttrInfos

    @ApiVarAttrInfos.setter
    def ApiVarAttrInfos(self, ApiVarAttrInfos):
        self._ApiVarAttrInfos = ApiVarAttrInfos


    def _deserialize(self, params):
        self._Condition = params.get("Condition")
        if params.get("ApiVarAttrInfos") is not None:
            self._ApiVarAttrInfos = []
            for item in params.get("ApiVarAttrInfos"):
                obj = ApiVarAttrInfo()
                obj._deserialize(item)
                self._ApiVarAttrInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchStrategy(AbstractModel):
    """Knowledge library retrieval strategy.

    """

    def __init__(self):
        r"""
        :param _StrategyType: Retrieval strategy type, 0: hybrid retrieval; 1: semantic retrieval.
        :type StrategyType: int
        :param _TableEnhancement: Excel retrieval enhancement switch.
        :type TableEnhancement: bool
        """
        self._StrategyType = None
        self._TableEnhancement = None

    @property
    def StrategyType(self):
        """Retrieval strategy type, 0: hybrid retrieval; 1: semantic retrieval.
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def TableEnhancement(self):
        """Excel retrieval enhancement switch.
        :rtype: bool
        """
        return self._TableEnhancement

    @TableEnhancement.setter
    def TableEnhancement(self, TableEnhancement):
        self._TableEnhancement = TableEnhancement


    def _deserialize(self, params):
        self._StrategyType = params.get("StrategyType")
        self._TableEnhancement = params.get("TableEnhancement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarQuestion(AbstractModel):
    """Similar question information.

    """

    def __init__(self):
        r"""
        :param _SimBizId: Similar question ID.
        :type SimBizId: str
        :param _Question: Similar question content.
        :type Question: str
        :param _AuditStatus: Similar question review status, 1: audit failure.
        :type AuditStatus: int
        """
        self._SimBizId = None
        self._Question = None
        self._AuditStatus = None

    @property
    def SimBizId(self):
        """Similar question ID.
        :rtype: str
        """
        return self._SimBizId

    @SimBizId.setter
    def SimBizId(self, SimBizId):
        self._SimBizId = SimBizId

    @property
    def Question(self):
        """Similar question content.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def AuditStatus(self):
        """Similar question review status, 1: audit failure.
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus


    def _deserialize(self, params):
        self._SimBizId = params.get("SimBizId")
        self._Question = params.get("Question")
        self._AuditStatus = params.get("AuditStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarQuestionModify(AbstractModel):
    """Similar question modification (update) information.

    """

    def __init__(self):
        r"""
        :param _AddQuestions: List of similar questions (content) to be added.
        :type AddQuestions: list of str
        :param _UpdateQuestions: List of similar questions to be updated.
        :type UpdateQuestions: list of SimilarQuestion
        :param _DeleteQuestions: List of similar questions to be deleted.
        :type DeleteQuestions: list of SimilarQuestion
        """
        self._AddQuestions = None
        self._UpdateQuestions = None
        self._DeleteQuestions = None

    @property
    def AddQuestions(self):
        """List of similar questions (content) to be added.
        :rtype: list of str
        """
        return self._AddQuestions

    @AddQuestions.setter
    def AddQuestions(self, AddQuestions):
        self._AddQuestions = AddQuestions

    @property
    def UpdateQuestions(self):
        """List of similar questions to be updated.
        :rtype: list of SimilarQuestion
        """
        return self._UpdateQuestions

    @UpdateQuestions.setter
    def UpdateQuestions(self, UpdateQuestions):
        self._UpdateQuestions = UpdateQuestions

    @property
    def DeleteQuestions(self):
        """List of similar questions to be deleted.
        :rtype: list of SimilarQuestion
        """
        return self._DeleteQuestions

    @DeleteQuestions.setter
    def DeleteQuestions(self, DeleteQuestions):
        self._DeleteQuestions = DeleteQuestions


    def _deserialize(self, params):
        self._AddQuestions = params.get("AddQuestions")
        if params.get("UpdateQuestions") is not None:
            self._UpdateQuestions = []
            for item in params.get("UpdateQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._UpdateQuestions.append(obj)
        if params.get("DeleteQuestions") is not None:
            self._DeleteQuestions = []
            for item in params.get("DeleteQuestions"):
                obj = SimilarQuestion()
                obj._deserialize(item)
                self._DeleteQuestions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Stat(AbstractModel):
    """Billing statistical information.

    """

    def __init__(self):
        r"""
        :param _X: X-axis: time zone; return three interval ranges of "minute/hour/day" according to the granularity of the query condition.
        :type X: str
        :param _Y: Y-axis: statistical values in this time period, such as token consumption, call count, or usage information.
        :type Y: float
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        """X-axis: time zone; return three interval ranges of "minute/hour/day" according to the granularity of the query condition.
        :rtype: str
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """Y-axis: statistical values in this time period, such as token consumption, call count, or usage information.
        :rtype: float
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
        


class StatisticInfo(AbstractModel):
    """Statistical information of large model tokens.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model name.
        :type ModelName: str
        :param _FirstTokenCost: Time consumption of the first token.
        :type FirstTokenCost: int
        :param _TotalCost: Total time consumption.
        :type TotalCost: int
        :param _InputTokens: Number of input tokens.
        :type InputTokens: int
        :param _OutputTokens: Number of output tokens.
        :type OutputTokens: int
        :param _TotalTokens: Total number of tokens.
        :type TotalTokens: int
        """
        self._ModelName = None
        self._FirstTokenCost = None
        self._TotalCost = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def ModelName(self):
        """Model name.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def FirstTokenCost(self):
        """Time consumption of the first token.
        :rtype: int
        """
        return self._FirstTokenCost

    @FirstTokenCost.setter
    def FirstTokenCost(self, FirstTokenCost):
        self._FirstTokenCost = FirstTokenCost

    @property
    def TotalCost(self):
        """Total time consumption.
        :rtype: int
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def InputTokens(self):
        """Number of input tokens.
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        """Number of output tokens.
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        """Total number of tokens.
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._FirstTokenCost = params.get("FirstTokenCost")
        self._TotalCost = params.get("TotalCost")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDocParseRequest(AbstractModel):
    """StopDocParse request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _DocBizId: Document ID.
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        """Document ID.
        :rtype: str
        """
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDocParseResponse(AbstractModel):
    """StopDocParse response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StrValue(AbstractModel):
    """String KV information.

    """

    def __init__(self):
        r"""
        :param _Name: Name.
        :type Name: str
        :param _Value: Value.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Value.
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
        


class SummaryConfig(AbstractModel):
    """Knowledge summary application configuration.

    """

    def __init__(self):
        r"""
        :param _Model: Model configuration.
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Output: Knowledge summary output configuration.
        :type Output: :class:`tencentcloud.lke.v20231130.models.SummaryOutput`
        :param _Greeting: Welcome words, within 200 characters.
        :type Greeting: str
        """
        self._Model = None
        self._Output = None
        self._Greeting = None

    @property
    def Model(self):
        """Model configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.AppModel`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Output(self):
        """Knowledge summary output configuration.
        :rtype: :class:`tencentcloud.lke.v20231130.models.SummaryOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Greeting(self):
        """Welcome words, within 200 characters.
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Output") is not None:
            self._Output = SummaryOutput()
            self._Output._deserialize(params.get("Output"))
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryOutput(AbstractModel):
    """Knowledge summary output configuration.

    """

    def __init__(self):
        r"""
        :param _Method: Output method: 1. streaming; 2. non-streaming.
        :type Method: int
        :param _Requirement: Output requirement 1: text summary. 2: customized requirement.
        :type Requirement: int
        :param _RequireCommand: Custom requirement command.
        :type RequireCommand: str
        """
        self._Method = None
        self._Requirement = None
        self._RequireCommand = None

    @property
    def Method(self):
        """Output method: 1. streaming; 2. non-streaming.
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Requirement(self):
        """Output requirement 1: text summary. 2: customized requirement.
        :rtype: int
        """
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def RequireCommand(self):
        """Custom requirement command.
        :rtype: str
        """
        return self._RequireCommand

    @RequireCommand.setter
    def RequireCommand(self, RequireCommand):
        self._RequireCommand = RequireCommand


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Requirement = params.get("Requirement")
        self._RequireCommand = params.get("RequireCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowInfo(AbstractModel):
    """Task process information.

    """

    def __init__(self):
        r"""
        :param _TaskFlowId: Task flow ID.
        :type TaskFlowId: str
        :param _TaskFlowName: Task flow name.
        :type TaskFlowName: str
        :param _QueryRewrite: Rewrite results of query.
        :type QueryRewrite: str
        :param _HitIntent: Hit intent.
        :type HitIntent: str
        :param _Type: Task flow response type.
0: Task flow response.
1: Silent task flow.
2: Pull back script of workflow.
3: Custom response of task flow.
        :type Type: int
        """
        self._TaskFlowId = None
        self._TaskFlowName = None
        self._QueryRewrite = None
        self._HitIntent = None
        self._Type = None

    @property
    def TaskFlowId(self):
        """Task flow ID.
        :rtype: str
        """
        return self._TaskFlowId

    @TaskFlowId.setter
    def TaskFlowId(self, TaskFlowId):
        self._TaskFlowId = TaskFlowId

    @property
    def TaskFlowName(self):
        """Task flow name.
        :rtype: str
        """
        return self._TaskFlowName

    @TaskFlowName.setter
    def TaskFlowName(self, TaskFlowName):
        self._TaskFlowName = TaskFlowName

    @property
    def QueryRewrite(self):
        """Rewrite results of query.
        :rtype: str
        """
        return self._QueryRewrite

    @QueryRewrite.setter
    def QueryRewrite(self, QueryRewrite):
        self._QueryRewrite = QueryRewrite

    @property
    def HitIntent(self):
        """Hit intent.
        :rtype: str
        """
        return self._HitIntent

    @HitIntent.setter
    def HitIntent(self, HitIntent):
        self._HitIntent = HitIntent

    @property
    def Type(self):
        """Task flow response type.
0: Task flow response.
1: Silent task flow.
2: Pull back script of workflow.
3: Custom response of task flow.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TaskFlowId = params.get("TaskFlowId")
        self._TaskFlowName = params.get("TaskFlowName")
        self._QueryRewrite = params.get("QueryRewrite")
        self._HitIntent = params.get("HitIntent")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowSummary(AbstractModel):
    """Task process debugging information.

    """

    def __init__(self):
        r"""
        :param _IntentName: Task flow name.
        :type IntentName: str
        :param _UpdatedSlotValues: Entity list.
        :type UpdatedSlotValues: list of ValueInfo
        :param _RunNodes: Node list.
        :type RunNodes: list of RunNodeInfo
        :param _Purposes: Intent determination.
        :type Purposes: list of str
        """
        self._IntentName = None
        self._UpdatedSlotValues = None
        self._RunNodes = None
        self._Purposes = None

    @property
    def IntentName(self):
        """Task flow name.
        :rtype: str
        """
        return self._IntentName

    @IntentName.setter
    def IntentName(self, IntentName):
        self._IntentName = IntentName

    @property
    def UpdatedSlotValues(self):
        """Entity list.
        :rtype: list of ValueInfo
        """
        return self._UpdatedSlotValues

    @UpdatedSlotValues.setter
    def UpdatedSlotValues(self, UpdatedSlotValues):
        self._UpdatedSlotValues = UpdatedSlotValues

    @property
    def RunNodes(self):
        """Node list.
        :rtype: list of RunNodeInfo
        """
        return self._RunNodes

    @RunNodes.setter
    def RunNodes(self, RunNodes):
        self._RunNodes = RunNodes

    @property
    def Purposes(self):
        """Intent determination.
        :rtype: list of str
        """
        return self._Purposes

    @Purposes.setter
    def Purposes(self, Purposes):
        self._Purposes = Purposes


    def _deserialize(self, params):
        self._IntentName = params.get("IntentName")
        if params.get("UpdatedSlotValues") is not None:
            self._UpdatedSlotValues = []
            for item in params.get("UpdatedSlotValues"):
                obj = ValueInfo()
                obj._deserialize(item)
                self._UpdatedSlotValues.append(obj)
        if params.get("RunNodes") is not None:
            self._RunNodes = []
            for item in params.get("RunNodes"):
                obj = RunNodeInfo()
                obj._deserialize(item)
                self._RunNodes.append(obj)
        self._Purposes = params.get("Purposes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskParams(AbstractModel):
    """Task parameter.

    """

    def __init__(self):
        r"""
        :param _CosPath: Download address. Download through the COS bucket temporary key.
        :type CosPath: str
        """
        self._CosPath = None

    @property
    def CosPath(self):
        """Download address. Download through the COS bucket temporary key.
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath


    def _deserialize(self, params):
        self._CosPath = params.get("CosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenStat(AbstractModel):
    """Current executed token statistical information.

    """

    def __init__(self):
        r"""
        :param _SessionId: Session ID.
        :type SessionId: str
        :param _RequestId: Request ID.
        :type RequestId: str
        :param _RecordId: It corresponds to a session, session id, used for storing messages for answering. It can be generated in advance, used when saving messages.
        :type RecordId: str
        :param _UsedCount: Number of consumed tokens.
        :type UsedCount: int
        :param _FreeCount: Number of free tokens.
        :type FreeCount: int
        :param _OrderCount: Total number of tokens for orders.
        :type OrderCount: int
        :param _StatusSummary: Current execution status summary. Constant: processing, success., failed.
        :type StatusSummary: str
        :param _StatusSummaryTitle: Chinese display after summarizing the current execution status.
        :type StatusSummaryTitle: str
        :param _Elapsed: Current request execution time, in milliseconds.
        :type Elapsed: int
        :param _TokenCount: Number of tokens consumed by the current request.
        :type TokenCount: int
        :param _Procedures: Execution information.
        :type Procedures: list of Procedure
        :param _TraceId: Execution process information TraceId.
        :type TraceId: str
        """
        self._SessionId = None
        self._RequestId = None
        self._RecordId = None
        self._UsedCount = None
        self._FreeCount = None
        self._OrderCount = None
        self._StatusSummary = None
        self._StatusSummaryTitle = None
        self._Elapsed = None
        self._TokenCount = None
        self._Procedures = None
        self._TraceId = None

    @property
    def SessionId(self):
        """Session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        """Request ID.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RecordId(self):
        """It corresponds to a session, session id, used for storing messages for answering. It can be generated in advance, used when saving messages.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def UsedCount(self):
        """Number of consumed tokens.
        :rtype: int
        """
        return self._UsedCount

    @UsedCount.setter
    def UsedCount(self, UsedCount):
        self._UsedCount = UsedCount

    @property
    def FreeCount(self):
        """Number of free tokens.
        :rtype: int
        """
        return self._FreeCount

    @FreeCount.setter
    def FreeCount(self, FreeCount):
        self._FreeCount = FreeCount

    @property
    def OrderCount(self):
        """Total number of tokens for orders.
        :rtype: int
        """
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def StatusSummary(self):
        """Current execution status summary. Constant: processing, success., failed.
        :rtype: str
        """
        return self._StatusSummary

    @StatusSummary.setter
    def StatusSummary(self, StatusSummary):
        self._StatusSummary = StatusSummary

    @property
    def StatusSummaryTitle(self):
        """Chinese display after summarizing the current execution status.
        :rtype: str
        """
        return self._StatusSummaryTitle

    @StatusSummaryTitle.setter
    def StatusSummaryTitle(self, StatusSummaryTitle):
        self._StatusSummaryTitle = StatusSummaryTitle

    @property
    def Elapsed(self):
        """Current request execution time, in milliseconds.
        :rtype: int
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def TokenCount(self):
        """Number of tokens consumed by the current request.
        :rtype: int
        """
        return self._TokenCount

    @TokenCount.setter
    def TokenCount(self, TokenCount):
        self._TokenCount = TokenCount

    @property
    def Procedures(self):
        """Execution information.
        :rtype: list of Procedure
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TraceId(self):
        """Execution process information TraceId.
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")
        self._RecordId = params.get("RecordId")
        self._UsedCount = params.get("UsedCount")
        self._FreeCount = params.get("FreeCount")
        self._OrderCount = params.get("OrderCount")
        self._StatusSummary = params.get("StatusSummary")
        self._StatusSummaryTitle = params.get("StatusSummaryTitle")
        self._Elapsed = params.get("Elapsed")
        self._TokenCount = params.get("TokenCount")
        if params.get("Procedures") is not None:
            self._Procedures = []
            for item in params.get("Procedures"):
                obj = Procedure()
                obj._deserialize(item)
                self._Procedures.append(obj)
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnsatisfiedReply(AbstractModel):
    """Unsatisfied response.

    """

    def __init__(self):
        r"""
        :param _ReplyBizId: Unsatisfied response ID.
        :type ReplyBizId: str
        :param _RecordBizId: Message record ID.
        :type RecordBizId: str
        :param _Question: User question.
        :type Question: str
        :param _Answer: Application response.
        :type Answer: str
        :param _Reasons: Error type.
        :type Reasons: list of str
        """
        self._ReplyBizId = None
        self._RecordBizId = None
        self._Question = None
        self._Answer = None
        self._Reasons = None

    @property
    def ReplyBizId(self):
        """Unsatisfied response ID.
        :rtype: str
        """
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def RecordBizId(self):
        """Message record ID.
        :rtype: str
        """
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def Question(self):
        """User question.
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """Application response.
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Reasons(self):
        """Error type.
        :rtype: list of str
        """
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._ReplyBizId = params.get("ReplyBizId")
        self._RecordBizId = params.get("RecordBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAttributeLabelRequest(AbstractModel):
    """UploadAttributeLabel request structure.

    """

    def __init__(self):
        r"""
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _FileName: Filename.
        :type FileName: str
        :param _CosUrl: Cos path.
        :type CosUrl: str
        :param _CosHash: Verify the consistency of files uploaded to the cloud and local files by validating the crc64 encoding in the x-cos-hash-crc64ecma header.
        :type CosHash: str
        :param _Size: File size.
        :type Size: str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._FileName = None
        self._CosUrl = None
        self._CosHash = None
        self._Size = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        """Filename.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CosUrl(self):
        """Cos path.
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def CosHash(self):
        """Verify the consistency of files uploaded to the cloud and local files by validating the crc64 encoding in the x-cos-hash-crc64ecma header.
        :rtype: str
        """
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        """File size.
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._CosUrl = params.get("CosUrl")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAttributeLabelResponse(AbstractModel):
    """UploadAttributeLabel response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Import error.
        :type ErrorMsg: str
        :param _ErrorLink: Error link.
        :type ErrorLink: str
        :param _ErrorLinkText: Error link text.
        :type ErrorLinkText: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """Import error.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        """Error link.
        :rtype: str
        """
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        """Error link text.
        :rtype: str
        """
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._RequestId = params.get("RequestId")


class ValueInfo(AbstractModel):
    """Task flow parameter information.

    """

    def __init__(self):
        r"""
        :param _Id: Value ID.
        :type Id: str
        :param _Name: Name.
        :type Name: str
        :param _ValueType: Value type, 0: unknown or empty; 1: string; 2: integer; 3: float; 4: boolean; 5: array (string array); 6: object_array (structure array); 7: object (structure).
        :type ValueType: int
        :param _ValueStr: String.
        :type ValueStr: str
        :param _ValueInt: Int (return as a string to avoid precision loss).
        :type ValueInt: str
        :param _ValueFloat: Float.
        :type ValueFloat: float
        :param _ValueBool: Bool.
        :type ValueBool: bool
        :param _ValueStrArray: Array.
        :type ValueStrArray: list of str
        """
        self._Id = None
        self._Name = None
        self._ValueType = None
        self._ValueStr = None
        self._ValueInt = None
        self._ValueFloat = None
        self._ValueBool = None
        self._ValueStrArray = None

    @property
    def Id(self):
        """Value ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ValueType(self):
        """Value type, 0: unknown or empty; 1: string; 2: integer; 3: float; 4: boolean; 5: array (string array); 6: object_array (structure array); 7: object (structure).
        :rtype: int
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ValueStr(self):
        """String.
        :rtype: str
        """
        return self._ValueStr

    @ValueStr.setter
    def ValueStr(self, ValueStr):
        self._ValueStr = ValueStr

    @property
    def ValueInt(self):
        """Int (return as a string to avoid precision loss).
        :rtype: str
        """
        return self._ValueInt

    @ValueInt.setter
    def ValueInt(self, ValueInt):
        self._ValueInt = ValueInt

    @property
    def ValueFloat(self):
        """Float.
        :rtype: float
        """
        return self._ValueFloat

    @ValueFloat.setter
    def ValueFloat(self, ValueFloat):
        self._ValueFloat = ValueFloat

    @property
    def ValueBool(self):
        """Bool.
        :rtype: bool
        """
        return self._ValueBool

    @ValueBool.setter
    def ValueBool(self, ValueBool):
        self._ValueBool = ValueBool

    @property
    def ValueStrArray(self):
        """Array.
        :rtype: list of str
        """
        return self._ValueStrArray

    @ValueStrArray.setter
    def ValueStrArray(self, ValueStrArray):
        self._ValueStrArray = ValueStrArray


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ValueType = params.get("ValueType")
        self._ValueStr = params.get("ValueStr")
        self._ValueInt = params.get("ValueInt")
        self._ValueFloat = params.get("ValueFloat")
        self._ValueBool = params.get("ValueBool")
        self._ValueStrArray = params.get("ValueStrArray")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQARequest(AbstractModel):
    """VerifyQA request structure.

    """

    def __init__(self):
        r"""
        :param _List: Q&A list.
        :type List: list of QAList
        :param _BotBizId: Application ID.
        :type BotBizId: str
        :param _LoginUin: Login to user's root account (required in integrator mode).
        :type LoginUin: str
        :param _LoginSubAccountUin: Login to user's sub-account (required in integrator mode).
        :type LoginSubAccountUin: str
        """
        self._List = None
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def List(self):
        """Q&A list.
        :rtype: list of QAList
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def BotBizId(self):
        """Application ID.
        :rtype: str
        """
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        """Login to user's root account (required in integrator mode).
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        """Login to user's sub-account (required in integrator mode).
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QAList()
                obj._deserialize(item)
                self._List.append(obj)
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQAResponse(AbstractModel):
    """VerifyQA response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class VoiceConfig(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _VoiceType: 
        :type VoiceType: int
        :param _TimbreKey: 
        :type TimbreKey: str
        :param _VoiceName: 
        :type VoiceName: str
        """
        self._VoiceType = None
        self._TimbreKey = None
        self._VoiceName = None

    @property
    def VoiceType(self):
        """
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def TimbreKey(self):
        """
        :rtype: str
        """
        return self._TimbreKey

    @TimbreKey.setter
    def TimbreKey(self, TimbreKey):
        self._TimbreKey = TimbreKey

    @property
    def VoiceName(self):
        """
        :rtype: str
        """
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName


    def _deserialize(self, params):
        self._VoiceType = params.get("VoiceType")
        self._TimbreKey = params.get("TimbreKey")
        self._VoiceName = params.get("VoiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkFlowSummary(AbstractModel):
    """Workflow debugging information.

    """

    def __init__(self):
        r"""
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _WorkflowRunId: Workflow running ID.
        :type WorkflowRunId: str
        :param _RunNodes: Node information.
        :type RunNodes: list of WorkflowRunNodeInfo
        :param _OptionCards: Tab.
        :type OptionCards: list of str
        :param _Outputs: Output results of multiple bubbles.
        :type Outputs: list of str
        :param _WorkflowReleaseTime: Workflow release time, Unix timestamp.
        :type WorkflowReleaseTime: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowRunId = None
        self._RunNodes = None
        self._OptionCards = None
        self._Outputs = None
        self._WorkflowReleaseTime = None

    @property
    def WorkflowId(self):
        """Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        """Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowRunId(self):
        """Workflow running ID.
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def RunNodes(self):
        """Node information.
        :rtype: list of WorkflowRunNodeInfo
        """
        return self._RunNodes

    @RunNodes.setter
    def RunNodes(self, RunNodes):
        self._RunNodes = RunNodes

    @property
    def OptionCards(self):
        """Tab.
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def Outputs(self):
        """Output results of multiple bubbles.
        :rtype: list of str
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def WorkflowReleaseTime(self):
        """Workflow release time, Unix timestamp.
        :rtype: str
        """
        return self._WorkflowReleaseTime

    @WorkflowReleaseTime.setter
    def WorkflowReleaseTime(self, WorkflowReleaseTime):
        self._WorkflowReleaseTime = WorkflowReleaseTime


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowRunId = params.get("WorkflowRunId")
        if params.get("RunNodes") is not None:
            self._RunNodes = []
            for item in params.get("RunNodes"):
                obj = WorkflowRunNodeInfo()
                obj._deserialize(item)
                self._RunNodes.append(obj)
        self._OptionCards = params.get("OptionCards")
        self._Outputs = params.get("Outputs")
        self._WorkflowReleaseTime = params.get("WorkflowReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 
        :type WorkflowId: str
        :param _WorkflowName: 
        :type WorkflowName: str
        :param _WorkflowRunId: 
        :type WorkflowRunId: str
        :param _OptionCards: 
        :type OptionCards: list of str
        :param _Outputs: 
        :type Outputs: list of str
        :param _WorkflowReleaseTime: 
        :type WorkflowReleaseTime: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowRunId = None
        self._OptionCards = None
        self._Outputs = None
        self._WorkflowReleaseTime = None

    @property
    def WorkflowId(self):
        """
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        """
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowRunId(self):
        """
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId

    @property
    def OptionCards(self):
        """
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def Outputs(self):
        """
        :rtype: list of str
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def WorkflowReleaseTime(self):
        """
        :rtype: str
        """
        return self._WorkflowReleaseTime

    @WorkflowReleaseTime.setter
    def WorkflowReleaseTime(self, WorkflowReleaseTime):
        self._WorkflowReleaseTime = WorkflowReleaseTime


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowRunId = params.get("WorkflowRunId")
        self._OptionCards = params.get("OptionCards")
        self._Outputs = params.get("Outputs")
        self._WorkflowReleaseTime = params.get("WorkflowReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowRunNodeInfo(AbstractModel):
    """Workflow running node information.

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID.
        :type NodeId: str
        :param _NodeType: Node type.
        :type NodeType: int
        :param _NodeName: Node name.
        :type NodeName: str
        :param _Status: Status.
        :type Status: int
        :param _Input: Input..
        :type Input: str
        :param _Output: Output.
        :type Output: str
        :param _TaskOutput: Task output.
        :type TaskOutput: str
        :param _FailMessage: Error message.
        :type FailMessage: str
        :param _CostMilliSeconds: Time consumption.
        :type CostMilliSeconds: int
        :param _StatisticInfos: Large model output information.
        :type StatisticInfos: list of StatisticInfo
        """
        self._NodeId = None
        self._NodeType = None
        self._NodeName = None
        self._Status = None
        self._Input = None
        self._Output = None
        self._TaskOutput = None
        self._FailMessage = None
        self._CostMilliSeconds = None
        self._StatisticInfos = None

    @property
    def NodeId(self):
        """Node ID.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeType(self):
        """Node type.
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeName(self):
        """Node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Status(self):
        """Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        """Input..
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        """Output.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def TaskOutput(self):
        """Task output.
        :rtype: str
        """
        return self._TaskOutput

    @TaskOutput.setter
    def TaskOutput(self, TaskOutput):
        self._TaskOutput = TaskOutput

    @property
    def FailMessage(self):
        """Error message.
        :rtype: str
        """
        return self._FailMessage

    @FailMessage.setter
    def FailMessage(self, FailMessage):
        self._FailMessage = FailMessage

    @property
    def CostMilliSeconds(self):
        """Time consumption.
        :rtype: int
        """
        return self._CostMilliSeconds

    @CostMilliSeconds.setter
    def CostMilliSeconds(self, CostMilliSeconds):
        self._CostMilliSeconds = CostMilliSeconds

    @property
    def StatisticInfos(self):
        """Large model output information.
        :rtype: list of StatisticInfo
        """
        return self._StatisticInfos

    @StatisticInfos.setter
    def StatisticInfos(self, StatisticInfos):
        self._StatisticInfos = StatisticInfos


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeType = params.get("NodeType")
        self._NodeName = params.get("NodeName")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._TaskOutput = params.get("TaskOutput")
        self._FailMessage = params.get("FailMessage")
        self._CostMilliSeconds = params.get("CostMilliSeconds")
        if params.get("StatisticInfos") is not None:
            self._StatisticInfos = []
            for item in params.get("StatisticInfos"):
                obj = StatisticInfo()
                obj._deserialize(item)
                self._StatisticInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        