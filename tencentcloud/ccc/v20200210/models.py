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


class AICallExtractConfigElement(AbstractModel):
    """AI call extraction configuration item.

    """

    def __init__(self):
        r"""
        :param _InfoType: Configuration item type, including.
Text.
Selector option.
Boolean value.
Number.
        :type InfoType: str
        :param _InfoName: Configuration item name, duplicat.
        :type InfoName: str
        :param _InfoContent: Specific content of the configuration item.
        :type InfoContent: str
        :param _Examples: Example of extracted content from the configuration item.
        :type Examples: list of str
        :param _Choices: When infotype is selector, this field needs to be configured.
        :type Choices: list of str
        """
        self._InfoType = None
        self._InfoName = None
        self._InfoContent = None
        self._Examples = None
        self._Choices = None

    @property
    def InfoType(self):
        """Configuration item type, including.
Text.
Selector option.
Boolean value.
Number.
        :rtype: str
        """
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def InfoName(self):
        """Configuration item name, duplicat.
        :rtype: str
        """
        return self._InfoName

    @InfoName.setter
    def InfoName(self, InfoName):
        self._InfoName = InfoName

    @property
    def InfoContent(self):
        """Specific content of the configuration item.
        :rtype: str
        """
        return self._InfoContent

    @InfoContent.setter
    def InfoContent(self, InfoContent):
        self._InfoContent = InfoContent

    @property
    def Examples(self):
        """Example of extracted content from the configuration item.
        :rtype: list of str
        """
        return self._Examples

    @Examples.setter
    def Examples(self, Examples):
        self._Examples = Examples

    @property
    def Choices(self):
        """When infotype is selector, this field needs to be configured.
        :rtype: list of str
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices


    def _deserialize(self, params):
        self._InfoType = params.get("InfoType")
        self._InfoName = params.get("InfoName")
        self._InfoContent = params.get("InfoContent")
        self._Examples = params.get("Examples")
        self._Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AICallExtractResultElement(AbstractModel):
    """AI call extraction result.

    """

    def __init__(self):
        r"""
        :param _InfoType: Type of extracted information.
Text.
Selector options.
Boolean value.
Number.
        :type InfoType: str
        :param _InfoName: Name of the extracted information.
        :type InfoName: str
        :param _InfoContent: Specific description of the extracted information.
        :type InfoContent: str
        :param _Result: Specific result of the extracted information.
        :type Result: :class:`tencentcloud.ccc.v20200210.models.AICallExtractResultInfo`
        """
        self._InfoType = None
        self._InfoName = None
        self._InfoContent = None
        self._Result = None

    @property
    def InfoType(self):
        """Type of extracted information.
Text.
Selector options.
Boolean value.
Number.
        :rtype: str
        """
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def InfoName(self):
        """Name of the extracted information.
        :rtype: str
        """
        return self._InfoName

    @InfoName.setter
    def InfoName(self, InfoName):
        self._InfoName = InfoName

    @property
    def InfoContent(self):
        """Specific description of the extracted information.
        :rtype: str
        """
        return self._InfoContent

    @InfoContent.setter
    def InfoContent(self, InfoContent):
        self._InfoContent = InfoContent

    @property
    def Result(self):
        """Specific result of the extracted information.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AICallExtractResultInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._InfoType = params.get("InfoType")
        self._InfoName = params.get("InfoName")
        self._InfoContent = params.get("InfoContent")
        if params.get("Result") is not None:
            self._Result = AICallExtractResultInfo()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AICallExtractResultInfo(AbstractModel):
    """Specific information of AI call result.

    """

    def __init__(self):
        r"""
        :param _Text: The extracted type is text.
        :type Text: str
        :param _Chosen: The extracted type is option.
        :type Chosen: list of str
        :param _Boolean: The extracted type is a boolean value.
        :type Boolean: bool
        :param _Number: The extracted type is a number.
        :type Number: float
        """
        self._Text = None
        self._Chosen = None
        self._Boolean = None
        self._Number = None

    @property
    def Text(self):
        """The extracted type is text.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Chosen(self):
        """The extracted type is option.
        :rtype: list of str
        """
        return self._Chosen

    @Chosen.setter
    def Chosen(self, Chosen):
        self._Chosen = Chosen

    @property
    def Boolean(self):
        """The extracted type is a boolean value.
        :rtype: bool
        """
        return self._Boolean

    @Boolean.setter
    def Boolean(self, Boolean):
        self._Boolean = Boolean

    @property
    def Number(self):
        """The extracted type is a number.
        :rtype: float
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Chosen = params.get("Chosen")
        self._Boolean = params.get("Boolean")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITransferItem(AbstractModel):
    """AI to human configuration item.

    """

    def __init__(self):
        r"""
        :param _TransferFunctionName: Name of the function calling for transfer to human.
        :type TransferFunctionName: str
        :param _TransferFunctionDesc: Takes effect when transferfunctionenable is true; the description of transfer_to_human function calling defaults to "transfer to human when the user has to transfer to human (like says transfer to human) or you are instructed to do so.".
        :type TransferFunctionDesc: str
        :param _TransferSkillGroupId: Skill group id for transferring to human agent.
        :type TransferSkillGroupId: int
        """
        self._TransferFunctionName = None
        self._TransferFunctionDesc = None
        self._TransferSkillGroupId = None

    @property
    def TransferFunctionName(self):
        """Name of the function calling for transfer to human.
        :rtype: str
        """
        return self._TransferFunctionName

    @TransferFunctionName.setter
    def TransferFunctionName(self, TransferFunctionName):
        self._TransferFunctionName = TransferFunctionName

    @property
    def TransferFunctionDesc(self):
        """Takes effect when transferfunctionenable is true; the description of transfer_to_human function calling defaults to "transfer to human when the user has to transfer to human (like says transfer to human) or you are instructed to do so.".
        :rtype: str
        """
        return self._TransferFunctionDesc

    @TransferFunctionDesc.setter
    def TransferFunctionDesc(self, TransferFunctionDesc):
        self._TransferFunctionDesc = TransferFunctionDesc

    @property
    def TransferSkillGroupId(self):
        """Skill group id for transferring to human agent.
        :rtype: int
        """
        return self._TransferSkillGroupId

    @TransferSkillGroupId.setter
    def TransferSkillGroupId(self, TransferSkillGroupId):
        self._TransferSkillGroupId = TransferSkillGroupId


    def _deserialize(self, params):
        self._TransferFunctionName = params.get("TransferFunctionName")
        self._TransferFunctionDesc = params.get("TransferFunctionDesc")
        self._TransferSkillGroupId = params.get("TransferSkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortAgentCruiseDialingCampaignRequest(AbstractModel):
    """AbortAgentCruiseDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: <Task id>.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """<Task id>.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortAgentCruiseDialingCampaignResponse(AbstractModel):
    """AbortAgentCruiseDialingCampaign response structure.

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


class AbortPredictiveDialingCampaignRequest(AbstractModel):
    """AbortPredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: Task id.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """Task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortPredictiveDialingCampaignResponse(AbstractModel):
    """AbortPredictiveDialingCampaign response structure.

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


class AsrData(AbstractModel):
    """Speech-to-text information

    """

    def __init__(self):
        r"""
        :param _User: User side.
        :type User: str
        :param _Message: Message content.
        :type Message: str
        :param _Timestamp: Timestamp.
        :type Timestamp: int
        :param _Start: Sentence start time, unix millisecond timestamp.
        :type Start: int
        :param _End: Sentence end time, unix millisecond timestamp.
        :type End: int
        """
        self._User = None
        self._Message = None
        self._Timestamp = None
        self._Start = None
        self._End = None

    @property
    def User(self):
        """User side.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Message(self):
        """Message content.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Timestamp(self):
        warnings.warn("parameter `Timestamp` is deprecated", DeprecationWarning) 

        """Timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        warnings.warn("parameter `Timestamp` is deprecated", DeprecationWarning) 

        self._Timestamp = Timestamp

    @property
    def Start(self):
        """Sentence start time, unix millisecond timestamp.
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        """Sentence end time, unix millisecond timestamp.
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Message = params.get("Message")
        self._Timestamp = params.get("Timestamp")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioFileInfo(AbstractModel):
    """Audio file review information

    """

    def __init__(self):
        r"""
        :param _FileId: File id.
        :type FileId: int
        :param _CustomFileName: File alias.
        :type CustomFileName: str
        :param _AudioFileName: Filename.
        :type AudioFileName: str
        :param _Status: Review status: 0 - unreviewed, 1 - approved, 2 - rejected.
        :type Status: int
        """
        self._FileId = None
        self._CustomFileName = None
        self._AudioFileName = None
        self._Status = None

    @property
    def FileId(self):
        """File id.
        :rtype: int
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def CustomFileName(self):
        """File alias.
        :rtype: str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioFileName(self):
        """Filename.
        :rtype: str
        """
        return self._AudioFileName

    @AudioFileName.setter
    def AudioFileName(self, AudioFileName):
        self._AudioFileName = AudioFileName

    @property
    def Status(self):
        """Review status: 0 - unreviewed, 1 - approved, 2 - rejected.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._CustomFileName = params.get("CustomFileName")
        self._AudioFileName = params.get("AudioFileName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskCalleeInfo(AbstractModel):
    """Outbound call task called information.

    """

    def __init__(self):
        r"""
        :param _Callee: Called number.
        :type Callee: str
        :param _State: Call status 0 - initial, 1 - answered, 2 - unanswered, 3 - calling, 4 - pending retry.
        :type State: int
        :param _Sessions: List of session ids.
        :type Sessions: list of str
        """
        self._Callee = None
        self._State = None
        self._Sessions = None

    @property
    def Callee(self):
        """Called number.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def State(self):
        """Call status 0 - initial, 1 - answered, 2 - unanswered, 3 - calling, 4 - pending retry.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Sessions(self):
        """List of session ids.
        :rtype: list of str
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._State = params.get("State")
        self._Sessions = params.get("Sessions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoCalloutTaskInfo(AbstractModel):
    """Automatic outbound call task list item.

    """

    def __init__(self):
        r"""
        :param _Name: Task name.
        :type Name: str
        :param _CalleeCount: Number of called parties.
        :type CalleeCount: int
        :param _Callers: List of calling numbers.
        :type Callers: list of str
        :param _NotBefore: Start timestamp.
        :type NotBefore: int
        :param _NotAfter: End timestamp
.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotAfter: int
        :param _IvrId: IvrId used by the task.
        :type IvrId: int
        :param _State: Task status:.
0 initial: task creation, call not started.
1 running.
2 completed: all calls in the task are completed.
3 ending: the task has expired, but there are still some calls not ended.
4 ended: task terminated due to expiration.
        :type State: int
        :param _TaskId: <Task id>.
        :type TaskId: int
        """
        self._Name = None
        self._CalleeCount = None
        self._Callers = None
        self._NotBefore = None
        self._NotAfter = None
        self._IvrId = None
        self._State = None
        self._TaskId = None

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CalleeCount(self):
        """Number of called parties.
        :rtype: int
        """
        return self._CalleeCount

    @CalleeCount.setter
    def CalleeCount(self, CalleeCount):
        self._CalleeCount = CalleeCount

    @property
    def Callers(self):
        """List of calling numbers.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def NotBefore(self):
        """Start timestamp.
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        """End timestamp
.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def IvrId(self):
        """IvrId used by the task.
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        """Task status:.
0 initial: task creation, call not started.
1 running.
2 completed: all calls in the task are completed.
3 ending: the task has expired, but there are still some calls not ended.
4 ended: task terminated due to expiration.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TaskId(self):
        """<Task id>.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CalleeCount = params.get("CalleeCount")
        self._Callers = params.get("Callers")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupRequest(AbstractModel):
    """BindNumberCallOutSkillGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Number: Number to be bound.
        :type Number: str
        :param _SkillGroupIds: Skill group id list to be bound.
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        """Number to be bound.
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        """Skill group id list to be bound.
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNumberCallOutSkillGroupResponse(AbstractModel):
    """BindNumberCallOutSkillGroup response structure.

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


class BindStaffSkillGroupListRequest(AbstractModel):
    """BindStaffSkillGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _StaffEmail: Agent email.
        :type StaffEmail: str
        :param _SkillGroupList: Bound skill group list.
        :type SkillGroupList: list of int
        :param _StaffSkillGroupList: Bound skill group list (required).
        :type StaffSkillGroupList: list of StaffSkillGroupList
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None
        self._StaffSkillGroupList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        """Agent email.
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        warnings.warn("parameter `SkillGroupList` is deprecated", DeprecationWarning) 

        """Bound skill group list.
        :rtype: list of int
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        warnings.warn("parameter `SkillGroupList` is deprecated", DeprecationWarning) 

        self._SkillGroupList = SkillGroupList

    @property
    def StaffSkillGroupList(self):
        """Bound skill group list (required).
        :rtype: list of StaffSkillGroupList
        """
        return self._StaffSkillGroupList

    @StaffSkillGroupList.setter
    def StaffSkillGroupList(self, StaffSkillGroupList):
        self._StaffSkillGroupList = StaffSkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        if params.get("StaffSkillGroupList") is not None:
            self._StaffSkillGroupList = []
            for item in params.get("StaffSkillGroupList"):
                obj = StaffSkillGroupList()
                obj._deserialize(item)
                self._StaffSkillGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindStaffSkillGroupListResponse(AbstractModel):
    """BindStaffSkillGroupList response structure.

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


class CallInMetrics(AbstractModel):
    """Real-Time inbound metric.

    """

    def __init__(self):
        r"""
        :param _IvrCount: Number of ivr residency.
        :type IvrCount: int
        :param _QueueCount: Number in queue.
        :type QueueCount: int
        :param _RingCount: Number in ringing.
        :type RingCount: int
        :param _AcceptCount: Number of connections.
        :type AcceptCount: int
        :param _TransferOuterCount: Number of customer service transferring to the external line.
        :type TransferOuterCount: int
        :param _MaxQueueDuration: Maximum queue duration.
        :type MaxQueueDuration: int
        :param _AvgQueueDuration: Average queue duration.
        :type AvgQueueDuration: int
        :param _MaxRingDuration: Maximum ringing duration.
        :type MaxRingDuration: int
        :param _AvgRingDuration: Average ringing duration.
        :type AvgRingDuration: int
        :param _MaxAcceptDuration: Maximum connection duration.
        :type MaxAcceptDuration: int
        :param _AvgAcceptDuration: Average connection duration.
        :type AvgAcceptDuration: int
        """
        self._IvrCount = None
        self._QueueCount = None
        self._RingCount = None
        self._AcceptCount = None
        self._TransferOuterCount = None
        self._MaxQueueDuration = None
        self._AvgQueueDuration = None
        self._MaxRingDuration = None
        self._AvgRingDuration = None
        self._MaxAcceptDuration = None
        self._AvgAcceptDuration = None

    @property
    def IvrCount(self):
        """Number of ivr residency.
        :rtype: int
        """
        return self._IvrCount

    @IvrCount.setter
    def IvrCount(self, IvrCount):
        self._IvrCount = IvrCount

    @property
    def QueueCount(self):
        """Number in queue.
        :rtype: int
        """
        return self._QueueCount

    @QueueCount.setter
    def QueueCount(self, QueueCount):
        self._QueueCount = QueueCount

    @property
    def RingCount(self):
        """Number in ringing.
        :rtype: int
        """
        return self._RingCount

    @RingCount.setter
    def RingCount(self, RingCount):
        self._RingCount = RingCount

    @property
    def AcceptCount(self):
        """Number of connections.
        :rtype: int
        """
        return self._AcceptCount

    @AcceptCount.setter
    def AcceptCount(self, AcceptCount):
        self._AcceptCount = AcceptCount

    @property
    def TransferOuterCount(self):
        """Number of customer service transferring to the external line.
        :rtype: int
        """
        return self._TransferOuterCount

    @TransferOuterCount.setter
    def TransferOuterCount(self, TransferOuterCount):
        self._TransferOuterCount = TransferOuterCount

    @property
    def MaxQueueDuration(self):
        """Maximum queue duration.
        :rtype: int
        """
        return self._MaxQueueDuration

    @MaxQueueDuration.setter
    def MaxQueueDuration(self, MaxQueueDuration):
        self._MaxQueueDuration = MaxQueueDuration

    @property
    def AvgQueueDuration(self):
        """Average queue duration.
        :rtype: int
        """
        return self._AvgQueueDuration

    @AvgQueueDuration.setter
    def AvgQueueDuration(self, AvgQueueDuration):
        self._AvgQueueDuration = AvgQueueDuration

    @property
    def MaxRingDuration(self):
        """Maximum ringing duration.
        :rtype: int
        """
        return self._MaxRingDuration

    @MaxRingDuration.setter
    def MaxRingDuration(self, MaxRingDuration):
        self._MaxRingDuration = MaxRingDuration

    @property
    def AvgRingDuration(self):
        """Average ringing duration.
        :rtype: int
        """
        return self._AvgRingDuration

    @AvgRingDuration.setter
    def AvgRingDuration(self, AvgRingDuration):
        self._AvgRingDuration = AvgRingDuration

    @property
    def MaxAcceptDuration(self):
        """Maximum connection duration.
        :rtype: int
        """
        return self._MaxAcceptDuration

    @MaxAcceptDuration.setter
    def MaxAcceptDuration(self, MaxAcceptDuration):
        self._MaxAcceptDuration = MaxAcceptDuration

    @property
    def AvgAcceptDuration(self):
        """Average connection duration.
        :rtype: int
        """
        return self._AvgAcceptDuration

    @AvgAcceptDuration.setter
    def AvgAcceptDuration(self, AvgAcceptDuration):
        self._AvgAcceptDuration = AvgAcceptDuration


    def _deserialize(self, params):
        self._IvrCount = params.get("IvrCount")
        self._QueueCount = params.get("QueueCount")
        self._RingCount = params.get("RingCount")
        self._AcceptCount = params.get("AcceptCount")
        self._TransferOuterCount = params.get("TransferOuterCount")
        self._MaxQueueDuration = params.get("MaxQueueDuration")
        self._AvgQueueDuration = params.get("AvgQueueDuration")
        self._MaxRingDuration = params.get("MaxRingDuration")
        self._AvgRingDuration = params.get("AvgRingDuration")
        self._MaxAcceptDuration = params.get("MaxAcceptDuration")
        self._AvgAcceptDuration = params.get("AvgAcceptDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInNumberMetrics(AbstractModel):
    """Inbound line dimension metrics.

    """

    def __init__(self):
        r"""
        :param _Number: Line number.
        :type Number: str
        :param _Metrics: Line-Related metrics.
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _SkillGroupMetrics: Bound skill group metrics.
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        """
        self._Number = None
        self._Metrics = None
        self._SkillGroupMetrics = None

    @property
    def Number(self):
        """Line number.
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Metrics(self):
        """Line-Related metrics.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def SkillGroupMetrics(self):
        """Bound skill group metrics.
        :rtype: list of CallInSkillGroupMetrics
        """
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics


    def _deserialize(self, params):
        self._Number = params.get("Number")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInSkillGroupMetrics(AbstractModel):
    """Inbound capability group metrics.

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _Metrics: Data metrics.
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _Name: Skill group name.
        :type Name: str
        """
        self._SkillGroupId = None
        self._Metrics = None
        self._Name = None

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Metrics(self):
        """Data metrics.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Name(self):
        """Skill group name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        if params.get("Metrics") is not None:
            self._Metrics = CallInMetrics()
            self._Metrics._deserialize(params.get("Metrics"))
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CalleeAttribute(AbstractModel):
    """Property of the called.

    """

    def __init__(self):
        r"""
        :param _Callee: Called number.
        :type Callee: str
        :param _UUI: Accompanying data.
        :type UUI: str
        :param _Variables: Parameter.
        :type Variables: list of Variable
        """
        self._Callee = None
        self._UUI = None
        self._Variables = None

    @property
    def Callee(self):
        """Called number.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def UUI(self):
        """Accompanying data.
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def Variables(self):
        """Parameter.
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables


    def _deserialize(self, params):
        self._Callee = params.get("Callee")
        self._UUI = params.get("UUI")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAgentCallRequest(AbstractModel):
    """CreateAIAgentCall request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _AIAgentId: AI agent id.
        :type AIAgentId: int
        :param _Callee: Callee number.
        :type Callee: str
        :param _Callers: Caller number list
        :type Callers: list of str
        :param _PromptVariables: Prompt variable.
        :type PromptVariables: list of Variable
        """
        self._SdkAppId = None
        self._AIAgentId = None
        self._Callee = None
        self._Callers = None
        self._PromptVariables = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AIAgentId(self):
        """AI agent id.
        :rtype: int
        """
        return self._AIAgentId

    @AIAgentId.setter
    def AIAgentId(self, AIAgentId):
        self._AIAgentId = AIAgentId

    @property
    def Callee(self):
        """Callee number.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Callers(self):
        """Caller number list
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def PromptVariables(self):
        warnings.warn("parameter `PromptVariables` is deprecated", DeprecationWarning) 

        """Prompt variable.
        :rtype: list of Variable
        """
        return self._PromptVariables

    @PromptVariables.setter
    def PromptVariables(self, PromptVariables):
        warnings.warn("parameter `PromptVariables` is deprecated", DeprecationWarning) 

        self._PromptVariables = PromptVariables


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AIAgentId = params.get("AIAgentId")
        self._Callee = params.get("Callee")
        self._Callers = params.get("Callers")
        if params.get("PromptVariables") is not None:
            self._PromptVariables = []
            for item in params.get("PromptVariables"):
                obj = Variable()
                obj._deserialize(item)
                self._PromptVariables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAgentCallResponse(AbstractModel):
    """CreateAIAgentCall response structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: Newly created session id.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """Newly created session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateAICallRequest(AbstractModel):
    """CreateAICall request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application ID (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Callee: Called number.
        :type Callee: str
        :param _LLMType: Model interface protocol types, currently compatible with three protocol types:

- OpenAI protocol (including GPT, DeepSeek, etc.):"openai"
- Azure protocol:"azure"
- Minimax protocol:"minimax"
        :type LLMType: str
        :param _APIKey: Model API key, for authentication information, please refer to the respective model's official website

- OpenAI protocol: [GPT](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key), [DeepSeek](https://api-docs.deepseek.com/zh-cn/);

- Azure protocol: [Azure GPT](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ctypescript%2Cpython-new&pivots=programming-language-studio#key-settings);

- Minimax:[Minimax](https://platform.minimaxi.com/document/Fast%20access?key=66701cf51d57f38758d581b2)
        :type APIKey: str
        :param _APIUrl: Model interface address

- OpenAI protocol
GPT:"https://api.openai.com/v1/"
Deepseek:"https://api.deepseek.com/v1"

- Azure protocol
 "https://{your-resource-name}.openai.azure.com?api-version={api-version}"

- Minimax protocol
"https://api.minimax.chat/v1"
        :type APIUrl: str
        :param _SystemPrompt: ## Identity
You are Kate from the appointment department at Retell Health calling Cindy over the phone to prepare for the annual checkup coming up. You are a pleasant and friendly receptionist caring deeply for the user. You don't provide medical advice but would use the medical knowledge to understand user responses.

## Style Guardrails
Be Concise: Respond succinctly, addressing one topic at most.
Embrace Variety: Use diverse language and rephrasing to enhance clarity without repeating content.
Be Conversational: Use everyday language, making the chat feel like talking to a friend.
Be Proactive: Lead the conversation, often wrapping up with a question or next-step suggestion.
Avoid multiple questions in a single response.
Get clarity: If the user only partially answers a question, or if the answer is unclear, keep asking to get clarity.
Use a colloquial way of referring to the date (like Friday, January 14th, or Tuesday, January 12th, 2024 at 8am).

## Response Guideline
Adapt and Guess: Try to understand transcripts that may contain transcription errors. Avoid mentioning "transcription error" in the response.
Stay in Character: Keep conversations within your role's scope, guiding them back creatively without repeating.
Ensure Fluid Dialogue: Respond in a role-appropriate, direct manner to maintain a smooth conversation flow.

## Task
You will follow the steps below, do not skip steps, and only ask up to one question in response.
If at any time the user showed anger or wanted a human agent, call transfer_call to transfer to a human representative.
1. Begin with a self-introduction and verify if callee is Cindy.
  - if callee is not Cindy, call end_call to hang up, say sorry for the confusion when hanging up.
  - if Cindy is not available, call end_call politely to hang up, say you will call back later when hanging up.
2. Inform Cindy she has an annual body check coming up on April 4th, 2024 at 10am PDT. Check if Cindy is available.
  - If not, tell Cindy to reschedule online and jump to step 5.
3. Ask Cindy if there's anything that the doctor should know before the annual checkup.
  - Ask followup questions as needed to assess the severity of the issue, and understand how it has progressed.
4. Tell Cindy to not eat or drink that day before the checkup. Also tell Cindy to give you a callback if there's any changes in health condition.
5. Ask Cindy if she has any questions, and if so, answer them until there are no questions.
  - If user asks something you do not know, let them know you don't have the answer. Ask them if they have any other questions.
  - If user do not have any questions, call function end_call to hang up.
        :type SystemPrompt: str
        :param _Model: Model name, such as

- OpenAI protocol
"gpt-4o-mini","gpt-4o","deepseek-chat";

- Azure protocol
"gpt-4o-mini", "gpt-4o";

- Minimax protocol
"deepseek-chat".
        :type Model: str
        :param _VoiceType: The following voice parameter values are available by default. If you wish to customize the voice type, please leave VoiceType blank and configure it in the CustomTTSConfig parameter.

Chinese:
ZhiMei: Zhimei, customer service female voice
ZhiXi: Zhixi, general female voice
ZhiQi: Zhiqi, customer service female voice
ZhiTian: Zhitian, female child voice
AiXiaoJing: Ai Xiaojing, dialogue female voice

English:
WeRose:English Female Voice
Monika:English Female Voice

Japanese:
Nanami

Korean:
SunHi

Indonesian (Indonesia):
Gadis

Malay (Malaysia):
Yasmin

 Tamil (Malaysia):
Kani

Thai (Thailand):
Achara

Vietnamese (Vietnam):
HoaiMy


        :type VoiceType: str
        :param _Callers: Caller number list
        :type Callers: list of str
        :param _WelcomeMessage: Used to set the AI Agent Welcome Message.
        :type WelcomeMessage: str
        :param _WelcomeType: 0: Use welcomeMessage (if empty, the callee speaks first; if not empty, the bot speaks first)
1:   Use AI to automatically generate welcomeMessage and speak first based on the prompt
        :type WelcomeType: int
        :param _WelcomeMessagePriority: 0: interruptible by default, 1: high priority and not interruptible.
        :type WelcomeMessagePriority: int
        :param _MaxDuration: Maximum Waiting Duration (milliseconds), default is 60 seconds, if the user does not speak within this time, the call is automatically terminated
        :type MaxDuration: int
        :param _Languages: ASR Supported Languages, default is "zh" Chinese,
Fill in the array with up to 4 languages, the first is the primary language for recognition, followed by optional languages,
Note: When the primary language is a Chinese dialect, optional languages are invalid
Currently, the supported languages are as follows. The English name of the language is on the left side of the equals sign, and the value to be filled in the Language field is on the right side, following ISO639:
1. Chinese = "zh" # Chinese
2. Chinese_TW = "zh-TW" # Taiwan (China)
3. Chinese_DIALECT = "zh-dialect" # Chinese Dialect
4. English = "en" # English
5. Vietnamese = "vi" # Vietnamese
6. Japanese = "ja" # Japanese
7. Korean = "ko" # Korean
8. Indonesia = "id" # Indonesian
9. Thai = "th" # Thai
10. Portuguese = "pt" # Portuguese
11. Turkish = "tr" # Turkish
12. Arabic = "ar" # Arabic
13. Spanish = "es" # Spanish
14. Hindi = "hi" # Hindi
15. French = "fr" # French
16. Malay = "ms" # Malay
17. Filipino = "fil" # Filipino
18. German = "de" # German
19. Italian = "it" # Italian
20. Russian = "ru" # Russian
        :type Languages: list of str
        :param _InterruptMode: Interrupt ai speaking mode. default is 0. 0 indicates automatic interruption and 1 indicates no interruption.
        :type InterruptMode: int
        :param _InterruptSpeechDuration: Used when InterruptMode is 0, unit in milliseconds, default is 500ms. It means that the server-side detects ongoing vocal input for the InterruptSpeechDuration milliseconds and then interrupts.
        :type InterruptSpeechDuration: int
        :param _EndFunctionEnable: Whether the model supports (or enables) call_end function calling
        :type EndFunctionEnable: bool
        :param _EndFunctionDesc: Effective when EndFunctionEnable is true; the description of call_end function calling, default is "End the call when user has to leave (like says bye) or you are instructed to do so."
        :type EndFunctionDesc: str
        :param _TransferFunctionEnable: Whether the model supports (or enables) transfer_to_human function calling.
        :type TransferFunctionEnable: bool
        :param _TransferItems: Takes effect when transferfunctionenable is true: transfer to human configuration.
        :type TransferItems: list of AITransferItem
        :param _NotifyDuration: The duration after which the user hasn't spoken to trigger a notification, minimum 10 seconds, default 10 seconds
        :type NotifyDuration: int
        :param _NotifyMessage: The AI prompt when NotifyDuration has passed without the user speaking, default is "Sorry, I didn't hear you clearly. Can you repeat that?"
        :type NotifyMessage: str
        :param _NotifyMaxCount: Maximum number of times to trigger ai prompt sound, unlimited by default.
        :type NotifyMaxCount: int
        :param _CustomTTSConfig: <p>And VoiceType field needs to select one, here is to use your own custom TTS, VoiceType is some built-in sound qualities</p>
<ul>
<li>Tencent TTS<br>
For configuration, please refer to <a href="https://intl.cloud.tencent.com/document/product/1073/92668?from_cn_redirect=1#55924b56-1a73-4663-a7a1-a8dd82d6e823" target="_blank">Tencent Cloud TTS documentation link</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;tencent&quot;, // String TTS type, currently supports &quot;tencent&quot; and "minixmax", other vendors support in progress
    &quot;AppId&quot;: &quot;Your application ID&quot;, // String required
    &quot;SecretId&quot;: &quot;Your Secret ID&quot;, // String Required
    &quot;SecretKey&quot;:  &quot;Your Secret Key&quot;, // String Required
    &quot;VoiceType&quot;: 101001, // Integer Required, Sound quality ID, includes standard and premium sound quality. Premium sound quality is more realistic and differently priced than standard sound quality. See TTS billing overview for details. For the full list of sound quality IDs, see the TTS sound quality list.
    "Speed": 1.25, // Integer Optional, speech speed, range: [-2,6], corresponding to different speeds: -2: represents 0.6x -1: represents 0.8x 0: represents 1.0x (default) 1: represents 1.2x 2: represents 1.5x 6: represents 2.5x For more precise speed control, you can retain two decimal places, such as 0.5/1.25/2.81, etc. For parameter value to actual speed conversion, refer to Speed Conversion
    &quot;Volume&quot;: 5, // Integer Optional, Volume level, range: [0,10], corresponding to 11 levels of volume, default is 0, which represents normal volume.
    &quot;PrimaryLanguage&quot;: 1, // Integer Optional, Primary language 1- Chinese (default) 2- English 3- Japanese
    &quot;FastVoiceType&quot;: &quot;xxxx&quot;   // Optional parameter, Fast VRS parameter
  }
</code></pre>

  </div></div><ul>

</div></div><ul>
<li>Azure TTS<br>
For configuration, refer to the<a href="https://docs.azure.cn/zh-cn/ai-services/speech-service/speech-synthesis-markup-voice" target="_blank">Azure TTS documentation</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;azure&quot;, // Required: String TTS type
    &quot;SubscriptionKey&quot;: &quot;xxxxxxxx&quot;, // Required: String subscription key
    &quot;Region&quot;: &quot;chinanorth3&quot;,  // Required: String subscription region
    &quot;VoiceName&quot;: &quot;zh-CN-XiaoxiaoNeural&quot;, // Required: String Timbre Name required
    &quot;Language&quot;: &quot;zh-CN&quot;, // Required: String Language for synthesis
    &quot;Rate&quot;: 1 // Optional: float Playback Speed 0.5-2 default is 1
}
</code></pre>

</div></div><ul>
<li>Custom</li>
</ul>
<p>TTS<br>
Please refer to the specific protocol standards in the <a href="https://doc.weixin.qq.com/doc/w3_ANQAiAbdAFwHILbJBmtSqSbV1WZ3L?scode=AJEAIQdfAAo5a1xajYANQAiAbdAFw" target="_blank">Tencent documentation</a></p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
  &quot;TTSType&quot;: &quot;custom&quot;, // Required String
  &quot;APIKey&quot;: &quot;ApiKey&quot;, // Required String for Authentication
  &quot;APIUrl&quot;: &quot;http://0.0.0.0:8080/stream-audio&quot; // Required String, TTS API URL
  &quot;AudioFormat&quot;: &quot;wav&quot;, // String, optional, expected audio format, such as mp3, ogg_opus, pcm, wav, default is wav, currently only pcm and wav are supported,
  &quot;SampleRate&quot;: 16000,  // Integer, optional, audio sample rate, default is 16000 (16k), recommended value is 16000
  &quot;AudioChannel&quot;: 1,    // Integer, optional, number of audio channels, values: 1 or 2, default is 1
}
</code></pre>

</div></div>
        :type CustomTTSConfig: str
        :param _PromptVariables: Prompt word variable.
        :type PromptVariables: list of Variable
        :param _VadSilenceTime: Automatic speech recognition vad time ranges from 240 to 2000, with a default of 1000, measured in milliseconds. smaller values will make automatic speech recognition segment faster.
        :type VadSilenceTime: int
        :param _ExtractConfig: Call content extraction configuration.
        :type ExtractConfig: list of AICallExtractConfigElement
        """
        self._SdkAppId = None
        self._Callee = None
        self._LLMType = None
        self._APIKey = None
        self._APIUrl = None
        self._SystemPrompt = None
        self._Model = None
        self._VoiceType = None
        self._Callers = None
        self._WelcomeMessage = None
        self._WelcomeType = None
        self._WelcomeMessagePriority = None
        self._MaxDuration = None
        self._Languages = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._EndFunctionEnable = None
        self._EndFunctionDesc = None
        self._TransferFunctionEnable = None
        self._TransferItems = None
        self._NotifyDuration = None
        self._NotifyMessage = None
        self._NotifyMaxCount = None
        self._CustomTTSConfig = None
        self._PromptVariables = None
        self._VadSilenceTime = None
        self._ExtractConfig = None

    @property
    def SdkAppId(self):
        """Application ID (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callee(self):
        """Called number.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def LLMType(self):
        """Model interface protocol types, currently compatible with three protocol types:

- OpenAI protocol (including GPT, DeepSeek, etc.):"openai"
- Azure protocol:"azure"
- Minimax protocol:"minimax"
        :rtype: str
        """
        return self._LLMType

    @LLMType.setter
    def LLMType(self, LLMType):
        self._LLMType = LLMType

    @property
    def APIKey(self):
        """Model API key, for authentication information, please refer to the respective model's official website

- OpenAI protocol: [GPT](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key), [DeepSeek](https://api-docs.deepseek.com/zh-cn/);

- Azure protocol: [Azure GPT](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ctypescript%2Cpython-new&pivots=programming-language-studio#key-settings);

- Minimax:[Minimax](https://platform.minimaxi.com/document/Fast%20access?key=66701cf51d57f38758d581b2)
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        self._APIKey = APIKey

    @property
    def APIUrl(self):
        """Model interface address

- OpenAI protocol
GPT:"https://api.openai.com/v1/"
Deepseek:"https://api.deepseek.com/v1"

- Azure protocol
 "https://{your-resource-name}.openai.azure.com?api-version={api-version}"

- Minimax protocol
"https://api.minimax.chat/v1"
        :rtype: str
        """
        return self._APIUrl

    @APIUrl.setter
    def APIUrl(self, APIUrl):
        self._APIUrl = APIUrl

    @property
    def SystemPrompt(self):
        """## Identity
You are Kate from the appointment department at Retell Health calling Cindy over the phone to prepare for the annual checkup coming up. You are a pleasant and friendly receptionist caring deeply for the user. You don't provide medical advice but would use the medical knowledge to understand user responses.

## Style Guardrails
Be Concise: Respond succinctly, addressing one topic at most.
Embrace Variety: Use diverse language and rephrasing to enhance clarity without repeating content.
Be Conversational: Use everyday language, making the chat feel like talking to a friend.
Be Proactive: Lead the conversation, often wrapping up with a question or next-step suggestion.
Avoid multiple questions in a single response.
Get clarity: If the user only partially answers a question, or if the answer is unclear, keep asking to get clarity.
Use a colloquial way of referring to the date (like Friday, January 14th, or Tuesday, January 12th, 2024 at 8am).

## Response Guideline
Adapt and Guess: Try to understand transcripts that may contain transcription errors. Avoid mentioning "transcription error" in the response.
Stay in Character: Keep conversations within your role's scope, guiding them back creatively without repeating.
Ensure Fluid Dialogue: Respond in a role-appropriate, direct manner to maintain a smooth conversation flow.

## Task
You will follow the steps below, do not skip steps, and only ask up to one question in response.
If at any time the user showed anger or wanted a human agent, call transfer_call to transfer to a human representative.
1. Begin with a self-introduction and verify if callee is Cindy.
  - if callee is not Cindy, call end_call to hang up, say sorry for the confusion when hanging up.
  - if Cindy is not available, call end_call politely to hang up, say you will call back later when hanging up.
2. Inform Cindy she has an annual body check coming up on April 4th, 2024 at 10am PDT. Check if Cindy is available.
  - If not, tell Cindy to reschedule online and jump to step 5.
3. Ask Cindy if there's anything that the doctor should know before the annual checkup.
  - Ask followup questions as needed to assess the severity of the issue, and understand how it has progressed.
4. Tell Cindy to not eat or drink that day before the checkup. Also tell Cindy to give you a callback if there's any changes in health condition.
5. Ask Cindy if she has any questions, and if so, answer them until there are no questions.
  - If user asks something you do not know, let them know you don't have the answer. Ask them if they have any other questions.
  - If user do not have any questions, call function end_call to hang up.
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt

    @property
    def Model(self):
        """Model name, such as

- OpenAI protocol
"gpt-4o-mini","gpt-4o","deepseek-chat";

- Azure protocol
"gpt-4o-mini", "gpt-4o";

- Minimax protocol
"deepseek-chat".
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VoiceType(self):
        """The following voice parameter values are available by default. If you wish to customize the voice type, please leave VoiceType blank and configure it in the CustomTTSConfig parameter.

Chinese:
ZhiMei: Zhimei, customer service female voice
ZhiXi: Zhixi, general female voice
ZhiQi: Zhiqi, customer service female voice
ZhiTian: Zhitian, female child voice
AiXiaoJing: Ai Xiaojing, dialogue female voice

English:
WeRose:English Female Voice
Monika:English Female Voice

Japanese:
Nanami

Korean:
SunHi

Indonesian (Indonesia):
Gadis

Malay (Malaysia):
Yasmin

 Tamil (Malaysia):
Kani

Thai (Thailand):
Achara

Vietnamese (Vietnam):
HoaiMy


        :rtype: str
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def Callers(self):
        """Caller number list
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def WelcomeMessage(self):
        """Used to set the AI Agent Welcome Message.
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def WelcomeType(self):
        """0: Use welcomeMessage (if empty, the callee speaks first; if not empty, the bot speaks first)
1:   Use AI to automatically generate welcomeMessage and speak first based on the prompt
        :rtype: int
        """
        return self._WelcomeType

    @WelcomeType.setter
    def WelcomeType(self, WelcomeType):
        self._WelcomeType = WelcomeType

    @property
    def WelcomeMessagePriority(self):
        """0: interruptible by default, 1: high priority and not interruptible.
        :rtype: int
        """
        return self._WelcomeMessagePriority

    @WelcomeMessagePriority.setter
    def WelcomeMessagePriority(self, WelcomeMessagePriority):
        self._WelcomeMessagePriority = WelcomeMessagePriority

    @property
    def MaxDuration(self):
        """Maximum Waiting Duration (milliseconds), default is 60 seconds, if the user does not speak within this time, the call is automatically terminated
        :rtype: int
        """
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Languages(self):
        """ASR Supported Languages, default is "zh" Chinese,
Fill in the array with up to 4 languages, the first is the primary language for recognition, followed by optional languages,
Note: When the primary language is a Chinese dialect, optional languages are invalid
Currently, the supported languages are as follows. The English name of the language is on the left side of the equals sign, and the value to be filled in the Language field is on the right side, following ISO639:
1. Chinese = "zh" # Chinese
2. Chinese_TW = "zh-TW" # Taiwan (China)
3. Chinese_DIALECT = "zh-dialect" # Chinese Dialect
4. English = "en" # English
5. Vietnamese = "vi" # Vietnamese
6. Japanese = "ja" # Japanese
7. Korean = "ko" # Korean
8. Indonesia = "id" # Indonesian
9. Thai = "th" # Thai
10. Portuguese = "pt" # Portuguese
11. Turkish = "tr" # Turkish
12. Arabic = "ar" # Arabic
13. Spanish = "es" # Spanish
14. Hindi = "hi" # Hindi
15. French = "fr" # French
16. Malay = "ms" # Malay
17. Filipino = "fil" # Filipino
18. German = "de" # German
19. Italian = "it" # Italian
20. Russian = "ru" # Russian
        :rtype: list of str
        """
        return self._Languages

    @Languages.setter
    def Languages(self, Languages):
        self._Languages = Languages

    @property
    def InterruptMode(self):
        """Interrupt ai speaking mode. default is 0. 0 indicates automatic interruption and 1 indicates no interruption.
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        """Used when InterruptMode is 0, unit in milliseconds, default is 500ms. It means that the server-side detects ongoing vocal input for the InterruptSpeechDuration milliseconds and then interrupts.
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def EndFunctionEnable(self):
        """Whether the model supports (or enables) call_end function calling
        :rtype: bool
        """
        return self._EndFunctionEnable

    @EndFunctionEnable.setter
    def EndFunctionEnable(self, EndFunctionEnable):
        self._EndFunctionEnable = EndFunctionEnable

    @property
    def EndFunctionDesc(self):
        """Effective when EndFunctionEnable is true; the description of call_end function calling, default is "End the call when user has to leave (like says bye) or you are instructed to do so."
        :rtype: str
        """
        return self._EndFunctionDesc

    @EndFunctionDesc.setter
    def EndFunctionDesc(self, EndFunctionDesc):
        self._EndFunctionDesc = EndFunctionDesc

    @property
    def TransferFunctionEnable(self):
        """Whether the model supports (or enables) transfer_to_human function calling.
        :rtype: bool
        """
        return self._TransferFunctionEnable

    @TransferFunctionEnable.setter
    def TransferFunctionEnable(self, TransferFunctionEnable):
        self._TransferFunctionEnable = TransferFunctionEnable

    @property
    def TransferItems(self):
        """Takes effect when transferfunctionenable is true: transfer to human configuration.
        :rtype: list of AITransferItem
        """
        return self._TransferItems

    @TransferItems.setter
    def TransferItems(self, TransferItems):
        self._TransferItems = TransferItems

    @property
    def NotifyDuration(self):
        """The duration after which the user hasn't spoken to trigger a notification, minimum 10 seconds, default 10 seconds
        :rtype: int
        """
        return self._NotifyDuration

    @NotifyDuration.setter
    def NotifyDuration(self, NotifyDuration):
        self._NotifyDuration = NotifyDuration

    @property
    def NotifyMessage(self):
        """The AI prompt when NotifyDuration has passed without the user speaking, default is "Sorry, I didn't hear you clearly. Can you repeat that?"
        :rtype: str
        """
        return self._NotifyMessage

    @NotifyMessage.setter
    def NotifyMessage(self, NotifyMessage):
        self._NotifyMessage = NotifyMessage

    @property
    def NotifyMaxCount(self):
        """Maximum number of times to trigger ai prompt sound, unlimited by default.
        :rtype: int
        """
        return self._NotifyMaxCount

    @NotifyMaxCount.setter
    def NotifyMaxCount(self, NotifyMaxCount):
        self._NotifyMaxCount = NotifyMaxCount

    @property
    def CustomTTSConfig(self):
        """<p>And VoiceType field needs to select one, here is to use your own custom TTS, VoiceType is some built-in sound qualities</p>
<ul>
<li>Tencent TTS<br>
For configuration, please refer to <a href="https://intl.cloud.tencent.com/document/product/1073/92668?from_cn_redirect=1#55924b56-1a73-4663-a7a1-a8dd82d6e823" target="_blank">Tencent Cloud TTS documentation link</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;tencent&quot;, // String TTS type, currently supports &quot;tencent&quot; and "minixmax", other vendors support in progress
    &quot;AppId&quot;: &quot;Your application ID&quot;, // String required
    &quot;SecretId&quot;: &quot;Your Secret ID&quot;, // String Required
    &quot;SecretKey&quot;:  &quot;Your Secret Key&quot;, // String Required
    &quot;VoiceType&quot;: 101001, // Integer Required, Sound quality ID, includes standard and premium sound quality. Premium sound quality is more realistic and differently priced than standard sound quality. See TTS billing overview for details. For the full list of sound quality IDs, see the TTS sound quality list.
    "Speed": 1.25, // Integer Optional, speech speed, range: [-2,6], corresponding to different speeds: -2: represents 0.6x -1: represents 0.8x 0: represents 1.0x (default) 1: represents 1.2x 2: represents 1.5x 6: represents 2.5x For more precise speed control, you can retain two decimal places, such as 0.5/1.25/2.81, etc. For parameter value to actual speed conversion, refer to Speed Conversion
    &quot;Volume&quot;: 5, // Integer Optional, Volume level, range: [0,10], corresponding to 11 levels of volume, default is 0, which represents normal volume.
    &quot;PrimaryLanguage&quot;: 1, // Integer Optional, Primary language 1- Chinese (default) 2- English 3- Japanese
    &quot;FastVoiceType&quot;: &quot;xxxx&quot;   // Optional parameter, Fast VRS parameter
  }
</code></pre>

  </div></div><ul>

</div></div><ul>
<li>Azure TTS<br>
For configuration, refer to the<a href="https://docs.azure.cn/zh-cn/ai-services/speech-service/speech-synthesis-markup-voice" target="_blank">Azure TTS documentation</a></li>
</ul>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
    &quot;TTSType&quot;: &quot;azure&quot;, // Required: String TTS type
    &quot;SubscriptionKey&quot;: &quot;xxxxxxxx&quot;, // Required: String subscription key
    &quot;Region&quot;: &quot;chinanorth3&quot;,  // Required: String subscription region
    &quot;VoiceName&quot;: &quot;zh-CN-XiaoxiaoNeural&quot;, // Required: String Timbre Name required
    &quot;Language&quot;: &quot;zh-CN&quot;, // Required: String Language for synthesis
    &quot;Rate&quot;: 1 // Optional: float Playback Speed 0.5-2 default is 1
}
</code></pre>

</div></div><ul>
<li>Custom</li>
</ul>
<p>TTS<br>
Please refer to the specific protocol standards in the <a href="https://doc.weixin.qq.com/doc/w3_ANQAiAbdAFwHILbJBmtSqSbV1WZ3L?scode=AJEAIQdfAAo5a1xajYANQAiAbdAFw" target="_blank">Tencent documentation</a></p>
<div><div class="v-md-pre-wrapper copy-code-mode v-md-pre-wrapper- extra-class"><pre class="v-md-prism-"><code>{
  &quot;TTSType&quot;: &quot;custom&quot;, // Required String
  &quot;APIKey&quot;: &quot;ApiKey&quot;, // Required String for Authentication
  &quot;APIUrl&quot;: &quot;http://0.0.0.0:8080/stream-audio&quot; // Required String, TTS API URL
  &quot;AudioFormat&quot;: &quot;wav&quot;, // String, optional, expected audio format, such as mp3, ogg_opus, pcm, wav, default is wav, currently only pcm and wav are supported,
  &quot;SampleRate&quot;: 16000,  // Integer, optional, audio sample rate, default is 16000 (16k), recommended value is 16000
  &quot;AudioChannel&quot;: 1,    // Integer, optional, number of audio channels, values: 1 or 2, default is 1
}
</code></pre>

</div></div>
        :rtype: str
        """
        return self._CustomTTSConfig

    @CustomTTSConfig.setter
    def CustomTTSConfig(self, CustomTTSConfig):
        self._CustomTTSConfig = CustomTTSConfig

    @property
    def PromptVariables(self):
        warnings.warn("parameter `PromptVariables` is deprecated", DeprecationWarning) 

        """Prompt word variable.
        :rtype: list of Variable
        """
        return self._PromptVariables

    @PromptVariables.setter
    def PromptVariables(self, PromptVariables):
        warnings.warn("parameter `PromptVariables` is deprecated", DeprecationWarning) 

        self._PromptVariables = PromptVariables

    @property
    def VadSilenceTime(self):
        """Automatic speech recognition vad time ranges from 240 to 2000, with a default of 1000, measured in milliseconds. smaller values will make automatic speech recognition segment faster.
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def ExtractConfig(self):
        """Call content extraction configuration.
        :rtype: list of AICallExtractConfigElement
        """
        return self._ExtractConfig

    @ExtractConfig.setter
    def ExtractConfig(self, ExtractConfig):
        self._ExtractConfig = ExtractConfig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callee = params.get("Callee")
        self._LLMType = params.get("LLMType")
        self._APIKey = params.get("APIKey")
        self._APIUrl = params.get("APIUrl")
        self._SystemPrompt = params.get("SystemPrompt")
        self._Model = params.get("Model")
        self._VoiceType = params.get("VoiceType")
        self._Callers = params.get("Callers")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._WelcomeType = params.get("WelcomeType")
        self._WelcomeMessagePriority = params.get("WelcomeMessagePriority")
        self._MaxDuration = params.get("MaxDuration")
        self._Languages = params.get("Languages")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._EndFunctionEnable = params.get("EndFunctionEnable")
        self._EndFunctionDesc = params.get("EndFunctionDesc")
        self._TransferFunctionEnable = params.get("TransferFunctionEnable")
        if params.get("TransferItems") is not None:
            self._TransferItems = []
            for item in params.get("TransferItems"):
                obj = AITransferItem()
                obj._deserialize(item)
                self._TransferItems.append(obj)
        self._NotifyDuration = params.get("NotifyDuration")
        self._NotifyMessage = params.get("NotifyMessage")
        self._NotifyMaxCount = params.get("NotifyMaxCount")
        self._CustomTTSConfig = params.get("CustomTTSConfig")
        if params.get("PromptVariables") is not None:
            self._PromptVariables = []
            for item in params.get("PromptVariables"):
                obj = Variable()
                obj._deserialize(item)
                self._PromptVariables.append(obj)
        self._VadSilenceTime = params.get("VadSilenceTime")
        if params.get("ExtractConfig") is not None:
            self._ExtractConfig = []
            for item in params.get("ExtractConfig"):
                obj = AICallExtractConfigElement()
                obj._deserialize(item)
                self._ExtractConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAICallResponse(AbstractModel):
    """CreateAICall response structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: Newly created session ID.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """Newly created session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateAdminURLRequest(AbstractModel):
    """CreateAdminURL request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SeatUserId: Admin account.
        :type SeatUserId: str
        """
        self._SdkAppId = None
        self._SeatUserId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SeatUserId(self):
        """Admin account.
        :rtype: str
        """
        return self._SeatUserId

    @SeatUserId.setter
    def SeatUserId(self, SeatUserId):
        self._SeatUserId = SeatUserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SeatUserId = params.get("SeatUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdminURLResponse(AbstractModel):
    """CreateAdminURL response structure.

    """

    def __init__(self):
        r"""
        :param _URL: Log-In link.
        :type URL: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._URL = None
        self._RequestId = None

    @property
    def URL(self):
        """Log-In link.
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

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
        self._URL = params.get("URL")
        self._RequestId = params.get("RequestId")


class CreateAgentCruiseDialingCampaignRequest(AbstractModel):
    """CreateAgentCruiseDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Name: Task name.
        :type Name: str
        :param _Agent: Agent account.
        :type Agent: str
        :param _ConcurrencyNumber: Single-Round concurrent call volume 1-20.
        :type ConcurrencyNumber: int
        :param _StartTime: Task start time. unix timestamp. the task will automatically start after this time.
        :type StartTime: int
        :param _EndTime: Task termination time. unix timestamp. the task will automatically terminate after this time.
        :type EndTime: int
        :param _Callees: Called list supporting e.164 or number formats without country code.
        :type Callees: list of str
        :param _Callers: Calling list using the number formats displayed on the management side.
        :type Callers: list of str
        :param _CallOrder: Being called sequence: 0 for random 1 for in order.
        :type CallOrder: int
        :param _UUI: Caller custom data, maximum length 1024.
        :type UUI: str
        """
        self._SdkAppId = None
        self._Name = None
        self._Agent = None
        self._ConcurrencyNumber = None
        self._StartTime = None
        self._EndTime = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Agent(self):
        """Agent account.
        :rtype: str
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ConcurrencyNumber(self):
        """Single-Round concurrent call volume 1-20.
        :rtype: int
        """
        return self._ConcurrencyNumber

    @ConcurrencyNumber.setter
    def ConcurrencyNumber(self, ConcurrencyNumber):
        self._ConcurrencyNumber = ConcurrencyNumber

    @property
    def StartTime(self):
        """Task start time. unix timestamp. the task will automatically start after this time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task termination time. unix timestamp. the task will automatically terminate after this time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Callees(self):
        """Called list supporting e.164 or number formats without country code.
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """Calling list using the number formats displayed on the management side.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """Being called sequence: 0 for random 1 for in order.
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def UUI(self):
        """Caller custom data, maximum length 1024.
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._Agent = params.get("Agent")
        self._ConcurrencyNumber = params.get("ConcurrencyNumber")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentCruiseDialingCampaignResponse(AbstractModel):
    """CreateAgentCruiseDialingCampaign response structure.

    """

    def __init__(self):
        r"""
        :param _CampaignId: Generated task id.
        :type CampaignId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CampaignId = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """Generated task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

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
        self._CampaignId = params.get("CampaignId")
        self._RequestId = params.get("RequestId")


class CreateAutoCalloutTaskRequest(AbstractModel):
    """CreateAutoCalloutTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _NotBefore: Task starting timestamp. unix second-level timestamp.
        :type NotBefore: int
        :param _Callees: List of called numbers.
        :type Callees: list of str
        :param _Callers: List of calling numbers.
        :type Callers: list of str
        :param _IvrId: IVR used for calling.
        :type IvrId: int
        :param _Name: Task name.
        :type Name: str
        :param _Description: <Task description>.
        :type Description: str
        :param _NotAfter: Task stop timestamp. unix second-level timestamp.
        :type NotAfter: int
        :param _Tries: Maximum attempts, 1-3 times.
        :type Tries: int
        :param _Variables: Custom variables (supported only in advanced versions).
        :type Variables: list of Variable
        :param _UUI: UUI
        :type UUI: str
        :param _CalleeAttributes: Property of the called.
        :type CalleeAttributes: list of CalleeAttribute
        """
        self._SdkAppId = None
        self._NotBefore = None
        self._Callees = None
        self._Callers = None
        self._IvrId = None
        self._Name = None
        self._Description = None
        self._NotAfter = None
        self._Tries = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def NotBefore(self):
        """Task starting timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def Callees(self):
        """List of called numbers.
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """List of calling numbers.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IvrId(self):
        """IVR used for calling.
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """<Task description>.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotAfter(self):
        """Task stop timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Tries(self):
        """Maximum attempts, 1-3 times.
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def Variables(self):
        """Custom variables (supported only in advanced versions).
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """Property of the called.
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._NotBefore = params.get("NotBefore")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._IvrId = params.get("IvrId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotAfter = params.get("NotAfter")
        self._Tries = params.get("Tries")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoCalloutTaskResponse(AbstractModel):
    """CreateAutoCalloutTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task id.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Task id.
        :rtype: int
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


class CreateCCCSkillGroupRequest(AbstractModel):
    """CreateCCCSkillGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SkillGroupName: Skill group name.
        :type SkillGroupName: str
        :param _SkillGroupType: Skill group type 0-cell phone, 1-online, 3-audio, 4-video.
        :type SkillGroupType: int
        :param _MaxConcurrency: The maximum number of people received by the skill group (the maximum number of people that one agent in this skill group can receive) is set to 1 by default. if the skill group type is online, the maximum can be set to one or more.
2. if the skill group type is phone, audio, or video, then the reception limit must be 1.
        :type MaxConcurrency: int
        """
        self._SdkAppId = None
        self._SkillGroupName = None
        self._SkillGroupType = None
        self._MaxConcurrency = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SkillGroupName(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def SkillGroupType(self):
        """Skill group type 0-cell phone, 1-online, 3-audio, 4-video.
        :rtype: int
        """
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType

    @property
    def MaxConcurrency(self):
        """The maximum number of people received by the skill group (the maximum number of people that one agent in this skill group can receive) is set to 1 by default. if the skill group type is online, the maximum can be set to one or more.
2. if the skill group type is phone, audio, or video, then the reception limit must be 1.
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._SkillGroupType = params.get("SkillGroupType")
        self._MaxConcurrency = params.get("MaxConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCCSkillGroupResponse(AbstractModel):
    """CreateCCCSkillGroup response structure.

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SkillGroupId = None
        self._RequestId = None

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

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
        self._SkillGroupId = params.get("SkillGroupId")
        self._RequestId = params.get("RequestId")


class CreateCallOutSessionRequest(AbstractModel):
    """CreateCallOutSession request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id.
        :type SdkAppId: int
        :param _UserId: Customer service user id usually refers to the customer service email.
        :type UserId: str
        :param _Callee: Called number must be preceded by 0086.
        :type Callee: str
        :param _Caller: Caller number (obsolete one and use callers) must be preceded by 0086.
        :type Caller: str
        :param _Callers: Designated caller number list. if the prior number fails, it will automatically switch to the next number that must be preceded by 0086.
        :type Callers: list of str
        :param _IsForceUseMobile: Whether to force the use of cell phone outbound call or not, currently only supports true, if true, please ensure that the allowlist has been configured.
        :type IsForceUseMobile: bool
        :param _Uui: Custom data, length limited to 1024 bytes.
        :type Uui: str
        :param _UUI: Custom data, length limited to 1024 bytes.
        :type UUI: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Callee = None
        self._Caller = None
        self._Callers = None
        self._IsForceUseMobile = None
        self._Uui = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """Application id.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        """Customer service user id usually refers to the customer service email.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Callee(self):
        """Called number must be preceded by 0086.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Caller(self):
        """Caller number (obsolete one and use callers) must be preceded by 0086.
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callers(self):
        """Designated caller number list. if the prior number fails, it will automatically switch to the next number that must be preceded by 0086.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def IsForceUseMobile(self):
        """Whether to force the use of cell phone outbound call or not, currently only supports true, if true, please ensure that the allowlist has been configured.
        :rtype: bool
        """
        return self._IsForceUseMobile

    @IsForceUseMobile.setter
    def IsForceUseMobile(self, IsForceUseMobile):
        self._IsForceUseMobile = IsForceUseMobile

    @property
    def Uui(self):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        """Custom data, length limited to 1024 bytes.
        :rtype: str
        """
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        self._Uui = Uui

    @property
    def UUI(self):
        """Custom data, length limited to 1024 bytes.
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Callee = params.get("Callee")
        self._Caller = params.get("Caller")
        self._Callers = params.get("Callers")
        self._IsForceUseMobile = params.get("IsForceUseMobile")
        self._Uui = params.get("Uui")
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCallOutSessionResponse(AbstractModel):
    """CreateCallOutSession response structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: Newly created session id.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """Newly created session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateExtensionRequest(AbstractModel):
    """CreateExtension request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        :param _ExtensionName: Extension name.
        :type ExtensionName: str
        :param _SkillGroupIds: Bound skill group list.
        :type SkillGroupIds: list of int non-negative
        :param _Relation: Bound agent email.
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        """Extension name.
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        """Bound skill group list.
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        """Bound agent email.
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExtensionResponse(AbstractModel):
    """CreateExtension response structure.

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


class CreateIVRSessionRequest(AbstractModel):
    """CreateIVRSession request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Callee: Called.
        :type Callee: str
        :param _IVRId: Specified ivr id. currently, it supports inbound and automatic outbound types.
        :type IVRId: int
        :param _Callers: List of calling numbers.
        :type Callers: list of str
        :param _Variables: Custom variable.
        :type Variables: list of Variable
        :param _UUI: User data.
        :type UUI: str
        """
        self._SdkAppId = None
        self._Callee = None
        self._IVRId = None
        self._Callers = None
        self._Variables = None
        self._UUI = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callee(self):
        """Called.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def IVRId(self):
        """Specified ivr id. currently, it supports inbound and automatic outbound types.
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def Callers(self):
        """List of calling numbers.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Variables(self):
        """Custom variable.
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """User data.
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callee = params.get("Callee")
        self._IVRId = params.get("IVRId")
        self._Callers = params.get("Callers")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIVRSessionResponse(AbstractModel):
    """CreateIVRSession response structure.

    """

    def __init__(self):
        r"""
        :param _SessionId: Newly created session id.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        """Newly created session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class CreateOwnNumberApplyRequest(AbstractModel):
    """CreateOwnNumberApply request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SipTrunkId: SIP connection id.
        :type SipTrunkId: int
        :param _DetailList: Circuit-Related parameters.
        :type DetailList: list of OwnNumberApplyDetailItem
        :param _Prefix: Prefix for sending numbers.
        :type Prefix: str
        """
        self._SdkAppId = None
        self._SipTrunkId = None
        self._DetailList = None
        self._Prefix = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SipTrunkId(self):
        """SIP connection id.
        :rtype: int
        """
        return self._SipTrunkId

    @SipTrunkId.setter
    def SipTrunkId(self, SipTrunkId):
        self._SipTrunkId = SipTrunkId

    @property
    def DetailList(self):
        """Circuit-Related parameters.
        :rtype: list of OwnNumberApplyDetailItem
        """
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def Prefix(self):
        """Prefix for sending numbers.
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SipTrunkId = params.get("SipTrunkId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = OwnNumberApplyDetailItem()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOwnNumberApplyResponse(AbstractModel):
    """CreateOwnNumberApply response structure.

    """

    def __init__(self):
        r"""
        :param _ApplyId: Approval id.
        :type ApplyId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplyId = None
        self._RequestId = None

    @property
    def ApplyId(self):
        """Approval id.
        :rtype: int
        """
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId

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
        self._ApplyId = params.get("ApplyId")
        self._RequestId = params.get("RequestId")


class CreatePredictiveDialingCampaignRequest(AbstractModel):
    """CreatePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Name: <Task name>.
        :type Name: str
        :param _Callees: Called list supporting e.164 or number formats without country code.
        :type Callees: list of str
        :param _Callers: Calling list using the number formats displayed on the management side.
        :type Callers: list of str
        :param _CallOrder: Being called sequence: 0 for random 1 for in order.
        :type CallOrder: int
        :param _SkillGroupId: ID of the used skill group of agents.
        :type SkillGroupId: int
        :param _Priority: Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :type Priority: int
        :param _ExpectedAbandonRate: Expected call drop rate, percentage, 5 - 50.
        :type ExpectedAbandonRate: int
        :param _RetryInterval: Call retry interval, in seconds, [60 - 86,400].
        :type RetryInterval: int
        :param _StartTime: Task start time. unix timestamp. the task will automatically start after this time.
        :type StartTime: int
        :param _EndTime: Task termination time. unix timestamp. the task will automatically terminate after this time.
        :type EndTime: int
        :param _IVRId: Specified ivr id.
        :type IVRId: int
        :param _RetryTimes: Number of call retries, 0 - 2.
        :type RetryTimes: int
        :param _Variables: Custom variable.
        :type Variables: list of Variable
        :param _UUI: UUI
        :type UUI: str
        :param _CalleeAttributes: Property of the called.
        :type CalleeAttributes: list of CalleeAttribute
        """
        self._SdkAppId = None
        self._Name = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._IVRId = None
        self._RetryTimes = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        """<Task name>.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Callees(self):
        """Called list supporting e.164 or number formats without country code.
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """Calling list using the number formats displayed on the management side.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """Being called sequence: 0 for random 1 for in order.
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """ID of the used skill group of agents.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """Expected call drop rate, percentage, 5 - 50.
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryInterval(self):
        """Call retry interval, in seconds, [60 - 86,400].
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """Task start time. unix timestamp. the task will automatically start after this time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task termination time. unix timestamp. the task will automatically terminate after this time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IVRId(self):
        """Specified ivr id.
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def RetryTimes(self):
        """Number of call retries, 0 - 2.
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def Variables(self):
        """Custom variable.
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """Property of the called.
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IVRId = params.get("IVRId")
        self._RetryTimes = params.get("RetryTimes")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePredictiveDialingCampaignResponse(AbstractModel):
    """CreatePredictiveDialingCampaign response structure.

    """

    def __init__(self):
        r"""
        :param _CampaignId: Generated task id.
        :type CampaignId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CampaignId = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """Generated task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

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
        self._CampaignId = params.get("CampaignId")
        self._RequestId = params.get("RequestId")


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SeatUserId: Agent account.
        :type SeatUserId: str
        :param _OnlyOnce: Whether the generated token is for one-time verification?.
        :type OnlyOnce: bool
        """
        self._SdkAppId = None
        self._SeatUserId = None
        self._OnlyOnce = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SeatUserId(self):
        """Agent account.
        :rtype: str
        """
        return self._SeatUserId

    @SeatUserId.setter
    def SeatUserId(self, SeatUserId):
        self._SeatUserId = SeatUserId

    @property
    def OnlyOnce(self):
        """Whether the generated token is for one-time verification?.
        :rtype: bool
        """
        return self._OnlyOnce

    @OnlyOnce.setter
    def OnlyOnce(self, OnlyOnce):
        self._OnlyOnce = OnlyOnce


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SeatUserId = params.get("SeatUserId")
        self._OnlyOnce = params.get("OnlyOnce")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSDKLoginTokenResponse(AbstractModel):
    """CreateSDKLoginToken response structure.

    """

    def __init__(self):
        r"""
        :param _Token: SDK log-in token.
        :type Token: str
        :param _ExpiredTime: Expiry timestamp. unix timestamp.
        :type ExpiredTime: int
        :param _SdkURL: The path in which the sdk is loaded will change with its release.
        :type SdkURL: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Token = None
        self._ExpiredTime = None
        self._SdkURL = None
        self._RequestId = None

    @property
    def Token(self):
        """SDK log-in token.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        """Expiry timestamp. unix timestamp.
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SdkURL(self):
        """The path in which the sdk is loaded will change with its release.
        :rtype: str
        """
        return self._SdkURL

    @SdkURL.setter
    def SdkURL(self, SdkURL):
        self._SdkURL = SdkURL

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
        self._ExpiredTime = params.get("ExpiredTime")
        self._SdkURL = params.get("SdkURL")
        self._RequestId = params.get("RequestId")


class CreateStaffRequest(AbstractModel):
    """CreateStaff request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Staffs: Customer information, no more than 10.
        :type Staffs: list of SeatUserInfo
        :param _SendPassword: Whether to send a password mail or not (the default is true).
        :type SendPassword: bool
        """
        self._SdkAppId = None
        self._Staffs = None
        self._SendPassword = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Staffs(self):
        """Customer information, no more than 10.
        :rtype: list of SeatUserInfo
        """
        return self._Staffs

    @Staffs.setter
    def Staffs(self, Staffs):
        self._Staffs = Staffs

    @property
    def SendPassword(self):
        """Whether to send a password mail or not (the default is true).
        :rtype: bool
        """
        return self._SendPassword

    @SendPassword.setter
    def SendPassword(self, SendPassword):
        self._SendPassword = SendPassword


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Staffs") is not None:
            self._Staffs = []
            for item in params.get("Staffs"):
                obj = SeatUserInfo()
                obj._deserialize(item)
                self._Staffs.append(obj)
        self._SendPassword = params.get("SendPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaffResponse(AbstractModel):
    """CreateStaff response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorStaffList: Error agent list and error information.
        :type ErrorStaffList: list of ErrStaffItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorStaffList = None
        self._RequestId = None

    @property
    def ErrorStaffList(self):
        """Error agent list and error information.
        :rtype: list of ErrStaffItem
        """
        return self._ErrorStaffList

    @ErrorStaffList.setter
    def ErrorStaffList(self, ErrorStaffList):
        self._ErrorStaffList = ErrorStaffList

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
        if params.get("ErrorStaffList") is not None:
            self._ErrorStaffList = []
            for item in params.get("ErrorStaffList"):
                obj = ErrStaffItem()
                obj._deserialize(item)
                self._ErrorStaffList.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteExtensionRequest(AbstractModel):
    """DeleteExtension request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExtensionResponse(AbstractModel):
    """DeleteExtension response structure.

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


class DeletePredictiveDialingCampaignRequest(AbstractModel):
    """DeletePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: <Task id>.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """<Task id>.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePredictiveDialingCampaignResponse(AbstractModel):
    """DeletePredictiveDialingCampaign response structure.

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


class DeleteStaffRequest(AbstractModel):
    """DeleteStaff request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _StaffList: List of customer service emails to be deleted, supports up to 200 at a time.
        :type StaffList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        """List of customer service emails to be deleted, supports up to 200 at a time.
        :rtype: list of str
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStaffResponse(AbstractModel):
    """DeleteStaff response structure.

    """

    def __init__(self):
        r"""
        :param _OnlineStaffList: List of customer service staff that cannot be deleted when they are online.
        :type OnlineStaffList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OnlineStaffList = None
        self._RequestId = None

    @property
    def OnlineStaffList(self):
        """List of customer service staff that cannot be deleted when they are online.
        :rtype: list of str
        """
        return self._OnlineStaffList

    @OnlineStaffList.setter
    def OnlineStaffList(self, OnlineStaffList):
        self._OnlineStaffList = OnlineStaffList

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
        self._OnlineStaffList = params.get("OnlineStaffList")
        self._RequestId = params.get("RequestId")


class DescribeAICallExtractResultRequest(AbstractModel):
    """DescribeAICallExtractResult request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SessionId: Session id.
        :type SessionId: str
        :param _StartTime: Search for the start time.
        :type StartTime: int
        :param _EndTime: Search for the end time.
        :type EndTime: int
        """
        self._SdkAppId = None
        self._SessionId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """Session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def StartTime(self):
        """Search for the start time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Search for the end time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAICallExtractResultResponse(AbstractModel):
    """DescribeAICallExtractResult response structure.

    """

    def __init__(self):
        r"""
        :param _ResultList: Result list.
        :type ResultList: list of AICallExtractResultElement
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResultList = None
        self._RequestId = None

    @property
    def ResultList(self):
        """Result list.
        :rtype: list of AICallExtractResultElement
        """
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

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
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = AICallExtractResultElement()
                obj._deserialize(item)
                self._ResultList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentCruiseDialingCampaignRequest(AbstractModel):
    """DescribeAgentCruiseDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: Task id.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """Task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentCruiseDialingCampaignResponse(AbstractModel):
    """DescribeAgentCruiseDialingCampaign response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Task name.
        :type Name: str
        :param _Agent: Agent account.
        :type Agent: str
        :param _ConcurrencyNumber: Single-Round concurrent call volume 1-20.
        :type ConcurrencyNumber: int
        :param _StartTime: Task start time. unix timestamp. the task will automatically start after this time.
        :type StartTime: int
        :param _EndTime: Task termination time. unix timestamp. the task will automatically terminate after this time.
        :type EndTime: int
        :param _CallOrder: Being called sequence: 0 for random 1 for in order.
        :type CallOrder: int
        :param _UUI: Caller custom data, maximum length 1024.
        :type UUI: str
        :param _State: Task status 0 not started 1 running 2 completed 3 terminated.
        :type State: int
        :param _TotalCalleeCount: Total number of called parties.
        :type TotalCalleeCount: int
        :param _CalledCalleeCount: Number of calls made and received.
        :type CalledCalleeCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Agent = None
        self._ConcurrencyNumber = None
        self._StartTime = None
        self._EndTime = None
        self._CallOrder = None
        self._UUI = None
        self._State = None
        self._TotalCalleeCount = None
        self._CalledCalleeCount = None
        self._RequestId = None

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Agent(self):
        """Agent account.
        :rtype: str
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ConcurrencyNumber(self):
        """Single-Round concurrent call volume 1-20.
        :rtype: int
        """
        return self._ConcurrencyNumber

    @ConcurrencyNumber.setter
    def ConcurrencyNumber(self, ConcurrencyNumber):
        self._ConcurrencyNumber = ConcurrencyNumber

    @property
    def StartTime(self):
        """Task start time. unix timestamp. the task will automatically start after this time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task termination time. unix timestamp. the task will automatically terminate after this time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CallOrder(self):
        """Being called sequence: 0 for random 1 for in order.
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def UUI(self):
        """Caller custom data, maximum length 1024.
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def State(self):
        """Task status 0 not started 1 running 2 completed 3 terminated.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TotalCalleeCount(self):
        """Total number of called parties.
        :rtype: int
        """
        return self._TotalCalleeCount

    @TotalCalleeCount.setter
    def TotalCalleeCount(self, TotalCalleeCount):
        self._TotalCalleeCount = TotalCalleeCount

    @property
    def CalledCalleeCount(self):
        """Number of calls made and received.
        :rtype: int
        """
        return self._CalledCalleeCount

    @CalledCalleeCount.setter
    def CalledCalleeCount(self, CalledCalleeCount):
        self._CalledCalleeCount = CalledCalleeCount

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
        self._Name = params.get("Name")
        self._Agent = params.get("Agent")
        self._ConcurrencyNumber = params.get("ConcurrencyNumber")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CallOrder = params.get("CallOrder")
        self._UUI = params.get("UUI")
        self._State = params.get("State")
        self._TotalCalleeCount = params.get("TotalCalleeCount")
        self._CalledCalleeCount = params.get("CalledCalleeCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTaskRequest(AbstractModel):
    """DescribeAutoCalloutTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _TaskId: Task id.
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """Task id.
        :rtype: int
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
        


class DescribeAutoCalloutTaskResponse(AbstractModel):
    """DescribeAutoCalloutTask response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Task name.
        :type Name: str
        :param _Description: <Task description>.
        :type Description: str
        :param _NotBefore: Task start timestamp.
        :type NotBefore: int
        :param _NotAfter: Task end timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotAfter: int
        :param _Callers: Calling list.
        :type Callers: list of str
        :param _Callees: Called information list.
        :type Callees: list of AutoCalloutTaskCalleeInfo
        :param _IvrId: IvrId used by the task.
        :type IvrId: int
        :param _State: Task status: 0 - initial, 1 - running, 2 - completed, 3 - ending, 4 - terminated.
        :type State: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._NotBefore = None
        self._NotAfter = None
        self._Callers = None
        self._Callees = None
        self._IvrId = None
        self._State = None
        self._RequestId = None

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """<Task description>.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NotBefore(self):
        """Task start timestamp.
        :rtype: int
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def NotAfter(self):
        """Task end timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Callers(self):
        """Calling list.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def Callees(self):
        """Called information list.
        :rtype: list of AutoCalloutTaskCalleeInfo
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def IvrId(self):
        """IvrId used by the task.
        :rtype: int
        """
        return self._IvrId

    @IvrId.setter
    def IvrId(self, IvrId):
        self._IvrId = IvrId

    @property
    def State(self):
        """Task status: 0 - initial, 1 - running, 2 - completed, 3 - ending, 4 - terminated.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

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
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._NotBefore = params.get("NotBefore")
        self._NotAfter = params.get("NotAfter")
        self._Callers = params.get("Callers")
        if params.get("Callees") is not None:
            self._Callees = []
            for item in params.get("Callees"):
                obj = AutoCalloutTaskCalleeInfo()
                obj._deserialize(item)
                self._Callees.append(obj)
        self._IvrId = params.get("IvrId")
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class DescribeAutoCalloutTasksRequest(AbstractModel):
    """DescribeAutoCalloutTasks request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: <Page size>.
        :type PageSize: int
        :param _PageNumber: Page number.
        :type PageNumber: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """<Page size>.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoCalloutTasksResponse(AbstractModel):
    """DescribeAutoCalloutTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _Tasks: <Task list>.
        :type Tasks: list of AutoCalloutTaskInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """<Task list>.
        :rtype: list of AutoCalloutTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AutoCalloutTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCCBuyInfoListRequest(AbstractModel):
    """DescribeCCCBuyInfoList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppIds: Application id list, query all applications when not transmitted.
        :type SdkAppIds: list of int
        """
        self._SdkAppIds = None

    @property
    def SdkAppIds(self):
        """Application id list, query all applications when not transmitted.
        :rtype: list of int
        """
        return self._SdkAppIds

    @SdkAppIds.setter
    def SdkAppIds(self, SdkAppIds):
        self._SdkAppIds = SdkAppIds


    def _deserialize(self, params):
        self._SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCCBuyInfoListResponse(AbstractModel):
    """DescribeCCCBuyInfoList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of applications.
        :type TotalCount: int
        :param _SdkAppIdBuyList: Application purchase information list.
        :type SdkAppIdBuyList: list of SdkAppIdBuyInfo
        :param _PackageBuyList: Package purchase information list.
        :type PackageBuyList: list of PackageBuyInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SdkAppIdBuyList = None
        self._PackageBuyList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of applications.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SdkAppIdBuyList(self):
        """Application purchase information list.
        :rtype: list of SdkAppIdBuyInfo
        """
        return self._SdkAppIdBuyList

    @SdkAppIdBuyList.setter
    def SdkAppIdBuyList(self, SdkAppIdBuyList):
        self._SdkAppIdBuyList = SdkAppIdBuyList

    @property
    def PackageBuyList(self):
        """Package purchase information list.
        :rtype: list of PackageBuyInfo
        """
        return self._PackageBuyList

    @PackageBuyList.setter
    def PackageBuyList(self, PackageBuyList):
        self._PackageBuyList = PackageBuyList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SdkAppIdBuyList") is not None:
            self._SdkAppIdBuyList = []
            for item in params.get("SdkAppIdBuyList"):
                obj = SdkAppIdBuyInfo()
                obj._deserialize(item)
                self._SdkAppIdBuyList.append(obj)
        if params.get("PackageBuyList") is not None:
            self._PackageBuyList = []
            for item in params.get("PackageBuyList"):
                obj = PackageBuyInfo()
                obj._deserialize(item)
                self._PackageBuyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallInMetricsRequest(AbstractModel):
    """DescribeCallInMetrics request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _EnabledSkillGroup: Whether to return skill group dimension information or not (the default is "yes").
        :type EnabledSkillGroup: bool
        :param _EnabledNumber: Whether to return line dimension information or not (the default is "no").
        :type EnabledNumber: bool
        :param _GroupIdList: Filter skill group list.
        :type GroupIdList: list of int
        """
        self._SdkAppId = None
        self._EnabledSkillGroup = None
        self._EnabledNumber = None
        self._GroupIdList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def EnabledSkillGroup(self):
        """Whether to return skill group dimension information or not (the default is "yes").
        :rtype: bool
        """
        return self._EnabledSkillGroup

    @EnabledSkillGroup.setter
    def EnabledSkillGroup(self, EnabledSkillGroup):
        self._EnabledSkillGroup = EnabledSkillGroup

    @property
    def EnabledNumber(self):
        """Whether to return line dimension information or not (the default is "no").
        :rtype: bool
        """
        return self._EnabledNumber

    @EnabledNumber.setter
    def EnabledNumber(self, EnabledNumber):
        self._EnabledNumber = EnabledNumber

    @property
    def GroupIdList(self):
        """Filter skill group list.
        :rtype: list of int
        """
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._EnabledSkillGroup = params.get("EnabledSkillGroup")
        self._EnabledNumber = params.get("EnabledNumber")
        self._GroupIdList = params.get("GroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallInMetricsResponse(AbstractModel):
    """DescribeCallInMetrics response structure.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Timestamp.
        :type Timestamp: int
        :param _TotalMetrics: Overall metrics.
        :type TotalMetrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param _NumberMetrics: Circuit dimension metrics.
        :type NumberMetrics: list of CallInNumberMetrics
        :param _SkillGroupMetrics: Skill group dimension metrics.
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Timestamp = None
        self._TotalMetrics = None
        self._NumberMetrics = None
        self._SkillGroupMetrics = None
        self._RequestId = None

    @property
    def Timestamp(self):
        """Timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def TotalMetrics(self):
        """Overall metrics.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        """
        return self._TotalMetrics

    @TotalMetrics.setter
    def TotalMetrics(self, TotalMetrics):
        self._TotalMetrics = TotalMetrics

    @property
    def NumberMetrics(self):
        """Circuit dimension metrics.
        :rtype: list of CallInNumberMetrics
        """
        return self._NumberMetrics

    @NumberMetrics.setter
    def NumberMetrics(self, NumberMetrics):
        self._NumberMetrics = NumberMetrics

    @property
    def SkillGroupMetrics(self):
        """Skill group dimension metrics.
        :rtype: list of CallInSkillGroupMetrics
        """
        return self._SkillGroupMetrics

    @SkillGroupMetrics.setter
    def SkillGroupMetrics(self, SkillGroupMetrics):
        self._SkillGroupMetrics = SkillGroupMetrics

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
        self._Timestamp = params.get("Timestamp")
        if params.get("TotalMetrics") is not None:
            self._TotalMetrics = CallInMetrics()
            self._TotalMetrics._deserialize(params.get("TotalMetrics"))
        if params.get("NumberMetrics") is not None:
            self._NumberMetrics = []
            for item in params.get("NumberMetrics"):
                obj = CallInNumberMetrics()
                obj._deserialize(item)
                self._NumberMetrics.append(obj)
        if params.get("SkillGroupMetrics") is not None:
            self._SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self._SkillGroupMetrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtensionRequest(AbstractModel):
    """DescribeExtension request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionResponse(AbstractModel):
    """DescribeExtension response structure.

    """

    def __init__(self):
        r"""
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        :param _ExtensionDomain: Domain name.
        :type ExtensionDomain: str
        :param _Password: Registered password.
        :type Password: str
        :param _OutboundProxy: Proxy server address.
        :type OutboundProxy: str
        :param _Transport: Transfer protocol.
        :type Transport: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExtensionId = None
        self._ExtensionDomain = None
        self._Password = None
        self._OutboundProxy = None
        self._Transport = None
        self._RequestId = None

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionDomain(self):
        """Domain name.
        :rtype: str
        """
        return self._ExtensionDomain

    @ExtensionDomain.setter
    def ExtensionDomain(self, ExtensionDomain):
        self._ExtensionDomain = ExtensionDomain

    @property
    def Password(self):
        """Registered password.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def OutboundProxy(self):
        """Proxy server address.
        :rtype: str
        """
        return self._OutboundProxy

    @OutboundProxy.setter
    def OutboundProxy(self, OutboundProxy):
        self._OutboundProxy = OutboundProxy

    @property
    def Transport(self):
        """Transfer protocol.
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

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
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionDomain = params.get("ExtensionDomain")
        self._Password = params.get("Password")
        self._OutboundProxy = params.get("OutboundProxy")
        self._Transport = params.get("Transport")
        self._RequestId = params.get("RequestId")


class DescribeExtensionsRequest(AbstractModel):
    """DescribeExtensions request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageNumber: Page number (starting from 0).
        :type PageNumber: int
        :param _ExtensionIds: Filtering extension number list.
        :type ExtensionIds: list of str
        :param _PageSize: Page size.
        :type PageSize: int
        :param _FuzzingKeyWord: Fuzzy query field (fuzzy query for extension number, extension name, agent email, and agent name).
        :type FuzzingKeyWord: str
        :param _IsNeedStatus: Whether to return the current status of the telephone or not.
        :type IsNeedStatus: bool
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._ExtensionIds = None
        self._PageSize = None
        self._FuzzingKeyWord = None
        self._IsNeedStatus = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """Page number (starting from 0).
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def ExtensionIds(self):
        """Filtering extension number list.
        :rtype: list of str
        """
        return self._ExtensionIds

    @ExtensionIds.setter
    def ExtensionIds(self, ExtensionIds):
        self._ExtensionIds = ExtensionIds

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
    def FuzzingKeyWord(self):
        """Fuzzy query field (fuzzy query for extension number, extension name, agent email, and agent name).
        :rtype: str
        """
        return self._FuzzingKeyWord

    @FuzzingKeyWord.setter
    def FuzzingKeyWord(self, FuzzingKeyWord):
        self._FuzzingKeyWord = FuzzingKeyWord

    @property
    def IsNeedStatus(self):
        """Whether to return the current status of the telephone or not.
        :rtype: bool
        """
        return self._IsNeedStatus

    @IsNeedStatus.setter
    def IsNeedStatus(self, IsNeedStatus):
        self._IsNeedStatus = IsNeedStatus


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._ExtensionIds = params.get("ExtensionIds")
        self._PageSize = params.get("PageSize")
        self._FuzzingKeyWord = params.get("FuzzingKeyWord")
        self._IsNeedStatus = params.get("IsNeedStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionsResponse(AbstractModel):
    """DescribeExtensions response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total query count.
        :type Total: int
        :param _ExtensionList: Telephone information list.
        :type ExtensionList: list of ExtensionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ExtensionList = None
        self._RequestId = None

    @property
    def Total(self):
        """Total query count.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ExtensionList(self):
        """Telephone information list.
        :rtype: list of ExtensionInfo
        """
        return self._ExtensionList

    @ExtensionList.setter
    def ExtensionList(self, ExtensionList):
        self._ExtensionList = ExtensionList

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
        if params.get("ExtensionList") is not None:
            self._ExtensionList = []
            for item in params.get("ExtensionList"):
                obj = ExtensionInfo()
                obj._deserialize(item)
                self._ExtensionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIvrAudioListRequest(AbstractModel):
    """DescribeIvrAudioList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size, upper limit 50.
        :type PageSize: int
        :param _PageNumber: Page number starting from 0.
        :type PageNumber: int
        :param _CustomFileName: File alias.
        :type CustomFileName: list of str
        :param _AudioFileName: Filename.
        :type AudioFileName: list of str
        :param _FileId: File id.
        :type FileId: list of int non-negative
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._CustomFileName = None
        self._AudioFileName = None
        self._FileId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size, upper limit 50.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def CustomFileName(self):
        """File alias.
        :rtype: list of str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioFileName(self):
        """Filename.
        :rtype: list of str
        """
        return self._AudioFileName

    @AudioFileName.setter
    def AudioFileName(self, AudioFileName):
        self._AudioFileName = AudioFileName

    @property
    def FileId(self):
        """File id.
        :rtype: list of int non-negative
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._CustomFileName = params.get("CustomFileName")
        self._AudioFileName = params.get("AudioFileName")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIvrAudioListResponse(AbstractModel):
    """DescribeIvrAudioList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _FileInfo: File information.
        :type FileInfo: list of AudioFileInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._FileInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FileInfo(self):
        """File information.
        :rtype: list of AudioFileInfo
        """
        return self._FileInfo

    @FileInfo.setter
    def FileInfo(self, FileInfo):
        self._FileInfo = FileInfo

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
        self._TotalCount = params.get("TotalCount")
        if params.get("FileInfo") is not None:
            self._FileInfo = []
            for item in params.get("FileInfo"):
                obj = AudioFileInfo()
                obj._deserialize(item)
                self._FileInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNumbersRequest(AbstractModel):
    """DescribeNumbers request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageNumber: Page number, starting from 0.
        :type PageNumber: int
        :param _PageSize: Page size, default 20.
        :type PageSize: int
        """
        self._SdkAppId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageNumber(self):
        """Page number, starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Page size, default 20.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNumbersResponse(AbstractModel):
    """DescribeNumbers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _Numbers: Number list.
        :type Numbers: list of NumberInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Numbers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Numbers(self):
        """Number list.
        :rtype: list of NumberInfo
        """
        return self._Numbers

    @Numbers.setter
    def Numbers(self, Numbers):
        self._Numbers = Numbers

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Numbers") is not None:
            self._Numbers = []
            for item in params.get("Numbers"):
                obj = NumberInfo()
                obj._deserialize(item)
                self._Numbers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePSTNActiveSessionListRequest(AbstractModel):
    """DescribePSTNActiveSessionList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Offset: Data offset.
        :type Offset: int
        :param _Limit: Number of returned data entries, up to 25.
        :type Limit: int
        """
        self._SdkAppId = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Offset(self):
        """Data offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned data entries, up to 25.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePSTNActiveSessionListResponse(AbstractModel):
    """DescribePSTNActiveSessionList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of items in the list.
        :type Total: int
        :param _Sessions: List content.
        :type Sessions: list of PSTNSessionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Sessions = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of items in the list.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sessions(self):
        """List content.
        :rtype: list of PSTNSessionInfo
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

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
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = PSTNSessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingCampaignRequest(AbstractModel):
    """DescribePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: <Task id>.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """<Task id>.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignResponse(AbstractModel):
    """DescribePredictiveDialingCampaign response structure.

    """

    def __init__(self):
        r"""
        :param _CampaignId: Task id.
        :type CampaignId: int
        :param _Name: Task name.
        :type Name: str
        :param _CallOrder: Being called sequence: 0 for random 1 for in order.
        :type CallOrder: int
        :param _SkillGroupId: ID of the used skill group of agents.
        :type SkillGroupId: int
        :param _IVRId: Specified ivr id.
        :type IVRId: int
        :param _Priority: Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :type Priority: int
        :param _ExpectedAbandonRate: Expected call drop rate, percentage, 5 - 50.
        :type ExpectedAbandonRate: int
        :param _RetryTimes: Number of call retries, 0 - 2.
        :type RetryTimes: int
        :param _RetryInterval: Call retry interval, in seconds, [60 - 86,400].
        :type RetryInterval: int
        :param _StartTime: Task start time. unix timestamp. the task will automatically start after this time.
        :type StartTime: int
        :param _EndTime: Task termination time. unix timestamp. the task will automatically terminate after this time.
        :type EndTime: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CampaignId = None
        self._Name = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._IVRId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryTimes = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def CampaignId(self):
        """Task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CallOrder(self):
        """Being called sequence: 0 for random 1 for in order.
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """ID of the used skill group of agents.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def IVRId(self):
        """Specified ivr id.
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def Priority(self):
        """Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """Expected call drop rate, percentage, 5 - 50.
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryTimes(self):
        """Number of call retries, 0 - 2.
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def RetryInterval(self):
        """Call retry interval, in seconds, [60 - 86,400].
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """Task start time. unix timestamp. the task will automatically start after this time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task termination time. unix timestamp. the task will automatically terminate after this time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._IVRId = params.get("IVRId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryTimes = params.get("RetryTimes")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingCampaignsElement(AbstractModel):
    """Query the predictive outbound call task list elements.

    """

    def __init__(self):
        r"""
        :param _CampaignId: <Task id>.
        :type CampaignId: int
        :param _Name: Task name.
        :type Name: str
        :param _Status: Task status 0 - ready to start, 1 - in progress, 2 - paused, 3 - terminated, 4 - completed.
        :type Status: int
        :param _StatusReason: Task status reasons 0 - normal, 1 - manually ended, 2 - ended due to overtime.
        :type StatusReason: int
        :param _CalleeCount: Number of called numbers.
        :type CalleeCount: int
        :param _FinishedCalleeCount: Number of completed calls.
        :type FinishedCalleeCount: int
        :param _Priority: Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :type Priority: int
        :param _SkillGroupId: ID of the used skill group of agents.
        :type SkillGroupId: int
        """
        self._CampaignId = None
        self._Name = None
        self._Status = None
        self._StatusReason = None
        self._CalleeCount = None
        self._FinishedCalleeCount = None
        self._Priority = None
        self._SkillGroupId = None

    @property
    def CampaignId(self):
        """<Task id>.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """Task status 0 - ready to start, 1 - in progress, 2 - paused, 3 - terminated, 4 - completed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        """Task status reasons 0 - normal, 1 - manually ended, 2 - ended due to overtime.
        :rtype: int
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def CalleeCount(self):
        """Number of called numbers.
        :rtype: int
        """
        return self._CalleeCount

    @CalleeCount.setter
    def CalleeCount(self, CalleeCount):
        self._CalleeCount = CalleeCount

    @property
    def FinishedCalleeCount(self):
        """Number of completed calls.
        :rtype: int
        """
        return self._FinishedCalleeCount

    @FinishedCalleeCount.setter
    def FinishedCalleeCount(self, FinishedCalleeCount):
        self._FinishedCalleeCount = FinishedCalleeCount

    @property
    def Priority(self):
        """Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def SkillGroupId(self):
        """ID of the used skill group of agents.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._CalleeCount = params.get("CalleeCount")
        self._FinishedCalleeCount = params.get("FinishedCalleeCount")
        self._Priority = params.get("Priority")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignsRequest(AbstractModel):
    """DescribePredictiveDialingCampaigns request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size, 100 maximum.
        :type PageSize: int
        :param _PageNumber: Page number starting from 0.
        :type PageNumber: int
        :param _Name: Query the task list name keyword.
        :type Name: str
        :param _SkillGroupId: Query task list skill group id.
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._Name = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size, 100 maximum.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Name(self):
        """Query the task list name keyword.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkillGroupId(self):
        """Query task list skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Name = params.get("Name")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingCampaignsResponse(AbstractModel):
    """DescribePredictiveDialingCampaigns response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total data volume.
        :type TotalCount: int
        :param _CampaignList: Data.
        :type CampaignList: list of DescribePredictiveDialingCampaignsElement
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CampaignList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total data volume.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CampaignList(self):
        """Data.
        :rtype: list of DescribePredictiveDialingCampaignsElement
        """
        return self._CampaignList

    @CampaignList.setter
    def CampaignList(self, CampaignList):
        self._CampaignList = CampaignList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("CampaignList") is not None:
            self._CampaignList = []
            for item in params.get("CampaignList"):
                obj = DescribePredictiveDialingCampaignsElement()
                obj._deserialize(item)
                self._CampaignList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePredictiveDialingSessionsRequest(AbstractModel):
    """DescribePredictiveDialingSessions request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: Generated task id.
        :type CampaignId: int
        :param _PageSize: Page size, maximum of 1000.
        :type PageSize: int
        :param _PageNumber: Page number starting from 0.
        :type PageNumber: int
        """
        self._SdkAppId = None
        self._CampaignId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """Generated task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def PageSize(self):
        """Page size, maximum of 1000.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePredictiveDialingSessionsResponse(AbstractModel):
    """DescribePredictiveDialingSessions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total data volume.
        :type TotalCount: int
        :param _SessionList: List of session ids for a call. you can access detailed call bills in batches through https://intl.cloud.tencent.com/document/product/679/47714.?from_cn_redirect=1.
        :type SessionList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SessionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total data volume.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SessionList(self):
        """List of session ids for a call. you can access detailed call bills in batches through https://intl.cloud.tencent.com/document/product/679/47714.?from_cn_redirect=1.
        :rtype: list of str
        """
        return self._SessionList

    @SessionList.setter
    def SessionList(self, SessionList):
        self._SessionList = SessionList

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
        self._TotalCount = params.get("TotalCount")
        self._SessionList = params.get("SessionList")
        self._RequestId = params.get("RequestId")


class DescribeProtectedTelCdrRequest(AbstractModel):
    """DescribeProtectedTelCdr request structure.

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: Start timestamp. unix second-level timestamp.
        :type StartTimeStamp: int
        :param _EndTimeStamp: End timestamp. unix second-level timestamp.
        :type EndTimeStamp: int
        :param _SdkAppId: For the application id, you can check https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size, upper limit 100.
        :type PageSize: int
        :param _PageNumber: Page number starting from 0.
        :type PageNumber: int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def StartTimeStamp(self):
        """Start timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """End timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppId(self):
        """For the application id, you can check https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size, upper limit 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectedTelCdrResponse(AbstractModel):
    """DescribeProtectedTelCdr response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of call records.
        :type TotalCount: int
        :param _TelCdrs: Call record.
        :type TelCdrs: list of TelCdrInfo
        :param _TelCdrList: Call record.
        :type TelCdrList: list of TelCdrInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._TelCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of call records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        """Call record.
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        self._TelCdrs = TelCdrs

    @property
    def TelCdrList(self):
        """Call record.
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrList

    @TelCdrList.setter
    def TelCdrList(self, TelCdrList):
        self._TelCdrList = TelCdrList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        if params.get("TelCdrList") is not None:
            self._TelCdrList = []
            for item in params.get("TelCdrList"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSkillGroupInfoListRequest(AbstractModel):
    """DescribeSkillGroupInfoList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size, upper limit 100.
        :type PageSize: int
        :param _PageNumber: <Page number starting from 0.>.
        :type PageNumber: int
        :param _SkillGroupId: Using skill group id when querying a single skill group.
        :type SkillGroupId: int
        :param _ModifiedTime: Used when querying skill groups with a modified time greater or equal to modifiedtime.
        :type ModifiedTime: int
        :param _SkillGroupName: Skill group name.
        :type SkillGroupName: str
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._SkillGroupId = None
        self._ModifiedTime = None
        self._SkillGroupName = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size, upper limit 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """<Page number starting from 0.>.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def SkillGroupId(self):
        """Using skill group id when querying a single skill group.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ModifiedTime(self):
        """Used when querying skill groups with a modified time greater or equal to modifiedtime.
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupName(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupName = params.get("SkillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillGroupInfoListResponse(AbstractModel):
    """DescribeSkillGroupInfoList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of skill groups.
        :type TotalCount: int
        :param _SkillGroupList: Skill group information list.
        :type SkillGroupList: list of SkillGroupInfoItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SkillGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of skill groups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SkillGroupList(self):
        """Skill group information list.
        :rtype: list of SkillGroupInfoItem
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupInfoItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffInfoListRequest(AbstractModel):
    """DescribeStaffInfoList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size, upper limit 9,999.
        :type PageSize: int
        :param _PageNumber: Page number starting from 0.
        :type PageNumber: int
        :param _StaffMail: Agent account used when querying a single agent.
        :type StaffMail: str
        :param _ModifiedTime: Use when querying for agents with a modification time greater or equal to modifiedtime.
        :type ModifiedTime: int
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        """
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._StaffMail = None
        self._ModifiedTime = None
        self._SkillGroupId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size, upper limit 9,999.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Page number starting from 0.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def StaffMail(self):
        """Agent account used when querying a single agent.
        :rtype: str
        """
        return self._StaffMail

    @StaffMail.setter
    def StaffMail(self, StaffMail):
        self._StaffMail = StaffMail

    @property
    def ModifiedTime(self):
        """Use when querying for agents with a modification time greater or equal to modifiedtime.
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._StaffMail = params.get("StaffMail")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SkillGroupId = params.get("SkillGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffInfoListResponse(AbstractModel):
    """DescribeStaffInfoList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of agent users.
        :type TotalCount: int
        :param _StaffList: Agent user information list.
        :type StaffList: list of StaffInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._StaffList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of agent users.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StaffList(self):
        """Agent user information list.
        :rtype: list of StaffInfo
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("StaffList") is not None:
            self._StaffList = []
            for item in params.get("StaffList"):
                obj = StaffInfo()
                obj._deserialize(item)
                self._StaffList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStaffStatusMetricsRequest(AbstractModel):
    """DescribeStaffStatusMetrics request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _StaffList: Filter agent list. by default, do not pass all returned agent information.
        :type StaffList: list of str
        :param _GroupIdList: Filter skill group id list.
        :type GroupIdList: list of int
        :param _StatusList: Filter agent status list agent status free available | busy busy | rest on break | notready not ready | aftercallwork post-call adjustment | offline offline . 
        :type StatusList: list of str
        """
        self._SdkAppId = None
        self._StaffList = None
        self._GroupIdList = None
        self._StatusList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffList(self):
        """Filter agent list. by default, do not pass all returned agent information.
        :rtype: list of str
        """
        return self._StaffList

    @StaffList.setter
    def StaffList(self, StaffList):
        self._StaffList = StaffList

    @property
    def GroupIdList(self):
        """Filter skill group id list.
        :rtype: list of int
        """
        return self._GroupIdList

    @GroupIdList.setter
    def GroupIdList(self, GroupIdList):
        self._GroupIdList = GroupIdList

    @property
    def StatusList(self):
        """Filter agent status list agent status free available | busy busy | rest on break | notready not ready | aftercallwork post-call adjustment | offline offline . 
        :rtype: list of str
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffList = params.get("StaffList")
        self._GroupIdList = params.get("GroupIdList")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffStatusMetricsResponse(AbstractModel):
    """DescribeStaffStatusMetrics response structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: Real-Time information on agent status.
        :type Metrics: list of StaffStatusMetrics
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        """Real-Time information on agent status.
        :rtype: list of StaffStatusMetrics
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

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
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = StaffStatusMetrics()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo request structure.

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: Start timestamp, unix timestamp (query dimension supports only daily. for example, to query may 1st, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-01 23:59:59" timestamp. to query may 1st and may 2nd, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-02 23:59:59" timestamp).
        :type StartTimeStamp: int
        :param _EndTimeStamp: End timestamp, unix timestamp, the query time range is up to 90 days (query dimension supports only daily. for example, to query may 1st, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-01 23:59:59" timestamp. to query may 1st and may 2nd, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-02 23:59:59" timestamp).
        :type EndTimeStamp: int
        :param _SdkAppIdList: Application id list, when having multiple ids, the returned value is the sum of all the ids.
        :type SdkAppIdList: list of int
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._SdkAppIdList = None

    @property
    def StartTimeStamp(self):
        """Start timestamp, unix timestamp (query dimension supports only daily. for example, to query may 1st, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-01 23:59:59" timestamp. to query may 1st and may 2nd, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-02 23:59:59" timestamp).
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """End timestamp, unix timestamp, the query time range is up to 90 days (query dimension supports only daily. for example, to query may 1st, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-01 23:59:59" timestamp. to query may 1st and may 2nd, pass starttime:"2023-05-01 00:00:00","endtime":"2023-05-02 23:59:59" timestamp).
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def SdkAppIdList(self):
        """Application id list, when having multiple ids, the returned value is the sum of all the ids.
        :rtype: list of int
        """
        return self._SdkAppIdList

    @SdkAppIdList.setter
    def SdkAppIdList(self, SdkAppIdList):
        self._SdkAppIdList = SdkAppIdList


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._SdkAppIdList = params.get("SdkAppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCallInfoResponse(AbstractModel):
    """DescribeTelCallInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TelCallOutCount: Number of minutes consumed by outbound package.
        :type TelCallOutCount: int
        :param _TelCallInCount: Number of minutes consumed by inbound package.
        :type TelCallInCount: int
        :param _SeatUsedCount: Number of agent usage statistics.
        :type SeatUsedCount: int
        :param _VoipCallInCount: Number of minutes consumed by audio package.
        :type VoipCallInCount: int
        :param _VOIPCallInCount: Number of minutes consumed by audio package.
        :type VOIPCallInCount: int
        :param _AsrOfflineCount: Number of minutes consumed by offline speech-to-text package.
        :type AsrOfflineCount: int
        :param _AsrRealtimeCount: Number of minutes consumed by real-time speech-to-text package.
        :type AsrRealtimeCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TelCallOutCount = None
        self._TelCallInCount = None
        self._SeatUsedCount = None
        self._VoipCallInCount = None
        self._VOIPCallInCount = None
        self._AsrOfflineCount = None
        self._AsrRealtimeCount = None
        self._RequestId = None

    @property
    def TelCallOutCount(self):
        """Number of minutes consumed by outbound package.
        :rtype: int
        """
        return self._TelCallOutCount

    @TelCallOutCount.setter
    def TelCallOutCount(self, TelCallOutCount):
        self._TelCallOutCount = TelCallOutCount

    @property
    def TelCallInCount(self):
        """Number of minutes consumed by inbound package.
        :rtype: int
        """
        return self._TelCallInCount

    @TelCallInCount.setter
    def TelCallInCount(self, TelCallInCount):
        self._TelCallInCount = TelCallInCount

    @property
    def SeatUsedCount(self):
        """Number of agent usage statistics.
        :rtype: int
        """
        return self._SeatUsedCount

    @SeatUsedCount.setter
    def SeatUsedCount(self, SeatUsedCount):
        self._SeatUsedCount = SeatUsedCount

    @property
    def VoipCallInCount(self):
        warnings.warn("parameter `VoipCallInCount` is deprecated", DeprecationWarning) 

        """Number of minutes consumed by audio package.
        :rtype: int
        """
        return self._VoipCallInCount

    @VoipCallInCount.setter
    def VoipCallInCount(self, VoipCallInCount):
        warnings.warn("parameter `VoipCallInCount` is deprecated", DeprecationWarning) 

        self._VoipCallInCount = VoipCallInCount

    @property
    def VOIPCallInCount(self):
        """Number of minutes consumed by audio package.
        :rtype: int
        """
        return self._VOIPCallInCount

    @VOIPCallInCount.setter
    def VOIPCallInCount(self, VOIPCallInCount):
        self._VOIPCallInCount = VOIPCallInCount

    @property
    def AsrOfflineCount(self):
        """Number of minutes consumed by offline speech-to-text package.
        :rtype: int
        """
        return self._AsrOfflineCount

    @AsrOfflineCount.setter
    def AsrOfflineCount(self, AsrOfflineCount):
        self._AsrOfflineCount = AsrOfflineCount

    @property
    def AsrRealtimeCount(self):
        """Number of minutes consumed by real-time speech-to-text package.
        :rtype: int
        """
        return self._AsrRealtimeCount

    @AsrRealtimeCount.setter
    def AsrRealtimeCount(self, AsrRealtimeCount):
        self._AsrRealtimeCount = AsrRealtimeCount

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
        self._TelCallOutCount = params.get("TelCallOutCount")
        self._TelCallInCount = params.get("TelCallInCount")
        self._SeatUsedCount = params.get("SeatUsedCount")
        self._VoipCallInCount = params.get("VoipCallInCount")
        self._VOIPCallInCount = params.get("VOIPCallInCount")
        self._AsrOfflineCount = params.get("AsrOfflineCount")
        self._AsrRealtimeCount = params.get("AsrRealtimeCount")
        self._RequestId = params.get("RequestId")


class DescribeTelCdrRequest(AbstractModel):
    """DescribeTelCdr request structure.

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: Start timestamp, unix timestamp in seconds. supports up to the past 180 days.
        :type StartTimeStamp: int
        :param _EndTimeStamp: End timestamp, unix timestamp in seconds. the range between the end time and start time is less than 90 days.
        :type EndTimeStamp: int
        :param _InstanceId: Instance id (deprecated).
        :type InstanceId: int
        :param _Limit: Maximum number of returned entries (deprecated).
        :type Limit: int
        :param _Offset: Offset (deprecated).
        :type Offset: int
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _PageSize: Page size (required), up to 100.
        :type PageSize: int
        :param _PageNumber: <Page number (required), starting from 0.>.
        :type PageNumber: int
        :param _Phones: Filter by phone number.
        :type Phones: list of str
        :param _SessionIds: Filter by sessionid.
        :type SessionIds: list of str
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._SdkAppId = None
        self._PageSize = None
        self._PageNumber = None
        self._Phones = None
        self._SessionIds = None

    @property
    def StartTimeStamp(self):
        """Start timestamp, unix timestamp in seconds. supports up to the past 180 days.
        :rtype: int
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        """End timestamp, unix timestamp in seconds. the range between the end time and start time is less than 90 days.
        :rtype: int
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        """Instance id (deprecated).
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """Maximum number of returned entries (deprecated).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset (deprecated).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PageSize(self):
        """Page size (required), up to 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """<Page number (required), starting from 0.>.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Phones(self):
        """Filter by phone number.
        :rtype: list of str
        """
        return self._Phones

    @Phones.setter
    def Phones(self, Phones):
        self._Phones = Phones

    @property
    def SessionIds(self):
        """Filter by sessionid.
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SdkAppId = params.get("SdkAppId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Phones = params.get("Phones")
        self._SessionIds = params.get("SessionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCdrResponse(AbstractModel):
    """DescribeTelCdr response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of call records.
        :type TotalCount: int
        :param _TelCdrs: Call record.
        :type TelCdrs: list of TelCdrInfo
        :param _TelCdrList: Call record.
        :type TelCdrList: list of TelCdrInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TelCdrs = None
        self._TelCdrList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of call records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TelCdrs(self):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        """Call record.
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrs

    @TelCdrs.setter
    def TelCdrs(self, TelCdrs):
        warnings.warn("parameter `TelCdrs` is deprecated", DeprecationWarning) 

        self._TelCdrs = TelCdrs

    @property
    def TelCdrList(self):
        """Call record.
        :rtype: list of TelCdrInfo
        """
        return self._TelCdrList

    @TelCdrList.setter
    def TelCdrList(self, TelCdrList):
        self._TelCdrList = TelCdrList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self._TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrs.append(obj)
        if params.get("TelCdrList") is not None:
            self._TelCdrList = []
            for item in params.get("TelCdrList"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self._TelCdrList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelRecordAsrRequest(AbstractModel):
    """DescribeTelRecordAsr request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SessionId: Session id.
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """Session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelRecordAsrResponse(AbstractModel):
    """DescribeTelRecordAsr response structure.

    """

    def __init__(self):
        r"""
        :param _AsrDataList: Recording to text information.
        :type AsrDataList: list of AsrData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsrDataList = None
        self._RequestId = None

    @property
    def AsrDataList(self):
        """Recording to text information.
        :rtype: list of AsrData
        """
        return self._AsrDataList

    @AsrDataList.setter
    def AsrDataList(self, AsrDataList):
        self._AsrDataList = AsrDataList

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
        if params.get("AsrDataList") is not None:
            self._AsrDataList = []
            for item in params.get("AsrDataList"):
                obj = AsrData()
                obj._deserialize(item)
                self._AsrDataList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTelSessionRequest(AbstractModel):
    """DescribeTelSession request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SessionId: Session id.
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """Session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelSessionResponse(AbstractModel):
    """DescribeTelSession response structure.

    """

    def __init__(self):
        r"""
        :param _Session: Session information.
        :type Session: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        """Session information.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

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
        if params.get("Session") is not None:
            self._Session = PSTNSession()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DisableCCCPhoneNumberRequest(AbstractModel):
    """DisableCCCPhoneNumber request structure.

    """

    def __init__(self):
        r"""
        :param _PhoneNumbers: Number list starting with 0086.
        :type PhoneNumbers: list of str
        :param _Disabled: Disable switch: 0 for enable, 1 for disable.
        :type Disabled: int
        :param _SdkAppId: TCCC instance application id.
        :type SdkAppId: int
        """
        self._PhoneNumbers = None
        self._Disabled = None
        self._SdkAppId = None

    @property
    def PhoneNumbers(self):
        """Number list starting with 0086.
        :rtype: list of str
        """
        return self._PhoneNumbers

    @PhoneNumbers.setter
    def PhoneNumbers(self, PhoneNumbers):
        self._PhoneNumbers = PhoneNumbers

    @property
    def Disabled(self):
        """Disable switch: 0 for enable, 1 for disable.
        :rtype: int
        """
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def SdkAppId(self):
        """TCCC instance application id.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._PhoneNumbers = params.get("PhoneNumbers")
        self._Disabled = params.get("Disabled")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCCCPhoneNumberResponse(AbstractModel):
    """DisableCCCPhoneNumber response structure.

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


class ErrStaffItem(AbstractModel):
    """When adding customer service personnel in batches, information of the customer service personnel with an error is returned.

    """

    def __init__(self):
        r"""
        :param _StaffEmail: Agent email address.
        :type StaffEmail: str
        :param _Code: Error code.
        :type Code: str
        :param _Message: Error description.
        :type Message: str
        """
        self._StaffEmail = None
        self._Code = None
        self._Message = None

    @property
    def StaffEmail(self):
        """Agent email address.
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def Code(self):
        """Error code.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """Error description.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._StaffEmail = params.get("StaffEmail")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionInfo(AbstractModel):
    """Telephone information.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Instance id.
        :type SdkAppId: int
        :param _FullExtensionId: Extension full name.
        :type FullExtensionId: str
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        :param _SkillGroupId: Affiliated skill group list.
        :type SkillGroupId: str
        :param _ExtensionName: Extension name.
        :type ExtensionName: str
        :param _CreateTime: Creation time.
        :type CreateTime: int
        :param _ModifyTime: Last modification time.
        :type ModifyTime: int
        :param _Status: Telephone status (0 offline, 100 free, 200 busy).
        :type Status: int
        :param _Register: Whether to register.
        :type Register: bool
        :param _Relation: Bind agent email.
        :type Relation: str
        :param _RelationName: Bind agent name.
        :type RelationName: str
        """
        self._SdkAppId = None
        self._FullExtensionId = None
        self._ExtensionId = None
        self._SkillGroupId = None
        self._ExtensionName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Status = None
        self._Register = None
        self._Relation = None
        self._RelationName = None

    @property
    def SdkAppId(self):
        """Instance id.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def FullExtensionId(self):
        """Extension full name.
        :rtype: str
        """
        return self._FullExtensionId

    @FullExtensionId.setter
    def FullExtensionId(self, FullExtensionId):
        self._FullExtensionId = FullExtensionId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def SkillGroupId(self):
        """Affiliated skill group list.
        :rtype: str
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def ExtensionName(self):
        """Extension name.
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """Last modification time.
        :rtype: int
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Status(self):
        """Telephone status (0 offline, 100 free, 200 busy).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Register(self):
        """Whether to register.
        :rtype: bool
        """
        return self._Register

    @Register.setter
    def Register(self, Register):
        self._Register = Register

    @property
    def Relation(self):
        """Bind agent email.
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def RelationName(self):
        """Bind agent name.
        :rtype: str
        """
        return self._RelationName

    @RelationName.setter
    def RelationName(self, RelationName):
        self._RelationName = RelationName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._FullExtensionId = params.get("FullExtensionId")
        self._ExtensionId = params.get("ExtensionId")
        self._SkillGroupId = params.get("SkillGroupId")
        self._ExtensionName = params.get("ExtensionName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Status = params.get("Status")
        self._Register = params.get("Register")
        self._Relation = params.get("Relation")
        self._RelationName = params.get("RelationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HangUpCallRequest(AbstractModel):
    """HangUpCall request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SessionId: Session id.
        :type SessionId: str
        """
        self._SdkAppId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """Session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HangUpCallResponse(AbstractModel):
    """HangUpCall response structure.

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


class IVRKeyPressedElement(AbstractModel):
    """IVR Key Information.

    """

    def __init__(self):
        r"""
        :param _Key: Hit keyword or press.
        :type Key: str
        :param _Label: Tag associated with the key.
        :type Label: str
        :param _Timestamp: UNIX millisecond timestamp.
        :type Timestamp: int
        :param _NodeLabel: Node tags.
        :type NodeLabel: str
        :param _OriginalContent: User'S original input.
        :type OriginalContent: str
        :param _TTSPrompt: TTS prompt content.
        :type TTSPrompt: str
        """
        self._Key = None
        self._Label = None
        self._Timestamp = None
        self._NodeLabel = None
        self._OriginalContent = None
        self._TTSPrompt = None

    @property
    def Key(self):
        """Hit keyword or press.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Label(self):
        """Tag associated with the key.
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Timestamp(self):
        """UNIX millisecond timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def NodeLabel(self):
        """Node tags.
        :rtype: str
        """
        return self._NodeLabel

    @NodeLabel.setter
    def NodeLabel(self, NodeLabel):
        self._NodeLabel = NodeLabel

    @property
    def OriginalContent(self):
        """User'S original input.
        :rtype: str
        """
        return self._OriginalContent

    @OriginalContent.setter
    def OriginalContent(self, OriginalContent):
        self._OriginalContent = OriginalContent

    @property
    def TTSPrompt(self):
        """TTS prompt content.
        :rtype: str
        """
        return self._TTSPrompt

    @TTSPrompt.setter
    def TTSPrompt(self, TTSPrompt):
        self._TTSPrompt = TTSPrompt


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Label = params.get("Label")
        self._Timestamp = params.get("Timestamp")
        self._NodeLabel = params.get("NodeLabel")
        self._OriginalContent = params.get("OriginalContent")
        self._TTSPrompt = params.get("TTSPrompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtensionRequest(AbstractModel):
    """ModifyExtension request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        :param _ExtensionName: Extension name.
        :type ExtensionName: str
        :param _SkillGroupIds: Affiliated skill group list.
        :type SkillGroupIds: list of int
        :param _Relation: Bind agent email account.
        :type Relation: str
        """
        self._SdkAppId = None
        self._ExtensionId = None
        self._ExtensionName = None
        self._SkillGroupIds = None
        self._Relation = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionName(self):
        """Extension name.
        :rtype: str
        """
        return self._ExtensionName

    @ExtensionName.setter
    def ExtensionName(self, ExtensionName):
        self._ExtensionName = ExtensionName

    @property
    def SkillGroupIds(self):
        """Affiliated skill group list.
        :rtype: list of int
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def Relation(self):
        """Bind agent email account.
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionName = params.get("ExtensionName")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtensionResponse(AbstractModel):
    """ModifyExtension response structure.

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


class ModifyOwnNumberApplyRequest(AbstractModel):
    """ModifyOwnNumberApply request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _DetailList: Circuit-Related parameters.
        :type DetailList: list of OwnNumberApplyDetailItem
        :param _ApplyId: Approval id.
        :type ApplyId: int
        :param _Prefix: Prefix for sending numbers.
        :type Prefix: str
        """
        self._SdkAppId = None
        self._DetailList = None
        self._ApplyId = None
        self._Prefix = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def DetailList(self):
        """Circuit-Related parameters.
        :rtype: list of OwnNumberApplyDetailItem
        """
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def ApplyId(self):
        """Approval id.
        :rtype: int
        """
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId

    @property
    def Prefix(self):
        """Prefix for sending numbers.
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = OwnNumberApplyDetailItem()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._ApplyId = params.get("ApplyId")
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnNumberApplyResponse(AbstractModel):
    """ModifyOwnNumberApply response structure.

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


class ModifyStaffPasswordRequest(AbstractModel):
    """ModifyStaffPassword request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Email: Agent email.
        :type Email: str
        :param _Password: The set password.
        :type Password: str
        """
        self._SdkAppId = None
        self._Email = None
        self._Password = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Email(self):
        """Agent email.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Password(self):
        """The set password.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Email = params.get("Email")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStaffPasswordResponse(AbstractModel):
    """ModifyStaffPassword response structure.

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


class ModifyStaffRequest(AbstractModel):
    """ModifyStaff request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Email: Agent account.
        :type Email: str
        :param _Name: Agent name.
        :type Name: str
        :param _Phone: Agent phone number (preceded by 0086, example: 008618011111111).
        :type Phone: str
        :param _Nick: Agent nickname.
        :type Nick: str
        :param _StaffNo: Agent id.
        :type StaffNo: str
        :param _SkillGroupIds: Bind skill group id list.
        :type SkillGroupIds: list of int
        :param _UseMobileCallOut: Whether the cell phone outbound call switch is enabled or not.
        :type UseMobileCallOut: bool
        :param _UseMobileAccept: Cell phone answering pattern: 0 - off | 1 - only when offline | 2 - always.
        :type UseMobileAccept: int
        :param _ExtensionNumber: Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :type ExtensionNumber: str
        """
        self._SdkAppId = None
        self._Email = None
        self._Name = None
        self._Phone = None
        self._Nick = None
        self._StaffNo = None
        self._SkillGroupIds = None
        self._UseMobileCallOut = None
        self._UseMobileAccept = None
        self._ExtensionNumber = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Email(self):
        """Agent account.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Name(self):
        """Agent name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        """Agent phone number (preceded by 0086, example: 008618011111111).
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """Agent nickname.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def StaffNo(self):
        """Agent id.
        :rtype: str
        """
        return self._StaffNo

    @StaffNo.setter
    def StaffNo(self, StaffNo):
        self._StaffNo = StaffNo

    @property
    def SkillGroupIds(self):
        """Bind skill group id list.
        :rtype: list of int
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds

    @property
    def UseMobileCallOut(self):
        """Whether the cell phone outbound call switch is enabled or not.
        :rtype: bool
        """
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def UseMobileAccept(self):
        """Cell phone answering pattern: 0 - off | 1 - only when offline | 2 - always.
        :rtype: int
        """
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept

    @property
    def ExtensionNumber(self):
        """Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Email = params.get("Email")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._StaffNo = params.get("StaffNo")
        self._SkillGroupIds = params.get("SkillGroupIds")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._UseMobileAccept = params.get("UseMobileAccept")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStaffResponse(AbstractModel):
    """ModifyStaff response structure.

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


class NumberInfo(AbstractModel):
    """Number information.

    """

    def __init__(self):
        r"""
        :param _Number: Number.
        :type Number: str
        :param _CallOutSkillGroupIds: Bound outbound call skill group.
        :type CallOutSkillGroupIds: list of int non-negative
        :param _State: Number status, 1-normal, 2-disabled due to overdue payment, 4-disabled by the administrator, 5-disabled due to violation.
        :type State: int
        """
        self._Number = None
        self._CallOutSkillGroupIds = None
        self._State = None

    @property
    def Number(self):
        """Number.
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def CallOutSkillGroupIds(self):
        """Bound outbound call skill group.
        :rtype: list of int non-negative
        """
        return self._CallOutSkillGroupIds

    @CallOutSkillGroupIds.setter
    def CallOutSkillGroupIds(self, CallOutSkillGroupIds):
        self._CallOutSkillGroupIds = CallOutSkillGroupIds

    @property
    def State(self):
        """Number status, 1-normal, 2-disabled due to overdue payment, 4-disabled by the administrator, 5-disabled due to violation.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._CallOutSkillGroupIds = params.get("CallOutSkillGroupIds")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnNumberApplyDetailItem(AbstractModel):
    """User-owned number approval detail data type

    """

    def __init__(self):
        r"""
        :param _CallType: Number type: 0 - inbound | 1 - outbound | 2 - inbound and outbound.
        :type CallType: int
        :param _PhoneNumber: Line number.
        :type PhoneNumber: str
        :param _MaxCallCount: Maximum concurrent call number.
        :type MaxCallCount: int
        :param _MaxCallPSec: Maximum number of concurrencies per second.
        :type MaxCallPSec: int
        :param _OutboundCalleeFormat: Outbound called number format, use {+e.164} or {e.164}. 
        :type OutboundCalleeFormat: str
        """
        self._CallType = None
        self._PhoneNumber = None
        self._MaxCallCount = None
        self._MaxCallPSec = None
        self._OutboundCalleeFormat = None

    @property
    def CallType(self):
        """Number type: 0 - inbound | 1 - outbound | 2 - inbound and outbound.
        :rtype: int
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def PhoneNumber(self):
        """Line number.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def MaxCallCount(self):
        """Maximum concurrent call number.
        :rtype: int
        """
        return self._MaxCallCount

    @MaxCallCount.setter
    def MaxCallCount(self, MaxCallCount):
        self._MaxCallCount = MaxCallCount

    @property
    def MaxCallPSec(self):
        """Maximum number of concurrencies per second.
        :rtype: int
        """
        return self._MaxCallPSec

    @MaxCallPSec.setter
    def MaxCallPSec(self, MaxCallPSec):
        self._MaxCallPSec = MaxCallPSec

    @property
    def OutboundCalleeFormat(self):
        """Outbound called number format, use {+e.164} or {e.164}. 
        :rtype: str
        """
        return self._OutboundCalleeFormat

    @OutboundCalleeFormat.setter
    def OutboundCalleeFormat(self, OutboundCalleeFormat):
        self._OutboundCalleeFormat = OutboundCalleeFormat


    def _deserialize(self, params):
        self._CallType = params.get("CallType")
        self._PhoneNumber = params.get("PhoneNumber")
        self._MaxCallCount = params.get("MaxCallCount")
        self._MaxCallPSec = params.get("MaxCallPSec")
        self._OutboundCalleeFormat = params.get("OutboundCalleeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSession(AbstractModel):
    """PSTN session type.

    """

    def __init__(self):
        r"""
        :param _SessionID: Session id.
        :type SessionID: str
        :param _RoomID: Temporary room id for session.
        :type RoomID: str
        :param _Caller: Caller.
        :type Caller: str
        :param _Callee: Called.
        :type Callee: str
        :param _StartTimestamp: Start time. unix timestamp.
        :type StartTimestamp: int
        :param _RingTimestamp: Ring time. unix timestamp.
        :type RingTimestamp: int
        :param _AcceptTimestamp: Answer time. unix timestamp.
        :type AcceptTimestamp: int
        :param _StaffEmail: Agent email.
        :type StaffEmail: str
        :param _StaffNumber: Agent id.
        :type StaffNumber: str
        :param _SessionStatus: Session status.
Ringing - in progress.
SeatJoining - waiting for the agent to answer.
InProgress: in progress.
Finished - completed.
        :type SessionStatus: str
        :param _Direction: Session call direction, 0 - inbound | 1 - outbound.
        :type Direction: int
        :param _OutBoundCaller: The number used for transferring to the external line (outbound caller).
        :type OutBoundCaller: str
        :param _OutBoundCallee: Outbound callee.
        :type OutBoundCallee: str
        :param _ProtectedCaller: Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :type ProtectedCaller: str
        :param _ProtectedCallee: Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._OutBoundCaller = None
        self._OutBoundCallee = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        """Session id.
        :rtype: str
        """
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        """Temporary room id for session.
        :rtype: str
        """
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        """Caller.
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """Called.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        """Start time. unix timestamp.
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def RingTimestamp(self):
        """Ring time. unix timestamp.
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """Answer time. unix timestamp.
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        """Agent email.
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        """Agent id.
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        """Session status.
Ringing - in progress.
SeatJoining - waiting for the agent to answer.
InProgress: in progress.
Finished - completed.
        :rtype: str
        """
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        """Session call direction, 0 - inbound | 1 - outbound.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OutBoundCaller(self):
        """The number used for transferring to the external line (outbound caller).
        :rtype: str
        """
        return self._OutBoundCaller

    @OutBoundCaller.setter
    def OutBoundCaller(self, OutBoundCaller):
        self._OutBoundCaller = OutBoundCaller

    @property
    def OutBoundCallee(self):
        """Outbound callee.
        :rtype: str
        """
        return self._OutBoundCallee

    @OutBoundCallee.setter
    def OutBoundCallee(self, OutBoundCallee):
        self._OutBoundCallee = OutBoundCallee

    @property
    def ProtectedCaller(self):
        """Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._OutBoundCaller = params.get("OutBoundCaller")
        self._OutBoundCallee = params.get("OutBoundCallee")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSessionInfo(AbstractModel):
    """PSTN Session Information.

    """

    def __init__(self):
        r"""
        :param _SessionID: Session id.
        :type SessionID: str
        :param _RoomID: Temporary room id for session.
        :type RoomID: str
        :param _Caller: Caller.
        :type Caller: str
        :param _Callee: Called.
        :type Callee: str
        :param _StartTimestamp: Start time. unix timestamp.
        :type StartTimestamp: str
        :param _AcceptTimestamp: Answer time. unix timestamp.
        :type AcceptTimestamp: str
        :param _StaffEmail: Agent email.
        :type StaffEmail: str
        :param _StaffNumber: Agent id.
        :type StaffNumber: str
        :param _SessionStatus: Agent status inprogress ongoing.
        :type SessionStatus: str
        :param _Direction: Session call direction, 0 - inbound | 1 - outbound.
        :type Direction: int
        :param _RingTimestamp: Ring time. unix timestamp.
        :type RingTimestamp: int
        :param _ProtectedCaller: Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :type ProtectedCaller: str
        :param _ProtectedCallee: Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :type ProtectedCallee: str
        """
        self._SessionID = None
        self._RoomID = None
        self._Caller = None
        self._Callee = None
        self._StartTimestamp = None
        self._AcceptTimestamp = None
        self._StaffEmail = None
        self._StaffNumber = None
        self._SessionStatus = None
        self._Direction = None
        self._RingTimestamp = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None

    @property
    def SessionID(self):
        """Session id.
        :rtype: str
        """
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def RoomID(self):
        """Temporary room id for session.
        :rtype: str
        """
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID

    @property
    def Caller(self):
        """Caller.
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """Called.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def StartTimestamp(self):
        """Start time. unix timestamp.
        :rtype: str
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def AcceptTimestamp(self):
        """Answer time. unix timestamp.
        :rtype: str
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def StaffEmail(self):
        """Agent email.
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def StaffNumber(self):
        """Agent id.
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def SessionStatus(self):
        """Agent status inprogress ongoing.
        :rtype: str
        """
        return self._SessionStatus

    @SessionStatus.setter
    def SessionStatus(self, SessionStatus):
        self._SessionStatus = SessionStatus

    @property
    def Direction(self):
        """Session call direction, 0 - inbound | 1 - outbound.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RingTimestamp(self):
        """Ring time. unix timestamp.
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def ProtectedCaller(self):
        """Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee


    def _deserialize(self, params):
        self._SessionID = params.get("SessionID")
        self._RoomID = params.get("RoomID")
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._StartTimestamp = params.get("StartTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._StaffEmail = params.get("StaffEmail")
        self._StaffNumber = params.get("StaffNumber")
        self._SessionStatus = params.get("SessionStatus")
        self._Direction = params.get("Direction")
        self._RingTimestamp = params.get("RingTimestamp")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageBuyInfo(AbstractModel):
    """Package purchase information.

    """

    def __init__(self):
        r"""
        :param _PackageId: Package id.
        :type PackageId: str
        :param _Type: Package type, 0 - outbound call package | 1 - 400 inbound call package.
        :type Type: int
        :param _CapacitySize: <TOTAL_PACKAGE>.
        :type CapacitySize: int
        :param _CapacityRemain: Remaining package balance.
        :type CapacityRemain: int
        :param _BuyTime: Purchased timestamp.
        :type BuyTime: int
        :param _EndTime: Deadline timestamp.
        :type EndTime: int
        """
        self._PackageId = None
        self._Type = None
        self._CapacitySize = None
        self._CapacityRemain = None
        self._BuyTime = None
        self._EndTime = None

    @property
    def PackageId(self):
        """Package id.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Type(self):
        """Package type, 0 - outbound call package | 1 - 400 inbound call package.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CapacitySize(self):
        """<TOTAL_PACKAGE>.
        :rtype: int
        """
        return self._CapacitySize

    @CapacitySize.setter
    def CapacitySize(self, CapacitySize):
        self._CapacitySize = CapacitySize

    @property
    def CapacityRemain(self):
        """Remaining package balance.
        :rtype: int
        """
        return self._CapacityRemain

    @CapacityRemain.setter
    def CapacityRemain(self, CapacityRemain):
        self._CapacityRemain = CapacityRemain

    @property
    def BuyTime(self):
        """Purchased timestamp.
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """Deadline timestamp.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._Type = params.get("Type")
        self._CapacitySize = params.get("CapacitySize")
        self._CapacityRemain = params.get("CapacityRemain")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PausePredictiveDialingCampaignRequest(AbstractModel):
    """PausePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: Task id.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """Task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PausePredictiveDialingCampaignResponse(AbstractModel):
    """PausePredictiveDialingCampaign response structure.

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


class PhoneNumBuyInfo(AbstractModel):
    """Number purchase information.

    """

    def __init__(self):
        r"""
        :param _PhoneNum: Telephone number.
        :type PhoneNum: str
        :param _Type: Number type, 0 - landline | 1 - virtual business number | 2 - ISP number | 3 - 400 number.
        :type Type: int
        :param _CallType: Call type of the number, 1 - inbound | 2 - outbound | 3 - inbound and outbound.
        :type CallType: int
        :param _BuyTime: Purchased timestamp.
        :type BuyTime: int
        :param _EndTime: Deadline timestamp.
        :type EndTime: int
        :param _State: Number status, 1-normal | 2-suspended due to non-payment | 4-admin suspended | 5-suspended due to violation.
        :type State: int
        """
        self._PhoneNum = None
        self._Type = None
        self._CallType = None
        self._BuyTime = None
        self._EndTime = None
        self._State = None

    @property
    def PhoneNum(self):
        """Telephone number.
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Type(self):
        """Number type, 0 - landline | 1 - virtual business number | 2 - ISP number | 3 - 400 number.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CallType(self):
        """Call type of the number, 1 - inbound | 2 - outbound | 3 - inbound and outbound.
        :rtype: int
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def BuyTime(self):
        """Purchased timestamp.
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """Deadline timestamp.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        """Number status, 1-normal | 2-suspended due to non-payment | 4-admin suspended | 5-suspended due to violation.
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._PhoneNum = params.get("PhoneNum")
        self._Type = params.get("Type")
        self._CallType = params.get("CallType")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordRequest(AbstractModel):
    """ResetExtensionPassword request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _ExtensionId: Extension.
        :type ExtensionId: str
        """
        self._SdkAppId = None
        self._ExtensionId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def ExtensionId(self):
        """Extension.
        :rtype: str
        """
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._ExtensionId = params.get("ExtensionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetExtensionPasswordResponse(AbstractModel):
    """ResetExtensionPassword response structure.

    """

    def __init__(self):
        r"""
        :param _Password: Reset password.
        :type Password: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        """Reset password.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

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
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class ResumePredictiveDialingCampaignRequest(AbstractModel):
    """ResumePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: <Task id>.
        :type CampaignId: int
        """
        self._SdkAppId = None
        self._CampaignId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """<Task id>.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumePredictiveDialingCampaignResponse(AbstractModel):
    """ResumePredictiveDialingCampaign response structure.

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


class SdkAppIdBuyInfo(AbstractModel):
    """Application purchase information.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id.
        :type SdkAppId: int
        :param _Name: Application name.
        :type Name: str
        :param _StaffBuyNum: Agent purchase count (still within the validity period).
        :type StaffBuyNum: int
        :param _StaffBuyList: Agent purchase list (still within the validity period).
        :type StaffBuyList: list of StaffBuyInfo
        :param _PhoneNumBuyList: List of numbers purchased.
        :type PhoneNumBuyList: list of PhoneNumBuyInfo
        :param _SipBuyNum: Number of office telephones purchased (still within the validity period).
        :type SipBuyNum: int
        """
        self._SdkAppId = None
        self._Name = None
        self._StaffBuyNum = None
        self._StaffBuyList = None
        self._PhoneNumBuyList = None
        self._SipBuyNum = None

    @property
    def SdkAppId(self):
        """Application id.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

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
    def StaffBuyNum(self):
        """Agent purchase count (still within the validity period).
        :rtype: int
        """
        return self._StaffBuyNum

    @StaffBuyNum.setter
    def StaffBuyNum(self, StaffBuyNum):
        self._StaffBuyNum = StaffBuyNum

    @property
    def StaffBuyList(self):
        """Agent purchase list (still within the validity period).
        :rtype: list of StaffBuyInfo
        """
        return self._StaffBuyList

    @StaffBuyList.setter
    def StaffBuyList(self, StaffBuyList):
        self._StaffBuyList = StaffBuyList

    @property
    def PhoneNumBuyList(self):
        """List of numbers purchased.
        :rtype: list of PhoneNumBuyInfo
        """
        return self._PhoneNumBuyList

    @PhoneNumBuyList.setter
    def PhoneNumBuyList(self, PhoneNumBuyList):
        self._PhoneNumBuyList = PhoneNumBuyList

    @property
    def SipBuyNum(self):
        """Number of office telephones purchased (still within the validity period).
        :rtype: int
        """
        return self._SipBuyNum

    @SipBuyNum.setter
    def SipBuyNum(self, SipBuyNum):
        self._SipBuyNum = SipBuyNum


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._StaffBuyNum = params.get("StaffBuyNum")
        if params.get("StaffBuyList") is not None:
            self._StaffBuyList = []
            for item in params.get("StaffBuyList"):
                obj = StaffBuyInfo()
                obj._deserialize(item)
                self._StaffBuyList.append(obj)
        if params.get("PhoneNumBuyList") is not None:
            self._PhoneNumBuyList = []
            for item in params.get("PhoneNumBuyList"):
                obj = PhoneNumBuyInfo()
                obj._deserialize(item)
                self._PhoneNumBuyList.append(obj)
        self._SipBuyNum = params.get("SipBuyNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeatUserInfo(AbstractModel):
    """Agent User Information

    """

    def __init__(self):
        r"""
        :param _Name: Agent name.
        :type Name: str
        :param _Mail: Agent email.
        :type Mail: str
        :param _StaffNumber: Worker number.
        :type StaffNumber: str
        :param _Phone: Agent'S telephone number (with 0086 prefix).
        :type Phone: str
        :param _Nick: Agent nickname.
        :type Nick: str
        :param _UserId: User id.
        :type UserId: str
        :param _SkillGroupNameList: List of skill groups associated with the agent.
        :type SkillGroupNameList: list of str
        :param _Role: 1: admin.
2: quality inspector.
3: ordinary agent.
Else: custom role id.
        :type Role: int
        :param _ExtensionNumber: Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :type ExtensionNumber: str
        """
        self._Name = None
        self._Mail = None
        self._StaffNumber = None
        self._Phone = None
        self._Nick = None
        self._UserId = None
        self._SkillGroupNameList = None
        self._Role = None
        self._ExtensionNumber = None

    @property
    def Name(self):
        """Agent name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """Agent email.
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def StaffNumber(self):
        """Worker number.
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def Phone(self):
        """Agent'S telephone number (with 0086 prefix).
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """Agent nickname.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def UserId(self):
        """User id.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SkillGroupNameList(self):
        """List of skill groups associated with the agent.
        :rtype: list of str
        """
        return self._SkillGroupNameList

    @SkillGroupNameList.setter
    def SkillGroupNameList(self, SkillGroupNameList):
        self._SkillGroupNameList = SkillGroupNameList

    @property
    def Role(self):
        """1: admin.
2: quality inspector.
3: ordinary agent.
Else: custom role id.
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def ExtensionNumber(self):
        """Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._StaffNumber = params.get("StaffNumber")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._UserId = params.get("UserId")
        self._SkillGroupNameList = params.get("SkillGroupNameList")
        self._Role = params.get("Role")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServeParticipant(AbstractModel):
    """Participant information.

    """

    def __init__(self):
        r"""
        :param _Mail: Agent email.
        :type Mail: str
        :param _Phone: Agent phone number.
        :type Phone: str
        :param _RingTimestamp: Ringing timestamp, unix second-level timestamp.
        :type RingTimestamp: int
        :param _AcceptTimestamp: Answer timestamp. unix second-level timestamp.
        :type AcceptTimestamp: int
        :param _EndedTimestamp: End timestamp. unix second-level timestamp.
        :type EndedTimestamp: int
        :param _RecordId: Recording id can be indexed to the agent side recording.
        :type RecordId: str
        :param _Type: Participant type: "staffseat", "outboundseat", "staffphoneseat".
        :type Type: str
        :param _TransferFrom: Transfer source agent information.
        :type TransferFrom: str
        :param _TransferFromType: Transfer source participant type is consistent with the type value.
        :type TransferFromType: str
        :param _TransferTo: Transfer destination agent information.
        :type TransferTo: str
        :param _TransferToType: Transfer destination participant type, which is consistent with type values.
        :type TransferToType: str
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _EndStatusString: Ending status.
        :type EndStatusString: str
        :param _RecordURL: Recording url.
        :type RecordURL: str
        :param _Sequence: Participant sequence number, starting from 0.
        :type Sequence: int
        :param _StartTimestamp: Start timestamp. unix second-level timestamp.
        :type StartTimestamp: int
        :param _SkillGroupName: Skill group name.
        :type SkillGroupName: str
        :param _CustomRecordURL: Address of the third-party cos for transferring recording.
        :type CustomRecordURL: str
        """
        self._Mail = None
        self._Phone = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._RecordId = None
        self._Type = None
        self._TransferFrom = None
        self._TransferFromType = None
        self._TransferTo = None
        self._TransferToType = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._RecordURL = None
        self._Sequence = None
        self._StartTimestamp = None
        self._SkillGroupName = None
        self._CustomRecordURL = None

    @property
    def Mail(self):
        """Agent email.
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        """Agent phone number.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def RingTimestamp(self):
        """Ringing timestamp, unix second-level timestamp.
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """Answer timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        """End timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def RecordId(self):
        """Recording id can be indexed to the agent side recording.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Type(self):
        """Participant type: "staffseat", "outboundseat", "staffphoneseat".
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TransferFrom(self):
        """Transfer source agent information.
        :rtype: str
        """
        return self._TransferFrom

    @TransferFrom.setter
    def TransferFrom(self, TransferFrom):
        self._TransferFrom = TransferFrom

    @property
    def TransferFromType(self):
        """Transfer source participant type is consistent with the type value.
        :rtype: str
        """
        return self._TransferFromType

    @TransferFromType.setter
    def TransferFromType(self, TransferFromType):
        self._TransferFromType = TransferFromType

    @property
    def TransferTo(self):
        """Transfer destination agent information.
        :rtype: str
        """
        return self._TransferTo

    @TransferTo.setter
    def TransferTo(self, TransferTo):
        self._TransferTo = TransferTo

    @property
    def TransferToType(self):
        """Transfer destination participant type, which is consistent with type values.
        :rtype: str
        """
        return self._TransferToType

    @TransferToType.setter
    def TransferToType(self, TransferToType):
        self._TransferToType = TransferToType

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        """Ending status.
        :rtype: str
        """
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def RecordURL(self):
        """Recording url.
        :rtype: str
        """
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def Sequence(self):
        """Participant sequence number, starting from 0.
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def StartTimestamp(self):
        """Start timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def SkillGroupName(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def CustomRecordURL(self):
        """Address of the third-party cos for transferring recording.
        :rtype: str
        """
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL


    def _deserialize(self, params):
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._RecordId = params.get("RecordId")
        self._Type = params.get("Type")
        self._TransferFrom = params.get("TransferFrom")
        self._TransferFromType = params.get("TransferFromType")
        self._TransferTo = params.get("TransferTo")
        self._TransferToType = params.get("TransferToType")
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._RecordURL = params.get("RecordURL")
        self._Sequence = params.get("Sequence")
        self._StartTimestamp = params.get("StartTimestamp")
        self._SkillGroupName = params.get("SkillGroupName")
        self._CustomRecordURL = params.get("CustomRecordURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupInfoItem(AbstractModel):
    """Skill group information.

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _SkillGroupName: Skill group name.
        :type SkillGroupName: str
        :param _Type: (Deprecated) type: im, tel, all (full media).
        :type Type: str
        :param _RoutePolicy: Session allocation policy.
        :type RoutePolicy: str
        :param _UsingLastSeat: Whether the session is allocated to the last serviced agent first.
        :type UsingLastSeat: int
        :param _MaxConcurrency: Maximum concurrency number of single client service (default 1 for telephone type).
        :type MaxConcurrency: int
        :param _LastModifyTimestamp: Last modification time.
        :type LastModifyTimestamp: int
        :param _SkillGroupType: Skill group type 0-cell phone, 1-online, 3-audio, 4-video.	.	
        :type SkillGroupType: int
        :param _Alias: Intra-Skill group line number.
        :type Alias: str
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Type = None
        self._RoutePolicy = None
        self._UsingLastSeat = None
        self._MaxConcurrency = None
        self._LastModifyTimestamp = None
        self._SkillGroupType = None
        self._Alias = None

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Type(self):
        """(Deprecated) type: im, tel, all (full media).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RoutePolicy(self):
        """Session allocation policy.
        :rtype: str
        """
        return self._RoutePolicy

    @RoutePolicy.setter
    def RoutePolicy(self, RoutePolicy):
        self._RoutePolicy = RoutePolicy

    @property
    def UsingLastSeat(self):
        """Whether the session is allocated to the last serviced agent first.
        :rtype: int
        """
        return self._UsingLastSeat

    @UsingLastSeat.setter
    def UsingLastSeat(self, UsingLastSeat):
        self._UsingLastSeat = UsingLastSeat

    @property
    def MaxConcurrency(self):
        """Maximum concurrency number of single client service (default 1 for telephone type).
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def LastModifyTimestamp(self):
        """Last modification time.
        :rtype: int
        """
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def SkillGroupType(self):
        """Skill group type 0-cell phone, 1-online, 3-audio, 4-video.	.	
        :rtype: int
        """
        return self._SkillGroupType

    @SkillGroupType.setter
    def SkillGroupType(self, SkillGroupType):
        self._SkillGroupType = SkillGroupType

    @property
    def Alias(self):
        """Intra-Skill group line number.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Type = params.get("Type")
        self._RoutePolicy = params.get("RoutePolicy")
        self._UsingLastSeat = params.get("UsingLastSeat")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._SkillGroupType = params.get("SkillGroupType")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupItem(AbstractModel):
    """Skill group information.

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _SkillGroupName: Skill group name.
        :type SkillGroupName: str
        :param _Priority: Priority.
        :type Priority: int
        :param _Type: Type: im, tel, all (full media).
        :type Type: str
        """
        self._SkillGroupId = None
        self._SkillGroupName = None
        self._Priority = None
        self._Type = None

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def SkillGroupName(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def Priority(self):
        """Priority.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Type(self):
        """Type: im, tel, all (full media).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._SkillGroupName = params.get("SkillGroupName")
        self._Priority = params.get("Priority")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffBuyInfo(AbstractModel):
    """Agent purchase information

    """

    def __init__(self):
        r"""
        :param _Num: Number of agents purchased.
        :type Num: int
        :param _BuyTime: Purchased timestamp.
        :type BuyTime: int
        :param _EndTime: Deadline timestamp.
        :type EndTime: int
        :param _SipNum: Quantity of office telephones purchased.
        :type SipNum: int
        """
        self._Num = None
        self._BuyTime = None
        self._EndTime = None
        self._SipNum = None

    @property
    def Num(self):
        """Number of agents purchased.
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def BuyTime(self):
        """Purchased timestamp.
        :rtype: int
        """
        return self._BuyTime

    @BuyTime.setter
    def BuyTime(self, BuyTime):
        self._BuyTime = BuyTime

    @property
    def EndTime(self):
        """Deadline timestamp.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SipNum(self):
        """Quantity of office telephones purchased.
        :rtype: int
        """
        return self._SipNum

    @SipNum.setter
    def SipNum(self, SipNum):
        self._SipNum = SipNum


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._BuyTime = params.get("BuyTime")
        self._EndTime = params.get("EndTime")
        self._SipNum = params.get("SipNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffInfo(AbstractModel):
    """Agent Information with Skill Group Priority

    """

    def __init__(self):
        r"""
        :param _Name: Agent name.
        :type Name: str
        :param _Mail: Agent email.
        :type Mail: str
        :param _Phone: Agent phone number.
        :type Phone: str
        :param _Nick: Agent nickname.
        :type Nick: str
        :param _StaffNumber: Agent id.
        :type StaffNumber: str
        :param _RoleId: User role id.
        :type RoleId: int
        :param _SkillGroupList: Affiliated skill group list.
        :type SkillGroupList: list of SkillGroupItem
        :param _LastModifyTimestamp: Last modification time.
        :type LastModifyTimestamp: int
        :param _ExtensionNumber: Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :type ExtensionNumber: str
        """
        self._Name = None
        self._Mail = None
        self._Phone = None
        self._Nick = None
        self._StaffNumber = None
        self._RoleId = None
        self._SkillGroupList = None
        self._LastModifyTimestamp = None
        self._ExtensionNumber = None

    @property
    def Name(self):
        """Agent name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """Agent email.
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Phone(self):
        """Agent phone number.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """Agent nickname.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def StaffNumber(self):
        """Agent id.
        :rtype: str
        """
        return self._StaffNumber

    @StaffNumber.setter
    def StaffNumber(self, StaffNumber):
        self._StaffNumber = StaffNumber

    @property
    def RoleId(self):
        warnings.warn("parameter `RoleId` is deprecated", DeprecationWarning) 

        """User role id.
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        warnings.warn("parameter `RoleId` is deprecated", DeprecationWarning) 

        self._RoleId = RoleId

    @property
    def SkillGroupList(self):
        """Affiliated skill group list.
        :rtype: list of SkillGroupItem
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList

    @property
    def LastModifyTimestamp(self):
        """Last modification time.
        :rtype: int
        """
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def ExtensionNumber(self):
        """Agent extension number (starting with 1 to 8, 4 - 6 digits).
        :rtype: str
        """
        return self._ExtensionNumber

    @ExtensionNumber.setter
    def ExtensionNumber(self, ExtensionNumber):
        self._ExtensionNumber = ExtensionNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._StaffNumber = params.get("StaffNumber")
        self._RoleId = params.get("RoleId")
        if params.get("SkillGroupList") is not None:
            self._SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupItem()
                obj._deserialize(item)
                self._SkillGroupList.append(obj)
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._ExtensionNumber = params.get("ExtensionNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffSkillGroupList(AbstractModel):
    """Bound skill group list for agents.

    """

    def __init__(self):
        r"""
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _Priority: Priority of the agent in the skill group (1 is the highest, 5 is the lowest, 3 by default).
        :type Priority: int
        """
        self._SkillGroupId = None
        self._Priority = None

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """Priority of the agent in the skill group (1 is the highest, 5 is the lowest, 3 by default).
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusExtra(AbstractModel):
    """Supplementary Information on Agent Status

    """

    def __init__(self):
        r"""
        :param _Type: IM - text | tel - cell phone | all - full media.
        :type Type: str
        :param _Direct: IN - inbound | out - outbound.
        :type Direct: str
        """
        self._Type = None
        self._Direct = None

    @property
    def Type(self):
        """IM - text | tel - cell phone | all - full media.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Direct(self):
        """IN - inbound | out - outbound.
        :rtype: str
        """
        return self._Direct

    @Direct.setter
    def Direct(self, Direct):
        self._Direct = Direct


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Direct = params.get("Direct")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusMetrics(AbstractModel):
    """Agent status-related information

    """

    def __init__(self):
        r"""
        :param _Email: Agent email.
        :type Email: str
        :param _Status: Agent status free available | busy busy | rest on break | notready not ready | aftercallwork post-call adjustment | offline offline.
        :type Status: str
        :param _StatusExtra: Supplementary information on agent status.
        :type StatusExtra: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        :param _OnlineDuration: Total online duration of the day.
        :type OnlineDuration: int
        :param _FreeDuration: Total available duration of the day.
        :type FreeDuration: int
        :param _BusyDuration: Total busy duration of the day.
        :type BusyDuration: int
        :param _NotReadyDuration: Total not ready status duration of the day.
        :type NotReadyDuration: int
        :param _RestDuration: Total break duration of the day.
        :type RestDuration: int
        :param _AfterCallWorkDuration: Adjust the total duration of after-call work for the day.
        :type AfterCallWorkDuration: int
        :param _Reason: Reason for break.
        :type Reason: str
        :param _ReserveRest: Whether to reserve break status.
        :type ReserveRest: bool
        :param _ReserveNotReady: Whether to reserve not ready status.
        :type ReserveNotReady: bool
        :param _UseMobileAccept: Cell phone answering pattern: 0 - off | 1 - only when offline | 2 - always.
        :type UseMobileAccept: int
        :param _UseMobileCallOut: Cell phone outbound call switch.
        :type UseMobileCallOut: bool
        :param _LastOnlineTimestamp: Last online timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastOnlineTimestamp: int
        :param _LastStatusTimestamp: Last status timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastStatusTimestamp: int
        """
        self._Email = None
        self._Status = None
        self._StatusExtra = None
        self._OnlineDuration = None
        self._FreeDuration = None
        self._BusyDuration = None
        self._NotReadyDuration = None
        self._RestDuration = None
        self._AfterCallWorkDuration = None
        self._Reason = None
        self._ReserveRest = None
        self._ReserveNotReady = None
        self._UseMobileAccept = None
        self._UseMobileCallOut = None
        self._LastOnlineTimestamp = None
        self._LastStatusTimestamp = None

    @property
    def Email(self):
        """Agent email.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        """Agent status free available | busy busy | rest on break | notready not ready | aftercallwork post-call adjustment | offline offline.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusExtra(self):
        """Supplementary information on agent status.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        """
        return self._StatusExtra

    @StatusExtra.setter
    def StatusExtra(self, StatusExtra):
        self._StatusExtra = StatusExtra

    @property
    def OnlineDuration(self):
        """Total online duration of the day.
        :rtype: int
        """
        return self._OnlineDuration

    @OnlineDuration.setter
    def OnlineDuration(self, OnlineDuration):
        self._OnlineDuration = OnlineDuration

    @property
    def FreeDuration(self):
        """Total available duration of the day.
        :rtype: int
        """
        return self._FreeDuration

    @FreeDuration.setter
    def FreeDuration(self, FreeDuration):
        self._FreeDuration = FreeDuration

    @property
    def BusyDuration(self):
        """Total busy duration of the day.
        :rtype: int
        """
        return self._BusyDuration

    @BusyDuration.setter
    def BusyDuration(self, BusyDuration):
        self._BusyDuration = BusyDuration

    @property
    def NotReadyDuration(self):
        """Total not ready status duration of the day.
        :rtype: int
        """
        return self._NotReadyDuration

    @NotReadyDuration.setter
    def NotReadyDuration(self, NotReadyDuration):
        self._NotReadyDuration = NotReadyDuration

    @property
    def RestDuration(self):
        """Total break duration of the day.
        :rtype: int
        """
        return self._RestDuration

    @RestDuration.setter
    def RestDuration(self, RestDuration):
        self._RestDuration = RestDuration

    @property
    def AfterCallWorkDuration(self):
        """Adjust the total duration of after-call work for the day.
        :rtype: int
        """
        return self._AfterCallWorkDuration

    @AfterCallWorkDuration.setter
    def AfterCallWorkDuration(self, AfterCallWorkDuration):
        self._AfterCallWorkDuration = AfterCallWorkDuration

    @property
    def Reason(self):
        """Reason for break.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReserveRest(self):
        """Whether to reserve break status.
        :rtype: bool
        """
        return self._ReserveRest

    @ReserveRest.setter
    def ReserveRest(self, ReserveRest):
        self._ReserveRest = ReserveRest

    @property
    def ReserveNotReady(self):
        """Whether to reserve not ready status.
        :rtype: bool
        """
        return self._ReserveNotReady

    @ReserveNotReady.setter
    def ReserveNotReady(self, ReserveNotReady):
        self._ReserveNotReady = ReserveNotReady

    @property
    def UseMobileAccept(self):
        """Cell phone answering pattern: 0 - off | 1 - only when offline | 2 - always.
        :rtype: int
        """
        return self._UseMobileAccept

    @UseMobileAccept.setter
    def UseMobileAccept(self, UseMobileAccept):
        self._UseMobileAccept = UseMobileAccept

    @property
    def UseMobileCallOut(self):
        """Cell phone outbound call switch.
        :rtype: bool
        """
        return self._UseMobileCallOut

    @UseMobileCallOut.setter
    def UseMobileCallOut(self, UseMobileCallOut):
        self._UseMobileCallOut = UseMobileCallOut

    @property
    def LastOnlineTimestamp(self):
        """Last online timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LastOnlineTimestamp

    @LastOnlineTimestamp.setter
    def LastOnlineTimestamp(self, LastOnlineTimestamp):
        self._LastOnlineTimestamp = LastOnlineTimestamp

    @property
    def LastStatusTimestamp(self):
        """Last status timestamp.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LastStatusTimestamp

    @LastStatusTimestamp.setter
    def LastStatusTimestamp(self, LastStatusTimestamp):
        self._LastStatusTimestamp = LastStatusTimestamp


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        if params.get("StatusExtra") is not None:
            self._StatusExtra = StaffStatusExtra()
            self._StatusExtra._deserialize(params.get("StatusExtra"))
        self._OnlineDuration = params.get("OnlineDuration")
        self._FreeDuration = params.get("FreeDuration")
        self._BusyDuration = params.get("BusyDuration")
        self._NotReadyDuration = params.get("NotReadyDuration")
        self._RestDuration = params.get("RestDuration")
        self._AfterCallWorkDuration = params.get("AfterCallWorkDuration")
        self._Reason = params.get("Reason")
        self._ReserveRest = params.get("ReserveRest")
        self._ReserveNotReady = params.get("ReserveNotReady")
        self._UseMobileAccept = params.get("UseMobileAccept")
        self._UseMobileCallOut = params.get("UseMobileCallOut")
        self._LastOnlineTimestamp = params.get("LastOnlineTimestamp")
        self._LastStatusTimestamp = params.get("LastStatusTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoCalloutTaskRequest(AbstractModel):
    """StopAutoCalloutTask request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _TaskId: Task id.
        :type TaskId: int
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """Task id.
        :rtype: int
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
        


class StopAutoCalloutTaskResponse(AbstractModel):
    """StopAutoCalloutTask response structure.

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


class TelCdrInfo(AbstractModel):
    """Phone call information

    """

    def __init__(self):
        r"""
        :param _Caller: Caller number.
        :type Caller: str
        :param _Callee: Called number.
        :type Callee: str
        :param _Time: Call initiation timestamp, unix timestamp.
        :type Time: int
        :param _Direction: Call direction: 0 - inbound, 1 - outbound.
        :type Direction: int
        :param _Duration: Call duration.
        :type Duration: int
        :param _RecordURL: Recording information.
        :type RecordURL: str
        :param _RecordId: Recording id.
        :type RecordId: str
        :param _SeatUser: Agent information.
        :type SeatUser: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        :param _EndStatus: EndStatus corresponds one-to-one with endstatusstring, with specific enumerations as follows:.

**Scenario	EndStatus	EndStatusString	Status description**.

Inbound call & call	1	ok	end properly.

Inbound call & call | 0 | error | system error.

Inbound call | 102 | ivrgiveup | user gives up during ivr.

Inbound call | 103 | waitinggiveup | user gives up during session queue.

Inbound call | 104 | ringinggiveup | user gives up during session ringing.

Inbound call | 105 | noseatonline | no agent online.

Inbound call              106	       non - working hour      non - working hour.   

Inbound call              107	       ivrend                   end directly after ivr.

Inbound call              100	       blocklist call - in      call - in blocklist. 

Outgoing call            2                 unconnected            unconnected.

Outgoing call            108           restricted callee      callee restricted due to high - risk.

Outgoing call         109        toomanyrequest        overfrequency.

Outgoing call         110        restrictedarea        outbound blind area.

Outgoing call         111        restrictedtime        outbound time restriction.
                         
Outgoing call         201        unknown               unknown status.

Outgoing call         202        notanswer             unanswered.

Outgoing call - 203 - userreject: reject call.

Outgoing call - 204 - poweroff: power off.

Outgoing call - 205 - numbernotexist: nonexistent number.

Outgoing call - 206 - busy: call in progress.

Outgoing call - 207 - outofcredit: arrears.

Outgoing call - 208 - operatorerror - ISP line exception.

Outgoing call - 209 - callercancel - caller cancellation.

Outgoing call - 210 - notinservice - not in service area.

Inbound and outgoing call - 211 - clienterror - client error.
Outgoing call - 212 - carrierblocked - ISP blocking.
        :type EndStatus: int
        :param _SkillGroup: Skill group name.
        :type SkillGroup: str
        :param _CallerLocation: Caller'S location.
        :type CallerLocation: str
        :param _IVRDuration: Time spent in ivr stage.
        :type IVRDuration: int
        :param _RingTimestamp: Ring timestamp. unix second-level timestamp.
        :type RingTimestamp: int
        :param _AcceptTimestamp: Answer timestamp. unix second-level timestamp.
        :type AcceptTimestamp: int
        :param _EndedTimestamp: End timestamp. unix second-level timestamp.
        :type EndedTimestamp: int
        :param _IVRKeyPressed: IVR key information, e.g. ["1","2","3"].
        :type IVRKeyPressed: list of str
        :param _HungUpSide: Hang-Up side, seat, user, system.
        :type HungUpSide: str
        :param _ServeParticipants: Service participant list.
        :type ServeParticipants: list of ServeParticipant
        :param _SkillGroupId: Skill group id.
        :type SkillGroupId: int
        :param _EndStatusString: EndStatus corresponds one-to-one with endstatusstring, with specific enumerations as follows:.

**Scenario	EndStatus	EndStatusString	Status description**.

Inbound call & call	1	ok	end properly.

Inbound call & call | 0 | error | system error.

Inbound call | 102 | ivrgiveup | user gives up during ivr.

Inbound call | 103 | waitinggiveup | user gives up during session queue.

Inbound call | 104 | ringinggiveup | user gives up during session ringing.

Inbound call | 105 | noseatonline | no agent online.

Inbound call              106	       non - working hour      non - working hour.   

Inbound call              107	       ivrend                   end directly after ivr.

Inbound call              100	       blocklist call - in      call - in blocklist. 

Outgoing call            2                 unconnected            unconnected.

Outgoing call            108           restricted callee      callee restricted due to high - risk.

Outgoing call         109        toomanyrequest        overfrequency.

Outgoing call         110        restrictedarea        outbound blind area.

Outgoing call         111        restrictedtime        outbound time restriction.
                         
Outgoing call         201        unknown               unknown status.

Outgoing call         202        notanswer             unanswered.

Outgoing call - 203 - userreject: reject call.

Outgoing call - 204 - poweroff: power off.

Outgoing call - 205 - numbernotexist: nonexistent number.

Outgoing call - 206 - busy: call in progress.

Outgoing call - 207 - outofcredit: arrears.

Outgoing call - 208 - operatorerror - ISP line exception.

Outgoing call - 209 - callercancel - caller cancellation.

Outgoing call - 210 - notinservice - not in service area.

Inbound and outgoing call - 211 - clienterror - client error.
Outgoing call - 212 - carrierblocked - ISP blocking.
        :type EndStatusString: str
        :param _StartTimestamp: Session start timestamp. unix second-level timestamp.
        :type StartTimestamp: int
        :param _QueuedTimestamp: Queue entry time. unix second-level timestamp.
        :type QueuedTimestamp: int
        :param _PostIVRKeyPressed: Post-IVR key information (e.g. [{"key":"1","label":"very satisfied"}]).
        :type PostIVRKeyPressed: list of IVRKeyPressedElement
        :param _QueuedSkillGroupId: Queue skill group id.
        :type QueuedSkillGroupId: int
        :param _SessionId: Session id.
        :type SessionId: str
        :param _ProtectedCaller: Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :type ProtectedCaller: str
        :param _ProtectedCallee: Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :type ProtectedCallee: str
        :param _Uui: Customer custom data. (user - to - user interface).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Uui: str
        :param _UUI: Customer custom data. (user - to - user interface).
        :type UUI: str
        :param _IVRKeyPressedEx: IVR key information (e.g. [{"key":"1","label":"very satisfied"}]).
        :type IVRKeyPressedEx: list of IVRKeyPressedElement
        :param _AsrUrl: Access to the asr text information address of the recording.
        :type AsrUrl: str
        :param _AsrStatus: ASRUrl status: complete.
Completed;.
Processing.
Generating.
NotExists.
No record (offline asr generation is not enabled or no package is available).
        :type AsrStatus: str
        :param _CustomRecordURL: Address of the third-party cos for transferring recording.
        :type CustomRecordURL: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _QueuedSkillGroupName: Queue skill group name.
        :type QueuedSkillGroupName: str
        :param _VoicemailRecordURL: Audio message recording url during call.
        :type VoicemailRecordURL: list of str
        :param _VoicemailAsrURL: Text information address of asr audio message during a call.
        :type VoicemailAsrURL: list of str
        """
        self._Caller = None
        self._Callee = None
        self._Time = None
        self._Direction = None
        self._Duration = None
        self._RecordURL = None
        self._RecordId = None
        self._SeatUser = None
        self._EndStatus = None
        self._SkillGroup = None
        self._CallerLocation = None
        self._IVRDuration = None
        self._RingTimestamp = None
        self._AcceptTimestamp = None
        self._EndedTimestamp = None
        self._IVRKeyPressed = None
        self._HungUpSide = None
        self._ServeParticipants = None
        self._SkillGroupId = None
        self._EndStatusString = None
        self._StartTimestamp = None
        self._QueuedTimestamp = None
        self._PostIVRKeyPressed = None
        self._QueuedSkillGroupId = None
        self._SessionId = None
        self._ProtectedCaller = None
        self._ProtectedCallee = None
        self._Uui = None
        self._UUI = None
        self._IVRKeyPressedEx = None
        self._AsrUrl = None
        self._AsrStatus = None
        self._CustomRecordURL = None
        self._Remark = None
        self._QueuedSkillGroupName = None
        self._VoicemailRecordURL = None
        self._VoicemailAsrURL = None

    @property
    def Caller(self):
        """Caller number.
        :rtype: str
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Callee(self):
        """Called number.
        :rtype: str
        """
        return self._Callee

    @Callee.setter
    def Callee(self, Callee):
        self._Callee = Callee

    @property
    def Time(self):
        """Call initiation timestamp, unix timestamp.
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Direction(self):
        """Call direction: 0 - inbound, 1 - outbound.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Duration(self):
        """Call duration.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordURL(self):
        """Recording information.
        :rtype: str
        """
        return self._RecordURL

    @RecordURL.setter
    def RecordURL(self, RecordURL):
        self._RecordURL = RecordURL

    @property
    def RecordId(self):
        """Recording id.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def SeatUser(self):
        """Agent information.
        :rtype: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        """
        return self._SeatUser

    @SeatUser.setter
    def SeatUser(self, SeatUser):
        self._SeatUser = SeatUser

    @property
    def EndStatus(self):
        """EndStatus corresponds one-to-one with endstatusstring, with specific enumerations as follows:.

**Scenario	EndStatus	EndStatusString	Status description**.

Inbound call & call	1	ok	end properly.

Inbound call & call | 0 | error | system error.

Inbound call | 102 | ivrgiveup | user gives up during ivr.

Inbound call | 103 | waitinggiveup | user gives up during session queue.

Inbound call | 104 | ringinggiveup | user gives up during session ringing.

Inbound call | 105 | noseatonline | no agent online.

Inbound call              106	       non - working hour      non - working hour.   

Inbound call              107	       ivrend                   end directly after ivr.

Inbound call              100	       blocklist call - in      call - in blocklist. 

Outgoing call            2                 unconnected            unconnected.

Outgoing call            108           restricted callee      callee restricted due to high - risk.

Outgoing call         109        toomanyrequest        overfrequency.

Outgoing call         110        restrictedarea        outbound blind area.

Outgoing call         111        restrictedtime        outbound time restriction.
                         
Outgoing call         201        unknown               unknown status.

Outgoing call         202        notanswer             unanswered.

Outgoing call - 203 - userreject: reject call.

Outgoing call - 204 - poweroff: power off.

Outgoing call - 205 - numbernotexist: nonexistent number.

Outgoing call - 206 - busy: call in progress.

Outgoing call - 207 - outofcredit: arrears.

Outgoing call - 208 - operatorerror - ISP line exception.

Outgoing call - 209 - callercancel - caller cancellation.

Outgoing call - 210 - notinservice - not in service area.

Inbound and outgoing call - 211 - clienterror - client error.
Outgoing call - 212 - carrierblocked - ISP blocking.
        :rtype: int
        """
        return self._EndStatus

    @EndStatus.setter
    def EndStatus(self, EndStatus):
        self._EndStatus = EndStatus

    @property
    def SkillGroup(self):
        """Skill group name.
        :rtype: str
        """
        return self._SkillGroup

    @SkillGroup.setter
    def SkillGroup(self, SkillGroup):
        self._SkillGroup = SkillGroup

    @property
    def CallerLocation(self):
        """Caller'S location.
        :rtype: str
        """
        return self._CallerLocation

    @CallerLocation.setter
    def CallerLocation(self, CallerLocation):
        self._CallerLocation = CallerLocation

    @property
    def IVRDuration(self):
        """Time spent in ivr stage.
        :rtype: int
        """
        return self._IVRDuration

    @IVRDuration.setter
    def IVRDuration(self, IVRDuration):
        self._IVRDuration = IVRDuration

    @property
    def RingTimestamp(self):
        """Ring timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._RingTimestamp

    @RingTimestamp.setter
    def RingTimestamp(self, RingTimestamp):
        self._RingTimestamp = RingTimestamp

    @property
    def AcceptTimestamp(self):
        """Answer timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._AcceptTimestamp

    @AcceptTimestamp.setter
    def AcceptTimestamp(self, AcceptTimestamp):
        self._AcceptTimestamp = AcceptTimestamp

    @property
    def EndedTimestamp(self):
        """End timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._EndedTimestamp

    @EndedTimestamp.setter
    def EndedTimestamp(self, EndedTimestamp):
        self._EndedTimestamp = EndedTimestamp

    @property
    def IVRKeyPressed(self):
        """IVR key information, e.g. ["1","2","3"].
        :rtype: list of str
        """
        return self._IVRKeyPressed

    @IVRKeyPressed.setter
    def IVRKeyPressed(self, IVRKeyPressed):
        self._IVRKeyPressed = IVRKeyPressed

    @property
    def HungUpSide(self):
        """Hang-Up side, seat, user, system.
        :rtype: str
        """
        return self._HungUpSide

    @HungUpSide.setter
    def HungUpSide(self, HungUpSide):
        self._HungUpSide = HungUpSide

    @property
    def ServeParticipants(self):
        """Service participant list.
        :rtype: list of ServeParticipant
        """
        return self._ServeParticipants

    @ServeParticipants.setter
    def ServeParticipants(self, ServeParticipants):
        self._ServeParticipants = ServeParticipants

    @property
    def SkillGroupId(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def EndStatusString(self):
        """EndStatus corresponds one-to-one with endstatusstring, with specific enumerations as follows:.

**Scenario	EndStatus	EndStatusString	Status description**.

Inbound call & call	1	ok	end properly.

Inbound call & call | 0 | error | system error.

Inbound call | 102 | ivrgiveup | user gives up during ivr.

Inbound call | 103 | waitinggiveup | user gives up during session queue.

Inbound call | 104 | ringinggiveup | user gives up during session ringing.

Inbound call | 105 | noseatonline | no agent online.

Inbound call              106	       non - working hour      non - working hour.   

Inbound call              107	       ivrend                   end directly after ivr.

Inbound call              100	       blocklist call - in      call - in blocklist. 

Outgoing call            2                 unconnected            unconnected.

Outgoing call            108           restricted callee      callee restricted due to high - risk.

Outgoing call         109        toomanyrequest        overfrequency.

Outgoing call         110        restrictedarea        outbound blind area.

Outgoing call         111        restrictedtime        outbound time restriction.
                         
Outgoing call         201        unknown               unknown status.

Outgoing call         202        notanswer             unanswered.

Outgoing call - 203 - userreject: reject call.

Outgoing call - 204 - poweroff: power off.

Outgoing call - 205 - numbernotexist: nonexistent number.

Outgoing call - 206 - busy: call in progress.

Outgoing call - 207 - outofcredit: arrears.

Outgoing call - 208 - operatorerror - ISP line exception.

Outgoing call - 209 - callercancel - caller cancellation.

Outgoing call - 210 - notinservice - not in service area.

Inbound and outgoing call - 211 - clienterror - client error.
Outgoing call - 212 - carrierblocked - ISP blocking.
        :rtype: str
        """
        return self._EndStatusString

    @EndStatusString.setter
    def EndStatusString(self, EndStatusString):
        self._EndStatusString = EndStatusString

    @property
    def StartTimestamp(self):
        """Session start timestamp. unix second-level timestamp.
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def QueuedTimestamp(self):
        """Queue entry time. unix second-level timestamp.
        :rtype: int
        """
        return self._QueuedTimestamp

    @QueuedTimestamp.setter
    def QueuedTimestamp(self, QueuedTimestamp):
        self._QueuedTimestamp = QueuedTimestamp

    @property
    def PostIVRKeyPressed(self):
        """Post-IVR key information (e.g. [{"key":"1","label":"very satisfied"}]).
        :rtype: list of IVRKeyPressedElement
        """
        return self._PostIVRKeyPressed

    @PostIVRKeyPressed.setter
    def PostIVRKeyPressed(self, PostIVRKeyPressed):
        self._PostIVRKeyPressed = PostIVRKeyPressed

    @property
    def QueuedSkillGroupId(self):
        """Queue skill group id.
        :rtype: int
        """
        return self._QueuedSkillGroupId

    @QueuedSkillGroupId.setter
    def QueuedSkillGroupId(self, QueuedSkillGroupId):
        self._QueuedSkillGroupId = QueuedSkillGroupId

    @property
    def SessionId(self):
        """Session id.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ProtectedCaller(self):
        """Caller number protection id. effective when the number protection map feature is activated, and the caller field is empty.
        :rtype: str
        """
        return self._ProtectedCaller

    @ProtectedCaller.setter
    def ProtectedCaller(self, ProtectedCaller):
        self._ProtectedCaller = ProtectedCaller

    @property
    def ProtectedCallee(self):
        """Called number protection id. effective when the number protection map feature is activated, and the callee field is empty.
        :rtype: str
        """
        return self._ProtectedCallee

    @ProtectedCallee.setter
    def ProtectedCallee(self, ProtectedCallee):
        self._ProtectedCallee = ProtectedCallee

    @property
    def Uui(self):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        """Customer custom data. (user - to - user interface).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uui

    @Uui.setter
    def Uui(self, Uui):
        warnings.warn("parameter `Uui` is deprecated", DeprecationWarning) 

        self._Uui = Uui

    @property
    def UUI(self):
        """Customer custom data. (user - to - user interface).
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def IVRKeyPressedEx(self):
        """IVR key information (e.g. [{"key":"1","label":"very satisfied"}]).
        :rtype: list of IVRKeyPressedElement
        """
        return self._IVRKeyPressedEx

    @IVRKeyPressedEx.setter
    def IVRKeyPressedEx(self, IVRKeyPressedEx):
        self._IVRKeyPressedEx = IVRKeyPressedEx

    @property
    def AsrUrl(self):
        """Access to the asr text information address of the recording.
        :rtype: str
        """
        return self._AsrUrl

    @AsrUrl.setter
    def AsrUrl(self, AsrUrl):
        self._AsrUrl = AsrUrl

    @property
    def AsrStatus(self):
        """ASRUrl status: complete.
Completed;.
Processing.
Generating.
NotExists.
No record (offline asr generation is not enabled or no package is available).
        :rtype: str
        """
        return self._AsrStatus

    @AsrStatus.setter
    def AsrStatus(self, AsrStatus):
        self._AsrStatus = AsrStatus

    @property
    def CustomRecordURL(self):
        """Address of the third-party cos for transferring recording.
        :rtype: str
        """
        return self._CustomRecordURL

    @CustomRecordURL.setter
    def CustomRecordURL(self, CustomRecordURL):
        self._CustomRecordURL = CustomRecordURL

    @property
    def Remark(self):
        """Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def QueuedSkillGroupName(self):
        """Queue skill group name.
        :rtype: str
        """
        return self._QueuedSkillGroupName

    @QueuedSkillGroupName.setter
    def QueuedSkillGroupName(self, QueuedSkillGroupName):
        self._QueuedSkillGroupName = QueuedSkillGroupName

    @property
    def VoicemailRecordURL(self):
        """Audio message recording url during call.
        :rtype: list of str
        """
        return self._VoicemailRecordURL

    @VoicemailRecordURL.setter
    def VoicemailRecordURL(self, VoicemailRecordURL):
        self._VoicemailRecordURL = VoicemailRecordURL

    @property
    def VoicemailAsrURL(self):
        """Text information address of asr audio message during a call.
        :rtype: list of str
        """
        return self._VoicemailAsrURL

    @VoicemailAsrURL.setter
    def VoicemailAsrURL(self, VoicemailAsrURL):
        self._VoicemailAsrURL = VoicemailAsrURL


    def _deserialize(self, params):
        self._Caller = params.get("Caller")
        self._Callee = params.get("Callee")
        self._Time = params.get("Time")
        self._Direction = params.get("Direction")
        self._Duration = params.get("Duration")
        self._RecordURL = params.get("RecordURL")
        self._RecordId = params.get("RecordId")
        if params.get("SeatUser") is not None:
            self._SeatUser = SeatUserInfo()
            self._SeatUser._deserialize(params.get("SeatUser"))
        self._EndStatus = params.get("EndStatus")
        self._SkillGroup = params.get("SkillGroup")
        self._CallerLocation = params.get("CallerLocation")
        self._IVRDuration = params.get("IVRDuration")
        self._RingTimestamp = params.get("RingTimestamp")
        self._AcceptTimestamp = params.get("AcceptTimestamp")
        self._EndedTimestamp = params.get("EndedTimestamp")
        self._IVRKeyPressed = params.get("IVRKeyPressed")
        self._HungUpSide = params.get("HungUpSide")
        if params.get("ServeParticipants") is not None:
            self._ServeParticipants = []
            for item in params.get("ServeParticipants"):
                obj = ServeParticipant()
                obj._deserialize(item)
                self._ServeParticipants.append(obj)
        self._SkillGroupId = params.get("SkillGroupId")
        self._EndStatusString = params.get("EndStatusString")
        self._StartTimestamp = params.get("StartTimestamp")
        self._QueuedTimestamp = params.get("QueuedTimestamp")
        if params.get("PostIVRKeyPressed") is not None:
            self._PostIVRKeyPressed = []
            for item in params.get("PostIVRKeyPressed"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._PostIVRKeyPressed.append(obj)
        self._QueuedSkillGroupId = params.get("QueuedSkillGroupId")
        self._SessionId = params.get("SessionId")
        self._ProtectedCaller = params.get("ProtectedCaller")
        self._ProtectedCallee = params.get("ProtectedCallee")
        self._Uui = params.get("Uui")
        self._UUI = params.get("UUI")
        if params.get("IVRKeyPressedEx") is not None:
            self._IVRKeyPressedEx = []
            for item in params.get("IVRKeyPressedEx"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self._IVRKeyPressedEx.append(obj)
        self._AsrUrl = params.get("AsrUrl")
        self._AsrStatus = params.get("AsrStatus")
        self._CustomRecordURL = params.get("CustomRecordURL")
        self._Remark = params.get("Remark")
        self._QueuedSkillGroupName = params.get("QueuedSkillGroupName")
        self._VoicemailRecordURL = params.get("VoicemailRecordURL")
        self._VoicemailAsrURL = params.get("VoicemailAsrURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindNumberCallOutSkillGroupRequest(AbstractModel):
    """UnbindNumberCallOutSkillGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _Number: Number to be unbound.
        :type Number: str
        :param _SkillGroupIds: List of skill group ids to be unbound.
        :type SkillGroupIds: list of int non-negative
        """
        self._SdkAppId = None
        self._Number = None
        self._SkillGroupIds = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Number(self):
        """Number to be unbound.
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def SkillGroupIds(self):
        """List of skill group ids to be unbound.
        :rtype: list of int non-negative
        """
        return self._SkillGroupIds

    @SkillGroupIds.setter
    def SkillGroupIds(self, SkillGroupIds):
        self._SkillGroupIds = SkillGroupIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Number = params.get("Number")
        self._SkillGroupIds = params.get("SkillGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindNumberCallOutSkillGroupResponse(AbstractModel):
    """UnbindNumberCallOutSkillGroup response structure.

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


class UnbindStaffSkillGroupListRequest(AbstractModel):
    """UnbindStaffSkillGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _StaffEmail: Customer service email.
        :type StaffEmail: str
        :param _SkillGroupList: Unbound skill group list.
        :type SkillGroupList: list of int
        """
        self._SdkAppId = None
        self._StaffEmail = None
        self._SkillGroupList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StaffEmail(self):
        """Customer service email.
        :rtype: str
        """
        return self._StaffEmail

    @StaffEmail.setter
    def StaffEmail(self, StaffEmail):
        self._StaffEmail = StaffEmail

    @property
    def SkillGroupList(self):
        """Unbound skill group list.
        :rtype: list of int
        """
        return self._SkillGroupList

    @SkillGroupList.setter
    def SkillGroupList(self, SkillGroupList):
        self._SkillGroupList = SkillGroupList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StaffEmail = params.get("StaffEmail")
        self._SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindStaffSkillGroupListResponse(AbstractModel):
    """UnbindStaffSkillGroupList response structure.

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


class UpdateCCCSkillGroupRequest(AbstractModel):
    """UpdateCCCSkillGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _SkillGroupID: Skill group id.
        :type SkillGroupID: int
        :param _SkillGroupName: Modified skill group name.
        :type SkillGroupName: str
        :param _MaxConcurrency: Modified maximum concurrency, with the maximum synchronization being 2.
        :type MaxConcurrency: int
        :param _RingAll: True for simultaneous ringing, false for sequential ringing.
        :type RingAll: bool
        """
        self._SdkAppId = None
        self._SkillGroupID = None
        self._SkillGroupName = None
        self._MaxConcurrency = None
        self._RingAll = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SkillGroupID(self):
        """Skill group id.
        :rtype: int
        """
        return self._SkillGroupID

    @SkillGroupID.setter
    def SkillGroupID(self, SkillGroupID):
        self._SkillGroupID = SkillGroupID

    @property
    def SkillGroupName(self):
        """Modified skill group name.
        :rtype: str
        """
        return self._SkillGroupName

    @SkillGroupName.setter
    def SkillGroupName(self, SkillGroupName):
        self._SkillGroupName = SkillGroupName

    @property
    def MaxConcurrency(self):
        """Modified maximum concurrency, with the maximum synchronization being 2.
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def RingAll(self):
        """True for simultaneous ringing, false for sequential ringing.
        :rtype: bool
        """
        return self._RingAll

    @RingAll.setter
    def RingAll(self, RingAll):
        self._RingAll = RingAll


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SkillGroupID = params.get("SkillGroupID")
        self._SkillGroupName = params.get("SkillGroupName")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._RingAll = params.get("RingAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCCCSkillGroupResponse(AbstractModel):
    """UpdateCCCSkillGroup response structure.

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


class UpdatePredictiveDialingCampaignRequest(AbstractModel):
    """UpdatePredictiveDialingCampaign request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _CampaignId: Generated task id.
        :type CampaignId: int
        :param _Name: Task name.
        :type Name: str
        :param _Callees: Called list supporting e.164 or number formats without country code.
        :type Callees: list of str
        :param _Callers: Calling list using the number formats displayed on the management side.
        :type Callers: list of str
        :param _CallOrder: Being called sequence: 0 for random 1 for in order.
        :type CallOrder: int
        :param _SkillGroupId: ID of the used skill group of agents.
        :type SkillGroupId: int
        :param _Priority: Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :type Priority: int
        :param _ExpectedAbandonRate: Expected call drop rate, percentage, 5 - 50.	.	
        :type ExpectedAbandonRate: int
        :param _RetryInterval: Call retry interval, in seconds, [60 - 86,400].
        :type RetryInterval: int
        :param _StartTime: Task start time. unix timestamp. the task will automatically start after this time.
        :type StartTime: int
        :param _EndTime: Task termination time. unix timestamp. the task will automatically terminate after this time.
        :type EndTime: int
        :param _IVRId: Specified ivr id.
        :type IVRId: int
        :param _RetryTimes: Number of call retries, 0 - 2.
        :type RetryTimes: int
        :param _Variables: Custom variable.
        :type Variables: list of Variable
        :param _UUI: 	UUI
        :type UUI: str
        :param _CalleeAttributes: Property of the called.
        :type CalleeAttributes: list of CalleeAttribute
        """
        self._SdkAppId = None
        self._CampaignId = None
        self._Name = None
        self._Callees = None
        self._Callers = None
        self._CallOrder = None
        self._SkillGroupId = None
        self._Priority = None
        self._ExpectedAbandonRate = None
        self._RetryInterval = None
        self._StartTime = None
        self._EndTime = None
        self._IVRId = None
        self._RetryTimes = None
        self._Variables = None
        self._UUI = None
        self._CalleeAttributes = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CampaignId(self):
        """Generated task id.
        :rtype: int
        """
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Name(self):
        """Task name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Callees(self):
        """Called list supporting e.164 or number formats without country code.
        :rtype: list of str
        """
        return self._Callees

    @Callees.setter
    def Callees(self, Callees):
        self._Callees = Callees

    @property
    def Callers(self):
        """Calling list using the number formats displayed on the management side.
        :rtype: list of str
        """
        return self._Callers

    @Callers.setter
    def Callers(self, Callers):
        self._Callers = Callers

    @property
    def CallOrder(self):
        """Being called sequence: 0 for random 1 for in order.
        :rtype: int
        """
        return self._CallOrder

    @CallOrder.setter
    def CallOrder(self, CallOrder):
        self._CallOrder = CallOrder

    @property
    def SkillGroupId(self):
        """ID of the used skill group of agents.
        :rtype: int
        """
        return self._SkillGroupId

    @SkillGroupId.setter
    def SkillGroupId(self, SkillGroupId):
        self._SkillGroupId = SkillGroupId

    @property
    def Priority(self):
        """Running priority of multiple tasks in the same application, from high to low 1 - 5.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ExpectedAbandonRate(self):
        """Expected call drop rate, percentage, 5 - 50.	.	
        :rtype: int
        """
        return self._ExpectedAbandonRate

    @ExpectedAbandonRate.setter
    def ExpectedAbandonRate(self, ExpectedAbandonRate):
        self._ExpectedAbandonRate = ExpectedAbandonRate

    @property
    def RetryInterval(self):
        """Call retry interval, in seconds, [60 - 86,400].
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def StartTime(self):
        """Task start time. unix timestamp. the task will automatically start after this time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task termination time. unix timestamp. the task will automatically terminate after this time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IVRId(self):
        """Specified ivr id.
        :rtype: int
        """
        return self._IVRId

    @IVRId.setter
    def IVRId(self, IVRId):
        self._IVRId = IVRId

    @property
    def RetryTimes(self):
        """Number of call retries, 0 - 2.
        :rtype: int
        """
        return self._RetryTimes

    @RetryTimes.setter
    def RetryTimes(self, RetryTimes):
        self._RetryTimes = RetryTimes

    @property
    def Variables(self):
        """Custom variable.
        :rtype: list of Variable
        """
        return self._Variables

    @Variables.setter
    def Variables(self, Variables):
        self._Variables = Variables

    @property
    def UUI(self):
        """	UUI
        :rtype: str
        """
        return self._UUI

    @UUI.setter
    def UUI(self, UUI):
        self._UUI = UUI

    @property
    def CalleeAttributes(self):
        """Property of the called.
        :rtype: list of CalleeAttribute
        """
        return self._CalleeAttributes

    @CalleeAttributes.setter
    def CalleeAttributes(self, CalleeAttributes):
        self._CalleeAttributes = CalleeAttributes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CampaignId = params.get("CampaignId")
        self._Name = params.get("Name")
        self._Callees = params.get("Callees")
        self._Callers = params.get("Callers")
        self._CallOrder = params.get("CallOrder")
        self._SkillGroupId = params.get("SkillGroupId")
        self._Priority = params.get("Priority")
        self._ExpectedAbandonRate = params.get("ExpectedAbandonRate")
        self._RetryInterval = params.get("RetryInterval")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IVRId = params.get("IVRId")
        self._RetryTimes = params.get("RetryTimes")
        if params.get("Variables") is not None:
            self._Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self._Variables.append(obj)
        self._UUI = params.get("UUI")
        if params.get("CalleeAttributes") is not None:
            self._CalleeAttributes = []
            for item in params.get("CalleeAttributes"):
                obj = CalleeAttribute()
                obj._deserialize(item)
                self._CalleeAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePredictiveDialingCampaignResponse(AbstractModel):
    """UpdatePredictiveDialingCampaign response structure.

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


class UploadAudioInfo(AbstractModel):
    """Upload Audio File Information

    """

    def __init__(self):
        r"""
        :param _CustomFileName: File alias (can be duplicated).
        :type CustomFileName: str
        :param _AudioUrl: Audio file link (supports mp3 and wav formats, file size not exceeding 5mb).
        :type AudioUrl: str
        """
        self._CustomFileName = None
        self._AudioUrl = None

    @property
    def CustomFileName(self):
        """File alias (can be duplicated).
        :rtype: str
        """
        return self._CustomFileName

    @CustomFileName.setter
    def CustomFileName(self, CustomFileName):
        self._CustomFileName = CustomFileName

    @property
    def AudioUrl(self):
        """Audio file link (supports mp3 and wav formats, file size not exceeding 5mb).
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl


    def _deserialize(self, params):
        self._CustomFileName = params.get("CustomFileName")
        self._AudioUrl = params.get("AudioUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioFailedInfo(AbstractModel):
    """Failed to upload audio file information

    """

    def __init__(self):
        r"""
        :param _FileName: Filename.
        :type FileName: str
        :param _FailedMsg: Reason for failure.
        :type FailedMsg: str
        """
        self._FileName = None
        self._FailedMsg = None

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
    def FailedMsg(self):
        """Reason for failure.
        :rtype: str
        """
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioRequest(AbstractModel):
    """UploadIvrAudio request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :type SdkAppId: int
        :param _AudioList: Audio file list.
        :type AudioList: list of UploadAudioInfo
        """
        self._SdkAppId = None
        self._AudioList = None

    @property
    def SdkAppId(self):
        """Application id (required) can be found at https://console.cloud.tencent.com/ccc.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioList(self):
        """Audio file list.
        :rtype: list of UploadAudioInfo
        """
        return self._AudioList

    @AudioList.setter
    def AudioList(self, AudioList):
        self._AudioList = AudioList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioList") is not None:
            self._AudioList = []
            for item in params.get("AudioList"):
                obj = UploadAudioInfo()
                obj._deserialize(item)
                self._AudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIvrAudioResponse(AbstractModel):
    """UploadIvrAudio response structure.

    """

    def __init__(self):
        r"""
        :param _FailedFileList: List of files that failed to be uploaded.
        :type FailedFileList: list of UploadIvrAudioFailedInfo
        :param _SuccessFileList: List of successfully uploaded files.
        :type SuccessFileList: list of AudioFileInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedFileList = None
        self._SuccessFileList = None
        self._RequestId = None

    @property
    def FailedFileList(self):
        """List of files that failed to be uploaded.
        :rtype: list of UploadIvrAudioFailedInfo
        """
        return self._FailedFileList

    @FailedFileList.setter
    def FailedFileList(self, FailedFileList):
        self._FailedFileList = FailedFileList

    @property
    def SuccessFileList(self):
        """List of successfully uploaded files.
        :rtype: list of AudioFileInfo
        """
        return self._SuccessFileList

    @SuccessFileList.setter
    def SuccessFileList(self, SuccessFileList):
        self._SuccessFileList = SuccessFileList

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
        if params.get("FailedFileList") is not None:
            self._FailedFileList = []
            for item in params.get("FailedFileList"):
                obj = UploadIvrAudioFailedInfo()
                obj._deserialize(item)
                self._FailedFileList.append(obj)
        if params.get("SuccessFileList") is not None:
            self._SuccessFileList = []
            for item in params.get("SuccessFileList"):
                obj = AudioFileInfo()
                obj._deserialize(item)
                self._SuccessFileList.append(obj)
        self._RequestId = params.get("RequestId")


class Variable(AbstractModel):
    """Variable.

    """

    def __init__(self):
        r"""
        :param _Key: Variable name.
        :type Key: str
        :param _Value: Variable value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Variable name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Variable value.
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
        