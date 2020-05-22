# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CosBackup(AbstractModel):
    """Auto-backup to COS for ES

    """

    def __init__(self):
        """
        :param IsAutoBackup: Whether to enable auto-backup to COS
        :type IsAutoBackup: bool
        :param BackupTime: Auto-backup time (accurate down to the hour), such as "22:00"
        :type BackupTime: str
        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        """
        :param Zone: Availability Zone
        :type Zone: str
        :param EsVersion: Instance version ("5.6.4", "6.4.3", "6.8.2", or "7.5.1")
        :type EsVersion: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Password: Access password, which must contain 8 to 16 characters, and include at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2–50)
        :type NodeNum: int
        :param ChargeType: Billing mode <li>POSTPAID_BY_HOUR: Pay-as-you-go hourly </li>Default value: POSTPAID_BY_HOUR
        :type ChargeType: str
        :param ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param DiskType: This parameter has been disused. Please use `NodeInfoList`
Node storage type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: premium cloud storage </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Node disk size in GB
        :type DiskSize: int
        :param TimeUnit: This parameter is not used on the global website
        :type TimeUnit: str
        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param EnableDedicatedMaster: This parameter has been disused. Please use `NodeInfoList`
Whether to create a dedicated master node <li>true: yes </li><li>false: no </li>Default value: false
        :type EnableDedicatedMaster: bool
        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated master nodes (only 3 and 5 are supported. This value must be passed in if `EnableDedicatedMaster` is `true`)
        :type MasterNodeNum: int
        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated master node type, which must be passed in if `EnableDedicatedMaster` is `true` <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated master node disk size in GB, which is optional. If passed in, it can only be 50 and cannot be customized currently
        :type MasterNodeDiskSize: int
        :param ClusterNameInConf: ClusterName in the cluster configuration file, which is the instance ID by default and currently cannot be customized
        :type ClusterNameInConf: str
        :param DeployMode: Cluster deployment mode <li>0: single-AZ deployment </li><li>1: multi-AZ deployment </li>Default value: 0
        :type DeployMode: int
        :param MultiZoneInfo: Details of AZs in multi-AZ deployment mode (which is required when DeployMode is 1)
        :type MultiZoneInfo: list of ZoneDetail
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param NodeInfoList: Node information list, which is used to describe the specification information of various types of nodes in the cluster, such as node type, node quantity, node specification, disk type, and disk size
        :type NodeInfoList: list of NodeInfo
        :param TagList: Node tag information list
        :type TagList: list of TagInfo
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        """
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


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param LogType: Log type. Default value: 1
<li>1: master log</li>
<li>2: search slow log</li>
<li>3: index slow log</li>
<li>4: GC log</li>
        :type LogType: int
        :param SearchKey: Search keyword, which supports LUCENE syntax, such as `level:WARN`, `ip:1.1.1.1`, and `message:test-index`
        :type SearchKey: str
        :param StartTime: Log start time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type StartTime: str
        :param EndTime: Log end time in the format of YYYY-MM-DD HH:MM:SS, such as 2019-01-22 20:15:53
        :type EndTime: str
        :param Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 100. Maximum value: 100
        :type Limit: int
        :param OrderByType: Time sorting order. Default value: 0
<li>0: descending</li>
<li>1: ascending</li>
        :type OrderByType: int
        """
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


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned logs
        :type TotalCount: int
        :param InstanceLogList: Log details list
        :type InstanceLogList: list of InstanceLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param StartTime: Start time, such as "2019-03-07 16:30:39"
        :type StartTime: str
        :param EndTime: End time, such as "2019-03-30 20:18:03"
        :type EndTime: str
        :param Offset: Pagination start value
        :type Offset: int
        :param Limit: Number of entries per page
        :type Limit: int
        """
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


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of operation records
        :type TotalCount: int
        :param Operations: Operation history
        :type Operations: list of Operation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Zone: AZ of the cluster instance. If this is not passed in, all AZs are used by default
        :type Zone: str
        :param InstanceIds: List of cluster instance IDs
        :type InstanceIds: list of str
        :param InstanceNames: List of cluster instance names
        :type InstanceNames: list of str
        :param Offset: Pagination start value. Default value: 0
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param OrderByKey: Sort by field <li>1: instance ID </li><li>2: instance name </li><li>3: AZ </li><li>4: creation time </li>If `orderKey` is not passed in, sort by creation time in descending order
        :type OrderByKey: int
        :param OrderByType: Sorting order <li>0: ascending </li><li>1: descending </li>If orderByKey is passed in but orderByType is not, ascending order is used by default
        :type OrderByType: int
        :param TagList: Node tag information list
        :type TagList: list of TagInfo
        :param IpList: VPC VIP list
        :type IpList: list of str
        """
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


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned instances
        :type TotalCount: int
        :param InstanceList: List of instance details
        :type InstanceList: list of InstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Key: Dictionary key value
        :type Key: str
        :param Name: Dictionary name
        :type Name: str
        :param Size: Dictionary size in B
        :type Size: int
        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")


class EsAcl(AbstractModel):
    """ES cluster configuration item

    """

    def __init__(self):
        """
        :param BlackIpList: Kibana access blacklist
        :type BlackIpList: list of str
        :param WhiteIpList: Kibana access whitelist
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")


class EsDictionaryInfo(AbstractModel):
    """ES IK dictionary information

    """

    def __init__(self):
        """
        :param MainDict: List of non-stop words
        :type MainDict: list of DictInfo
        :param Stopwords: List of stop words
        :type Stopwords: list of DictInfo
        """
        self.MainDict = None
        self.Stopwords = None


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


class EsPublicAcl(AbstractModel):
    """Public network ACL information of ES

    """

    def __init__(self):
        """
        :param BlackIpList: Access blacklist
        :type BlackIpList: list of str
        :param WhiteIpList: Access whitelist
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Region: Region
        :type Region: str
        :param Zone: Availability Zone
        :type Zone: str
        :param AppId: User ID
        :type AppId: int
        :param Uin: User UIN
        :type Uin: str
        :param VpcUid: UID of the VPC where the instance resides
        :type VpcUid: str
        :param SubnetUid: UID of the subnet where the instance resides
        :type SubnetUid: str
        :param Status: Instance status. 0: processing; 1: normal; -1: stopped; -2: terminating; -3: terminated
        :type Status: int
        :param ChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
        :type ChargeType: str
        :param ChargePeriod: This parameter is not used on the global website
        :type ChargePeriod: int
        :param RenewFlag: This parameter is not used on the global website
        :type RenewFlag: str
        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param CpuNum: Number of CPU cores of the node
        :type CpuNum: int
        :param MemSize: Node memory size in GB
        :type MemSize: int
        :param DiskType: Node disk type
        :type DiskType: str
        :param DiskSize: Node disk size in GB
        :type DiskSize: int
        :param EsDomain: ES domain name
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES port
        :type EsPort: int
        :param KibanaUrl: Kibana access URL
        :type KibanaUrl: str
        :param EsVersion: ES version number
        :type EsVersion: str
        :param EsConfig: ES configuration item
        :type EsConfig: str
        :param EsAcl: Kibana access control configuration
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param CreateTime: Instance creation time
        :type CreateTime: str
        :param UpdateTime: Last modified time of the instance
        :type UpdateTime: str
        :param Deadline: This parameter is not used on the global website
        :type Deadline: str
        :param InstanceType: Instance type (instance type identifier, which can be only 1 or 2 currently)
        :type InstanceType: int
        :param IkConfig: IK analyzer configuration
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param MasterNodeInfo: Dedicated master node configuration
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param CosBackup: Auto-backup to COS configuration
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param AllowCosBackup: Whether to allow auto-backup to COS
        :type AllowCosBackup: bool
        :param TagList: List of tags owned by the instance
        :type TagList: list of TagInfo
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param EnableHotWarmMode: Whether it is a hot/warm cluster <li>true: yes </li><li>false: no</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type EnableHotWarmMode: bool
        :param WarmNodeType: Warm node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmNodeType: str
        :param WarmNodeNum: Number of warm nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmNodeNum: int
        :param WarmCpuNum: Number of warm node CPU cores
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmCpuNum: int
        :param WarmMemSize: Warm node memory size in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmMemSize: int
        :param WarmDiskType: Warm node disk type
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmDiskType: str
        :param WarmDiskSize: Warm node disk size in GB
Note: This field may return null, indicating that no valid values can be obtained.
        :type WarmDiskSize: int
        :param NodeInfoList: Cluster node information list
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeInfoList: list of NodeInfo
        :param EsPublicUrl: ES public IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsPublicUrl: str
        :param MultiZoneInfo: Multi-AZ network information
Note: This field may return null, indicating that no valid values can be obtained.
        :type MultiZoneInfo: list of ZoneDetail
        :param DeployMode: Deployment mode <li>0: single-AZ </li><li>1: multi-AZ</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployMode: int
        :param PublicAccess: ES public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicAccess: str
        :param EsPublicAcl: ES public access control configuration
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param KibanaPrivateUrl: Kibana private IP address
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateUrl: str
        :param KibanaPublicAccess: Kibana public access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: Kibana private access status <li>OPEN: enabled </li><li>CLOSE: disabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type KibanaPrivateAccess: str
        :param SecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: int
        """
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


class InstanceLog(AbstractModel):
    """ES cluster log details

    """

    def __init__(self):
        """
        :param Time: Log time
        :type Time: str
        :param Level: Log level
        :type Level: str
        :param Ip: Cluster node IP
        :type Ip: str
        :param Message: Log content
        :type Message: str
        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")


class KeyValue(AbstractModel):
    """`OperationDetail` uses an array of this structure to describe the old and new configuration information

    """

    def __init__(self):
        """
        :param Key: Key
        :type Key: str
        :param Value: Value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class LocalDiskInfo(AbstractModel):
    """Local disk information of node

    """

    def __init__(self):
        """
        :param LocalDiskType: Local disk type <li>LOCAL_SATA: big data </li><li>NVME_SSD: high IO</li>
        :type LocalDiskType: str
        :param LocalDiskSize: Size of a single local disk
        :type LocalDiskSize: int
        :param LocalDiskCount: Number of local disks
        :type LocalDiskCount: int
        """
        self.LocalDiskType = None
        self.LocalDiskSize = None
        self.LocalDiskCount = None


    def _deserialize(self, params):
        self.LocalDiskType = params.get("LocalDiskType")
        self.LocalDiskSize = params.get("LocalDiskSize")
        self.LocalDiskCount = params.get("LocalDiskCount")


class MasterNodeInfo(AbstractModel):
    """Information of the dedicated master node in an instance

    """

    def __init__(self):
        """
        :param EnableDedicatedMaster: Whether to enable the dedicated master node
        :type EnableDedicatedMaster: bool
        :param MasterNodeType: Dedicated master node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeNum: Number of dedicated master nodes
        :type MasterNodeNum: int
        :param MasterNodeCpuNum: Number of CPU cores of the dedicated master node
        :type MasterNodeCpuNum: int
        :param MasterNodeMemSize: Memory size of the dedicated master node in GB
        :type MasterNodeMemSize: int
        :param MasterNodeDiskSize: Disk size of the dedicated master node in GB
        :type MasterNodeDiskSize: int
        :param MasterNodeDiskType: Disk type of the dedicated master node
        :type MasterNodeDiskType: str
        """
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


class NodeInfo(AbstractModel):
    """Specification information of a node type in the cluster (such as hot data node, warm data node, or dedicated master node), including node type, number of nodes, node specification, disk type, and disk size. If `Type` is not specified, it will be a hot data node by default; if the node is a master node, then the `DiskType` and `DiskSize` parameters will be ignored (as a master node has no data disks)

    """

    def __init__(self):
        """
        :param NodeNum: Number of nodes
        :type NodeNum: int
        :param NodeType: Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param Type: Node type <li>hotData: hot data node</li>
<li>warmData: warm data node</li>
<li>dedicatedMaster: dedicated master node</li>
Default value: hotData
        :type Type: str
        :param DiskType: Node disk type <li>CLOUD_SSD: SSD cloud storage </li><li>CLOUD_PREMIUM: Premium cloud disk </li>Default value: CLOUD_SSD
        :type DiskType: str
        :param DiskSize: Node disk size in GB
        :type DiskSize: int
        :param LocalDiskInfo: Local disk information
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param DiskCount: Number of node disks
        :type DiskCount: int
        """
        self.NodeNum = None
        self.NodeType = None
        self.Type = None
        self.DiskType = None
        self.DiskSize = None
        self.LocalDiskInfo = None
        self.DiskCount = None


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


class Operation(AbstractModel):
    """ES cluster operation details

    """

    def __init__(self):
        """
        :param Id: Unique operation ID
        :type Id: int
        :param StartTime: Operation start time
        :type StartTime: str
        :param Type: Operation type
        :type Type: str
        :param Detail: Operation details
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param Result: Operation result
        :type Result: str
        :param Tasks: Workflow task information
        :type Tasks: list of TaskDetail
        :param Progress: Operation progress
        :type Progress: float
        """
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


class OperationDetail(AbstractModel):
    """Operation details

    """

    def __init__(self):
        """
        :param OldInfo: Original instance configuration information
        :type OldInfo: list of KeyValue
        :param NewInfo: Updated instance configuration information
        :type NewInfo: list of KeyValue
        """
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


class RestartInstanceRequest(AbstractModel):
    """RestartInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ForceRestart: Whether to force restart <li>true: Yes </li><li>false: No </li>Default value: false
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")


class RestartInstanceResponse(AbstractModel):
    """RestartInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """Information of subtask in workflow task in the instance operation history (such as each check item in a upgrade check task)

    """

    def __init__(self):
        """
        :param Name: Subtask name
        :type Name: str
        :param Result: Subtask result
        :type Result: bool
        :param ErrMsg: Subtask error message
        :type ErrMsg: str
        :param Type: Subtask type
        :type Type: str
        :param Status: Subtask status. 0: processing, 1: succeeded, -1: failed
        :type Status: int
        :param FailedIndices: Name of the index for which the check for upgrade failed
        :type FailedIndices: list of str
        :param FinishTime: Subtask end time
        :type FinishTime: str
        :param Level: Subtask level. 1: warning, 2: failed
        :type Level: int
        """
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


class TagInfo(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        """
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TaskDetail(AbstractModel):
    """Information of workflow task in instance operation history

    """

    def __init__(self):
        """
        :param Name: Task name
        :type Name: str
        :param Progress: Task progress
        :type Progress: float
        :param FinishTime: Task completion time
        :type FinishTime: str
        :param SubTasks: Subtask
        :type SubTasks: list of SubTaskDetail
        """
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


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name, which can contain 1 to 50 English letters, Chinese characters, digits, dashes (-), or underscores (_)
        :type InstanceName: str
        :param NodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of nodes (2–50)
        :type NodeNum: int
        :param EsConfig: Configuration item (JSON string). Only the following items are supported currently: <li>action.destructive_requires_name</li><li>indices.fielddata.cache.size</li><li>indices.query.bool.max_clause_count</li>
        :type EsConfig: str
        :param Password: Password of the default user “elastic“, which must contain 8 to 16 characters, including at least two of the following three types of characters: [a-z,A-Z], [0-9] and [-!@#$%&^*+=_:;,.?]
        :type Password: str
        :param EsAcl: Access control list
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param DiskSize: This parameter has been disused. Please use `NodeInfoList`
Disk size in GB
        :type DiskSize: int
        :param NodeType: This parameter has been disused. Please use `NodeInfoList`
Node specification <li>ES.S1.SMALL2: 1-core 2 GB </li><li>ES.S1.MEDIUM4: 2-core 4 GB </li><li>ES.S1.MEDIUM8: 2-core 8 GB </li><li>ES.S1.LARGE16: 4-core 16 GB </li><li>ES.S1.2XLARGE32: 8-core 32 GB </li><li>ES.S1.4XLARGE32: 16-core 32 GB </li><li>ES.S1.4XLARGE64: 16-core 64 GB </li>
        :type NodeType: str
        :param MasterNodeNum: This parameter has been disused. Please use `NodeInfoList`
Number of dedicated master nodes (only 3 and 5 are supported)
        :type MasterNodeNum: int
        :param MasterNodeType: This parameter has been disused. Please use `NodeInfoList`
Dedicated master node specification <li>ES.S1.SMALL2: 1-core 2 GB</li><li>ES.S1.MEDIUM4: 2-core 4 GB</li><li>ES.S1.MEDIUM8: 2-core 8 GB</li><li>ES.S1.LARGE16: 4-core 16 GB</li><li>ES.S1.2XLARGE32: 8-core 32 GB</li><li>ES.S1.4XLARGE32: 16-core 32 GB</li><li>ES.S1.4XLARGE64: 16-core 64 GB</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: This parameter has been disused. Please use `NodeInfoList`
Dedicated master node disk size in GB. This is 50 GB by default and currently cannot be customized
        :type MasterNodeDiskSize: int
        :param ForceRestart: Whether to force restart during configuration update <li>true: Yes </li><li>false: No </li>This needs to be set only for EsConfig. Default value: false
        :type ForceRestart: bool
        :param CosBackup: Auto-backup to COS
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param NodeInfoList: Node information list. You can pass in only the nodes to be updated and their corresponding specification information. Supported operations include: <li>modifying the number of nodes in the same type </li><li>modifying the specification and disk size of nodes in the same type </li><li>adding a node type (you must also specify the node type, quantity, specification, disk, etc.) </li>The above operations can only be performed one at a time, and the disk type cannot be modified
        :type NodeInfoList: list of NodeInfo
        :param PublicAccess: Public network access status
        :type PublicAccess: str
        :param EsPublicAcl: Public network ACL
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param KibanaPublicAccess: Public network access status of Kibana
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: Private network access status of Kibana
        :type KibanaPrivateAccess: str
        :param BasicSecurityType: Enables or disables user authentication for ES Basic Edition v6.8 and above
        :type BasicSecurityType: int
        :param KibanaPrivatePort: Kibana private port
        :type KibanaPrivatePort: int
        """
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


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param EsVersion: Target ES version. Valid values: 6.4.3, 6.8.2, 7.5.1
        :type EsVersion: str
        :param CheckOnly: Whether to check for upgrade only. Default value: false
        :type CheckOnly: bool
        :param LicenseType: Target X-Pack edition: <li>OSS: Open-source Edition </li><li>basic: Basic Edition </li>Currently only used for v5.6.4 to v6.x upgrade. Default value: basic
        :type LicenseType: str
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        """
        self.InstanceId = None
        self.EsVersion = None
        self.CheckOnly = None
        self.LicenseType = None
        self.BasicSecurityType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EsVersion = params.get("EsVersion")
        self.CheckOnly = params.get("CheckOnly")
        self.LicenseType = params.get("LicenseType")
        self.BasicSecurityType = params.get("BasicSecurityType")


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param LicenseType: License type <li>oss: Open Source Edition </li><li>basic: Basic Edition </li><li>platinum: Platinum Edition </li>Default value: Platinum
        :type LicenseType: str
        :param AutoVoucher: Whether to automatically use vouchers <li>0: No </li><li>1: Yes </li>Default value: 0
        :type AutoVoucher: int
        :param VoucherIds: List of voucher IDs (only one voucher can be specified at a time currently)
        :type VoucherIds: list of str
        :param BasicSecurityType: Whether to enable X-Pack security authentication in Basic Edition 6.8 (and above) <li>1: disabled </li><li>2: enabled</li>
        :type BasicSecurityType: int
        :param ForceRestart: Whether to force restart <li>true: yes </li><li>false: no </li>Default value: false
        :type ForceRestart: bool
        """
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


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ZoneDetail(AbstractModel):
    """Details of AZs in multi-AZ deployment mode

    """

    def __init__(self):
        """
        :param Zone: AZ
        :type Zone: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")