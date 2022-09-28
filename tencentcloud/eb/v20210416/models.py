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
        :param Protocol: HTTPS
        :type Protocol: str
        :param Method: POST
        :type Method: str
        """
        self.Protocol = None
        self.Method = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckTransformationRequest(AbstractModel):
    """CheckTransformation request structure.

    """

    def __init__(self):
        r"""
        :param Input: JSON string to be processed
        :type Input: str
        :param Transformations: Transformation rule list
        :type Transformations: list of Transformation
        """
        self.Input = None
        self.Transformations = None


    def _deserialize(self, params):
        self.Input = params.get("Input")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTransformationResponse(AbstractModel):
    """CheckTransformation response structure.

    """

    def __init__(self):
        r"""
        :param Output: Data processed by `Transformations`
        :type Output: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Output = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Output = params.get("Output")
        self.RequestId = params.get("RequestId")


class CkafkaDeliveryParams(AbstractModel):
    """Parameter of the Kafka topic to be delivered to

    """

    def __init__(self):
        r"""
        :param TopicName: ckafka topic name
        :type TopicName: str
        :param ResourceDescription: Six-Segment QCS description of CKafka resource
        :type ResourceDescription: str
        """
        self.TopicName = None
        self.ResourceDescription = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.ResourceDescription = params.get("ResourceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaParams(AbstractModel):
    """CKafka connector parameter

    """

    def __init__(self):
        r"""
        :param Offset: kafka offset
        :type Offset: str
        :param TopicName: ckafka  topic
        :type TopicName: str
        """
        self.Offset = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaTargetParams(AbstractModel):
    """CKafka delivery target description

    """

    def __init__(self):
        r"""
        :param TopicName: CKafka topic to be delivered to
        :type TopicName: str
        :param RetryPolicy: Retry policy
        :type RetryPolicy: :class:`tencentcloud.eb.v20210416.models.RetryPolicy`
        """
        self.TopicName = None
        self.RetryPolicy = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        if params.get("RetryPolicy") is not None:
            self.RetryPolicy = RetryPolicy()
            self.RetryPolicy._deserialize(params.get("RetryPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Connection(AbstractModel):
    """Connection information

    """

    def __init__(self):
        r"""
        :param Status: Status
        :type Status: str
        :param ModTime: Update time
        :type ModTime: str
        :param Enable: Switch
        :type Enable: bool
        :param Description: Description
        :type Description: str
        :param AddTime: Creation time
        :type AddTime: str
        :param ConnectionId: Connector ID
        :type ConnectionId: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param ConnectionDescription: Connector description
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param ConnectionName: Connector name
        :type ConnectionName: str
        :param Type: Type
        :type Type: str
        """
        self.Status = None
        self.ModTime = None
        self.Enable = None
        self.Description = None
        self.AddTime = None
        self.ConnectionId = None
        self.EventBusId = None
        self.ConnectionDescription = None
        self.ConnectionName = None
        self.Type = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ModTime = params.get("ModTime")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        if params.get("ConnectionDescription") is not None:
            self.ConnectionDescription = ConnectionDescription()
            self.ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self.ConnectionName = params.get("ConnectionName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionDescription(AbstractModel):
    """Connection description

    """

    def __init__(self):
        r"""
        :param ResourceDescription: Six-Segment QCS resource description. For more information, see [Resource Description Method](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type ResourceDescription: str
        :param APIGWParams: API Gateway parameters
Note: this field may return null, indicating that no valid values can be obtained.
        :type APIGWParams: :class:`tencentcloud.eb.v20210416.models.APIGWParams`
        :param CkafkaParams: CKafka parameters
Note: this field may return null, indicating that no valid values can be obtained.
        :type CkafkaParams: :class:`tencentcloud.eb.v20210416.models.CkafkaParams`
        """
        self.ResourceDescription = None
        self.APIGWParams = None
        self.CkafkaParams = None


    def _deserialize(self, params):
        self.ResourceDescription = params.get("ResourceDescription")
        if params.get("APIGWParams") is not None:
            self.APIGWParams = APIGWParams()
            self.APIGWParams._deserialize(params.get("APIGWParams"))
        if params.get("CkafkaParams") is not None:
            self.CkafkaParams = CkafkaParams()
            self.CkafkaParams._deserialize(params.get("CkafkaParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionRequest(AbstractModel):
    """CreateConnection request structure.

    """

    def __init__(self):
        r"""
        :param ConnectionDescription: Connector description
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param ConnectionName: Connector name
        :type ConnectionName: str
        :param Description: Description
        :type Description: str
        :param Enable: Whether to enable
        :type Enable: bool
        :param Type: Type of the connector
        :type Type: str
        """
        self.ConnectionDescription = None
        self.EventBusId = None
        self.ConnectionName = None
        self.Description = None
        self.Enable = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("ConnectionDescription") is not None:
            self.ConnectionDescription = ConnectionDescription()
            self.ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self.EventBusId = params.get("EventBusId")
        self.ConnectionName = params.get("ConnectionName")
        self.Description = params.get("Description")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionResponse(AbstractModel):
    """CreateConnection response structure.

    """

    def __init__(self):
        r"""
        :param ConnectionId: Connector ID
        :type ConnectionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConnectionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.RequestId = params.get("RequestId")


class CreateEventBusRequest(AbstractModel):
    """CreateEventBus request structure.

    """

    def __init__(self):
        r"""
        :param EventBusName: Event bus name: it can contain 2-60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter.
        :type EventBusName: str
        :param Description: Event bus description, which can contain up to 200 characters of any type.
        :type Description: str
        """
        self.EventBusName = None
        self.Description = None


    def _deserialize(self, params):
        self.EventBusName = params.get("EventBusName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEventBusResponse(AbstractModel):
    """CreateEventBus response structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventBusId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param EventPattern: See [Event Pattern](https://intl.cloud.tencent.com/document/product/1359/56084?from_cn_redirect=1)
        :type EventPattern: str
        :param EventBusId: Event bus ID.
        :type EventBusId: str
        :param RuleName: Event bus name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type RuleName: str
        :param Enable: Switch.
        :type Enable: bool
        :param Description: Event bus description, which can contain up to 200 characters of any type
        :type Description: str
        """
        self.EventPattern = None
        self.EventBusId = None
        self.RuleName = None
        self.Enable = None
        self.Description = None


    def _deserialize(self, params):
        self.EventPattern = params.get("EventPattern")
        self.EventBusId = params.get("EventBusId")
        self.RuleName = params.get("RuleName")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Event rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateTargetRequest(AbstractModel):
    """CreateTarget request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Type: Target type
        :type Type: str
        :param TargetDescription: Target description
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param RuleId: Event rule ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.Type = None
        self.TargetDescription = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        if params.get("TargetDescription") is not None:
            self.TargetDescription = TargetDescription()
            self.TargetDescription._deserialize(params.get("TargetDescription"))
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetResponse(AbstractModel):
    """CreateTarget response structure.

    """

    def __init__(self):
        r"""
        :param TargetId: Target ID
        :type TargetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TargetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetId = params.get("TargetId")
        self.RequestId = params.get("RequestId")


class CreateTransformationRequest(AbstractModel):
    """CreateTransformation request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Transformations: Transformation rule list (currently, only one is supported)
        :type Transformations: list of Transformation
        """
        self.EventBusId = None
        self.RuleId = None
        self.Transformations = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransformationResponse(AbstractModel):
    """CreateTransformation response structure.

    """

    def __init__(self):
        r"""
        :param TransformationId: Generated transformer ID
        :type TransformationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TransformationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransformationId = params.get("TransformationId")
        self.RequestId = params.get("RequestId")


class DeadLetterConfig(AbstractModel):
    """DLQ configuration of rule

    """

    def __init__(self):
        r"""
        :param DisposeMethod: Three modes are supported: DLQ, drop, and ignore error, which correspond to `DLQ`, `DROP`, and `IGNORE_ERROR` respectively
        :type DisposeMethod: str
        :param CkafkaDeliveryParams: If the DLQ mode is set, this option is required. Error messages will be delivered to the corresponding Kafka topic
Note: this field may return null, indicating that no valid values can be obtained.
        :type CkafkaDeliveryParams: :class:`tencentcloud.eb.v20210416.models.CkafkaDeliveryParams`
        """
        self.DisposeMethod = None
        self.CkafkaDeliveryParams = None


    def _deserialize(self, params):
        self.DisposeMethod = params.get("DisposeMethod")
        if params.get("CkafkaDeliveryParams") is not None:
            self.CkafkaDeliveryParams = CkafkaDeliveryParams()
            self.CkafkaDeliveryParams._deserialize(params.get("CkafkaDeliveryParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionRequest(AbstractModel):
    """DeleteConnection request structure.

    """

    def __init__(self):
        r"""
        :param ConnectionId: Connector ID
        :type ConnectionId: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        """
        self.ConnectionId = None
        self.EventBusId = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionResponse(AbstractModel):
    """DeleteConnection response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEventBusRequest(AbstractModel):
    """DeleteEventBus request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        """
        self.EventBusId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEventBusResponse(AbstractModel):
    """DeleteEventBus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Event rule ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTargetRequest(AbstractModel):
    """DeleteTarget request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param TargetId: Delivery target ID
        :type TargetId: str
        :param RuleId: Event rule ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.TargetId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.TargetId = params.get("TargetId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetResponse(AbstractModel):
    """DeleteTarget response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTransformationRequest(AbstractModel):
    """DeleteTransformation request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param TransformationId: Transformer ID
        :type TransformationId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTransformationResponse(AbstractModel):
    """DeleteTransformation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ESTargetParams(AbstractModel):
    """ES rule targets

    """

    def __init__(self):
        r"""
        :param NetMode: Network connection type
        :type NetMode: str
        :param IndexPrefix: Index prefix
        :type IndexPrefix: str
        :param RotationInterval: ES log rotation interval
        :type RotationInterval: str
        :param OutputMode: DTS event configuration
        :type OutputMode: str
        :param IndexSuffixMode: DTS indexing configuration
        :type IndexSuffixMode: str
        :param IndexTemplateType: ES template type
        :type IndexTemplateType: str
        """
        self.NetMode = None
        self.IndexPrefix = None
        self.RotationInterval = None
        self.OutputMode = None
        self.IndexSuffixMode = None
        self.IndexTemplateType = None


    def _deserialize(self, params):
        self.NetMode = params.get("NetMode")
        self.IndexPrefix = params.get("IndexPrefix")
        self.RotationInterval = params.get("RotationInterval")
        self.OutputMode = params.get("OutputMode")
        self.IndexSuffixMode = params.get("IndexSuffixMode")
        self.IndexTemplateType = params.get("IndexTemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtlFilter(AbstractModel):
    """Describes how to filter data

    """

    def __init__(self):
        r"""
        :param Filter: The syntax is the same as that of `Rule`
        :type Filter: str
        """
        self.Filter = None


    def _deserialize(self, params):
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventBus(AbstractModel):
    """Event bus information

    """

    def __init__(self):
        r"""
        :param ModTime: Update time
        :type ModTime: str
        :param Description: Event bus description, which can contain up to 200 characters of any type
        :type Description: str
        :param AddTime: Creation time
        :type AddTime: str
        :param EventBusName: Event bus name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type EventBusName: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Type: Event bus type
        :type Type: str
        """
        self.ModTime = None
        self.Description = None
        self.AddTime = None
        self.EventBusName = None
        self.EventBusId = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.EventBusName = params.get("EventBusName")
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Extraction(AbstractModel):
    """Describes how to extract data

    """

    def __init__(self):
        r"""
        :param ExtractionInputPath: JsonPath, which will be `$.` by default if not specified
        :type ExtractionInputPath: str
        :param Format: Valid values: TEXT/JSON
        :type Format: str
        :param TextParams: Only required for `Text`
Note: this field may return null, indicating that no valid values can be obtained.
        :type TextParams: :class:`tencentcloud.eb.v20210416.models.TextParams`
        """
        self.ExtractionInputPath = None
        self.Format = None
        self.TextParams = None


    def _deserialize(self, params):
        self.ExtractionInputPath = params.get("ExtractionInputPath")
        self.Format = params.get("Format")
        if params.get("TextParams") is not None:
            self.TextParams = TextParams()
            self.TextParams._deserialize(params.get("TextParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries, such as filtering ID, name, and status
    * If more than one filter exists, the logical relationship between these filters is `AND`.
    * If multiple values exist in one filter, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param Values: One or more filter values.
        :type Values: list of str
        :param Name: Filter name.
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusRequest(AbstractModel):
    """GetEventBus request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        """
        self.EventBusId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusResponse(AbstractModel):
    """GetEventBus response structure.

    """

    def __init__(self):
        r"""
        :param ModTime: Update time
        :type ModTime: str
        :param Description: Event bus description
        :type Description: str
        :param ClsTopicId: Log topic ID
        :type ClsTopicId: str
        :param AddTime: Creation time.
        :type AddTime: str
        :param ClsLogsetId: Logset ID
        :type ClsLogsetId: str
        :param EventBusName: Event bus name
        :type EventBusName: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Type: (Disused) Event bus type
        :type Type: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ModTime = None
        self.Description = None
        self.ClsTopicId = None
        self.AddTime = None
        self.ClsLogsetId = None
        self.EventBusName = None
        self.EventBusId = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Description = params.get("Description")
        self.ClsTopicId = params.get("ClsTopicId")
        self.AddTime = params.get("AddTime")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.EventBusName = params.get("EventBusName")
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    """GetRule request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Event rule ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    """GetRule response structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Event rule ID
        :type RuleId: str
        :param RuleName: Event rule name
        :type RuleName: str
        :param Status: Event rule status
        :type Status: str
        :param Enable: Switch
        :type Enable: bool
        :param Description: Event rule description
        :type Description: str
        :param EventPattern: Event pattern
        :type EventPattern: str
        :param AddTime: Creation time
        :type AddTime: str
        :param ModTime: Update time
        :type ModTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Enable = None
        self.Description = None
        self.EventPattern = None
        self.AddTime = None
        self.ModTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.EventPattern = params.get("EventPattern")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.RequestId = params.get("RequestId")


class GetTransformationRequest(AbstractModel):
    """GetTransformation request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param TransformationId: Transformer ID
        :type TransformationId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTransformationResponse(AbstractModel):
    """GetTransformation response structure.

    """

    def __init__(self):
        r"""
        :param Transformations: Transformation rule list
        :type Transformations: list of Transformation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Transformations = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        self.RequestId = params.get("RequestId")


class ListConnectionsRequest(AbstractModel):
    """ListConnections request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime, ModTime
        :type OrderBy: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC, DESC
        :type Order: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.EventBusId = None
        self.OrderBy = None
        self.Limit = None
        self.Order = None
        self.Offset = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConnectionsResponse(AbstractModel):
    """ListConnections response structure.

    """

    def __init__(self):
        r"""
        :param Connections: Connector information
        :type Connections: list of Connection
        :param TotalCount: Total number of connectors
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Connections = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Connections") is not None:
            self.Connections = []
            for item in params.get("Connections"):
                obj = Connection()
                obj._deserialize(item)
                self.Connections.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListEventBusesRequest(AbstractModel):
    """ListEventBuses request structure.

    """

    def __init__(self):
        r"""
        :param OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        :param Filters: Filter. For more information, see the Instance Filter Table below. Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        """
        self.OrderBy = None
        self.Limit = None
        self.Order = None
        self.Filters = None
        self.Offset = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventBusesResponse(AbstractModel):
    """ListEventBuses response structure.

    """

    def __init__(self):
        r"""
        :param EventBuses: Event bus information
        :type EventBuses: list of EventBus
        :param TotalCount: Total number of event buses
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventBuses = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBuses") is not None:
            self.EventBuses = []
            for item in params.get("EventBuses"):
                obj = EventBus()
                obj._deserialize(item)
                self.EventBuses.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListRulesRequest(AbstractModel):
    """ListRules request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        """
        self.EventBusId = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRulesResponse(AbstractModel):
    """ListRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Event rule information
        :type Rules: list of Rule
        :param TotalCount: Total number of event rules
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListTargetsRequest(AbstractModel):
    """ListTargets request structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Event rule ID
        :type RuleId: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime (creation time), ModTime (modification time)
        :type OrderBy: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC (ascending order), DESC (descending order)
        :type Order: str
        """
        self.RuleId = None
        self.EventBusId = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsResponse(AbstractModel):
    """ListTargets response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of targets
        :type TotalCount: int
        :param Targets: Target information
        :type Targets: list of Target
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class OutputStructParam(AbstractModel):
    """`Transform` output parameter

    """

    def __init__(self):
        r"""
        :param Key: Key in the corresponding JSON output
        :type Key: str
        :param Value: You can enter a JsonPath, constant, or built-in date type
        :type Value: str
        :param ValueType: Data type of `Value`. Valid values: STRING, NUMBER, BOOLEAN, NULL, SYS_VARIABLE, JSONPATH
        :type ValueType: str
        """
        self.Key = None
        self.Value = None
        self.ValueType = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryPolicy(AbstractModel):
    """Description of CKafka delivery target retry policy

    """

    def __init__(self):
        r"""
        :param RetryInterval: Retry interval in seconds
        :type RetryInterval: int
        :param MaxRetryAttempts: Maximum number of retries
        :type MaxRetryAttempts: int
        """
        self.RetryInterval = None
        self.MaxRetryAttempts = None


    def _deserialize(self, params):
        self.RetryInterval = params.get("RetryInterval")
        self.MaxRetryAttempts = params.get("MaxRetryAttempts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Rule information

    """

    def __init__(self):
        r"""
        :param Status: Status
        :type Status: str
        :param ModTime: Modification time
        :type ModTime: str
        :param Enable: Switch
        :type Enable: bool
        :param Description: Description
        :type Description: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param AddTime: Creation time
        :type AddTime: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleName: Rule name
        :type RuleName: str
        :param Targets: Target overview
Note: this field may return null, indicating that no valid values can be obtained.
        :type Targets: list of TargetBrief
        :param DeadLetterConfig: DLQ rule set by the rule, which may be null
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterConfig: :class:`tencentcloud.eb.v20210416.models.DeadLetterConfig`
        """
        self.Status = None
        self.ModTime = None
        self.Enable = None
        self.Description = None
        self.RuleId = None
        self.AddTime = None
        self.EventBusId = None
        self.RuleName = None
        self.Targets = None
        self.DeadLetterConfig = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ModTime = params.get("ModTime")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.RuleId = params.get("RuleId")
        self.AddTime = params.get("AddTime")
        self.EventBusId = params.get("EventBusId")
        self.RuleName = params.get("RuleName")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetBrief()
                obj._deserialize(item)
                self.Targets.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SCFParams(AbstractModel):
    """SCF parameter

    """

    def __init__(self):
        r"""
        :param BatchTimeout: Maximum waiting time for batch delivery
        :type BatchTimeout: int
        :param BatchEventCount: Maximum number of events in batch delivery
        :type BatchEventCount: int
        :param EnableBatchDelivery: Enables batch delivery
        :type EnableBatchDelivery: bool
        """
        self.BatchTimeout = None
        self.BatchEventCount = None
        self.EnableBatchDelivery = None


    def _deserialize(self, params):
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """Target information

    """

    def __init__(self):
        r"""
        :param Type: Target type
        :type Type: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param TargetId: Target ID
        :type TargetId: str
        :param TargetDescription: Target description
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param RuleId: Event rule ID
        :type RuleId: str
        :param EnableBatchDelivery: Enables batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableBatchDelivery: bool
        :param BatchTimeout: Maximum waiting time for batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type BatchTimeout: int
        :param BatchEventCount: Maximum number of events in batch delivery
Note: this field may return null, indicating that no valid values can be obtained.
        :type BatchEventCount: int
        """
        self.Type = None
        self.EventBusId = None
        self.TargetId = None
        self.TargetDescription = None
        self.RuleId = None
        self.EnableBatchDelivery = None
        self.BatchTimeout = None
        self.BatchEventCount = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.EventBusId = params.get("EventBusId")
        self.TargetId = params.get("TargetId")
        if params.get("TargetDescription") is not None:
            self.TargetDescription = TargetDescription()
            self.TargetDescription._deserialize(params.get("TargetDescription"))
        self.RuleId = params.get("RuleId")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetBrief(AbstractModel):
    """Target overview

    """

    def __init__(self):
        r"""
        :param TargetId: Target ID
        :type TargetId: str
        :param Type: Target type
        :type Type: str
        """
        self.TargetId = None
        self.Type = None


    def _deserialize(self, params):
        self.TargetId = params.get("TargetId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetDescription(AbstractModel):
    """Target description

    """

    def __init__(self):
        r"""
        :param ResourceDescription: Six-Segment QCS resource description. For more information, see [Resource Description Method](https://intl.cloud.tencent.com/document/product/598/10606?from_cn_redirect=1)
        :type ResourceDescription: str
        :param SCFParams: SCF parameter
        :type SCFParams: :class:`tencentcloud.eb.v20210416.models.SCFParams`
        :param CkafkaTargetParams: CKafka parameters
        :type CkafkaTargetParams: :class:`tencentcloud.eb.v20210416.models.CkafkaTargetParams`
        :param ESTargetParams: ElasticSearch parameters
        :type ESTargetParams: :class:`tencentcloud.eb.v20210416.models.ESTargetParams`
        """
        self.ResourceDescription = None
        self.SCFParams = None
        self.CkafkaTargetParams = None
        self.ESTargetParams = None


    def _deserialize(self, params):
        self.ResourceDescription = params.get("ResourceDescription")
        if params.get("SCFParams") is not None:
            self.SCFParams = SCFParams()
            self.SCFParams._deserialize(params.get("SCFParams"))
        if params.get("CkafkaTargetParams") is not None:
            self.CkafkaTargetParams = CkafkaTargetParams()
            self.CkafkaTargetParams._deserialize(params.get("CkafkaTargetParams"))
        if params.get("ESTargetParams") is not None:
            self.ESTargetParams = ESTargetParams()
            self.ESTargetParams._deserialize(params.get("ESTargetParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextParams(AbstractModel):
    """Describes how to slice data

    """

    def __init__(self):
        r"""
        :param Separator: Comma, | , tab, space, line break, %, or #, which can contain only 1 character.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Separator: str
        :param Regex: Entered regex (128 characters)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Regex: str
        """
        self.Separator = None
        self.Regex = None


    def _deserialize(self, params):
        self.Separator = params.get("Separator")
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transform(AbstractModel):
    """Describes how to transform data

    """

    def __init__(self):
        r"""
        :param OutputStructs: Describes how to transform data
        :type OutputStructs: list of OutputStructParam
        """
        self.OutputStructs = None


    def _deserialize(self, params):
        if params.get("OutputStructs") is not None:
            self.OutputStructs = []
            for item in params.get("OutputStructs"):
                obj = OutputStructParam()
                obj._deserialize(item)
                self.OutputStructs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transformation(AbstractModel):
    """Transformer

    """

    def __init__(self):
        r"""
        :param Extraction: Describes how to extract data
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extraction: :class:`tencentcloud.eb.v20210416.models.Extraction`
        :param EtlFilter: Describes how to filter data
Note: this field may return null, indicating that no valid values can be obtained.
        :type EtlFilter: :class:`tencentcloud.eb.v20210416.models.EtlFilter`
        :param Transform: Describes how to transform data
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transform: :class:`tencentcloud.eb.v20210416.models.Transform`
        """
        self.Extraction = None
        self.EtlFilter = None
        self.Transform = None


    def _deserialize(self, params):
        if params.get("Extraction") is not None:
            self.Extraction = Extraction()
            self.Extraction._deserialize(params.get("Extraction"))
        if params.get("EtlFilter") is not None:
            self.EtlFilter = EtlFilter()
            self.EtlFilter._deserialize(params.get("EtlFilter"))
        if params.get("Transform") is not None:
            self.Transform = Transform()
            self.Transform._deserialize(params.get("Transform"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionRequest(AbstractModel):
    """UpdateConnection request structure.

    """

    def __init__(self):
        r"""
        :param ConnectionId: Connector ID
        :type ConnectionId: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Enable: Switch
        :type Enable: bool
        :param Description: Description
        :type Description: str
        :param ConnectionName: Connector name
        :type ConnectionName: str
        """
        self.ConnectionId = None
        self.EventBusId = None
        self.Enable = None
        self.Description = None
        self.ConnectionName = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.ConnectionName = params.get("ConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionResponse(AbstractModel):
    """UpdateConnection response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateEventBusRequest(AbstractModel):
    """UpdateEventBus request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Description: Event bus description, which can contain up to 200 characters of any type.
        :type Description: str
        :param EventBusName: Event bus name: it can contain 2-60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter.
        :type EventBusName: str
        """
        self.EventBusId = None
        self.Description = None
        self.EventBusName = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.Description = params.get("Description")
        self.EventBusName = params.get("EventBusName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEventBusResponse(AbstractModel):
    """UpdateEventBus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    """UpdateRule request structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Event rule ID
        :type RuleId: str
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param Enable: Switch.
        :type Enable: bool
        :param Description: Rule description, which can contain up to 200 characters of any type.
        :type Description: str
        :param EventPattern: See [CKafka Target](https://intl.cloud.tencent.com/document/product/1359/56084?from_cn_redirect=1)
        :type EventPattern: str
        :param RuleName: Event rule name, which can contain 2–60 letters, digits, underscores, and hyphens and must start with a letter and end with a digit or letter
        :type RuleName: str
        """
        self.RuleId = None
        self.EventBusId = None
        self.Enable = None
        self.Description = None
        self.EventPattern = None
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.EventBusId = params.get("EventBusId")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.EventPattern = params.get("EventPattern")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    """UpdateRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateTargetRequest(AbstractModel):
    """UpdateTarget request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Event rule ID
        :type RuleId: str
        :param TargetId: Delivery target ID
        :type TargetId: str
        :param EnableBatchDelivery: Enables batch delivery
        :type EnableBatchDelivery: bool
        :param BatchTimeout: Maximum waiting time for batch delivery
        :type BatchTimeout: int
        :param BatchEventCount: Maximum number of events in batch delivery
        :type BatchEventCount: int
        """
        self.EventBusId = None
        self.RuleId = None
        self.TargetId = None
        self.EnableBatchDelivery = None
        self.BatchTimeout = None
        self.BatchEventCount = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TargetId = params.get("TargetId")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTargetResponse(AbstractModel):
    """UpdateTarget response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateTransformationRequest(AbstractModel):
    """UpdateTransformation request structure.

    """

    def __init__(self):
        r"""
        :param EventBusId: Event bus ID
        :type EventBusId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param TransformationId: Transformer ID
        :type TransformationId: str
        :param Transformations: Transformation rule list (currently, only one is supported)
        :type Transformations: list of Transformation
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None
        self.Transformations = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTransformationResponse(AbstractModel):
    """UpdateTransformation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")