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


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueueName: DeadLetterQueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueueName: str
        :param _DeadLetterQueue: DeadLetterQueue
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueue: str
        :param _Policy: Policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type Policy: int
        :param _MaxTimeToLive: MaxTimeToLive
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: MaxReceiveCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueueName = None
        self._DeadLetterQueue = None
        self._Policy = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None

    @property
    def DeadLetterQueueName(self):
        """DeadLetterQueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def DeadLetterQueue(self):
        """DeadLetterQueue
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeadLetterQueue

    @DeadLetterQueue.setter
    def DeadLetterQueue(self, DeadLetterQueue):
        self._DeadLetterQueue = DeadLetterQueue

    @property
    def Policy(self):
        """Policy
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxTimeToLive(self):
        """MaxTimeToLive
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        """MaxReceiveCount
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount


    def _deserialize(self, params):
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._DeadLetterQueue = params.get("DeadLetterQueue")
        self._Policy = params.get("Policy")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        r"""
        :param _QueueId: QueueId
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueId: str
        :param _QueueName: QueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueName: str
        """
        self._QueueId = None
        self._QueueName = None

    @property
    def QueueId(self):
        """QueueId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        """QueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _Filters: Filter parameter. Currently, filtering by `QueueName` is supported, and only one keyword is allowed
        :type Filters: list of Filter
        :param _TagKey: Tag search
        :type TagKey: str
        :param _QueueName: Exact match by `QueueName`
        :type QueueName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._QueueName = None

    @property
    def Offset(self):
        """Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter parameter. Currently, filtering by `QueueName` is supported, and only one keyword is allowed
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        """Tag search
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def QueueName(self):
        """Exact match by `QueueName`
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of queues
        :type TotalCount: int
        :param _QueueSet: Queue list
        :type QueueSet: list of QueueSet
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of queues
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        """Queue list
        :rtype: list of QueueSet
        """
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

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
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _Filters: Currently, only filtering by `TopicName` is supported, and only one filter value can be entered
        :type Filters: list of Filter
        :param _TagKey: Tag match
        :type TagKey: str
        :param _TopicName: Exact match by `TopicName`
        :type TopicName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._TopicName = None

    @property
    def Offset(self):
        """Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Currently, only filtering by `TopicName` is supported, and only one filter value can be entered
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        """Tag match
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TopicName(self):
        """Exact match by `TopicName`
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: TotalCount
        :type TotalCount: int
        :param _TopicSet: TopicSet
        :type TopicSet: list of TopicSet
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """TotalCount
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicSet(self):
        """TopicSet
        :rtype: list of TopicSet
        """
        return self._TopicSet

    @TopicSet.setter
    def TopicSet(self, TopicSet):
        self._TopicSet = TopicSet

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
        if params.get("TopicSet") is not None:
            self._TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self._TopicSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        r"""
        :param _Name: Filter parameter name
        :type Name: str
        :param _Values: Value
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Filter parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Value
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
        


class QueueSet(AbstractModel):
    """Batch queue attribute information

    """

    def __init__(self):
        r"""
        :param _QueueId: QueueId
        :type QueueId: str
        :param _QueueName: QueueName
        :type QueueName: str
        :param _Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _Bps: Bps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bps: int
        :param _MaxDelaySeconds: MaxDelaySeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDelaySeconds: int
        :param _MaxMsgHeapNum: MaxMsgHeapNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: PollingWaitSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type PollingWaitSeconds: int
        :param _MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _VisibilityTimeout: VisibilityTimeout
Note: this field may return null, indicating that no valid values can be obtained.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _RewindSeconds: RewindSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindSeconds: int
        :param _CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _ActiveMsgNum: ActiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActiveMsgNum: int
        :param _InactiveMsgNum: InactiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type InactiveMsgNum: int
        :param _DelayMsgNum: DelayMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type DelayMsgNum: int
        :param _RewindMsgNum: RewindMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindMsgNum: int
        :param _MinMsgTime: MinMsgTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinMsgTime: int
        :param _Transaction: Transaction
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transaction: bool
        :param _DeadLetterSource: DeadLetterSource
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterSource: list of DeadLetterSource
        :param _DeadLetterPolicy: DeadLetterPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param _TransactionPolicy: TransactionPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param _CreateUin: Creator `uin`
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Message trace flag. true: enabled, false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        """
        self._QueueId = None
        self._QueueName = None
        self._Qps = None
        self._Bps = None
        self._MaxDelaySeconds = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._MsgRetentionSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._RewindSeconds = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._ActiveMsgNum = None
        self._InactiveMsgNum = None
        self._DelayMsgNum = None
        self._RewindMsgNum = None
        self._MinMsgTime = None
        self._Transaction = None
        self._DeadLetterSource = None
        self._DeadLetterPolicy = None
        self._TransactionPolicy = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None

    @property
    def QueueId(self):
        """QueueId
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        """QueueName
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Qps(self):
        """Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Bps(self):
        """Bps
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Bps

    @Bps.setter
    def Bps(self, Bps):
        self._Bps = Bps

    @property
    def MaxDelaySeconds(self):
        """MaxDelaySeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDelaySeconds

    @MaxDelaySeconds.setter
    def MaxDelaySeconds(self, MaxDelaySeconds):
        self._MaxDelaySeconds = MaxDelaySeconds

    @property
    def MaxMsgHeapNum(self):
        """MaxMsgHeapNum
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        """PollingWaitSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def MsgRetentionSeconds(self):
        """MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def VisibilityTimeout(self):
        """VisibilityTimeout
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        """MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def RewindSeconds(self):
        """RewindSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def CreateTime(self):
        """CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        """LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def ActiveMsgNum(self):
        """ActiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ActiveMsgNum

    @ActiveMsgNum.setter
    def ActiveMsgNum(self, ActiveMsgNum):
        self._ActiveMsgNum = ActiveMsgNum

    @property
    def InactiveMsgNum(self):
        """InactiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InactiveMsgNum

    @InactiveMsgNum.setter
    def InactiveMsgNum(self, InactiveMsgNum):
        self._InactiveMsgNum = InactiveMsgNum

    @property
    def DelayMsgNum(self):
        """DelayMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DelayMsgNum

    @DelayMsgNum.setter
    def DelayMsgNum(self, DelayMsgNum):
        self._DelayMsgNum = DelayMsgNum

    @property
    def RewindMsgNum(self):
        """RewindMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RewindMsgNum

    @RewindMsgNum.setter
    def RewindMsgNum(self, RewindMsgNum):
        self._RewindMsgNum = RewindMsgNum

    @property
    def MinMsgTime(self):
        """MinMsgTime
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinMsgTime

    @MinMsgTime.setter
    def MinMsgTime(self, MinMsgTime):
        self._MinMsgTime = MinMsgTime

    @property
    def Transaction(self):
        """Transaction
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def DeadLetterSource(self):
        """DeadLetterSource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DeadLetterSource
        """
        return self._DeadLetterSource

    @DeadLetterSource.setter
    def DeadLetterSource(self, DeadLetterSource):
        self._DeadLetterSource = DeadLetterSource

    @property
    def DeadLetterPolicy(self):
        """DeadLetterPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        """
        return self._DeadLetterPolicy

    @DeadLetterPolicy.setter
    def DeadLetterPolicy(self, DeadLetterPolicy):
        self._DeadLetterPolicy = DeadLetterPolicy

    @property
    def TransactionPolicy(self):
        """TransactionPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        """
        return self._TransactionPolicy

    @TransactionPolicy.setter
    def TransactionPolicy(self, TransactionPolicy):
        self._TransactionPolicy = TransactionPolicy

    @property
    def CreateUin(self):
        """Creator `uin`
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        """Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        """Message trace flag. true: enabled, false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        self._Qps = params.get("Qps")
        self._Bps = params.get("Bps")
        self._MaxDelaySeconds = params.get("MaxDelaySeconds")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._RewindSeconds = params.get("RewindSeconds")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._ActiveMsgNum = params.get("ActiveMsgNum")
        self._InactiveMsgNum = params.get("InactiveMsgNum")
        self._DelayMsgNum = params.get("DelayMsgNum")
        self._RewindMsgNum = params.get("RewindMsgNum")
        self._MinMsgTime = params.get("MinMsgTime")
        self._Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self._DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self._DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self._DeadLetterPolicy = DeadLetterPolicy()
            self._DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self._TransactionPolicy = TransactionPolicy()
            self._TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
Note: this field may return null, indicating that no valid values can be obtained.
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
        


class TopicSet(AbstractModel):
    """Field for displaying returned topic information

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicId
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _TopicName: TopicName
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _FilterType: FilterType
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: int
        :param _CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _MsgCount: MsgCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param _CreateUin: CreateUin
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Tags
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Whether to enable message trace for a topic. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        """
        self._TopicId = None
        self._TopicName = None
        self._MsgRetentionSeconds = None
        self._MaxMsgSize = None
        self._Qps = None
        self._FilterType = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._MsgCount = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None

    @property
    def TopicId(self):
        """TopicId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """TopicName
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgRetentionSeconds(self):
        """MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def MaxMsgSize(self):
        """MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def Qps(self):
        """Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def FilterType(self):
        """FilterType
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def CreateTime(self):
        """CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        """LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def MsgCount(self):
        """MsgCount
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def CreateUin(self):
        """CreateUin
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        """Tags
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        """Whether to enable message trace for a topic. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._Qps = params.get("Qps")
        self._FilterType = params.get("FilterType")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._MsgCount = params.get("MsgCount")
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        r"""
        :param _FirstQueryInterval: FirstQueryInterval
Note: this field may return null, indicating that no valid values can be obtained.
        :type FirstQueryInterval: int
        :param _MaxQueryCount: MaxQueryCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxQueryCount: int
        """
        self._FirstQueryInterval = None
        self._MaxQueryCount = None

    @property
    def FirstQueryInterval(self):
        """FirstQueryInterval
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        """MaxQueryCount
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount


    def _deserialize(self, params):
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        