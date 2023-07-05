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


class APIGWParams(AbstractModel):
    """`APIGWParams` description

    """

    def __init__(self):
        r"""
        :param _Protocol: HTTPS
        :type Protocol: str
        :param _Method: POST
        :type Method: str
        """
        self._Protocol = None
        self._Method = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRuleRequest(AbstractModel):
    """CheckRule request structure.

    """


class CheckRuleResponse(AbstractModel):
    """CheckRule response structure.

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


class CheckTransformationRequest(AbstractModel):
    """CheckTransformation request structure.

    """

    def __init__(self):
        r"""
        :param _Input: JSON string to be processed
        :type Input: str
        :param _Transformations: Transformation rule list
        :type Transformations: list of Transformation
        """
        self._Input = None
        self._Transformations = None

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._Input = params.get("Input")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTransformationResponse(AbstractModel):
    """CheckTransformation response structure.

    """

    def __init__(self):
        r"""
        :param _Output: Data processed by `Transformations`
        :type Output: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Output = None
        self._RequestId = None

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Output = params.get("Output")
        self._RequestId = params.get("RequestId")


class CkafkaDeliveryParams(AbstractModel):
    """Parameter of the Kafka topic to be delivered to

    """

    def __init__(self):
        r"""
        :param _TopicName: ckafka topic name
        :type TopicName: str
        :param _ResourceDescription: Six-Segment QCS description of CKafka resource
        :type ResourceDescription: str
        """
        self._TopicName = None
        self._ResourceDescription = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._ResourceDescription = params.get("ResourceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaParams(AbstractModel):
    """CKafka connector parameter

    """

    def __init__(self):
        r"""
        :param _Offset: kafka offset
        :type Offset: str
        :param _TopicName: ckafka  topic
        :type TopicName: str
        """
        self._Offset = None
        self._TopicName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaTargetParams(AbstractModel):
    """CKafka delivery target description

    """

    def __init__(self):
        r"""
        :param _TopicName: CKafka topic to be delivered to
        :type TopicName: str
        :param _RetryPolicy: Retry policy
        :type RetryPolicy: :class:`tencentcloud.eb.v20210416.models.RetryPolicy`
        """
        self._TopicName = None
        self._RetryPolicy = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        if params.get("RetryPolicy") is not None:
            self._RetryPolicy = RetryPolicy()
            self._RetryPolicy._deserialize(params.get("RetryPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Connection(AbstractModel):
    """Connection information

    """

    def __init__(self):
        r"""
        :param _Status: Status
        :type Status: str
        :param _ModTime: Update time
        :type ModTime: str
        :param _Enable: Switch
        :type Enable: bool
        :param _Description: Description
        :type Description: str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _ConnectionId: Connector ID
        :type ConnectionId: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _ConnectionDescription: Connector description
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param _ConnectionName: Connector name
        :type ConnectionName: str
        :param _Type: Type
        :type Type: str
        """
        self._Status = None
        self._ModTime = None
        self._Enable = None
        self._Description = None
        self._AddTime = None
        self._ConnectionId = None
        self._EventBusId = None
        self._ConnectionDescription = None
        self._ConnectionName = None
        self._Type = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ConnectionDescription(self):
        return self._ConnectionDescription

    @ConnectionDescription.setter
    def ConnectionDescription(self, ConnectionDescription):
        self._ConnectionDescription = ConnectionDescription

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ModTime = params.get("ModTime")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        if params.get("ConnectionDescription") is not None:
            self._ConnectionDescription = ConnectionDescription()
            self._ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self._ConnectionName = params.get("ConnectionName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionBrief(AbstractModel):
    """Connector basic information

    """

    def __init__(self):
        r"""
        :param _Type: Connector type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param _Status: Connector status
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._Type = None
        self._Status = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionDescription(AbstractModel):
    """Connection description

    """

    def __init__(self):
        r"""
        :param _ResourceDescription: Six-Segment QCS resource description. For more information, see [Resource Description Method](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type ResourceDescription: str
        :param _APIGWParams: API Gateway parameters
Note: this field may return null, indicating that no valid values can be obtained.
        :type APIGWParams: :class:`tencentcloud.eb.v20210416.models.APIGWParams`
        :param _CkafkaParams: CKafka parameters
Note: this field may return null, indicating that no valid values can be obtained.
        :type CkafkaParams: :class:`tencentcloud.eb.v20210416.models.CkafkaParams`
        :param _DTSParams: Data Transfer Service (DTS) connector information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DTSParams: :class:`tencentcloud.eb.v20210416.models.DTSParams`
        """
        self._ResourceDescription = None
        self._APIGWParams = None
        self._CkafkaParams = None
        self._DTSParams = None

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription

    @property
    def APIGWParams(self):
        return self._APIGWParams

    @APIGWParams.setter
    def APIGWParams(self, APIGWParams):
        self._APIGWParams = APIGWParams

    @property
    def CkafkaParams(self):
        return self._CkafkaParams

    @CkafkaParams.setter
    def CkafkaParams(self, CkafkaParams):
        self._CkafkaParams = CkafkaParams

    @property
    def DTSParams(self):
        return self._DTSParams

    @DTSParams.setter
    def DTSParams(self, DTSParams):
        self._DTSParams = DTSParams


    def _deserialize(self, params):
        self._ResourceDescription = params.get("ResourceDescription")
        if params.get("APIGWParams") is not None:
            self._APIGWParams = APIGWParams()
            self._APIGWParams._deserialize(params.get("APIGWParams"))
        if params.get("CkafkaParams") is not None:
            self._CkafkaParams = CkafkaParams()
            self._CkafkaParams._deserialize(params.get("CkafkaParams"))
        if params.get("DTSParams") is not None:
            self._DTSParams = DTSParams()
            self._DTSParams._deserialize(params.get("DTSParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionRequest(AbstractModel):
    """CreateConnection request structure.

    """

    def __init__(self):
        r"""
        :param _ConnectionDescription: Connector description
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _ConnectionName: Connector name
        :type ConnectionName: str
        :param _Description: Description
        :type Description: str
        :param _Enable: Whether to enable
        :type Enable: bool
        :param _Type: Type of the connector
        :type Type: str
        """
        self._ConnectionDescription = None
        self._EventBusId = None
        self._ConnectionName = None
        self._Description = None
        self._Enable = None
        self._Type = None

    @property
    def ConnectionDescription(self):
        return self._ConnectionDescription

    @ConnectionDescription.setter
    def ConnectionDescription(self, ConnectionDescription):
        self._ConnectionDescription = ConnectionDescription

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("ConnectionDescription") is not None:
            self._ConnectionDescription = ConnectionDescription()
            self._ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self._EventBusId = params.get("EventBusId")
        self._ConnectionName = params.get("ConnectionName")
        self._Description = params.get("Description")
        self._Enable = params.get("Enable")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionResponse(AbstractModel):
    """CreateConnection response structure.

    """

    def __init__(self):
        r"""
        :param _ConnectionId: Connector ID
        :type ConnectionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConnectionId = None
        self._RequestId = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._RequestId = params.get("RequestId")


class CreateEventBusRequest(AbstractModel):
    """CreateEventBus request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusName: Event bus name: it can contain 2-60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter.
        :type EventBusName: str
        :param _Description: Event bus description, which can contain up to 200 characters of any type.
        :type Description: str
        :param _SaveDays: Log retention period
        :type SaveDays: int
        :param _EnableStore: Whether to enable log storage
        :type EnableStore: bool
        """
        self._EventBusName = None
        self._Description = None
        self._SaveDays = None
        self._EnableStore = None

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore


    def _deserialize(self, params):
        self._EventBusName = params.get("EventBusName")
        self._Description = params.get("Description")
        self._SaveDays = params.get("SaveDays")
        self._EnableStore = params.get("EnableStore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEventBusResponse(AbstractModel):
    """CreateEventBus response structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EventBusId = None
        self._RequestId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param _EventPattern: See [Event Pattern](https://intl.cloud.tencent.com/document/product/1359/56084?from_cn_redirect=1)
        :type EventPattern: str
        :param _EventBusId: Event bus ID.
        :type EventBusId: str
        :param _RuleName: Event bus name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type RuleName: str
        :param _Enable: Switch.
        :type Enable: bool
        :param _Description: Event bus description, which can contain up to 200 characters of any type
        :type Description: str
        """
        self._EventPattern = None
        self._EventBusId = None
        self._RuleName = None
        self._Enable = None
        self._Description = None

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EventPattern = params.get("EventPattern")
        self._EventBusId = params.get("EventBusId")
        self._RuleName = params.get("RuleName")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateTargetRequest(AbstractModel):
    """CreateTarget request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Type: Target type
        :type Type: str
        :param _TargetDescription: Target description
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param _RuleId: Event rule ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._Type = None
        self._TargetDescription = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TargetDescription(self):
        return self._TargetDescription

    @TargetDescription.setter
    def TargetDescription(self, TargetDescription):
        self._TargetDescription = TargetDescription

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        if params.get("TargetDescription") is not None:
            self._TargetDescription = TargetDescription()
            self._TargetDescription._deserialize(params.get("TargetDescription"))
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetResponse(AbstractModel):
    """CreateTarget response structure.

    """

    def __init__(self):
        r"""
        :param _TargetId: Target ID
        :type TargetId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetId = None
        self._RequestId = None

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._RequestId = params.get("RequestId")


class CreateTransformationRequest(AbstractModel):
    """CreateTransformation request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _Transformations: Transformation rule list (currently, only one is supported)
        :type Transformations: list of Transformation
        """
        self._EventBusId = None
        self._RuleId = None
        self._Transformations = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransformationResponse(AbstractModel):
    """CreateTransformation response structure.

    """

    def __init__(self):
        r"""
        :param _TransformationId: Generated transformer ID
        :type TransformationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TransformationId = None
        self._RequestId = None

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TransformationId = params.get("TransformationId")
        self._RequestId = params.get("RequestId")


class DTSParams(AbstractModel):
    """Data Transfer Service (DTS) connector information

    """


class DeadLetterConfig(AbstractModel):
    """DLQ configuration of rule

    """

    def __init__(self):
        r"""
        :param _DisposeMethod: Three modes are supported: DLQ, drop, and ignore error, which correspond to `DLQ`, `DROP`, and `IGNORE_ERROR` respectively
        :type DisposeMethod: str
        :param _CkafkaDeliveryParams: If the DLQ mode is set, this option is required. Error messages will be delivered to the corresponding Kafka topic
Note: this field may return null, indicating that no valid values can be obtained.
        :type CkafkaDeliveryParams: :class:`tencentcloud.eb.v20210416.models.CkafkaDeliveryParams`
        """
        self._DisposeMethod = None
        self._CkafkaDeliveryParams = None

    @property
    def DisposeMethod(self):
        return self._DisposeMethod

    @DisposeMethod.setter
    def DisposeMethod(self, DisposeMethod):
        self._DisposeMethod = DisposeMethod

    @property
    def CkafkaDeliveryParams(self):
        return self._CkafkaDeliveryParams

    @CkafkaDeliveryParams.setter
    def CkafkaDeliveryParams(self, CkafkaDeliveryParams):
        self._CkafkaDeliveryParams = CkafkaDeliveryParams


    def _deserialize(self, params):
        self._DisposeMethod = params.get("DisposeMethod")
        if params.get("CkafkaDeliveryParams") is not None:
            self._CkafkaDeliveryParams = CkafkaDeliveryParams()
            self._CkafkaDeliveryParams._deserialize(params.get("CkafkaDeliveryParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionRequest(AbstractModel):
    """DeleteConnection request structure.

    """

    def __init__(self):
        r"""
        :param _ConnectionId: Connector ID
        :type ConnectionId: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        """
        self._ConnectionId = None
        self._EventBusId = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionResponse(AbstractModel):
    """DeleteConnection response structure.

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


class DeleteEventBusRequest(AbstractModel):
    """DeleteEventBus request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        """
        self._EventBusId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEventBusResponse(AbstractModel):
    """DeleteEventBus response structure.

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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Event rule ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

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


class DeleteTargetRequest(AbstractModel):
    """DeleteTarget request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _TargetId: Delivery target ID
        :type TargetId: str
        :param _RuleId: Event rule ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._TargetId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._TargetId = params.get("TargetId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetResponse(AbstractModel):
    """DeleteTarget response structure.

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


class DeleteTransformationRequest(AbstractModel):
    """DeleteTransformation request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _TransformationId: Transformer ID
        :type TransformationId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTransformationResponse(AbstractModel):
    """DeleteTransformation response structure.

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


class ESTargetParams(AbstractModel):
    """ES rule targets

    """

    def __init__(self):
        r"""
        :param _NetMode: Network connection type
        :type NetMode: str
        :param _IndexPrefix: Index prefix
        :type IndexPrefix: str
        :param _RotationInterval: ES log rotation interval
        :type RotationInterval: str
        :param _OutputMode: DTS event configuration
        :type OutputMode: str
        :param _IndexSuffixMode: DTS indexing configuration
        :type IndexSuffixMode: str
        :param _IndexTemplateType: ES template type
        :type IndexTemplateType: str
        """
        self._NetMode = None
        self._IndexPrefix = None
        self._RotationInterval = None
        self._OutputMode = None
        self._IndexSuffixMode = None
        self._IndexTemplateType = None

    @property
    def NetMode(self):
        return self._NetMode

    @NetMode.setter
    def NetMode(self, NetMode):
        self._NetMode = NetMode

    @property
    def IndexPrefix(self):
        return self._IndexPrefix

    @IndexPrefix.setter
    def IndexPrefix(self, IndexPrefix):
        self._IndexPrefix = IndexPrefix

    @property
    def RotationInterval(self):
        return self._RotationInterval

    @RotationInterval.setter
    def RotationInterval(self, RotationInterval):
        self._RotationInterval = RotationInterval

    @property
    def OutputMode(self):
        return self._OutputMode

    @OutputMode.setter
    def OutputMode(self, OutputMode):
        self._OutputMode = OutputMode

    @property
    def IndexSuffixMode(self):
        return self._IndexSuffixMode

    @IndexSuffixMode.setter
    def IndexSuffixMode(self, IndexSuffixMode):
        self._IndexSuffixMode = IndexSuffixMode

    @property
    def IndexTemplateType(self):
        return self._IndexTemplateType

    @IndexTemplateType.setter
    def IndexTemplateType(self, IndexTemplateType):
        self._IndexTemplateType = IndexTemplateType


    def _deserialize(self, params):
        self._NetMode = params.get("NetMode")
        self._IndexPrefix = params.get("IndexPrefix")
        self._RotationInterval = params.get("RotationInterval")
        self._OutputMode = params.get("OutputMode")
        self._IndexSuffixMode = params.get("IndexSuffixMode")
        self._IndexTemplateType = params.get("IndexTemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtlFilter(AbstractModel):
    """Describes how to filter data

    """

    def __init__(self):
        r"""
        :param _Filter: The syntax is the same as that of `Rule`
        :type Filter: str
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventBus(AbstractModel):
    """Event bus information

    """

    def __init__(self):
        r"""
        :param _ModTime: Update time
        :type ModTime: str
        :param _Description: Event bus description, which can contain up to 200 characters of any type
        :type Description: str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _EventBusName: Event bus name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type EventBusName: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Type: Event bus type
        :type Type: str
        :param _PayMode: Billing Mode
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _ConnectionBriefs: Connector basic information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ConnectionBriefs: list of ConnectionBrief
        :param _TargetBriefs: Target information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetBriefs: list of TargetBrief
        """
        self._ModTime = None
        self._Description = None
        self._AddTime = None
        self._EventBusName = None
        self._EventBusId = None
        self._Type = None
        self._PayMode = None
        self._ConnectionBriefs = None
        self._TargetBriefs = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ConnectionBriefs(self):
        return self._ConnectionBriefs

    @ConnectionBriefs.setter
    def ConnectionBriefs(self, ConnectionBriefs):
        self._ConnectionBriefs = ConnectionBriefs

    @property
    def TargetBriefs(self):
        return self._TargetBriefs

    @TargetBriefs.setter
    def TargetBriefs(self, TargetBriefs):
        self._TargetBriefs = TargetBriefs


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._EventBusName = params.get("EventBusName")
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        self._PayMode = params.get("PayMode")
        if params.get("ConnectionBriefs") is not None:
            self._ConnectionBriefs = []
            for item in params.get("ConnectionBriefs"):
                obj = ConnectionBrief()
                obj._deserialize(item)
                self._ConnectionBriefs.append(obj)
        if params.get("TargetBriefs") is not None:
            self._TargetBriefs = []
            for item in params.get("TargetBriefs"):
                obj = TargetBrief()
                obj._deserialize(item)
                self._TargetBriefs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Extraction(AbstractModel):
    """Describes how to extract data

    """

    def __init__(self):
        r"""
        :param _ExtractionInputPath: JsonPath, which will be `$.` by default if not specified
        :type ExtractionInputPath: str
        :param _Format: Valid values: TEXT/JSON
        :type Format: str
        :param _TextParams: Only required for `Text`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TextParams: :class:`tencentcloud.eb.v20210416.models.TextParams`
        """
        self._ExtractionInputPath = None
        self._Format = None
        self._TextParams = None

    @property
    def ExtractionInputPath(self):
        return self._ExtractionInputPath

    @ExtractionInputPath.setter
    def ExtractionInputPath(self, ExtractionInputPath):
        self._ExtractionInputPath = ExtractionInputPath

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TextParams(self):
        return self._TextParams

    @TextParams.setter
    def TextParams(self, TextParams):
        self._TextParams = TextParams


    def _deserialize(self, params):
        self._ExtractionInputPath = params.get("ExtractionInputPath")
        self._Format = params.get("Format")
        if params.get("TextParams") is not None:
            self._TextParams = TextParams()
            self._TextParams._deserialize(params.get("TextParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries, such as filtering ID, name, and status
    * If more than one filter exists, the logical relationship between these filters is `AND`.
    * If multiple values exist in one filter, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param _Values: One or more filter values.
        :type Values: list of str
        :param _Name: Filter name.
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusRequest(AbstractModel):
    """GetEventBus request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        """
        self._EventBusId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusResponse(AbstractModel):
    """GetEventBus response structure.

    """

    def __init__(self):
        r"""
        :param _ModTime: Update time
        :type ModTime: str
        :param _Description: Event bus description
        :type Description: str
        :param _ClsTopicId: Log topic ID
        :type ClsTopicId: str
        :param _AddTime: Creation time.
        :type AddTime: str
        :param _ClsLogsetId: Logset ID
        :type ClsLogsetId: str
        :param _EventBusName: Event bus name
        :type EventBusName: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Type: (Disused) Event bus type
        :type Type: str
        :param _PayMode: Billing mode
        :type PayMode: str
        :param _SaveDays: EventBridge log storage period
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SaveDays: int
        :param _LogTopicId: EventBridge log topic ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogTopicId: str
        :param _EnableStore: Whether to enable log storage
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableStore: bool
        :param _LinkMode: Whether to sort the message
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LinkMode: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ModTime = None
        self._Description = None
        self._ClsTopicId = None
        self._AddTime = None
        self._ClsLogsetId = None
        self._EventBusName = None
        self._EventBusId = None
        self._Type = None
        self._PayMode = None
        self._SaveDays = None
        self._LogTopicId = None
        self._EnableStore = None
        self._LinkMode = None
        self._RequestId = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore

    @property
    def LinkMode(self):
        return self._LinkMode

    @LinkMode.setter
    def LinkMode(self, LinkMode):
        self._LinkMode = LinkMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Description = params.get("Description")
        self._ClsTopicId = params.get("ClsTopicId")
        self._AddTime = params.get("AddTime")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._EventBusName = params.get("EventBusName")
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        self._PayMode = params.get("PayMode")
        self._SaveDays = params.get("SaveDays")
        self._LogTopicId = params.get("LogTopicId")
        self._EnableStore = params.get("EnableStore")
        self._LinkMode = params.get("LinkMode")
        self._RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    """GetRule request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Event rule ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    """GetRule response structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _RuleName: Event rule name
        :type RuleName: str
        :param _Status: Event rule status
        :type Status: str
        :param _Enable: Switch
        :type Enable: bool
        :param _Description: Event rule description
        :type Description: str
        :param _EventPattern: Event pattern
        :type EventPattern: str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _ModTime: Update time
        :type ModTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Enable = None
        self._Description = None
        self._EventPattern = None
        self._AddTime = None
        self._ModTime = None
        self._RequestId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._EventPattern = params.get("EventPattern")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._RequestId = params.get("RequestId")


class GetTransformationRequest(AbstractModel):
    """GetTransformation request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _TransformationId: Transformer ID
        :type TransformationId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTransformationResponse(AbstractModel):
    """GetTransformation response structure.

    """

    def __init__(self):
        r"""
        :param _Transformations: Transformation rule list
        :type Transformations: list of Transformation
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Transformations = None
        self._RequestId = None

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        self._RequestId = params.get("RequestId")


class ListConnectionsRequest(AbstractModel):
    """ListConnections request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime, ModTime
        :type OrderBy: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC, DESC
        :type Order: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._EventBusId = None
        self._OrderBy = None
        self._Limit = None
        self._Order = None
        self._Offset = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConnectionsResponse(AbstractModel):
    """ListConnections response structure.

    """

    def __init__(self):
        r"""
        :param _Connections: Connector information
        :type Connections: list of Connection
        :param _TotalCount: Total number of connectors
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Connections = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Connections(self):
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Connections") is not None:
            self._Connections = []
            for item in params.get("Connections"):
                obj = Connection()
                obj._deserialize(item)
                self._Connections.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListEventBusesRequest(AbstractModel):
    """ListEventBuses request structure.

    """

    def __init__(self):
        r"""
        :param _OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        :param _Filters: Filter. For more information, see the Instance Filter Table below. Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        """
        self._OrderBy = None
        self._Limit = None
        self._Order = None
        self._Filters = None
        self._Offset = None

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventBusesResponse(AbstractModel):
    """ListEventBuses response structure.

    """

    def __init__(self):
        r"""
        :param _EventBuses: Event bus information
        :type EventBuses: list of EventBus
        :param _TotalCount: Total number of event buses
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EventBuses = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EventBuses(self):
        return self._EventBuses

    @EventBuses.setter
    def EventBuses(self, EventBuses):
        self._EventBuses = EventBuses

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventBuses") is not None:
            self._EventBuses = []
            for item in params.get("EventBuses"):
                obj = EventBus()
                obj._deserialize(item)
                self._EventBuses.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListRulesRequest(AbstractModel):
    """ListRules request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param _Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        """
        self._EventBusId = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._Order = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRulesResponse(AbstractModel):
    """ListRules response structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Event rule information
        :type Rules: list of Rule
        :param _TotalCount: Total number of event rules
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListTargetsRequest(AbstractModel):
    """ListTargets request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param _Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        """
        self._RuleId = None
        self._EventBusId = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._Order = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsResponse(AbstractModel):
    """ListTargets response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of targets
        :type TotalCount: int
        :param _Targets: Target information
        :type Targets: list of Target
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Targets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class OutputStructParam(AbstractModel):
    """`Transform` output parameter

    """

    def __init__(self):
        r"""
        :param _Key: Key in the corresponding JSON output
        :type Key: str
        :param _Value: You can enter a JsonPath, constant, or built-in date type
        :type Value: str
        :param _ValueType: Data type of `Value`. Valid values: STRING, NUMBER, BOOLEAN, NULL, SYS_VARIABLE, JSONPATH
        :type ValueType: str
        """
        self._Key = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryPolicy(AbstractModel):
    """Description of CKafka delivery target retry policy

    """

    def __init__(self):
        r"""
        :param _RetryInterval: Retry interval in seconds
        :type RetryInterval: int
        :param _MaxRetryAttempts: Maximum number of retries
        :type MaxRetryAttempts: int
        """
        self._RetryInterval = None
        self._MaxRetryAttempts = None

    @property
    def RetryInterval(self):
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def MaxRetryAttempts(self):
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts


    def _deserialize(self, params):
        self._RetryInterval = params.get("RetryInterval")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Rule information

    """

    def __init__(self):
        r"""
        :param _Status: Status
        :type Status: str
        :param _ModTime: Modification time
        :type ModTime: str
        :param _Enable: Switch
        :type Enable: bool
        :param _Description: Description
        :type Description: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleName: Rule name
        :type RuleName: str
        :param _Targets: Target overview
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of TargetBrief
        :param _DeadLetterConfig: DLQ rule set by the rule, which may be null
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterConfig: :class:`tencentcloud.eb.v20210416.models.DeadLetterConfig`
        """
        self._Status = None
        self._ModTime = None
        self._Enable = None
        self._Description = None
        self._RuleId = None
        self._AddTime = None
        self._EventBusId = None
        self._RuleName = None
        self._Targets = None
        self._DeadLetterConfig = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DeadLetterConfig(self):
        return self._DeadLetterConfig

    @DeadLetterConfig.setter
    def DeadLetterConfig(self, DeadLetterConfig):
        self._DeadLetterConfig = DeadLetterConfig


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ModTime = params.get("ModTime")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._RuleId = params.get("RuleId")
        self._AddTime = params.get("AddTime")
        self._EventBusId = params.get("EventBusId")
        self._RuleName = params.get("RuleName")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetBrief()
                obj._deserialize(item)
                self._Targets.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self._DeadLetterConfig = DeadLetterConfig()
            self._DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SCFParams(AbstractModel):
    """SCF parameter

    """

    def __init__(self):
        r"""
        :param _BatchTimeout: Maximum waiting time for batch delivery
        :type BatchTimeout: int
        :param _BatchEventCount: Maximum number of events in batch delivery
        :type BatchEventCount: int
        :param _EnableBatchDelivery: Enables batch delivery
        :type EnableBatchDelivery: bool
        """
        self._BatchTimeout = None
        self._BatchEventCount = None
        self._EnableBatchDelivery = None

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery


    def _deserialize(self, params):
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """Target information

    """

    def __init__(self):
        r"""
        :param _Type: Target type
        :type Type: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _TargetId: Target ID
        :type TargetId: str
        :param _TargetDescription: Target description
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _EnableBatchDelivery: Enables batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableBatchDelivery: bool
        :param _BatchTimeout: Maximum waiting time for batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type BatchTimeout: int
        :param _BatchEventCount: Maximum number of events in batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type BatchEventCount: int
        """
        self._Type = None
        self._EventBusId = None
        self._TargetId = None
        self._TargetDescription = None
        self._RuleId = None
        self._EnableBatchDelivery = None
        self._BatchTimeout = None
        self._BatchEventCount = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetDescription(self):
        return self._TargetDescription

    @TargetDescription.setter
    def TargetDescription(self, TargetDescription):
        self._TargetDescription = TargetDescription

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._EventBusId = params.get("EventBusId")
        self._TargetId = params.get("TargetId")
        if params.get("TargetDescription") is not None:
            self._TargetDescription = TargetDescription()
            self._TargetDescription._deserialize(params.get("TargetDescription"))
        self._RuleId = params.get("RuleId")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetBrief(AbstractModel):
    """Target overview

    """

    def __init__(self):
        r"""
        :param _TargetId: Target ID
        :type TargetId: str
        :param _Type: Target type
        :type Type: str
        """
        self._TargetId = None
        self._Type = None

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetDescription(AbstractModel):
    """Target description

    """

    def __init__(self):
        r"""
        :param _ResourceDescription: Six-Segment QCS resource description. For more information, see [Resource Description Method](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type ResourceDescription: str
        :param _SCFParams: SCF parameter
        :type SCFParams: :class:`tencentcloud.eb.v20210416.models.SCFParams`
        :param _CkafkaTargetParams: CKafka parameters
        :type CkafkaTargetParams: :class:`tencentcloud.eb.v20210416.models.CkafkaTargetParams`
        :param _ESTargetParams: ElasticSearch parameters
        :type ESTargetParams: :class:`tencentcloud.eb.v20210416.models.ESTargetParams`
        """
        self._ResourceDescription = None
        self._SCFParams = None
        self._CkafkaTargetParams = None
        self._ESTargetParams = None

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription

    @property
    def SCFParams(self):
        return self._SCFParams

    @SCFParams.setter
    def SCFParams(self, SCFParams):
        self._SCFParams = SCFParams

    @property
    def CkafkaTargetParams(self):
        return self._CkafkaTargetParams

    @CkafkaTargetParams.setter
    def CkafkaTargetParams(self, CkafkaTargetParams):
        self._CkafkaTargetParams = CkafkaTargetParams

    @property
    def ESTargetParams(self):
        return self._ESTargetParams

    @ESTargetParams.setter
    def ESTargetParams(self, ESTargetParams):
        self._ESTargetParams = ESTargetParams


    def _deserialize(self, params):
        self._ResourceDescription = params.get("ResourceDescription")
        if params.get("SCFParams") is not None:
            self._SCFParams = SCFParams()
            self._SCFParams._deserialize(params.get("SCFParams"))
        if params.get("CkafkaTargetParams") is not None:
            self._CkafkaTargetParams = CkafkaTargetParams()
            self._CkafkaTargetParams._deserialize(params.get("CkafkaTargetParams"))
        if params.get("ESTargetParams") is not None:
            self._ESTargetParams = ESTargetParams()
            self._ESTargetParams._deserialize(params.get("ESTargetParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextParams(AbstractModel):
    """Describes how to slice data

    """

    def __init__(self):
        r"""
        :param _Separator: Comma, | , tab, space, line break, %, or #, which can contain only 1 character.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Separator: str
        :param _Regex: Entered regex (128 characters)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Regex: str
        """
        self._Separator = None
        self._Regex = None

    @property
    def Separator(self):
        return self._Separator

    @Separator.setter
    def Separator(self, Separator):
        self._Separator = Separator

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Separator = params.get("Separator")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transform(AbstractModel):
    """Describes how to transform data

    """

    def __init__(self):
        r"""
        :param _OutputStructs: Describes how to transform data
        :type OutputStructs: list of OutputStructParam
        """
        self._OutputStructs = None

    @property
    def OutputStructs(self):
        return self._OutputStructs

    @OutputStructs.setter
    def OutputStructs(self, OutputStructs):
        self._OutputStructs = OutputStructs


    def _deserialize(self, params):
        if params.get("OutputStructs") is not None:
            self._OutputStructs = []
            for item in params.get("OutputStructs"):
                obj = OutputStructParam()
                obj._deserialize(item)
                self._OutputStructs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transformation(AbstractModel):
    """Transformer

    """

    def __init__(self):
        r"""
        :param _Extraction: Describes how to extract data
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extraction: :class:`tencentcloud.eb.v20210416.models.Extraction`
        :param _EtlFilter: Describes how to filter data
Note: this field may return null, indicating that no valid values can be obtained.
        :type EtlFilter: :class:`tencentcloud.eb.v20210416.models.EtlFilter`
        :param _Transform: Describes how to transform data
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transform: :class:`tencentcloud.eb.v20210416.models.Transform`
        """
        self._Extraction = None
        self._EtlFilter = None
        self._Transform = None

    @property
    def Extraction(self):
        return self._Extraction

    @Extraction.setter
    def Extraction(self, Extraction):
        self._Extraction = Extraction

    @property
    def EtlFilter(self):
        return self._EtlFilter

    @EtlFilter.setter
    def EtlFilter(self, EtlFilter):
        self._EtlFilter = EtlFilter

    @property
    def Transform(self):
        return self._Transform

    @Transform.setter
    def Transform(self, Transform):
        self._Transform = Transform


    def _deserialize(self, params):
        if params.get("Extraction") is not None:
            self._Extraction = Extraction()
            self._Extraction._deserialize(params.get("Extraction"))
        if params.get("EtlFilter") is not None:
            self._EtlFilter = EtlFilter()
            self._EtlFilter._deserialize(params.get("EtlFilter"))
        if params.get("Transform") is not None:
            self._Transform = Transform()
            self._Transform._deserialize(params.get("Transform"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionRequest(AbstractModel):
    """UpdateConnection request structure.

    """

    def __init__(self):
        r"""
        :param _ConnectionId: Connector ID
        :type ConnectionId: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Enable: Switch
        :type Enable: bool
        :param _Description: Description
        :type Description: str
        :param _ConnectionName: Connector name
        :type ConnectionName: str
        """
        self._ConnectionId = None
        self._EventBusId = None
        self._Enable = None
        self._Description = None
        self._ConnectionName = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._ConnectionName = params.get("ConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionResponse(AbstractModel):
    """UpdateConnection response structure.

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


class UpdateEventBusRequest(AbstractModel):
    """UpdateEventBus request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Description: Event bus description, which can contain up to 200 characters of any type.
        :type Description: str
        :param _EventBusName: Event bus name: it can contain 2-60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter.
        :type EventBusName: str
        :param _SaveDays: Log retention period
        :type SaveDays: int
        :param _LogTopicId: EventBridge log topic ID
        :type LogTopicId: str
        :param _EnableStore: Whether to enable log retention
        :type EnableStore: bool
        """
        self._EventBusId = None
        self._Description = None
        self._EventBusName = None
        self._SaveDays = None
        self._LogTopicId = None
        self._EnableStore = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._Description = params.get("Description")
        self._EventBusName = params.get("EventBusName")
        self._SaveDays = params.get("SaveDays")
        self._LogTopicId = params.get("LogTopicId")
        self._EnableStore = params.get("EnableStore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEventBusResponse(AbstractModel):
    """UpdateEventBus response structure.

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


class UpdateRuleRequest(AbstractModel):
    """UpdateRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _Enable: Switch.
        :type Enable: bool
        :param _Description: Rule description, which can contain up to 200 characters of any type.
        :type Description: str
        :param _EventPattern: See [CKafka Target](https://intl.cloud.tencent.com/document/product/1359/56084?from_cn_redirect=1)
        :type EventPattern: str
        :param _RuleName: Event rule name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type RuleName: str
        """
        self._RuleId = None
        self._EventBusId = None
        self._Enable = None
        self._Description = None
        self._EventPattern = None
        self._RuleName = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._EventBusId = params.get("EventBusId")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._EventPattern = params.get("EventPattern")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    """UpdateRule response structure.

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


class UpdateTargetRequest(AbstractModel):
    """UpdateTarget request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Event rule ID
        :type RuleId: str
        :param _TargetId: Delivery target ID
        :type TargetId: str
        :param _EnableBatchDelivery: Enables batch delivery
        :type EnableBatchDelivery: bool
        :param _BatchTimeout: Maximum waiting time for batch delivery
        :type BatchTimeout: int
        :param _BatchEventCount: Maximum number of events in batch delivery
        :type BatchEventCount: int
        """
        self._EventBusId = None
        self._RuleId = None
        self._TargetId = None
        self._EnableBatchDelivery = None
        self._BatchTimeout = None
        self._BatchEventCount = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TargetId = params.get("TargetId")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTargetResponse(AbstractModel):
    """UpdateTarget response structure.

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


class UpdateTransformationRequest(AbstractModel):
    """UpdateTransformation request structure.

    """

    def __init__(self):
        r"""
        :param _EventBusId: Event bus ID
        :type EventBusId: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _TransformationId: Transformer ID
        :type TransformationId: str
        :param _Transformations: Transformation rule list (currently, only one is supported)
        :type Transformations: list of Transformation
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None
        self._Transformations = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTransformationResponse(AbstractModel):
    """UpdateTransformation response structure.

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