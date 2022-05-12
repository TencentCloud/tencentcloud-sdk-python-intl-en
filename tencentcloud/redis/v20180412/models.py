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


class Account(AbstractModel):
    """Sub-account information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param AccountName: Account name (`root` for a root account)
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        :param Remark: Account description information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param Privilege: Read/write policy. r: read-only; w: write-only; rw: read/write
Note: This field may return null, indicating that no valid values can be obtained.
        :type Privilege: str
        :param ReadonlyPolicy: Routing policy. master: master node; replication: secondary node
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadonlyPolicy: list of str
        :param Status: Sub-account status. 1: account is being changed; 2: account is valid; -4: account has been deleted
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self.InstanceId = None
        self.AccountName = None
        self.Remark = None
        self.Privilege = None
        self.ReadonlyPolicy = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.Privilege = params.get("Privilege")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateWanAddressRequest(AbstractModel):
    """AllocateWanAddress request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateWanAddressResponse(AbstractModel):
    """AllocateWanAddress response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async task ID
        :type FlowId: int
        :param WanStatus: Status of enabling public network access
        :type WanStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.WanStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.WanStatus = params.get("WanStatus")
        self.RequestId = params.get("RequestId")


class BigKeyInfo(AbstractModel):
    """Big key details

    """

    def __init__(self):
        r"""
        :param DB: Database
        :type DB: int
        :param Key: Big key
        :type Key: str
        :param Type: Type
        :type Type: str
        :param Size: Size
        :type Size: int
        :param Updatetime: Data timestamp
        :type Updatetime: int
        """
        self.DB = None
        self.Key = None
        self.Type = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.DB = params.get("DB")
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyTypeInfo(AbstractModel):
    """Big key type distribution details

    """

    def __init__(self):
        r"""
        :param Type: Type
        :type Type: str
        :param Count: Count
        :type Count: int
        :param Size: Size
        :type Size: int
        :param Updatetime: Timestamp
        :type Updatetime: int
        """
        self.Type = None
        self.Count = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterRequest(AbstractModel):
    """ChangeReplicaToMaster request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param GroupId: Replica group ID, which is required for multi-AZ instances.
        :type GroupId: int
        """
        self.InstanceId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterResponse(AbstractModel):
    """ChangeReplicaToMaster response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Async task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CommandTake(AbstractModel):
    """Command duration

    """

    def __init__(self):
        r"""
        :param Cmd: Command
        :type Cmd: str
        :param Took: Duration
        :type Took: int
        """
        self.Cmd = None
        self.Took = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Took = params.get("Took")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelayDistribution(AbstractModel):
    """Delay distribution details

    """

    def __init__(self):
        r"""
        :param Ladder: Delay distribution. The mapping between delay range and `Ladder` value is as follows:
[0ms,1ms]: 1;
[1ms,5ms]: 5;
[5ms,10ms]: 10;
[10ms,50ms]: 50;
[50ms,200ms]: 200;
[200ms,∞]: -1.
        :type Ladder: int
        :param Size: The number of commands whose delay falls within the current delay range
        :type Size: int
        :param Updatetime: Modification time
        :type Updatetime: int
        """
        self.Ladder = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Ladder = params.get("Ladder")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAccountRequest(AbstractModel):
    """DescribeInstanceAccount request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAccountResponse(AbstractModel):
    """DescribeInstanceAccount response structure.

    """

    def __init__(self):
        r"""
        :param Accounts: Account details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Accounts: list of Account
        :param TotalCount: Number of accounts
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Accounts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    """DescribeInstanceMonitorBigKey request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ReqType: Request type. 1: string type; 2: all types
        :type ReqType: int
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.ReqType = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReqType = params.get("ReqType")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyResponse(AbstractModel):
    """DescribeInstanceMonitorBigKey response structure.

    """

    def __init__(self):
        r"""
        :param Data: Big key details
        :type Data: list of BigKeyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeySizeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeySizeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist response structure.

    """

    def __init__(self):
        r"""
        :param Data: Big key size distribution details
        :type Data: list of DelayDistribution
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyTypeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyTypeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist response structure.

    """

    def __init__(self):
        r"""
        :param Data: Big key type distribution details
        :type Data: list of BigKeyTypeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyTypeInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorHotKeyRequest(AbstractModel):
    """DescribeInstanceMonitorHotKey request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: past 30 minutes; 3: past 6 hours; 4: past 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorHotKeyResponse(AbstractModel):
    """DescribeInstanceMonitorHotKey response structure.

    """

    def __init__(self):
        r"""
        :param Data: Hot key details
        :type Data: list of HotKeyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = HotKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorSIPRequest(AbstractModel):
    """DescribeInstanceMonitorSIP request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorSIPResponse(AbstractModel):
    """DescribeInstanceMonitorSIP response structure.

    """

    def __init__(self):
        r"""
        :param Data: Access source information
        :type Data: list of SourceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTookDistRequest(AbstractModel):
    """DescribeInstanceMonitorTookDist request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Date: Time, such as "20190219"
        :type Date: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.Date = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTookDistResponse(AbstractModel):
    """DescribeInstanceMonitorTookDist response structure.

    """

    def __init__(self):
        r"""
        :param Data: Latency distribution information
        :type Data: list of DelayDistribution
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmd request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmd response structure.

    """

    def __init__(self):
        r"""
        :param Data: Access command information
        :type Data: list of SourceCommand
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceCommand()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdTookRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdTookResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook response structure.

    """

    def __init__(self):
        r"""
        :param Data: Duration details
        :type Data: list of CommandTake
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CommandTake()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: List size
        :type Limit: int
        :param Offset: The offset value
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo response structure.

    """

    def __init__(self):
        r"""
        :param ProxyCount: The number of proxy nodes
        :type ProxyCount: int
        :param Proxy: Proxy node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Proxy: list of ProxyNodes
        :param RedisCount: The number of redis nodes
        :type RedisCount: int
        :param Redis: Redis node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Redis: list of RedisNodes
        :param TendisCount: The number of tendis nodes
        :type TendisCount: int
        :param Tendis: Tendis node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Tendis: list of TendisNodes
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyCount = None
        self.Proxy = None
        self.RedisCount = None
        self.Redis = None
        self.TendisCount = None
        self.Tendis = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self.Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodes()
                obj._deserialize(item)
                self.Proxy.append(obj)
        self.RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self.Redis = []
            for item in params.get("Redis"):
                obj = RedisNodes()
                obj._deserialize(item)
                self.Redis.append(obj)
        self.TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self.Tendis = []
            for item in params.get("Tendis"):
                obj = TendisNodes()
                obj._deserialize(item)
                self.Tendis.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    """DescribeMaintenanceWindow request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    """DescribeMaintenanceWindow response structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the maintenance window, such as 17:00.
        :type StartTime: str
        :param EndTime: End time of the maintenance window, such as 19:00.
        :type EndTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo request structure.

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo response structure.

    """

    def __init__(self):
        r"""
        :param RegionSet: Sale information of a region
        :type RegionSet: list of RegionConf
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReplicationGroupRequest(AbstractModel):
    """DescribeReplicationGroup request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Instance list size. Default value: 20
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        :param GroupId: Replication group ID
        :type GroupId: str
        :param SearchKey: Instance ID/name. Fuzzy query is supported.
        :type SearchKey: str
        """
        self.Limit = None
        self.Offset = None
        self.GroupId = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.GroupId = params.get("GroupId")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationGroupResponse(AbstractModel):
    """DescribeReplicationGroup response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of replication group
        :type TotalCount: int
        :param Groups: Replication group info
        :type Groups: list of Groups
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = Groups()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param BeginTime: Start time
        :type BeginTime: str
        :param EndTime: End time
        :type EndTime: str
        :param MinQueryTime: Slow log threshold in microseconds
        :type MinQueryTime: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Offset, which is an integral multiple of `Limit`
        :type Offset: int
        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of slow logs
        :type TotalCount: int
        :param InstanceSlowlogDetail: Slow log details
        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSlowlogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSlowlogDetail") is not None:
            self.InstanceSlowlogDetail = []
            for item in params.get("InstanceSlowlogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self.InstanceSlowlogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class Groups(AbstractModel):
    """Replication group info

    """

    def __init__(self):
        r"""
        :param AppId: User App ID
        :type AppId: int
        :param RegionId: Region ID. 1: Guangzhou; 4: Shanghai; 5: Hong Kong (China); 6: Toronto; 7: Shanghai Finance; 8: Beijing; 9: Singapore; 11: Shenzhen Finance; 15: West US (Silicon Valley); 16: Chengdu; 17: Germany; 18: South Korea; 19: Chongqing; 21: India; 22: East US (Virginia); 23: Thailand; 24: Russia; 25: Japan
        :type RegionId: int
        :param GroupId: Replication group info
        :type GroupId: str
        :param GroupName: Replication group name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type GroupName: str
        :param Status: Replication group status. Valid values: 37 (Associating replication group), 38 (Reconnecting to replication group), 51 (Disassociating the replication group), 52 (Switching primary instance in the replication group), 53 (Modifying roles)
        :type Status: int
        :param InstanceCount: Number of replication groups
        :type InstanceCount: int
        :param Instances: Instances in replication group
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Instances: list of Instances
        :param Remark: Remarks
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self.AppId = None
        self.RegionId = None
        self.GroupId = None
        self.GroupName = None
        self.Status = None
        self.InstanceCount = None
        self.Instances = None
        self.Remark = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.RegionId = params.get("RegionId")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Status = params.get("Status")
        self.InstanceCount = params.get("InstanceCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instances()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HotKeyInfo(AbstractModel):
    """Hot key details

    """

    def __init__(self):
        r"""
        :param Key: Hot key
        :type Key: str
        :param Type: Type
        :type Type: str
        :param Count: Count
        :type Count: int
        """
        self.Key = None
        self.Type = None
        self.Count = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param TypeId: Instance type. Valid values: `2` (Redis 2.8 memory edition in standard architecture), `3` (CKV 3.2 memory edition in standard architecture), `4` (CKV 3.2 memory edition in cluster architecture), `6` (Redis 4.0 memory edition in standard architecture), `7` (Redis 4.0 memory edition in cluster architecture), `8` (Redis 5.0 memory edition in standard architecture), `9` (Redis 5.0 memory edition in cluster architecture).
        :type TypeId: int
        :param MemSize: Memory capacity in MB, which must be a multiple of 1,024. It is subject to the purchasable specifications returned by the [DescribeProductInfo API](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1).
If `TypeId` indicates the standard architecture, `MemSize` indicates the total memory capacity of an instance; if `TypeId` indicates the cluster architecture, `MemSize` indicates the memory capacity per shard.
        :type MemSize: int
        :param GoodsNum: Number of instances. The actual quantity purchasable at a time is subject to the specifications returned by the [DescribeProductInfo API](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1).
        :type GoodsNum: int
        :param Period: Length of purchase in months, which is required when creating a monthly-subscribed instance. Value range: [1,2,3,4,5,6,7,8,9,10,11,12,24,36]. For pay-as-you-go instances, set the parameter to `1`.
        :type Period: int
        :param BillingMode: Billing mode. Valid values: `0` (pay-as-you-go), `1` (monthly subscription).
        :type BillingMode: int
        :param ZoneId: ID of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneId: int
        :param RedisShardNum: Instance shard quantity. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, Redis 2.8 standalone edition, and Redis 4.0 standard architecture.
        :type RedisShardNum: int
        :param RedisReplicasNum: Instance replica quantity. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, and Redis 2.8 standalone edition.
        :type RedisReplicasNum: int
        :param ReplicasReadonly: Whether to support read-only replicas. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, and Redis 2.8 standalone edition.
        :type ReplicasReadonly: bool
        :param ZoneName: Name of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneName: str
        """
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.BillingMode = None
        self.ZoneId = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.ReplicasReadonly = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.BillingMode = params.get("BillingMode")
        self.ZoneId = params.get("ZoneId")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.ReplicasReadonly = params.get("ReplicasReadonly")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price. Unit: USD (accurate down to the cent)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Price: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param MemSize: Shard size in MB.
        :type MemSize: int
        :param RedisShardNum: Number of shards. This parameter can be left blank for Redis 2.8 in standard architecture, CKV in standard architecture, and Redis 2.8 in standalone architecture.
        :type RedisShardNum: int
        :param RedisReplicasNum: Number of replicas. This parameter can be left blank for Redis 2.8 in standard architecture, CKV in standard architecture, and Redis 2.8 in standalone architecture.
        :type RedisReplicasNum: int
        """
        self.InstanceId = None
        self.MemSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price. Unit: USD
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Price: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InstanceSlowlogDetail(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        r"""
        :param Duration: Slow log duration
        :type Duration: int
        :param Client: Client address
        :type Client: str
        :param Command: Command
        :type Command: str
        :param CommandLine: Command line details
        :type CommandLine: str
        :param ExecuteTime: Execution duration
        :type ExecuteTime: str
        :param Node: Node ID
        :type Node: str
        """
        self.Duration = None
        self.Client = None
        self.Command = None
        self.CommandLine = None
        self.ExecuteTime = None
        self.Node = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Client = params.get("Client")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.ExecuteTime = params.get("ExecuteTime")
        self.Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instances(AbstractModel):
    """Instances in replication group

    """

    def __init__(self):
        r"""
        :param AppId: User App ID
        :type AppId: int
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param RegionId: Region ID. 1: Guangzhou; 4: Shanghai; 5: Hong Kong (China); 6: Toronto; 7: Shanghai Finance; 8: Beijing; 9: Singapore; 11: Shenzhen Finance; 15: West US (Silicon Valley)
        :type RegionId: int
        :param ZoneId: Region ID
        :type ZoneId: int
        :param RedisReplicasNum: Number of replicas
        :type RedisReplicasNum: int
        :param RedisShardNum: Number of shards
        :type RedisShardNum: int
        :param RedisShardSize: Shard size
        :type RedisShardSize: int
        :param DiskSize: Instance disk size
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param Engine: Engine: Redis community edition, Tencent Cloud CKV
        :type Engine: str
        :param Role: Instance role. Valid values: `rw` (read-write), `r`( read-only)
        :type Role: str
        :param Vip: Instance VIP
        :type Vip: str
        :param Vip6: Internal parameter, which can be ignored.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Vip6: str
        :param VpcID: VPC ID, such as 75101
        :type VpcID: int
        :param VPort: Instance Port
        :type VPort: int
        :param Status: Instance status. 0: to be initialized; 1: in process; 2: running; -2: isolated; -3: to be deleted
        :type Status: int
        :param GrocerySysId: Repository ID
        :type GrocerySysId: int
        :param ProductType: Instance type. Valid values: `1` (Redis 2.8 memory edition in cluster architecture), `2` (Redis 2.8 memory edition in standard architecture), `3` (CKV 3.2 memory edition in standard architecture), `4` (CKV 3.2 memory edition in cluster architecture), `5` (Redis 2.8 memory edition in standalone architecture), `6` (Redis 4.0 memory edition in standard architecture), `7` (Redis 4.0 memory edition in cluster architecture), `8` (Redis 5.0 memory edition in standard architecture), `9` (Redis 5.0 memory edition in cluster architecture)
        :type ProductType: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        """
        self.AppId = None
        self.InstanceId = None
        self.InstanceName = None
        self.RegionId = None
        self.ZoneId = None
        self.RedisReplicasNum = None
        self.RedisShardNum = None
        self.RedisShardSize = None
        self.DiskSize = None
        self.Engine = None
        self.Role = None
        self.Vip = None
        self.Vip6 = None
        self.VpcID = None
        self.VPort = None
        self.Status = None
        self.GrocerySysId = None
        self.ProductType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisShardSize = params.get("RedisShardSize")
        self.DiskSize = params.get("DiskSize")
        self.Engine = params.get("Engine")
        self.Role = params.get("Role")
        self.Vip = params.get("Vip")
        self.Vip6 = params.get("Vip6")
        self.VpcID = params.get("VpcID")
        self.VPort = params.get("VPort")
        self.Status = params.get("Status")
        self.GrocerySysId = params.get("GrocerySysId")
        self.ProductType = params.get("ProductType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param OldPassword: Old password of an instance
        :type OldPassword: str
        :param Password: New password of an instance
        :type Password: str
        """
        self.InstanceId = None
        self.OldPassword = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProductConf(AbstractModel):
    """Product information

    """

    def __init__(self):
        r"""
        :param Type: Product type. Valid values: `2` (Redis 2.8 Memory Edition in standard architecture), `3` (CKV 3.2 Memory Edition in standard architecture), `4` (CKV 3.2 Memory Edition in cluster architecture), `5` (Redis 2.8 Memory Edition in standalone architecture), `6` (Redis 4.0 Memory Edition in standard architecture), `7` (Redis 4.0 Memory Edition in cluster architecture), `8` (Redis 5.0 Memory Edition in standard architecture), `9` (Redis 5.0 Memory Edition in cluster architecture), `10` (Redis 4.0 Hybrid Storage Edition (Tendis)).
        :type Type: int
        :param TypeName: Product name: Redis Master-Replica Edition, CKV Master-Replica Edition, CKV Cluster Edition, Redis Standalone Edition, Redis Cluster Edition, Tendis Hybrid Storage Edition
        :type TypeName: str
        :param MinBuyNum: Minimum purchasable quantity
        :type MinBuyNum: int
        :param MaxBuyNum: Maximum purchasable quantity
        :type MaxBuyNum: int
        :param Saleout: Whether a product is sold out
        :type Saleout: bool
        :param Engine: Product engine: Tencent Cloud CKV or Redis community edition
        :type Engine: str
        :param Version: Compatible version: Redis 2.8, Redis 3.2, or Redis 4.0
        :type Version: str
        :param TotalSize: Total capacity in GB
        :type TotalSize: list of str
        :param ShardSize: Shard size in GB
        :type ShardSize: list of str
        :param ReplicaNum: Number of replicas
        :type ReplicaNum: list of str
        :param ShardNum: Number of shards
        :type ShardNum: list of str
        :param PayMode: Supported billing method. 1: monthly subscription; 0: pay-as-you-go
        :type PayMode: str
        :param EnableRepicaReadOnly: Whether to support read-only replicas
        :type EnableRepicaReadOnly: bool
        """
        self.Type = None
        self.TypeName = None
        self.MinBuyNum = None
        self.MaxBuyNum = None
        self.Saleout = None
        self.Engine = None
        self.Version = None
        self.TotalSize = None
        self.ShardSize = None
        self.ReplicaNum = None
        self.ShardNum = None
        self.PayMode = None
        self.EnableRepicaReadOnly = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.Saleout = params.get("Saleout")
        self.Engine = params.get("Engine")
        self.Version = params.get("Version")
        self.TotalSize = params.get("TotalSize")
        self.ShardSize = params.get("ShardSize")
        self.ReplicaNum = params.get("ReplicaNum")
        self.ShardNum = params.get("ShardNum")
        self.PayMode = params.get("PayMode")
        self.EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodes(AbstractModel):
    """Proxy node information

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NodeId: str
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodes(AbstractModel):
    """Redis node information

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID
        :type NodeId: str
        :param NodeRole: Node role
        :type NodeRole: str
        :param ClusterId: Shard ID
        :type ClusterId: int
        :param ZoneId: AZ ID
        :type ZoneId: int
        """
        self.NodeId = None
        self.NodeRole = None
        self.ClusterId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        self.ClusterId = params.get("ClusterId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID
        :type RegionId: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionShortName: Region abbreviation
        :type RegionShortName: str
        :param Area: Name of the area where a region is located
        :type Area: str
        :param ZoneSet: AZ information
        :type ZoneSet: list of ZoneCapacityConf
        """
        self.RegionId = None
        self.RegionName = None
        self.RegionShortName = None
        self.Area = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionShortName = params.get("RegionShortName")
        self.Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseWanAddressRequest(AbstractModel):
    """ReleaseWanAddress request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseWanAddressResponse(AbstractModel):
    """ReleaseWanAddress response structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Async task ID
        :type FlowId: int
        :param WanStatus: Status of disabling public network access
        :type WanStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.WanStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.WanStatus = params.get("WanStatus")
        self.RequestId = params.get("RequestId")


class SourceCommand(AbstractModel):
    """Access command

    """

    def __init__(self):
        r"""
        :param Cmd: Command
        :type Cmd: str
        :param Count: Number of executions
        :type Count: int
        """
        self.Cmd = None
        self.Count = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    """Access source information

    """

    def __init__(self):
        r"""
        :param Ip: Source IP
        :type Ip: str
        :param Conn: Number of connections
        :type Conn: int
        :param Cmd: Command
        :type Cmd: int
        """
        self.Ip = None
        self.Conn = None
        self.Cmd = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Conn = params.get("Conn")
        self.Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisNodes(AbstractModel):
    """Tendis node information

    """

    def __init__(self):
        r"""
        :param NodeId: Node ID
        :type NodeId: str
        :param NodeRole: Node role
        :type NodeRole: str
        """
        self.NodeId = None
        self.NodeRole = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneCapacityConf(AbstractModel):
    """Product information in the availability zone

    """

    def __init__(self):
        r"""
        :param ZoneId: AZ ID, such as ap-guangzhou-3
        :type ZoneId: str
        :param ZoneName: AZ name
        :type ZoneName: str
        :param IsSaleout: Whether a product is sold out in an AZ
        :type IsSaleout: bool
        :param IsDefault: Whether it is a default AZ
        :type IsDefault: bool
        :param NetWorkType: Network type. basenet: basic network; vpcnet: VPC
        :type NetWorkType: list of str
        :param ProductSet: Information of an AZ, such as product specifications in it
        :type ProductSet: list of ProductConf
        :param OldZoneId: AZ ID, such as 100003
        :type OldZoneId: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.IsSaleout = None
        self.IsDefault = None
        self.NetWorkType = None
        self.ProductSet = None
        self.OldZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.IsSaleout = params.get("IsSaleout")
        self.IsDefault = params.get("IsDefault")
        self.NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self.ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self.ProductSet.append(obj)
        self.OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        