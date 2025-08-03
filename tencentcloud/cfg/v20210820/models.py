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


class ActionFieldConfigDetail(AbstractModel):
    """Response format of dynamic action parameters

    """

    def __init__(self):
        r"""
        :param _Type: Component type
The options are as follows:
input: text box
textarea: multi-line text box
number: number input box
select: selector
cascader: cascade selector
radio: single choice
time: time selection
        :type Type: str
        :param _Lable: Component label
        :type Lable: str
        :param _Field: Unique identifier of the component, key when it is sent back to the backend
        :type Field: str
        :param _DefaultValue: Default value
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param _Config: The supported configuration items are as follows. You can select the configuration items as needed. If no configuration is required, set the value to {}.

{  placeholder: string (placeholder)

  tooltip: string (prompt message)

  reg: RegExp (regular expression for the input content format)

  max: number (maximum number of input characters for text boxes and upper limit of the input number for number input boxes)

  min: number (lower limit of the input number for number input boxes)

  step: number (step size for number input boxes; default value: 1)

  format: string (format for time selection, for example YYYY-MM-DD and YYYY-MM-DD HH:mm:ss)

  separator: string[] (separator for multi-line input boxes. If it is left blank, no separator is used, and the text string entered by the user is returned directly.)

  multiple: boolean (multiple-choice or not, valid for selectors and cascade selectors)

  options: selector options (support the following two forms)

Directly provide the option array: { value: string; label: string }[]
Obtain options by calling the API: { api: string (API URL), params: string[] (interface parameters, corresponding to field of the parameter configuration. The frontend uses the input values of all components corresponding to field as parameters to query data. If no value is input, the frontend directly requests data when components are loaded.) 
}
}
        :type Config: str
        :param _Required: Whether it is required (0: no; 1: yes)
        :type Required: int
        :param _Validate: The compute configuration passes the verification when other fields that it depends on meet the conditions. (For example, at least one of the three form items must be filled in.)

[fieldName,

{ config: This item is retained and will be refined based on subsequent scenes. }

]
        :type Validate: str
        :param _Visible: Whether it is visible
        :type Visible: str
        """
        self._Type = None
        self._Lable = None
        self._Field = None
        self._DefaultValue = None
        self._Config = None
        self._Required = None
        self._Validate = None
        self._Visible = None

    @property
    def Type(self):
        """Component type
The options are as follows:
input: text box
textarea: multi-line text box
number: number input box
select: selector
cascader: cascade selector
radio: single choice
time: time selection
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Lable(self):
        """Component label
        :rtype: str
        """
        return self._Lable

    @Lable.setter
    def Lable(self, Lable):
        self._Lable = Lable

    @property
    def Field(self):
        """Unique identifier of the component, key when it is sent back to the backend
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def DefaultValue(self):
        """Default value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Config(self):
        """The supported configuration items are as follows. You can select the configuration items as needed. If no configuration is required, set the value to {}.

{  placeholder: string (placeholder)

  tooltip: string (prompt message)

  reg: RegExp (regular expression for the input content format)

  max: number (maximum number of input characters for text boxes and upper limit of the input number for number input boxes)

  min: number (lower limit of the input number for number input boxes)

  step: number (step size for number input boxes; default value: 1)

  format: string (format for time selection, for example YYYY-MM-DD and YYYY-MM-DD HH:mm:ss)

  separator: string[] (separator for multi-line input boxes. If it is left blank, no separator is used, and the text string entered by the user is returned directly.)

  multiple: boolean (multiple-choice or not, valid for selectors and cascade selectors)

  options: selector options (support the following two forms)

Directly provide the option array: { value: string; label: string }[]
Obtain options by calling the API: { api: string (API URL), params: string[] (interface parameters, corresponding to field of the parameter configuration. The frontend uses the input values of all components corresponding to field as parameters to query data. If no value is input, the frontend directly requests data when components are loaded.) 
}
}
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Required(self):
        """Whether it is required (0: no; 1: yes)
        :rtype: int
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Validate(self):
        """The compute configuration passes the verification when other fields that it depends on meet the conditions. (For example, at least one of the three form items must be filled in.)

[fieldName,

{ config: This item is retained and will be refined based on subsequent scenes. }

]
        :rtype: str
        """
        return self._Validate

    @Validate.setter
    def Validate(self, Validate):
        self._Validate = Validate

    @property
    def Visible(self):
        """Whether it is visible
        :rtype: str
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Lable = params.get("Lable")
        self._Field = params.get("Field")
        self._DefaultValue = params.get("DefaultValue")
        self._Config = params.get("Config")
        self._Required = params.get("Required")
        self._Validate = params.get("Validate")
        self._Visible = params.get("Visible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionFieldConfigResult(AbstractModel):
    """Action field configuration result

    """

    def __init__(self):
        r"""
        :param _ActionId: Action ID
        :type ActionId: int
        :param _ActionName: Action name
        :type ActionName: str
        :param _ConfigDetail: Filed configuration details corresponding to the action
        :type ConfigDetail: list of ActionFieldConfigDetail
        """
        self._ActionId = None
        self._ActionName = None
        self._ConfigDetail = None

    @property
    def ActionId(self):
        """Action ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def ActionName(self):
        """Action name
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def ConfigDetail(self):
        """Filed configuration details corresponding to the action
        :rtype: list of ActionFieldConfigDetail
        """
        return self._ConfigDetail

    @ConfigDetail.setter
    def ConfigDetail(self, ConfigDetail):
        self._ConfigDetail = ConfigDetail


    def _deserialize(self, params):
        self._ActionId = params.get("ActionId")
        self._ActionName = params.get("ActionName")
        if params.get("ConfigDetail") is not None:
            self._ConfigDetail = []
            for item in params.get("ConfigDetail"):
                obj = ActionFieldConfigDetail()
                obj._deserialize(item)
                self._ConfigDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionFilter(AbstractModel):
    """Action library filtering field

    """

    def __init__(self):
        r"""
        :param _Keyword: Keyword
        :type Keyword: str
        :param _Values: Content for search
        :type Values: list of str
        """
        self._Keyword = None
        self._Values = None

    @property
    def Keyword(self):
        """Keyword
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Values(self):
        """Content for search
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionLibraryListResult(AbstractModel):
    """Action library data list

    """

    def __init__(self):
        r"""
        :param _ActionName: Action name
        :type ActionName: str
        :param _Desc: Action description
        :type Desc: str
        :param _ActionType: Action type: ["platform" and "custom"]
        :type ActionType: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Creator: Creator
        :type Creator: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _RiskDesc: Action risk description
        :type RiskDesc: str
        :param _ActionId: Action ID
        :type ActionId: int
        :param _AttributeId: Action attribute (1: fault; 2: recovery)
        :type AttributeId: int
        :param _RelationActionId: ID of the associated action
        :type RelationActionId: int
        :param _ActionCommand: Operation command
        :type ActionCommand: str
        :param _ActionCommandType: Action type (0: tat; 1: cloud API)
        :type ActionCommandType: int
        :param _ActionContent: Parameters of the custom action, in JSON string format
        :type ActionContent: str
        :param _ResourceType: Level-2 type
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _ActionDetail: Action description
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionDetail: str
        :param _IsAllowed: Whether to allow usage by the current account
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAllowed: bool
        :param _ActionBestCase: Link to best practices
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionBestCase: str
        :param _ObjectType: Object type
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectType: str
        :param _MetricIdList: Monitoring metric ID list
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricIdList: list of int non-negative
        :param _IsNewAction: Whether the action is new
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsNewAction: bool
        """
        self._ActionName = None
        self._Desc = None
        self._ActionType = None
        self._CreateTime = None
        self._Creator = None
        self._UpdateTime = None
        self._RiskDesc = None
        self._ActionId = None
        self._AttributeId = None
        self._RelationActionId = None
        self._ActionCommand = None
        self._ActionCommandType = None
        self._ActionContent = None
        self._ResourceType = None
        self._ActionDetail = None
        self._IsAllowed = None
        self._ActionBestCase = None
        self._ObjectType = None
        self._MetricIdList = None
        self._IsNewAction = None

    @property
    def ActionName(self):
        """Action name
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Desc(self):
        """Action description
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ActionType(self):
        """Action type: ["platform" and "custom"]
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        """Creator
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RiskDesc(self):
        """Action risk description
        :rtype: str
        """
        return self._RiskDesc

    @RiskDesc.setter
    def RiskDesc(self, RiskDesc):
        self._RiskDesc = RiskDesc

    @property
    def ActionId(self):
        """Action ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def AttributeId(self):
        """Action attribute (1: fault; 2: recovery)
        :rtype: int
        """
        return self._AttributeId

    @AttributeId.setter
    def AttributeId(self, AttributeId):
        self._AttributeId = AttributeId

    @property
    def RelationActionId(self):
        """ID of the associated action
        :rtype: int
        """
        return self._RelationActionId

    @RelationActionId.setter
    def RelationActionId(self, RelationActionId):
        self._RelationActionId = RelationActionId

    @property
    def ActionCommand(self):
        """Operation command
        :rtype: str
        """
        return self._ActionCommand

    @ActionCommand.setter
    def ActionCommand(self, ActionCommand):
        self._ActionCommand = ActionCommand

    @property
    def ActionCommandType(self):
        """Action type (0: tat; 1: cloud API)
        :rtype: int
        """
        return self._ActionCommandType

    @ActionCommandType.setter
    def ActionCommandType(self, ActionCommandType):
        self._ActionCommandType = ActionCommandType

    @property
    def ActionContent(self):
        """Parameters of the custom action, in JSON string format
        :rtype: str
        """
        return self._ActionContent

    @ActionContent.setter
    def ActionContent(self, ActionContent):
        self._ActionContent = ActionContent

    @property
    def ResourceType(self):
        """Level-2 type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ActionDetail(self):
        """Action description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionDetail

    @ActionDetail.setter
    def ActionDetail(self, ActionDetail):
        self._ActionDetail = ActionDetail

    @property
    def IsAllowed(self):
        """Whether to allow usage by the current account
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsAllowed

    @IsAllowed.setter
    def IsAllowed(self, IsAllowed):
        self._IsAllowed = IsAllowed

    @property
    def ActionBestCase(self):
        """Link to best practices
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionBestCase

    @ActionBestCase.setter
    def ActionBestCase(self, ActionBestCase):
        self._ActionBestCase = ActionBestCase

    @property
    def ObjectType(self):
        """Object type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def MetricIdList(self):
        """Monitoring metric ID list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int non-negative
        """
        return self._MetricIdList

    @MetricIdList.setter
    def MetricIdList(self, MetricIdList):
        self._MetricIdList = MetricIdList

    @property
    def IsNewAction(self):
        """Whether the action is new
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsNewAction

    @IsNewAction.setter
    def IsNewAction(self, IsNewAction):
        self._IsNewAction = IsNewAction


    def _deserialize(self, params):
        self._ActionName = params.get("ActionName")
        self._Desc = params.get("Desc")
        self._ActionType = params.get("ActionType")
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._UpdateTime = params.get("UpdateTime")
        self._RiskDesc = params.get("RiskDesc")
        self._ActionId = params.get("ActionId")
        self._AttributeId = params.get("AttributeId")
        self._RelationActionId = params.get("RelationActionId")
        self._ActionCommand = params.get("ActionCommand")
        self._ActionCommandType = params.get("ActionCommandType")
        self._ActionContent = params.get("ActionContent")
        self._ResourceType = params.get("ResourceType")
        self._ActionDetail = params.get("ActionDetail")
        self._IsAllowed = params.get("IsAllowed")
        self._ActionBestCase = params.get("ActionBestCase")
        self._ObjectType = params.get("ObjectType")
        self._MetricIdList = params.get("MetricIdList")
        self._IsNewAction = params.get("IsNewAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmServiceInfo(AbstractModel):
    """Application information on Application Performance Monitoring

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _ServiceNameList: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceNameList: list of str
        :param _RegionId: Region ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        """
        self._InstanceId = None
        self._ServiceNameList = None
        self._RegionId = None

    @property
    def InstanceId(self):
        """Business ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceNameList(self):
        """Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ServiceNameList

    @ServiceNameList.setter
    def ServiceNameList(self, ServiceNameList):
        self._ServiceNameList = ServiceNameList

    @property
    def RegionId(self):
        """Region ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceNameList = params.get("ServiceNameList")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromActionRequest(AbstractModel):
    """CreateTaskFromAction request structure.

    """

    def __init__(self):
        r"""
        :param _TaskActionId: Action ID, which can be obtained by using the action list API DescribeActionLibraryList.
        :type TaskActionId: int
        :param _TaskInstances: ID of the instance participating in the experiment.
        :type TaskInstances: list of str
        :param _TaskTitle: Experiment name. If this parameter is left blank, the action name is used by default.
        :type TaskTitle: str
        :param _TaskDescription: Experiment description. If this parameter is left blank, the action description is used by default.
        :type TaskDescription: str
        :param _TaskActionGeneralConfiguration: General action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the action details API DescribeActionFieldConfigList. If this field is left blank, the default action parameters are used by default.
        :type TaskActionGeneralConfiguration: str
        :param _TaskActionCustomConfiguration: Action custom parameters need to be passed in as json serialization. They can be obtained from the action details interface DescribeActionFieldConfigList. If not filled in, the default action parameters will be used. Note: Required parameters have no default values. Be sure to pass in valid values.
        :type TaskActionCustomConfiguration: str
        :param _TaskPauseDuration: Automatic experiment pause time, in minutes. If this parameter is left blank, the default value 60 is used.
        :type TaskPauseDuration: int
        """
        self._TaskActionId = None
        self._TaskInstances = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskActionGeneralConfiguration = None
        self._TaskActionCustomConfiguration = None
        self._TaskPauseDuration = None

    @property
    def TaskActionId(self):
        """Action ID, which can be obtained by using the action list API DescribeActionLibraryList.
        :rtype: int
        """
        return self._TaskActionId

    @TaskActionId.setter
    def TaskActionId(self, TaskActionId):
        self._TaskActionId = TaskActionId

    @property
    def TaskInstances(self):
        """ID of the instance participating in the experiment.
        :rtype: list of str
        """
        return self._TaskInstances

    @TaskInstances.setter
    def TaskInstances(self, TaskInstances):
        self._TaskInstances = TaskInstances

    @property
    def TaskTitle(self):
        """Experiment name. If this parameter is left blank, the action name is used by default.
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """Experiment description. If this parameter is left blank, the action description is used by default.
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskActionGeneralConfiguration(self):
        """General action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the action details API DescribeActionFieldConfigList. If this field is left blank, the default action parameters are used by default.
        :rtype: str
        """
        return self._TaskActionGeneralConfiguration

    @TaskActionGeneralConfiguration.setter
    def TaskActionGeneralConfiguration(self, TaskActionGeneralConfiguration):
        self._TaskActionGeneralConfiguration = TaskActionGeneralConfiguration

    @property
    def TaskActionCustomConfiguration(self):
        """Action custom parameters need to be passed in as json serialization. They can be obtained from the action details interface DescribeActionFieldConfigList. If not filled in, the default action parameters will be used. Note: Required parameters have no default values. Be sure to pass in valid values.
        :rtype: str
        """
        return self._TaskActionCustomConfiguration

    @TaskActionCustomConfiguration.setter
    def TaskActionCustomConfiguration(self, TaskActionCustomConfiguration):
        self._TaskActionCustomConfiguration = TaskActionCustomConfiguration

    @property
    def TaskPauseDuration(self):
        """Automatic experiment pause time, in minutes. If this parameter is left blank, the default value 60 is used.
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration


    def _deserialize(self, params):
        self._TaskActionId = params.get("TaskActionId")
        self._TaskInstances = params.get("TaskInstances")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskActionGeneralConfiguration = params.get("TaskActionGeneralConfiguration")
        self._TaskActionCustomConfiguration = params.get("TaskActionCustomConfiguration")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromActionResponse(AbstractModel):
    """CreateTaskFromAction response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the successfully created experiment
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """ID of the successfully created experiment
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


class CreateTaskFromTemplateRequest(AbstractModel):
    """CreateTaskFromTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID retrieved from the template library
        :type TemplateId: int
        :param _TaskConfig: Experiment configuration parameters
        :type TaskConfig: :class:`tencentcloud.cfg.v20210820.models.TaskConfig`
        """
        self._TemplateId = None
        self._TaskConfig = None

    @property
    def TemplateId(self):
        """Template ID retrieved from the template library
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TaskConfig(self):
        """Experiment configuration parameters
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TaskConfig`
        """
        return self._TaskConfig

    @TaskConfig.setter
    def TaskConfig(self, TaskConfig):
        self._TaskConfig = TaskConfig


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TaskConfig") is not None:
            self._TaskConfig = TaskConfig()
            self._TaskConfig._deserialize(params.get("TaskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromTemplateResponse(AbstractModel):
    """CreateTaskFromTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the successfully created experiment
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """ID of the successfully created experiment
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


class DeleteTaskRequest(AbstractModel):
    """DeleteTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Task ID
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
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask response structure.

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


class DescribeActionFieldConfigListRequest(AbstractModel):
    """DescribeActionFieldConfigList request structure.

    """

    def __init__(self):
        r"""
        :param _ActionIds: Action ID list
        :type ActionIds: list of int non-negative
        :param _ObjectTypeId: Object type ID
        :type ObjectTypeId: int
        """
        self._ActionIds = None
        self._ObjectTypeId = None

    @property
    def ActionIds(self):
        """Action ID list
        :rtype: list of int non-negative
        """
        return self._ActionIds

    @ActionIds.setter
    def ActionIds(self, ActionIds):
        self._ActionIds = ActionIds

    @property
    def ObjectTypeId(self):
        """Object type ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId


    def _deserialize(self, params):
        self._ActionIds = params.get("ActionIds")
        self._ObjectTypeId = params.get("ObjectTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionFieldConfigListResponse(AbstractModel):
    """DescribeActionFieldConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _Common: List of general filed configuration parameters
        :type Common: list of ActionFieldConfigResult
        :param _Results: List of action filed configuration parameters
        :type Results: list of ActionFieldConfigResult
        :param _ResourceOffline: Information on the decommissioned resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceOffline: list of ResourceOffline
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Common = None
        self._Results = None
        self._ResourceOffline = None
        self._RequestId = None

    @property
    def Common(self):
        """List of general filed configuration parameters
        :rtype: list of ActionFieldConfigResult
        """
        return self._Common

    @Common.setter
    def Common(self, Common):
        self._Common = Common

    @property
    def Results(self):
        """List of action filed configuration parameters
        :rtype: list of ActionFieldConfigResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ResourceOffline(self):
        """Information on the decommissioned resource
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceOffline
        """
        return self._ResourceOffline

    @ResourceOffline.setter
    def ResourceOffline(self, ResourceOffline):
        self._ResourceOffline = ResourceOffline

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
        if params.get("Common") is not None:
            self._Common = []
            for item in params.get("Common"):
                obj = ActionFieldConfigResult()
                obj._deserialize(item)
                self._Common.append(obj)
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ActionFieldConfigResult()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("ResourceOffline") is not None:
            self._ResourceOffline = []
            for item in params.get("ResourceOffline"):
                obj = ResourceOffline()
                obj._deserialize(item)
                self._ResourceOffline.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeActionLibraryListRequest(AbstractModel):
    """DescribeActionLibraryList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: 0-100
        :type Limit: int
        :param _Offset: Default value: 0
        :type Offset: int
        :param _ObjectType: Object type ID
        :type ObjectType: int
        :param _Filters: Keyword value {"action name": "a_title", "description": "a_desc", "action type": "a_type", "creation time": "a_create_time", "level-2 type": "a_resource_type"}
        :type Filters: list of ActionFilter
        :param _Attribute: Action type. 1: fault action; 2: recovery action.
        :type Attribute: list of int
        :param _ActionIds: Filter item - action ID
        :type ActionIds: list of int non-negative
        """
        self._Limit = None
        self._Offset = None
        self._ObjectType = None
        self._Filters = None
        self._Attribute = None
        self._ActionIds = None

    @property
    def Limit(self):
        """0-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ObjectType(self):
        """Object type ID
        :rtype: int
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Filters(self):
        """Keyword value {"action name": "a_title", "description": "a_desc", "action type": "a_type", "creation time": "a_create_time", "level-2 type": "a_resource_type"}
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Attribute(self):
        """Action type. 1: fault action; 2: recovery action.
        :rtype: list of int
        """
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def ActionIds(self):
        """Filter item - action ID
        :rtype: list of int non-negative
        """
        return self._ActionIds

    @ActionIds.setter
    def ActionIds(self, ActionIds):
        self._ActionIds = ActionIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ObjectType = params.get("ObjectType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Attribute = params.get("Attribute")
        self._ActionIds = params.get("ActionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLibraryListResponse(AbstractModel):
    """DescribeActionLibraryList response structure.

    """

    def __init__(self):
        r"""
        :param _Results: Query result list
        :type Results: list of ActionLibraryListResult
        :param _Total: Number of matching records
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Results = None
        self._Total = None
        self._RequestId = None

    @property
    def Results(self):
        """Query result list
        :rtype: list of ActionLibraryListResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Total(self):
        """Number of matching records
        :rtype: int
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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ActionLibraryListResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeObjectTypeListRequest(AbstractModel):
    """DescribeObjectTypeList request structure.

    """

    def __init__(self):
        r"""
        :param _SupportType: Supported object
0: all platform products
1: objects connected to the platform
2: some objects supported by the application
        :type SupportType: int
        """
        self._SupportType = None

    @property
    def SupportType(self):
        """Supported object
0: all platform products
1: objects connected to the platform
2: some objects supported by the application
        :rtype: int
        """
        return self._SupportType

    @SupportType.setter
    def SupportType(self, SupportType):
        self._SupportType = SupportType


    def _deserialize(self, params):
        self._SupportType = params.get("SupportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeObjectTypeListResponse(AbstractModel):
    """DescribeObjectTypeList response structure.

    """

    def __init__(self):
        r"""
        :param _ObjectTypeList: Object type list
        :type ObjectTypeList: list of ObjectType
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ObjectTypeList = None
        self._RequestId = None

    @property
    def ObjectTypeList(self):
        """Object type list
        :rtype: list of ObjectType
        """
        return self._ObjectTypeList

    @ObjectTypeList.setter
    def ObjectTypeList(self, ObjectTypeList):
        self._ObjectTypeList = ObjectTypeList

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
        if params.get("ObjectTypeList") is not None:
            self._ObjectTypeList = []
            for item in params.get("ObjectTypeList"):
                obj = ObjectType()
                obj._deserialize(item)
                self._ObjectTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicy(AbstractModel):
    """Protection policy

    """

    def __init__(self):
        r"""
        :param _TaskPolicyIdList: Protection policy ID list
        :type TaskPolicyIdList: list of str
        :param _TaskPolicyStatus: Protection policy status
        :type TaskPolicyStatus: str
        :param _TaskPolicyRule: Policy rule
        :type TaskPolicyRule: str
        :param _TaskPolicyDealType: Process method when the guardrail policy takes effect. 1: sequential execution, 2: pausing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPolicyDealType: int
        """
        self._TaskPolicyIdList = None
        self._TaskPolicyStatus = None
        self._TaskPolicyRule = None
        self._TaskPolicyDealType = None

    @property
    def TaskPolicyIdList(self):
        """Protection policy ID list
        :rtype: list of str
        """
        return self._TaskPolicyIdList

    @TaskPolicyIdList.setter
    def TaskPolicyIdList(self, TaskPolicyIdList):
        self._TaskPolicyIdList = TaskPolicyIdList

    @property
    def TaskPolicyStatus(self):
        """Protection policy status
        :rtype: str
        """
        return self._TaskPolicyStatus

    @TaskPolicyStatus.setter
    def TaskPolicyStatus(self, TaskPolicyStatus):
        self._TaskPolicyStatus = TaskPolicyStatus

    @property
    def TaskPolicyRule(self):
        """Policy rule
        :rtype: str
        """
        return self._TaskPolicyRule

    @TaskPolicyRule.setter
    def TaskPolicyRule(self, TaskPolicyRule):
        self._TaskPolicyRule = TaskPolicyRule

    @property
    def TaskPolicyDealType(self):
        """Process method when the guardrail policy takes effect. 1: sequential execution, 2: pausing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskPolicyDealType

    @TaskPolicyDealType.setter
    def TaskPolicyDealType(self, TaskPolicyDealType):
        self._TaskPolicyDealType = TaskPolicyDealType


    def _deserialize(self, params):
        self._TaskPolicyIdList = params.get("TaskPolicyIdList")
        self._TaskPolicyStatus = params.get("TaskPolicyStatus")
        self._TaskPolicyRule = params.get("TaskPolicyRule")
        self._TaskPolicyDealType = params.get("TaskPolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsRequest(AbstractModel):
    """DescribeTaskExecuteLogs request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _Limit: Number of returned content lines
        :type Limit: int
        :param _Offset: Log start line
        :type Offset: int
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """Number of returned content lines
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Log start line
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsResponse(AbstractModel):
    """DescribeTaskExecuteLogs response structure.

    """

    def __init__(self):
        r"""
        :param _LogMessage: Log data
        :type LogMessage: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogMessage = None
        self._RequestId = None

    @property
    def LogMessage(self):
        """Log data
        :rtype: list of str
        """
        return self._LogMessage

    @LogMessage.setter
    def LogMessage(self, LogMessage):
        self._LogMessage = LogMessage

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
        self._LogMessage = params.get("LogMessage")
        self._RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _TaskTitle: Experiment name
        :type TaskTitle: str
        :param _TaskTag: Tag key
        :type TaskTag: list of str
        :param _TaskStatus: Task status (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :type TaskStatus: int
        :param _TaskStartTime: Start time, in fixed format: %Y-%m-%d %H:%M:%S
        :type TaskStartTime: str
        :param _TaskEndTime: End time, in fixed format: %Y-%m-%d %H:%M:%S
        :type TaskEndTime: str
        :param _TaskUpdateTime: Update time, in fixed format: %Y-%m-%d %H:%M:%S
        :type TaskUpdateTime: str
        :param _Tags: Tag pair
        :type Tags: list of TagWithDescribe
        :param _Filters: Filtering criteria
        :type Filters: list of ActionFilter
        :param _TaskId: Experiment ID
        :type TaskId: list of int non-negative
        :param _ApplicationId: ID of the associated application for filtering
        :type ApplicationId: list of str
        :param _ApplicationName: Associated application for filtering
        :type ApplicationName: list of str
        :param _TaskStatusList: Task status for filtering, supporting multiple states (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :type TaskStatusList: list of int non-negative
        :param _ArchId: 
        :type ArchId: str
        :param _ArchName: 
        :type ArchName: str
        """
        self._Limit = None
        self._Offset = None
        self._TaskTitle = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskStartTime = None
        self._TaskEndTime = None
        self._TaskUpdateTime = None
        self._Tags = None
        self._Filters = None
        self._TaskId = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._TaskStatusList = None
        self._ArchId = None
        self._ArchName = None

    @property
    def Limit(self):
        """Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TaskTitle(self):
        """Experiment name
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskTag(self):
        """Tag key
        :rtype: list of str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """Task status (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskStartTime(self):
        """Start time, in fixed format: %Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskStartTime

    @TaskStartTime.setter
    def TaskStartTime(self, TaskStartTime):
        self._TaskStartTime = TaskStartTime

    @property
    def TaskEndTime(self):
        """End time, in fixed format: %Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskEndTime

    @TaskEndTime.setter
    def TaskEndTime(self, TaskEndTime):
        self._TaskEndTime = TaskEndTime

    @property
    def TaskUpdateTime(self):
        """Update time, in fixed format: %Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def Tags(self):
        """Tag pair
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Filters(self):
        """Filtering criteria
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TaskId(self):
        """Experiment ID
        :rtype: list of int non-negative
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ApplicationId(self):
        """ID of the associated application for filtering
        :rtype: list of str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """Associated application for filtering
        :rtype: list of str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def TaskStatusList(self):
        """Task status for filtering, supporting multiple states (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :rtype: list of int non-negative
        """
        return self._TaskStatusList

    @TaskStatusList.setter
    def TaskStatusList(self, TaskStatusList):
        self._TaskStatusList = TaskStatusList

    @property
    def ArchId(self):
        """
        :rtype: str
        """
        return self._ArchId

    @ArchId.setter
    def ArchId(self, ArchId):
        self._ArchId = ArchId

    @property
    def ArchName(self):
        """
        :rtype: str
        """
        return self._ArchName

    @ArchName.setter
    def ArchName(self, ArchName):
        self._ArchName = ArchName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskStartTime = params.get("TaskStartTime")
        self._TaskEndTime = params.get("TaskEndTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TaskId = params.get("TaskId")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._TaskStatusList = params.get("TaskStatusList")
        self._ArchId = params.get("ArchId")
        self._ArchName = params.get("ArchName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList response structure.

    """

    def __init__(self):
        r"""
        :param _TaskList: None
        :type TaskList: list of TaskListItem
        :param _Total: Number of tables in the list
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskList = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskList(self):
        """None
        :rtype: list of TaskListItem
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def Total(self):
        """Number of tables in the list
        :rtype: int
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
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = TaskListItem()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTaskPolicyTriggerLogRequest(AbstractModel):
    """DescribeTaskPolicyTriggerLog request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Experiment ID
        :type TaskId: int
        :param _Page: Page number
        :type Page: int
        :param _PageSize: Number of entries per page
        :type PageSize: int
        """
        self._TaskId = None
        self._Page = None
        self._PageSize = None

    @property
    def TaskId(self):
        """Experiment ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Page(self):
        """Page number
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """Number of entries per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskPolicyTriggerLogResponse(AbstractModel):
    """DescribeTaskPolicyTriggerLog response structure.

    """

    def __init__(self):
        r"""
        :param _TriggerLogs: Triggering log
Note: This field may return null, indicating that no valid values can be obtained.
        :type TriggerLogs: list of PolicyTriggerLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TriggerLogs = None
        self._RequestId = None

    @property
    def TriggerLogs(self):
        """Triggering log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PolicyTriggerLog
        """
        return self._TriggerLogs

    @TriggerLogs.setter
    def TriggerLogs(self, TriggerLogs):
        self._TriggerLogs = TriggerLogs

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
        if params.get("TriggerLogs") is not None:
            self._TriggerLogs = []
            for item in params.get("TriggerLogs"):
                obj = PolicyTriggerLog()
                obj._deserialize(item)
                self._TriggerLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Task ID
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
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask response structure.

    """

    def __init__(self):
        r"""
        :param _Task: Task information
        :type Task: :class:`tencentcloud.cfg.v20210820.models.Task`
        :param _ReportInfo: Experiment report information corresponding to the task. The value null indicates that no report is exported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReportInfo: :class:`tencentcloud.cfg.v20210820.models.TaskReportInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Task = None
        self._ReportInfo = None
        self._RequestId = None

    @property
    def Task(self):
        """Task information
        :rtype: :class:`tencentcloud.cfg.v20210820.models.Task`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def ReportInfo(self):
        """Experiment report information corresponding to the task. The value null indicates that no report is exported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TaskReportInfo`
        """
        return self._ReportInfo

    @ReportInfo.setter
    def ReportInfo(self, ReportInfo):
        self._ReportInfo = ReportInfo

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
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        if params.get("ReportInfo") is not None:
            self._ReportInfo = TaskReportInfo()
            self._ReportInfo._deserialize(params.get("ReportInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTemplateListRequest(AbstractModel):
    """DescribeTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Pagination limit.Maximum value:100.
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Title: Experiment name
        :type Title: str
        :param _Tag: Tag key
        :type Tag: list of str
        :param _IsUsed: Status. 1: in use; 2: not in use.
        :type IsUsed: int
        :param _Tags: Tag pair
        :type Tags: list of TagWithDescribe
        :param _TemplateSource: Template library source. 0: self-built; 1: recommended by experts.
        :type TemplateSource: int
        :param _TemplateIdList: Template ID
        :type TemplateIdList: list of int
        :param _Filters: Filter parameters
        :type Filters: list of ActionFilter
        """
        self._Limit = None
        self._Offset = None
        self._Title = None
        self._Tag = None
        self._IsUsed = None
        self._Tags = None
        self._TemplateSource = None
        self._TemplateIdList = None
        self._Filters = None

    @property
    def Limit(self):
        """Pagination limit.Maximum value:100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Title(self):
        """Experiment name
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Tag(self):
        """Tag key
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def IsUsed(self):
        """Status. 1: in use; 2: not in use.
        :rtype: int
        """
        return self._IsUsed

    @IsUsed.setter
    def IsUsed(self, IsUsed):
        self._IsUsed = IsUsed

    @property
    def Tags(self):
        """Tag pair
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TemplateSource(self):
        """Template library source. 0: self-built; 1: recommended by experts.
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource

    @property
    def TemplateIdList(self):
        """Template ID
        :rtype: list of int
        """
        return self._TemplateIdList

    @TemplateIdList.setter
    def TemplateIdList(self, TemplateIdList):
        self._TemplateIdList = TemplateIdList

    @property
    def Filters(self):
        """Filter parameters
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Title = params.get("Title")
        self._Tag = params.get("Tag")
        self._IsUsed = params.get("IsUsed")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TemplateSource = params.get("TemplateSource")
        self._TemplateIdList = params.get("TemplateIdList")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateListResponse(AbstractModel):
    """DescribeTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateList: Template library list
        :type TemplateList: list of TemplateListItem
        :param _Total: Number of template libraries in the list
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateList = None
        self._Total = None
        self._RequestId = None

    @property
    def TemplateList(self):
        """Template library list
        :rtype: list of TemplateListItem
        """
        return self._TemplateList

    @TemplateList.setter
    def TemplateList(self, TemplateList):
        self._TemplateList = TemplateList

    @property
    def Total(self):
        """Number of template libraries in the list
        :rtype: int
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
        if params.get("TemplateList") is not None:
            self._TemplateList = []
            for item in params.get("TemplateList"):
                obj = TemplateListItem()
                obj._deserialize(item)
                self._TemplateList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTemplateRequest(AbstractModel):
    """DescribeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template library ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """Template library ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateResponse(AbstractModel):
    """DescribeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Template: Template library details
        :type Template: :class:`tencentcloud.cfg.v20210820.models.Template`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        """Template library details
        :rtype: :class:`tencentcloud.cfg.v20210820.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

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
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class ExecuteTaskInstanceRequest(AbstractModel):
    """ExecuteTaskInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _TaskActionId: Task action ID
        :type TaskActionId: int
        :param _TaskInstanceIds: Task action instance ID
        :type TaskInstanceIds: list of int non-negative
        :param _IsOperateAll: Whether to operate on the entire task
        :type IsOperateAll: bool
        :param _ActionType: Operation type (1: start; 2: execute; 3: skip; 5: retry)
        :type ActionType: int
        :param _TaskGroupId: Action group ID
        :type TaskGroupId: int
        """
        self._TaskId = None
        self._TaskActionId = None
        self._TaskInstanceIds = None
        self._IsOperateAll = None
        self._ActionType = None
        self._TaskGroupId = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskActionId(self):
        """Task action ID
        :rtype: int
        """
        return self._TaskActionId

    @TaskActionId.setter
    def TaskActionId(self, TaskActionId):
        self._TaskActionId = TaskActionId

    @property
    def TaskInstanceIds(self):
        """Task action instance ID
        :rtype: list of int non-negative
        """
        return self._TaskInstanceIds

    @TaskInstanceIds.setter
    def TaskInstanceIds(self, TaskInstanceIds):
        self._TaskInstanceIds = TaskInstanceIds

    @property
    def IsOperateAll(self):
        """Whether to operate on the entire task
        :rtype: bool
        """
        return self._IsOperateAll

    @IsOperateAll.setter
    def IsOperateAll(self, IsOperateAll):
        self._IsOperateAll = IsOperateAll

    @property
    def ActionType(self):
        """Operation type (1: start; 2: execute; 3: skip; 5: retry)
        :rtype: int
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def TaskGroupId(self):
        """Action group ID
        :rtype: int
        """
        return self._TaskGroupId

    @TaskGroupId.setter
    def TaskGroupId(self, TaskGroupId):
        self._TaskGroupId = TaskGroupId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskActionId = params.get("TaskActionId")
        self._TaskInstanceIds = params.get("TaskInstanceIds")
        self._IsOperateAll = params.get("IsOperateAll")
        self._ActionType = params.get("ActionType")
        self._TaskGroupId = params.get("TaskGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskInstanceResponse(AbstractModel):
    """ExecuteTaskInstance response structure.

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


class ExecuteTaskRequest(AbstractModel):
    """ExecuteTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the task to be executed
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """ID of the task to be executed
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
        


class ExecuteTaskResponse(AbstractModel):
    """ExecuteTask response structure.

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


class ModifyTaskRunStatusRequest(AbstractModel):
    """ModifyTaskRunStatus request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _Status: Task status. 1001: not started; 1002: in progress (executing); 1003: in progress (paused); 1004: execution ended.
        :type Status: int
        :param _IsExpect: Whether the execution result meets expectations (This field is required when the task status is Execution Ended.)
        :type IsExpect: bool
        :param _Summary: Experiment result (This field is required when the experiment status changes to Execution Ended.)
        :type Summary: str
        """
        self._TaskId = None
        self._Status = None
        self._IsExpect = None
        self._Summary = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """Task status. 1001: not started; 1002: in progress (executing); 1003: in progress (paused); 1004: execution ended.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsExpect(self):
        """Whether the execution result meets expectations (This field is required when the task status is Execution Ended.)
        :rtype: bool
        """
        return self._IsExpect

    @IsExpect.setter
    def IsExpect(self, IsExpect):
        self._IsExpect = IsExpect

    @property
    def Summary(self):
        """Experiment result (This field is required when the experiment status changes to Execution Ended.)
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._IsExpect = params.get("IsExpect")
        self._Summary = params.get("Summary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskRunStatusResponse(AbstractModel):
    """ModifyTaskRunStatus response structure.

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


class ObjectType(AbstractModel):
    """Object type

    """

    def __init__(self):
        r"""
        :param _ObjectTypeId: Object type ID
        :type ObjectTypeId: int
        :param _ObjectTypeTitle: Object type name
        :type ObjectTypeTitle: str
        :param _ObjectTypeLevelOne: Level-1 object type
        :type ObjectTypeLevelOne: str
        :param _ObjectTypeParams: Object type parameters
        :type ObjectTypeParams: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeConfig`
        :param _ObjectTypeJsonParse: JSON parsing rule for TKE APIs. If the value is null, no parsing is needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectTypeJsonParse: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeJsonParse`
        :param _ObjectHasNewAction: Whether new action is included
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectHasNewAction: bool
        """
        self._ObjectTypeId = None
        self._ObjectTypeTitle = None
        self._ObjectTypeLevelOne = None
        self._ObjectTypeParams = None
        self._ObjectTypeJsonParse = None
        self._ObjectHasNewAction = None

    @property
    def ObjectTypeId(self):
        """Object type ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def ObjectTypeTitle(self):
        """Object type name
        :rtype: str
        """
        return self._ObjectTypeTitle

    @ObjectTypeTitle.setter
    def ObjectTypeTitle(self, ObjectTypeTitle):
        self._ObjectTypeTitle = ObjectTypeTitle

    @property
    def ObjectTypeLevelOne(self):
        """Level-1 object type
        :rtype: str
        """
        return self._ObjectTypeLevelOne

    @ObjectTypeLevelOne.setter
    def ObjectTypeLevelOne(self, ObjectTypeLevelOne):
        self._ObjectTypeLevelOne = ObjectTypeLevelOne

    @property
    def ObjectTypeParams(self):
        """Object type parameters
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeConfig`
        """
        return self._ObjectTypeParams

    @ObjectTypeParams.setter
    def ObjectTypeParams(self, ObjectTypeParams):
        self._ObjectTypeParams = ObjectTypeParams

    @property
    def ObjectTypeJsonParse(self):
        """JSON parsing rule for TKE APIs. If the value is null, no parsing is needed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeJsonParse`
        """
        return self._ObjectTypeJsonParse

    @ObjectTypeJsonParse.setter
    def ObjectTypeJsonParse(self, ObjectTypeJsonParse):
        self._ObjectTypeJsonParse = ObjectTypeJsonParse

    @property
    def ObjectHasNewAction(self):
        """Whether new action is included
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ObjectHasNewAction

    @ObjectHasNewAction.setter
    def ObjectHasNewAction(self, ObjectHasNewAction):
        self._ObjectHasNewAction = ObjectHasNewAction


    def _deserialize(self, params):
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._ObjectTypeTitle = params.get("ObjectTypeTitle")
        self._ObjectTypeLevelOne = params.get("ObjectTypeLevelOne")
        if params.get("ObjectTypeParams") is not None:
            self._ObjectTypeParams = ObjectTypeConfig()
            self._ObjectTypeParams._deserialize(params.get("ObjectTypeParams"))
        if params.get("ObjectTypeJsonParse") is not None:
            self._ObjectTypeJsonParse = ObjectTypeJsonParse()
            self._ObjectTypeJsonParse._deserialize(params.get("ObjectTypeJsonParse"))
        self._ObjectHasNewAction = params.get("ObjectHasNewAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeConfig(AbstractModel):
    """Object type configuration

    """

    def __init__(self):
        r"""
        :param _Key: Primary key
        :type Key: str
        :param _Fields: List of object type configuration fields
        :type Fields: list of ObjectTypeConfigFields
        """
        self._Key = None
        self._Fields = None

    @property
    def Key(self):
        """Primary key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Fields(self):
        """List of object type configuration fields
        :rtype: list of ObjectTypeConfigFields
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = ObjectTypeConfigFields()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeConfigFields(AbstractModel):
    """Field information on the experiment resource object

    """

    def __init__(self):
        r"""
        :param _Key: instanceId
        :type Key: str
        :param _Header: Instance ID
        :type Header: str
        :param _Transfer: Whether the field value needs to be translated. If not, this field returns null.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Transfer: str
        :param _JsonParse: Value returned for container Pod resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonParse: str
        """
        self._Key = None
        self._Header = None
        self._Transfer = None
        self._JsonParse = None

    @property
    def Key(self):
        """instanceId
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Header(self):
        """Instance ID
        :rtype: str
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Transfer(self):
        """Whether the field value needs to be translated. If not, this field returns null.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Transfer

    @Transfer.setter
    def Transfer(self, Transfer):
        self._Transfer = Transfer

    @property
    def JsonParse(self):
        """Value returned for container Pod resources
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JsonParse

    @JsonParse.setter
    def JsonParse(self, JsonParse):
        self._JsonParse = JsonParse


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Header = params.get("Header")
        self._Transfer = params.get("Transfer")
        self._JsonParse = params.get("JsonParse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeJsonParse(AbstractModel):
    """Value returned for container Pod resources

    """

    def __init__(self):
        r"""
        :param _NameSpace: Namespace

Note: This field may return null, indicating that no valid values can be obtained.
        :type NameSpace: str
        :param _WorkloadName: Workload name
Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkloadName: str
        :param _LanIP: Node IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type LanIP: str
        :param _InstanceId: Node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        """
        self._NameSpace = None
        self._WorkloadName = None
        self._LanIP = None
        self._InstanceId = None

    @property
    def NameSpace(self):
        """Namespace

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def WorkloadName(self):
        """Workload name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName

    @property
    def LanIP(self):
        """Node IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def InstanceId(self):
        """Node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._NameSpace = params.get("NameSpace")
        self._WorkloadName = params.get("WorkloadName")
        self._LanIP = params.get("LanIP")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyTriggerLog(AbstractModel):
    """Guardrail policy triggering log

    """

    def __init__(self):
        r"""
        :param _TaskId: Experiment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _Name: Name

Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _TriggerType: Type. 0: trigger; 1: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TriggerType: int
        :param _Content: Content
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param _CreatTime: Triggering time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatTime: str
        """
        self._TaskId = None
        self._Name = None
        self._TriggerType = None
        self._Content = None
        self._CreatTime = None

    @property
    def TaskId(self):
        """Experiment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """Name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TriggerType(self):
        """Type. 0: trigger; 1: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Content(self):
        """Content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreatTime(self):
        """Triggering time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._TriggerType = params.get("TriggerType")
        self._Content = params.get("Content")
        self._CreatTime = params.get("CreatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOffline(AbstractModel):
    """Decommissioned resource

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceId: int
        :param _ResourceDeleteTime: Resource decommissioning time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceDeleteTime: str
        :param _ResourceDeleteMessage: Resource decommissioning reminder
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceDeleteMessage: str
        """
        self._ResourceId = None
        self._ResourceDeleteTime = None
        self._ResourceDeleteMessage = None

    @property
    def ResourceId(self):
        """Resource ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceDeleteTime(self):
        """Resource decommissioning time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceDeleteTime

    @ResourceDeleteTime.setter
    def ResourceDeleteTime(self, ResourceDeleteTime):
        self._ResourceDeleteTime = ResourceDeleteTime

    @property
    def ResourceDeleteMessage(self):
        """Resource decommissioning reminder
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceDeleteMessage

    @ResourceDeleteMessage.setter
    def ResourceDeleteMessage(self, ResourceDeleteMessage):
        self._ResourceDeleteMessage = ResourceDeleteMessage


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceDeleteTime = params.get("ResourceDeleteTime")
        self._ResourceDeleteMessage = params.get("ResourceDeleteMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagWithCreate(AbstractModel):
    """Tag information, which is used during experiment resource creation and editing.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: str
        """
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
        


class TagWithDescribe(AbstractModel):
    """List of displayed tags

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: str
        """
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
        


class Task(AbstractModel):
    """Task

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _TaskTitle: Task name
        :type TaskTitle: str
        :param _TaskDescription: Task description
        :type TaskDescription: str
        :param _TaskTag: Custom tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskTag: str
        :param _TaskStatus: Task status. 1001: not started; 1002: in progress (executing); 1003: in progress (paused); 1004: execution ended.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskStatus: int
        :param _TaskStatusType: Task end status, indicating the status of the task when it ends. 0: not ended; 1: successful; 2: failed; 3: terminated.
        :type TaskStatusType: int
        :param _TaskProtectStrategy: Protection policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskProtectStrategy: str
        :param _TaskCreateTime: Task creation time
        :type TaskCreateTime: str
        :param _TaskUpdateTime: Task update time
        :type TaskUpdateTime: str
        :param _TaskGroups: Task action group
        :type TaskGroups: list of TaskGroup
        :param _TaskStartTime: Start time

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskStartTime: str
        :param _TaskEndTime: End time

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskEndTime: str
        :param _TaskExpect: Whether expectations are met. 1: expectations met; 2: expectations not met.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskExpect: int
        :param _TaskSummary: Experiment record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskSummary: str
        :param _TaskMode: Task mode. 1: manual execution; 2: automatic execution.
        :type TaskMode: int
        :param _TaskPauseDuration: Automatic pause duration. Unit: minutes.
        :type TaskPauseDuration: int
        :param _TaskOwnerUin: Main account that creates the experiment
        :type TaskOwnerUin: str
        :param _TaskRegionId: Region ID
        :type TaskRegionId: int
        :param _TaskMonitors: Monitoring metric list
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskMonitors: list of TaskMonitor
        :param _TaskPolicy: Protection policy
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPolicy: :class:`tencentcloud.cfg.v20210820.models.DescribePolicy`
        :param _Tags: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagWithDescribe
        :param _TaskPlanId: ID of the associated experiment plan
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPlanId: int
        :param _TaskPlanTitle: Name of the associated experiment plan
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPlanTitle: str
        :param _ApplicationId: ID of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _ApplicationName: Name of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _AlarmPolicy: Associated alarm metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlarmPolicy: list of str
        :param _ApmServiceList: Associated APM services
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmServiceList: list of ApmServiceInfo
        :param _VerifyId: ID of the associated threat verification item
Note: This field may return null, indicating that no valid values can be obtained.
        :type VerifyId: int
        :param _PolicyDealType: Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyDealType: int
        """
        self._TaskId = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskStatusType = None
        self._TaskProtectStrategy = None
        self._TaskCreateTime = None
        self._TaskUpdateTime = None
        self._TaskGroups = None
        self._TaskStartTime = None
        self._TaskEndTime = None
        self._TaskExpect = None
        self._TaskSummary = None
        self._TaskMode = None
        self._TaskPauseDuration = None
        self._TaskOwnerUin = None
        self._TaskRegionId = None
        self._TaskMonitors = None
        self._TaskPolicy = None
        self._Tags = None
        self._TaskPlanId = None
        self._TaskPlanTitle = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._AlarmPolicy = None
        self._ApmServiceList = None
        self._VerifyId = None
        self._PolicyDealType = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTitle(self):
        """Task name
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """Task description
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskTag(self):
        """Custom tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """Task status. 1001: not started; 1002: in progress (executing); 1003: in progress (paused); 1004: execution ended.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskStatusType(self):
        """Task end status, indicating the status of the task when it ends. 0: not ended; 1: successful; 2: failed; 3: terminated.
        :rtype: int
        """
        return self._TaskStatusType

    @TaskStatusType.setter
    def TaskStatusType(self, TaskStatusType):
        self._TaskStatusType = TaskStatusType

    @property
    def TaskProtectStrategy(self):
        """Protection policy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskProtectStrategy

    @TaskProtectStrategy.setter
    def TaskProtectStrategy(self, TaskProtectStrategy):
        self._TaskProtectStrategy = TaskProtectStrategy

    @property
    def TaskCreateTime(self):
        """Task creation time
        :rtype: str
        """
        return self._TaskCreateTime

    @TaskCreateTime.setter
    def TaskCreateTime(self, TaskCreateTime):
        self._TaskCreateTime = TaskCreateTime

    @property
    def TaskUpdateTime(self):
        """Task update time
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def TaskGroups(self):
        """Task action group
        :rtype: list of TaskGroup
        """
        return self._TaskGroups

    @TaskGroups.setter
    def TaskGroups(self, TaskGroups):
        self._TaskGroups = TaskGroups

    @property
    def TaskStartTime(self):
        """Start time

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskStartTime

    @TaskStartTime.setter
    def TaskStartTime(self, TaskStartTime):
        self._TaskStartTime = TaskStartTime

    @property
    def TaskEndTime(self):
        """End time

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskEndTime

    @TaskEndTime.setter
    def TaskEndTime(self, TaskEndTime):
        self._TaskEndTime = TaskEndTime

    @property
    def TaskExpect(self):
        """Whether expectations are met. 1: expectations met; 2: expectations not met.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskExpect

    @TaskExpect.setter
    def TaskExpect(self, TaskExpect):
        self._TaskExpect = TaskExpect

    @property
    def TaskSummary(self):
        """Experiment record
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskSummary

    @TaskSummary.setter
    def TaskSummary(self, TaskSummary):
        self._TaskSummary = TaskSummary

    @property
    def TaskMode(self):
        """Task mode. 1: manual execution; 2: automatic execution.
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def TaskPauseDuration(self):
        """Automatic pause duration. Unit: minutes.
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration

    @property
    def TaskOwnerUin(self):
        """Main account that creates the experiment
        :rtype: str
        """
        return self._TaskOwnerUin

    @TaskOwnerUin.setter
    def TaskOwnerUin(self, TaskOwnerUin):
        self._TaskOwnerUin = TaskOwnerUin

    @property
    def TaskRegionId(self):
        """Region ID
        :rtype: int
        """
        return self._TaskRegionId

    @TaskRegionId.setter
    def TaskRegionId(self, TaskRegionId):
        self._TaskRegionId = TaskRegionId

    @property
    def TaskMonitors(self):
        """Monitoring metric list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TaskMonitor
        """
        return self._TaskMonitors

    @TaskMonitors.setter
    def TaskMonitors(self, TaskMonitors):
        self._TaskMonitors = TaskMonitors

    @property
    def TaskPolicy(self):
        """Protection policy
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribePolicy`
        """
        return self._TaskPolicy

    @TaskPolicy.setter
    def TaskPolicy(self, TaskPolicy):
        self._TaskPolicy = TaskPolicy

    @property
    def Tags(self):
        """Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TaskPlanId(self):
        """ID of the associated experiment plan
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskPlanId

    @TaskPlanId.setter
    def TaskPlanId(self, TaskPlanId):
        self._TaskPlanId = TaskPlanId

    @property
    def TaskPlanTitle(self):
        """Name of the associated experiment plan
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskPlanTitle

    @TaskPlanTitle.setter
    def TaskPlanTitle(self, TaskPlanTitle):
        self._TaskPlanTitle = TaskPlanTitle

    @property
    def ApplicationId(self):
        """ID of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """Name of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def AlarmPolicy(self):
        """Associated alarm metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def ApmServiceList(self):
        """Associated APM services
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmServiceInfo
        """
        return self._ApmServiceList

    @ApmServiceList.setter
    def ApmServiceList(self, ApmServiceList):
        self._ApmServiceList = ApmServiceList

    @property
    def VerifyId(self):
        """ID of the associated threat verification item
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VerifyId

    @VerifyId.setter
    def VerifyId(self, VerifyId):
        self._VerifyId = VerifyId

    @property
    def PolicyDealType(self):
        """Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskStatusType = params.get("TaskStatusType")
        self._TaskProtectStrategy = params.get("TaskProtectStrategy")
        self._TaskCreateTime = params.get("TaskCreateTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        if params.get("TaskGroups") is not None:
            self._TaskGroups = []
            for item in params.get("TaskGroups"):
                obj = TaskGroup()
                obj._deserialize(item)
                self._TaskGroups.append(obj)
        self._TaskStartTime = params.get("TaskStartTime")
        self._TaskEndTime = params.get("TaskEndTime")
        self._TaskExpect = params.get("TaskExpect")
        self._TaskSummary = params.get("TaskSummary")
        self._TaskMode = params.get("TaskMode")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        self._TaskOwnerUin = params.get("TaskOwnerUin")
        self._TaskRegionId = params.get("TaskRegionId")
        if params.get("TaskMonitors") is not None:
            self._TaskMonitors = []
            for item in params.get("TaskMonitors"):
                obj = TaskMonitor()
                obj._deserialize(item)
                self._TaskMonitors.append(obj)
        if params.get("TaskPolicy") is not None:
            self._TaskPolicy = DescribePolicy()
            self._TaskPolicy._deserialize(params.get("TaskPolicy"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TaskPlanId = params.get("TaskPlanId")
        self._TaskPlanTitle = params.get("TaskPlanTitle")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._AlarmPolicy = params.get("AlarmPolicy")
        if params.get("ApmServiceList") is not None:
            self._ApmServiceList = []
            for item in params.get("ApmServiceList"):
                obj = ApmServiceInfo()
                obj._deserialize(item)
                self._ApmServiceList.append(obj)
        self._VerifyId = params.get("VerifyId")
        self._PolicyDealType = params.get("PolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskConfig(AbstractModel):
    """Task parameters that need to be configured when an experiment is created by using a template

    """

    def __init__(self):
        r"""
        :param _TaskGroupsConfig: Action group configurations. The number of configured action groups needs to be consistent with that in the template.
        :type TaskGroupsConfig: list of TaskGroupConfig
        :param _TaskTitle: Experiment name after change. If this parameter is left blank, the template name is used by default.
        :type TaskTitle: str
        :param _TaskDescription: Experiment description after change. If this parameter is left blank, the template description is used by default.
        :type TaskDescription: str
        :param _TaskMode: Experiment execution mode. 1: manual execution; 2: automatic execution. If this parameter is left blank, the template execution mode is used by default.
        :type TaskMode: int
        :param _TaskPauseDuration: Automatic pause time of the experiment, in minutes. If this parameter is left blank, the automatic pause time of the template is used by default.
        :type TaskPauseDuration: int
        :param _Tags: Experiment tag. If this parameter is left blank, the template tag is used by default.
        :type Tags: list of TagWithCreate
        :param _PolicyDealType: Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
        :type PolicyDealType: int
        """
        self._TaskGroupsConfig = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskMode = None
        self._TaskPauseDuration = None
        self._Tags = None
        self._PolicyDealType = None

    @property
    def TaskGroupsConfig(self):
        """Action group configurations. The number of configured action groups needs to be consistent with that in the template.
        :rtype: list of TaskGroupConfig
        """
        return self._TaskGroupsConfig

    @TaskGroupsConfig.setter
    def TaskGroupsConfig(self, TaskGroupsConfig):
        self._TaskGroupsConfig = TaskGroupsConfig

    @property
    def TaskTitle(self):
        """Experiment name after change. If this parameter is left blank, the template name is used by default.
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """Experiment description after change. If this parameter is left blank, the template description is used by default.
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskMode(self):
        """Experiment execution mode. 1: manual execution; 2: automatic execution. If this parameter is left blank, the template execution mode is used by default.
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def TaskPauseDuration(self):
        """Automatic pause time of the experiment, in minutes. If this parameter is left blank, the automatic pause time of the template is used by default.
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration

    @property
    def Tags(self):
        """Experiment tag. If this parameter is left blank, the template tag is used by default.
        :rtype: list of TagWithCreate
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PolicyDealType(self):
        """Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType


    def _deserialize(self, params):
        if params.get("TaskGroupsConfig") is not None:
            self._TaskGroupsConfig = []
            for item in params.get("TaskGroupsConfig"):
                obj = TaskGroupConfig()
                obj._deserialize(item)
                self._TaskGroupsConfig.append(obj)
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskMode = params.get("TaskMode")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithCreate()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PolicyDealType = params.get("PolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroup(AbstractModel):
    """Task group

    """

    def __init__(self):
        r"""
        :param _TaskGroupId: Task action ID
        :type TaskGroupId: int
        :param _TaskGroupTitle: Group name
        :type TaskGroupTitle: str
        :param _TaskGroupDescription: Group description
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupDescription: str
        :param _TaskGroupOrder: Task group order
        :type TaskGroupOrder: int
        :param _ObjectTypeId: Object type ID
        :type ObjectTypeId: int
        :param _TaskGroupCreateTime: Task group creation time
        :type TaskGroupCreateTime: str
        :param _TaskGroupUpdateTime: Task group update time
        :type TaskGroupUpdateTime: str
        :param _TaskGroupActions: List of actions in the group
        :type TaskGroupActions: list of TaskGroupAction
        :param _TaskGroupInstanceList: Instance list
        :type TaskGroupInstanceList: list of str
        :param _TaskGroupMode: Execution mode. 1: sequential execution; 2: execution by stage.
        :type TaskGroupMode: int
        :param _TaskGroupDiscardInstanceList: List of instances not involved in the experiment
        :type TaskGroupDiscardInstanceList: list of str
        :param _TaskGroupSelectedInstanceList: List of instances involved in the experiment
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupSelectedInstanceList: list of str
        :param _TaskGroupInstancesExecuteRule: Machine selection rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstancesExecuteRule: list of TaskGroupInstancesExecuteRules
        """
        self._TaskGroupId = None
        self._TaskGroupTitle = None
        self._TaskGroupDescription = None
        self._TaskGroupOrder = None
        self._ObjectTypeId = None
        self._TaskGroupCreateTime = None
        self._TaskGroupUpdateTime = None
        self._TaskGroupActions = None
        self._TaskGroupInstanceList = None
        self._TaskGroupMode = None
        self._TaskGroupDiscardInstanceList = None
        self._TaskGroupSelectedInstanceList = None
        self._TaskGroupInstancesExecuteRule = None

    @property
    def TaskGroupId(self):
        """Task action ID
        :rtype: int
        """
        return self._TaskGroupId

    @TaskGroupId.setter
    def TaskGroupId(self, TaskGroupId):
        self._TaskGroupId = TaskGroupId

    @property
    def TaskGroupTitle(self):
        """Group name
        :rtype: str
        """
        return self._TaskGroupTitle

    @TaskGroupTitle.setter
    def TaskGroupTitle(self, TaskGroupTitle):
        self._TaskGroupTitle = TaskGroupTitle

    @property
    def TaskGroupDescription(self):
        """Group description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupDescription

    @TaskGroupDescription.setter
    def TaskGroupDescription(self, TaskGroupDescription):
        self._TaskGroupDescription = TaskGroupDescription

    @property
    def TaskGroupOrder(self):
        """Task group order
        :rtype: int
        """
        return self._TaskGroupOrder

    @TaskGroupOrder.setter
    def TaskGroupOrder(self, TaskGroupOrder):
        self._TaskGroupOrder = TaskGroupOrder

    @property
    def ObjectTypeId(self):
        """Object type ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def TaskGroupCreateTime(self):
        """Task group creation time
        :rtype: str
        """
        return self._TaskGroupCreateTime

    @TaskGroupCreateTime.setter
    def TaskGroupCreateTime(self, TaskGroupCreateTime):
        self._TaskGroupCreateTime = TaskGroupCreateTime

    @property
    def TaskGroupUpdateTime(self):
        """Task group update time
        :rtype: str
        """
        return self._TaskGroupUpdateTime

    @TaskGroupUpdateTime.setter
    def TaskGroupUpdateTime(self, TaskGroupUpdateTime):
        self._TaskGroupUpdateTime = TaskGroupUpdateTime

    @property
    def TaskGroupActions(self):
        """List of actions in the group
        :rtype: list of TaskGroupAction
        """
        return self._TaskGroupActions

    @TaskGroupActions.setter
    def TaskGroupActions(self, TaskGroupActions):
        self._TaskGroupActions = TaskGroupActions

    @property
    def TaskGroupInstanceList(self):
        """Instance list
        :rtype: list of str
        """
        return self._TaskGroupInstanceList

    @TaskGroupInstanceList.setter
    def TaskGroupInstanceList(self, TaskGroupInstanceList):
        self._TaskGroupInstanceList = TaskGroupInstanceList

    @property
    def TaskGroupMode(self):
        """Execution mode. 1: sequential execution; 2: execution by stage.
        :rtype: int
        """
        return self._TaskGroupMode

    @TaskGroupMode.setter
    def TaskGroupMode(self, TaskGroupMode):
        self._TaskGroupMode = TaskGroupMode

    @property
    def TaskGroupDiscardInstanceList(self):
        """List of instances not involved in the experiment
        :rtype: list of str
        """
        return self._TaskGroupDiscardInstanceList

    @TaskGroupDiscardInstanceList.setter
    def TaskGroupDiscardInstanceList(self, TaskGroupDiscardInstanceList):
        self._TaskGroupDiscardInstanceList = TaskGroupDiscardInstanceList

    @property
    def TaskGroupSelectedInstanceList(self):
        """List of instances involved in the experiment
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TaskGroupSelectedInstanceList

    @TaskGroupSelectedInstanceList.setter
    def TaskGroupSelectedInstanceList(self, TaskGroupSelectedInstanceList):
        self._TaskGroupSelectedInstanceList = TaskGroupSelectedInstanceList

    @property
    def TaskGroupInstancesExecuteRule(self):
        """Machine selection rule
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TaskGroupInstancesExecuteRules
        """
        return self._TaskGroupInstancesExecuteRule

    @TaskGroupInstancesExecuteRule.setter
    def TaskGroupInstancesExecuteRule(self, TaskGroupInstancesExecuteRule):
        self._TaskGroupInstancesExecuteRule = TaskGroupInstancesExecuteRule


    def _deserialize(self, params):
        self._TaskGroupId = params.get("TaskGroupId")
        self._TaskGroupTitle = params.get("TaskGroupTitle")
        self._TaskGroupDescription = params.get("TaskGroupDescription")
        self._TaskGroupOrder = params.get("TaskGroupOrder")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._TaskGroupCreateTime = params.get("TaskGroupCreateTime")
        self._TaskGroupUpdateTime = params.get("TaskGroupUpdateTime")
        if params.get("TaskGroupActions") is not None:
            self._TaskGroupActions = []
            for item in params.get("TaskGroupActions"):
                obj = TaskGroupAction()
                obj._deserialize(item)
                self._TaskGroupActions.append(obj)
        self._TaskGroupInstanceList = params.get("TaskGroupInstanceList")
        self._TaskGroupMode = params.get("TaskGroupMode")
        self._TaskGroupDiscardInstanceList = params.get("TaskGroupDiscardInstanceList")
        self._TaskGroupSelectedInstanceList = params.get("TaskGroupSelectedInstanceList")
        if params.get("TaskGroupInstancesExecuteRule") is not None:
            self._TaskGroupInstancesExecuteRule = []
            for item in params.get("TaskGroupInstancesExecuteRule"):
                obj = TaskGroupInstancesExecuteRules()
                obj._deserialize(item)
                self._TaskGroupInstancesExecuteRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupAction(AbstractModel):
    """Task group action

    """

    def __init__(self):
        r"""
        :param _TaskGroupActionId: Task group action ID
        :type TaskGroupActionId: int
        :param _TaskGroupInstances: Action instance list of the task group
        :type TaskGroupInstances: list of TaskGroupInstance
        :param _ActionId: Action ID
        :type ActionId: int
        :param _TaskGroupActionOrder: Order of actions in the group
        :type TaskGroupActionOrder: int
        :param _TaskGroupActionGeneralConfiguration: General configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionGeneralConfiguration: str
        :param _TaskGroupActionCustomConfiguration: Custom configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionCustomConfiguration: str
        :param _TaskGroupActionStatus: Status of actions in the group
        :type TaskGroupActionStatus: int
        :param _TaskGroupActionCreateTime: Action group creation time
        :type TaskGroupActionCreateTime: str
        :param _TaskGroupActionUpdateTime: Action group update time
        :type TaskGroupActionUpdateTime: str
        :param _ActionTitle: Action name
        :type ActionTitle: str
        :param _TaskGroupActionStatusType: Status. 0: no status; 1: successful; 2; failed; 3: terminated; 4: skipped.
        :type TaskGroupActionStatusType: int
        :param _TaskGroupActionRandomId: RandomId
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionRandomId: int
        :param _TaskGroupActionRecoverId: RecoverId
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionRecoverId: int
        :param _TaskGroupActionExecuteId: ExecuteId
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionExecuteId: int
        :param _ActionApiType: Called API type. 0: tat; 1: cloud API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionApiType: int
        :param _ActionAttribute: 1: fault; 2: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionAttribute: int
        :param _ActionType: Action type: platform and custom
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _IsExecuteRedo: Whether retry is allowed
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsExecuteRedo: bool
        :param _ActionRisk: Action risk level
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionRisk: str
        :param _TaskGroupActionExecuteTime: Action running time
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupActionExecuteTime: int
        """
        self._TaskGroupActionId = None
        self._TaskGroupInstances = None
        self._ActionId = None
        self._TaskGroupActionOrder = None
        self._TaskGroupActionGeneralConfiguration = None
        self._TaskGroupActionCustomConfiguration = None
        self._TaskGroupActionStatus = None
        self._TaskGroupActionCreateTime = None
        self._TaskGroupActionUpdateTime = None
        self._ActionTitle = None
        self._TaskGroupActionStatusType = None
        self._TaskGroupActionRandomId = None
        self._TaskGroupActionRecoverId = None
        self._TaskGroupActionExecuteId = None
        self._ActionApiType = None
        self._ActionAttribute = None
        self._ActionType = None
        self._IsExecuteRedo = None
        self._ActionRisk = None
        self._TaskGroupActionExecuteTime = None

    @property
    def TaskGroupActionId(self):
        """Task group action ID
        :rtype: int
        """
        return self._TaskGroupActionId

    @TaskGroupActionId.setter
    def TaskGroupActionId(self, TaskGroupActionId):
        self._TaskGroupActionId = TaskGroupActionId

    @property
    def TaskGroupInstances(self):
        """Action instance list of the task group
        :rtype: list of TaskGroupInstance
        """
        return self._TaskGroupInstances

    @TaskGroupInstances.setter
    def TaskGroupInstances(self, TaskGroupInstances):
        self._TaskGroupInstances = TaskGroupInstances

    @property
    def ActionId(self):
        """Action ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def TaskGroupActionOrder(self):
        """Order of actions in the group
        :rtype: int
        """
        return self._TaskGroupActionOrder

    @TaskGroupActionOrder.setter
    def TaskGroupActionOrder(self, TaskGroupActionOrder):
        self._TaskGroupActionOrder = TaskGroupActionOrder

    @property
    def TaskGroupActionGeneralConfiguration(self):
        """General configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupActionGeneralConfiguration

    @TaskGroupActionGeneralConfiguration.setter
    def TaskGroupActionGeneralConfiguration(self, TaskGroupActionGeneralConfiguration):
        self._TaskGroupActionGeneralConfiguration = TaskGroupActionGeneralConfiguration

    @property
    def TaskGroupActionCustomConfiguration(self):
        """Custom configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupActionCustomConfiguration

    @TaskGroupActionCustomConfiguration.setter
    def TaskGroupActionCustomConfiguration(self, TaskGroupActionCustomConfiguration):
        self._TaskGroupActionCustomConfiguration = TaskGroupActionCustomConfiguration

    @property
    def TaskGroupActionStatus(self):
        """Status of actions in the group
        :rtype: int
        """
        return self._TaskGroupActionStatus

    @TaskGroupActionStatus.setter
    def TaskGroupActionStatus(self, TaskGroupActionStatus):
        self._TaskGroupActionStatus = TaskGroupActionStatus

    @property
    def TaskGroupActionCreateTime(self):
        """Action group creation time
        :rtype: str
        """
        return self._TaskGroupActionCreateTime

    @TaskGroupActionCreateTime.setter
    def TaskGroupActionCreateTime(self, TaskGroupActionCreateTime):
        self._TaskGroupActionCreateTime = TaskGroupActionCreateTime

    @property
    def TaskGroupActionUpdateTime(self):
        """Action group update time
        :rtype: str
        """
        return self._TaskGroupActionUpdateTime

    @TaskGroupActionUpdateTime.setter
    def TaskGroupActionUpdateTime(self, TaskGroupActionUpdateTime):
        self._TaskGroupActionUpdateTime = TaskGroupActionUpdateTime

    @property
    def ActionTitle(self):
        """Action name
        :rtype: str
        """
        return self._ActionTitle

    @ActionTitle.setter
    def ActionTitle(self, ActionTitle):
        self._ActionTitle = ActionTitle

    @property
    def TaskGroupActionStatusType(self):
        """Status. 0: no status; 1: successful; 2; failed; 3: terminated; 4: skipped.
        :rtype: int
        """
        return self._TaskGroupActionStatusType

    @TaskGroupActionStatusType.setter
    def TaskGroupActionStatusType(self, TaskGroupActionStatusType):
        self._TaskGroupActionStatusType = TaskGroupActionStatusType

    @property
    def TaskGroupActionRandomId(self):
        """RandomId
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupActionRandomId

    @TaskGroupActionRandomId.setter
    def TaskGroupActionRandomId(self, TaskGroupActionRandomId):
        self._TaskGroupActionRandomId = TaskGroupActionRandomId

    @property
    def TaskGroupActionRecoverId(self):
        """RecoverId
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupActionRecoverId

    @TaskGroupActionRecoverId.setter
    def TaskGroupActionRecoverId(self, TaskGroupActionRecoverId):
        self._TaskGroupActionRecoverId = TaskGroupActionRecoverId

    @property
    def TaskGroupActionExecuteId(self):
        """ExecuteId
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupActionExecuteId

    @TaskGroupActionExecuteId.setter
    def TaskGroupActionExecuteId(self, TaskGroupActionExecuteId):
        self._TaskGroupActionExecuteId = TaskGroupActionExecuteId

    @property
    def ActionApiType(self):
        """Called API type. 0: tat; 1: cloud API.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ActionApiType

    @ActionApiType.setter
    def ActionApiType(self, ActionApiType):
        self._ActionApiType = ActionApiType

    @property
    def ActionAttribute(self):
        """1: fault; 2: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ActionAttribute

    @ActionAttribute.setter
    def ActionAttribute(self, ActionAttribute):
        self._ActionAttribute = ActionAttribute

    @property
    def ActionType(self):
        """Action type: platform and custom
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def IsExecuteRedo(self):
        """Whether retry is allowed
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsExecuteRedo

    @IsExecuteRedo.setter
    def IsExecuteRedo(self, IsExecuteRedo):
        self._IsExecuteRedo = IsExecuteRedo

    @property
    def ActionRisk(self):
        """Action risk level
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionRisk

    @ActionRisk.setter
    def ActionRisk(self, ActionRisk):
        self._ActionRisk = ActionRisk

    @property
    def TaskGroupActionExecuteTime(self):
        """Action running time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupActionExecuteTime

    @TaskGroupActionExecuteTime.setter
    def TaskGroupActionExecuteTime(self, TaskGroupActionExecuteTime):
        self._TaskGroupActionExecuteTime = TaskGroupActionExecuteTime


    def _deserialize(self, params):
        self._TaskGroupActionId = params.get("TaskGroupActionId")
        if params.get("TaskGroupInstances") is not None:
            self._TaskGroupInstances = []
            for item in params.get("TaskGroupInstances"):
                obj = TaskGroupInstance()
                obj._deserialize(item)
                self._TaskGroupInstances.append(obj)
        self._ActionId = params.get("ActionId")
        self._TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self._TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self._TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        self._TaskGroupActionStatus = params.get("TaskGroupActionStatus")
        self._TaskGroupActionCreateTime = params.get("TaskGroupActionCreateTime")
        self._TaskGroupActionUpdateTime = params.get("TaskGroupActionUpdateTime")
        self._ActionTitle = params.get("ActionTitle")
        self._TaskGroupActionStatusType = params.get("TaskGroupActionStatusType")
        self._TaskGroupActionRandomId = params.get("TaskGroupActionRandomId")
        self._TaskGroupActionRecoverId = params.get("TaskGroupActionRecoverId")
        self._TaskGroupActionExecuteId = params.get("TaskGroupActionExecuteId")
        self._ActionApiType = params.get("ActionApiType")
        self._ActionAttribute = params.get("ActionAttribute")
        self._ActionType = params.get("ActionType")
        self._IsExecuteRedo = params.get("IsExecuteRedo")
        self._ActionRisk = params.get("ActionRisk")
        self._TaskGroupActionExecuteTime = params.get("TaskGroupActionExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupActionConfig(AbstractModel):
    """Action parameters in the action group

    """

    def __init__(self):
        r"""
        :param _TaskGroupActionOrder: Order of this action in the action group. The entire order starts from 1. If this parameter is left blank or set to an invalid value, the action whose parameters need to be modified in the template cannot be matched.
        :type TaskGroupActionOrder: int
        :param _TaskGroupActionGeneralConfiguration: General action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the template details query API. If this field is left blank, action parameters in the template are used by default.
        :type TaskGroupActionGeneralConfiguration: str
        :param _TaskGroupActionCustomConfiguration: Custom action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the template details query API. If this field is left blank, action parameters in the template are used by default.
        :type TaskGroupActionCustomConfiguration: str
        """
        self._TaskGroupActionOrder = None
        self._TaskGroupActionGeneralConfiguration = None
        self._TaskGroupActionCustomConfiguration = None

    @property
    def TaskGroupActionOrder(self):
        """Order of this action in the action group. The entire order starts from 1. If this parameter is left blank or set to an invalid value, the action whose parameters need to be modified in the template cannot be matched.
        :rtype: int
        """
        return self._TaskGroupActionOrder

    @TaskGroupActionOrder.setter
    def TaskGroupActionOrder(self, TaskGroupActionOrder):
        self._TaskGroupActionOrder = TaskGroupActionOrder

    @property
    def TaskGroupActionGeneralConfiguration(self):
        """General action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the template details query API. If this field is left blank, action parameters in the template are used by default.
        :rtype: str
        """
        return self._TaskGroupActionGeneralConfiguration

    @TaskGroupActionGeneralConfiguration.setter
    def TaskGroupActionGeneralConfiguration(self, TaskGroupActionGeneralConfiguration):
        self._TaskGroupActionGeneralConfiguration = TaskGroupActionGeneralConfiguration

    @property
    def TaskGroupActionCustomConfiguration(self):
        """Custom action parameters, which need to be passed in after JSON serialization. The parameters can be obtained by using the template details query API. If this field is left blank, action parameters in the template are used by default.
        :rtype: str
        """
        return self._TaskGroupActionCustomConfiguration

    @TaskGroupActionCustomConfiguration.setter
    def TaskGroupActionCustomConfiguration(self, TaskGroupActionCustomConfiguration):
        self._TaskGroupActionCustomConfiguration = TaskGroupActionCustomConfiguration


    def _deserialize(self, params):
        self._TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self._TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self._TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupConfig(AbstractModel):
    """Action group configuration item

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstances: Instance object associated with the action group
        :type TaskGroupInstances: list of str
        :param _TaskGroupTitle: Action group name. If this parameter is left blank, the action group name in the template is used by default.
        :type TaskGroupTitle: str
        :param _TaskGroupDescription: Action group description. If this parameter is left blank, the action group description in the template is used by default.
        :type TaskGroupDescription: str
        :param _TaskGroupMode: Action group execution mode. 1: sequential execution; 2: execution by stage. If this parameter is left blank, the action execution mode in the template is used by default.
        :type TaskGroupMode: int
        :param _TaskGroupActionsConfig: Action parameters in the action group. If this field is left blank, the action parameters in the template is used by default. You only need to specify the action whose parameters are to be modified during configuration.
        :type TaskGroupActionsConfig: list of TaskGroupActionConfig
        """
        self._TaskGroupInstances = None
        self._TaskGroupTitle = None
        self._TaskGroupDescription = None
        self._TaskGroupMode = None
        self._TaskGroupActionsConfig = None

    @property
    def TaskGroupInstances(self):
        """Instance object associated with the action group
        :rtype: list of str
        """
        return self._TaskGroupInstances

    @TaskGroupInstances.setter
    def TaskGroupInstances(self, TaskGroupInstances):
        self._TaskGroupInstances = TaskGroupInstances

    @property
    def TaskGroupTitle(self):
        """Action group name. If this parameter is left blank, the action group name in the template is used by default.
        :rtype: str
        """
        return self._TaskGroupTitle

    @TaskGroupTitle.setter
    def TaskGroupTitle(self, TaskGroupTitle):
        self._TaskGroupTitle = TaskGroupTitle

    @property
    def TaskGroupDescription(self):
        """Action group description. If this parameter is left blank, the action group description in the template is used by default.
        :rtype: str
        """
        return self._TaskGroupDescription

    @TaskGroupDescription.setter
    def TaskGroupDescription(self, TaskGroupDescription):
        self._TaskGroupDescription = TaskGroupDescription

    @property
    def TaskGroupMode(self):
        """Action group execution mode. 1: sequential execution; 2: execution by stage. If this parameter is left blank, the action execution mode in the template is used by default.
        :rtype: int
        """
        return self._TaskGroupMode

    @TaskGroupMode.setter
    def TaskGroupMode(self, TaskGroupMode):
        self._TaskGroupMode = TaskGroupMode

    @property
    def TaskGroupActionsConfig(self):
        """Action parameters in the action group. If this field is left blank, the action parameters in the template is used by default. You only need to specify the action whose parameters are to be modified during configuration.
        :rtype: list of TaskGroupActionConfig
        """
        return self._TaskGroupActionsConfig

    @TaskGroupActionsConfig.setter
    def TaskGroupActionsConfig(self, TaskGroupActionsConfig):
        self._TaskGroupActionsConfig = TaskGroupActionsConfig


    def _deserialize(self, params):
        self._TaskGroupInstances = params.get("TaskGroupInstances")
        self._TaskGroupTitle = params.get("TaskGroupTitle")
        self._TaskGroupDescription = params.get("TaskGroupDescription")
        self._TaskGroupMode = params.get("TaskGroupMode")
        if params.get("TaskGroupActionsConfig") is not None:
            self._TaskGroupActionsConfig = []
            for item in params.get("TaskGroupActionsConfig"):
                obj = TaskGroupActionConfig()
                obj._deserialize(item)
                self._TaskGroupActionsConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupInstance(AbstractModel):
    """Task group action instance

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstanceId: Instance ID
        :type TaskGroupInstanceId: int
        :param _TaskGroupInstanceObjectId: Instance ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceObjectId: str
        :param _TaskGroupInstanceStatus: Instance action execution status

        :type TaskGroupInstanceStatus: int
        :param _TaskGroupInstanceCreateTime: Instance creation time
        :type TaskGroupInstanceCreateTime: str
        :param _TaskGroupInstanceUpdateTime: Instance update time
        :type TaskGroupInstanceUpdateTime: str
        :param _TaskGroupInstanceStatusType: Status. 0: no status; 1: successful; 2: failed; 3: terminated; 4: skipped.
        :type TaskGroupInstanceStatusType: int
        :param _TaskGroupInstanceStartTime: Execution start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceStartTime: str
        :param _TaskGroupInstanceEndTime: Execution end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceEndTime: str
        :param _TaskGroupInstanceExecuteLog: Instance action execution log
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceExecuteLog: str
        :param _TaskGroupInstanceIsRedo: Whether the instance can be retried
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceIsRedo: bool
        :param _TaskGroupInstanceExecuteTime: Action instance execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstanceExecuteTime: int
        """
        self._TaskGroupInstanceId = None
        self._TaskGroupInstanceObjectId = None
        self._TaskGroupInstanceStatus = None
        self._TaskGroupInstanceCreateTime = None
        self._TaskGroupInstanceUpdateTime = None
        self._TaskGroupInstanceStatusType = None
        self._TaskGroupInstanceStartTime = None
        self._TaskGroupInstanceEndTime = None
        self._TaskGroupInstanceExecuteLog = None
        self._TaskGroupInstanceIsRedo = None
        self._TaskGroupInstanceExecuteTime = None

    @property
    def TaskGroupInstanceId(self):
        """Instance ID
        :rtype: int
        """
        return self._TaskGroupInstanceId

    @TaskGroupInstanceId.setter
    def TaskGroupInstanceId(self, TaskGroupInstanceId):
        self._TaskGroupInstanceId = TaskGroupInstanceId

    @property
    def TaskGroupInstanceObjectId(self):
        """Instance ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupInstanceObjectId

    @TaskGroupInstanceObjectId.setter
    def TaskGroupInstanceObjectId(self, TaskGroupInstanceObjectId):
        self._TaskGroupInstanceObjectId = TaskGroupInstanceObjectId

    @property
    def TaskGroupInstanceStatus(self):
        """Instance action execution status

        :rtype: int
        """
        return self._TaskGroupInstanceStatus

    @TaskGroupInstanceStatus.setter
    def TaskGroupInstanceStatus(self, TaskGroupInstanceStatus):
        self._TaskGroupInstanceStatus = TaskGroupInstanceStatus

    @property
    def TaskGroupInstanceCreateTime(self):
        """Instance creation time
        :rtype: str
        """
        return self._TaskGroupInstanceCreateTime

    @TaskGroupInstanceCreateTime.setter
    def TaskGroupInstanceCreateTime(self, TaskGroupInstanceCreateTime):
        self._TaskGroupInstanceCreateTime = TaskGroupInstanceCreateTime

    @property
    def TaskGroupInstanceUpdateTime(self):
        """Instance update time
        :rtype: str
        """
        return self._TaskGroupInstanceUpdateTime

    @TaskGroupInstanceUpdateTime.setter
    def TaskGroupInstanceUpdateTime(self, TaskGroupInstanceUpdateTime):
        self._TaskGroupInstanceUpdateTime = TaskGroupInstanceUpdateTime

    @property
    def TaskGroupInstanceStatusType(self):
        """Status. 0: no status; 1: successful; 2: failed; 3: terminated; 4: skipped.
        :rtype: int
        """
        return self._TaskGroupInstanceStatusType

    @TaskGroupInstanceStatusType.setter
    def TaskGroupInstanceStatusType(self, TaskGroupInstanceStatusType):
        self._TaskGroupInstanceStatusType = TaskGroupInstanceStatusType

    @property
    def TaskGroupInstanceStartTime(self):
        """Execution start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupInstanceStartTime

    @TaskGroupInstanceStartTime.setter
    def TaskGroupInstanceStartTime(self, TaskGroupInstanceStartTime):
        self._TaskGroupInstanceStartTime = TaskGroupInstanceStartTime

    @property
    def TaskGroupInstanceEndTime(self):
        """Execution end time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupInstanceEndTime

    @TaskGroupInstanceEndTime.setter
    def TaskGroupInstanceEndTime(self, TaskGroupInstanceEndTime):
        self._TaskGroupInstanceEndTime = TaskGroupInstanceEndTime

    @property
    def TaskGroupInstanceExecuteLog(self):
        warnings.warn("parameter `TaskGroupInstanceExecuteLog` is deprecated", DeprecationWarning) 

        """Instance action execution log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskGroupInstanceExecuteLog

    @TaskGroupInstanceExecuteLog.setter
    def TaskGroupInstanceExecuteLog(self, TaskGroupInstanceExecuteLog):
        warnings.warn("parameter `TaskGroupInstanceExecuteLog` is deprecated", DeprecationWarning) 

        self._TaskGroupInstanceExecuteLog = TaskGroupInstanceExecuteLog

    @property
    def TaskGroupInstanceIsRedo(self):
        """Whether the instance can be retried
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._TaskGroupInstanceIsRedo

    @TaskGroupInstanceIsRedo.setter
    def TaskGroupInstanceIsRedo(self, TaskGroupInstanceIsRedo):
        self._TaskGroupInstanceIsRedo = TaskGroupInstanceIsRedo

    @property
    def TaskGroupInstanceExecuteTime(self):
        """Action instance execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupInstanceExecuteTime

    @TaskGroupInstanceExecuteTime.setter
    def TaskGroupInstanceExecuteTime(self, TaskGroupInstanceExecuteTime):
        self._TaskGroupInstanceExecuteTime = TaskGroupInstanceExecuteTime


    def _deserialize(self, params):
        self._TaskGroupInstanceId = params.get("TaskGroupInstanceId")
        self._TaskGroupInstanceObjectId = params.get("TaskGroupInstanceObjectId")
        self._TaskGroupInstanceStatus = params.get("TaskGroupInstanceStatus")
        self._TaskGroupInstanceCreateTime = params.get("TaskGroupInstanceCreateTime")
        self._TaskGroupInstanceUpdateTime = params.get("TaskGroupInstanceUpdateTime")
        self._TaskGroupInstanceStatusType = params.get("TaskGroupInstanceStatusType")
        self._TaskGroupInstanceStartTime = params.get("TaskGroupInstanceStartTime")
        self._TaskGroupInstanceEndTime = params.get("TaskGroupInstanceEndTime")
        self._TaskGroupInstanceExecuteLog = params.get("TaskGroupInstanceExecuteLog")
        self._TaskGroupInstanceIsRedo = params.get("TaskGroupInstanceIsRedo")
        self._TaskGroupInstanceExecuteTime = params.get("TaskGroupInstanceExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupInstancesExecuteRules(AbstractModel):
    """Machine selection rule

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstancesExecuteMode: Instance selection mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstancesExecuteMode: int
        :param _TaskGroupInstancesExecutePercent: Proportion of selected machines in selection by proportion mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstancesExecutePercent: int
        :param _TaskGroupInstancesExecuteNum: Number of selected machines in selection by quantity mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskGroupInstancesExecuteNum: int
        """
        self._TaskGroupInstancesExecuteMode = None
        self._TaskGroupInstancesExecutePercent = None
        self._TaskGroupInstancesExecuteNum = None

    @property
    def TaskGroupInstancesExecuteMode(self):
        """Instance selection mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupInstancesExecuteMode

    @TaskGroupInstancesExecuteMode.setter
    def TaskGroupInstancesExecuteMode(self, TaskGroupInstancesExecuteMode):
        self._TaskGroupInstancesExecuteMode = TaskGroupInstancesExecuteMode

    @property
    def TaskGroupInstancesExecutePercent(self):
        """Proportion of selected machines in selection by proportion mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupInstancesExecutePercent

    @TaskGroupInstancesExecutePercent.setter
    def TaskGroupInstancesExecutePercent(self, TaskGroupInstancesExecutePercent):
        self._TaskGroupInstancesExecutePercent = TaskGroupInstancesExecutePercent

    @property
    def TaskGroupInstancesExecuteNum(self):
        """Number of selected machines in selection by quantity mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskGroupInstancesExecuteNum

    @TaskGroupInstancesExecuteNum.setter
    def TaskGroupInstancesExecuteNum(self, TaskGroupInstancesExecuteNum):
        self._TaskGroupInstancesExecuteNum = TaskGroupInstancesExecuteNum


    def _deserialize(self, params):
        self._TaskGroupInstancesExecuteMode = params.get("TaskGroupInstancesExecuteMode")
        self._TaskGroupInstancesExecutePercent = params.get("TaskGroupInstancesExecutePercent")
        self._TaskGroupInstancesExecuteNum = params.get("TaskGroupInstancesExecuteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskListItem(AbstractModel):
    """Task list information

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _TaskTitle: Task name
        :type TaskTitle: str
        :param _TaskDescription: Task description
        :type TaskDescription: str
        :param _TaskTag: Task tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskTag: str
        :param _TaskStatus: Task status (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :type TaskStatus: int
        :param _TaskCreateTime: Task creation time
        :type TaskCreateTime: str
        :param _TaskUpdateTime: Task update time
        :type TaskUpdateTime: str
        :param _TaskPreCheckStatus: 0: not started; 1: in progress; 2: completed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPreCheckStatus: int
        :param _TaskPreCheckSuccess: Whether the environmental check is passed
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskPreCheckSuccess: bool
        :param _TaskExpect: Whether the experiment result meets expectations. 1: expectations met; 2: expectations not met.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskExpect: int
        :param _ApplicationId: ID of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _ApplicationName: Name of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _VerifyId: Verification item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VerifyId: int
        :param _TaskStatusType: Status. 0: no status; 1: successful; 2: failed; 3: terminated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskStatusType: int
        """
        self._TaskId = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskCreateTime = None
        self._TaskUpdateTime = None
        self._TaskPreCheckStatus = None
        self._TaskPreCheckSuccess = None
        self._TaskExpect = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._VerifyId = None
        self._TaskStatusType = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTitle(self):
        """Task name
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """Task description
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskTag(self):
        """Task tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """Task status (1001: not started; 1002: in progress; 1003: paused; 1004: ended)
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskCreateTime(self):
        """Task creation time
        :rtype: str
        """
        return self._TaskCreateTime

    @TaskCreateTime.setter
    def TaskCreateTime(self, TaskCreateTime):
        self._TaskCreateTime = TaskCreateTime

    @property
    def TaskUpdateTime(self):
        """Task update time
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def TaskPreCheckStatus(self):
        """0: not started; 1: in progress; 2: completed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskPreCheckStatus

    @TaskPreCheckStatus.setter
    def TaskPreCheckStatus(self, TaskPreCheckStatus):
        self._TaskPreCheckStatus = TaskPreCheckStatus

    @property
    def TaskPreCheckSuccess(self):
        """Whether the environmental check is passed
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._TaskPreCheckSuccess

    @TaskPreCheckSuccess.setter
    def TaskPreCheckSuccess(self, TaskPreCheckSuccess):
        self._TaskPreCheckSuccess = TaskPreCheckSuccess

    @property
    def TaskExpect(self):
        """Whether the experiment result meets expectations. 1: expectations met; 2: expectations not met.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskExpect

    @TaskExpect.setter
    def TaskExpect(self, TaskExpect):
        self._TaskExpect = TaskExpect

    @property
    def ApplicationId(self):
        """ID of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """Name of the associated application
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VerifyId(self):
        """Verification item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VerifyId

    @VerifyId.setter
    def VerifyId(self, VerifyId):
        self._VerifyId = VerifyId

    @property
    def TaskStatusType(self):
        """Status. 0: no status; 1: successful; 2: failed; 3: terminated.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskStatusType

    @TaskStatusType.setter
    def TaskStatusType(self, TaskStatusType):
        self._TaskStatusType = TaskStatusType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskCreateTime = params.get("TaskCreateTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        self._TaskPreCheckStatus = params.get("TaskPreCheckStatus")
        self._TaskPreCheckSuccess = params.get("TaskPreCheckSuccess")
        self._TaskExpect = params.get("TaskExpect")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._VerifyId = params.get("VerifyId")
        self._TaskStatusType = params.get("TaskStatusType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMonitor(AbstractModel):
    """Monitoring metrics

    """

    def __init__(self):
        r"""
        :param _TaskMonitorId: Experiment monitoring metric ID
        :type TaskMonitorId: int
        :param _MetricId: Monitoring metric ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricId: int
        :param _TaskMonitorObjectTypeId: Object type ID of the monitoring metric
        :type TaskMonitorObjectTypeId: int
        :param _MetricName: Metric name
        :type MetricName: str
        :param _InstancesIds: Instance ID list
        :type InstancesIds: list of str
        :param _MetricChineseName: Metric in Chinese
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricChineseName: str
        :param _Unit: Unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        """
        self._TaskMonitorId = None
        self._MetricId = None
        self._TaskMonitorObjectTypeId = None
        self._MetricName = None
        self._InstancesIds = None
        self._MetricChineseName = None
        self._Unit = None

    @property
    def TaskMonitorId(self):
        """Experiment monitoring metric ID
        :rtype: int
        """
        return self._TaskMonitorId

    @TaskMonitorId.setter
    def TaskMonitorId(self, TaskMonitorId):
        self._TaskMonitorId = TaskMonitorId

    @property
    def MetricId(self):
        """Monitoring metric ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def TaskMonitorObjectTypeId(self):
        """Object type ID of the monitoring metric
        :rtype: int
        """
        return self._TaskMonitorObjectTypeId

    @TaskMonitorObjectTypeId.setter
    def TaskMonitorObjectTypeId(self, TaskMonitorObjectTypeId):
        self._TaskMonitorObjectTypeId = TaskMonitorObjectTypeId

    @property
    def MetricName(self):
        """Metric name
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def InstancesIds(self):
        """Instance ID list
        :rtype: list of str
        """
        return self._InstancesIds

    @InstancesIds.setter
    def InstancesIds(self, InstancesIds):
        self._InstancesIds = InstancesIds

    @property
    def MetricChineseName(self):
        """Metric in Chinese
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MetricChineseName

    @MetricChineseName.setter
    def MetricChineseName(self, MetricChineseName):
        self._MetricChineseName = MetricChineseName

    @property
    def Unit(self):
        """Unit
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._TaskMonitorId = params.get("TaskMonitorId")
        self._MetricId = params.get("MetricId")
        self._TaskMonitorObjectTypeId = params.get("TaskMonitorObjectTypeId")
        self._MetricName = params.get("MetricName")
        self._InstancesIds = params.get("InstancesIds")
        self._MetricChineseName = params.get("MetricChineseName")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskReportInfo(AbstractModel):
    """Experiment report status information

    """

    def __init__(self):
        r"""
        :param _Stage: 0: not started; 1: exporting; 2: export successful; 3: export failed.
        :type Stage: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ExpirationTime: End time of the validity period
        :type ExpirationTime: str
        :param _Expired: Whether it is effective
        :type Expired: bool
        :param _CosUrl: Address of the COS experiment report file
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosUrl: str
        :param _Log: Experiment report export log
Note: This field may return null, indicating that no valid values can be obtained.
        :type Log: str
        """
        self._Stage = None
        self._CreateTime = None
        self._ExpirationTime = None
        self._Expired = None
        self._CosUrl = None
        self._Log = None

    @property
    def Stage(self):
        """0: not started; 1: exporting; 2: export successful; 3: export failed.
        :rtype: int
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpirationTime(self):
        """End time of the validity period
        :rtype: str
        """
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Expired(self):
        """Whether it is effective
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def CosUrl(self):
        """Address of the COS experiment report file
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def Log(self):
        """Experiment report export log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log


    def _deserialize(self, params):
        self._Stage = params.get("Stage")
        self._CreateTime = params.get("CreateTime")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Expired = params.get("Expired")
        self._CosUrl = params.get("CosUrl")
        self._Log = params.get("Log")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """Template library

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template library ID
        :type TemplateId: int
        :param _TemplateTitle: Template library name
        :type TemplateTitle: str
        :param _TemplateDescription: Template library description
        :type TemplateDescription: str
        :param _TemplateTag: Custom tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateTag: str
        :param _TemplateIsUsed: Usage status. 1: in use; 2: not in use.
        :type TemplateIsUsed: int
        :param _TemplateCreateTime: Template library creation time
        :type TemplateCreateTime: str
        :param _TemplateUpdateTime: Template library update time
        :type TemplateUpdateTime: str
        :param _TemplateMode: Template library mode. 1: manual execution; 2: automatic execution.
        :type TemplateMode: int
        :param _TemplatePauseDuration: Automatic pause duration. Unit: minutes.
        :type TemplatePauseDuration: int
        :param _TemplateOwnerUin: Main account that creates the experiment
        :type TemplateOwnerUin: str
        :param _TemplateRegionId: Region ID
        :type TemplateRegionId: int
        :param _TemplateGroups: Action group
        :type TemplateGroups: list of TemplateGroup
        :param _TemplateMonitors: Monitoring metrics
        :type TemplateMonitors: list of TemplateMonitor
        :param _TemplatePolicy: Guardrail monitoring
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplatePolicy: :class:`tencentcloud.cfg.v20210820.models.TemplatePolicy`
        :param _Tags: Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagWithDescribe
        :param _TemplateSource: Template library source. 0: self-built; 1: recommended by experts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateSource: int
        :param _ApmServiceList: Application information on Application Performance Monitoring
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmServiceList: list of ApmServiceInfo
        :param _AlarmPolicy: Alarm metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlarmPolicy: list of str
        :param _PolicyDealType: Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyDealType: int
        """
        self._TemplateId = None
        self._TemplateTitle = None
        self._TemplateDescription = None
        self._TemplateTag = None
        self._TemplateIsUsed = None
        self._TemplateCreateTime = None
        self._TemplateUpdateTime = None
        self._TemplateMode = None
        self._TemplatePauseDuration = None
        self._TemplateOwnerUin = None
        self._TemplateRegionId = None
        self._TemplateGroups = None
        self._TemplateMonitors = None
        self._TemplatePolicy = None
        self._Tags = None
        self._TemplateSource = None
        self._ApmServiceList = None
        self._AlarmPolicy = None
        self._PolicyDealType = None

    @property
    def TemplateId(self):
        """Template library ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateTitle(self):
        """Template library name
        :rtype: str
        """
        return self._TemplateTitle

    @TemplateTitle.setter
    def TemplateTitle(self, TemplateTitle):
        self._TemplateTitle = TemplateTitle

    @property
    def TemplateDescription(self):
        """Template library description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateTag(self):
        """Custom tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TemplateTag

    @TemplateTag.setter
    def TemplateTag(self, TemplateTag):
        self._TemplateTag = TemplateTag

    @property
    def TemplateIsUsed(self):
        """Usage status. 1: in use; 2: not in use.
        :rtype: int
        """
        return self._TemplateIsUsed

    @TemplateIsUsed.setter
    def TemplateIsUsed(self, TemplateIsUsed):
        self._TemplateIsUsed = TemplateIsUsed

    @property
    def TemplateCreateTime(self):
        """Template library creation time
        :rtype: str
        """
        return self._TemplateCreateTime

    @TemplateCreateTime.setter
    def TemplateCreateTime(self, TemplateCreateTime):
        self._TemplateCreateTime = TemplateCreateTime

    @property
    def TemplateUpdateTime(self):
        """Template library update time
        :rtype: str
        """
        return self._TemplateUpdateTime

    @TemplateUpdateTime.setter
    def TemplateUpdateTime(self, TemplateUpdateTime):
        self._TemplateUpdateTime = TemplateUpdateTime

    @property
    def TemplateMode(self):
        """Template library mode. 1: manual execution; 2: automatic execution.
        :rtype: int
        """
        return self._TemplateMode

    @TemplateMode.setter
    def TemplateMode(self, TemplateMode):
        self._TemplateMode = TemplateMode

    @property
    def TemplatePauseDuration(self):
        """Automatic pause duration. Unit: minutes.
        :rtype: int
        """
        return self._TemplatePauseDuration

    @TemplatePauseDuration.setter
    def TemplatePauseDuration(self, TemplatePauseDuration):
        self._TemplatePauseDuration = TemplatePauseDuration

    @property
    def TemplateOwnerUin(self):
        """Main account that creates the experiment
        :rtype: str
        """
        return self._TemplateOwnerUin

    @TemplateOwnerUin.setter
    def TemplateOwnerUin(self, TemplateOwnerUin):
        self._TemplateOwnerUin = TemplateOwnerUin

    @property
    def TemplateRegionId(self):
        """Region ID
        :rtype: int
        """
        return self._TemplateRegionId

    @TemplateRegionId.setter
    def TemplateRegionId(self, TemplateRegionId):
        self._TemplateRegionId = TemplateRegionId

    @property
    def TemplateGroups(self):
        """Action group
        :rtype: list of TemplateGroup
        """
        return self._TemplateGroups

    @TemplateGroups.setter
    def TemplateGroups(self, TemplateGroups):
        self._TemplateGroups = TemplateGroups

    @property
    def TemplateMonitors(self):
        """Monitoring metrics
        :rtype: list of TemplateMonitor
        """
        return self._TemplateMonitors

    @TemplateMonitors.setter
    def TemplateMonitors(self, TemplateMonitors):
        self._TemplateMonitors = TemplateMonitors

    @property
    def TemplatePolicy(self):
        """Guardrail monitoring
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TemplatePolicy`
        """
        return self._TemplatePolicy

    @TemplatePolicy.setter
    def TemplatePolicy(self, TemplatePolicy):
        self._TemplatePolicy = TemplatePolicy

    @property
    def Tags(self):
        """Tag list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TemplateSource(self):
        """Template library source. 0: self-built; 1: recommended by experts.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource

    @property
    def ApmServiceList(self):
        """Application information on Application Performance Monitoring
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmServiceInfo
        """
        return self._ApmServiceList

    @ApmServiceList.setter
    def ApmServiceList(self, ApmServiceList):
        self._ApmServiceList = ApmServiceList

    @property
    def AlarmPolicy(self):
        """Alarm metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def PolicyDealType(self):
        """Guardrail processing method. 1: roll back sequentially; 2: pause experiment.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateTitle = params.get("TemplateTitle")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateTag = params.get("TemplateTag")
        self._TemplateIsUsed = params.get("TemplateIsUsed")
        self._TemplateCreateTime = params.get("TemplateCreateTime")
        self._TemplateUpdateTime = params.get("TemplateUpdateTime")
        self._TemplateMode = params.get("TemplateMode")
        self._TemplatePauseDuration = params.get("TemplatePauseDuration")
        self._TemplateOwnerUin = params.get("TemplateOwnerUin")
        self._TemplateRegionId = params.get("TemplateRegionId")
        if params.get("TemplateGroups") is not None:
            self._TemplateGroups = []
            for item in params.get("TemplateGroups"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self._TemplateGroups.append(obj)
        if params.get("TemplateMonitors") is not None:
            self._TemplateMonitors = []
            for item in params.get("TemplateMonitors"):
                obj = TemplateMonitor()
                obj._deserialize(item)
                self._TemplateMonitors.append(obj)
        if params.get("TemplatePolicy") is not None:
            self._TemplatePolicy = TemplatePolicy()
            self._TemplatePolicy._deserialize(params.get("TemplatePolicy"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TemplateSource = params.get("TemplateSource")
        if params.get("ApmServiceList") is not None:
            self._ApmServiceList = []
            for item in params.get("ApmServiceList"):
                obj = ApmServiceInfo()
                obj._deserialize(item)
                self._ApmServiceList.append(obj)
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._PolicyDealType = params.get("PolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """Task group

    """

    def __init__(self):
        r"""
        :param _TemplateGroupId: Template library action ID
        :type TemplateGroupId: int
        :param _TemplateGroupActions: List of actions in the template library action group
        :type TemplateGroupActions: list of TemplateGroupAction
        :param _Title: Group name
        :type Title: str
        :param _Description: Group description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Order: Group order
        :type Order: int
        :param _Mode: Execution mode. 1: sequential execution; 2: execution by stage.
        :type Mode: int
        :param _ObjectTypeId: Object type ID
        :type ObjectTypeId: int
        :param _CreateTime: Group creation time
        :type CreateTime: str
        :param _UpdateTime: Group update time
        :type UpdateTime: str
        """
        self._TemplateGroupId = None
        self._TemplateGroupActions = None
        self._Title = None
        self._Description = None
        self._Order = None
        self._Mode = None
        self._ObjectTypeId = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TemplateGroupId(self):
        """Template library action ID
        :rtype: int
        """
        return self._TemplateGroupId

    @TemplateGroupId.setter
    def TemplateGroupId(self, TemplateGroupId):
        self._TemplateGroupId = TemplateGroupId

    @property
    def TemplateGroupActions(self):
        """List of actions in the template library action group
        :rtype: list of TemplateGroupAction
        """
        return self._TemplateGroupActions

    @TemplateGroupActions.setter
    def TemplateGroupActions(self, TemplateGroupActions):
        self._TemplateGroupActions = TemplateGroupActions

    @property
    def Title(self):
        """Group name
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """Group description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Order(self):
        """Group order
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Mode(self):
        """Execution mode. 1: sequential execution; 2: execution by stage.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ObjectTypeId(self):
        """Object type ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def CreateTime(self):
        """Group creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Group update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TemplateGroupId = params.get("TemplateGroupId")
        if params.get("TemplateGroupActions") is not None:
            self._TemplateGroupActions = []
            for item in params.get("TemplateGroupActions"):
                obj = TemplateGroupAction()
                obj._deserialize(item)
                self._TemplateGroupActions.append(obj)
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._Order = params.get("Order")
        self._Mode = params.get("Mode")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroupAction(AbstractModel):
    """Task group action

    """

    def __init__(self):
        r"""
        :param _TemplateGroupActionId: Template library group action ID
        :type TemplateGroupActionId: int
        :param _ActionId: Action ID
        :type ActionId: int
        :param _Order: Order of actions in the group
        :type Order: int
        :param _GeneralConfiguration: General configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :type GeneralConfiguration: str
        :param _CustomConfiguration: Custom configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :type CustomConfiguration: str
        :param _CreateTime: Action group creation time
        :type CreateTime: str
        :param _UpdateTime: Action group update time
        :type UpdateTime: str
        :param _ActionTitle: Action name
        :type ActionTitle: str
        :param _RandomId: Random ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RandomId: int
        :param _RecoverId: Recovery action ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecoverId: int
        :param _ExecuteId: Executed action ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecuteId: int
        :param _ActionApiType: Called API type. 0: tat; 1: cloud API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionApiType: int
        :param _ActionAttribute: 1: fault; 2: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionAttribute: int
        :param _ActionType: Action type: platform and custom
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionType: str
        :param _ActionRisk: Action risk level. 1: low-risk; 2: medium-risk; 3: high-risk.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActionRisk: str
        """
        self._TemplateGroupActionId = None
        self._ActionId = None
        self._Order = None
        self._GeneralConfiguration = None
        self._CustomConfiguration = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ActionTitle = None
        self._RandomId = None
        self._RecoverId = None
        self._ExecuteId = None
        self._ActionApiType = None
        self._ActionAttribute = None
        self._ActionType = None
        self._ActionRisk = None

    @property
    def TemplateGroupActionId(self):
        """Template library group action ID
        :rtype: int
        """
        return self._TemplateGroupActionId

    @TemplateGroupActionId.setter
    def TemplateGroupActionId(self, TemplateGroupActionId):
        self._TemplateGroupActionId = TemplateGroupActionId

    @property
    def ActionId(self):
        """Action ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def Order(self):
        """Order of actions in the group
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def GeneralConfiguration(self):
        """General configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GeneralConfiguration

    @GeneralConfiguration.setter
    def GeneralConfiguration(self, GeneralConfiguration):
        self._GeneralConfiguration = GeneralConfiguration

    @property
    def CustomConfiguration(self):
        """Custom configurations of actions in the group
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def CreateTime(self):
        """Action group creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Action group update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ActionTitle(self):
        """Action name
        :rtype: str
        """
        return self._ActionTitle

    @ActionTitle.setter
    def ActionTitle(self, ActionTitle):
        self._ActionTitle = ActionTitle

    @property
    def RandomId(self):
        """Random ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RandomId

    @RandomId.setter
    def RandomId(self, RandomId):
        self._RandomId = RandomId

    @property
    def RecoverId(self):
        """Recovery action ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RecoverId

    @RecoverId.setter
    def RecoverId(self, RecoverId):
        self._RecoverId = RecoverId

    @property
    def ExecuteId(self):
        """Executed action ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ExecuteId

    @ExecuteId.setter
    def ExecuteId(self, ExecuteId):
        self._ExecuteId = ExecuteId

    @property
    def ActionApiType(self):
        """Called API type. 0: tat; 1: cloud API.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ActionApiType

    @ActionApiType.setter
    def ActionApiType(self, ActionApiType):
        self._ActionApiType = ActionApiType

    @property
    def ActionAttribute(self):
        """1: fault; 2: recovery.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ActionAttribute

    @ActionAttribute.setter
    def ActionAttribute(self, ActionAttribute):
        self._ActionAttribute = ActionAttribute

    @property
    def ActionType(self):
        """Action type: platform and custom
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionRisk(self):
        """Action risk level. 1: low-risk; 2: medium-risk; 3: high-risk.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ActionRisk

    @ActionRisk.setter
    def ActionRisk(self, ActionRisk):
        self._ActionRisk = ActionRisk


    def _deserialize(self, params):
        self._TemplateGroupActionId = params.get("TemplateGroupActionId")
        self._ActionId = params.get("ActionId")
        self._Order = params.get("Order")
        self._GeneralConfiguration = params.get("GeneralConfiguration")
        self._CustomConfiguration = params.get("CustomConfiguration")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ActionTitle = params.get("ActionTitle")
        self._RandomId = params.get("RandomId")
        self._RecoverId = params.get("RecoverId")
        self._ExecuteId = params.get("ExecuteId")
        self._ActionApiType = params.get("ActionApiType")
        self._ActionAttribute = params.get("ActionAttribute")
        self._ActionType = params.get("ActionType")
        self._ActionRisk = params.get("ActionRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateListItem(AbstractModel):
    """Template library list information

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template library ID
        :type TemplateId: int
        :param _TemplateTitle: Template library name
        :type TemplateTitle: str
        :param _TemplateDescription: Template library description
        :type TemplateDescription: str
        :param _TemplateTag: Template library tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateTag: str
        :param _TemplateIsUsed: Template library status. 1: in use; 2: not in use.
        :type TemplateIsUsed: int
        :param _TemplateCreateTime: Template library creation time
        :type TemplateCreateTime: str
        :param _TemplateUpdateTime: Template library update time
        :type TemplateUpdateTime: str
        :param _TemplateUsedNum: Number of tasks associated with the template library
        :type TemplateUsedNum: int
        :param _TemplateSource: Template library source. 0: self-built; 1: recommended by experts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateSource: int
        """
        self._TemplateId = None
        self._TemplateTitle = None
        self._TemplateDescription = None
        self._TemplateTag = None
        self._TemplateIsUsed = None
        self._TemplateCreateTime = None
        self._TemplateUpdateTime = None
        self._TemplateUsedNum = None
        self._TemplateSource = None

    @property
    def TemplateId(self):
        """Template library ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateTitle(self):
        """Template library name
        :rtype: str
        """
        return self._TemplateTitle

    @TemplateTitle.setter
    def TemplateTitle(self, TemplateTitle):
        self._TemplateTitle = TemplateTitle

    @property
    def TemplateDescription(self):
        """Template library description
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateTag(self):
        """Template library tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TemplateTag

    @TemplateTag.setter
    def TemplateTag(self, TemplateTag):
        self._TemplateTag = TemplateTag

    @property
    def TemplateIsUsed(self):
        """Template library status. 1: in use; 2: not in use.
        :rtype: int
        """
        return self._TemplateIsUsed

    @TemplateIsUsed.setter
    def TemplateIsUsed(self, TemplateIsUsed):
        self._TemplateIsUsed = TemplateIsUsed

    @property
    def TemplateCreateTime(self):
        """Template library creation time
        :rtype: str
        """
        return self._TemplateCreateTime

    @TemplateCreateTime.setter
    def TemplateCreateTime(self, TemplateCreateTime):
        self._TemplateCreateTime = TemplateCreateTime

    @property
    def TemplateUpdateTime(self):
        """Template library update time
        :rtype: str
        """
        return self._TemplateUpdateTime

    @TemplateUpdateTime.setter
    def TemplateUpdateTime(self, TemplateUpdateTime):
        self._TemplateUpdateTime = TemplateUpdateTime

    @property
    def TemplateUsedNum(self):
        """Number of tasks associated with the template library
        :rtype: int
        """
        return self._TemplateUsedNum

    @TemplateUsedNum.setter
    def TemplateUsedNum(self, TemplateUsedNum):
        self._TemplateUsedNum = TemplateUsedNum

    @property
    def TemplateSource(self):
        """Template library source. 0: self-built; 1: recommended by experts.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateTitle = params.get("TemplateTitle")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateTag = params.get("TemplateTag")
        self._TemplateIsUsed = params.get("TemplateIsUsed")
        self._TemplateCreateTime = params.get("TemplateCreateTime")
        self._TemplateUpdateTime = params.get("TemplateUpdateTime")
        self._TemplateUsedNum = params.get("TemplateUsedNum")
        self._TemplateSource = params.get("TemplateSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateMonitor(AbstractModel):
    """Monitoring metrics

    """

    def __init__(self):
        r"""
        :param _MonitorId: pk
        :type MonitorId: int
        :param _MetricId: Monitoring metric ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricId: int
        :param _ObjectTypeId: Object type ID of the monitoring metric
        :type ObjectTypeId: int
        :param _MetricName: Metric name
        :type MetricName: str
        :param _MetricChineseName: Metric in Chinese
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricChineseName: str
        """
        self._MonitorId = None
        self._MetricId = None
        self._ObjectTypeId = None
        self._MetricName = None
        self._MetricChineseName = None

    @property
    def MonitorId(self):
        """pk
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MetricId(self):
        """Monitoring metric ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def ObjectTypeId(self):
        """Object type ID of the monitoring metric
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def MetricName(self):
        """Metric name
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricChineseName(self):
        """Metric in Chinese
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MetricChineseName

    @MetricChineseName.setter
    def MetricChineseName(self, MetricChineseName):
        self._MetricChineseName = MetricChineseName


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MetricId = params.get("MetricId")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._MetricName = params.get("MetricName")
        self._MetricChineseName = params.get("MetricChineseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatePolicy(AbstractModel):
    """Protection policy

    """

    def __init__(self):
        r"""
        :param _TemplatePolicyIdList: Protection policy ID list
        :type TemplatePolicyIdList: list of str
        :param _TemplatePolicyRule: Policy rules
        :type TemplatePolicyRule: str
        :param _TemplatePolicyDealType: Process method when the guardrail policy takes effect. 1: sequential execution, 2: pausing.
        :type TemplatePolicyDealType: int
        """
        self._TemplatePolicyIdList = None
        self._TemplatePolicyRule = None
        self._TemplatePolicyDealType = None

    @property
    def TemplatePolicyIdList(self):
        """Protection policy ID list
        :rtype: list of str
        """
        return self._TemplatePolicyIdList

    @TemplatePolicyIdList.setter
    def TemplatePolicyIdList(self, TemplatePolicyIdList):
        self._TemplatePolicyIdList = TemplatePolicyIdList

    @property
    def TemplatePolicyRule(self):
        """Policy rules
        :rtype: str
        """
        return self._TemplatePolicyRule

    @TemplatePolicyRule.setter
    def TemplatePolicyRule(self, TemplatePolicyRule):
        self._TemplatePolicyRule = TemplatePolicyRule

    @property
    def TemplatePolicyDealType(self):
        """Process method when the guardrail policy takes effect. 1: sequential execution, 2: pausing.
        :rtype: int
        """
        return self._TemplatePolicyDealType

    @TemplatePolicyDealType.setter
    def TemplatePolicyDealType(self, TemplatePolicyDealType):
        self._TemplatePolicyDealType = TemplatePolicyDealType


    def _deserialize(self, params):
        self._TemplatePolicyIdList = params.get("TemplatePolicyIdList")
        self._TemplatePolicyRule = params.get("TemplatePolicyRule")
        self._TemplatePolicyDealType = params.get("TemplatePolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerPolicyRequest(AbstractModel):
    """TriggerPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Chaos engineering experiment ID
        :type TaskId: int
        :param _Name: Name
        :type Name: str
        :param _Content: Triggering content
        :type Content: str
        :param _TriggerType: Triggering type. 0: trigger; 1: recovery.
        :type TriggerType: int
        """
        self._TaskId = None
        self._Name = None
        self._Content = None
        self._TriggerType = None

    @property
    def TaskId(self):
        """Chaos engineering experiment ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """Triggering content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def TriggerType(self):
        """Triggering type. 0: trigger; 1: recovery.
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._TriggerType = params.get("TriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerPolicyResponse(AbstractModel):
    """TriggerPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Experiment ID
        :type TaskId: int
        :param _Success: Whether triggering is successful
        :type Success: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Success = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Experiment ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Success(self):
        """Whether triggering is successful
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

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
        self._Success = params.get("Success")
        self._RequestId = params.get("RequestId")