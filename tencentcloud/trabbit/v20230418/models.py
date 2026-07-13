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


class CreateRabbitMQServerlessBindingRequest(AbstractModel):
    r"""CreateRabbitMQServerlessBinding request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance Id</p>
        :type InstanceId: str
        :param _VirtualHost: <p>Vhost parameter</p>
        :type VirtualHost: str
        :param _Source: <p>Source exchange</p>
        :type Source: str
        :param _DestinationType: <p>Target type, value queue or exchange</p>
        :type DestinationType: str
        :param _Destination: <p>Target queue or switch</p>
        :type Destination: str
        :param _RoutingKey: <p>Bind key</p>
        :type RoutingKey: str
        :param _Arguments: <p>When creating a Binding for Header type Exchange, parameters can be passed in. No need to input for other types of Exchange.</p>
        :type Arguments: list of RabbitMQServerlessKeyValuePair
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Source = None
        self._DestinationType = None
        self._Destination = None
        self._RoutingKey = None
        self._Arguments = None

    @property
    def InstanceId(self):
        r"""<p>Instance Id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""<p>Vhost parameter</p>
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Source(self):
        r"""<p>Source exchange</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DestinationType(self):
        r"""<p>Target type, value queue or exchange</p>
        :rtype: str
        """
        return self._DestinationType

    @DestinationType.setter
    def DestinationType(self, DestinationType):
        self._DestinationType = DestinationType

    @property
    def Destination(self):
        r"""<p>Target queue or switch</p>
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def RoutingKey(self):
        r"""<p>Bind key</p>
        :rtype: str
        """
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey

    @property
    def Arguments(self):
        r"""<p>When creating a Binding for Header type Exchange, parameters can be passed in. No need to input for other types of Exchange.</p>
        :rtype: list of RabbitMQServerlessKeyValuePair
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Source = params.get("Source")
        self._DestinationType = params.get("DestinationType")
        self._Destination = params.get("Destination")
        self._RoutingKey = params.get("RoutingKey")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = RabbitMQServerlessKeyValuePair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessBindingResponse(AbstractModel):
    r"""CreateRabbitMQServerlessBinding response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Queue name</p>
        :type InstanceId: str
        :param _VirtualHost: <p>vhost parameter</p>
        :type VirtualHost: str
        :param _BindingId: <p>Routing relationship Id</p>
        :type BindingId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Queue name</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""<p>vhost parameter</p>
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        r"""<p>Routing relationship Id</p>
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

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
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessExchangeRequest(AbstractModel):
    r"""CreateRabbitMQServerlessExchange request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: VHost parameter.
        :type VirtualHost: str
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _ExchangeType: Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :type ExchangeType: str
        :param _Remark: Specifies the remark for exchange.
        :type Remark: str
        :param _Durable: Specifies whether it is a persistent exchange. when the cluster restarts, all exchanges with this field set to "false" will be cleared.
        :type Durable: bool
        :param _AutoDelete: Whether to auto-delete this exchange. if set to "true", the exchange will be automatically deleted when all routing relationships on the current exchange are unbound.
        :type AutoDelete: bool
        :param _Internal: Specifies whether it is an internal exchange. if set to "true", messages cannot be directly delivered to this exchange. they need to be forwarded through another exchange in the routing settings.
        :type Internal: bool
        :param _AlternateExchange: Alternative exchange. if a message cannot be sent to the current exchange, it will be sent to this alternative exchange.
        :type AlternateExchange: str
        :param _DelayedExchangeType: exchange type behind delay type, supports "fanout", "direct", "topic", "headers".
        :type DelayedExchangeType: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None
        self._ExchangeType = None
        self._Remark = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._AlternateExchange = None
        self._DelayedExchangeType = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""VHost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def ExchangeType(self):
        r"""Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def Remark(self):
        r"""Specifies the remark for exchange.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Durable(self):
        r"""Specifies whether it is a persistent exchange. when the cluster restarts, all exchanges with this field set to "false" will be cleared.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Whether to auto-delete this exchange. if set to "true", the exchange will be automatically deleted when all routing relationships on the current exchange are unbound.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        r"""Specifies whether it is an internal exchange. if set to "true", messages cannot be directly delivered to this exchange. they need to be forwarded through another exchange in the routing settings.
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def AlternateExchange(self):
        r"""Alternative exchange. if a message cannot be sent to the current exchange, it will be sent to this alternative exchange.
        :rtype: str
        """
        return self._AlternateExchange

    @AlternateExchange.setter
    def AlternateExchange(self, AlternateExchange):
        self._AlternateExchange = AlternateExchange

    @property
    def DelayedExchangeType(self):
        r"""exchange type behind delay type, supports "fanout", "direct", "topic", "headers".
        :rtype: str
        """
        return self._DelayedExchangeType

    @DelayedExchangeType.setter
    def DelayedExchangeType(self, DelayedExchangeType):
        self._DelayedExchangeType = DelayedExchangeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        self._ExchangeType = params.get("ExchangeType")
        self._Remark = params.get("Remark")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._AlternateExchange = params.get("AlternateExchange")
        self._DelayedExchangeType = params.get("DelayedExchangeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessExchangeResponse(AbstractModel):
    r"""CreateRabbitMQServerlessExchange response structure.

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

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
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessQueueRequest(AbstractModel):
    r"""CreateRabbitMQServerlessQueue request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: VHost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _QueueType: Supports only classic.
        :type QueueType: str
        :param _Durable: Durable flag. specifies that for the classic type, it must be passed in. for the quorum type, there is no need to pass it in and it is fixed as true.
        :type Durable: bool
        :param _AutoDelete: Automatic cleanup. the classic type must be passed. the quorum type does not need to be passed and is fixed as false.
        :type AutoDelete: bool
        :param _Remark: Remarks
        :type Remark: str
        :param _MessageTTL: The MessageTTL parameter specifies settings dedicated to the classic type.
        :type MessageTTL: int
        :param _AutoExpire: The AutoExpire parameter, in milliseconds, indicates that the queue will be deleted if it is not used within a specified time.
        :type AutoExpire: int
        :param _MaxLength: MaxLength parameter. specifies the maximum number of entries the queue can hold. if the limit is exceeded, it will be handled according to the overview behavior.
        :type MaxLength: int
        :param _MaxLengthBytes: The MaxLengthBytes parameter specifies the maximum length in bytes. if the value exceeds the limit, it will be handled according to the overview behavior.
        :type MaxLengthBytes: int
        :param _DeliveryLimit: DeliveryLimit parameter. specifies the parameter dedicated to the quorum type.
        :type DeliveryLimit: int
        :param _OverflowBehaviour: OverflowBehaviour parameter specifies a value of drop-head, reject-publish, or reject-publish-dlx.
        :type OverflowBehaviour: str
        :param _DeadLetterExchange: The DeadLetterExchange parameter specifies that expired or rejected messages can be routed to a designated dead letter exchange.
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: The DeadLetterRoutingKey parameter specifies that it can only contain letters, digits, ".", "-", "@", and "_".
        :type DeadLetterRoutingKey: str
        :param _SingleActiveConsumer: The SingleActiveConsumer parameter. if enabled, ensure that there is only one consumer consuming from the queue every time.
        :type SingleActiveConsumer: bool
        :param _MaximumPriority: MaximumPriority parameter. specifies that it is dedicated for the classic type.
        :type MaximumPriority: int
        :param _LazyMode: LazyMode parameter. specifies that it is dedicated for the classic type.
        :type LazyMode: bool
        :param _MasterLocator: The MasterLocator parameter, dedicated to the classic type, specifies a value of min-masters, client-local, or random.
        :type MasterLocator: str
        :param _MaxInMemoryLength: MaxInMemoryLength parameter, dedicated for quorum type. specifies the maximum number of messages in memory for quorum queues.
        :type MaxInMemoryLength: int
        :param _MaxInMemoryBytes: The MaxInMemoryBytes parameter is dedicated to the quorum type. it specifies the maximum total message size in memory for quorum queues.
        :type MaxInMemoryBytes: int
        :param _Node: Node parameter. optional. specifies the node where the specified creation queue is located.
        :type Node: str
        :param _DeadLetterStrategy: Consistency policy for dead-letter in arbitrating queues. specifies valid values: at-most-once, at-least-once. at-most-once is selected by default.
        :type DeadLetterStrategy: str
        :param _QueueLeaderLocator: Specifies the leader election strategy for the arbitration queue. valid values are client-local and balanced. the default value is client-local.
        :type QueueLeaderLocator: str
        :param _QuorumInitialGroupSize: Specifies the initial replica group size of the arbitration queue. the default value is 3.
        :type QuorumInitialGroupSize: int
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._QueueType = None
        self._Durable = None
        self._AutoDelete = None
        self._Remark = None
        self._MessageTTL = None
        self._AutoExpire = None
        self._MaxLength = None
        self._MaxLengthBytes = None
        self._DeliveryLimit = None
        self._OverflowBehaviour = None
        self._DeadLetterExchange = None
        self._DeadLetterRoutingKey = None
        self._SingleActiveConsumer = None
        self._MaximumPriority = None
        self._LazyMode = None
        self._MasterLocator = None
        self._MaxInMemoryLength = None
        self._MaxInMemoryBytes = None
        self._Node = None
        self._DeadLetterStrategy = None
        self._QueueLeaderLocator = None
        self._QuorumInitialGroupSize = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""VHost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueType(self):
        r"""Supports only classic.
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Durable(self):
        r"""Durable flag. specifies that for the classic type, it must be passed in. for the quorum type, there is no need to pass it in and it is fixed as true.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Automatic cleanup. the classic type must be passed. the quorum type does not need to be passed and is fixed as false.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        r"""The MessageTTL parameter specifies settings dedicated to the classic type.
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def AutoExpire(self):
        r"""The AutoExpire parameter, in milliseconds, indicates that the queue will be deleted if it is not used within a specified time.
        :rtype: int
        """
        return self._AutoExpire

    @AutoExpire.setter
    def AutoExpire(self, AutoExpire):
        self._AutoExpire = AutoExpire

    @property
    def MaxLength(self):
        r"""MaxLength parameter. specifies the maximum number of entries the queue can hold. if the limit is exceeded, it will be handled according to the overview behavior.
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def MaxLengthBytes(self):
        r"""The MaxLengthBytes parameter specifies the maximum length in bytes. if the value exceeds the limit, it will be handled according to the overview behavior.
        :rtype: int
        """
        return self._MaxLengthBytes

    @MaxLengthBytes.setter
    def MaxLengthBytes(self, MaxLengthBytes):
        self._MaxLengthBytes = MaxLengthBytes

    @property
    def DeliveryLimit(self):
        r"""DeliveryLimit parameter. specifies the parameter dedicated to the quorum type.
        :rtype: int
        """
        return self._DeliveryLimit

    @DeliveryLimit.setter
    def DeliveryLimit(self, DeliveryLimit):
        self._DeliveryLimit = DeliveryLimit

    @property
    def OverflowBehaviour(self):
        r"""OverflowBehaviour parameter specifies a value of drop-head, reject-publish, or reject-publish-dlx.
        :rtype: str
        """
        return self._OverflowBehaviour

    @OverflowBehaviour.setter
    def OverflowBehaviour(self, OverflowBehaviour):
        self._OverflowBehaviour = OverflowBehaviour

    @property
    def DeadLetterExchange(self):
        r"""The DeadLetterExchange parameter specifies that expired or rejected messages can be routed to a designated dead letter exchange.
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        r"""The DeadLetterRoutingKey parameter specifies that it can only contain letters, digits, ".", "-", "@", and "_".
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey

    @property
    def SingleActiveConsumer(self):
        r"""The SingleActiveConsumer parameter. if enabled, ensure that there is only one consumer consuming from the queue every time.
        :rtype: bool
        """
        return self._SingleActiveConsumer

    @SingleActiveConsumer.setter
    def SingleActiveConsumer(self, SingleActiveConsumer):
        self._SingleActiveConsumer = SingleActiveConsumer

    @property
    def MaximumPriority(self):
        r"""MaximumPriority parameter. specifies that it is dedicated for the classic type.
        :rtype: int
        """
        return self._MaximumPriority

    @MaximumPriority.setter
    def MaximumPriority(self, MaximumPriority):
        self._MaximumPriority = MaximumPriority

    @property
    def LazyMode(self):
        r"""LazyMode parameter. specifies that it is dedicated for the classic type.
        :rtype: bool
        """
        return self._LazyMode

    @LazyMode.setter
    def LazyMode(self, LazyMode):
        self._LazyMode = LazyMode

    @property
    def MasterLocator(self):
        r"""The MasterLocator parameter, dedicated to the classic type, specifies a value of min-masters, client-local, or random.
        :rtype: str
        """
        return self._MasterLocator

    @MasterLocator.setter
    def MasterLocator(self, MasterLocator):
        self._MasterLocator = MasterLocator

    @property
    def MaxInMemoryLength(self):
        r"""MaxInMemoryLength parameter, dedicated for quorum type. specifies the maximum number of messages in memory for quorum queues.
        :rtype: int
        """
        return self._MaxInMemoryLength

    @MaxInMemoryLength.setter
    def MaxInMemoryLength(self, MaxInMemoryLength):
        self._MaxInMemoryLength = MaxInMemoryLength

    @property
    def MaxInMemoryBytes(self):
        r"""The MaxInMemoryBytes parameter is dedicated to the quorum type. it specifies the maximum total message size in memory for quorum queues.
        :rtype: int
        """
        return self._MaxInMemoryBytes

    @MaxInMemoryBytes.setter
    def MaxInMemoryBytes(self, MaxInMemoryBytes):
        self._MaxInMemoryBytes = MaxInMemoryBytes

    @property
    def Node(self):
        r"""Node parameter. optional. specifies the node where the specified creation queue is located.
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def DeadLetterStrategy(self):
        r"""Consistency policy for dead-letter in arbitrating queues. specifies valid values: at-most-once, at-least-once. at-most-once is selected by default.
        :rtype: str
        """
        return self._DeadLetterStrategy

    @DeadLetterStrategy.setter
    def DeadLetterStrategy(self, DeadLetterStrategy):
        self._DeadLetterStrategy = DeadLetterStrategy

    @property
    def QueueLeaderLocator(self):
        r"""Specifies the leader election strategy for the arbitration queue. valid values are client-local and balanced. the default value is client-local.
        :rtype: str
        """
        return self._QueueLeaderLocator

    @QueueLeaderLocator.setter
    def QueueLeaderLocator(self, QueueLeaderLocator):
        self._QueueLeaderLocator = QueueLeaderLocator

    @property
    def QuorumInitialGroupSize(self):
        r"""Specifies the initial replica group size of the arbitration queue. the default value is 3.
        :rtype: int
        """
        return self._QuorumInitialGroupSize

    @QuorumInitialGroupSize.setter
    def QuorumInitialGroupSize(self, QuorumInitialGroupSize):
        self._QuorumInitialGroupSize = QuorumInitialGroupSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._QueueType = params.get("QueueType")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Remark = params.get("Remark")
        self._MessageTTL = params.get("MessageTTL")
        self._AutoExpire = params.get("AutoExpire")
        self._MaxLength = params.get("MaxLength")
        self._MaxLengthBytes = params.get("MaxLengthBytes")
        self._DeliveryLimit = params.get("DeliveryLimit")
        self._OverflowBehaviour = params.get("OverflowBehaviour")
        self._DeadLetterExchange = params.get("DeadLetterExchange")
        self._DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        self._SingleActiveConsumer = params.get("SingleActiveConsumer")
        self._MaximumPriority = params.get("MaximumPriority")
        self._LazyMode = params.get("LazyMode")
        self._MasterLocator = params.get("MasterLocator")
        self._MaxInMemoryLength = params.get("MaxInMemoryLength")
        self._MaxInMemoryBytes = params.get("MaxInMemoryBytes")
        self._Node = params.get("Node")
        self._DeadLetterStrategy = params.get("DeadLetterStrategy")
        self._QueueLeaderLocator = params.get("QueueLeaderLocator")
        self._QuorumInitialGroupSize = params.get("QuorumInitialGroupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessQueueResponse(AbstractModel):
    r"""CreateRabbitMQServerlessQueue response structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

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
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessUserRequest(AbstractModel):
    r"""CreateRabbitMQServerlessUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username used when logging in.
        :type User: str
        :param _Password: Password. specifies the password used when logging in.
        :type Password: str
        :param _Description: Description
        :type Description: str
        :param _Tags: The serverless instance field is invalid.
        :type Tags: list of str
        :param _MaxConnections: Specifies the maximum number of connections for this user. if not specified, there is no limit.
        :type MaxConnections: int
        :param _MaxChannels: Specifies the maximum number of channels for the user. if not specified, there is no limit.
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username used when logging in.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""Password. specifies the password used when logging in.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""The serverless instance field is invalid.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MaxConnections(self):
        r"""Specifies the maximum number of connections for this user. if not specified, there is no limit.
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        r"""Specifies the maximum number of channels for the user. if not specified, there is no limit.
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessUserResponse(AbstractModel):
    r"""CreateRabbitMQServerlessUser response structure.

    """

    def __init__(self):
        r"""
        :param _User: Specifies the username used when logging in.
        :type User: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""Specifies the username used when logging in.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

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
        self._User = params.get("User")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessVirtualHostRequest(AbstractModel):
    r"""CreateRabbitMQServerlessVirtualHost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost name
        :type VirtualHost: str
        :param _Description: Description information
        :type Description: str
        :param _TraceFlag: Message trace switch. specifies that the value "true" turns it on, "false" turns it off. indicates that it is off by default.
        :type TraceFlag: bool
        :param _MirrorQueuePolicyFlag: Specifies whether to create a mirrored queue policy. the default value is true.
        :type MirrorQueuePolicyFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._TraceFlag = None
        self._MirrorQueuePolicyFlag = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost name
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        r"""Description information
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceFlag(self):
        r"""Message trace switch. specifies that the value "true" turns it on, "false" turns it off. indicates that it is off by default.
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag

    @property
    def MirrorQueuePolicyFlag(self):
        r"""Specifies whether to create a mirrored queue policy. the default value is true.
        :rtype: bool
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._TraceFlag = params.get("TraceFlag")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessVirtualHostResponse(AbstractModel):
    r"""CreateRabbitMQServerlessVirtualHost response structure.

    """

    def __init__(self):
        r"""
        :param _VirtualHost: Vhost name
        :type VirtualHost: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VirtualHost = None
        self._RequestId = None

    @property
    def VirtualHost(self):
        r"""Vhost name
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

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
        self._VirtualHost = params.get("VirtualHost")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessBindingRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessBinding request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _BindingId: binding relationship Id.
        :type BindingId: int
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        r"""binding relationship Id.
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessBindingResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessBinding response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Queue name.
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost parameter.
        :type VirtualHost: str
        :param _BindingId: binding relationship Id.
        :type BindingId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Queue name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        r"""binding relationship Id.
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

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
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessExchangeRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessExchange request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost parameter.
        :type VirtualHost: str
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None

    @property
    def InstanceId(self):
        r"""Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessExchangeResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessExchange response structure.

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

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
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessPermissionRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessPermission request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username used when logging in.
        :type User: str
        :param _VirtualHost: Specifies the vhost name.
        :type VirtualHost: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username used when logging in.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessPermissionResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessPermission response structure.

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


class DeleteRabbitMQServerlessQueueRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessQueue request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessQueueResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessQueue response structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

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
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessUserRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username used when logging in.
        :type User: str
        """
        self._InstanceId = None
        self._User = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username used when logging in.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessUserResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessUser response structure.

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


class DeleteRabbitMQServerlessVirtualHostRequest(AbstractModel):
    r"""DeleteRabbitMQServerlessVirtualHost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost name.
        :type VirtualHost: str
        """
        self._InstanceId = None
        self._VirtualHost = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessVirtualHostResponse(AbstractModel):
    r"""DeleteRabbitMQServerlessVirtualHost response structure.

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


class DescribeRabbitMQServerlessBindingsRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessBindings request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance Id</p>
        :type InstanceId: str
        :param _VirtualHost: <p>Vhost parameter</p>
        :type VirtualHost: str
        :param _Offset: <p>Pagination offset</p>
        :type Offset: int
        :param _Limit: <p>Pagination limit</p>
        :type Limit: int
        :param _SearchWord: <p>Search keywords, do fuzzy search based on source exchange name/target resource name</p>
        :type SearchWord: str
        :param _SourceExchange: <p>Precise search and filter based on source Exchange</p>
        :type SourceExchange: str
        :param _QueueName: <p>Precise search filter based on target QueueName and DestinationExchange cannot be set both at the same time</p>
        :type QueueName: str
        :param _DestinationExchange: <p>Precise search filter based on target Exchange and QueueName filter cannot be set both at the same time</p>
        :type DestinationExchange: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._SourceExchange = None
        self._QueueName = None
        self._DestinationExchange = None

    @property
    def InstanceId(self):
        r"""<p>Instance Id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""<p>Vhost parameter</p>
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        r"""<p>Pagination offset</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Pagination limit</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        r"""<p>Search keywords, do fuzzy search based on source exchange name/target resource name</p>
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def SourceExchange(self):
        r"""<p>Precise search and filter based on source Exchange</p>
        :rtype: str
        """
        return self._SourceExchange

    @SourceExchange.setter
    def SourceExchange(self, SourceExchange):
        self._SourceExchange = SourceExchange

    @property
    def QueueName(self):
        r"""<p>Precise search filter based on target QueueName and DestinationExchange cannot be set both at the same time</p>
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def DestinationExchange(self):
        r"""<p>Precise search filter based on target Exchange and QueueName filter cannot be set both at the same time</p>
        :rtype: str
        """
        return self._DestinationExchange

    @DestinationExchange.setter
    def DestinationExchange(self, DestinationExchange):
        self._DestinationExchange = DestinationExchange


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._SourceExchange = params.get("SourceExchange")
        self._QueueName = params.get("QueueName")
        self._DestinationExchange = params.get("DestinationExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessBindingsResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessBindings response structure.

    """

    def __init__(self):
        r"""
        :param _BindingInfoList: <p>Route relationship list</p>
        :type BindingInfoList: list of RabbitMQBindingListInfo
        :param _TotalCount: <p>Quantity</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BindingInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BindingInfoList(self):
        r"""<p>Route relationship list</p>
        :rtype: list of RabbitMQBindingListInfo
        """
        return self._BindingInfoList

    @BindingInfoList.setter
    def BindingInfoList(self, BindingInfoList):
        self._BindingInfoList = BindingInfoList

    @property
    def TotalCount(self):
        r"""<p>Quantity</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("BindingInfoList") is not None:
            self._BindingInfoList = []
            for item in params.get("BindingInfoList"):
                obj = RabbitMQBindingListInfo()
                obj._deserialize(item)
                self._BindingInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessConnectionRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessConnection request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID		
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost name.
        :type VirtualHost: str
        :param _SortElement: Sort by which field. Supported values: channel (number of channels), incoming_bytes (inbound traffic volume), outgoing_bytes (outbound traffic volume).
        :type SortElement: str
        :param _SortType: Sorting method: ASC, DESC
        :type SortType: str
        :param _Offset: Pagination parameters, started from which data entry
        :type Offset: int
        :param _Limit: Page size.
        :type Limit: int
        :param _Name: Connection name fuzzy search
        :type Name: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._SortElement = None
        self._SortType = None
        self._Offset = None
        self._Limit = None
        self._Name = None

    @property
    def InstanceId(self):
        r"""instance ID		
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def SortElement(self):
        r"""Sort by which field. Supported values: channel (number of channels), incoming_bytes (inbound traffic volume), outgoing_bytes (outbound traffic volume).
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortType(self):
        r"""Sorting method: ASC, DESC
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        r"""Pagination parameters, started from which data entry
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Page size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        r"""Connection name fuzzy search
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._SortElement = params.get("SortElement")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessConnectionResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessConnection response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Return the number of connections.
        :type TotalCount: int
        :param _Connections: List of connection details.
        :type Connections: list of RabbitMQConnection
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Connections = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Return the number of connections.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Connections(self):
        r"""List of connection details.
        :rtype: list of RabbitMQConnection
        """
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Connections") is not None:
            self._Connections = []
            for item in params.get("Connections"):
                obj = RabbitMQConnection()
                obj._deserialize(item)
                self._Connections.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessConsumersRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessConsumers request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _SearchWord: Search keywords
        :type SearchWord: str
        :param _Channel: channelId
        :type Channel: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._Limit = None
        self._Offset = None
        self._SearchWord = None
        self._Channel = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Limit(self):
        r"""Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SearchWord(self):
        r"""Search keywords
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Channel(self):
        r"""channelId
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SearchWord = params.get("SearchWord")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessConsumersResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessConsumers response structure.

    """

    def __init__(self):
        r"""
        :param _ConsumerInfoList: Consumer list information.
        :type ConsumerInfoList: list of RabbitMQConsumersListInfo
        :param _TotalCount: Quantity
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConsumerInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConsumerInfoList(self):
        r"""Consumer list information.
        :rtype: list of RabbitMQConsumersListInfo
        """
        return self._ConsumerInfoList

    @ConsumerInfoList.setter
    def ConsumerInfoList(self, ConsumerInfoList):
        self._ConsumerInfoList = ConsumerInfoList

    @property
    def TotalCount(self):
        r"""Quantity
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ConsumerInfoList") is not None:
            self._ConsumerInfoList = []
            for item in params.get("ConsumerInfoList"):
                obj = RabbitMQConsumersListInfo()
                obj._deserialize(item)
                self._ConsumerInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessExchangeDetailRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessExchangeDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost parameter.
        :type VirtualHost: str
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None

    @property
    def InstanceId(self):
        r"""Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessExchangeDetailResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessExchangeDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _Durable: Specifies whether it is a persistent exchange. when the cluster restarts, all exchanges with this field set to "false" will be cleared.
        :type Durable: bool
        :param _AutoDelete: Whether to auto-delete this exchange. if set to "true", the exchange will be automatically deleted when all routing relationships on the current exchange are unbound.
        :type AutoDelete: bool
        :param _Internal: Specifies whether it is an internal exchange. if set to "true", messages cannot be directly delivered to this exchange. they need to be forwarded through another exchange in the routing settings.
        :type Internal: bool
        :param _AlternateExchange: Alternative exchange. if a message does not match all queues or exchanges bound to the current exchange, it will be sent to this alternative exchange.
        :type AlternateExchange: str
        :param _ExchangeType: Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :type ExchangeType: str
        :param _VirtualHost: VHost parameter.
        :type VirtualHost: str
        :param _ExchangeCreator: exchange creator. valid values: `system` (generated by the system), `user` (user-created).
        :type ExchangeCreator: str
        :param _Arguments: Additional parameters key-value string.
        :type Arguments: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExchangeName = None
        self._Remark = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._AlternateExchange = None
        self._ExchangeType = None
        self._VirtualHost = None
        self._ExchangeCreator = None
        self._Arguments = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Durable(self):
        r"""Specifies whether it is a persistent exchange. when the cluster restarts, all exchanges with this field set to "false" will be cleared.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Whether to auto-delete this exchange. if set to "true", the exchange will be automatically deleted when all routing relationships on the current exchange are unbound.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        r"""Specifies whether it is an internal exchange. if set to "true", messages cannot be directly delivered to this exchange. they need to be forwarded through another exchange in the routing settings.
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def AlternateExchange(self):
        r"""Alternative exchange. if a message does not match all queues or exchanges bound to the current exchange, it will be sent to this alternative exchange.
        :rtype: str
        """
        return self._AlternateExchange

    @AlternateExchange.setter
    def AlternateExchange(self, AlternateExchange):
        self._AlternateExchange = AlternateExchange

    @property
    def ExchangeType(self):
        r"""Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def VirtualHost(self):
        r"""VHost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeCreator(self):
        r"""exchange creator. valid values: `system` (generated by the system), `user` (user-created).
        :rtype: str
        """
        return self._ExchangeCreator

    @ExchangeCreator.setter
    def ExchangeCreator(self, ExchangeCreator):
        self._ExchangeCreator = ExchangeCreator

    @property
    def Arguments(self):
        r"""Additional parameters key-value string.
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

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
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._AlternateExchange = params.get("AlternateExchange")
        self._ExchangeType = params.get("ExchangeType")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeCreator = params.get("ExchangeCreator")
        self._Arguments = params.get("Arguments")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessExchangesRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessExchanges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost parameter.
        :type VirtualHost: str
        :param _Offset: Paging offset.
        :type Offset: int
        :param _Limit: Paginate limit.
        :type Limit: int
        :param _SearchWord: Search keywords support fuzzy matching.
        :type SearchWord: str
        :param _ExchangeTypeFilters: Specifies the filter type for each selected element in the array of exchange types.
        :type ExchangeTypeFilters: list of str
        :param _ExchangeCreatorFilters: Specifies the exchange creation source. valid values: "system" (generated by the system), "user" (user-created).
        :type ExchangeCreatorFilters: list of str
        :param _ExchangeName: exchange name. specifies that it is used for exact matching.
        :type ExchangeName: str
        :param _SortElement: Sorting field.
MessageRateInOut specifies the total production and consumption rate.
MessageRateIn specifies the production rate.
MessageRateOut specifies the consumption rate.
        :type SortElement: str
        :param _SortOrder: Sort order. valid values: ascend or descend.
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._ExchangeTypeFilters = None
        self._ExchangeCreatorFilters = None
        self._ExchangeName = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        r"""Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        r"""Paging offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Paginate limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        r"""Search keywords support fuzzy matching.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def ExchangeTypeFilters(self):
        r"""Specifies the filter type for each selected element in the array of exchange types.
        :rtype: list of str
        """
        return self._ExchangeTypeFilters

    @ExchangeTypeFilters.setter
    def ExchangeTypeFilters(self, ExchangeTypeFilters):
        self._ExchangeTypeFilters = ExchangeTypeFilters

    @property
    def ExchangeCreatorFilters(self):
        r"""Specifies the exchange creation source. valid values: "system" (generated by the system), "user" (user-created).
        :rtype: list of str
        """
        return self._ExchangeCreatorFilters

    @ExchangeCreatorFilters.setter
    def ExchangeCreatorFilters(self, ExchangeCreatorFilters):
        self._ExchangeCreatorFilters = ExchangeCreatorFilters

    @property
    def ExchangeName(self):
        r"""exchange name. specifies that it is used for exact matching.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def SortElement(self):
        r"""Sorting field.
MessageRateInOut specifies the total production and consumption rate.
MessageRateIn specifies the production rate.
MessageRateOut specifies the consumption rate.
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        r"""Sort order. valid values: ascend or descend.
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._ExchangeTypeFilters = params.get("ExchangeTypeFilters")
        self._ExchangeCreatorFilters = params.get("ExchangeCreatorFilters")
        self._ExchangeName = params.get("ExchangeName")
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessExchangesResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessExchanges response structure.

    """

    def __init__(self):
        r"""
        :param _ExchangeInfoList: exchanges list.
        :type ExchangeInfoList: list of RabbitMQExchangeListInfo
        :param _TotalCount: Total count of exchanges.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExchangeInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ExchangeInfoList(self):
        r"""exchanges list.
        :rtype: list of RabbitMQExchangeListInfo
        """
        return self._ExchangeInfoList

    @ExchangeInfoList.setter
    def ExchangeInfoList(self, ExchangeInfoList):
        self._ExchangeInfoList = ExchangeInfoList

    @property
    def TotalCount(self):
        r"""Total count of exchanges.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ExchangeInfoList") is not None:
            self._ExchangeInfoList = []
            for item in params.get("ExchangeInfoList"):
                obj = RabbitMQExchangeListInfo()
                obj._deserialize(item)
                self._ExchangeInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessInstanceRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessInstanceResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessInstance response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: Cluster information.
        :type ClusterInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterInfo`
        :param _ClusterSpecInfo: Specifies the cluster specification information.
        :type ClusterSpecInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterSpecInfo`
        :param _VirtualHostQuota: Specifies the quota information of the vhost.
        :type VirtualHostQuota: :class:`tencentcloud.trabbit.v20230418.models.VirtualHostQuota`
        :param _ExchangeQuota: Specifies the exchange quota information.
        :type ExchangeQuota: :class:`tencentcloud.trabbit.v20230418.models.ExchangeQuota`
        :param _QueueQuota: Specifies the quota information of the queue.
        :type QueueQuota: :class:`tencentcloud.trabbit.v20230418.models.QueueQuota`
        :param _ClusterNetInfo: Network information.
        :type ClusterNetInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessAccessInfo`
        :param _ClusterWhiteListInfo: Public network allowlist information.
        :type ClusterWhiteListInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessWhiteListInfo`
        :param _UserQuota: Specifies the quota information of the user.
        :type UserQuota: :class:`tencentcloud.trabbit.v20230418.models.UserQuota`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._ClusterSpecInfo = None
        self._VirtualHostQuota = None
        self._ExchangeQuota = None
        self._QueueQuota = None
        self._ClusterNetInfo = None
        self._ClusterWhiteListInfo = None
        self._UserQuota = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        r"""Cluster information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def ClusterSpecInfo(self):
        r"""Specifies the cluster specification information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterSpecInfo`
        """
        return self._ClusterSpecInfo

    @ClusterSpecInfo.setter
    def ClusterSpecInfo(self, ClusterSpecInfo):
        self._ClusterSpecInfo = ClusterSpecInfo

    @property
    def VirtualHostQuota(self):
        r"""Specifies the quota information of the vhost.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.VirtualHostQuota`
        """
        return self._VirtualHostQuota

    @VirtualHostQuota.setter
    def VirtualHostQuota(self, VirtualHostQuota):
        self._VirtualHostQuota = VirtualHostQuota

    @property
    def ExchangeQuota(self):
        r"""Specifies the exchange quota information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ExchangeQuota`
        """
        return self._ExchangeQuota

    @ExchangeQuota.setter
    def ExchangeQuota(self, ExchangeQuota):
        self._ExchangeQuota = ExchangeQuota

    @property
    def QueueQuota(self):
        r"""Specifies the quota information of the queue.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.QueueQuota`
        """
        return self._QueueQuota

    @QueueQuota.setter
    def QueueQuota(self, QueueQuota):
        self._QueueQuota = QueueQuota

    @property
    def ClusterNetInfo(self):
        r"""Network information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessAccessInfo`
        """
        return self._ClusterNetInfo

    @ClusterNetInfo.setter
    def ClusterNetInfo(self, ClusterNetInfo):
        self._ClusterNetInfo = ClusterNetInfo

    @property
    def ClusterWhiteListInfo(self):
        r"""Public network allowlist information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessWhiteListInfo`
        """
        return self._ClusterWhiteListInfo

    @ClusterWhiteListInfo.setter
    def ClusterWhiteListInfo(self, ClusterWhiteListInfo):
        self._ClusterWhiteListInfo = ClusterWhiteListInfo

    @property
    def UserQuota(self):
        r"""Specifies the quota information of the user.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.UserQuota`
        """
        return self._UserQuota

    @UserQuota.setter
    def UserQuota(self, UserQuota):
        self._UserQuota = UserQuota

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
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = RabbitMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterSpecInfo") is not None:
            self._ClusterSpecInfo = RabbitMQClusterSpecInfo()
            self._ClusterSpecInfo._deserialize(params.get("ClusterSpecInfo"))
        if params.get("VirtualHostQuota") is not None:
            self._VirtualHostQuota = VirtualHostQuota()
            self._VirtualHostQuota._deserialize(params.get("VirtualHostQuota"))
        if params.get("ExchangeQuota") is not None:
            self._ExchangeQuota = ExchangeQuota()
            self._ExchangeQuota._deserialize(params.get("ExchangeQuota"))
        if params.get("QueueQuota") is not None:
            self._QueueQuota = QueueQuota()
            self._QueueQuota._deserialize(params.get("QueueQuota"))
        if params.get("ClusterNetInfo") is not None:
            self._ClusterNetInfo = RabbitMQServerlessAccessInfo()
            self._ClusterNetInfo._deserialize(params.get("ClusterNetInfo"))
        if params.get("ClusterWhiteListInfo") is not None:
            self._ClusterWhiteListInfo = RabbitMQServerlessWhiteListInfo()
            self._ClusterWhiteListInfo._deserialize(params.get("ClusterWhiteListInfo"))
        if params.get("UserQuota") is not None:
            self._UserQuota = UserQuota()
            self._UserQuota._deserialize(params.get("UserQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessPermissionRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessPermission request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID.
        :type InstanceId: str
        :param _User: Specifies the username for query filtering. if not provided, all will be queried.
        :type User: str
        :param _VirtualHost: Specifies the vhost name. used for query filtering. if it is not provided, query all.
        :type VirtualHost: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Pagination limit
        :type Limit: int
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username for query filtering. if not provided, all will be queried.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name. used for query filtering. if it is not provided, query all.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        r"""Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessPermissionResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessPermission response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Return the number of permissions.
        :type TotalCount: int
        :param _RabbitMQPermissionList: List of permission details.
        :type RabbitMQPermissionList: list of RabbitMQPermission
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RabbitMQPermissionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Return the number of permissions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RabbitMQPermissionList(self):
        r"""List of permission details.
        :rtype: list of RabbitMQPermission
        """
        return self._RabbitMQPermissionList

    @RabbitMQPermissionList.setter
    def RabbitMQPermissionList(self, RabbitMQPermissionList):
        self._RabbitMQPermissionList = RabbitMQPermissionList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("RabbitMQPermissionList") is not None:
            self._RabbitMQPermissionList = []
            for item in params.get("RabbitMQPermissionList"):
                obj = RabbitMQPermission()
                obj._deserialize(item)
                self._RabbitMQPermissionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessQueueDetailRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessQueueDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessQueueDetailResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessQueueDetail response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _QueueType: Specifies the queue type. the valid values are classic or quorum.
        :type QueueType: str
        :param _Consumers: Number of online consumers.
        :type Consumers: int
        :param _Durable: Durable flag.
        :type Durable: bool
        :param _AutoDelete: Automatic cleanup.
        :type AutoDelete: bool
        :param _Remark: Remarks
        :type Remark: str
        :param _MessageTTL: MessageTTL parameter, dedicated for classic type.
        :type MessageTTL: int
        :param _AutoExpire: AutoExpire parameter.
        :type AutoExpire: int
        :param _MaxLength: MaxLength parameter.
        :type MaxLength: int
        :param _MaxLengthBytes: MaxLengthBytes parameter.
        :type MaxLengthBytes: int
        :param _DeliveryLimit: DeliveryLimit parameter. specifies the parameter dedicated to the quorum type.
        :type DeliveryLimit: int
        :param _OverflowBehaviour: OverflowBehaviour parameter specifies a value of drop-head, reject-publish, or reject-publish-dlx.
        :type OverflowBehaviour: str
        :param _DeadLetterExchange: DeadLetterExchange parameter.
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: The DeadLetterRoutingKey parameter.
        :type DeadLetterRoutingKey: str
        :param _SingleActiveConsumer: SingleActiveConsumer parameter.
        :type SingleActiveConsumer: bool
        :param _MaximumPriority: MaximumPriority parameter. specifies that it is dedicated for the classic type.
        :type MaximumPriority: int
        :param _LazyMode: LazyMode parameter, dedicated for classic type.
        :type LazyMode: bool
        :param _MasterLocator: MasterLocator parameter, dedicated for classic type.
        :type MasterLocator: str
        :param _MaxInMemoryLength: MaxInMemoryLength parameter, dedicated for quorum type.
        :type MaxInMemoryLength: int
        :param _MaxInMemoryBytes: The MaxInMemoryBytes parameter is dedicated to the quorum type.
        :type MaxInMemoryBytes: int
        :param _CreateTime: Create timestamp, in seconds.
        :type CreateTime: int
        :param _Node: Node.
        :type Node: str
        :param _DeadLetterStrategy: Arbitration queue dead letter consistency policy.
        :type DeadLetterStrategy: str
        :param _QueueLeaderLocator: Leadership election policy for arbitration queue.
        :type QueueLeaderLocator: str
        :param _QuorumInitialGroupSize: Specifies the initial replica group size of the arbitration queue.
        :type QuorumInitialGroupSize: int
        :param _Exclusive: Whether it is an exclusive queue.
        :type Exclusive: bool
        :param _Policy: The name of the policy that takes effect.
        :type Policy: str
        :param _Arguments: Additional parameters key-value.
        :type Arguments: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._QueueType = None
        self._Consumers = None
        self._Durable = None
        self._AutoDelete = None
        self._Remark = None
        self._MessageTTL = None
        self._AutoExpire = None
        self._MaxLength = None
        self._MaxLengthBytes = None
        self._DeliveryLimit = None
        self._OverflowBehaviour = None
        self._DeadLetterExchange = None
        self._DeadLetterRoutingKey = None
        self._SingleActiveConsumer = None
        self._MaximumPriority = None
        self._LazyMode = None
        self._MasterLocator = None
        self._MaxInMemoryLength = None
        self._MaxInMemoryBytes = None
        self._CreateTime = None
        self._Node = None
        self._DeadLetterStrategy = None
        self._QueueLeaderLocator = None
        self._QuorumInitialGroupSize = None
        self._Exclusive = None
        self._Policy = None
        self._Arguments = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueType(self):
        r"""Specifies the queue type. the valid values are classic or quorum.
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Consumers(self):
        r"""Number of online consumers.
        :rtype: int
        """
        return self._Consumers

    @Consumers.setter
    def Consumers(self, Consumers):
        self._Consumers = Consumers

    @property
    def Durable(self):
        r"""Durable flag.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Automatic cleanup.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        r"""MessageTTL parameter, dedicated for classic type.
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def AutoExpire(self):
        r"""AutoExpire parameter.
        :rtype: int
        """
        return self._AutoExpire

    @AutoExpire.setter
    def AutoExpire(self, AutoExpire):
        self._AutoExpire = AutoExpire

    @property
    def MaxLength(self):
        r"""MaxLength parameter.
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def MaxLengthBytes(self):
        r"""MaxLengthBytes parameter.
        :rtype: int
        """
        return self._MaxLengthBytes

    @MaxLengthBytes.setter
    def MaxLengthBytes(self, MaxLengthBytes):
        self._MaxLengthBytes = MaxLengthBytes

    @property
    def DeliveryLimit(self):
        r"""DeliveryLimit parameter. specifies the parameter dedicated to the quorum type.
        :rtype: int
        """
        return self._DeliveryLimit

    @DeliveryLimit.setter
    def DeliveryLimit(self, DeliveryLimit):
        self._DeliveryLimit = DeliveryLimit

    @property
    def OverflowBehaviour(self):
        r"""OverflowBehaviour parameter specifies a value of drop-head, reject-publish, or reject-publish-dlx.
        :rtype: str
        """
        return self._OverflowBehaviour

    @OverflowBehaviour.setter
    def OverflowBehaviour(self, OverflowBehaviour):
        self._OverflowBehaviour = OverflowBehaviour

    @property
    def DeadLetterExchange(self):
        r"""DeadLetterExchange parameter.
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        r"""The DeadLetterRoutingKey parameter.
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey

    @property
    def SingleActiveConsumer(self):
        r"""SingleActiveConsumer parameter.
        :rtype: bool
        """
        return self._SingleActiveConsumer

    @SingleActiveConsumer.setter
    def SingleActiveConsumer(self, SingleActiveConsumer):
        self._SingleActiveConsumer = SingleActiveConsumer

    @property
    def MaximumPriority(self):
        r"""MaximumPriority parameter. specifies that it is dedicated for the classic type.
        :rtype: int
        """
        return self._MaximumPriority

    @MaximumPriority.setter
    def MaximumPriority(self, MaximumPriority):
        self._MaximumPriority = MaximumPriority

    @property
    def LazyMode(self):
        r"""LazyMode parameter, dedicated for classic type.
        :rtype: bool
        """
        return self._LazyMode

    @LazyMode.setter
    def LazyMode(self, LazyMode):
        self._LazyMode = LazyMode

    @property
    def MasterLocator(self):
        r"""MasterLocator parameter, dedicated for classic type.
        :rtype: str
        """
        return self._MasterLocator

    @MasterLocator.setter
    def MasterLocator(self, MasterLocator):
        self._MasterLocator = MasterLocator

    @property
    def MaxInMemoryLength(self):
        r"""MaxInMemoryLength parameter, dedicated for quorum type.
        :rtype: int
        """
        return self._MaxInMemoryLength

    @MaxInMemoryLength.setter
    def MaxInMemoryLength(self, MaxInMemoryLength):
        self._MaxInMemoryLength = MaxInMemoryLength

    @property
    def MaxInMemoryBytes(self):
        r"""The MaxInMemoryBytes parameter is dedicated to the quorum type.
        :rtype: int
        """
        return self._MaxInMemoryBytes

    @MaxInMemoryBytes.setter
    def MaxInMemoryBytes(self, MaxInMemoryBytes):
        self._MaxInMemoryBytes = MaxInMemoryBytes

    @property
    def CreateTime(self):
        r"""Create timestamp, in seconds.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Node(self):
        r"""Node.
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def DeadLetterStrategy(self):
        r"""Arbitration queue dead letter consistency policy.
        :rtype: str
        """
        return self._DeadLetterStrategy

    @DeadLetterStrategy.setter
    def DeadLetterStrategy(self, DeadLetterStrategy):
        self._DeadLetterStrategy = DeadLetterStrategy

    @property
    def QueueLeaderLocator(self):
        r"""Leadership election policy for arbitration queue.
        :rtype: str
        """
        return self._QueueLeaderLocator

    @QueueLeaderLocator.setter
    def QueueLeaderLocator(self, QueueLeaderLocator):
        self._QueueLeaderLocator = QueueLeaderLocator

    @property
    def QuorumInitialGroupSize(self):
        r"""Specifies the initial replica group size of the arbitration queue.
        :rtype: int
        """
        return self._QuorumInitialGroupSize

    @QuorumInitialGroupSize.setter
    def QuorumInitialGroupSize(self, QuorumInitialGroupSize):
        self._QuorumInitialGroupSize = QuorumInitialGroupSize

    @property
    def Exclusive(self):
        r"""Whether it is an exclusive queue.
        :rtype: bool
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def Policy(self):
        r"""The name of the policy that takes effect.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        r"""Additional parameters key-value.
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

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
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._QueueType = params.get("QueueType")
        self._Consumers = params.get("Consumers")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Remark = params.get("Remark")
        self._MessageTTL = params.get("MessageTTL")
        self._AutoExpire = params.get("AutoExpire")
        self._MaxLength = params.get("MaxLength")
        self._MaxLengthBytes = params.get("MaxLengthBytes")
        self._DeliveryLimit = params.get("DeliveryLimit")
        self._OverflowBehaviour = params.get("OverflowBehaviour")
        self._DeadLetterExchange = params.get("DeadLetterExchange")
        self._DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        self._SingleActiveConsumer = params.get("SingleActiveConsumer")
        self._MaximumPriority = params.get("MaximumPriority")
        self._LazyMode = params.get("LazyMode")
        self._MasterLocator = params.get("MasterLocator")
        self._MaxInMemoryLength = params.get("MaxInMemoryLength")
        self._MaxInMemoryBytes = params.get("MaxInMemoryBytes")
        self._CreateTime = params.get("CreateTime")
        self._Node = params.get("Node")
        self._DeadLetterStrategy = params.get("DeadLetterStrategy")
        self._QueueLeaderLocator = params.get("QueueLeaderLocator")
        self._QuorumInitialGroupSize = params.get("QuorumInitialGroupSize")
        self._Exclusive = params.get("Exclusive")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessQueuesRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessQueues request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance Id</p>
        :type InstanceId: str
        :param _VirtualHost: <p>Vhost parameter</p>
        :type VirtualHost: str
        :param _Offset: <p>Pagination offset.</p>
        :type Offset: int
        :param _Limit: <p>Pagination limit.</p>
        :type Limit: int
        :param _SearchWord: <p>Search keyword</p>
        :type SearchWord: str
        :param _QueueType: <p>Queue type filter criteria. Leave blank or use "all" for classic and quorum queues; "classic" for classic queues; "quorum" for quorum queues.</p>
        :type QueueType: str
        :param _SortElement: <p>Sorting field:<br>messages_ready - message backlog;<br>publish - production rate;<br>deliver - consumption rate;<br>consumers - number of online consumers;</p>
        :type SortElement: str
        :param _SortOrder: <p>Sort order, asc or desc</p>
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._QueueType = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        r"""<p>Instance Id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""<p>Vhost parameter</p>
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        r"""<p>Pagination offset.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Pagination limit.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        r"""<p>Search keyword</p>
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def QueueType(self):
        r"""<p>Queue type filter criteria. Leave blank or use "all" for classic and quorum queues; "classic" for classic queues; "quorum" for quorum queues.</p>
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def SortElement(self):
        r"""<p>Sorting field:<br>messages_ready - message backlog;<br>publish - production rate;<br>deliver - consumption rate;<br>consumers - number of online consumers;</p>
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        r"""<p>Sort order, asc or desc</p>
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._QueueType = params.get("QueueType")
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessQueuesResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessQueues response structure.

    """

    def __init__(self):
        r"""
        :param _QueueInfoList: <p>Queue list info</p>
        :type QueueInfoList: list of RabbitMQQueueListInfo
        :param _TotalCount: <p>Quantity</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def QueueInfoList(self):
        r"""<p>Queue list info</p>
        :rtype: list of RabbitMQQueueListInfo
        """
        return self._QueueInfoList

    @QueueInfoList.setter
    def QueueInfoList(self, QueueInfoList):
        self._QueueInfoList = QueueInfoList

    @property
    def TotalCount(self):
        r"""<p>Quantity</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("QueueInfoList") is not None:
            self._QueueInfoList = []
            for item in params.get("QueueInfoList"):
                obj = RabbitMQQueueListInfo()
                obj._deserialize(item)
                self._QueueInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessUserRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _SearchUser: Retrieves usernames. supports prefix match and suffix matching.
        :type SearchUser: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Pagination limit
        :type Limit: int
        :param _User: Specifies the username for an exact query.
        :type User: str
        :param _Tags: User tag. filters by Tag filter list.
        :type Tags: list of str
        """
        self._InstanceId = None
        self._SearchUser = None
        self._Offset = None
        self._Limit = None
        self._User = None
        self._Tags = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchUser(self):
        r"""Retrieves usernames. supports prefix match and suffix matching.
        :rtype: str
        """
        return self._SearchUser

    @SearchUser.setter
    def SearchUser(self, SearchUser):
        self._SearchUser = SearchUser

    @property
    def Offset(self):
        r"""Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def User(self):
        r"""Specifies the username for an exact query.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tags(self):
        r"""User tag. filters by Tag filter list.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchUser = params.get("SearchUser")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._User = params.get("User")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessUserResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessUser response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of returned users.
        :type TotalCount: int
        :param _RabbitMQUserList: Currently created RabbitMQ list of users.
        :type RabbitMQUserList: list of RabbitMQUser
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RabbitMQUserList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The number of returned users.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RabbitMQUserList(self):
        r"""Currently created RabbitMQ list of users.
        :rtype: list of RabbitMQUser
        """
        return self._RabbitMQUserList

    @RabbitMQUserList.setter
    def RabbitMQUserList(self, RabbitMQUserList):
        self._RabbitMQUserList = RabbitMQUserList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("RabbitMQUserList") is not None:
            self._RabbitMQUserList = []
            for item in params.get("RabbitMQUserList"):
                obj = RabbitMQUser()
                obj._deserialize(item)
                self._RabbitMQUserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessVirtualHostRequest(AbstractModel):
    r"""DescribeRabbitMQServerlessVirtualHost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost name. if it is not provided, query all.
        :type VirtualHost: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Filters: search-virtual-host: specifies fuzzy name search of vhost names. earlier, it supported both prefix and suffix matching.
        :type Filters: :class:`tencentcloud.trabbit.v20230418.models.Filter`
        :param _SortElement: Sorting field.
MessageHeapCount specifies the number of message backlogs.
MessageRateInOut specifies the total production and consumption rate.
MessageRateIn specifies the production rate.
MessageRateOut specifies the consumption rate.
        :type SortElement: str
        :param _SortOrder: Sort order. valid values: ascend or descend.
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name. if it is not provided, query all.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        r"""Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""search-virtual-host: specifies fuzzy name search of vhost names. earlier, it supported both prefix and suffix matching.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.Filter`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortElement(self):
        r"""Sorting field.
MessageHeapCount specifies the number of message backlogs.
MessageRateInOut specifies the total production and consumption rate.
MessageRateIn specifies the production rate.
MessageRateOut specifies the consumption rate.
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        r"""Sort order. valid values: ascend or descend.
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = Filter()
            self._Filters._deserialize(params.get("Filters"))
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessVirtualHostResponse(AbstractModel):
    r"""DescribeRabbitMQServerlessVirtualHost response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Return the number of vhosts.
        :type TotalCount: int
        :param _VirtualHostList: Specifies the list of details of the vhost.
        :type VirtualHostList: list of RabbitMQVirtualHostInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VirtualHostList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Return the number of vhosts.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VirtualHostList(self):
        r"""Specifies the list of details of the vhost.
        :rtype: list of RabbitMQVirtualHostInfo
        """
        return self._VirtualHostList

    @VirtualHostList.setter
    def VirtualHostList(self, VirtualHostList):
        self._VirtualHostList = VirtualHostList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("VirtualHostList") is not None:
            self._VirtualHostList = []
            for item in params.get("VirtualHostList"):
                obj = RabbitMQVirtualHostInfo()
                obj._deserialize(item)
                self._VirtualHostList.append(obj)
        self._RequestId = params.get("RequestId")


class ExchangeQuota(AbstractModel):
    r"""Specifies the exchange usage quota information.

    """

    def __init__(self):
        r"""
        :param _MaxExchange: Specifies the maximum number of exchanges that can be created.
        :type MaxExchange: int
        :param _UsedExchange: Specifies the number of exchanges that have been created.
        :type UsedExchange: int
        """
        self._MaxExchange = None
        self._UsedExchange = None

    @property
    def MaxExchange(self):
        r"""Specifies the maximum number of exchanges that can be created.
        :rtype: int
        """
        return self._MaxExchange

    @MaxExchange.setter
    def MaxExchange(self, MaxExchange):
        self._MaxExchange = MaxExchange

    @property
    def UsedExchange(self):
        r"""Specifies the number of exchanges that have been created.
        :rtype: int
        """
        return self._UsedExchange

    @UsedExchange.setter
    def UsedExchange(self, UsedExchange):
        self._UsedExchange = UsedExchange


    def _deserialize(self, params):
        self._MaxExchange = params.get("MaxExchange")
        self._UsedExchange = params.get("UsedExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Filter parameter

    """

    def __init__(self):
        r"""
        :param _Name: name.
        :type Name: str
        :param _Values: Value.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Value.
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
        


class ListRabbitMQServerlessInstancesRequest(AbstractModel):
    r"""ListRabbitMQServerlessInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        :param _Limit: Page size.
        :type Limit: int
        :param _Offset: Starting index value for pagination.
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        r"""Filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Page size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Starting index value for pagination.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRabbitMQServerlessInstancesResponse(AbstractModel):
    r"""ListRabbitMQServerlessInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: Instance list
        :type Instances: list of RabbitMQServerlessInstance
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""Instance list
        :rtype: list of RabbitMQServerlessInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
                obj = RabbitMQServerlessInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessExchangeRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessExchange request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost parameter.
        :type VirtualHost: str
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AlternateExchange: standby switch
        :type AlternateExchange: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None
        self._Remark = None
        self._AlternateExchange = None

    @property
    def InstanceId(self):
        r"""Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AlternateExchange(self):
        r"""standby switch
        :rtype: str
        """
        return self._AlternateExchange

    @AlternateExchange.setter
    def AlternateExchange(self, AlternateExchange):
        self._AlternateExchange = AlternateExchange


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        self._AlternateExchange = params.get("AlternateExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessExchangeResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessExchange response structure.

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

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
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessInstanceRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterName: Cluster name.
        :type ClusterName: str
        :param _Remark: Remarks
        :type Remark: str
        :param _TraceFlag: Whether trace is enabled.
        :type TraceFlag: bool
        :param _SendReceiveRatio: Traffic throttling production consumption ratio
        :type SendReceiveRatio: float
        :param _DeleteAllTags: Specifies whether to delete all tags. Default value: false.
        :type DeleteAllTags: bool
        :param _InstanceTags: Modified instance tag list
        :type InstanceTags: list of RabbitMQServerlessTag
        """
        self._InstanceId = None
        self._ClusterName = None
        self._Remark = None
        self._TraceFlag = None
        self._SendReceiveRatio = None
        self._DeleteAllTags = None
        self._InstanceTags = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterName(self):
        r"""Cluster name.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TraceFlag(self):
        r"""Whether trace is enabled.
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag

    @property
    def SendReceiveRatio(self):
        r"""Traffic throttling production consumption ratio
        :rtype: float
        """
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def DeleteAllTags(self):
        r"""Specifies whether to delete all tags. Default value: false.
        :rtype: bool
        """
        return self._DeleteAllTags

    @DeleteAllTags.setter
    def DeleteAllTags(self, DeleteAllTags):
        self._DeleteAllTags = DeleteAllTags

    @property
    def InstanceTags(self):
        r"""Modified instance tag list
        :rtype: list of RabbitMQServerlessTag
        """
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._TraceFlag = params.get("TraceFlag")
        self._SendReceiveRatio = params.get("SendReceiveRatio")
        self._DeleteAllTags = params.get("DeleteAllTags")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = RabbitMQServerlessTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessInstanceResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessPermissionRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessPermission request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username, which is the user associated with the permission.
        :type User: str
        :param _VirtualHost: Specifies the vhost name.
        :type VirtualHost: str
        :param _ConfigRegexp: Types of permissions. declare related operations. for the user, it is operable to perform operations on the resource name under the vhost that matches the regular expression.
        :type ConfigRegexp: str
        :param _WriteRegexp: Types of permissions. message write related operations. the user can operate on the resource names under the vhost that match the regular expression.
        :type WriteRegexp: str
        :param _ReadRegexp: Types of permissions. message read related operations. the user can operate on the resource name under the vhost that matches the regular expression.
        :type ReadRegexp: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._ConfigRegexp = None
        self._WriteRegexp = None
        self._ReadRegexp = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username, which is the user associated with the permission.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ConfigRegexp(self):
        r"""Types of permissions. declare related operations. for the user, it is operable to perform operations on the resource name under the vhost that matches the regular expression.
        :rtype: str
        """
        return self._ConfigRegexp

    @ConfigRegexp.setter
    def ConfigRegexp(self, ConfigRegexp):
        self._ConfigRegexp = ConfigRegexp

    @property
    def WriteRegexp(self):
        r"""Types of permissions. message write related operations. the user can operate on the resource names under the vhost that match the regular expression.
        :rtype: str
        """
        return self._WriteRegexp

    @WriteRegexp.setter
    def WriteRegexp(self, WriteRegexp):
        self._WriteRegexp = WriteRegexp

    @property
    def ReadRegexp(self):
        r"""Types of permissions. message read related operations. the user can operate on the resource name under the vhost that matches the regular expression.
        :rtype: str
        """
        return self._ReadRegexp

    @ReadRegexp.setter
    def ReadRegexp(self, ReadRegexp):
        self._ReadRegexp = ReadRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._ConfigRegexp = params.get("ConfigRegexp")
        self._WriteRegexp = params.get("WriteRegexp")
        self._ReadRegexp = params.get("ReadRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessPermissionResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessPermission response structure.

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


class ModifyRabbitMQServerlessQueueRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessQueue request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost parameter.
        :type VirtualHost: str
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _Remark: Newly modified remark.
        :type Remark: str
        :param _MessageTTL: MessageTTL parameter in milliseconds, dedicated to classic event type	
        :type MessageTTL: int
        :param _DeadLetterExchange: DeadLetterExchange parameter. It specifies that expired or rejected messages can be delivered to the specified dead letter exchange.
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: DeadLetterRoutingKey parameter. The value can only contain letters, digits, periods (.), hyphens (-), at signs (@), and underscores (_).
        :type DeadLetterRoutingKey: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._Remark = None
        self._MessageTTL = None
        self._DeadLetterExchange = None
        self._DeadLetterRoutingKey = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Remark(self):
        r"""Newly modified remark.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        r"""MessageTTL parameter in milliseconds, dedicated to classic event type	
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def DeadLetterExchange(self):
        r"""DeadLetterExchange parameter. It specifies that expired or rejected messages can be delivered to the specified dead letter exchange.
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        r"""DeadLetterRoutingKey parameter. The value can only contain letters, digits, periods (.), hyphens (-), at signs (@), and underscores (_).
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._Remark = params.get("Remark")
        self._MessageTTL = params.get("MessageTTL")
        self._DeadLetterExchange = params.get("DeadLetterExchange")
        self._DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessQueueResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessQueue response structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

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
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessUserRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username.
        :type User: str
        :param _Password: Password. specifies the password.
        :type Password: str
        :param _Description: Description. if not provided, no modification will be made.
        :type Description: str
        :param _Tags: User tag. specifies to determine the access permission scope of this user to RabbitMQ Management. if it is not passed in, no modification will be made.
        :type Tags: list of str
        :param _MaxConnections: Specifies the maximum number of connections for this user. if not provided, it will not be modified.
        :type MaxConnections: int
        :param _MaxChannels: Specifies the maximum number of channels for this user. if not provided, it will not be modified.
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""Password. specifies the password.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""Description. if not provided, no modification will be made.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""User tag. specifies to determine the access permission scope of this user to RabbitMQ Management. if it is not passed in, no modification will be made.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MaxConnections(self):
        r"""Specifies the maximum number of connections for this user. if not provided, it will not be modified.
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        r"""Specifies the maximum number of channels for this user. if not provided, it will not be modified.
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessUserResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessUser response structure.

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


class ModifyRabbitMQServerlessVirtualHostRequest(AbstractModel):
    r"""ModifyRabbitMQServerlessVirtualHost request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _VirtualHost: Specifies the vhost name.
        :type VirtualHost: str
        :param _Description: Specifies the description information of the vhost.
        :type Description: str
        :param _TraceFlag: Message trace switch. specifies that the value true turns on the switch and the value false turns it off.
        :type TraceFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._TraceFlag = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Specifies the vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        r"""Specifies the description information of the vhost.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceFlag(self):
        r"""Message trace switch. specifies that the value true turns on the switch and the value false turns it off.
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._TraceFlag = params.get("TraceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessVirtualHostResponse(AbstractModel):
    r"""ModifyRabbitMQServerlessVirtualHost response structure.

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


class QueueQuota(AbstractModel):
    r"""Specifies the queue usage quota information.

    """

    def __init__(self):
        r"""
        :param _MaxQueue: Specifies the maximum number of queues that can be created.
        :type MaxQueue: int
        :param _UsedQueue: Number of queues created.
        :type UsedQueue: int
        """
        self._MaxQueue = None
        self._UsedQueue = None

    @property
    def MaxQueue(self):
        r"""Specifies the maximum number of queues that can be created.
        :rtype: int
        """
        return self._MaxQueue

    @MaxQueue.setter
    def MaxQueue(self, MaxQueue):
        self._MaxQueue = MaxQueue

    @property
    def UsedQueue(self):
        r"""Number of queues created.
        :rtype: int
        """
        return self._UsedQueue

    @UsedQueue.setter
    def UsedQueue(self, UsedQueue):
        self._UsedQueue = UsedQueue


    def _deserialize(self, params):
        self._MaxQueue = params.get("MaxQueue")
        self._UsedQueue = params.get("UsedQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQBindingListInfo(AbstractModel):
    r"""Rabbitmq binding relationship list member.

    """

    def __init__(self):
        r"""
        :param _BindingId: <p>Routing relationship id</p>
        :type BindingId: int
        :param _VirtualHost: <p>Vhost parameter</p>
        :type VirtualHost: str
        :param _Source: <p>Source exchange name</p>
        :type Source: str
        :param _DestinationType: <p>Target type, queue or exchange</p>
        :type DestinationType: str
        :param _Destination: <p>Target resource name</p>
        :type Destination: str
        :param _RoutingKey: <p>Bind key</p>
        :type RoutingKey: str
        :param _SourceExchangeType: <p>Source exchange type</p>
        :type SourceExchangeType: str
        :param _CreateTime: <p>Creation time.</p>
        :type CreateTime: str
        :param _ModifyTime: <p>Modification time.</p>
        :type ModifyTime: str
        :param _Arguments: <p>Bind parameter. Parameters can be passed in during binding for header type Exchange. No need to input for other types of Exchange.</p>
        :type Arguments: list of RabbitMQServerlessKeyValuePair
        """
        self._BindingId = None
        self._VirtualHost = None
        self._Source = None
        self._DestinationType = None
        self._Destination = None
        self._RoutingKey = None
        self._SourceExchangeType = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Arguments = None

    @property
    def BindingId(self):
        r"""<p>Routing relationship id</p>
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def VirtualHost(self):
        r"""<p>Vhost parameter</p>
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Source(self):
        r"""<p>Source exchange name</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DestinationType(self):
        r"""<p>Target type, queue or exchange</p>
        :rtype: str
        """
        return self._DestinationType

    @DestinationType.setter
    def DestinationType(self, DestinationType):
        self._DestinationType = DestinationType

    @property
    def Destination(self):
        r"""<p>Target resource name</p>
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def RoutingKey(self):
        r"""<p>Bind key</p>
        :rtype: str
        """
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey

    @property
    def SourceExchangeType(self):
        r"""<p>Source exchange type</p>
        :rtype: str
        """
        return self._SourceExchangeType

    @SourceExchangeType.setter
    def SourceExchangeType(self, SourceExchangeType):
        self._SourceExchangeType = SourceExchangeType

    @property
    def CreateTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""<p>Modification time.</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Arguments(self):
        r"""<p>Bind parameter. Parameters can be passed in during binding for header type Exchange. No need to input for other types of Exchange.</p>
        :rtype: list of RabbitMQServerlessKeyValuePair
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._BindingId = params.get("BindingId")
        self._VirtualHost = params.get("VirtualHost")
        self._Source = params.get("Source")
        self._DestinationType = params.get("DestinationType")
        self._Destination = params.get("Destination")
        self._RoutingKey = params.get("RoutingKey")
        self._SourceExchangeType = params.get("SourceExchangeType")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = RabbitMQServerlessKeyValuePair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQClusterInfo(AbstractModel):
    r"""RabbitMQ cluster basic information.

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>Cluster ID.</p>
        :type ClusterId: str
        :param _ClusterName: <p>Cluster name.</p>
        :type ClusterName: str
        :param _Region: <p>Regional information</p>
        :type Region: str
        :param _CreateTime: <p>Creation time in milliseconds</p>
        :type CreateTime: int
        :param _Remark: <p>Cluster description information</p>
        :type Remark: str
        :param _Vpcs: <p>VPC and network info</p>
        :type Vpcs: list of VpcEndpointInfo
        :param _ZoneIds: <p>AZ information</p>
        :type ZoneIds: list of int
        :param _VirtualHostNumber: <p>Number of virtual hosts</p>
        :type VirtualHostNumber: int
        :param _QueueNumber: <p>Number of queues</p>
        :type QueueNumber: int
        :param _MessagePublishRate: <p>Number of messages produced per second Unit: messages/second</p>
        :type MessagePublishRate: float
        :param _MessageStackNumber: <p>Number of accumulated messages Unit: unit</p>
        :type MessageStackNumber: int
        :param _ExpireTime: <p>Expiration time</p>
        :type ExpireTime: int
        :param _ChannelNumber: <p>Number of channels</p>
        :type ChannelNumber: int
        :param _ConnectionNumber: <p>Number of connections</p>
        :type ConnectionNumber: int
        :param _ConsumerNumber: <p>Number of consumers</p>
        :type ConsumerNumber: int
        :param _ExchangeNumber: <p>Number of Exchanges</p>
        :type ExchangeNumber: int
        :param _ExceptionInformation: <p>Cluster exception information</p>
        :type ExceptionInformation: str
        :param _ClusterStatus: <p>Instance status. 0 indicates creating in progress, 1 indicates normal, 2 indicates isolated, 3 indicates terminated, 4 - abnormal, 5 - delivery failed</p>
        :type ClusterStatus: int
        :param _AutoRenewFlag: <p>Automatic renewal flag. 0: default status (initial status (that is manual renewal) if no status is set by the user); 1: automatic renewal; 2: no automatic renewal (set by the user).</p>
        :type AutoRenewFlag: int
        :param _MirrorQueuePolicyFlag: <p>Whether to enable the mirror queue policy. 1 means enabled, 0 means disabled.</p>
        :type MirrorQueuePolicyFlag: int
        :param _MessageConsumeRate: <p>Number of messages consumed per second Unit: messages/second</p>
        :type MessageConsumeRate: float
        :param _ClusterVersion: <p>Cluster version information</p>
        :type ClusterVersion: str
        :param _PayMode: <p>Billing mode. 0 - Postpaid, 1 - Prepaid</p>
        :type PayMode: int
        :param _InstanceType: <p>Cluster type.</p>
        :type InstanceType: int
        :param _MessageRetainTime: <p>Message retention period Unit: hour</p>
        :type MessageRetainTime: int
        :param _SendReceiveRatio: <p>Traffic ratio of sending messages</p>
        :type SendReceiveRatio: float
        :param _TraceTime: <p>Message trace retention time in hours</p>
        :type TraceTime: int
        :param _Tags: <p>Instance tag list</p>
        :type Tags: list of RabbitMQServerlessTag
        :param _ElasticTpsFlag: <p>Elastic scaling enabled tps</p>
        :type ElasticTpsFlag: bool
        :param _ElasticTpsRatio: <p>Elastic tps multiple, default is 1x</p>
        :type ElasticTpsRatio: float
        :param _MaxRedeliverCount: <p>Maximum retry count</p>
        :type MaxRedeliverCount: int
        :param _ConsumerTimeout: <p>Consumption timeout period Unit: min</p>
        :type ConsumerTimeout: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._CreateTime = None
        self._Remark = None
        self._Vpcs = None
        self._ZoneIds = None
        self._VirtualHostNumber = None
        self._QueueNumber = None
        self._MessagePublishRate = None
        self._MessageStackNumber = None
        self._ExpireTime = None
        self._ChannelNumber = None
        self._ConnectionNumber = None
        self._ConsumerNumber = None
        self._ExchangeNumber = None
        self._ExceptionInformation = None
        self._ClusterStatus = None
        self._AutoRenewFlag = None
        self._MirrorQueuePolicyFlag = None
        self._MessageConsumeRate = None
        self._ClusterVersion = None
        self._PayMode = None
        self._InstanceType = None
        self._MessageRetainTime = None
        self._SendReceiveRatio = None
        self._TraceTime = None
        self._Tags = None
        self._ElasticTpsFlag = None
        self._ElasticTpsRatio = None
        self._MaxRedeliverCount = None
        self._ConsumerTimeout = None

    @property
    def ClusterId(self):
        r"""<p>Cluster ID.</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>Cluster name.</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        r"""<p>Regional information</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        r"""<p>Creation time in milliseconds</p>
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        r"""<p>Cluster description information</p>
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Vpcs(self):
        r"""<p>VPC and network info</p>
        :rtype: list of VpcEndpointInfo
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def ZoneIds(self):
        r"""<p>AZ information</p>
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def VirtualHostNumber(self):
        r"""<p>Number of virtual hosts</p>
        :rtype: int
        """
        return self._VirtualHostNumber

    @VirtualHostNumber.setter
    def VirtualHostNumber(self, VirtualHostNumber):
        self._VirtualHostNumber = VirtualHostNumber

    @property
    def QueueNumber(self):
        r"""<p>Number of queues</p>
        :rtype: int
        """
        return self._QueueNumber

    @QueueNumber.setter
    def QueueNumber(self, QueueNumber):
        self._QueueNumber = QueueNumber

    @property
    def MessagePublishRate(self):
        r"""<p>Number of messages produced per second Unit: messages/second</p>
        :rtype: float
        """
        return self._MessagePublishRate

    @MessagePublishRate.setter
    def MessagePublishRate(self, MessagePublishRate):
        self._MessagePublishRate = MessagePublishRate

    @property
    def MessageStackNumber(self):
        r"""<p>Number of accumulated messages Unit: unit</p>
        :rtype: int
        """
        return self._MessageStackNumber

    @MessageStackNumber.setter
    def MessageStackNumber(self, MessageStackNumber):
        self._MessageStackNumber = MessageStackNumber

    @property
    def ExpireTime(self):
        r"""<p>Expiration time</p>
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelNumber(self):
        r"""<p>Number of channels</p>
        :rtype: int
        """
        return self._ChannelNumber

    @ChannelNumber.setter
    def ChannelNumber(self, ChannelNumber):
        self._ChannelNumber = ChannelNumber

    @property
    def ConnectionNumber(self):
        r"""<p>Number of connections</p>
        :rtype: int
        """
        return self._ConnectionNumber

    @ConnectionNumber.setter
    def ConnectionNumber(self, ConnectionNumber):
        self._ConnectionNumber = ConnectionNumber

    @property
    def ConsumerNumber(self):
        r"""<p>Number of consumers</p>
        :rtype: int
        """
        return self._ConsumerNumber

    @ConsumerNumber.setter
    def ConsumerNumber(self, ConsumerNumber):
        self._ConsumerNumber = ConsumerNumber

    @property
    def ExchangeNumber(self):
        r"""<p>Number of Exchanges</p>
        :rtype: int
        """
        return self._ExchangeNumber

    @ExchangeNumber.setter
    def ExchangeNumber(self, ExchangeNumber):
        self._ExchangeNumber = ExchangeNumber

    @property
    def ExceptionInformation(self):
        r"""<p>Cluster exception information</p>
        :rtype: str
        """
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation

    @property
    def ClusterStatus(self):
        r"""<p>Instance status. 0 indicates creating in progress, 1 indicates normal, 2 indicates isolated, 3 indicates terminated, 4 - abnormal, 5 - delivery failed</p>
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def AutoRenewFlag(self):
        r"""<p>Automatic renewal flag. 0: default status (initial status (that is manual renewal) if no status is set by the user); 1: automatic renewal; 2: no automatic renewal (set by the user).</p>
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def MirrorQueuePolicyFlag(self):
        r"""<p>Whether to enable the mirror queue policy. 1 means enabled, 0 means disabled.</p>
        :rtype: int
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag

    @property
    def MessageConsumeRate(self):
        r"""<p>Number of messages consumed per second Unit: messages/second</p>
        :rtype: float
        """
        return self._MessageConsumeRate

    @MessageConsumeRate.setter
    def MessageConsumeRate(self, MessageConsumeRate):
        self._MessageConsumeRate = MessageConsumeRate

    @property
    def ClusterVersion(self):
        r"""<p>Cluster version information</p>
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def PayMode(self):
        r"""<p>Billing mode. 0 - Postpaid, 1 - Prepaid</p>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceType(self):
        r"""<p>Cluster type.</p>
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MessageRetainTime(self):
        r"""<p>Message retention period Unit: hour</p>
        :rtype: int
        """
        return self._MessageRetainTime

    @MessageRetainTime.setter
    def MessageRetainTime(self, MessageRetainTime):
        self._MessageRetainTime = MessageRetainTime

    @property
    def SendReceiveRatio(self):
        r"""<p>Traffic ratio of sending messages</p>
        :rtype: float
        """
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def TraceTime(self):
        r"""<p>Message trace retention time in hours</p>
        :rtype: int
        """
        return self._TraceTime

    @TraceTime.setter
    def TraceTime(self, TraceTime):
        self._TraceTime = TraceTime

    @property
    def Tags(self):
        r"""<p>Instance tag list</p>
        :rtype: list of RabbitMQServerlessTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ElasticTpsFlag(self):
        r"""<p>Elastic scaling enabled tps</p>
        :rtype: bool
        """
        return self._ElasticTpsFlag

    @ElasticTpsFlag.setter
    def ElasticTpsFlag(self, ElasticTpsFlag):
        self._ElasticTpsFlag = ElasticTpsFlag

    @property
    def ElasticTpsRatio(self):
        r"""<p>Elastic tps multiple, default is 1x</p>
        :rtype: float
        """
        return self._ElasticTpsRatio

    @ElasticTpsRatio.setter
    def ElasticTpsRatio(self, ElasticTpsRatio):
        self._ElasticTpsRatio = ElasticTpsRatio

    @property
    def MaxRedeliverCount(self):
        r"""<p>Maximum retry count</p>
        :rtype: int
        """
        return self._MaxRedeliverCount

    @MaxRedeliverCount.setter
    def MaxRedeliverCount(self, MaxRedeliverCount):
        self._MaxRedeliverCount = MaxRedeliverCount

    @property
    def ConsumerTimeout(self):
        r"""<p>Consumption timeout period Unit: min</p>
        :rtype: int
        """
        return self._ConsumerTimeout

    @ConsumerTimeout.setter
    def ConsumerTimeout(self, ConsumerTimeout):
        self._ConsumerTimeout = ConsumerTimeout


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcEndpointInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._ZoneIds = params.get("ZoneIds")
        self._VirtualHostNumber = params.get("VirtualHostNumber")
        self._QueueNumber = params.get("QueueNumber")
        self._MessagePublishRate = params.get("MessagePublishRate")
        self._MessageStackNumber = params.get("MessageStackNumber")
        self._ExpireTime = params.get("ExpireTime")
        self._ChannelNumber = params.get("ChannelNumber")
        self._ConnectionNumber = params.get("ConnectionNumber")
        self._ConsumerNumber = params.get("ConsumerNumber")
        self._ExchangeNumber = params.get("ExchangeNumber")
        self._ExceptionInformation = params.get("ExceptionInformation")
        self._ClusterStatus = params.get("ClusterStatus")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        self._MessageConsumeRate = params.get("MessageConsumeRate")
        self._ClusterVersion = params.get("ClusterVersion")
        self._PayMode = params.get("PayMode")
        self._InstanceType = params.get("InstanceType")
        self._MessageRetainTime = params.get("MessageRetainTime")
        self._SendReceiveRatio = params.get("SendReceiveRatio")
        self._TraceTime = params.get("TraceTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RabbitMQServerlessTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ElasticTpsFlag = params.get("ElasticTpsFlag")
        self._ElasticTpsRatio = params.get("ElasticTpsRatio")
        self._MaxRedeliverCount = params.get("MaxRedeliverCount")
        self._ConsumerTimeout = params.get("ConsumerTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQClusterSpecInfo(AbstractModel):
    r"""RabbitMQ cluster specification information.

    """

    def __init__(self):
        r"""
        :param _SpecName: Specifies the cluster specification name.
        :type SpecName: str
        :param _MaxTps: Max tps.
        :type MaxTps: int
        :param _MaxQueueNum: Maximum number of queues.
        :type MaxQueueNum: int
        :param _MaxExchangeNum: Maximum number of exchanges.
        :type MaxExchangeNum: int
        :param _MaxVhostNum: Maximum number of vhosts.
        :type MaxVhostNum: int
        :param _MaxConnNum: Maximum number of connections.
        :type MaxConnNum: int
        :param _MaxUserNum: Maximum number of users.
        :type MaxUserNum: int
        :param _MaxBandWidth: Peak bandwidth. abandoned.
        :type MaxBandWidth: int
        :param _PublicNetworkTps: Public network bandwidth. abandoned.
        :type PublicNetworkTps: int
        :param _Features: Feature list corresponding to the instance, yes means supported, no means unsupported
        :type Features: str
        """
        self._SpecName = None
        self._MaxTps = None
        self._MaxQueueNum = None
        self._MaxExchangeNum = None
        self._MaxVhostNum = None
        self._MaxConnNum = None
        self._MaxUserNum = None
        self._MaxBandWidth = None
        self._PublicNetworkTps = None
        self._Features = None

    @property
    def SpecName(self):
        r"""Specifies the cluster specification name.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def MaxTps(self):
        r"""Max tps.
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxQueueNum(self):
        r"""Maximum number of queues.
        :rtype: int
        """
        return self._MaxQueueNum

    @MaxQueueNum.setter
    def MaxQueueNum(self, MaxQueueNum):
        self._MaxQueueNum = MaxQueueNum

    @property
    def MaxExchangeNum(self):
        r"""Maximum number of exchanges.
        :rtype: int
        """
        return self._MaxExchangeNum

    @MaxExchangeNum.setter
    def MaxExchangeNum(self, MaxExchangeNum):
        self._MaxExchangeNum = MaxExchangeNum

    @property
    def MaxVhostNum(self):
        r"""Maximum number of vhosts.
        :rtype: int
        """
        return self._MaxVhostNum

    @MaxVhostNum.setter
    def MaxVhostNum(self, MaxVhostNum):
        self._MaxVhostNum = MaxVhostNum

    @property
    def MaxConnNum(self):
        r"""Maximum number of connections.
        :rtype: int
        """
        return self._MaxConnNum

    @MaxConnNum.setter
    def MaxConnNum(self, MaxConnNum):
        self._MaxConnNum = MaxConnNum

    @property
    def MaxUserNum(self):
        r"""Maximum number of users.
        :rtype: int
        """
        return self._MaxUserNum

    @MaxUserNum.setter
    def MaxUserNum(self, MaxUserNum):
        self._MaxUserNum = MaxUserNum

    @property
    def MaxBandWidth(self):
        r"""Peak bandwidth. abandoned.
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def PublicNetworkTps(self):
        r"""Public network bandwidth. abandoned.
        :rtype: int
        """
        return self._PublicNetworkTps

    @PublicNetworkTps.setter
    def PublicNetworkTps(self, PublicNetworkTps):
        self._PublicNetworkTps = PublicNetworkTps

    @property
    def Features(self):
        r"""Feature list corresponding to the instance, yes means supported, no means unsupported
        :rtype: str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._MaxTps = params.get("MaxTps")
        self._MaxQueueNum = params.get("MaxQueueNum")
        self._MaxExchangeNum = params.get("MaxExchangeNum")
        self._MaxVhostNum = params.get("MaxVhostNum")
        self._MaxConnNum = params.get("MaxConnNum")
        self._MaxUserNum = params.get("MaxUserNum")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._PublicNetworkTps = params.get("PublicNetworkTps")
        self._Features = params.get("Features")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQConnection(AbstractModel):
    r"""RabbitMQ connection detail.

    """

    def __init__(self):
        r"""
        :param _ConnectionName: Connection name.
        :type ConnectionName: str
        :param _PeerHost: Client IP
        :type PeerHost: str
        :param _State: Specifies the connection status, including starting, tuning, opening, running, flow, blocking, blocked, closing, and closed.
        :type State: str
        :param _User: User that who has created this connection.
        :type User: str
        :param _SSL: Whether ssl is enabled.
        :type SSL: bool
        :param _Protocol: Connection protocol.
        :type Protocol: str
        :param _Channels: Specifies the number of channels under the connection.
        :type Channels: int
        :param _IncomingBytes: Inbound traffic volume in bytes
        :type IncomingBytes: float
        :param _OutgoingBytes: Outbound traffic volume in bytes
        :type OutgoingBytes: float
        :param _Heartbeat: Heartbeat interval. Default 60s.
        :type Heartbeat: int
        :param _MaxChannel: Maximum number of channels per link. Default 1024.
        :type MaxChannel: int
        :param _IdleSince: Idle time point
        :type IdleSince: str
        """
        self._ConnectionName = None
        self._PeerHost = None
        self._State = None
        self._User = None
        self._SSL = None
        self._Protocol = None
        self._Channels = None
        self._IncomingBytes = None
        self._OutgoingBytes = None
        self._Heartbeat = None
        self._MaxChannel = None
        self._IdleSince = None

    @property
    def ConnectionName(self):
        r"""Connection name.
        :rtype: str
        """
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def PeerHost(self):
        r"""Client IP
        :rtype: str
        """
        return self._PeerHost

    @PeerHost.setter
    def PeerHost(self, PeerHost):
        self._PeerHost = PeerHost

    @property
    def State(self):
        r"""Specifies the connection status, including starting, tuning, opening, running, flow, blocking, blocked, closing, and closed.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        r"""User that who has created this connection.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def SSL(self):
        r"""Whether ssl is enabled.
        :rtype: bool
        """
        return self._SSL

    @SSL.setter
    def SSL(self, SSL):
        self._SSL = SSL

    @property
    def Protocol(self):
        r"""Connection protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Channels(self):
        r"""Specifies the number of channels under the connection.
        :rtype: int
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def IncomingBytes(self):
        r"""Inbound traffic volume in bytes
        :rtype: float
        """
        return self._IncomingBytes

    @IncomingBytes.setter
    def IncomingBytes(self, IncomingBytes):
        self._IncomingBytes = IncomingBytes

    @property
    def OutgoingBytes(self):
        r"""Outbound traffic volume in bytes
        :rtype: float
        """
        return self._OutgoingBytes

    @OutgoingBytes.setter
    def OutgoingBytes(self, OutgoingBytes):
        self._OutgoingBytes = OutgoingBytes

    @property
    def Heartbeat(self):
        r"""Heartbeat interval. Default 60s.
        :rtype: int
        """
        return self._Heartbeat

    @Heartbeat.setter
    def Heartbeat(self, Heartbeat):
        self._Heartbeat = Heartbeat

    @property
    def MaxChannel(self):
        r"""Maximum number of channels per link. Default 1024.
        :rtype: int
        """
        return self._MaxChannel

    @MaxChannel.setter
    def MaxChannel(self, MaxChannel):
        self._MaxChannel = MaxChannel

    @property
    def IdleSince(self):
        r"""Idle time point
        :rtype: str
        """
        return self._IdleSince

    @IdleSince.setter
    def IdleSince(self, IdleSince):
        self._IdleSince = IdleSince


    def _deserialize(self, params):
        self._ConnectionName = params.get("ConnectionName")
        self._PeerHost = params.get("PeerHost")
        self._State = params.get("State")
        self._User = params.get("User")
        self._SSL = params.get("SSL")
        self._Protocol = params.get("Protocol")
        self._Channels = params.get("Channels")
        self._IncomingBytes = params.get("IncomingBytes")
        self._OutgoingBytes = params.get("OutgoingBytes")
        self._Heartbeat = params.get("Heartbeat")
        self._MaxChannel = params.get("MaxChannel")
        self._IdleSince = params.get("IdleSince")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQConsumersListInfo(AbstractModel):
    r"""Queue consumer list information.

    """

    def __init__(self):
        r"""
        :param _ClientIp: Client Ip.
        :type ClientIp: str
        :param _ConsumerTag: Consumer Tag.
        :type ConsumerTag: str
        :param _QueueName: Consume target queue
        :type QueueName: str
        :param _AckRequired: Whether required for the consumer to manually ack
        :type AckRequired: bool
        :param _PrefetchCount: Consumer qos value
        :type PrefetchCount: int
        :param _Active: Consumer status
        :type Active: str
        :param _LastDeliveredTime: Time of the last message submission
        :type LastDeliveredTime: str
        :param _UnAckMsgCount: Number of unconfirmed messages of the consumer
        :type UnAckMsgCount: int
        :param _ChannelName: channel belonging to the consumer
        :type ChannelName: str
        """
        self._ClientIp = None
        self._ConsumerTag = None
        self._QueueName = None
        self._AckRequired = None
        self._PrefetchCount = None
        self._Active = None
        self._LastDeliveredTime = None
        self._UnAckMsgCount = None
        self._ChannelName = None

    @property
    def ClientIp(self):
        r"""Client Ip.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def ConsumerTag(self):
        r"""Consumer Tag.
        :rtype: str
        """
        return self._ConsumerTag

    @ConsumerTag.setter
    def ConsumerTag(self, ConsumerTag):
        self._ConsumerTag = ConsumerTag

    @property
    def QueueName(self):
        r"""Consume target queue
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def AckRequired(self):
        r"""Whether required for the consumer to manually ack
        :rtype: bool
        """
        return self._AckRequired

    @AckRequired.setter
    def AckRequired(self, AckRequired):
        self._AckRequired = AckRequired

    @property
    def PrefetchCount(self):
        r"""Consumer qos value
        :rtype: int
        """
        return self._PrefetchCount

    @PrefetchCount.setter
    def PrefetchCount(self, PrefetchCount):
        self._PrefetchCount = PrefetchCount

    @property
    def Active(self):
        r"""Consumer status
        :rtype: str
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def LastDeliveredTime(self):
        r"""Time of the last message submission
        :rtype: str
        """
        return self._LastDeliveredTime

    @LastDeliveredTime.setter
    def LastDeliveredTime(self, LastDeliveredTime):
        self._LastDeliveredTime = LastDeliveredTime

    @property
    def UnAckMsgCount(self):
        r"""Number of unconfirmed messages of the consumer
        :rtype: int
        """
        return self._UnAckMsgCount

    @UnAckMsgCount.setter
    def UnAckMsgCount(self, UnAckMsgCount):
        self._UnAckMsgCount = UnAckMsgCount

    @property
    def ChannelName(self):
        r"""channel belonging to the consumer
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._ConsumerTag = params.get("ConsumerTag")
        self._QueueName = params.get("QueueName")
        self._AckRequired = params.get("AckRequired")
        self._PrefetchCount = params.get("PrefetchCount")
        self._Active = params.get("Active")
        self._LastDeliveredTime = params.get("LastDeliveredTime")
        self._UnAckMsgCount = params.get("UnAckMsgCount")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQExchangeListInfo(AbstractModel):
    r"""RabbitMQ exchange list member information.

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange name.
        :type ExchangeName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _ExchangeType: Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :type ExchangeType: str
        :param _VirtualHost: VHost parameter.
        :type VirtualHost: str
        :param _ExchangeCreator: exchange creator. valid values: `system` (generated by the system), `user` (user-created).
        :type ExchangeCreator: str
        :param _CreateTimeStamp: exchange creation time.
        :type CreateTimeStamp: str
        :param _ModTimeStamp: exchange modification time.
        :type ModTimeStamp: str
        :param _MessageRateIn: Input message rate.
        :type MessageRateIn: float
        :param _MessageRateOut: Output message rate.
        :type MessageRateOut: float
        :param _Durable: Specifies whether it is a persistent exchange. true indicates persistent, and false indicates non-persistent.
        :type Durable: bool
        :param _AutoDelete: Specifies whether to automatically delete the switch. true indicates automatic deletion, and false indicates non-automatic deletion.
        :type AutoDelete: bool
        :param _Internal: Whether it is an internal switch. valid values: true (indicating an internal switch).
        :type Internal: bool
        :param _InstanceId: Specifies the ID of the associated instance to which the switch belongs.
        :type InstanceId: str
        :param _Policy: The name of the effective policy.
        :type Policy: str
        :param _Arguments: Additional parameters key-value objects.
        :type Arguments: str
        :param _MessagesDelayed: Number of unscheduled delayed messages.
        :type MessagesDelayed: int
        """
        self._ExchangeName = None
        self._Remark = None
        self._ExchangeType = None
        self._VirtualHost = None
        self._ExchangeCreator = None
        self._CreateTimeStamp = None
        self._ModTimeStamp = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._InstanceId = None
        self._Policy = None
        self._Arguments = None
        self._MessagesDelayed = None

    @property
    def ExchangeName(self):
        r"""exchange name.
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ExchangeType(self):
        r"""Specifies the exchange type. valid values: "fanout", "direct", "topic", "headers".
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def VirtualHost(self):
        r"""VHost parameter.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeCreator(self):
        r"""exchange creator. valid values: `system` (generated by the system), `user` (user-created).
        :rtype: str
        """
        return self._ExchangeCreator

    @ExchangeCreator.setter
    def ExchangeCreator(self, ExchangeCreator):
        self._ExchangeCreator = ExchangeCreator

    @property
    def CreateTimeStamp(self):
        r"""exchange creation time.
        :rtype: str
        """
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def ModTimeStamp(self):
        r"""exchange modification time.
        :rtype: str
        """
        return self._ModTimeStamp

    @ModTimeStamp.setter
    def ModTimeStamp(self, ModTimeStamp):
        self._ModTimeStamp = ModTimeStamp

    @property
    def MessageRateIn(self):
        r"""Input message rate.
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        r"""Output message rate.
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def Durable(self):
        r"""Specifies whether it is a persistent exchange. true indicates persistent, and false indicates non-persistent.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Specifies whether to automatically delete the switch. true indicates automatic deletion, and false indicates non-automatic deletion.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        r"""Whether it is an internal switch. valid values: true (indicating an internal switch).
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def InstanceId(self):
        r"""Specifies the ID of the associated instance to which the switch belongs.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Policy(self):
        r"""The name of the effective policy.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        r"""Additional parameters key-value objects.
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def MessagesDelayed(self):
        r"""Number of unscheduled delayed messages.
        :rtype: int
        """
        return self._MessagesDelayed

    @MessagesDelayed.setter
    def MessagesDelayed(self, MessagesDelayed):
        self._MessagesDelayed = MessagesDelayed


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        self._ExchangeType = params.get("ExchangeType")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeCreator = params.get("ExchangeCreator")
        self._CreateTimeStamp = params.get("CreateTimeStamp")
        self._ModTimeStamp = params.get("ModTimeStamp")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._InstanceId = params.get("InstanceId")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._MessagesDelayed = params.get("MessagesDelayed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQPermission(AbstractModel):
    r"""RabbitMQ permission details.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username, which is the user associated with the permission.
        :type User: str
        :param _VirtualHost: vhost name.
        :type VirtualHost: str
        :param _ConfigRegexp: Types of permissions. declare related operations. for the user, it is operable to perform operations on the resource name under the vhost that matches the regular expression.
        :type ConfigRegexp: str
        :param _WriteRegexp: Types of permissions. message write related operations. the user can operate on the resource names under the vhost that match the regular expression.
        :type WriteRegexp: str
        :param _ReadRegexp: Types of permissions. message read related operations. the user can operate on the resource name under the vhost that matches the regular expression.
        :type ReadRegexp: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._ConfigRegexp = None
        self._WriteRegexp = None
        self._ReadRegexp = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username, which is the user associated with the permission.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        r"""vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ConfigRegexp(self):
        r"""Types of permissions. declare related operations. for the user, it is operable to perform operations on the resource name under the vhost that matches the regular expression.
        :rtype: str
        """
        return self._ConfigRegexp

    @ConfigRegexp.setter
    def ConfigRegexp(self, ConfigRegexp):
        self._ConfigRegexp = ConfigRegexp

    @property
    def WriteRegexp(self):
        r"""Types of permissions. message write related operations. the user can operate on the resource names under the vhost that match the regular expression.
        :rtype: str
        """
        return self._WriteRegexp

    @WriteRegexp.setter
    def WriteRegexp(self, WriteRegexp):
        self._WriteRegexp = WriteRegexp

    @property
    def ReadRegexp(self):
        r"""Types of permissions. message read related operations. the user can operate on the resource name under the vhost that matches the regular expression.
        :rtype: str
        """
        return self._ReadRegexp

    @ReadRegexp.setter
    def ReadRegexp(self, ReadRegexp):
        self._ReadRegexp = ReadRegexp

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._ConfigRegexp = params.get("ConfigRegexp")
        self._WriteRegexp = params.get("WriteRegexp")
        self._ReadRegexp = params.get("ReadRegexp")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQQueueListConsumerDetailInfo(AbstractModel):
    r"""RabbitMQ queue list consumer information response parameters structure.

    """

    def __init__(self):
        r"""
        :param _ConsumersNumber: Number of consumers.
        :type ConsumersNumber: int
        """
        self._ConsumersNumber = None

    @property
    def ConsumersNumber(self):
        r"""Number of consumers.
        :rtype: int
        """
        return self._ConsumersNumber

    @ConsumersNumber.setter
    def ConsumersNumber(self, ConsumersNumber):
        self._ConsumersNumber = ConsumersNumber


    def _deserialize(self, params):
        self._ConsumersNumber = params.get("ConsumersNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQQueueListInfo(AbstractModel):
    r"""RabbitMQ queue list member information.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name.
        :type QueueName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _ConsumerDetail: Consumer information.
        :type ConsumerDetail: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQQueueListConsumerDetailInfo`
        :param _QueueType: Specifies the queue type. the valid values are "classic" and "quorum".
        :type QueueType: str
        :param _MessageHeapCount: Number of message backlogs.
        :type MessageHeapCount: int
        :param _MessageRateIn: Message production rate per second.
        :type MessageRateIn: float
        :param _MessageRateOut: Message consumption rate per second.
        :type MessageRateOut: float
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        :param _Durable: Specifies whether the queue is persistent. true indicates persistent, and false indicates non-persistent.
        :type Durable: bool
        :param _AutoDelete: Specifies whether the queue is an auto-delete queue. true indicates auto-delete, and false indicates non-auto-delete.
        :type AutoDelete: bool
        :param _InstanceId: instanceId to which the queue belongs.
        :type InstanceId: str
        :param _VirtualHost: Name of the virtual host to which the queue belongs.
        :type VirtualHost: str
        :param _Node: Specifies the name of the primary node where the queue is located.
        :type Node: str
        :param _Policy: The name of the effective policy.
        :type Policy: str
        :param _Arguments: Additional parameters key-value objects.
        :type Arguments: str
        :param _Exclusive: Whether it is an exclusive queue.
        :type Exclusive: bool
        """
        self._QueueName = None
        self._Remark = None
        self._ConsumerDetail = None
        self._QueueType = None
        self._MessageHeapCount = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Durable = None
        self._AutoDelete = None
        self._InstanceId = None
        self._VirtualHost = None
        self._Node = None
        self._Policy = None
        self._Arguments = None
        self._Exclusive = None

    @property
    def QueueName(self):
        r"""Queue name.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Remark(self):
        r"""Remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsumerDetail(self):
        r"""Consumer information.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQQueueListConsumerDetailInfo`
        """
        return self._ConsumerDetail

    @ConsumerDetail.setter
    def ConsumerDetail(self, ConsumerDetail):
        self._ConsumerDetail = ConsumerDetail

    @property
    def QueueType(self):
        r"""Specifies the queue type. the valid values are "classic" and "quorum".
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def MessageHeapCount(self):
        r"""Number of message backlogs.
        :rtype: int
        """
        return self._MessageHeapCount

    @MessageHeapCount.setter
    def MessageHeapCount(self, MessageHeapCount):
        self._MessageHeapCount = MessageHeapCount

    @property
    def MessageRateIn(self):
        r"""Message production rate per second.
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        r"""Message consumption rate per second.
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Durable(self):
        r"""Specifies whether the queue is persistent. true indicates persistent, and false indicates non-persistent.
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        r"""Specifies whether the queue is an auto-delete queue. true indicates auto-delete, and false indicates non-auto-delete.
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def InstanceId(self):
        r"""instanceId to which the queue belongs.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Name of the virtual host to which the queue belongs.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Node(self):
        r"""Specifies the name of the primary node where the queue is located.
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Policy(self):
        r"""The name of the effective policy.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        r"""Additional parameters key-value objects.
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def Exclusive(self):
        r"""Whether it is an exclusive queue.
        :rtype: bool
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._Remark = params.get("Remark")
        if params.get("ConsumerDetail") is not None:
            self._ConsumerDetail = RabbitMQQueueListConsumerDetailInfo()
            self._ConsumerDetail._deserialize(params.get("ConsumerDetail"))
        self._QueueType = params.get("QueueType")
        self._MessageHeapCount = params.get("MessageHeapCount")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Node = params.get("Node")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._Exclusive = params.get("Exclusive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessAccessInfo(AbstractModel):
    r"""Public network access information.

    """

    def __init__(self):
        r"""
        :param _PublicAccessEndpoint: Public network domain.
        :type PublicAccessEndpoint: str
        :param _PublicDataStreamStatus: Public network status.
        :type PublicDataStreamStatus: str
        :param _PublicClbId: Public network CLB instance ID
        :type PublicClbId: str
        """
        self._PublicAccessEndpoint = None
        self._PublicDataStreamStatus = None
        self._PublicClbId = None

    @property
    def PublicAccessEndpoint(self):
        r"""Public network domain.
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def PublicDataStreamStatus(self):
        r"""Public network status.
        :rtype: str
        """
        return self._PublicDataStreamStatus

    @PublicDataStreamStatus.setter
    def PublicDataStreamStatus(self, PublicDataStreamStatus):
        self._PublicDataStreamStatus = PublicDataStreamStatus

    @property
    def PublicClbId(self):
        r"""Public network CLB instance ID
        :rtype: str
        """
        return self._PublicClbId

    @PublicClbId.setter
    def PublicClbId(self, PublicClbId):
        self._PublicClbId = PublicClbId


    def _deserialize(self, params):
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        self._PublicDataStreamStatus = params.get("PublicDataStreamStatus")
        self._PublicClbId = params.get("PublicClbId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessEndpoint(AbstractModel):
    r"""Access point.

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _SubnetId: subnet id
        :type SubnetId: str
        :param _VpcEndpoint: Access address
        :type VpcEndpoint: str
        :param _VpcDataStreamEndpointStatus: Access address status.
        :type VpcDataStreamEndpointStatus: str
        :param _PublicNetwork: Whether it is a public network.
        :type PublicNetwork: bool
        :param _AccessStrategy: Specifies the access policy.
        :type AccessStrategy: str
        :param _Bandwidth: Bandwidth
        :type Bandwidth: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._VpcEndpoint = None
        self._VpcDataStreamEndpointStatus = None
        self._PublicNetwork = None
        self._AccessStrategy = None
        self._Bandwidth = None

    @property
    def VpcId(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""subnet id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcEndpoint(self):
        r"""Access address
        :rtype: str
        """
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint

    @property
    def VpcDataStreamEndpointStatus(self):
        r"""Access address status.
        :rtype: str
        """
        return self._VpcDataStreamEndpointStatus

    @VpcDataStreamEndpointStatus.setter
    def VpcDataStreamEndpointStatus(self, VpcDataStreamEndpointStatus):
        self._VpcDataStreamEndpointStatus = VpcDataStreamEndpointStatus

    @property
    def PublicNetwork(self):
        r"""Whether it is a public network.
        :rtype: bool
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def AccessStrategy(self):
        r"""Specifies the access policy.
        :rtype: str
        """
        return self._AccessStrategy

    @AccessStrategy.setter
    def AccessStrategy(self, AccessStrategy):
        self._AccessStrategy = AccessStrategy

    @property
    def Bandwidth(self):
        r"""Bandwidth
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VpcEndpoint = params.get("VpcEndpoint")
        self._VpcDataStreamEndpointStatus = params.get("VpcDataStreamEndpointStatus")
        self._PublicNetwork = params.get("PublicNetwork")
        self._AccessStrategy = params.get("AccessStrategy")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessInstance(AbstractModel):
    r"""TDMQ for rabbitmq serverless instance.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceVersion: Instance version.
        :type InstanceVersion: str
        :param _Status: Instance status. 0 indicates creating in progress. 1 indicates normal. 2 indicates isolated. 3 indicates terminated. 4 indicates exception. 5 indicates delivery failed.
        :type Status: int
        :param _MaxTps: MaxTPS
        :type MaxTps: int
        :param _MaxBandWidth: MaxBandwidth
        :type MaxBandWidth: int
        :param _ExpireTime: Expiration time of the cluster.
        :type ExpireTime: int
        :param _AutoRenewFlag: Auto-renewal flag. 0 indicates the default status (If the default status is not configured, manual renewal is enabled), 1 indicates auto-renewal, and 2 indicates explicitly no auto-renewal (configured by the user).
        :type AutoRenewFlag: int
        :param _PayMode: 0: Postpaid, 1: Prepaid
        :type PayMode: int
        :param _Remark: Remarks
        :type Remark: str
        :param _SpecName: Cluster specifications
        :type SpecName: str
        :param _ExceptionInformation: Exception information.
        :type ExceptionInformation: str
        :param _PublicAccessEndpoint: Public network access point.
        :type PublicAccessEndpoint: str
        :param _Vpcs: The virtual private cloud (vpc) network access point.
        :type Vpcs: list of RabbitMQServerlessEndpoint
        :param _ClusterStatus: Instance status. 0 indicates creating in progress. 1 indicates normal. 2 indicates isolated. 3 indicates terminated. 4 indicates exception. 5 indicates delivery failed.

        :type ClusterStatus: int
        :param _InstanceType: Specifies the cluster type: 1.
        :type InstanceType: int
        :param _CreateTime: Expiration time
        :type CreateTime: int
        :param _NodeCount: For compatibility with the managed version, the fixed value is 0.
        :type NodeCount: int
        :param _MaxStorage: For compatibility with the managed version, the fixed value is 0.
        :type MaxStorage: int
        :param _IsolatedTime: Isolation time
        :type IsolatedTime: int
        :param _ServerlessExt: Serverless Extension Fields
        :type ServerlessExt: str
        :param _Tags: Instance tag list.
        :type Tags: list of RabbitMQServerlessTag
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ExceptionInformation = None
        self._PublicAccessEndpoint = None
        self._Vpcs = None
        self._ClusterStatus = None
        self._InstanceType = None
        self._CreateTime = None
        self._NodeCount = None
        self._MaxStorage = None
        self._IsolatedTime = None
        self._ServerlessExt = None
        self._Tags = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceVersion(self):
        r"""Instance version.
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        r"""Instance status. 0 indicates creating in progress. 1 indicates normal. 2 indicates isolated. 3 indicates terminated. 4 indicates exception. 5 indicates delivery failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxTps(self):
        r"""MaxTPS
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        r"""MaxBandwidth
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def ExpireTime(self):
        r"""Expiration time of the cluster.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        r"""Auto-renewal flag. 0 indicates the default status (If the default status is not configured, manual renewal is enabled), 1 indicates auto-renewal, and 2 indicates explicitly no auto-renewal (configured by the user).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PayMode(self):
        r"""0: Postpaid, 1: Prepaid
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        r"""Cluster specifications
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ExceptionInformation(self):
        r"""Exception information.
        :rtype: str
        """
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation

    @property
    def PublicAccessEndpoint(self):
        r"""Public network access point.
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def Vpcs(self):
        r"""The virtual private cloud (vpc) network access point.
        :rtype: list of RabbitMQServerlessEndpoint
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def ClusterStatus(self):
        r"""Instance status. 0 indicates creating in progress. 1 indicates normal. 2 indicates isolated. 3 indicates terminated. 4 indicates exception. 5 indicates delivery failed.

        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def InstanceType(self):
        r"""Specifies the cluster type: 1.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CreateTime(self):
        r"""Expiration time
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NodeCount(self):
        r"""For compatibility with the managed version, the fixed value is 0.
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def MaxStorage(self):
        r"""For compatibility with the managed version, the fixed value is 0.
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def IsolatedTime(self):
        r"""Isolation time
        :rtype: int
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ServerlessExt(self):
        r"""Serverless Extension Fields
        :rtype: str
        """
        return self._ServerlessExt

    @ServerlessExt.setter
    def ServerlessExt(self, ServerlessExt):
        self._ServerlessExt = ServerlessExt

    @property
    def Tags(self):
        r"""Instance tag list.
        :rtype: list of RabbitMQServerlessTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ExceptionInformation = params.get("ExceptionInformation")
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = RabbitMQServerlessEndpoint()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._ClusterStatus = params.get("ClusterStatus")
        self._InstanceType = params.get("InstanceType")
        self._CreateTime = params.get("CreateTime")
        self._NodeCount = params.get("NodeCount")
        self._MaxStorage = params.get("MaxStorage")
        self._IsolatedTime = params.get("IsolatedTime")
        self._ServerlessExt = params.get("ServerlessExt")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RabbitMQServerlessTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessKeyValuePair(AbstractModel):
    r"""Key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: Key.
        :type Key: str
        :param _Value: Value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value.
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
        


class RabbitMQServerlessTag(AbstractModel):
    r"""Tag.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.
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
        


class RabbitMQServerlessWhiteListInfo(AbstractModel):
    r"""Public network allowlist information.

    """

    def __init__(self):
        r"""
        :param _PublicDataStreamWhiteList: Public network data stream allowlist.
        :type PublicDataStreamWhiteList: str
        :param _PublicDataStreamWhiteListStatus: Public network data stream allowlist status.
        :type PublicDataStreamWhiteListStatus: str
        """
        self._PublicDataStreamWhiteList = None
        self._PublicDataStreamWhiteListStatus = None

    @property
    def PublicDataStreamWhiteList(self):
        r"""Public network data stream allowlist.
        :rtype: str
        """
        return self._PublicDataStreamWhiteList

    @PublicDataStreamWhiteList.setter
    def PublicDataStreamWhiteList(self, PublicDataStreamWhiteList):
        self._PublicDataStreamWhiteList = PublicDataStreamWhiteList

    @property
    def PublicDataStreamWhiteListStatus(self):
        r"""Public network data stream allowlist status.
        :rtype: str
        """
        return self._PublicDataStreamWhiteListStatus

    @PublicDataStreamWhiteListStatus.setter
    def PublicDataStreamWhiteListStatus(self, PublicDataStreamWhiteListStatus):
        self._PublicDataStreamWhiteListStatus = PublicDataStreamWhiteListStatus


    def _deserialize(self, params):
        self._PublicDataStreamWhiteList = params.get("PublicDataStreamWhiteList")
        self._PublicDataStreamWhiteListStatus = params.get("PublicDataStreamWhiteListStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQUser(AbstractModel):
    r"""RabbitMQ user info detail.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _User: Specifies the username used when logging in.
        :type User: str
        :param _Password: Password. specifies the password used when logging in.
        :type Password: str
        :param _Description: User description
        :type Description: str
        :param _Tags: User tag. specifies to determine the access permission scope of this user to RabbitMQ Management.
        :type Tags: list of str
        :param _CreateTime: User creation time
        :type CreateTime: str
        :param _ModifyTime: Last modification time of the user.
        :type ModifyTime: str
        :param _Type: Type of User. specifies that "System" indicates System creation and "User" indicates User-created.
        :type Type: str
        :param _MaxConnections: Specifies the maximum number of connections allowed for this user.
        :type MaxConnections: int
        :param _MaxChannels: The maximum number of channels allowed for this user.
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Type = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        r"""Specifies the username used when logging in.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""Password. specifies the password used when logging in.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""User description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""User tag. specifies to determine the access permission scope of this user to RabbitMQ Management.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        r"""User creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Last modification time of the user.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Type(self):
        r"""Type of User. specifies that "System" indicates System creation and "User" indicates User-created.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MaxConnections(self):
        r"""Specifies the maximum number of connections allowed for this user.
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        r"""The maximum number of channels allowed for this user.
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Type = params.get("Type")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQVirtualHostInfo(AbstractModel):
    r"""RabbitMQ vhost detail.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID
        :type InstanceId: str
        :param _VirtualHost: Vhost name.
        :type VirtualHost: str
        :param _Description: Specifies the description information of the vhost.
        :type Description: str
        :param _Tags: Specifies the Tag of the vhost.
        :type Tags: list of str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        :param _VirtualHostStatistics: Specifies the overview statistics information of the vhost.
        :type VirtualHostStatistics: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQVirtualHostStatistics`
        :param _Status: vhost status. specifies the status that corresponds to the native console and can be running, partial, stopped, or unknown.
        :type Status: str
        :param _MessageHeapCount: Specifies the number of message backlogs.
        :type MessageHeapCount: int
        :param _MessageRateIn: Input message rate.
        :type MessageRateIn: float
        :param _MessageRateOut: Output message rate.
        :type MessageRateOut: float
        :param _MirrorQueuePolicyFlag: Specifies whether a mirrored queue policy exists. true indicates existence, and false indicates non-existence.
        :type MirrorQueuePolicyFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._Tags = None
        self._CreateTime = None
        self._ModifyTime = None
        self._VirtualHostStatistics = None
        self._Status = None
        self._MessageHeapCount = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._MirrorQueuePolicyFlag = None

    @property
    def InstanceId(self):
        r"""instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        r"""Vhost name.
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        r"""Specifies the description information of the vhost.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""Specifies the Tag of the vhost.
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def VirtualHostStatistics(self):
        r"""Specifies the overview statistics information of the vhost.
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQVirtualHostStatistics`
        """
        return self._VirtualHostStatistics

    @VirtualHostStatistics.setter
    def VirtualHostStatistics(self, VirtualHostStatistics):
        self._VirtualHostStatistics = VirtualHostStatistics

    @property
    def Status(self):
        r"""vhost status. specifies the status that corresponds to the native console and can be running, partial, stopped, or unknown.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageHeapCount(self):
        r"""Specifies the number of message backlogs.
        :rtype: int
        """
        return self._MessageHeapCount

    @MessageHeapCount.setter
    def MessageHeapCount(self, MessageHeapCount):
        self._MessageHeapCount = MessageHeapCount

    @property
    def MessageRateIn(self):
        r"""Input message rate.
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        r"""Output message rate.
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def MirrorQueuePolicyFlag(self):
        r"""Specifies whether a mirrored queue policy exists. true indicates existence, and false indicates non-existence.
        :rtype: bool
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("VirtualHostStatistics") is not None:
            self._VirtualHostStatistics = RabbitMQVirtualHostStatistics()
            self._VirtualHostStatistics._deserialize(params.get("VirtualHostStatistics"))
        self._Status = params.get("Status")
        self._MessageHeapCount = params.get("MessageHeapCount")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQVirtualHostStatistics(AbstractModel):
    r"""vhost overview statistical information.

    """

    def __init__(self):
        r"""
        :param _CurrentQueues: Number of queues of the current vhost.
        :type CurrentQueues: int
        :param _CurrentExchanges: Number of exchanges in the current vhost.
        :type CurrentExchanges: int
        :param _CurrentConnections: Number of current connections of the vhost.
        :type CurrentConnections: int
        :param _CurrentChannels: Number of channels for the current vhost.
        :type CurrentChannels: int
        :param _CurrentUsers: Number of users of the current vhost.
        :type CurrentUsers: int
        """
        self._CurrentQueues = None
        self._CurrentExchanges = None
        self._CurrentConnections = None
        self._CurrentChannels = None
        self._CurrentUsers = None

    @property
    def CurrentQueues(self):
        r"""Number of queues of the current vhost.
        :rtype: int
        """
        return self._CurrentQueues

    @CurrentQueues.setter
    def CurrentQueues(self, CurrentQueues):
        self._CurrentQueues = CurrentQueues

    @property
    def CurrentExchanges(self):
        r"""Number of exchanges in the current vhost.
        :rtype: int
        """
        return self._CurrentExchanges

    @CurrentExchanges.setter
    def CurrentExchanges(self, CurrentExchanges):
        self._CurrentExchanges = CurrentExchanges

    @property
    def CurrentConnections(self):
        r"""Number of current connections of the vhost.
        :rtype: int
        """
        return self._CurrentConnections

    @CurrentConnections.setter
    def CurrentConnections(self, CurrentConnections):
        self._CurrentConnections = CurrentConnections

    @property
    def CurrentChannels(self):
        r"""Number of channels for the current vhost.
        :rtype: int
        """
        return self._CurrentChannels

    @CurrentChannels.setter
    def CurrentChannels(self, CurrentChannels):
        self._CurrentChannels = CurrentChannels

    @property
    def CurrentUsers(self):
        r"""Number of users of the current vhost.
        :rtype: int
        """
        return self._CurrentUsers

    @CurrentUsers.setter
    def CurrentUsers(self, CurrentUsers):
        self._CurrentUsers = CurrentUsers


    def _deserialize(self, params):
        self._CurrentQueues = params.get("CurrentQueues")
        self._CurrentExchanges = params.get("CurrentExchanges")
        self._CurrentConnections = params.get("CurrentConnections")
        self._CurrentChannels = params.get("CurrentChannels")
        self._CurrentUsers = params.get("CurrentUsers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserQuota(AbstractModel):
    r"""Number of users quota.

    """

    def __init__(self):
        r"""
        :param _MaxUser: Maximum number of users.
        :type MaxUser: int
        :param _UsedUser: Used number of users.
        :type UsedUser: int
        """
        self._MaxUser = None
        self._UsedUser = None

    @property
    def MaxUser(self):
        r"""Maximum number of users.
        :rtype: int
        """
        return self._MaxUser

    @MaxUser.setter
    def MaxUser(self, MaxUser):
        self._MaxUser = MaxUser

    @property
    def UsedUser(self):
        r"""Used number of users.
        :rtype: int
        """
        return self._UsedUser

    @UsedUser.setter
    def UsedUser(self, UsedUser):
        self._UsedUser = UsedUser


    def _deserialize(self, params):
        self._MaxUser = params.get("MaxUser")
        self._UsedUser = params.get("UsedUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualHostQuota(AbstractModel):
    r"""Virtual host quota.

    """

    def __init__(self):
        r"""
        :param _MaxVirtualHost: Maximum number of virtual hosts.
        :type MaxVirtualHost: int
        :param _UsedVirtualHost: Number of already used virtual hosts.
        :type UsedVirtualHost: int
        """
        self._MaxVirtualHost = None
        self._UsedVirtualHost = None

    @property
    def MaxVirtualHost(self):
        r"""Maximum number of virtual hosts.
        :rtype: int
        """
        return self._MaxVirtualHost

    @MaxVirtualHost.setter
    def MaxVirtualHost(self, MaxVirtualHost):
        self._MaxVirtualHost = MaxVirtualHost

    @property
    def UsedVirtualHost(self):
        r"""Number of already used virtual hosts.
        :rtype: int
        """
        return self._UsedVirtualHost

    @UsedVirtualHost.setter
    def UsedVirtualHost(self, UsedVirtualHost):
        self._UsedVirtualHost = UsedVirtualHost


    def _deserialize(self, params):
        self._MaxVirtualHost = params.get("MaxVirtualHost")
        self._UsedVirtualHost = params.get("UsedVirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcEndpointInfo(AbstractModel):
    r"""VPC access point information

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _VpcEndpoint: vpc access point information.
        :type VpcEndpoint: str
        :param _VpcDataStreamEndpointStatus: vpc access point status.
OFF/ON/CREATING/DELETING
        :type VpcDataStreamEndpointStatus: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._VpcEndpoint = None
        self._VpcDataStreamEndpointStatus = None

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcEndpoint(self):
        r"""vpc access point information.
        :rtype: str
        """
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint

    @property
    def VpcDataStreamEndpointStatus(self):
        r"""vpc access point status.
OFF/ON/CREATING/DELETING
        :rtype: str
        """
        return self._VpcDataStreamEndpointStatus

    @VpcDataStreamEndpointStatus.setter
    def VpcDataStreamEndpointStatus(self, VpcDataStreamEndpointStatus):
        self._VpcDataStreamEndpointStatus = VpcDataStreamEndpointStatus


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VpcEndpoint = params.get("VpcEndpoint")
        self._VpcDataStreamEndpointStatus = params.get("VpcDataStreamEndpointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        