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


class CosBackup(AbstractModel):
    """Auto-backup to COS for ES

    """

    def __init__(self):
        """
        :param IsAutoBackup: Whether to enable auto-backup to COS\n        :type IsAutoBackup: bool\n        :param BackupTime: Auto-backup time (accurate down to the hour), such as "22:00"\n        :type BackupTime: str\n        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        """
        :param Zone: Availability Zone\n        :type Zone: str\n        :param EsVersion: Instance version. Valid values: `5.6.4`, `6.4.3`, `6.8.2`, `7.5.1`, `7.10.1`\n        :type EsVersion: str\n        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param Password: Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]\n        :type Password: str\n        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)\n        :type InstanceName: str\n        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)\n        :type NodeNum: int\n        :param ChargeType: Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR\n        :type ChargeType: str\n        :param ChargePeriod: This parameter is not used on the global website\n        :type ChargePeriod: int\n        :param RenewFlag: This parameter is not used on the global website\n        :type RenewFlag: str\n        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>\n        :type NodeType: str\n        :param DiskType: This parameter has been disused. Please use `NodeInfoList`
Node storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD\n        :type DiskType: str\n        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Node disk size in GB\n        :type DiskSize: int\n        :param TimeUnit: This parameter is not used on the global website\n        :type TimeUnit: str\n        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0\n        :type AutoVoucher: int\n        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)\n        :type VoucherIds: list of str\n        :param EnableDedicatedMaster: This parameter has been disused. Please use `NodeInfoList`
Whether to create a dedicated primary node <li>true: yes </li><li>false: no </li>Default value: false\n        :type EnableDedicatedMaster: bool\n        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)\n        :type MasterNodeNum: int\n        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>\n        :type MasterNodeType: str\n        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently\n        :type MasterNodeDiskSize: int\n        :param ClusterNameInConf: ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized\n        :type ClusterNameInConf: str\n        :param DeployMode: Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0\n        :type DeployMode: int\n        :param MultiZoneInfo: Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)\n        :type MultiZoneInfo: list of ZoneDetail\n        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum\n        :type LicenseType: str\n        :param NodeInfoList: Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size\n        :type NodeInfoList: list of NodeInfo\n        :param TagList: Node tag information list\n        :type TagList: list of TagInfo\n        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>\n        :type BasicSecurityType: int\n        :param SceneType: Scenario template type. 0: not enabled; 1: general; 2: log; 3: search\n        :type SceneType: int\n        :param WebNodeTypeInfo: Visual node configuration\n        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`\n        """
        self.Zone = None
        self.EsVersion = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.NodeNum = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None
        self.DeployMode = None
        self.MultiZoneInfo = None
        self.LicenseType = None
        self.NodeInfoList = None
        self.TagList = None
        self.BasicSecurityType = None
        self.SceneType = None
        self.WebNodeTypeInfo = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.EsVersion = params.get("EsVersion")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")
        self.DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Cluster instance ID\n        :type InstanceId: str\n        :param LogType: Log type. Default value: 1
<li>1: primary log</li>
<li>2: search slow log</li>
<li>3: index slow log</li>
<li>4: GC log</li>\n        :type LogType: int\n        :param SearchKey: Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`\n        :type SearchKey: str\n        :param StartTime: Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53\n        :type StartTime: str\n        :param EndTime: Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53\n        :type EndTime: str\n        :param Offset: Pagination start value. Default value: 0\n        :type Offset: int\n        :param Limit: Number of entries per page. Default value: 100. Maximum value: 100\n        :type Limit: int\n        :param OrderByType: Time sorting order. Default value: 0
<li>0: descending</li>
<li>1: ascending</li>\n        :type OrderByType: int\n        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned logs\n        :type TotalCount: int\n        :param InstanceLogList: Log details list\n        :type InstanceLogList: list of InstanceLog\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Cluster instance ID\n        :type InstanceId: str\n        :param StartTime: Start time, such as "2019-03-07 16:30:39"\n        :type StartTime: str\n        :param EndTime: End time, such as "2019-03-30 20:18:03"\n        :type EndTime: str\n        :param Offset: Pagination start value\n        :type Offset: int\n        :param Limit: Number of entries per page\n        :type Limit: int\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of operation records\n        :type TotalCount: int\n        :param Operations: Operation history\n        :type Operations: list of Operation\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
        :param Zone: AZ of the cluster instance. If this is not passed in, all AZs are used by default\n        :type Zone: str\n        :param InstanceIds: List of cluster instance IDs\n        :type InstanceIds: list of str\n        :param InstanceNames: List of cluster instance names\n        :type InstanceNames: list of str\n        :param Offset: Pagination start value. Default value: 0\n        :type Offset: int\n        :param Limit: Number of entries per page. Default value: 20\n        :type Limit: int\n        :param OrderByKey: Sort by field <li>1: instance ID </li><li>2: instance name </li><li>3: AZ </li><li>4: creation time </li>If `orderKey` is not passed in, sort by creation time in descending order\n        :type OrderByKey: int\n        :param OrderByType: Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default\n        :type OrderByType: int\n        :param TagList: Node tag information list\n        :type TagList: list of TagInfo\n        :param IpList: VPC VIP list\n        :type IpList: list of str\n        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None
        self.TagList = None
        self.IpList = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned instances\n        :type TotalCount: int\n        :param InstanceList: List of instance details\n        :type InstanceList: list of InstanceInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """Information of the IK plugin dictionary

    """

    def __init__(self):
        """
        :param Key: Dictionary key value\n        :type Key: str\n        :param Name: Dictionary name\n        :type Name: str\n        :param Size: Dictionary size in B\n        :type Size: int\n        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    """ES cluster configuration item

    """

    def __init__(self):
        """
        :param BlackIpList: Kibana access blocklist\n        :type BlackIpList: list of str\n        :param WhiteIpList: Kibana access allowlist\n        :type WhiteIpList: list of str\n        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    """ES dictionary information

    """

    def __init__(self):
        """
        :param MainDict: List of non-stop words\n        :type MainDict: list of DictInfo\n        :param Stopwords: List of stop words\n        :type Stopwords: list of DictInfo\n        :param QQDict: QQ dictionary list\n        :type QQDict: list of DictInfo\n        :param Synonym: Synonym dictionary list\n        :type Synonym: list of DictInfo\n        :param UpdateType: Update dictionary type\n        :type UpdateType: str\n        """
        self.MainDict = None
        self.Stopwords = None
        self.QQDict = None
        self.Synonym = None
        self.UpdateType = None


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self.MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self.Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Stopwords.append(obj)
        if params.get("QQDict") is not None:
            self.QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.QQDict.append(obj)
        if params.get("Synonym") is not None:
            self.Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Synonym.append(obj)
        self.UpdateType = params.get("UpdateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    """Public network ACL information of ES

    """

    def __init__(self):
        """
        :param BlackIpList: Access blocklist\n        :type BlackIpList: list of str\n        :param WhiteIpList: Access allowlist\n        :type WhiteIpList: list of str\n        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesRequest(AbstractModel):
    """GetRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    """GetRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        """
        :param TargetNodeTypes: A list of node types used to receive requests.\n        :type TargetNodeTypes: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TargetNodeTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param Region: Region\n        :type Region: str\n        :param Zone: Availability Zone\n        :type Zone: str\n        :param AppId: User ID\n        :type AppId: int\n        :param Uin: User UIN\n        :type Uin: str\n        :param VpcUid: UID of the VPC where the instance resides\n        :type VpcUid: str\n        :param SubnetUid: UID of the subnet where the instance resides\n        :type SubnetUid: str\n        :param Status: Instance status. 0: processing; 1: normal; -1: stopped; -2: terminating; -3: terminated\n        :type Status: int\n        :param ChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)\n        :type ChargeType: str\n        :param ChargePeriod: This parameter is not used on the global website\n        :type ChargePeriod: int\n        :param RenewFlag: This parameter is not used on the global website\n        :type RenewFlag: str\n        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>\n        :type NodeType: str\n        :param NodeNum: Number of nodes\n        :type NodeNum: int\n        :param CpuNum: Number of CPU cores of the node\n        :type CpuNum: int\n        :param MemSize: Node memory size in GB\n        :type MemSize: int\n        :param DiskType: Node disk type\n        :type DiskType: str\n        :param DiskSize: Node disk size in GB\n        :type DiskSize: int\n        :param EsDomain: ES domain name\n        :type EsDomain: str\n        :param EsVip: ES VIP\n        :type EsVip: str\n        :param EsPort: ES port\n        :type EsPort: int\n        :param KibanaUrl: Kibana access URL\n        :type KibanaUrl: str\n        :param EsVersion: ES version number\n        :type EsVersion: str\n        :param EsConfig: ES configuration item\n        :type EsConfig: str\n        :param EsAcl: Kibana access control configuration\n        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param CreateTime: Instance creation time\n        :type CreateTime: str\n        :param UpdateTime: Last modified time of the instance\n        :type UpdateTime: str\n        :param Deadline: This parameter is not used on the global website\n        :type Deadline: str\n        :param InstanceType: Instance type (instance type identifier, which can be only 1 or 2 currently)\n        :type InstanceType: int\n        :param IkConfig: IK analyzer configuration\n        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`\n        :param MasterNodeInfo: Dedicated primary node configuration\n        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`\n        :param CosBackup: Auto-backup to COS configuration\n        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`\n        :param AllowCosBackup: Whether to allow auto-backup to COS\n        :type AllowCosBackup: bool\n        :param TagList: List of tags owned by the instance\n        :type TagList: list of TagInfo\n        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum\n        :type LicenseType: str\n        :param EnableHotWarmMode: Whether it is a hot/warm cluster <li>true: yes </li><li>false: no</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EnableHotWarmMode: bool\n        :param WarmNodeType: Warm node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmNodeType: str\n        :param WarmNodeNum: Number of warm nodes
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmNodeNum: int\n        :param WarmCpuNum: Number of warm node CPU cores
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmCpuNum: int\n        :param WarmMemSize: Warm node memory size in GB
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmMemSize: int\n        :param WarmDiskType: Warm node disk type
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmDiskType: str\n        :param WarmDiskSize: Warm node disk size in GB
Note: This field may return null, indicating that no valid values can be obtained.\n        :type WarmDiskSize: int\n        :param NodeInfoList: Cluster node information list
Note: This field may return null, indicating that no valid values can be obtained.\n        :type NodeInfoList: list of NodeInfo\n        :param EsPublicUrl: ES public IP address
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EsPublicUrl: str\n        :param MultiZoneInfo: Multi-AZ network information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type MultiZoneInfo: list of ZoneDetail\n        :param DeployMode: Deployment mode <li>0: single-AZ </li><li>1: multi-AZ</li>
Note: This field may return null, indicating that no valid values can be obtained.\n        :type DeployMode: int\n        :param PublicAccess: ES public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PublicAccess: str\n        :param EsPublicAcl: ES public access control configuration\n        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param KibanaPrivateUrl: Kibana private IP address
Note: This field may return null, indicating that no valid values can be obtained.\n        :type KibanaPrivateUrl: str\n        :param KibanaPublicAccess: Kibana public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.\n        :type KibanaPublicAccess: str\n        :param KibanaPrivateAccess: Kibana private access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.\n        :type KibanaPrivateAccess: str\n        :param SecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
Note: This field may return null, indicating that no valid values can be obtained.\n        :type SecurityType: int\n        :param SceneType: Scenario template type. 0: not enabled; 1: general scenario; 2: log scenario; 3: search scenario
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SceneType: int\n        :param KibanaConfig: Kibana configuration item.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type KibanaConfig: str\n        :param KibanaNodeInfo: Kibana node information
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.InstanceType = None
        self.IkConfig = None
        self.MasterNodeInfo = None
        self.CosBackup = None
        self.AllowCosBackup = None
        self.TagList = None
        self.LicenseType = None
        self.EnableHotWarmMode = None
        self.WarmNodeType = None
        self.WarmNodeNum = None
        self.WarmCpuNum = None
        self.WarmMemSize = None
        self.WarmDiskType = None
        self.WarmDiskSize = None
        self.NodeInfoList = None
        self.EsPublicUrl = None
        self.MultiZoneInfo = None
        self.DeployMode = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPrivateUrl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.SecurityType = None
        self.SceneType = None
        self.KibanaConfig = None
        self.KibanaNodeInfo = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        self.InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self.IkConfig = EsDictionaryInfo()
            self.IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self.MasterNodeInfo = MasterNodeInfo()
            self.MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        self.AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.LicenseType = params.get("LicenseType")
        self.EnableHotWarmMode = params.get("EnableHotWarmMode")
        self.WarmNodeType = params.get("WarmNodeType")
        self.WarmNodeNum = params.get("WarmNodeNum")
        self.WarmCpuNum = params.get("WarmCpuNum")
        self.WarmMemSize = params.get("WarmMemSize")
        self.WarmDiskType = params.get("WarmDiskType")
        self.WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.SecurityType = params.get("SecurityType")
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self.KibanaNodeInfo = KibanaNodeInfo()
            self.KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """ES cluster log details

    """

    def __init__(self):
        """
        :param Time: Log time\n        :type Time: str\n        :param Level: Log level\n        :type Level: str\n        :param Ip: Cluster node IP\n        :type Ip: str\n        :param Message: Log content\n        :type Message: str\n        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """`OperationDetail` uses an array of this structure to describe the old and new configuration information

    """

    def __init__(self):
        """
        :param Key: Key\n        :type Key: str\n        :param Value: Value\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaNodeInfo(AbstractModel):
    """Kibana node information

    """

    def __init__(self):
        """
        :param KibanaNodeType: Kibana node specification\n        :type KibanaNodeType: str\n        :param KibanaNodeNum: Number of Kibana nodes\n        :type KibanaNodeNum: int\n        :param KibanaNodeCpuNum: Number of Kibana node's CPUs\n        :type KibanaNodeCpuNum: int\n        :param KibanaNodeMemSize: Kibana node's memory in GB\n        :type KibanaNodeMemSize: int\n        :param KibanaNodeDiskType: Kibana node's disk type\n        :type KibanaNodeDiskType: str\n        :param KibanaNodeDiskSize: Kibana node's disk size\n        :type KibanaNodeDiskSize: int\n        """
        self.KibanaNodeType = None
        self.KibanaNodeNum = None
        self.KibanaNodeCpuNum = None
        self.KibanaNodeMemSize = None
        self.KibanaNodeDiskType = None
        self.KibanaNodeDiskSize = None


    def _deserialize(self, params):
        self.KibanaNodeType = params.get("KibanaNodeType")
        self.KibanaNodeNum = params.get("KibanaNodeNum")
        self.KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self.KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self.KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self.KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    """Local disk information of node

    """

    def __init__(self):
        """
        :param LocalDiskType: Local disk type <li>LOCAL_SATA: big data </li><li>NVME_SSD: high IO</li>\n        :type LocalDiskType: str\n        :param LocalDiskSize: Size of a single local disk\n        :type LocalDiskSize: int\n        :param LocalDiskCount: Number of local disks\n        :type LocalDiskCount: int\n        """
        self.LocalDiskType = None
        self.LocalDiskSize = None
        self.LocalDiskCount = None


    def _deserialize(self, params):
        self.LocalDiskType = params.get("LocalDiskType")
        self.LocalDiskSize = params.get("LocalDiskSize")
        self.LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    """Information of the dedicated primary node in an instance

    """

    def __init__(self):
        """
        :param EnableDedicatedMaster: Whether to enable the dedicated primary node\n        :type EnableDedicatedMaster: bool\n        :param MasterNodeType: Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>\n        :type MasterNodeType: str\n        :param MasterNodeNum: Number of dedicated primary nodes\n        :type MasterNodeNum: int\n        :param MasterNodeCpuNum: Number of CPU cores of the dedicated primary node\n        :type MasterNodeCpuNum: int\n        :param MasterNodeMemSize: Memory size of the dedicated primary node in GB\n        :type MasterNodeMemSize: int\n        :param MasterNodeDiskSize: Disk size of the dedicated primary node in GB\n        :type MasterNodeDiskSize: int\n        :param MasterNodeDiskType: Disk type of the dedicated primary node\n        :type MasterNodeDiskType: str\n        """
        self.EnableDedicatedMaster = None
        self.MasterNodeType = None
        self.MasterNodeNum = None
        self.MasterNodeCpuNum = None
        self.MasterNodeMemSize = None
        self.MasterNodeDiskSize = None
        self.MasterNodeDiskType = None


    def _deserialize(self, params):
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self.MasterNodeMemSize = params.get("MasterNodeMemSize")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.MasterNodeDiskType = params.get("MasterNodeDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """Specification information of a node type in the cluster (such as hot data node, warm data node, or dedicated primary node), including node type, number of nodes, node specification, disk type, and disk size. If `Type` is not specified, it will be a hot data node by default; if the node is a primary node, then the `DiskType` and `DiskSize` parameters will be ignored (as a primary node has no data disks)

    """

    def __init__(self):
        """
        :param NodeNum: Number of nodes\n        :type NodeNum: int\n        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>\n        :type NodeType: str\n        :param Type: Node type<li>`hotData`: hot data node</li>
<li>`warmData`: warm data node</li>
<li>`dedicatedMaster`: dedicated master node</li>
<li>`kibana`: Kibana node</li>
Default value: `hotData`\n        :type Type: str\n        :param DiskType: Node disk type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD\n        :type DiskType: str\n        :param DiskSize: Node disk size in GB\n        :type DiskSize: int\n        :param LocalDiskInfo: Local disk information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`\n        :param DiskCount: Number of node disks\n        :type DiskCount: int\n        :param DiskEncrypt: Whether to encrypt node disk. 0: no (default); 1: yes.\n        :type DiskEncrypt: int\n        """
        self.NodeNum = None
        self.NodeType = None
        self.Type = None
        self.DiskType = None
        self.DiskSize = None
        self.LocalDiskInfo = None
        self.DiskCount = None
        self.DiskEncrypt = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        self.Type = params.get("Type")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self.LocalDiskInfo = LocalDiskInfo()
            self.LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self.DiskCount = params.get("DiskCount")
        self.DiskEncrypt = params.get("DiskEncrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    """ES cluster operation details

    """

    def __init__(self):
        """
        :param Id: Unique operation ID\n        :type Id: int\n        :param StartTime: Operation start time\n        :type StartTime: str\n        :param Type: Operation type\n        :type Type: str\n        :param Detail: Operation details\n        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`\n        :param Result: Operation result\n        :type Result: str\n        :param Tasks: Workflow task information\n        :type Tasks: list of TaskDetail\n        :param Progress: Operation progress\n        :type Progress: float\n        """
        self.Id = None
        self.StartTime = None
        self.Type = None
        self.Detail = None
        self.Result = None
        self.Tasks = None
        self.Progress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        if params.get("Detail") is not None:
            self.Detail = OperationDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.Result = params.get("Result")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    """Operation details

    """

    def __init__(self):
        """
        :param OldInfo: Original instance configuration information\n        :type OldInfo: list of KeyValue\n        :param NewInfo: Updated instance configuration information\n        :type NewInfo: list of KeyValue\n        """
        self.OldInfo = None
        self.NewInfo = None


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self.OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self.NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.NewInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ForceRestart: Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartKibanaRequest(AbstractModel):
    """RestartKibana request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ES instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartKibanaResponse(AbstractModel):
    """RestartKibana response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartNodesRequest(AbstractModel):
    """RestartNodes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Cluster instance ID\n        :type InstanceId: str\n        :param NodeNames: Node name list\n        :type NodeNames: list of str\n        :param ForceRestart: Whether to force restart\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.NodeNames = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeNames = params.get("NodeNames")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    """RestartNodes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """Information of subtask in workflow task in the instance operation history (such as each check item in a upgrade check task)

    """

    def __init__(self):
        """
        :param Name: Subtask name\n        :type Name: str\n        :param Result: Subtask result\n        :type Result: bool\n        :param ErrMsg: Subtask error message\n        :type ErrMsg: str\n        :param Type: Subtask type\n        :type Type: str\n        :param Status: Subtask status. 0: processing, 1: succeeded, -1: failed\n        :type Status: int\n        :param FailedIndices: Name of the index for which the check for upgrade failed\n        :type FailedIndices: list of str\n        :param FinishTime: Subtask end time\n        :type FinishTime: str\n        :param Level: Subtask level. 1: warning, 2: failed\n        :type Level: int\n        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None
        self.Type = None
        self.Status = None
        self.FailedIndices = None
        self.FinishTime = None
        self.Level = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.FailedIndices = params.get("FailedIndices")
        self.FinishTime = params.get("FinishTime")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """Information of workflow task in instance operation history

    """

    def __init__(self):
        """
        :param Name: Task name\n        :type Name: str\n        :param Progress: Task progress\n        :type Progress: float\n        :param FinishTime: Task completion time\n        :type FinishTime: str\n        :param SubTasks: Subtask\n        :type SubTasks: list of SubTaskDetail\n        """
        self.Name = None
        self.Progress = None
        self.FinishTime = None
        self.SubTasks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Progress = params.get("Progress")
        self.FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self.SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self.SubTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)\n        :type InstanceName: str\n        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2-50)\n        :type NodeNum: int\n        :param EsConfig: ES configuration item (JSON string)\n        :type EsConfig: str\n        :param Password: Password of the default user 'elastic', which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]\n        :type Password: str\n        :param EsAcl: Access control list\n        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Disk size in GB\n        :type DiskSize: int\n        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>\n        :type NodeType: str\n        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated primary nodes (only 3 and 5 are supported)\n        :type MasterNodeNum: int\n        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>\n        :type MasterNodeType: str\n        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated primary node disk size in GB. This is 50 GB by default and currently cannot be customized\n        :type MasterNodeDiskSize: int\n        :param ForceRestart: Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false\n        :type ForceRestart: bool\n        :param CosBackup: Auto-backup to COS\n        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`\n        :param NodeInfoList: Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified\n        :type NodeInfoList: list of NodeInfo\n        :param PublicAccess: Public network access status\n        :type PublicAccess: str\n        :param EsPublicAcl: Public network ACL\n        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`\n        :param KibanaPublicAccess: Public network access status of Kibana\n        :type KibanaPublicAccess: str\n        :param KibanaPrivateAccess: Private network access status of Kibana\n        :type KibanaPrivateAccess: str\n        :param BasicSecurityType: Enables or disables user authentication for ES Basic Edition v6.8 and above\n        :type BasicSecurityType: int\n        :param KibanaPrivatePort: Kibana private port\n        :type KibanaPrivatePort: int\n        :param ScaleType: 0: scaling in blue/green deployment mode without cluster restart (default); 1: scaling by unmounting disk with rolling cluster restart\n        :type ScaleType: int\n        :param MultiZoneInfo: Multi-AZ deployment\n        :type MultiZoneInfo: list of ZoneDetail\n        :param SceneType: Scenario template type. -1: not enabled; 1: general; 2: log; 3: search\n        :type SceneType: int\n        :param KibanaConfig: Kibana configuration item (JSON string)\n        :type KibanaConfig: str\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None
        self.DiskSize = None
        self.NodeType = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ForceRestart = None
        self.CosBackup = None
        self.NodeInfoList = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.BasicSecurityType = None
        self.KibanaPrivatePort = None
        self.ScaleType = None
        self.MultiZoneInfo = None
        self.SceneType = None
        self.KibanaConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.DiskSize = params.get("DiskSize")
        self.NodeType = params.get("NodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsPublicAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.KibanaPrivatePort = params.get("KibanaPrivatePort")
        self.ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    """UpdatePlugins request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstallPluginList: List of names of the plugins to be installed\n        :type InstallPluginList: list of str\n        :param RemovePluginList: List of names of the plugins to be uninstalled\n        :type RemovePluginList: list of str\n        :param ForceRestart: Whether to force restart\n        :type ForceRestart: bool\n        :param ForceUpdate: Whether to reinstall\n        :type ForceUpdate: bool\n        """
        self.InstanceId = None
        self.InstallPluginList = None
        self.RemovePluginList = None
        self.ForceRestart = None
        self.ForceUpdate = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstallPluginList = params.get("InstallPluginList")
        self.RemovePluginList = params.get("RemovePluginList")
        self.ForceRestart = params.get("ForceRestart")
        self.ForceUpdate = params.get("ForceUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    """UpdatePlugins response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    """UpdateRequestTargetNodeTypes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param TargetNodeTypes: A list of node types used to receive requests.\n        :type TargetNodeTypes: list of str\n        """
        self.InstanceId = None
        self.TargetNodeTypes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    """UpdateRequestTargetNodeTypes response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param EsVersion: Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1\n        :type EsVersion: str\n        :param CheckOnly: Whether to check for upgrade only. Default value: false\n        :type CheckOnly: bool\n        :param LicenseType: Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic\n        :type LicenseType: str\n        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>\n        :type BasicSecurityType: int\n        :param UpgradeMode: Upgrade mode. <li>scale: blue/green deployment</li><li>restart: rolling restart</li>Default value: scale\n        :type UpgradeMode: str\n        """
        self.InstanceId = None
        self.EsVersion = None
        self.CheckOnly = None
        self.LicenseType = None
        self.BasicSecurityType = None
        self.UpgradeMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EsVersion = params.get("EsVersion")
        self.CheckOnly = params.get("CheckOnly")
        self.LicenseType = params.get("LicenseType")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.UpgradeMode = params.get("UpgradeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum\n        :type LicenseType: str\n        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0\n        :type AutoVoucher: int\n        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)\n        :type VoucherIds: list of str\n        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>\n        :type BasicSecurityType: int\n        :param ForceRestart: Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.LicenseType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.BasicSecurityType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LicenseType = params.get("LicenseType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    """Visual node configuration

    """

    def __init__(self):
        """
        :param NodeNum: Number of visual nodes. The value is always `1`.\n        :type NodeNum: int\n        :param NodeType: Visual node specification\n        :type NodeType: str\n        """
        self.NodeNum = None
        self.NodeType = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    """Details of AZs in multi-AZ deployment mode

    """

    def __init__(self):
        """
        :param Zone: AZ\n        :type Zone: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        